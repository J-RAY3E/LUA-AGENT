"""
pipeline.py — Threaded pipeline orchestrator.

Each phase runs in its own thread, connected by queue.Queue:

  [DiscoveryWorker] ──put──▶ discovery_q ──get──▶ [DownloadWorker]
  [DownloadWorker]  ──put──▶ download_q  ──get──▶ [ExtractionWorker]
  [ExtractionWorker]──put──▶ output_q    ──get──▶ [AssemblyWorker]

Each worker blocks on its input queue until an item arrives.
A None sentinel signals the worker to shut down and propagate the sentinel downstream.
"""

import queue
import threading
from pathlib import Path

from config import CONFIG, logger, setup_logging
from scraper import LabelScraper, ModuleFetcher, ModuleInfo
from queue_manager import ProcessedManifest
from downloader import ContentDownloader
from chunker import Chunker
from llm_extractor import LLMExtractor
from fallback_extractor import FallbackExtractor
from assembler import OutputAssembler
from utils import is_valid_homepage

# Sentinel value to signal worker shutdown
_STOP = None


class Pipeline:
    """Threaded pipeline with 4 worker stages connected by queues.

    Stage 1 — Discovery:  scrape labels → filter → put valid modules
    Stage 2 — Download:   download repo content for each module
    Stage 3 — Extraction: chunk + LLM extract + fallback
    Stage 4 — Assembly:   write structured JSON output
    """

    def __init__(self, labels: list[str]) -> None:
        self.labels = labels

        # Thread-safe inter-stage queues
        self.discovery_q: queue.Queue[ModuleInfo | None] = queue.Queue()
        self.download_q: queue.Queue[tuple[ModuleInfo, Path] | None] = queue.Queue()
        self.output_q: queue.Queue[tuple[ModuleInfo, list[dict]] | None] = queue.Queue()

        # Shared components
        self.manifest = ProcessedManifest()

        # Stage-specific components (each owned by its worker thread)
        self._scraper = LabelScraper()
        self._fetcher = ModuleFetcher()
        self._downloader = ContentDownloader()
        self._chunker = Chunker()
        self._llm = LLMExtractor()
        self._fallback = FallbackExtractor()
        self._assembler = OutputAssembler()

        # Counters (thread-safe via GIL for simple int ops)
        self.stats = {
            "discovered": 0,
            "queued": 0,
            "downloaded": 0,
            "extracted": 0,
            "assembled": 0,
            "errors": 0,
        }

    def run(self) -> None:
        """Launch all worker threads and wait for completion."""
        setup_logging()

        # Ensure directories exist
        for key in ("raw_dir", "output_dir", "logs_dir"):
            CONFIG[key].mkdir(parents=True, exist_ok=True)

        logger.info("=" * 70)
        logger.info("LuaRocks MCP Builder — Threaded Pipeline")
        logger.info("Labels: %s", ", ".join(self.labels))
        logger.info("LLM endpoint: %s", CONFIG["llm_api_url"])
        logger.info("LLM model: %s", CONFIG["llm_model"])
        logger.info("=" * 70)

        workers = [
            threading.Thread(target=self._discovery_worker, name="Discovery", daemon=True),
            threading.Thread(target=self._download_worker, name="Download", daemon=True),
            threading.Thread(target=self._extraction_worker, name="Extraction", daemon=True),
            threading.Thread(target=self._assembly_worker, name="Assembly", daemon=True),
        ]

        for w in workers:
            logger.info("Starting thread: %s", w.name)
            w.start()

        for w in workers:
            w.join()

        # Summary
        logger.info("=" * 70)
        logger.info("Pipeline complete")
        for k, v in self.stats.items():
            logger.info("  %-12s %d", k + ":", v)
        logger.info("  Output dir:  %s", CONFIG["output_dir"])
        logger.info("=" * 70)

    # ── Stage 1: Discovery ────────────────────────────────────────

    def _discovery_worker(self) -> None:
        """Scrape label pages → filter → put valid modules into discovery_q."""
        logger.info("[Discovery] Starting — %d labels to scrape", len(self.labels))

        try:
            for label in self.labels:
                modules = self._scraper.scrape_label(label)
                self.stats["discovered"] += len(modules)

                for mod in modules:
                    # Fetch detail page for version + homepage
                    detail = self._fetcher.fetch_detail(mod.author, mod.module_name)
                    if not detail:
                        continue

                    mod.version = detail.get("version", "unknown")
                    mod.homepage_url = detail.get("homepage_url", "")

                    # Skip if already processed
                    if self.manifest.is_processed(mod.key):
                        logger.debug("[Discovery] Already processed: %s", mod.key)
                        continue

                    # Filter: must have a non-empty homepage
                    if not mod.homepage_url:
                        logger.info(
                            "[Discovery] SKIP %s — no homepage",
                            mod.module_name,
                        )
                        continue

                    self.discovery_q.put(mod)
                    self.stats["queued"] += 1
                    logger.info("[Discovery] Queued: %s", mod.key)

        except Exception as exc:
            logger.error("[Discovery] Fatal error: %s", exc, exc_info=True)
            self.stats["errors"] += 1
        finally:
            self.discovery_q.put(_STOP)
            logger.info("[Discovery] Done — %d modules queued", self.stats["queued"])

    # ── Stage 2: Download ─────────────────────────────────────────

    def _download_worker(self) -> None:
        """Pull from discovery_q → download content → put into download_q."""
        logger.info("[Download] Waiting for modules...")

        try:
            while True:
                item = self.discovery_q.get()
                if item is _STOP:
                    break

                logger.info("[Download] Downloading: %s", item.key)
                try:
                    content_dir = self._downloader.download(item)
                    if content_dir:
                        self.download_q.put((item, content_dir))
                        self.stats["downloaded"] += 1
                    else:
                        logger.warning("[Download] No content for %s", item.key)
                        self.manifest.mark_processed(item.key)
                except Exception as exc:
                    logger.error("[Download] Error for %s: %s", item.key, exc)
                    self.stats["errors"] += 1
                    self.manifest.mark_processed(item.key)

        except Exception as exc:
            logger.error("[Download] Fatal error: %s", exc, exc_info=True)
        finally:
            self.download_q.put(_STOP)
            logger.info("[Download] Done — %d downloaded", self.stats["downloaded"])

    # ── Stage 3: Extraction ───────────────────────────────────────

    def _extraction_worker(self) -> None:
        """Pull from download_q → chunk → LLM extract → fallback → put into output_q."""
        logger.info("[Extraction] Waiting for downloads...")

        try:
            while True:
                item = self.download_q.get()
                if item is _STOP:
                    break

                mod_info, content_dir = item
                logger.info("[Extraction] Processing: %s", mod_info.key)

                try:
                    # Phase 4: Chunk
                    chunks = self._chunker.chunk(content_dir, mod_info.key)

                    # Phase 5: LLM extraction
                    all_functions: list[dict[str, str]] = []
                    for chunk in chunks:
                        funcs = self._llm.extract(chunk)
                        all_functions.extend(funcs)

                    # Phase 6: Fallback if LLM returned nothing
                    if not all_functions:
                        logger.info("[Extraction] LLM empty for %s — using fallback", mod_info.key)
                        all_functions = self._fallback.extract(content_dir)

                    if all_functions:
                        self.output_q.put((mod_info, all_functions))
                        self.stats["extracted"] += 1
                    else:
                        logger.warning("[Extraction] No functions found for %s", mod_info.key)
                        self.manifest.mark_processed(mod_info.key)

                except Exception as exc:
                    logger.error("[Extraction] Error for %s: %s", mod_info.key, exc)
                    self.stats["errors"] += 1
                    self.manifest.mark_processed(mod_info.key)

        except Exception as exc:
            logger.error("[Extraction] Fatal error: %s", exc, exc_info=True)
        finally:
            self.output_q.put(_STOP)
            logger.info("[Extraction] Done — %d extracted", self.stats["extracted"])

    # ── Stage 4: Assembly ─────────────────────────────────────────

    def _assembly_worker(self) -> None:
        """Pull from output_q → assemble JSON → write to disk → mark processed."""
        logger.info("[Assembly] Waiting for results...")

        try:
            while True:
                item = self.output_q.get()
                if item is _STOP:
                    break

                mod_info, functions = item
                logger.info("[Assembly] Writing: %s (%d functions)", mod_info.key, len(functions))

                try:
                    self._assembler.assemble(mod_info, functions)
                    self.manifest.mark_processed(mod_info.key)
                    self.stats["assembled"] += 1
                except Exception as exc:
                    logger.error("[Assembly] Error for %s: %s", mod_info.key, exc)
                    self.stats["errors"] += 1
                    self.manifest.mark_processed(mod_info.key)

        except Exception as exc:
            logger.error("[Assembly] Fatal error: %s", exc, exc_info=True)
        finally:
            logger.info("[Assembly] Done — %d assembled", self.stats["assembled"])
