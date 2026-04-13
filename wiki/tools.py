"""
tools.py — Filesystem tools for the Wiki Brain.

These are the ONLY file operations the system performs.
All writes go to wiki/drafts/ first (promote_draft moves them out).
"""

import os
import re
import json
import shutil
import glob
from datetime import datetime, timezone
from typing import List, Optional


# ── Base paths ────────────────────────────────────────────────────────
_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(_PROJECT_ROOT, "raw")
WIKI_DIR = _PROJECT_ROOT  # The module itself IS the wiki directory now
DRAFTS_DIR = os.path.join(WIKI_DIR, "drafts")
ENTITIES_DIR = os.path.join(WIKI_DIR, "entities")
CONCEPTS_DIR = os.path.join(WIKI_DIR, "concepts")
CONFIG_DIR = os.path.join(_PROJECT_ROOT, "config")


def _ensure_dirs():
    """Create wiki directories if they don't exist."""
    for d in [RAW_DIR, DRAFTS_DIR, ENTITIES_DIR, CONCEPTS_DIR]:
        os.makedirs(d, exist_ok=True)


def _safe_filename(name: str) -> str:
    """Convert a name to a safe, normalized filename."""
    name = name.lower().strip()
    name = re.sub(r"[^a-z0-9_\-.]", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name


# ═══════════════════════════════════════════════════════════════════════
# READ operations
# ═══════════════════════════════════════════════════════════════════════

def read_source(filename: str) -> str:
    """
    Read a raw source file from raw/.
    Supports: .txt, .md, .json
    For JSON files, extracts the text content fields.
    """
    path = os.path.join(RAW_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Source not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # For JSON sources (like existing raw_data format), extract text
    if filename.endswith(".json"):
        try:
            data = json.loads(content)
            parts = []
            for key in ["rock_name", "summary", "raw_content",
                        "phase1", "phase2", "phase3"]:
                if key in data and data[key]:
                    parts.append(f"## {key}\n{data[key]}")
            return "\n\n".join(parts) if parts else content
        except json.JSONDecodeError:
            return content

    return content


def read_wiki_page(page_name: str) -> Optional[str]:
    """
    Read an existing wiki page by name.
    Searches entities/ and concepts/ directories.
    """
    safe = _safe_filename(page_name)
    if not safe.endswith(".md"):
        safe += ".md"

    for subdir in [ENTITIES_DIR, CONCEPTS_DIR, DRAFTS_DIR]:
        path = os.path.join(subdir, safe)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
    return None


def list_raw_sources() -> List[str]:
    """List all files in raw/."""
    _ensure_dirs()
    return sorted(os.listdir(RAW_DIR))


def list_wiki_files() -> dict:
    """
    List all wiki pages organized by category.
    Returns: {"entities": [...], "concepts": [...], "drafts": [...]}
    """
    _ensure_dirs()
    result = {}
    for category, directory in [("entities", ENTITIES_DIR),
                                 ("concepts", CONCEPTS_DIR),
                                 ("drafts", DRAFTS_DIR)]:
        files = [f for f in os.listdir(directory) if f.endswith(".md")]
        result[category] = sorted(files)
    return result


# ═══════════════════════════════════════════════════════════════════════
# WRITE operations (always to drafts first)
# ═══════════════════════════════════════════════════════════════════════

def write_draft(page_name: str, content: str, category: str = "entities") -> str:
    """
    Write a wiki page to the drafts directory.

    Args:
        page_name: Name of the page (will be sanitized).
        content: Markdown content for the page.
        category: "entities" or "concepts" — stored as metadata for promote.

    Returns:
        The path to the created draft file.
    """
    _ensure_dirs()
    safe = _safe_filename(page_name)
    if not safe.endswith(".md"):
        safe += ".md"

    path = os.path.join(DRAFTS_DIR, safe)

    # Add front matter with metadata
    front_matter = (
        f"---\n"
        f"title: {page_name}\n"
        f"category: {category}\n"
        f"created: {datetime.now(timezone.utc).isoformat()}\n"
        f"status: draft\n"
        f"---\n\n"
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(front_matter + content)

    return path


def promote_draft(page_name: str) -> str:
    """
    Move a draft from wiki/drafts/ to its target directory (entities/ or concepts/).

    The target is determined by the 'category' field in the YAML front matter.
    Returns the destination path.
    """
    safe = _safe_filename(page_name)
    if not safe.endswith(".md"):
        safe += ".md"

    src = os.path.join(DRAFTS_DIR, safe)
    if not os.path.exists(src):
        raise FileNotFoundError(f"Draft not found: {src}")

    # Read front matter to determine category
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()

    category = "entities"  # default
    fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        cat_match = re.search(r"category:\s*(\w+)", fm_text)
        if cat_match:
            category = cat_match.group(1)

    # Update status in front matter
    content = content.replace("status: draft", "status: published")

    dest_dir = CONCEPTS_DIR if category == "concepts" else ENTITIES_DIR
    dest = os.path.join(dest_dir, safe)

    with open(dest, "w", encoding="utf-8") as f:
        f.write(content)

    os.remove(src)
    return dest


def promote_all_drafts() -> List[str]:
    """Promote all drafts to their target directories."""
    _ensure_dirs()
    promoted = []
    for fname in os.listdir(DRAFTS_DIR):
        if fname.endswith(".md"):
            try:
                dest = promote_draft(fname.replace(".md", ""))
                promoted.append(dest)
            except Exception as e:
                print(f"  [!] Failed to promote {fname}: {e}")
    return promoted


# ═══════════════════════════════════════════════════════════════════════
# SEARCH operations
# ═══════════════════════════════════════════════════════════════════════

def search_wiki(query: str, case_insensitive: bool = True) -> List[dict]:
    """
    Grep-based search across all wiki pages.

    Returns a list of matches:
      [{"file": "entities/csv.md", "line": 5, "text": "...matching line..."}]
    """
    _ensure_dirs()
    results = []
    flags = re.IGNORECASE if case_insensitive else 0
    pattern = re.compile(re.escape(query), flags)

    for subdir_name, subdir_path in [("entities", ENTITIES_DIR),
                                      ("concepts", CONCEPTS_DIR),
                                      ("drafts", DRAFTS_DIR)]:
        for fname in os.listdir(subdir_path):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(subdir_path, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    if pattern.search(line):
                        results.append({
                            "file": f"{subdir_name}/{fname}",
                            "line": i,
                            "text": line.strip(),
                        })

    return results


def get_related_pages(page_name: str) -> List[str]:
    """
    Find all wiki pages that reference a given page via [[page_name]] syntax.
    """
    _ensure_dirs()
    safe = _safe_filename(page_name)
    pattern = re.compile(r"\[\[" + re.escape(safe.replace(".md", "")) + r"\]\]",
                         re.IGNORECASE)
    related = []

    for subdir_name, subdir_path in [("entities", ENTITIES_DIR),
                                      ("concepts", CONCEPTS_DIR)]:
        for fname in os.listdir(subdir_path):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(subdir_path, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                if pattern.search(f.read()):
                    related.append(f"{subdir_name}/{fname}")

    return related
