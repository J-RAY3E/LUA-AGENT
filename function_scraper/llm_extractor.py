"""
llm_extractor.py — Phase 5: LLM-based function extraction.

Uses OpenAI-compatible /v1/chat/completions endpoint (works with llama.cpp,
Ollama /v1, LiteLLM, or any compatible server).

Retries once with temperature=0 on parse failure before deferring to fallback.
"""

import json
import re
from typing import Optional

import requests

from config import CONFIG, logger
from chunker import Chunk

_FUNC_SCHEMA_KEYS = {"name", "input_format", "output_format", "description"}

LLM_PROMPT = """You are an expert Lua developer and technical documentation analyzer. 
Extract all functions, methods, or modules from the provided text (which could be source code or documentation).

Each object must follow this strict JSON schema:
{
  "name": "exact function name (e.g., module.func or global_func)",
  "input_format": "description of expected arguments (types, names, optionality)",
  "output_format": "description of return values (types, structure, or multiple returns)",
  "description": "concise summary of purpose and side effects (max 2 sentences)"
}

Rules:
1. INFERS types and structures from context/comments if not explicitly stated.
2. If the text is source code, look at function parameters and return statements.
3. If the text is documentation, look for signature blocks or usage examples.
4. Return ONLY a valid JSON array. If no functions are found, return [].

Text to process:
{chunk_text}"""


class LLMExtractor:
    """Extracts function signatures from chunks via OpenAI-compatible LLM endpoint.

    Endpoint: CONFIG["llm_api_url"] + "/chat/completions"
    Model:    CONFIG["llm_model"]
    """

    def __init__(self) -> None:
        self._api_url: str = CONFIG["llm_api_url"].rstrip("/")
        self._model: str = CONFIG["llm_model"]

    def extract(self, chunk: Chunk) -> list[dict[str, str]]:
        """Extract function entries from a chunk. Returns validated list or []."""
        prompt = LLM_PROMPT.replace("{chunk_text}", chunk.text)

        # Attempt 1: normal temperature
        result = self._call_llm(prompt, temperature=CONFIG["llm_temperature"])
        if result is not None:
            if result == []:
                logger.info("[%s] LLM determined NO functions exist in: %s / %s", chunk.rock_id, chunk.source_file, chunk.section_header)
                return []
            validated = self._validate(result, chunk)
            if validated:
                return validated

        # Attempt 2: temperature=0
        logger.debug("[%s] LLM retry (temp=0) for: %s", chunk.rock_id, chunk.section_header)
        result = self._call_llm(prompt, temperature=0.0)
        if result is not None:
            if result == []:
                logger.info("[%s] LLM determined NO functions exist in: %s / %s", chunk.rock_id, chunk.source_file, chunk.section_header)
                return []
            validated = self._validate(result, chunk)
            if validated:
                return validated

        logger.warning("[%s] LLM formatting or extraction failed heavily for: %s / %s", chunk.rock_id, chunk.source_file, chunk.section_header)
        return []

    def _call_llm(self, prompt: str, temperature: float) -> Optional[list[dict]]:
        """Send prompt to OpenAI-compatible /v1/chat/completions endpoint."""
        payload = {
            "model": self._model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "temperature": temperature,
            "max_tokens": CONFIG["llm_max_tokens"],
        }

        try:
            resp = requests.post(
                f"{self._api_url}/chat/completions",
                json=payload,
                timeout=120,
            )
            if resp.status_code != 200:
                logger.warning("LLM HTTP %d: %s", resp.status_code, resp.text[:200])
                return None

            message = resp.json()["choices"][0]["message"]
            content = (message.get("content") or "").strip()

            # Handle DeepSeek-R1 models that put thinking in reasoning_content
            # and might leave content empty on token limit.
            if not content:
                reasoning = (message.get("reasoning_content") or "").strip()
                if reasoning:
                    content = reasoning

            if not content:
                return []

            # Strip <think>...</think> tags if present (R1 format)
            content_clean = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
            if not content_clean:
                content_clean = content

            # Clean markdown fencing
            if content_clean.startswith("```json"):
                content_clean = content_clean.replace("```json", "", 1).replace("```", "").strip()
            elif content_clean.startswith("```"):
                content_clean = content_clean.replace("```", "", 1).replace("```", "").strip()

            # Extract JSON from possible surrounding text
            if "{" in content_clean or "[" in content_clean:
                # Find the outermost JSON structure
                bracket_start = -1
                for i, ch in enumerate(content_clean):
                    if ch in ("[", "{"):
                        bracket_start = i
                        break
                if bracket_start >= 0:
                    closing = "]" if content_clean[bracket_start] == "[" else "}"
                    bracket_end = content_clean.rfind(closing)
                    if bracket_end > bracket_start:
                        content_clean = content_clean[bracket_start:bracket_end + 1]

            try:
                parsed = json.loads(content_clean, strict=False)
            except json.JSONDecodeError as exc:
                # Fallback purely using regex if the structure is broken
                match = re.search(r'\[.*\]', content_clean, re.DOTALL)
                if match:
                    try:
                        parsed = json.loads(match.group(0), strict=False)
                    except json.JSONDecodeError:
                        logger.debug("JSON decode error: %s on content: %s", exc, content_clean[:100])
                        return None
                else:
                    logger.debug("JSON decode error: %s on content: %s", exc, content_clean[:100])
                    return None

            # Normalize to list
            if isinstance(parsed, dict):
                for key in ("functions", "result", "data", "items"):
                    if key in parsed and isinstance(parsed[key], list):
                        return parsed[key]
                if "name" in parsed:
                    return [parsed]
                return []

            if isinstance(parsed, list):
                return parsed

            return []

        except json.JSONDecodeError as exc:
            logger.debug("JSON decode error: %s", exc)
            return None
        except requests.RequestException as exc:
            logger.error("LLM connection error: %s", exc)
            return None
        except Exception as exc:
            logger.error("Unexpected LLM error: %s", exc)
            return None

    def _validate(self, items: list[dict], chunk: Chunk) -> list[dict[str, str]]:
        """Validate schema + annotate with extraction metadata."""
        validated: list[dict[str, str]] = []

        for item in items:
            if not isinstance(item, dict):
                continue
            if "name" not in item or not item["name"]:
                continue

            validated.append({
                "name": str(item.get("name", "")),
                "input_format": str(item.get("input_format", "") or ""),
                "output_format": str(item.get("output_format", "") or ""),
                "description": str(item.get("description", "") or ""),
                "extraction_method": "llm",
                "source_ref": f"{chunk.source_file}#{chunk.section_header}",
            })

        return validated
