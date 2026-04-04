import os
import time
import json
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional
from pathlib import Path
import re

class ProfessionalLuaScraper:
    BASE_URL = "https://luarocks.org"
    
    def __init__(self, output_dir: str = "raw_data", rocks_per_label: int = 10):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.rocks_per_label = rocks_per_label
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "MCT-LuaRedactor-Bot/2.0 (Expert Knowledge Ingestion)"
        })

    def get_labels(self) -> List[Dict[str, str]]:
        """Scrapes all labels from the main page."""
        print("Scraping labels from LuaRocks homepage...")
        try:
            r = self.session.get(self.BASE_URL)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, 'lxml')
            
            # Find the section with h2 "View Modules by Labels"
            section = soup.find('h2', string=re.compile("View Modules by Labels", re.I)).parent
            links = section.find_all('a', href=True)
            
            labels = []
            for a in links:
                labels.append({
                    "name": a.text.strip(),
                    "url": a['href']
                })
            return labels
        except Exception as e:
            print(f"Error getting labels: {e}")
            return []

    def get_rocks_from_label(self, label_url: str) -> List[Dict[str, str]]:
        """Scrapes the list of modules for a specific label."""
        url = f"{self.BASE_URL}{label_url}"
        print(f"  Fetching rocks for label: {label_url}...")
        try:
            r = self.session.get(url)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, 'lxml')
            
            rock_rows = soup.select("li.module_row")
            rocks = []
            for row in rock_rows:
                link = row.select_one(".main a.title")
                if link:
                    rocks.append({
                        "name": link.text.strip(),
                        "url": link['href']
                    })
                if len(rocks) >= self.rocks_per_label:
                    break
            return rocks
        except Exception as e:
            print(f"    Error getting rocks for label {label_url}: {e}")
            return []

    def extract_deep_content(self, rock_info: Dict[str, str]) -> Optional[Dict[str, Any]]:
        """Goes deep into the rock page and its homepage (GitHub)."""
        url = f"{self.BASE_URL}{rock_info['url']}"
        try:
            r = self.session.get(url)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, 'lxml')
            
            # 1. Basic Metadata
            description_div = soup.select_one(".description")
            description = description_div.get_text(separator="\n").strip() if description_div else ""
            
            tags = [a.text.strip() for a in soup.select("div.label_row a[href^='/labels/']")]
            
            homepage_link = soup.select_one("a.external_url")
            homepage_url = homepage_link['href'] if homepage_link else None
            
            content = description
            source_url = url
            
            # 2. Deep Scrape GitHub if homepage is GitHub
            if homepage_url and "github.com" in homepage_url:
                raw_base = homepage_url.replace("github.com", "raw.githubusercontent.com")
                raw_base = re.sub(r'/(tree|blob)/[^/]+', '', raw_base).rstrip('/')
                
                # Common README filenames and branches
                for branch_path in ["/master/README.md", "/main/README.md", "/master/README.markdown", "/master/README"]:
                    try:
                        readme_r = self.session.get(raw_base + branch_path, timeout=5)
                        if readme_r.status_code == 200 and len(readme_r.text) > len(content):
                            content = readme_r.text
                            source_url = homepage_url
                            break
                    except:
                        continue
            
            # 3. Validation
            if len(content) < 100:
                return None # Signal too low
                
            return {
                "rock_name": rock_info['name'],
                "summary": description[:500],
                "tags": tags,
                "raw_content": content,
                "source": source_url
            }
        except Exception as e:
            print(f"    Error in deep extraction for {rock_info['name']}: {e}")
            return None

    def run(self):
        labels = self.get_labels()
        if not labels:
            print("No labels found. Exiting.")
            return

        for label in labels:
            print(f"Processing Label: {label['name']}")
            rocks = self.get_rocks_from_label(label['url'])
            
            for rock in rocks:
                # Check if we already have this rock (avoid duplicates across labels)
                safe_name = rock['name'].replace('/', '--').replace(' ', '_')
                file_path = self.output_dir / f"{safe_name}.json"
                if file_path.exists():
                    continue

                data = self.extract_deep_content(rock)
                if data:
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2)
                    print(f"    [SAVED] {rock['name']} ({len(data['raw_content'])} chars)")
                else:
                    print(f"    [SKIP] {rock['name']} (low content or error)")
                
                time.sleep(1) # Be nice to servers

if __name__ == "__main__":
    # Start with a limited run for user verification
    # We can increase rocks_per_label later
    scraper = ProfessionalLuaScraper(rocks_per_label=5)
    scraper.run()
