"""
downloader.py — Phase 3: Repository content acquisition.

Downloads README, docs, and .lua source files from:
  - GitHub  (via git/trees API with Bearer token + API version header)
  - GitLab  (via repository/tree API)
  - Bitbucket (via src/ API)
  - Doc sites (via crawl4ai → markdown, with html2text fallback)
"""

import json
import os
import urllib.parse
from pathlib import Path
from typing import Optional

from config import CONFIG, logger
from scraper import ModuleInfo
from utils import (
    delay, http_get, github_headers, parse_git_url,
    safe_dirname, crawl_to_markdown, html_to_markdown,
)


class ContentDownloader:
    """Downloads repository documentation and source files."""

    README_NAMES = {"readme.md", "readme", "readme.rst", "readme.txt"}
    DOC_DIRS = {"docs", "doc", "documentation", "man"}
    SRC_DIRS = {"src", "lib"}
    DOC_EXTENSIONS = {".md", ".txt", ".rst", ".lua"}

    def download(self, module_info: ModuleInfo) -> Optional[Path]:
        """Download content for a module. Returns save directory or None."""
        homepage = module_info.homepage_url
        if not homepage:
            logger.warning("No homepage for %s — skipping download", module_info.key)
            return None

        save_dir = CONFIG["raw_dir"] / safe_dirname(
            module_info.author, module_info.module_name, module_info.version,
        )
        save_dir.mkdir(parents=True, exist_ok=True)

        # Write metadata sidecar
        meta_path = save_dir / "metadata.json"
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(module_info.to_dict(), f, indent=2, ensure_ascii=False)

        git_info = parse_git_url(homepage)
        if not git_info:
            logger.warning("Cannot parse Git URL: %s — scraping as doc site", homepage)
            return self._scrape_doc_site(homepage, save_dir)

        host = git_info["host"].lower()
        try:
            if "github.com" in host:
                self._download_github(git_info["owner"], git_info["repo"], save_dir)
            elif "gitlab.com" in host:
                self._download_gitlab(git_info["owner"], git_info["repo"], save_dir)
            elif "bitbucket.org" in host:
                self._download_bitbucket(git_info["owner"], git_info["repo"], save_dir)
            else:
                return self._scrape_doc_site(homepage, save_dir)
        except Exception as exc:
            logger.error("Download error for %s: %s", module_info.key, exc)
            return None

        content_files = [
            f for f in save_dir.iterdir()
            if f.suffix in (".md", ".txt", ".lua", ".rst") and f.is_file()
        ]
        if not content_files:
            logger.warning("No content files for %s", module_info.key)
            return None

        logger.info("Downloaded %d files for %s", len(content_files), module_info.key)
        return save_dir

    # ── GitHub ────────────────────────────────────────────────────

    def _download_github(self, owner: str, repo: str, save_dir: Path) -> None:
        """Download via GitHub git/trees API with Bearer auth."""
        headers = github_headers()

        # Step 1: Get default branch
        repo_url = f"https://api.github.com/repos/{owner}/{repo}"
        delay()
        resp = http_get(repo_url, headers=headers)
        if not resp:
            logger.error("Cannot access GitHub repo %s/%s", owner, repo)
            return

        default_branch = resp.json().get("default_branch", "main")

        # Step 2: Get full file tree (recursive)
        tree_url = (
            f"https://api.github.com/repos/{owner}/{repo}"
            f"/git/trees/{default_branch}?recursive=1"
        )
        delay()
        resp = http_get(tree_url, headers=headers)
        if not resp:
            logger.error("Cannot fetch tree for %s/%s", owner, repo)
            return

        tree_items = resp.json().get("tree", [])

        # Step 3: Select files to download
        files_to_download: list[str] = []
        lua_count = 0

        for item in tree_items:
            if item.get("type") != "blob":
                continue
            path = item.get("path", "")
            basename = Path(path).name.lower()
            parent_parts = Path(path).parts[:-1] if Path(path).parts else ()

            # README files
            if basename in self.README_NAMES:
                files_to_download.append(path)
                continue

            # Doc directory files
            if parent_parts and parent_parts[0].lower() in self.DOC_DIRS:
                if Path(path).suffix.lower() in self.DOC_EXTENSIONS:
                    files_to_download.append(path)
                    continue

            # Lua files in root or src/
            if path.lower().endswith(".lua"):
                in_root = len(Path(path).parts) == 1
                in_src = parent_parts and parent_parts[0].lower() in self.SRC_DIRS
                if (in_root or in_src) and lua_count < CONFIG["max_lua_files_per_repo"]:
                    files_to_download.append(path)
                    lua_count += 1

        # Step 4: Download from raw.githubusercontent.com
        for file_path in files_to_download:
            raw_url = (
                f"https://raw.githubusercontent.com/{owner}/{repo}"
                f"/{default_branch}/{file_path}"
            )
            delay()
            resp = http_get(raw_url)
            if not resp:
                continue

            local_path = save_dir / file_path.replace("/", os.sep)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                local_path.write_text(resp.text, encoding="utf-8")
            except Exception as exc:
                logger.debug("Write failed %s: %s", local_path, exc)

    # ── GitLab ────────────────────────────────────────────────────

    def _download_gitlab(self, owner: str, repo: str, save_dir: Path) -> None:
        """Download via GitLab repository/tree API."""
        project_path = urllib.parse.quote(f"{owner}/{repo}", safe="")

        tree_url = (
            f"https://gitlab.com/api/v4/projects/{project_path}"
            f"/repository/tree?recursive=true&per_page=100"
        )
        delay()
        resp = http_get(tree_url)
        if not resp:
            logger.error("Cannot fetch GitLab tree for %s/%s", owner, repo)
            return

        tree_items = resp.json() if isinstance(resp.json(), list) else []
        lua_count = 0

        for item in tree_items:
            if item.get("type") != "blob":
                continue
            path = item.get("path", "")
            basename = Path(path).name.lower()
            parent_parts = Path(path).parts[:-1] if Path(path).parts else ()

            should_download = False
            if basename in self.README_NAMES:
                should_download = True
            elif parent_parts and parent_parts[0].lower() in self.DOC_DIRS:
                if Path(path).suffix.lower() in self.DOC_EXTENSIONS:
                    should_download = True
            elif path.lower().endswith(".lua"):
                in_root = len(Path(path).parts) == 1
                in_src = parent_parts and parent_parts[0].lower() in self.SRC_DIRS
                if (in_root or in_src) and lua_count < CONFIG["max_lua_files_per_repo"]:
                    should_download = True
                    lua_count += 1

            if not should_download:
                continue

            encoded_file = urllib.parse.quote(path, safe="")
            for ref in ("main", "master"):
                file_url = (
                    f"https://gitlab.com/api/v4/projects/{project_path}"
                    f"/repository/files/{encoded_file}/raw?ref={ref}"
                )
                delay()
                file_resp = http_get(file_url)
                if file_resp:
                    break
            else:
                continue

            local_path = save_dir / path.replace("/", os.sep)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                local_path.write_text(file_resp.text, encoding="utf-8")
            except Exception as exc:
                logger.debug("Write failed %s: %s", local_path, exc)

    # ── Bitbucket ─────────────────────────────────────────────────

    def _download_bitbucket(self, owner: str, repo: str, save_dir: Path) -> None:
        """Download via Bitbucket src/ API."""
        list_url = (
            f"https://api.bitbucket.org/2.0/repositories/{owner}/{repo}"
            f"/src/HEAD/?pagelen=100"
        )
        delay()
        resp = http_get(list_url)
        if not resp:
            logger.error("Cannot fetch Bitbucket listing for %s/%s", owner, repo)
            return

        entries = resp.json().get("values", [])
        lua_count = 0

        for entry in entries:
            path = entry.get("path", "")
            entry_type = entry.get("type", "")
            basename = Path(path).name.lower()

            if entry_type == "commit_directory":
                if basename in self.DOC_DIRS:
                    self._bb_download_dir(owner, repo, path, save_dir)
                elif basename in self.SRC_DIRS:
                    self._bb_download_dir(owner, repo, path, save_dir, lua_only=True)
                continue

            if entry_type != "commit_file":
                continue

            should_download = False
            if basename in self.README_NAMES:
                should_download = True
            elif path.lower().endswith(".lua") and lua_count < CONFIG["max_lua_files_per_repo"]:
                should_download = True
                lua_count += 1

            if not should_download:
                continue

            file_url = (
                f"https://api.bitbucket.org/2.0/repositories/{owner}/{repo}"
                f"/src/HEAD/{path}"
            )
            delay()
            file_resp = http_get(file_url)
            if not file_resp:
                continue

            local_path = save_dir / path.replace("/", os.sep)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                local_path.write_text(file_resp.text, encoding="utf-8")
            except Exception as exc:
                logger.debug("Write failed %s: %s", local_path, exc)

    def _bb_download_dir(
        self, owner: str, repo: str, dir_path: str,
        save_dir: Path, lua_only: bool = False,
    ) -> None:
        """Download files from a Bitbucket subdirectory."""
        list_url = (
            f"https://api.bitbucket.org/2.0/repositories/{owner}/{repo}"
            f"/src/HEAD/{dir_path}/?pagelen=100"
        )
        delay()
        resp = http_get(list_url)
        if not resp:
            return

        count = 0
        for entry in resp.json().get("values", []):
            if entry.get("type") != "commit_file":
                continue
            path = entry.get("path", "")
            ext = Path(path).suffix.lower()
            if lua_only and ext != ".lua":
                continue
            if not lua_only and ext not in self.DOC_EXTENSIONS:
                continue

            file_url = (
                f"https://api.bitbucket.org/2.0/repositories/{owner}/{repo}"
                f"/src/HEAD/{path}"
            )
            delay()
            file_resp = http_get(file_url)
            if not file_resp:
                continue

            local_path = save_dir / path.replace("/", os.sep)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                local_path.write_text(file_resp.text, encoding="utf-8")
            except Exception as exc:
                logger.debug("Write failed %s: %s", local_path, exc)

            count += 1
            if count >= CONFIG["max_lua_files_per_repo"]:
                break

    # ── Doc Site Scraping ─────────────────────────────────────────

    def _scrape_doc_site(self, url: str, save_dir: Path) -> Optional[Path]:
        """Scrape a documentation site to markdown via crawl4ai / html2text."""
        logger.info("Scraping doc site: %s", url)

        markdown = crawl_to_markdown(url)
        if len(markdown.strip()) < 50:
            logger.warning("Doc site %s produced too little content", url)
            return None

        (save_dir / "documentation.md").write_text(markdown, encoding="utf-8")
        return save_dir
