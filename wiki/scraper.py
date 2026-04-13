"""
scraper.py — DevDocs Lua 5.5 Scraper for Wiki Brain.
Fetches official documentation and writes clean Markdown chunks into raw/
"""

import os
import json
import requests
import re
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Adjust paths to hit the wiki raw folder
_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(_PROJECT_ROOT, "raw")

INDEX_URL = "https://documents.devdocs.io/lua~5.5/index.json"
DB_URL = "https://documents.devdocs.io/lua~5.5/db.json"

def clean_html(html_str: str) -> str:
    """Pre-process HTML before feeding to markdownify."""
    soup = BeautifulSoup(html_str, 'html.parser')
    
    # Remove header links (the little anchor symbols)
    for a in soup.find_all('a', class_='_list-arrow'):
        a.decompose()
        
    return str(soup)

def run():
    print(f"Fetching Lua 5.5 Index from {INDEX_URL}...")
    try:
        index_data = requests.get(INDEX_URL).json()
    except Exception as e:
        print(f"Failed to fetch index: {e}")
        return

    print(f"Fetching HTML payload from {DB_URL}...")
    try:
        db_data = requests.get(DB_URL).json()
    except Exception as e:
        print(f"Failed to fetch payload: {e}")
        return

    # Group entries by type (e.g., "API", "Standard Libraries")
    categories = {}
    
    # Track the main entry (the index.html equivalent) which sometimes has no direct type in entries
    if "index" in db_data:
        categories["Language (Main)"] = [("Main Overview", db_data["index"])]
        
    entries = index_data.get("entries", [])
    print(f"Loaded {len(entries)} entries. Processing...")

    for entry in entries:
        path = entry.get("path")
        name = entry.get("name")
        type_name = entry.get("type", "General")
        
        # db.json might have the exact path or it might not
        # Sometimes DevDocs paths include hash anchors like index#pdf-lua_absindex
        # but the db.json keys are usually just the base path without the hash if it's all one page.
        # DevDocs for small languages packs everything into a few pages or even one "index" page.
        
        db_key = path
        # If the direct key doesn't exist, it might be inside the main page
        if db_key not in db_data and '#' in db_key:
            db_key = db_key.split('#')[0]
            
        if db_key in db_data:
            if type_name not in categories:
                categories[type_name] = []
                
            # DevDocs puts the entire HTML for a base page in db_data[db_key].
            # If multiple entries point to the same base page but different hashes,
            # we shouldn't parse the whole page repeatedly.
            # We'll just group by db_key and parse it once per base page.
            pass

    # Wait, for Lua 5.5, let's see how db.json actually stores it.
    # We will just iterate over db_data keys directly because each key in db.json is an HTML chunk!
    
    print("\nGrouping by chunks...")
    grouped_content = {}
    
    for key, html in db_data.items():
        # Determine category based on the first entry that points to this key
        # or defaults
        category_name = "General"
        for entry in entries:
            path = entry.get("path", "")
            if path == key or path.startswith(key + "#"):
                category_name = entry.get("type", "General")
                break
                
        if category_name not in grouped_content:
            grouped_content[category_name] = []
        
        # Convert to markdown
        clean = clean_html(html)
        markdown_text = md(clean, heading_style="ATX", code_language="lua")
        
        # Cleanup extra newlines
        markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)
        
        grouped_content[category_name].append(markdown_text)
        
    os.makedirs(RAW_DIR, exist_ok=True)
    
    # DevDocs Lua 5.5 basically ships as one massive 'index' HTML page.
    # Output it as one single monolithic document which our wiki_brain chunker will Map-Reduce process perfectly.
    filename = "lua_5_5_devdocs.md"
    filepath = os.path.join(RAW_DIR, filename)
    
    full_markdown = "# Lua 5.5 Official Documentation\n\n"
    for chunks in grouped_content.values():
        full_markdown += "\n\n---\n\n".join(chunks)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_markdown)
        
    print(f" -> Saved {filename} ({len(full_markdown)} chars)")
        
    print("\nDone! Run `python -m wiki status` to verify.")

if __name__ == "__main__":
    run()
