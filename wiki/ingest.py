"""
ingest.py — The Ingest Pipeline for the Wiki Brain.

Flow:
  1. Read source from raw/
  2. Chunk if needed (Map-Reduce for large files)
  3. Summarize each chunk
  4. Extract entities from each chunk
  5. Merge entity extractions across chunks (dedup)
  6. Write/update wiki draft pages
  7. Run contradiction check against existing wiki pages
"""

import os
import json
import re
import yaml
from datetime import datetime, timezone
from typing import List, Optional

from . import llm_client
from . import chunker
from . import tools


# ── Load schema config ────────────────────────────────────────────────
_SCHEMA_PATH = os.path.join(tools.CONFIG_DIR, "wiki_schema.yaml")


def _load_schema() -> dict:
    with open(_SCHEMA_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _get_prompt(schema: dict, key: str) -> str:
    """Get a prompt template from the schema."""
    return schema.get("prompts", {}).get(key, "")


# ═══════════════════════════════════════════════════════════════════════
# STEP 1: Summarize
# ═══════════════════════════════════════════════════════════════════════

def _summarize_chunk(text: str, schema: dict) -> str:
    """Summarize a single chunk of text."""
    prompt_template = _get_prompt(schema, "summarize")
    if not prompt_template:
        prompt_template = (
            "Summarize the following text in under 200 words. "
            "Focus on what the module does, key features, and use cases.\n\n"
            "SOURCE TEXT:\n{text}"
        )
    prompt = prompt_template.replace("{text}", text)
    return llm_client.chat(prompt, temperature=0.1, max_tokens=500)


def _summarize_source(text: str, schema: dict) -> str:
    """
    Summarize a source, handling large files via Map-Reduce.

    MAP:    Summarize each chunk independently.
    REDUCE: If multiple summaries, ask the LLM to merge them.
    """
    chunks = chunker.split_into_chunks(text)

    if len(chunks) == 1:
        print(f"    -> Single chunk ({chunks[0]['tokens_est']} tokens)")
        return _summarize_chunk(chunks[0]["text"], schema)

    print(f"    -> {len(chunks)} chunks (Map-Reduce mode)")

    # MAP: Summarize each chunk
    chunk_summaries = []
    for c in chunks:
        print(f"      Chunk {c['index'] + 1}/{len(chunks)} "
              f"({c['tokens_est']} tokens)...", end=" ")
        summary = _summarize_chunk(c["text"], schema)
        chunk_summaries.append(summary)
        print("OK")

    # REDUCE: Merge all summaries into one
    combined = "\n\n---\n\n".join(
        [f"Chunk {i+1} Summary:\n{s}" for i, s in enumerate(chunk_summaries)]
    )
    merge_prompt = (
        "You are given multiple partial summaries of the SAME Lua source document. "
        "Merge them into ONE coherent summary (under 250 words). "
        "Remove duplicates. Keep the most important details.\n\n"
        f"{combined}"
    )
    print("      Merging summaries...", end=" ")
    merged = llm_client.chat(merge_prompt, temperature=0.1, max_tokens=600)
    print("OK")
    return merged


# ═══════════════════════════════════════════════════════════════════════
# STEP 2: Extract Entities
# ═══════════════════════════════════════════════════════════════════════

def _extract_entities_chunk(text: str, schema: dict) -> dict:
    """Extract entities from a single chunk."""
    prompt_template = _get_prompt(schema, "extract_entities")
    if not prompt_template:
        prompt_template = (
            "Extract all entities (modules, functions, concepts, dependencies) "
            "from this text. Return valid JSON.\n\nSOURCE TEXT:\n{text}"
        )
    prompt = prompt_template.replace("{text}", text)
    result = llm_client.chat_json(prompt, temperature=0.05, max_tokens=1500)

    # Ensure all expected keys exist
    for key in ["modules", "functions", "api_types", "constants", "concepts", "dependencies"]:
        if key not in result:
            result[key] = []

    return result


def _extract_entities_source(text: str, schema: dict) -> dict:
    """
    Extract entities from a source, handling large files via Map-Reduce.

    MAP:    Extract from each chunk.
    REDUCE: Merge + deduplicate entities across chunks.
    """
    chunks = chunker.split_into_chunks(text)

    if len(chunks) == 1:
        return _extract_entities_chunk(chunks[0]["text"], schema)

    print(f"    -> Entity extraction across {len(chunks)} chunks")

    # MAP
    all_entities = {"modules": [], "functions": [], "api_types": [], "constants": [],
                    "concepts": [], "dependencies": []}

    for c in chunks:
        print(f"      Extracting chunk {c['index'] + 1}/{len(chunks)}...", end=" ")
        extracted = _extract_entities_chunk(c["text"], schema)
        for key in all_entities:
            all_entities[key].extend(extracted.get(key, []))
        print("OK")

    # REDUCE: Deduplicate by name
    for key in all_entities:
        seen = {}
        deduped = []
        for entity in all_entities[key]:
            name = entity.get("name", "").lower().strip()
            if name and name not in seen:
                seen[name] = True
                deduped.append(entity)
            elif name in seen:
                # Merge: keep the one with more content
                pass
        all_entities[key] = deduped

    return all_entities


# ═══════════════════════════════════════════════════════════════════════
# STEP 3: Write Wiki Drafts
# ═══════════════════════════════════════════════════════════════════════

def _write_entity_drafts(entities: dict, summary: str,
                          source_file: str) -> List[str]:
    """
    Create draft wiki pages for extracted entities.
    Returns list of created draft paths.
    """
    created = []

    # Write module pages
    for mod in entities.get("modules", []):
        # Handle case where mod might be a string instead of dict
        if isinstance(mod, str):
            name = mod.strip()
            if not name:
                continue
            source = source_file
            summary_text = summary
        else:
            name = mod.get("name", "").strip()
            if not name:
                continue
            source = mod.get("source", source_file)
            summary_text = mod.get("summary", summary)

        # Collect functions belonging to this module
        mod_functions = [
            f for f in entities.get("functions", [])
            if isinstance(f, dict) and f.get("module", "").lower() == name.lower()
        ]

        func_lines = []
        for fn in mod_functions:
            # Handle case where function might be a string
            if isinstance(fn, str):
                sig = fn
                desc = ""
            else:
                sig = fn.get("signature", fn.get("name", ""))
                desc = fn.get("description", "")
            func_lines.append(f"- `{sig}` - {desc}")

        # Collect dependencies
        mod_deps = [
            d for d in entities.get("dependencies", [])
            if isinstance(d, dict) and name.lower() in d.get("used_by", "").lower()
        ]
        dep_lines = []
        for d in mod_deps:
            if isinstance(d, dict):
                dep_lines.append(f"- [[{d.get('name', '')}]]")

        # Build cross-references from concepts
        xrefs = []
        for c in entities.get("concepts", []):
            if isinstance(c, dict):
                xrefs.append(f"- [[{c.get('name', '')}]]")
            elif isinstance(c, str) and c.strip():
                xrefs.append(f"- [[{c.strip()}]]")

        content = (
            f"# {name}\n\n"
            f"**Type**: Module  \n"
            f"**Source**: {source}  \n\n"
            f"## Summary\n{summary_text}\n\n"
            f"## Key Functions\n"
            f"{chr(10).join(func_lines) if func_lines else '_None extracted_'}\n\n"
            f"## Dependencies\n"
            f"{chr(10).join(dep_lines) if dep_lines else '_None_'}\n\n"
            f"## See Also\n"
            f"{chr(10).join(xrefs) if xrefs else '_None_'}\n"
        )
        path = tools.write_draft(name, content, category="entities")
        created.append(path)
        print(f"      [+] Draft: entities/{name}")

    # Write concept pages
    for concept in entities.get("concepts", []):
        # Handle case where concept might be a string instead of dict
        if isinstance(concept, str):
            name = concept.strip()
            if not name:
                continue
            overview = ""
            code = "_none_"
            related_concepts = []
        else:
            name = concept.get("name", "").strip()
            if not name:
                continue
            overview = concept.get("overview", "")
            code = concept.get("code", "_none_")
            related_concepts = concept.get("related_concepts", [])

        # Find related concepts
        related_concepts_lines = [
            f"- [[{c}]]" for c in related_concepts if c
        ]

        # Find related modules
        related = [
            f"- [[{m.get('name', '')}]]"
            for m in entities.get("modules", [])
        ]

        content = (
            f"# {name}\n\n"
            f"**Type**: Concept  \n\n"
            f"## Overview\n{overview}\n\n"
            f"## Implementation / Context Code\n```lua\n{code}\n```\n\n"
            f"## Related Concepts\n"
            f"{chr(10).join(related_concepts_lines) if related_concepts_lines else '_None_'}\n\n"
            f"## Related Modules\n"
            f"{chr(10).join(related) if related else '_None_'}\n\n"
            f"## Notes\n_Auto-generated from source: {source_file}_\n"
        )
        path = tools.write_draft(name, content, category="concepts")
        created.append(path)
        print(f"      [+] Draft: concepts/{name}")

    # Write function pages (for all functions)
    for fn in entities.get("functions", []):
        name = fn.get("name", "").strip()
        if not name:
            continue
        
        module_name = fn.get("module", "unknown")
        module_ref = f"[[{module_name}]]" if module_name and module_name.lower() != "unknown" else "_unknown_"
        
        # Format parameters
        params_raw = fn.get("parameters", [])
        if isinstance(params_raw, list) and len(params_raw) > 0:
            params_str = "\n".join([f"- `{p.get('name', 'arg')}` ({p.get('type', 'any')}): {p.get('description', '')}" for p in params_raw if isinstance(p, dict)])
        elif isinstance(params_raw, list):
            params_str = "_None_"
        else:
            params_str = str(params_raw)
            
        # Format returns
        returns_raw = fn.get("returns", [])
        if isinstance(returns_raw, list) and len(returns_raw) > 0:
            returns_str = "\n".join([f"- ({r.get('type', 'any')}): {r.get('description', '')}" for r in returns_raw if isinstance(r, dict)])
        elif isinstance(returns_raw, list):
            returns_str = "_None_"
        else:
            returns_str = str(returns_raw)

        content = (
            f"# {name}\n\n"
            f"**Type**: Function  \n"
            f"**Module**: {module_ref}  \n\n"
            f"## Signature\n```lua\n{fn.get('signature', name)}\n```\n\n"
            f"## Description\n{fn.get('description', '')}\n\n"
            f"## Parameters\n{params_str}\n\n"
            f"## Returns\n{returns_str}\n\n"
            f"## Implementation Code\n```c\n{fn.get('code', '_none_')}\n```\n"
        )
        path = tools.write_draft(name, content, category="entities")
        created.append(path)
        print(f"      [+] Draft: entities/{name} (function)")

    # Write dependency pages
    for dep in entities.get("dependencies", []):
        name = dep.get("name", "").strip()
        if not name:
            continue
        content = (
            f"# {name}\n\n"
            f"**Type**: Dependency  \n\n"
            f"## Description\n{dep.get('description', '')}\n\n"
            f"## Used By\n- {dep.get('used_by', '_unknown_')}\n"
        )
        path = tools.write_draft(name, content, category="entities")
        created.append(path)
        print(f"      [+] Draft: entities/{name} (dependency)")

    # Write api_types pages
    for typ in entities.get("api_types", []):
        name = typ.get("name", "").strip()
        if not name:
            continue
        content = (
            f"# {name}\n\n"
            f"**Type**: API Type ({typ.get('type_of', 'unknown')})  \n\n"
            f"## Definition\n```c\n{typ.get('code', '_none_')}\n```\n\n"
            f"## Description\n{typ.get('description', '')}\n"
        )
        path = tools.write_draft(name, content, category="entities")
        created.append(path)
        print(f"      [+] Draft: entities/{name} (api_type)")

    # Write constants pages
    for const in entities.get("constants", []):
        name = const.get("name", "").strip()
        if not name:
            continue
        content = (
            f"# {name}\n\n"
            f"**Type**: Constant  \n\n"
            f"## Value\n```c\n{const.get('code', '_none_')}\n```\n\n"
            f"## Description\n{const.get('description', '')}\n"
        )
        path = tools.write_draft(name, content, category="entities")
        created.append(path)
        print(f"      [+] Draft: entities/{name} (constant)")

    return created


# ═══════════════════════════════════════════════════════════════════════
# STEP 4: Contradiction Check
# ═══════════════════════════════════════════════════════════════════════

def _check_contradictions(entities: dict, schema: dict) -> List[dict]:
    """
    Compare extracted entities against existing wiki pages.
    Returns a list of contradiction reports.
    """
    contradictions = []

    for mod in entities.get("modules", []):
        name = mod.get("name", "").strip()
        if not name:
            continue

        existing = tools.read_wiki_page(name)
        if not existing:
            continue  # New page, no contradiction possible

        prompt_template = _get_prompt(schema, "contradiction_check")
        if not prompt_template:
            continue

        prompt = prompt_template.replace(
            "{existing}", existing[:2000]
        ).replace(
            "{new_info}", json.dumps(mod, indent=2)[:2000]
        )

        result = llm_client.chat_json(prompt, temperature=0.05, max_tokens=800)
        if result.get("contradictions"):
            contradictions.extend(result["contradictions"])
            print(f"      [!] Contradiction found in: {name}")

    return contradictions


# ═══════════════════════════════════════════════════════════════════════
# MAIN: Ingest Pipeline
# ═══════════════════════════════════════════════════════════════════════

def ingest_source(filename: str, auto_promote: bool = False, skip_existing: bool = False) -> dict:
    """
    Full ingest pipeline for a single source file.

    Args:
        filename: Name of the file in raw/ to ingest.
        auto_promote: If True, automatically promote drafts after ingest.
        skip_existing: If True, skip ingestion if draft already exists for this source.

    Returns:
        A report dict with stats about the ingest operation.
    """
    schema = _load_schema()

    report = {
        "source": filename,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "summary": "",
        "entities_found": {},
        "drafts_created": [],
        "contradictions": [],
        "status": "ok",
    }

    # Step 0: Check if we should skip existing
    if skip_existing:
        # Check if any draft already exists - if so, skip entire ingestion
        # This matches the request: "solo poner para existe el name of file in draft y suficiente"
        drafts_dir = tools.DRAFTS_DIR
        if os.path.exists(drafts_dir) and os.listdir(drafts_dir):
            print(f"  [SKIP] Drafts already exist in {drafts_dir}. Skipping ingestion of {filename}")
            report["status"] = "skipped"
            return report

    # Step 0: Read source
    print(f"\n{'=' * 60}")
    print(f"  INGEST: {filename}")
    print(f"{'=' * 60}")

    try:
        text = tools.read_source(filename)
    except FileNotFoundError as e:
        print(f"  [X] {e}")
        report["status"] = "error"
        return report

    total_tokens = chunker.estimate_tokens(text)
    print(f"  Source size: ~{total_tokens} tokens")

    # Step 1: Summarize
    print(f"\n  [1/4] Summarizing...")
    summary = _summarize_source(text, schema)
    report["summary"] = summary
    print(f"    [OK] Summary: {summary[:100]}...")

    # Step 2: Extract entities
    print(f"\n  [2/4] Extracting entities...")
    entities = _extract_entities_source(text, schema)
    counts = {k: len(v) for k, v in entities.items()}
    report["entities_found"] = counts
    print(f"    [OK] Found: {counts}")

    # Step 3: Write drafts
    print(f"\n  [3/4] Writing wiki drafts...")
    drafts = _write_entity_drafts(entities, summary, filename)
    report["drafts_created"] = [os.path.basename(d) for d in drafts]
    print(f"    [OK] Created {len(drafts)} draft(s)")

    # Step 4: Contradiction check
    print(f"\n  [4/4] Checking contradictions...")
    contradictions = _check_contradictions(entities, schema)
    report["contradictions"] = contradictions
    if contradictions:
        print(f"    [!] {len(contradictions)} contradiction(s) detected")
        for c in contradictions:
            print(f"      - {c.get('entity', '?')}.{c.get('field', '?')}: "
                  f"{c.get('existing_value', '?')} vs {c.get('new_value', '?')}")
    else:
        print(f"    [OK] No contradictions")

    # Optional: auto-promote
    if auto_promote and drafts:
        print(f"\n  Auto-promoting {len(drafts)} draft(s)...")
        promoted = tools.promote_all_drafts()
        print(f"    [OK] Promoted: {len(promoted)} page(s)")

    print(f"\n{'=' * 60}")
    print(f"  INGEST COMPLETE: {filename}")
    print(f"  Summary: {len(summary)} chars | "
          f"Entities: {sum(counts.values())} | "
          f"Drafts: {len(drafts)} | "
          f"Contradictions: {len(contradictions)}")
    print(f"{'=' * 60}\n")

    return report


def ingest_all(auto_promote: bool = False, skip_existing: bool = False) -> List[dict]:
    """
    Ingest ALL files in raw/.
    Returns a list of ingest reports.
    """
    sources = tools.list_raw_sources()
    if not sources:
        print("  No sources found in raw/")
        return []

    print(f"\n{'=' * 60}")
    print(f"  BATCH INGEST: {len(sources)} source(s)")
    print(f"{'=' * 60}\n")

    reports = []
    for i, src in enumerate(sources, 1):
        print(f"\n[{i}/{len(sources)}] Processing: {src}")
        report = ingest_source(src, auto_promote=auto_promote)
        reports.append(report)

    # Final summary
    ok = sum(1 for r in reports if r["status"] == "ok")
    err = sum(1 for r in reports if r["status"] == "error")
    skipped = sum(1 for r in reports if r["status"] == "skipped")
    total_entities = sum(
        sum(r["entities_found"].values()) for r in reports
    )
    total_drafts = sum(len(r["drafts_created"]) for r in reports)
    total_contradictions = sum(len(r["contradictions"]) for r in reports)

    print(f"\n{'=' * 60}")
    print(f"  BATCH COMPLETE")
    print(f"  OK: {ok} | Errors: {err} | Skipped: {skipped}")
    print(f"  Total entities: {total_entities}")
    print(f"  Total drafts: {total_drafts}")
    print(f"  Total contradictions: {total_contradictions}")
    print(f"{'=' * 60}\n")

    return reports
