"""
cli.py — Command-line interface for the Wiki Brain.

Usage:
  python -m wiki ingest <filename>       Ingest a single source from raw/
  python -m wiki ingest --all            Ingest all sources in raw/
  python -m wiki query "your question"   Query the compiled wiki
  python -m wiki lint                    Run health checks
  python -m wiki promote                 Promote all drafts to wiki
  python -m wiki status                  Show wiki stats
"""

import sys
import os
import json

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wiki import ingest, query as query_module, lint as lint_module, tools


def cmd_ingest(args):
    """Handle the 'ingest' command."""
    auto_promote = "--auto-promote" in args
    skip_existing = "--skip-existing" in args
    filtered_args = [a for a in args if a not in ["--auto-promote", "--skip-existing"]]
    
    print(f"[DEBUG] auto_promote: {auto_promote}, skip_existing: {skip_existing}")

    if "--all" in filtered_args:
        print(f"[DEBUG] Calling ingest_all with skip_existing={skip_existing}")
        reports = ingest.ingest_all(auto_promote=auto_promote, skip_existing=skip_existing)
        # Save batch report
        report_path = os.path.join(tools.CONFIG_DIR, "last_batch_report.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(reports, f, indent=2, ensure_ascii=False)
        print(f"\n  Report saved to: {report_path}")
    elif filtered_args:
        filename = filtered_args[0]
        print(f"[DEBUG] Calling ingest_source for {filename} with skip_existing={skip_existing}")
        report = ingest.ingest_source(filename, auto_promote=auto_promote, skip_existing=skip_existing)
        # Save report
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
    # Save report
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
    }

    if command in commands:
        commands[command](args)
    else:
        print(f"Unknown command: {command}")
        print(__doc__)


if __name__ == "__main__":
    main()
