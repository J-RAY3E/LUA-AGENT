import os
import re
from typing import List, Dict, Any, Optional

# --- KONFIGURASI PATH ---
# Mendapatkan root directory proyek (asumsi file ini ada di src/ atau similar)
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_ENTITIES_DIR = os.path.join(_PROJECT_ROOT, "wiki", "entities")
WIKI_CONCEPTS_DIR = os.path.join(_PROJECT_ROOT, "wiki", "concepts")

# Nama file khusus untuk knowledge dasar
BASIC_KNOWLEDGE_FILE = "basic.md"

def get_system_knowledge() -> str:
    """
    Mengambil konten dari concepts/basic.md untuk disuntikkan ke System Prompt.
    Ini memastikan aturan dasar SELALU diketahui oleh AI, terlepas dari query user.
    """
    basic_path = os.path.join(WIKI_CONCEPTS_DIR, BASIC_KNOWLEDGE_FILE)
    if os.path.exists(basic_path):
        try:
            with open(basic_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"[WARNING] Failed to load system knowledge from {basic_path}: {e}")
    return ""

def load_data() -> List[Dict[str, str]]:
    """
    Memuat semua file markdown dari wiki/entities dan wiki/concepts.
    Mengecualikan 'basic.md' dari hasil pencarian biasa jika diinginkan, 
    atau membiarkannya ada sebagai referensi tambahan.
    """
    data = []
    directories = [WIKI_ENTITIES_DIR, WIKI_CONCEPTS_DIR]
    
    for directory in directories:
        if not os.path.exists(directory):
            continue
            
        for fname in os.listdir(directory):
            if not fname.endswith(".md"):
                continue
                
            # Opsional: Skip basic.md di sini jika Anda TIDAK ingin ia muncul 
            # dalam hasil search() biasa, karena sudah ada di System Prompt.
            # if fname == BASIC_KNOWLEDGE_FILE:
            #     continue
                
            fpath = os.path.join(directory, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                # Extract clean name without extension
                name = fname.replace(".md", "")
                
                # Try to extract the Title from markdown header (# Title)
                title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else name
                
                data.append({
                    "rock_id": name,
                    "title": title.lower(),
                    "content": content,
                    "source_phase": "wiki_pipeline",
                    "is_basic_knowledge": (fname == BASIC_KNOWLEDGE_FILE)
                })
            except Exception as e:
                print(f"[RAG] Failed to load {fname}: {e}")
                
    return data

def get_index(data: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Membangun Indeks Leksikal Cepat.
    - exact_map: Untuk pencocokan nama fungsi/entitas persis (Prioritas Tinggi).
    - token_map: Untuk pencocokan parsial/kata kunci (Prioritas Rendah).
    """
    index = {
        "exact_map": {}, 
        "token_map": {}
    }
    
    for i, item in enumerate(data):
        # Abaikan indexing untuk basic knowledge jika sudah di system prompt (opsional)
        # if item.get("is_basic_knowledge"):
        #     continue

        # 1. Exact Name Mapping
        exact_name = item["rock_id"].lower()
        # Jika ada duplikat, yang terakhir menimpa (atau bisa dibuat list jika perlu)
        index["exact_map"][exact_name] = i
        
        # Map juga berdasarkan Title dokumen
        title = item["title"].lower()
        if title not in index["exact_map"]:
            index["exact_map"][title] = i
            
        # 2. Token Mapping (Split by _, -, space)
        tokens = set(re.split(r'[_ \-]', exact_name))
        tokens.update(re.split(r'[_ \-]', title))
        
        for token in tokens:
            # Filter token terlalu pendek atau noise
            if len(token) > 2 and token.isalnum(): 
                if token not in index["token_map"]:
                    index["token_map"][token] = []
                # Hindari duplikasi index dalam list token
                if i not in index["token_map"][token]:
                    index["token_map"][token].append(i)
                
    return index

def search(query: str, index: Dict[str, Any], data: List[Dict[str, str]], k: int = 5) -> List[Dict[str, Any]]:
    """
    Mencari dokumen relevan berdasarkan query pengguna.
    Menggunakan strategi scoring hybrid: Exact Match > Token Match > Naive Text Search.
    """
    query_lower = query.lower()
    
    # Ekstrak identifier teknis dari query (contoh: lua_pushstring, my_var)
    # Regex ini menangkap kata yang dimulai dengan huruf/underscore, diikuti alfanumerik/underscore
    potential_entities = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', query_lower)
    
    scored_indices: Dict[int, float] = {}
    
    # --- STRATEGI 1: Exact Match (Skor Tinggi: 100) ---
    for entity in potential_entities:
        if entity in index["exact_map"]:
            idx = index["exact_map"][entity]
            scored_indices[idx] = scored_indices.get(idx, 0) + 100.0
            
    # --- STRATEGI 2: Token Match (Skor Sedang: 10) ---
    for token in potential_entities:
        if token in index["token_map"]:
            for idx in index["token_map"][token]:
                scored_indices[idx] = scored_indices.get(idx, 0) + 10.0
                
    # --- STRATEGI 3: Fallback Naive Search (Jika tidak ada match teknis) ---
    # Hanya dijalankan jika scored_indices masih kosong atau sangat sedikit
    if not scored_indices:
        query_words = set([w for w in query_lower.split() if len(w) > 3])
        for i, item in enumerate(data):
            # Skip basic knowledge di fallback jika sudah di system prompt (opsional)
            # if item.get("is_basic_knowledge"):
            #     continue

            content_lower = item["content"].lower()
            score = 0.0
            for w in query_words:
                if w in content_lower:
                    score += 1.0
            if score > 0:
                scored_indices[i] = score

    # Urutkan berdasarkan skor tertinggi
    sorted_idx = sorted(scored_indices.items(), key=lambda x: x[1], reverse=True)
    
    results = []
    for idx, score in sorted_idx[:k]:
        item = data[idx].copy()
        # Normalisasi skor untuk keperluan UI/Debugging
        item["similarity_score"] = score 
        results.append(item)
        
    return results

# --- CONTOH PENGGUNAAN (MAIN) ---
if __name__ == "__main__":
    print("Loading Wiki Data...")
    wiki_data = load_data()
    print(f"Loaded {len(wiki_data)} documents.")
    
    print("Building Index...")
    wiki_index = get_index(wiki_data)
    
    # Ambil Knowledge Dasar untuk System Prompt
    system_prompt_context = get_system_knowledge()
    print("-" * 20)
    print("SYSTEM KNOWLEDGE (Basic.md):")
    print(system_prompt_context[:200] + "..." if len(system_prompt_context) > 200 else system_prompt_context)
    print("-" * 20)

    # Tes Pencarian
    test_query = "How to use lua_next to iterate a table safely?"
    print(f"\nSearching for: '{test_query}'")
    
    results = search(test_query, wiki_index, wiki_data)
    
    if results:
        print(f"Found {len(results)} relevant documents:")
        for r in results:
            print(f"- [{r['similarity_score']}] {r['title']} (ID: {r['rock_id']})")
    else:
        print("No relevant documents found.")
