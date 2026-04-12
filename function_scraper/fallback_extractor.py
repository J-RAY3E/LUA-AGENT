"""
fallback_extractor.py — Phase 6: Regex-based static fallback extraction.

Applied when LLM extraction fails or returns empty. Detects:
  - function module.name(args)
  - local function name(args)
  - --- @function module.name
  - --- @param / --- @return annotations
"""

import re
from pathlib import Path

from config import logger


class FallbackExtractor:
    """Regex-based function extraction from raw .lua files."""

    _GLOBAL_FUNC = re.compile(
        r"function\s+([A-Za-z0-9_.:\[\]]+)\s*\(([^)]*)\)", re.MULTILINE
    )
    _LOCAL_FUNC = re.compile(
        r"local\s+function\s+([A-Za-z0-9_]+)\s*\(([^)]*)\)", re.MULTILINE
    )
    _LDOC_FUNC = re.compile(
        r"---\s*@function\s+([A-Za-z0-9_.]+)", re.MULTILINE
    )
    _EMMYLUA_PARAM = re.compile(
        r"---\s*@param\s+(\w+)\s+(\S+)(?:\s+(.+))?", re.MULTILINE
    )
    _EMMYLUA_RETURN = re.compile(
        r"---\s*@return\s+(\S+)(?:\s+(.+))?", re.MULTILINE
    )

    def extract(self, content_dir: Path) -> list[dict[str, str]]:
        """Extract function signatures from .lua files in content_dir."""
        all_funcs: list[dict[str, str]] = []
        seen: set[str] = set()

        for lua_file in content_dir.rglob("*.lua"):
            try:
                content = lua_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            rel_path = str(lua_file.relative_to(content_dir))

            # @function annotations
            for match in self._LDOC_FUNC.finditer(content):
                name = match.group(1)
                if name in seen:
                    continue
                seen.add(name)
                line_no = content[:match.start()].count("\n") + 1
                params, returns = self._nearby_annotations(content, match.start())
                all_funcs.append({
                    "name": name,
                    "input_format": params or "Extracted via static fallback - verify manually",
                    "output_format": returns or "Extracted via static fallback - verify manually",
                    "description": "Extracted via static fallback - verify manually",
                    "extraction_method": "static_fallback",
                    "source_ref": f"{rel_path}:{line_no}",
                })

            # Global functions
            for match in self._GLOBAL_FUNC.finditer(content):
                name = match.group(1)
                if name in seen:
                    continue
                seen.add(name)
                params_raw = match.group(2).strip()
                line_no = content[:match.start()].count("\n") + 1
                _, returns = self._nearby_annotations(content, match.start())
                all_funcs.append({
                    "name": name,
                    "input_format": self._format_params(params_raw),
                    "output_format": returns or "Extracted via static fallback - verify manually",
                    "description": "Extracted via static fallback - verify manually",
                    "extraction_method": "static_fallback",
                    "source_ref": f"{rel_path}:{line_no}",
                })

            # Local functions
            for match in self._LOCAL_FUNC.finditer(content):
                name = match.group(1)
                if name in seen:
                    continue
                seen.add(name)
                params_raw = match.group(2).strip()
                line_no = content[:match.start()].count("\n") + 1
                _, returns = self._nearby_annotations(content, match.start())
                all_funcs.append({
                    "name": name,
                    "input_format": self._format_params(params_raw),
                    "output_format": returns or "Extracted via static fallback - verify manually",
                    "description": "Extracted via static fallback - verify manually",
                    "extraction_method": "static_fallback",
                    "source_ref": f"{rel_path}:{line_no}",
                })

        if all_funcs:
            logger.info("Fallback found %d functions in %s", len(all_funcs), content_dir.name)
        return all_funcs

    def _format_params(self, params_str: str) -> str:
        """Convert parameter list to human-readable string."""
        if not params_str:
            return "no arguments"
        params = [p.strip() for p in params_str.split(",") if p.strip()]
        parts = []
        for p in params:
            if p == "...":
                parts.append("... (varargs)")
            elif p == "self":
                parts.append("self (implicit)")
            else:
                parts.append(p)
        return ", ".join(parts)

    def _nearby_annotations(self, content: str, pos: int) -> tuple[str, str]:
        """Look for EmmyLua/LDoc annotations above a function definition."""
        block = content[max(0, pos - 500):pos]

        params = []
        for m in self._EMMYLUA_PARAM.finditer(block):
            name, typ = m.group(1), m.group(2)
            desc = m.group(3) or ""
            params.append(f"{name}: {typ}" + (f" — {desc}" if desc else ""))

        returns = []
        for m in self._EMMYLUA_RETURN.finditer(block):
            ret_type = m.group(1)
            desc = m.group(2) or ""
            returns.append(f"{ret_type}" + (f" — {desc}" if desc else ""))

        return "; ".join(params), "; ".join(returns)
