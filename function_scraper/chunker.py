"""
chunker.py — Phase 4: Semantic chunking of documentation and source code.

Primary split:   Markdown headers (^#{1,3} )
Secondary split: Lua function blocks
Overlap:         ~300 chars from previous chunk appended for context continuity
"""

import re
from dataclasses import dataclass, asdict
from pathlib import Path

from config import CONFIG, logger


@dataclass
class Chunk:
    """A semantically meaningful text chunk with source metadata."""
    text: str
    source_file: str
    line_range: str
    section_header: str
    rock_id: str = "unknown"

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


class Chunker:
    """Splits aggregated documentation/source into processing chunks."""

    def __init__(self) -> None:
        self._max_chars: int = CONFIG["max_chunk_chars"]
        self._overlap: int = CONFIG["chunk_overlap_chars"]

    def chunk(self, content_dir: Path, rock_id: str) -> list[Chunk]:
        """Chunk all content files in a directory."""
        all_chunks: list[Chunk] = []

        files = sorted(content_dir.rglob("*"), key=self._file_priority)

        for filepath in files:
            if not filepath.is_file():
                continue
            if filepath.suffix.lower() not in (".md", ".txt", ".rst", ".lua"):
                continue
            if filepath.name == "metadata.json":
                continue

            try:
                content = filepath.read_text(encoding="utf-8", errors="replace")
            except Exception as exc:
                logger.debug("Cannot read %s: %s", filepath, exc)
                continue

            if len(content.strip()) < 20:
                continue

            rel_path = str(filepath.relative_to(content_dir))

            if filepath.suffix.lower() == ".lua":
                chunks = self._chunk_lua(content, rel_path, rock_id)
            else:
                chunks = self._chunk_markdown(content, rel_path, rock_id)

            all_chunks.extend(chunks)

        logger.info("Created %d chunks for %s from %s", len(all_chunks), rock_id, content_dir.name)
        return all_chunks

    def _file_priority(self, path: Path) -> tuple[int, str]:
        """README first, then docs, then source."""
        name = path.name.lower()
        if name.startswith("readme"):
            return (0, name)
        if path.suffix.lower() in (".md", ".rst"):
            return (1, name)
        if path.suffix.lower() == ".txt":
            return (2, name)
        return (3, name)

    def _chunk_markdown(self, text: str, source_file: str, rock_id: str) -> list[Chunk]:
        """Split by markdown headers, then enforce max chunk size."""
        sections = re.split(r"(?=^#{1,3}\s)", text, flags=re.MULTILINE)
        chunks: list[Chunk] = []
        prev_tail = ""

        for i, section in enumerate(sections):
            section = section.strip()
            if not section:
                continue

            header_match = re.match(r"^(#{1,3}\s+.+?)$", section, re.MULTILINE)
            header = header_match.group(1).strip() if header_match else f"Section {i+1}"

            full_text = prev_tail + section if prev_tail else section
            chunks.extend(self._enforce_max_size(full_text, source_file, header, rock_id))
            prev_tail = section[-self._overlap:] + "\n" if len(section) > self._overlap else ""

        return chunks

    def _chunk_lua(self, text: str, source_file: str, rock_id: str) -> list[Chunk]:
        """Split by function definitions."""
        pattern = re.compile(
            r"((?:---[^\n]*\n)*(?:local\s+)?function\s+[A-Za-z0-9_.:\[\]]+\s*\([^)]*\))",
            re.MULTILINE,
        )
        boundaries = [m.start() for m in pattern.finditer(text)]

        if not boundaries:
            return self._enforce_max_size(text, source_file, f"File: {source_file}", rock_id)

        chunks: list[Chunk] = []
        prev_tail = ""

        for idx, start in enumerate(boundaries):
            end = boundaries[idx + 1] if idx + 1 < len(boundaries) else len(text)
            block = text[start:end].strip()
            if not block:
                continue

            fn_match = re.match(r"(?:local\s+)?function\s+([A-Za-z0-9_.:\[\]]+)", block)
            header = f"function {fn_match.group(1)}" if fn_match else f"Block {idx+1}"

            full_text = prev_tail + block if prev_tail else block
            chunks.extend(self._enforce_max_size(full_text, source_file, header, rock_id))
            prev_tail = block[-self._overlap:] + "\n" if len(block) > self._overlap else ""

        return chunks

    def _enforce_max_size(self, text: str, source_file: str, header: str, rock_id: str) -> list[Chunk]:
        """Split text into chunks ≤ max_chunk_chars with overlap."""
        if len(text) <= self._max_chars:
            return [Chunk(
                text=text, source_file=source_file,
                line_range=f"1-{text.count(chr(10)) + 1}",
                section_header=header,
                rock_id=rock_id,
            )]

        chunks: list[Chunk] = []
        start = 0
        part = 1

        while start < len(text):
            end = start + self._max_chars
            if end >= len(text):
                segment = text[start:]
            else:
                nl_pos = text.rfind("\n", start + self._max_chars // 2, end)
                if nl_pos > start:
                    end = nl_pos + 1
                segment = text[start:end]

            chunks.append(Chunk(
                text=segment, source_file=source_file,
                line_range=f"part_{part}",
                section_header=f"{header} (part {part})",
                rock_id=rock_id,
            ))
            start = end - self._overlap
            part += 1

        return chunks
