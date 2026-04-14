"""
cli.py — Command-line interface for the Wiki Brain & Code Generator.

Usage:
  python -m wiki ingest <filename>       Ingest a single source from raw/
  python -m wiki ingest --all            Ingest all sources in raw/
  python -m wiki query "your question"   Query the compiled wiki
  python -m wiki lint                    Run health checks
  python -m wiki promote                 Promote all drafts to wiki
  python -m wiki status                  Show wiki stats
  python -m wiki agent "task"            Generate Lua code using AI Agent (Auto-Context + Validation)
"""

import sys
import os
import json

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wiki import ingest, query as query_module, lint as lint_module, tools

# --- IMPORTS FOR CODE GENERATOR ---
try:
    from agents.coder import generate_code
    from agents.validator import validate_and_reconstruct_lua
    HAS_AGENT = True
except ImportError as e:
    print(f"[!] Warning: Could not import agent modules. {e}")
    HAS_AGENT = False
    generate_code = None
    validate_and_reconstruct_lua = None
# ----------------------------------


def cmd_ingest(args):
    """Handle the 'ingest' command."""
    auto_promote = "--auto-promote" in args
    skip_existing = "--skip-existing" in args
    filtered_args = [a for a in args if a not in ["--auto-promote", "--skip-existing"]]
    
    # Debug logs removed for cleaner output, kept for reference if needed
    if "--all" in filtered_args:
        reports = ingest.ingest_all(auto_promote=auto_promote, skip_existing=skip_existing)
        report_path = os.path.join(tools.CONFIG_DIR, "last_batch_report.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(reports, f, indent=2, ensure_ascii=False)
        print(f"\n  Report saved to: {report_path}")
    elif filtered_args:
        filename = filtered_args[0]
        report = ingest.ingest_source(filename, auto_promote=auto_promote, skip_existing=skip_existing)
        report_path = os.path.join(tools.CONFIG_DIR, "last_ingest_report.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n  Report saved to: {report_path}")
    else:
        print("Usage: python -m wiki ingest <filename|--all> [--auto-promote] [--skip-existing]")


def cmd_query(args):
    """Handle the 'query' command."""
    if not args:
        print("Usage: python -m wiki query \"your question here\"")
        return

    question = " ".join(args)
    save = "--save" in args
    if save:
        question = question.replace("--save", "").strip()

    answer = query_module.query(question, save_answer=save)
    print(f"\n{'-' * 60}")
    print(answer)
    print(f"{'-' * 60}")


def cmd_lint(_args):
    """Handle the 'lint' command."""
    report = lint_module.lint_wiki(verbose=True)
    report_path = os.path.join(tools.CONFIG_DIR, "last_lint_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n  Report saved to: {report_path}")


def cmd_promote(_args):
    """Promote all drafts."""
    promoted = tools.promote_all_drafts()
    if promoted:
        print(f"\n  [OK] Promoted {len(promoted)} draft(s):")
        for p in promoted:
            print(f"    -> {p}")
    else:
        print("\n  No drafts to promote.")


def cmd_status(_args):
    """Show wiki statistics."""
    wiki_files = tools.list_wiki_files()
    raw_sources = tools.list_raw_sources()

    print(f"\n{'=' * 60}")
    print(f"  WIKI BRAIN STATUS")
    print(f"{'=' * 60}")
    print(f"  Raw sources:  {len(raw_sources)}")
    print(f"  Entities:     {len(wiki_files.get('entities', []))}")
    print(f"  Concepts:     {len(wiki_files.get('concepts', []))}")
    print(f"  Drafts:       {len(wiki_files.get('drafts', []))}")
    print(f"{'=' * 60}")

    if wiki_files.get("drafts"):
        print(f"\n  Pending drafts:")
        for d in wiki_files["drafts"]:
            print(f"    [draft] {d}")

    if raw_sources:
        print(f"\n  Raw sources:")
        for s in raw_sources[:10]:
            print(f"    [raw] {s}")
        if len(raw_sources) > 10:
            print(f"    ... and {len(raw_sources) - 10} more")


def cmd_agent(args):
    """
    Handle the 'agent' command.
    Generates Lua code with automatic context retrieval, pure logic fallback, 
    and AST-based syntax validation.
    """
    if not args:
        print("Usage: python -m wiki agent \"your coding task here\"")
        print("Example: python -m wiki agent \"buat fungsi baca file CSV menggunakan iterator\"")
        return

    force_logic = "--force-logic" in args
    
    if not HAS_AGENT:
        print("[!] Error: Agent module not found.")
        print("    Please ensure the 'agents/' folder exists with coder.py and validator.py.")
        return

    task = " ".join(args)
    
    print(f"\n{'='*60}")
    print(f"  LUA CODING AGENT: {task}")
    print(f"{'='*60}")

    try:
        code = generate_code(task)
        
        if not code or code.startswith("--"):
            print(f"  [ERROR] Gagal menghasilkan kode valid: {code}")
            return

        preview = code[:300].replace('\n', '\\n')
        print(f"      Preview: {preview}...")

        safe_name = task.lower().replace(" ", "_").replace("?", "").replace("/", "_")[:40] + ".lua"
        filepath = generate_code.__globals__.get('save_code', lambda c, n, d="projects": None)(code, safe_name)
        
        os.makedirs("projects", exist_ok=True)
        final_path = os.path.join("projects", safe_name)
        with open(final_path, "w", encoding="utf-8") as f:
            f.write(code)
            
        print(f"      [OK] Kode tersimpan di: {final_path}")
        print(f"\n--- Generated Code ---\n{code}\n--- End Code ---\n")

    except Exception as e:
        print(f"      [ERROR] Terjadi kesalahan: {e}")
        import traceback
        traceback.print_exc()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    commands = {
        "ingest": cmd_ingest,
        "query": cmd_query,
        "lint": cmd_lint,
        "promote": cmd_promote,
        "status": cmd_status,
        "agent": cmd_agent,
    }

    if command in commands:
        commands[command](args)
    else:
        print(f"Unknown command: {command}")
        print(__doc__)


if __name__ == "__main__":
    main()
