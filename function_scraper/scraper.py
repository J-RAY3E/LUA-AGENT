"""
scraper.py — Phase 1: LuaRocks label-based module discovery.

LabelScraper:  Scrapes /labels/<label> pages to discover modules.
ModuleFetcher: Fetches module detail pages for version + homepage URL.
"""

import re
from dataclasses import dataclass, asdict
from typing import Optional

from bs4 import BeautifulSoup

from config import CONFIG, logger
from utils import delay, http_get, is_valid_homepage, module_key


@dataclass
class ModuleInfo:
    """Scraped metadata for a single LuaRocks module."""
    module_name: str
    author: str
    downloads: str = ""
    summary: str = ""
    version: str = ""
    homepage_url: str = ""
    label: str = ""

    @property
    def key(self) -> str:
        return module_key(self.author, self.module_name, self.version)

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


class LabelScraper:
    """Scrapes LuaRocks label pages to discover modules.

    Parses HTML <li class="module_row"> elements.
    Handles pagination via ?page=N and includes non-root modules.
    """

    def __init__(self) -> None:
        self._base = CONFIG["base_url"]

    def scrape_label(self, label: str) -> list[ModuleInfo]:
        """Scrape all modules for a given label across all pages."""
        logger.info("Scraping label: %s", label)
        all_modules: list[ModuleInfo] = []
        page = 1

        while True:
            url = f"{self._base}/labels/{label}?non_root=on&page={page}"
            delay()
            resp = http_get(url)
            if not resp:
                logger.error("Failed to fetch label page: %s page %d", label, page)
                break

            soup = BeautifulSoup(resp.text, "html.parser")
            rows = soup.select("li.module_row")

            if not rows and page == 1:
                logger.warning("No module_row elements for label '%s' — trying fallback", label)
                all_modules.extend(self._fallback_parse(soup, label))
                break

            if not rows:
                break

            for row in rows:
                mod = self._parse_row(row, label)
                if mod:
                    all_modules.append(mod)

            # Check for next page
            next_link = soup.select_one('a.next_page, a[rel="next"]')
            if not next_link:
                break
            page += 1

        logger.info("Label '%s': discovered %d modules", label, len(all_modules))
        return all_modules

    def _parse_row(self, row: BeautifulSoup, label: str) -> Optional[ModuleInfo]:
        """Extract module info from a single <li class='module_row'>."""
        try:
            # Module name from <a class="title">
            title_el = row.select_one("a.title")
            if not title_el:
                for a_tag in row.find_all("a"):
                    href = a_tag.get("href", "")
                    if "/modules/" in href and href.count("/") >= 3:
                        title_el = a_tag
                        break
            if not title_el:
                return None

            module_name = title_el.get_text(strip=True)
            href = title_el.get("href", "")

            # Author from href pattern /modules/<author>/<module>
            author = ""
            href_parts = [p for p in href.strip("/").split("/") if p]
            if len(href_parts) >= 2 and href_parts[0] == "modules":
                author = href_parts[1]
                if len(href_parts) >= 3:
                    module_name = href_parts[2]

            if not author:
                author_el = row.select_one("a.author")
                if not author_el:
                    for a_tag in row.find_all("a"):
                        a_href = a_tag.get("href", "")
                        if re.match(r"^/modules/[^/]+/?$", a_href):
                            author_el = a_tag
                            break
                if author_el:
                    author = author_el.get_text(strip=True)

            if not author or not module_name:
                return None

            downloads = ""
            dl_el = row.select_one("span.value, .download_count .value")
            if dl_el:
                downloads = dl_el.get_text(strip=True)

            summary = ""
            sum_el = row.select_one("div.summary, span.summary, p.summary")
            if sum_el:
                summary = sum_el.get_text(strip=True)

            return ModuleInfo(
                module_name=module_name, author=author,
                downloads=downloads, summary=summary, label=label,
            )
        except Exception as exc:
            logger.debug("Error parsing module_row: %s", exc)
            return None

    def _fallback_parse(self, soup: BeautifulSoup, label: str) -> list[ModuleInfo]:
        """Fallback: find all /modules/<author>/<module> links."""
        modules: list[ModuleInfo] = []
        seen: set[str] = set()

        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            match = re.match(r"^/modules/([^/]+)/([^/]+)/?$", href)
            if not match:
                continue
            author, mod = match.group(1), match.group(2)
            key = f"{author}/{mod}"
            if key in seen:
                continue
            seen.add(key)
            modules.append(ModuleInfo(module_name=mod, author=author, label=label))

        return modules


class ModuleFetcher:
    """Fetches version and homepage URL from a module's detail page."""

    def __init__(self) -> None:
        self._base = CONFIG["base_url"]

    def fetch_detail(self, author: str, module_name: str) -> Optional[dict[str, str]]:
        """Returns dict with 'version' and 'homepage_url', or None."""
        url = f"{self._base}/modules/{author}/{module_name}"
        delay()
        resp = http_get(url)
        if not resp:
            logger.warning("Failed to fetch detail for %s/%s", author, module_name)
            return None

        soup = BeautifulSoup(resp.text, "html.parser")
        homepage_url = self._extract_homepage(soup)
        version = self._extract_version(soup) or "unknown"

        return {"version": version, "homepage_url": homepage_url or ""}

    def _extract_homepage(self, soup: BeautifulSoup) -> Optional[str]:
        """Find homepage URL via multiple strategies."""
        # Strategy 1: h3 "Homepage" + next <a>
        for h3 in soup.find_all("h3"):
            if "homepage" in h3.get_text(strip=True).lower():
                parent = h3.parent
                if parent:
                    link = parent.find("a", href=True)
                    if link:
                        return link["href"]
                next_el = h3.find_next("a", href=True)
                if next_el:
                    return next_el["href"]

        # Strategy 2: <a class="external_url">
        ext_link = soup.select_one("a.external_url")
        if ext_link and ext_link.get("href"):
            return ext_link["href"]

        # Strategy 3: any link to supported Git hosts
        for a_tag in soup.find_all("a", href=True):
            if is_valid_homepage(a_tag["href"]):
                return a_tag["href"]

        return None

    def _extract_version(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract latest version from versions section."""
        for h3 in soup.find_all("h3"):
            if "version" in h3.get_text(strip=True).lower():
                parent = h3.parent or h3
                first_link = parent.find_next("a", href=True)
                if first_link:
                    text = first_link.get_text(strip=True)
                    if re.match(r"[\d]", text):
                        return text

        version_sel = soup.select_one("select.version_selector option, .version_row a")
        if version_sel:
            return version_sel.get_text(strip=True)

        for a_tag in soup.find_all("a", href=True):
            match = re.search(r"/(\d+[\d.\-]+)/?$", a_tag["href"])
            if match:
                return match.group(1)

        return None
