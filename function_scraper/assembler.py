"""
assembler.py — Phase 7: Output assembly and storage.

Produces:
  output/<key>.json               — structured per-module result
  output/all_libs_consolidated.jsonl — append-only JSONL stream
"""

import json
from typing import Any

from config import CONFIG, logger
from scraper import ModuleInfo
from utils import safe_dirname


class OutputAssembler:
    """Aggregates extracted functions per library and writes validated JSON."""

    def __init__(self) -> None:
        self._output_dir = CONFIG["output_dir"]
        self._output_dir.mkdir(parents=True, exist_ok=True)
        self._consolidated = self._output_dir / "all_libs_consolidated.jsonl"

    def assemble(self, module_info: ModuleInfo, functions: list[dict[str, str]]) -> None:
        """Assemble and write output for a module."""
        lib_name = module_info.module_name

        # Build functions dict keyed by name (deduplicated)
        func_dict: dict[str, dict[str, str]] = {}
        for func in functions:
            name = func.get("name", "unknown")
            if name not in func_dict:
                func_dict[name] = {
                    "name_funct": name,
                    "input_format": func.get("input_format", ""),
                    "output_format": func.get("output_format", ""),
                    "description": func.get("description", ""),
                    "extraction_method": func.get("extraction_method", ""),
                    "source_ref": func.get("source_ref", ""),
                }

        output: dict[str, Any] = {
            lib_name: {
                "version": module_info.version,
                "source_homepage": module_info.homepage_url,
                "functions": func_dict,
            }
        }

        # Validate JSON roundtrip before writing
        try:
            serialized = json.dumps(output, indent=2, ensure_ascii=False)
            json.loads(serialized)
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            logger.error("JSON validation failed for %s: %s", module_info.key, exc)
            return

        # Write per-module JSON
        filename = safe_dirname(module_info.author, module_info.module_name, module_info.version)
        out_path = self._output_dir / f"{filename}.json"
        out_path.write_text(serialized, encoding="utf-8")

        # Append to consolidated JSONL
        with open(self._consolidated, "a", encoding="utf-8") as f:
            f.write(json.dumps(output, ensure_ascii=False) + "\n")

        llm_n = sum(1 for v in func_dict.values() if v["extraction_method"] == "llm")
        fb_n = sum(1 for v in func_dict.values() if v["extraction_method"] == "static_fallback")
        logger.info(
            "Output %s: %d functions (%d LLM, %d fallback) → %s",
            lib_name, len(func_dict), llm_n, fb_n, out_path.name,
        )
