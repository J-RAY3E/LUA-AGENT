"""
config.py — Configuration, constants, and logging for the LuaRocks MCP pipeline.

Set GITHUB_TOKEN before running, either directly or via environment variable.
LLM endpoint uses OpenAI-compatible /v1/chat/completions (llama.cpp / Ollama / LiteLLM).
"""

import os
import sys
import logging
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent

# ─── Global Tokens ────────────────────────────────────────────────
# Set directly:  config.GITHUB_TOKEN = "ghp_..."
# Or via env:    GITHUB_TOKEN=ghp_... python luarocks_mcp_builder.py
GITHUB_TOKEN: str = os.environ.get("GITHUB_TOKEN", "")

# ─── Pipeline Configuration ──────────────────────────────────────
CONFIG: dict[str, Any] = {
    # LuaRocks
    "base_url": "https://luarocks.org",

    # LLM — OpenAI-compatible endpoint (llama.cpp, Ollama /v1, LiteLLM)
    "llm_api_url": os.environ.get("LOCAL_LLM_URL", "http://127.0.0.1:8080/v1"),
    "llm_model": os.environ.get("LOCAL_LLM_MODEL", "qwen2.5:7b-q6_K_M"),
    "llm_temperature": 0.1,
    "llm_max_tokens": 2000,

    # Rate limiting
    "request_delay_min": 1.0,
    "request_delay_max": 2.0,
    "max_retries": 3,

    # Chunking
    "max_chunk_chars": 14000,
    "chunk_overlap_chars": 300,

    # Paths
    "raw_dir": BASE_DIR / "raw",
    "output_dir": BASE_DIR / "output",
    "logs_dir": BASE_DIR / "logs",
    "processed_file": BASE_DIR / "processed.jsonl",

    # Valid Git hosts
    "valid_hosts": {"github.com", "gitlab.com", "bitbucket.org"},

    # HTTP
    "user_agent": "LuaRocks-MCP-Builder/1.0",
    "max_lua_files_per_repo": 30,
}

# ─── All LuaRocks Labels ─────────────────────────────────────────
ALL_LABELS: list[str] = [
    "audio", "authentication", "awesome", "aws", "base-n", "batteries",
    "bitwise", "commandline", "compression", "crypto", "database",
    "datastructure", "dbus", "debug", "dns", "doc", "email", "event",
    "feed", "ffi", "filesystem", "game", "git", "gui", "haml", "html",
    "http", "i18n", "image", "ini", "irc", "jit", "json", "kong",
    "lapis", "lint", "linux", "logs", "love", "lpeg", "markdown",
    "math", "messagepack", "metalua", "midi", "mjolnir", "moonscript",
    "mpi", "neovim", "network", "nginx", "object", "openresty", "posix",
    "redis", "regexp", "rocks", "search", "security", "serialization",
    "spreadsheet", "statemachine", "strict", "template", "test",
    "threads", "time", "torch", "unicode", "vim", "web", "wiki",
    "windows", "wsapi", "xml", "yaml", "zeromq",
]

# ─── Logger ───────────────────────────────────────────────────────
logger = logging.getLogger("luarocks_mcp")


def setup_logging() -> None:
    """Configure file + console logging with timestamps."""
    logs_dir: Path = CONFIG["logs_dir"]
    logs_dir.mkdir(parents=True, exist_ok=True)

    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    fh = logging.FileHandler(logs_dir / "pipeline.log", encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)

    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)
