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
    Uses greedy extraction to find the outermost { ... }.
    Falls back to an empty dict on failure.
    """
    raw = chat(prompt, system=system, temperature=temperature,
               max_tokens=max_tokens)

    # Greedy match outermost JSON object
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not match:
        print(f"  [!] LLM returned no JSON. Raw:\n{raw[:300]}")
        return {}

    json_str = match.group(0)
    # Clean common model artifacts
    json_str = json_str.replace("`", '"')
    json_str = re.sub(r"//.*", "", json_str)  # Remove JS-style comments

    try:
        return json.loads(json_str, strict=False)
    except json.JSONDecodeError as e:
        print(f"  [!] JSON parse fail: {e}\n  Raw: {json_str[:300]}")
        return {}
