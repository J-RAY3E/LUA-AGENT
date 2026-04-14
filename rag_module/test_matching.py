import json
import os
import sys
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Reconfigure encoding for Windows compatibility
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

    # ── Test cases: Explicit Python library matching ──
    tests = [
        # Data formats
        {"python_lib": "csv", "query": "CSV file parser for reading and writing delimited data", "expected_lua": "csv"},
        {"python_lib": "json", "query": "JSON serialization and deserialization library", "expected_lua": "yyjson"}, 
        {"python_lib": "xml", "query": "XML document parser that converts XML to native data structures", "expected_lua": "xml2lua"},
        {"python_lib": "PyYAML", "query": "YAML configuration file parser and emitter", "expected_lua": "yaml"},
        {"python_lib": "umsgpack", "query": "MessagePack binary serialization format", "expected_lua": "lua-MessagePack-lua53"}, 

        # Networking / Web
        {"python_lib": "requests", "query": "HTTP requests library for sending GET and POST requests", "expected_lua": "lua-requests-async"}, 
        {"python_lib": "elasticsearch", "query": "Elasticsearch search engine client for indexing and querying documents", "expected_lua": "elasticsearch"},
        {"python_lib": "redis-py", "query": "Redis client for connecting and interacting with Redis data store", "expected_lua": "moon-redis"},
        {"python_lib": "FastAPI / Flask", "query": "Web framework for building APIs and applications", "expected_lua": "lapis-community"},

        # OOP / Class systems
        {"python_lib": "built-in classes", "query": "Object-oriented programming class system with inheritance and mixins", "expected_lua": "middleclass"},

        # Crypto / Security
        {"python_lib": "cryptography", "query": "OpenSSL cryptographic operations including TLS and certificate handling", "expected_lua": "openssl"},
        {"python_lib": "PyJWT", "query": "JWT token creation and verification for authentication", "expected_lua": "lua-resty-jwt-verification"}, 

        # Development tools
        {"python_lib": "pdb", "query": "Remote debugging tool for stepping through code execution", "expected_lua": "MobDebug"},
        {"python_lib": "Sphinx", "query": "Code documentation generator", "expected_lua": "ldoc"},
        {"python_lib": "pylint / flake8", "query": "Static code analysis and linting tool", "expected_lua": "lglob"}, 

        # Date/Time
        {"python_lib": "datetime / pytz", "query": "Timezone handling and date-time conversion library", "expected_lua": "luatz"},

        # Text / String
        {"python_lib": "unicodedata", "query": "UTF-8 string manipulation and Unicode text processing", "expected_lua": "lutf8"},
        {"python_lib": "colorama", "query": "ANSI terminal color and formatting escape sequences", "expected_lua": "eansi"},

        # Data structures
        {"python_lib": "bitarray", "query": "Bit array and bitwise operations data structure", "expected_lua": "bitarray"},
        {"python_lib": "collections.deque", "query": "Linked list data structure implementation", "expected_lua": "linked-list"},
        {"python_lib": "pygtrie", "query": "Prefix tree (trie) data structure for efficient string lookups", "expected_lua": "prefix_tree"},

        # Build / Package
        {"python_lib": "pip / poetry", "query": "Package manager and dependency resolver", "expected_lua": "loverocks"},
    ]

    output_lines = []
    def log(msg=""):
        print(msg)
        output_lines.append(str(msg))

    log("=" * 70)
    log("  LUAREDACTOR RAG - Cross-Language Matching Test Suite")
    log("=" * 70)

    passed = 0
    total_with_expected = 0
    k = 5  # search top-5 but check top-3

    for test in tests:
        query = test["query"]
        expected = test["expected_lua"]
        python_lib = test["python_lib"]
        
        results = search(query, index, data, k=k)
        top3_ids = [r["rock_id"] for r in results[:3]]
        top3_scores = [r["similarity"] for r in results[:3]]

        # Check pass/fail
        if expected:
            total_with_expected += 1
            hit = expected in top3_ids
            if hit:
                passed += 1
                status = "[PASS]"
            else:
                status = "[FAIL]"
        else:
            status = "[INFO]"

        log(f"\n{status} | Python Lib: {python_lib}")
        log(f"       | Query: {query[:70]}...")
        if expected:
            is_hit = "Yes" if expected in top3_ids else "No"
            log(f"       | Expected Lua: {expected} | Found in top-3: {is_hit}")
        for i, r in enumerate(results[:3], 1):
            marker = "->" if expected and r["rock_id"] == expected else "  "
            log(f"  {marker} {i}. [{r['rock_id']}] sim={r['similarity']:.4f} ({r['source_phase']})")
            log(f"       {r['content'][:100]}...")

    log("\n" + "=" * 70)
    if total_with_expected > 0:
        accuracy = passed / total_with_expected * 100
        log(f"  ACCURACY: {passed}/{total_with_expected} = {accuracy:.1f}%")
        log(f"  TARGET:   >=70%")
        if accuracy >= 70:
            log(f"  STATUS:   [PASSED]")
        else:
            log(f"  STATUS:   [NEEDS IMPROVEMENT]")
    log("=" * 70)

    with open("test_out.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines) + "\n")


if __name__ == "__main__":
    run_tests()
