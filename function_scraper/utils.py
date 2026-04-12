"""
utils.py — HTTP helpers, GitHub API auth, URL parsing, and markdown conversion.

Uses Bearer token auth + X-GitHub-Api-Version header for GitHub API.
"""

import random
import re
import time
import urllib.parse
from typing import Optional

import requests

from config import CONFIG, GITHUB_TOKEN, logger

# ─── Optional: crawl4ai for HTML → Markdown ─────────────────────
try:
    import asyncio
    from crawl4ai import AsyncWebCrawler
    HAS_CRAWL4AI = True
except ImportError:
    HAS_CRAWL4AI = False

try:
    import html2text as _html2text_mod
    _H2T = _html2text_mod.HTML2Text()
    _H2T.ignore_links = False
    _H2T.ignore_images = True
    _H2T.body_width = 0
    HAS_HTML2TEXT = True
except ImportError:
    HAS_HTML2TEXT = False


def delay() -> None:
    """Sleep for a random duration within configured bounds."""
    time.sleep(random.uniform(CONFIG["request_delay_min"], CONFIG["request_delay_max"]))


def http_get(url: str, headers: Optional[dict] = None, timeout: int = 30) -> Optional[requests.Response]:
    """GET with retries + exponential backoff. Returns None on permanent failure."""
    hdrs = {"User-Agent": CONFIG["user_agent"]}
    if headers:
        hdrs.update(headers)

    for attempt in range(1, CONFIG["max_retries"] + 1):
        try:
            resp = requests.get(url, headers=hdrs, timeout=timeout)
            if resp.status_code == 200:
                return resp
            if resp.status_code in (404, 410, 451):
                logger.warning("HTTP %d (permanent) for %s", resp.status_code, url)
                return None
            if resp.status_code == 403 and "rate limit" in resp.text.lower():
                wait = int(resp.headers.get("Retry-After", 60))
                logger.warning("Rate-limited on %s — sleeping %ds", url, wait)
                time.sleep(wait)
                continue
            logger.warning("HTTP %d on attempt %d for %s", resp.status_code, attempt, url)
        except requests.RequestException as exc:
            logger.warning("Network error on attempt %d for %s: %s", attempt, url, exc)

        if attempt < CONFIG["max_retries"]:
            backoff = 2 ** attempt + random.random()
            time.sleep(backoff)

    logger.error("All %d attempts failed for %s", CONFIG["max_retries"], url)
    return None


def github_headers() -> dict[str, str]:
    """GitHub API headers with Bearer token auth + API version."""
    headers: dict[str, str] = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = GITHUB_TOKEN
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def parse_git_url(url: str) -> Optional[dict[str, str]]:
    """Parse a GitHub/GitLab/Bitbucket URL into {host, owner, repo}."""
    url = url.rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]

    parsed = urllib.parse.urlparse(url)
    host = parsed.hostname or ""
    parts = [p for p in parsed.path.strip("/").split("/") if p]

    if len(parts) < 2:
        return None
    return {"host": host, "owner": parts[0], "repo": parts[1]}


def is_valid_homepage(url: Optional[str]) -> bool:
    """Check if URL points to a supported Git host."""
    if not url:
        return False
    parsed = urllib.parse.urlparse(url)
    hostname = (parsed.hostname or "").lower()
    return any(hostname.endswith(h) for h in CONFIG["valid_hosts"])


def module_key(author: str, module: str, version: str) -> str:
    """Create a unique key for a module."""
    return f"{author}__{module}__{version}"


def safe_dirname(author: str, module: str, version: str) -> str:
    """Create a filesystem-safe directory name."""
    return re.sub(r"[^\w.\-]", "_", f"{author}__{module}__{version}")


def crawl_to_markdown(url: str) -> str:
    """Convert a URL to markdown using crawl4ai (async).

    Falls back to requests + html2text if crawl4ai is not installed.
    """
    if HAS_CRAWL4AI:
        try:
            async def _crawl() -> str:
                async with AsyncWebCrawler(verbose=False) as crawler:
                    result = await crawler.arun(url=url)
                    return result.markdown or ""
            return asyncio.run(_crawl())
        except Exception as exc:
            logger.warning("crawl4ai failed for %s: %s — falling back", url, exc)

    # Fallback: requests + html2text
    resp = http_get(url)
    if not resp:
        return ""
    return html_to_markdown(resp.text)


def html_to_markdown(html: str) -> str:
    """Convert raw HTML to markdown."""
    if HAS_HTML2TEXT:
        return _H2T.handle(html)
    # Minimal fallback: strip tags
    text = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", text).strip()
