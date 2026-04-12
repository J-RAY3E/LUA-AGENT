#!/usr/bin/env python3
"""
luarocks_mcp_builder.py — CLI entry point for the LuaRocks MCP pipeline.

Usage:
    pip install -r requirements.txt
    python luarocks_mcp_builder.py --labels json,http,database
    python luarocks_mcp_builder.py --labels json --model qwen2.5:7b-q6_K_M
    python luarocks_mcp_builder.py --all-labels

Architecture:
    4 worker threads connected by queue.Queue:
    [Discovery] → [Download] → [Extraction] → [Assembly]

Scaling Notes:
    - Parallelize: increase download/extraction workers in pipeline.py
    - Switch LLM: --model <name> or LOCAL_LLM_MODEL env var
    - Add labels:  append to ALL_LABELS in config.py or pass --labels
    - Rate limits: --delay-min / --delay-max
    - Incremental: idempotent via processed.jsonl manifest
"""

import argparse
import sys

import config
from config import CONFIG, ALL_LABELS
from pipeline import Pipeline


def main() -> None:
    parser = argparse.ArgumentParser(
        description="LuaRocks MCP Knowledge Base Builder (threaded pipeline)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python luarocks_mcp_builder.py --labels json,http,database
  python luarocks_mcp_builder.py --labels json --model qwen2.5:7b-q6_K_M
  python luarocks_mcp_builder.py --all-labels --delay-min 2 --delay-max 3
  GITHUB_TOKEN=ghp_xxx python luarocks_mcp_builder.py --labels json
        """,
    )
    parser.add_argument(
        "--labels", type=str, default="json",
        help="Comma-separated list of LuaRocks labels (default: json)",
    )
    parser.add_argument(
        "--all-labels", action="store_true",
        help="Scrape ALL known labels",
    )
    parser.add_argument(
        "--model", type=str, default=None,
        help=f"LLM model name (default: {CONFIG['llm_model']})",
    )
    parser.add_argument(
        "--llm-url", type=str, default=None,
        help=f"LLM API base URL (default: {CONFIG['llm_api_url']})",
    )
    parser.add_argument(
        "--github-token", type=str, default=None,
        help="GitHub API token (or set GITHUB_TOKEN env var)",
    )
    parser.add_argument(
        "--delay-min", type=float, default=None,
        help="Minimum delay between requests (seconds)",
    )
    parser.add_argument(
        "--delay-max", type=float, default=None,
        help="Maximum delay between requests (seconds)",
    )

    args = parser.parse_args()

    # Apply CLI overrides
    if args.model:
        CONFIG["llm_model"] = args.model
    if args.llm_url:
        CONFIG["llm_api_url"] = args.llm_url
    if args.github_token:
        config.GITHUB_TOKEN = args.github_token
    if args.delay_min is not None:
        CONFIG["request_delay_min"] = args.delay_min
    if args.delay_max is not None:
        CONFIG["request_delay_max"] = args.delay_max

    # Resolve labels
    if args.all_labels:
        labels = ALL_LABELS
    else:
        labels = [l.strip() for l in args.labels.split(",") if l.strip()]

    if not labels:
        print("Error: no labels specified. Use --labels or --all-labels.", file=sys.stderr)
        sys.exit(1)

    # Run
    pipeline = Pipeline(labels)
    pipeline.run()


if __name__ == "__main__":
    main()
