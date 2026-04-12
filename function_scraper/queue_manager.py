"""
queue_manager.py — Phase 2: File-backed processed manifest for idempotency.

ProcessedManifest tracks which (author, module, version) combos have been
completed so the pipeline can be restarted without re-processing.

Thread-safe inter-stage communication uses stdlib queue.Queue (see pipeline.py).
"""

import json
import threading
import time
from pathlib import Path

from config import CONFIG, logger


class ProcessedManifest:
    """Thread-safe file-backed manifest of processed module keys.

    Each line in processed.jsonl is: {"key": "author__module__version", "timestamp": ...}
    """

    def __init__(self) -> None:
        self._path: Path = CONFIG["processed_file"]
        self._lock = threading.Lock()
        self._keys: set[str] = set()
        self._load()

    def _load(self) -> None:
        """Load already-processed keys from disk."""
        if not self._path.exists():
            return
        with open(self._path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    self._keys.add(obj.get("key", ""))
                except json.JSONDecodeError:
                    continue
        logger.info("Loaded %d processed keys from manifest", len(self._keys))

    def is_processed(self, key: str) -> bool:
        """Check if a module key has been processed."""
        with self._lock:
            return key in self._keys

    def mark_processed(self, key: str) -> None:
        """Mark a key as processed (thread-safe, appends to disk)."""
        with self._lock:
            if key in self._keys:
                return
            self._keys.add(key)
            with open(self._path, "a", encoding="utf-8") as f:
                f.write(json.dumps({"key": key, "timestamp": time.time()}) + "\n")

    @property
    def count(self) -> int:
        with self._lock:
            return len(self._keys)
