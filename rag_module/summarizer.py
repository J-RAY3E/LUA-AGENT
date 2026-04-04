import requests
import json
import os
import glob
import re

LOCAL_API_URL = os.getenv("LOCAL_LLM_URL", "http://localhost:8080/v1")
LOCAL_MODEL = os.getenv("LOCAL_LLM_MODEL", "Volko76/Qwen2.5-1.5B-Instruct-Q5_K_M-GGUF:Q5_K_M")

# ── Anti-hallucination blacklist ──────────────────────────────────────────
PYTHON_BLACKLIST = [
    "numpy", "pandas", "requests", "fastapi", "sqlalchemy",
    "django", "flask", "scipy", "matplotlib", "tensorflow",
    "pytorch", "torch", "sklearn", "scikit", "celery",
    "beautifulsoup", "scrapy", "pillow", "pip", "conda",
]

# ── Domain dictionary for fallback enrichment ─────────────────────────────
TAG_DOMAIN_MAP = {
    "http": "HTTP networking, web client, request handling",
    "web": "web development, web framework, web server",
    "json": "JSON data serialization and deserialization",
    "xml": "XML document parsing and generation",
    "csv": "CSV tabular data parsing and file I/O",
    "database": "database access, query execution, data persistence",
    "orm": "object-relational mapping, database abstraction",
    "search": "search engine, full-text search, indexing",
    "crypto": "cryptography, encryption, hashing",
    "object": "object-oriented programming, class system, inheritance",
    "testing": "test framework, test runner, assertions",
    "debug": "debugging, profiling, introspection",
    "async": "asynchronous I/O, coroutines, concurrency",
    "socket": "socket programming, TCP/UDP networking",
    "template": "template engine, text rendering, markup",
    "logging": "logging, log management, diagnostics",
    "math": "mathematics, numerical computing, arithmetic",
    "string": "string manipulation, text processing, pattern matching",
    "file": "file system operations, file I/O, path handling",
    "date": "date, time, timezone handling",
    "compression": "data compression, encoding, archive handling",
    "image": "image processing, graphics, visual rendering",
    "audio": "audio processing, sound, multimedia",
    "game": "game development, game engine, interactive media",
    "gui": "graphical user interface, windowing, widgets",
    "cli": "command-line interface, terminal, console",
    "parser": "parsing, lexing, grammar processing",
    "serialization": "data serialization, encoding, marshalling",
    "validation": "input validation, data verification, schema checking",
    "uuid": "unique identifier generation, UUID",
    "redis": "Redis client, in-memory data store, caching",
    "openssl": "TLS/SSL, X.509 certificates, cryptographic operations",
    "zeromq": "message queue, distributed messaging, ZeroMQ",
    "irc": "IRC protocol, chat client, messaging",
    "email": "email sending, SMTP, mail handling",
    "ffi": "foreign function interface, C binding, native interop",
    "bitwise": "bit manipulation, bitwise operations, binary data",
    "i18n": "internationalization, localization, translation",
    "spreadsheet": "spreadsheet processing, tabular data, delimited files",
    "neovim": "Neovim plugin, editor extension, IDE tooling",
    "nvim": "Neovim plugin, editor extension, IDE tooling",
    "kong": "Kong API gateway, middleware, plugin",
    "nginx": "Nginx module, OpenResty, web server extension",
    "resty": "OpenResty module, Nginx Lua, web server scripting",
    "love": "LÖVE2D game framework, 2D game development",
}


def validate_phases(phases, rock_name):
    """Validates LLM output against hallucination patterns."""
    for key in ["phase1", "phase2", "phase3"]:
        val = phases.get(key, "")
        if not val or val.strip().lower() == "none" or len(val.strip()) < 10:
            return False
        # Check for Python library names
        val_lower = val.lower()
        for blacklisted in PYTHON_BLACKLIST:
            if blacklisted in val_lower:
                print(f"  ⚠ BLOCKED hallucination in {key}: found '{blacklisted}' → retrying")
                return False
    return True


def build_fallback_phases(rock_data):
    """Deterministic fallback: build phases from summary, tags, raw_content."""
    rock_name = rock_data.get("rock_name", "Unknown")
    summary = rock_data.get("summary", "").strip()
    tags = rock_data.get("tags", [])
    raw_content = rock_data.get("raw_content", "")

    # Phase 1: Functional description from summary or first paragraph
    if summary and len(summary) > 20:
        phase1 = f"{rock_name} is a Lua library that {summary[:200].rstrip('.')}"
    else:
        # Extract first meaningful paragraph from raw_content
        lines = [l.strip() for l in raw_content.split("\n") if l.strip() and not l.startswith(("!", "[", "#", "```", "---", "==="))]
        first_para = " ".join(lines[:3])[:250]
        phase1 = f"{rock_name} is a Lua library: {first_para}"

    # Phase 2: Implementation details from raw_content patterns
    impl_details = []
    content_lower = raw_content.lower()
    if "pure lua" in content_lower:
        impl_details.append("Pure Lua implementation")
    if "luajit" in content_lower:
        impl_details.append("LuaJIT compatible")
    if "ffi" in content_lower and "luajit" in content_lower:
        impl_details.append("uses FFI bindings")
    if "lua 5.1" in content_lower or "lua 5.2" in content_lower or "lua 5.3" in content_lower or "lua 5.4" in content_lower:
        versions = re.findall(r'[Ll]ua\s*5\.[1-4]', raw_content)
        if versions:
            impl_details.append(f"supports {', '.join(set(versions))}")
    if any(x in content_lower for x in ["written in c", "pure c", "c library", "c binding", "c module"]):
        impl_details.append("C native binding")
    if "openresty" in content_lower or "ngx" in content_lower:
        impl_details.append("OpenResty/Nginx module")
    if "luarocks" in content_lower:
        impl_details.append("installable via LuaRocks")

    phase2 = f"Implemented as {', '.join(impl_details)}" if impl_details else f"{rock_name} is a Lua module installable via LuaRocks"

    # Phase 3: Domain from tags
    domains = []
    for tag in tags:
        tag_lower = tag.lower()
        if tag_lower in TAG_DOMAIN_MAP:
            domains.append(TAG_DOMAIN_MAP[tag_lower])
        else:
            domains.append(tag_lower)
    phase3 = f"Used in the domain of {', '.join(domains)}" if domains else f"General purpose Lua utility library"

    return {
        "phase1": phase1,
        "phase2": phase2,
        "phase3": phase3,
    }


def generate_dna_description(rock_data, attempt=1):
    """Generate 3 descriptive phases via LLM with anti-hallucination validation."""
    rock_name = rock_data.get("rock_name", "Unknown")
    tags = ", ".join(rock_data.get("tags", []))
    summary = rock_data.get("summary", "")
    raw_content = rock_data.get("raw_content", "")[:3500]

    prompt = f"""You are a Lua library documentation expert. Your task is to write exactly 3 descriptive English phrases about the Lua library '{rock_name}'.

### ABSOLUTE RULES:
1. Use ONLY information from the README text below. Do NOT invent features.
2. NEVER mention Python libraries (NumPy, Pandas, Requests, FastAPI, SQLAlchemy, etc.)
3. Each phase MUST be a COMPLETE DESCRIPTIVE SENTENCE (15-40 words), NOT comma-separated keywords.
4. Focus exclusively on what THIS Lua library does.

### EXAMPLES OF GOOD OUTPUT:
For a CSV parser library:
{{"phase1": "A Lua module for reading and parsing delimited text files including CSV and tab-separated formats with automatic separator detection",
  "phase2": "Implemented in pure Lua with iterator-based line reading, supports Lua 5.1, 5.2 and LuaJIT, with configurable buffer sizes",
  "phase3": "Used for data processing tasks involving tabular file formats, spreadsheet data import, and structured text file handling"}}

For an OOP library:
{{"phase1": "A lightweight object-oriented programming system for Lua providing class definitions, single inheritance, and mixin support",
  "phase2": "Written in pure Lua with metamethod support for operator overloading, class variables, and method chaining",
  "phase3": "Used as a foundational library for structuring Lua applications with classes, enabling code reuse through inheritance and mixins"}}

### DATA TO ANALYZE:
Name: {rock_name}
Tags: {tags}
Summary: {summary}
README:
{raw_content}

### OUTPUT (valid JSON only, no markdown, no explanation):"""

    temperature = 0.1 if attempt == 1 else 0.3

    try:
        payload = {
            "model": LOCAL_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "temperature": temperature,
            "max_tokens": 400,
        }
        response = requests.post(
            f"{LOCAL_API_URL}/chat/completions", json=payload, timeout=120
        )
        if response.status_code == 200:
            raw_content_resp = (
                response.json()["choices"][0]["message"]["content"].strip()
            )
            # Extract JSON from response
            match = re.search(r"\{.*\}", raw_content_resp, re.DOTALL)
            if match:
                clean_json = match.group(0).replace("\n", " ").replace("\r", " ")
                phases = json.loads(clean_json)

                if validate_phases(phases, rock_name):
                    return phases
                elif attempt < 2:
                    print(f"  ↻ Retry {rock_name} (attempt {attempt+1})...")
                    return generate_dna_description(rock_data, attempt + 1)
                else:
                    print(f"  ⚡ Fallback for {rock_name} after {attempt} failed attempts")
                    return build_fallback_phases(rock_data)
            else:
                if attempt < 2:
                    return generate_dna_description(rock_data, attempt + 1)
                return build_fallback_phases(rock_data)
        else:
            print(f"  HTTP {response.status_code} for {rock_name}")
            return build_fallback_phases(rock_data)
    except Exception as e:
        print(f"  Error processing {rock_name}: {e}")
        return build_fallback_phases(rock_data)


def process_files():
    # Clean old index to force rebuild
    if os.path.exists("index.faiss"):
        os.remove("index.faiss")
    if os.path.exists("master_index.json"):
        os.remove("master_index.json")

    files = glob.glob("raw_data/*.json")
    print(f"═══ Generating DNA descriptions for {len(files)} libraries ═══\n")

    stats = {"ok": 0, "fallback": 0, "fail": 0}

    for i, file_path in enumerate(files, 1):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        rock_name = data.get("rock_name", os.path.basename(file_path))
        print(f"[{i}/{len(files)}] {rock_name}...", end=" ")

        dna_data = generate_dna_description(data)

        if dna_data and all(k in dna_data for k in ["phase1", "phase2", "phase3"]):
            data["phase1"] = dna_data["phase1"]
            data["phase2"] = dna_data["phase2"]
            data["phase3"] = dna_data["phase3"]

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            # Check if it was a fallback
            if dna_data["phase1"].startswith(f"{rock_name} is a Lua library"):
                stats["fallback"] += 1
                print("OK (fallback)")
            else:
                stats["ok"] += 1
                print("OK (LLM)")
        else:
            stats["fail"] += 1
            print("FAIL")

    print(f"\n═══ RESULTS ═══")
    print(f"  LLM OK:    {stats['ok']}")
    print(f"  Fallback:  {stats['fallback']}")
    print(f"  Failed:    {stats['fail']}")
    print(f"  Total:     {len(files)}")


if __name__ == "__main__":
    process_files()
