import json
import os
import sys
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Fix Windows encoding issue for emoji output
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuration
MODEL_NAME = 'all-MiniLM-L6-v2'
INDEX_FILE = "index.faiss"
DATA_FILE = "master_index.json"

model = SentenceTransformer(MODEL_NAME)


def search(query, index, data, k=5):
    """Search with cosine similarity. Returns top-k results."""
    query_vector = model.encode([query]).astype('float32')
    faiss.normalize_L2(query_vector)
    scores, indices = index.search(query_vector, k)

    results = []
    seen_rocks = set()
    for i in range(min(k * 2, indices.shape[1])):  # look at more to deduplicate
        idx = indices[0][i]
        if idx < len(data):
            rock_id = data[idx]["rock_id"]
            if rock_id not in seen_rocks:
                seen_rocks.add(rock_id)
                results.append({
                    "rock_id": rock_id,
                    "content": data[idx]["content"],
                    "source_phase": data[idx].get("source_phase", "?"),
                    "similarity": float(scores[0][i]),
                })
        if len(results) >= k:
            break
    return results


def run_tests():
    if not os.path.exists(INDEX_FILE) or not os.path.exists(DATA_FILE):
        print("Error: Run ingest_data.py and vector_engine.py first.")
        return

    index = faiss.read_index(INDEX_FILE)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # ── Test cases: (Python-style description, expected Lua library in top-3) ──
    tests = [
        # Data formats
        ("CSV file parser for reading and writing delimited data like Python csv module", "csv"),
        ("JSON serialization and deserialization library like Python json module", "yyjson"), 
        ("XML document parser that converts XML to native data structures like Python xml package", "xml2lua"),
        ("YAML configuration file parser and emitter like Python PyYAML", "yaml"),
        ("MessagePack binary serialization format like Python umsgpack", "lua-MessagePack-lua53"), 

        # Networking / Web
        ("HTTP requests library for sending GET and POST requests like Python requests module", "lua-requests-async"), 
        ("Elasticsearch search engine client for indexing and querying documents like Python elasticsearch client", "elasticsearch"),
        ("Redis client for connecting and interacting with Redis data store like Python redis-py", "moon-redis"),
        ("Web framework for building APIs and applications like Python FastAPI or Flask", "lapis-community"),

        # OOP / Class systems
        ("Object-oriented programming class system with inheritance and mixins like Python classes", "middleclass"),

        # Crypto / Security
        ("OpenSSL cryptographic operations including TLS and certificate handling like Python cryptography module", "openssl"),
        ("JWT token creation and verification for authentication like Python PyJWT", "lua-resty-jwt-verification"), 

        # Development tools
        ("Remote debugging tool for stepping through code execution like Python pdb", "MobDebug"),
        ("Code documentation generator like Python Sphinx or pydoc", "ldoc"),
        ("Static code analysis and linting tool like Python pylint or flake8", "lglob"), 

        # Date/Time
        ("Timezone handling and date-time conversion library like Python datetime and pytz", "luatz"),

        # Text / String
        ("UTF-8 string manipulation and Unicode text processing like Python unicodedata", "lutf8"),
        ("ANSI terminal color and formatting escape sequences like Python colorama", "eansi"),

        # Data structures
        ("Bit array and bitwise operations data structure like Python bitarray module", "bitarray"),
        ("Linked list data structure implementation like Python collections.deque", "linked-list"),
        ("Prefix tree (trie) data structure for efficient string lookups like Python pygtrie", "prefix_tree"),

        # Build / Package
        ("Package manager and dependency resolver like Python pip or poetry", "loverocks"),
    ]

    print("═" * 70)
    print("  LUAREDACTOR RAG — Cross-Language Matching Test Suite")
    print("═" * 70)

    passed = 0
    total_with_expected = 0
    k = 5  # search top-5 but check top-3

    for query, expected in tests:
        results = search(query, index, data, k=k)
        top3_ids = [r["rock_id"] for r in results[:3]]
        top3_scores = [r["similarity"] for r in results[:3]]

        # Check pass/fail
        if expected:
            total_with_expected += 1
            hit = expected in top3_ids
            if hit:
                passed += 1
                status = "✅ PASS"
            else:
                status = "❌ FAIL"
        else:
            status = "🔍 INFO"

        print(f"\n{status} | Query: {query[:70]}...")
        if expected:
            print(f"       Expected: {expected} | Found in top-3: {expected in top3_ids}")
        for i, r in enumerate(results[:3], 1):
            marker = "→" if expected and r["rock_id"] == expected else " "
            print(f"  {marker} {i}. [{r['rock_id']}] sim={r['similarity']:.4f} ({r['source_phase']})")
            print(f"       {r['content'][:100]}...")

    print("\n" + "═" * 70)
    if total_with_expected > 0:
        accuracy = passed / total_with_expected * 100
        print(f"  ACCURACY: {passed}/{total_with_expected} = {accuracy:.1f}%")
        print(f"  TARGET:   ≥70%")
        if accuracy >= 70:
            print(f"  STATUS:   ✅ PASSED")
        else:
            print(f"  STATUS:   ❌ NEEDS IMPROVEMENT")
    print("═" * 70)


if __name__ == "__main__":
    run_tests()
