"""
chunker.py — Map-Reduce text splitter for large files.

Strategy:
  1. SPLIT: Divide source text into overlapping chunks (~3000 tokens each,
     with ~300 token overlap) so nothing falls through the cracks.
  2. MAP:   The caller processes each chunk independently (summarize,
     extract entities, etc.).
  3. REDUCE: The caller merges results across all chunks.

Token estimation: 1 token ≈ 4 characters (conservative for English text).
"""

import re
from typing import List


# ── Configuration ─────────────────────────────────────────────────────
CHARS_PER_TOKEN = 4
DEFAULT_MAX_CHUNK_TOKENS = 3000
DEFAULT_OVERLAP_TOKENS = 300


def estimate_tokens(text: str) -> int:
    """Rough token count based on character length."""
    return len(text) // CHARS_PER_TOKEN


def needs_chunking(text: str, max_tokens: int = DEFAULT_MAX_CHUNK_TOKENS) -> bool:
    """Check if a text exceeds the chunk threshold."""
    return estimate_tokens(text) > max_tokens


def split_into_chunks(
    text: str,
    max_tokens: int = DEFAULT_MAX_CHUNK_TOKENS,
    overlap_tokens: int = DEFAULT_OVERLAP_TOKENS,
) -> List[dict]:
    """
    Split text into overlapping chunks.

    Returns a list of dicts:
      [{"index": 0, "text": "...", "tokens_est": 1234, "is_first": True, "is_last": False}, ...]

    The split strategy:
    1. Try to split at paragraph boundaries (double newlines).
    2. If a paragraph is too large, split at sentence boundaries.
    3. If a sentence is too large, hard-split at the character limit.
    """
    if not needs_chunking(text, max_tokens):
        return [{
            "index": 0,
            "text": text,
            "tokens_est": estimate_tokens(text),
            "is_first": True,
            "is_last": True,
        }]

    max_chars = max_tokens * CHARS_PER_TOKEN
    overlap_chars = overlap_tokens * CHARS_PER_TOKEN

    # Split into paragraphs first
    paragraphs = re.split(r"\n\s*\n", text)

    chunks = []
    current_text = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # Would adding this paragraph exceed the limit?
        if len(current_text) + len(para) + 2 > max_chars:
            if current_text:
                # Save current chunk
                chunks.append(current_text.strip())

                # Start next chunk with overlap from the end of current
                overlap_start = max(0, len(current_text) - overlap_chars)
                current_text = current_text[overlap_start:] + "\n\n" + para
            else:
                # Single paragraph is too big — split by sentences
                sentences = _split_paragraph_into_sentences(para)
                sub_chunks = _merge_sentences(sentences, max_chars, overlap_chars)
                chunks.extend(sub_chunks[:-1])
                current_text = sub_chunks[-1] if sub_chunks else ""
        else:
            current_text = current_text + "\n\n" + para if current_text else para

    if current_text.strip():
        chunks.append(current_text.strip())

    # Build output dicts
    result = []
    for i, chunk_text in enumerate(chunks):
        result.append({
            "index": i,
            "text": chunk_text,
            "tokens_est": estimate_tokens(chunk_text),
            "is_first": (i == 0),
            "is_last": (i == len(chunks) - 1),
        })

    return result


def _split_paragraph_into_sentences(text: str) -> List[str]:
    """Split a large paragraph into sentences."""
    # Split on sentence-ending punctuation followed by whitespace
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if p.strip()]


def _merge_sentences(
    sentences: List[str], max_chars: int, overlap_chars: int
) -> List[str]:
    """Merge sentences into chunks respecting the size limit."""
    chunks = []
    current = ""

    for sent in sentences:
        if len(current) + len(sent) + 1 > max_chars:
            if current:
                chunks.append(current.strip())
                # Overlap: take the tail of current
                overlap_start = max(0, len(current) - overlap_chars)
                current = current[overlap_start:] + " " + sent
            else:
                # Single sentence exceeds limit — hard split
                while len(sent) > max_chars:
                    chunks.append(sent[:max_chars])
                    sent = sent[max_chars - overlap_chars:]
                current = sent
        else:
            current = current + " " + sent if current else sent

    if current.strip():
        chunks.append(current.strip())

    return chunks
