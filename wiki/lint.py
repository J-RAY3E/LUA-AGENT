"""
lint.py — Health checks for the Wiki Brain.

Finds:
  - Orphan pages (not referenced by any other page)
  - Broken cross-references ([[missing-page]])
  - Stale pages (not updated recently)
  - Missing cross-references (entities that should link but don't)
  - Empty or stub pages
"""

import os
import re
from datetime import datetime, timezone, timedelta
from typing import List

from . import tools


def lint_wiki(verbose: bool = True) -> dict:
    """
    Run all health checks on the wiki.

    Returns a report dict:
    {
        "orphans": [...],
        "broken_refs": [...],
        "stale_pages": [...],
        "empty_pages": [...],
        "suggestions": [...]
    }
    """
    report = {
        "orphans": [],
        "broken_refs": [],
        "stale_pages": [],
        "empty_pages": [],
        "suggestions": [],
    }

    wiki_files = tools.list_wiki_files()
    all_pages = {}  # page_name -> full content

    # Load all wiki pages
    for category in ["entities", "concepts"]:
        for fname in wiki_files.get(category, []):
            page_name = fname.replace(".md", "")
            subdir = tools.ENTITIES_DIR if category == "entities" else tools.CONCEPTS_DIR
            fpath = os.path.join(subdir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                all_pages[page_name] = f.read()

    if not all_pages:
        if verbose:
            print("  Wiki is empty. Nothing to lint.")
        return report

    if verbose:
        print(f"\n{'=' * 60}")
        print(f"  LINT: Checking {len(all_pages)} wiki page(s)")
        print(f"{'=' * 60}")

    # ── Check 1: Orphan pages ─────────────────────────────────────────
    if verbose:
        print(f"\n  [1/5] Checking for orphan pages...")

    for page_name in all_pages:
        refs = tools.get_related_pages(page_name)
        if not refs:
            report["orphans"].append(page_name)
            if verbose:
                print(f"    [!] Orphan: {page_name}")

    # ── Check 2: Broken cross-references ──────────────────────────────
    if verbose:
        print(f"\n  [2/5] Checking for broken cross-references...")

    ref_pattern = re.compile(r"\[\[([^\]]+)\]\]")
    for page_name, content in all_pages.items():
        refs = ref_pattern.findall(content)
        for ref in refs:
            ref_clean = ref.strip().lower()
            if ref_clean not in all_pages:
                report["broken_refs"].append({
                    "page": page_name,
                    "broken_ref": ref,
                })
                if verbose:
                    print(f"    [X] Broken ref in {page_name}: [[{ref}]]")

    # ── Check 3: Stale pages ──────────────────────────────────────────
    if verbose:
        print(f"\n  [3/5] Checking for stale pages...")

    stale_threshold = timedelta(days=30)
    now = datetime.now(timezone.utc)

    for page_name, content in all_pages.items():
        # Look for last-updated in front matter
        match = re.search(r"created:\s*(.+)", content)
        if match:
            try:
                created = datetime.fromisoformat(match.group(1).strip())
                if now - created > stale_threshold:
                    report["stale_pages"].append({
                        "page": page_name,
                        "age_days": (now - created).days,
                    })
                    if verbose:
                        print(f"    [STALE] Stale: {page_name} "
                              f"({(now - created).days} days old)")
            except (ValueError, TypeError):
                pass

    # ── Check 4: Empty or stub pages ──────────────────────────────────
    if verbose:
        print(f"\n  [4/5] Checking for empty/stub pages...")

    for page_name, content in all_pages.items():
        # Strip front matter
        stripped = re.sub(r"^---.*?---\s*", "", content, flags=re.DOTALL)
        # Count actual content (excluding headers and whitespace)
        text_only = re.sub(r"[#*\-_\[\]\n\r\s]", "", stripped)
        if len(text_only) < 50:
            report["empty_pages"].append(page_name)
            if verbose:
                print(f"    [EMPTY] Empty/stub: {page_name}")

    # ── Check 5: Generate suggestions ─────────────────────────────────
    if verbose:
        print(f"\n  [5/5] Generating suggestions...")

    if report["orphans"]:
        report["suggestions"].append(
            f"Consider adding cross-references to {len(report['orphans'])} "
            f"orphan page(s): {', '.join(report['orphans'][:5])}"
        )
    if report["broken_refs"]:
        missing = set(r["broken_ref"] for r in report["broken_refs"])
        report["suggestions"].append(
            f"Consider creating pages for: {', '.join(list(missing)[:5])}"
        )
    if report["stale_pages"]:
        report["suggestions"].append(
            f"Re-ingest sources for {len(report['stale_pages'])} stale page(s)"
        )
    if report["empty_pages"]:
        report["suggestions"].append(
            f"Flesh out {len(report['empty_pages'])} empty/stub page(s)"
        )

    # No issues
    if not any(report[k] for k in ["orphans", "broken_refs",
                                    "stale_pages", "empty_pages"]):
        report["suggestions"].append("[OK] Wiki is healthy! No issues found.")

    # Summary
    if verbose:
        print(f"\n{'=' * 60}")
        print(f"  LINT RESULTS")
        print(f"  Orphans:       {len(report['orphans'])}")
        print(f"  Broken refs:   {len(report['broken_refs'])}")
        print(f"  Stale pages:   {len(report['stale_pages'])}")
        print(f"  Empty pages:   {len(report['empty_pages'])}")
        print(f"  Suggestions:   {len(report['suggestions'])}")
        for s in report["suggestions"]:
            print(f"    -> {s}")
        print(f"{'=' * 60}\n")

    return report
