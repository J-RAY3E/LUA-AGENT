import os
import re
from typing import List, Dict, Any

# Define paths relative to this file
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_ENTITIES_DIR = os.path.join(_PROJECT_ROOT, "wiki", "entities")
WIKI_CONCEPTS_DIR = os.path.join(_PROJECT_ROOT, "wiki", "concepts")

def load_data() -> List[Dict[str, str]]:
    """
    Loads all markdown files constructed by the wiki/ingest pipeline.
    """
    data = []
    
    for directory in [WIKI_ENTITIES_DIR, WIKI_CONCEPTS_DIR]:
        if not os.path.exists(directory):
            continue
            
        for fname in os.listdir(directory):
            if not fname.endswith(".md"):
                continue
                
            fpath = os.path.join(directory, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                # Extract clean name without extension
                name = fname.replace(".md", "")
                
                # Try to extract the Title or Type from markdown
                title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else name
                
                data.append({
                    "rock_id": name,
                    "title": title.lower(),
                    "content": content,
                    "source_phase": "wiki_pipeline"
                })
            except Exception as e:
                print(f"[RAG] Failed to load {fname}: {e}")
                
    return data

def get_index(data: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Builds a fast Lexical Index mapping entity names and major tokens to their data index.
    This replaces FAISS clustering with a highly accurate exact-match index.
    """
    index = {
        "exact_map": {}, 
        "token_map": {}
    }
    
    for i, item in enumerate(data):
        # 1. Exact Name Mapping (e.g., 'lua_alloc', 'lual_addgsub')
        exact_name = item["rock_id"].lower()
        index["exact_map"][exact_name] = i
        
        # Also map the document Title
        title = item["title"].lower()
        if title not in index["exact_map"]:
            index["exact_map"][title] = i
            
        # 2. Basic Token Mapping for partial matches
        # Splits by _, -, and spaces
        tokens = set(re.split(r'[_ \-]', exact_name))
        tokens.update(re.split(r'[_ \-]', title))
        
        for token in tokens:
            if len(token) > 2: # Ignore tiny tokens like 'a', 'to'
                if token not in index["token_map"]:
                    index["token_map"][token] = []
                index["token_map"][token].append(i)
                
    return index

def search(query: str, index: Dict[str, Any], data: List[Dict[str, str]], k: int = 5) -> List[Dict[str, Any]]:
    """
    Searches the lexical database for exact entity matches derived from the query.
    """
    query_lower = query.lower()
    
    # 1. Identify potential Lua/C entities explicitly mentioned in the query
    # E.g. "Generate code using lua_Alloc and lua_pushstring"
    # Matches words that look like technical identifiers
    potential_entities = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', query_lower)
    
    scored_indices = {}
    
    # Check exact maps first (Highest priority: 100 points)
    for entity in potential_entities:
        if entity in index["exact_map"]:
            idx = index["exact_map"][entity]
            scored_indices[idx] = scored_indices.get(idx, 0) + 100.0
            
    # Check token maps (Lower priority: 10 points)
    for token in potential_entities:
        if token in index["token_map"]:
            for idx in index["token_map"][token]:
                scored_indices[idx] = scored_indices.get(idx, 0) + 10.0
                
    # If no exact or high-score token matches, we fall back to a naive text search
    if not scored_indices:
        query_words = set(query_lower.split())
        for i, item in enumerate(data):
            content_lower = item["content"].lower()
            score = 0.0
            for w in query_words:
                if len(w) > 3 and w in content_lower:
                    score += 1.0
            if score > 0:
                scored_indices[i] = score

    # Sort results by score
    sorted_idx = sorted(scored_indices.items(), key=lambda x: x[1], reverse=True)
    
    results = []
    for idx, score in sorted_idx[:k]:
        item = data[idx].copy()
        item["similarity"] = score / 100.0 # Normalize roughly
        results.append(item)
        
    return results
