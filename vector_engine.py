import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Configuration
MODEL_NAME = 'all-MiniLM-L6-v2'
INDEX_FILE = "index.faiss"
DATA_FILE = "master_index.json"

model = SentenceTransformer(MODEL_NAME)

def load_data():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found. Run ingest_data.py first.")
        return None
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def build_and_save_index(data):
    """Build FAISS index with cosine similarity (normalized inner product)."""
    texts = [doc["semantic_content"] for doc in data]

    print(f"Vectorizing {len(texts)} fragments...")
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype('float32')

    # Normalize for cosine similarity
    faiss.normalize_L2(embeddings)

    # Inner product index (cosine similarity after normalization)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)

    faiss.write_index(index, INDEX_FILE)
    print(f"Index saved to: {INDEX_FILE} ({index.ntotal} vectors, dim={dimension})")
    return index

def get_index(data):
    if os.path.exists(INDEX_FILE):
        print("Loading existing index from disk...")
        return faiss.read_index(INDEX_FILE)
    else:
        print("Index not found. Building new one...")
        return build_and_save_index(data)

def search(query, index, data, k=5):
    """Search with cosine similarity. Higher score = better match."""
    query_vector = model.encode([query]).astype('float32')
    faiss.normalize_L2(query_vector)

    scores, indices = index.search(query_vector, k)

    results = []
    for i in range(k):
        idx = indices[0][i]
        if idx < len(data):
            results.append({
                "rock_id": data[idx]["rock_id"],
                "content": data[idx]["content"],
                "source_phase": data[idx].get("source_phase", "unknown"),
                "similarity": float(scores[0][i]),  # cosine similarity 0..1
            })
    return results

if __name__ == "__main__":
    data = load_data()
    if data:
        # Force rebuild
        if os.path.exists(INDEX_FILE):
            os.remove(INDEX_FILE)
        index = build_and_save_index(data)

        # Quick test
        query = "How to handle database ORM in Python?"
        print(f"\n>>> Searching: {query}")
        results = search(query, index, data, k=3)

        for r in results:
            print(f"[{r['rock_id']}] Similarity: {r['similarity']:.4f} ({r['source_phase']})")
            print(f"   {r['content'][:120]}...")
