"""
llm_client.py — Shared LLM client for the Wiki Brain.
Talks to a local OpenAI-compatible endpoint (LM Studio, Ollama, etc.).
"""

import requests
import json
import re
import os
import yaml


# ── Load config from schema ──────────────────────────────────────────────
_SCHEMA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "config", "wiki_schema.yaml"
)

def _load_llm_config():
    """Load LLM settings from wiki_schema.yaml, with env-var overrides."""
    defaults = {
        "api_url": "http://localhost:8080/v1",
        "model": "Volko76/Qwen2.5-1.5B-Instruct-Q5_K_M-GGUF:Q5_K_M",
        "temperature": 0.1,
        "max_tokens": 2048,
        "timeout": 120,
    }
    try:
        with open(_SCHEMA_PATH, "r", encoding="utf-8") as f:
            schema = yaml.safe_load(f)
        cfg = schema.get("llm", {})
        for k, v in cfg.items():
            defaults[k] = v
    except Exception:
        pass

    # Environment overrides always win
    defaults["api_url"] = os.getenv("LOCAL_LLM_URL", defaults["api_url"])
    defaults["model"] = os.getenv("LOCAL_LLM_MODEL", defaults["model"])
    return defaults


_CFG = _load_llm_config()


def chat(prompt: str, system: str = None, temperature: float = None,
         max_tokens: int = None) -> str:
    """
    Send a chat completion request to the local LLM.

    Returns the raw response text (stripped).
    Raises RuntimeError on HTTP errors or timeouts.
    """
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": _CFG["model"],
        "messages": messages,
        "stream": False,
        "temperature": temperature if temperature is not None else _CFG["temperature"],
        "max_tokens": max_tokens or _CFG["max_tokens"],
    }

    resp = requests.post(
        f"{_CFG['api_url']}/chat/completions",
        json=payload,
        timeout=_CFG["timeout"],
    )

    if resp.status_code != 200:
        raise RuntimeError(f"LLM HTTP {resp.status_code}: {resp.text[:200]}")

    content = resp.json()["choices"][0]["message"].get("content", "")

    # Strip <think>...</think> tags from reasoning models (DeepSeek-R1, etc.)
    content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL)

    return content.strip()


def chat_json(prompt: str, system: str = None, temperature: float = None,
              max_tokens: int = None) -> dict:
    """
    Like chat(), but parses the response as JSON.
    Uses multiple strategies to find valid JSON.
    Falls back to an empty dict on failure.
    """
    raw = chat(prompt, system=system, temperature=temperature,
               max_tokens=max_tokens)

    # Strategy 1: Look for ```json ... ``` blocks (most reliable)
    json_str = ""
    code_block_match = re.search(r"```json\s*(\{[\s\S]*?\})\s*```", raw, re.DOTALL)
    if code_block_match:
        json_str = code_block_match.group(1)
    else:
        # Strategy 2: Find first { and last } with proper nesting
        start = raw.find('{')
        if start != -1:
            # Find matching closing brace
            depth = 0
            for i in range(start, len(raw)):
                if raw[i] == '{':
                    depth += 1
                elif raw[i] == '}':
                    depth -= 1
                    if depth == 0:
                        json_str = raw[start:i+1]
                        break
    
    # Strategy 3: Fallback to any {...} pattern (take longest match)
    if not json_str:
        matches = re.findall(r'\{[\s\S]*\}', raw)
        if matches:
            # Take the longest match (most likely to be complete)
            json_str = max(matches, key=len)
        else:
            print(f"  [!] LLM returned no JSON. Raw:\n{raw[:300]}")
            return {}

    # Clean common model artifacts
    json_str = json_str.replace("```", "").strip()
    
    # Fix literal newlines INSIDE JSON strings (critical for descriptions)
    in_string = False
    escaped = False
    fixed_chars = []
    for char in json_str:
        if char == '"' and not escaped:
            in_string = not in_string
        if char == '\\' and not escaped:
            escaped = True
        else:
            escaped = False
            
        if char == '\n' and in_string:
            fixed_chars.append('\\')
            fixed_chars.append('n')
        elif char == '\r' and in_string:
            pass  # Ignore \r inside strings
        else:
            fixed_chars.append(char)
    
    json_str = "".join(fixed_chars)

    # Try to parse
    try:
        return json.loads(json_str, strict=False)
    except json.JSONDecodeError as e:
        # Last resort: try to salvage by fixing common quote issues in descriptions
        try:
            # Simple heuristic: replace unescaped quotes that look like they're in text values
            # Look for patterns like : "... text with "quotes" ... " and escape inner quotes
            
            # This is a simplified fixer for common cases
            # Replace quotes that appear after : " and before the final "
            def fix_description_quotes(s):
                # Find all "key": "value" patterns
                result = ""
                i = 0
                while i < len(s):
                    if s[i:i+2] == '":' and i+2 < len(s):
                        result += s[i:i+2]
                        i += 2
                        # Skip whitespace
                        while i < len(s) and s[i] in ' \t\n\r':
                            result += s[i]
                            i += 1
                        # Expect opening quote
                        if i < len(s) and s[i] == '"':
                            result += '"'
                            i += 1
                            # Process until closing quote
                            while i < len(s) and s[i] != '"':
                                if s[i] == '\\' and i+1 < len(s):
                                    result += s[i:i+2]
                                    i += 2
                                else:
                                    result += s[i]
                                    i += 1
                            # Add closing quote
                            if i < len(s) and s[i] == '"':
                                result += '"'
                                i += 1
                        else:
                            # Malformed, just copy
                            result += s[i]
                            i += 1
                return result
            
            json_str_fixed = fix_description_quotes(json_str)
            if json_str_fixed != json_str:
                return json.loads(json_str_fixed, strict=False)
        except:
            pass  # If fixing fails, continue to error
        
        print(f"  [!] JSON parse fail: {e}\n  Raw: {json_str[:500]}")
        return {}
