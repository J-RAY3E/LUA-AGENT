from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# ===== CONFIGURATION =====
LOCAL_LLM_URL = os.getenv("LOCAL_LLM_URL", "http://127.0.0.1:1234/v1")
LOCAL_LLM_MODEL = os.getenv("LOCAL_LLM_MODEL", "deepseek-r1-distill-qwen-1.5b")

print(f"⚙️  Config: Using LLM at {LOCAL_LLM_URL}")
print(f"⚙️  Config: Using Model {LOCAL_LLM_MODEL}")

# ===== IMPORT MODULES =====
rag_available = False
codex_available = False

# 1. Import RAG Module
try:
    from rag_module.vector_engine import load_data, get_index, search
    rag_available = True
    print("✓ Successfully imported RAG module")
except ImportError as e:
    print(f"⚠️  RAG module not found or error: {e}")
    print("   -> Search endpoint will be disabled.")
    # Dummy functions
    def load_data(): return []
    def get_index(data): return None
    def search(q, idx, data, k=3): return []

# 2. Import Codex Module
try:
    from codex_module.llm_coder import extract_raw_lua_code
    from codex_module.ast_lua_parser import validate_and_reconstruct_lua
    codex_available = True
    print("✓ Successfully imported Codex module")
except ImportError as e:
    print(f"⚠️  Codex module not found or error: {e}")
    print("   -> Generate/Validate endpoints will fail.")
    # Dummy functions
    def extract_raw_lua_code(p): return "-- Error: Module missing"
    def validate_and_reconstruct_lua(c): return None

# ===== INITIALIZATION =====
rag_data = []
rag_index = None

if rag_available:
    print("📚 Loading RAG data...")
    try:
        rag_data = load_data()
        rag_index = get_index(rag_data)
        print(f"✓ Loaded {len(rag_data)} fragments into memory")
    except Exception as e:
        print(f"✗ Error loading RAG data: {e}")
        rag_data = []
        rag_index = None

# ===== API ENDPOINTS =====

@app.route('/generate', methods=['POST'])
def generate_code():
    """
    Generates CLEAN Lua code (Raw String) using LLM with optional RAG context.
    Expects JSON: { "prompt": "...", "use_rag": true/false }
    Returns JSON: { "code": "raw lua code string", "status": "success" }
    """
    if not codex_available:
        return jsonify({"error": "Codex module not loaded"}), 503

    try:
        request_data = request.json
        if not request_data or 'prompt' not in request_data:
            return jsonify({"error": "Missing 'prompt' in request body"}), 400

        prompt = request_data.get('prompt', '')
        use_rag = request_data.get('use_rag', True)
        
        print(f"\n[GENERATE] Received prompt: {prompt[:50]}...")
        
        # 1. Build Context from RAG (Optional)
        rag_context = ""
        if use_rag and rag_data and rag_index:
            try:
                results = search(prompt, rag_index, rag_data, k=3)
                if results:
                    rag_context = "\n\nRelevant Lua Context from Database:\n"
                    for r in results:
                        content = r.get('content', r.get('text', ''))
                        rock_id = r.get('rock_id', r.get('source', 'unknown'))
                        rag_context += f"- [{rock_id}]: {content[:150]}...\n"
                    print(f"[RAG] Found {len(results)} relevant contexts.")
            except Exception as e:
                print(f"[RAG] Search error: {e}")
                rag_context = "" 
        
        # 2. Construct Final Prompt for RAW CODE
        # Notice: We explicitly ask for NO JSON, NO Markdown
        full_prompt = (
            f"Task: {prompt}\n\n"
            "Requirements:\n"
            "1. Write valid Lua code.\n"
            "2. Include concise inline comments ('--') for clarity.\n"
            "3. Return ONLY the raw Lua code string.\n"
            "4. DO NOT wrap in JSON.\n"
            "5. DO NOT use Markdown blocks (no ```lua).\n"
            f"{rag_context}"
        )
        
        # 3. Call LLM to get Raw Code
        print("[LLM] Generating raw code...")
        raw_code = extract_raw_lua_code(full_prompt)
        
        if not raw_code or raw_code.startswith("-- Error"):
            return jsonify({
                "error": "LLM returned empty or invalid response",
                "code": "-- Error: Generation failed"
            }), 500
        
        # 4. Optional: Syntax Validation Check (Does not modify code, just checks validity)
        syntax_valid = False
        try:
            if codex_available:
                # We check validity but still return the original raw_code 
                # to preserve comments and formatting exactly as generated
                parsed = validate_and_reconstruct_lua(raw_code)
                syntax_valid = (parsed is not None)
        except Exception as e:
            print(f"[VALIDATE] Error during validation: {e}")

        print("[SUCCESS] Code generated successfully.")
        
        # Return simple structure for Extension
        return jsonify({
            "code": raw_code,
            "syntax_valid": syntax_valid,
            "status": "success"
        })
        
    except Exception as e:
        print(f"[ERROR] Exception in /generate: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "error": str(e),
            "code": f"-- Server Error: {str(e)}"
        }), 500

@app.route('/search', methods=['POST'])
def search_libraries():
    """Search Lua libraries from RAG database"""
    if not rag_available or not rag_data:
        return jsonify({"error": "RAG system not initialized", "results": []}), 503

    try:
        request_data = request.json
        if not request_data or 'query' not in request_data:
            return jsonify({"error": "Missing 'query'"}), 400

        query = request_data.get('query', '')
        k = request_data.get('k', 5)
        
        print(f"\n[SEARCH] Query: {query}")
        results = search(query, rag_index, rag_data, k=k)
        
        formatted_results = []
        for r in results:
            formatted_results.append({
                "library_name": r.get('rock_id', r.get('source', 'unknown')),
                "similarity_score": round(float(r.get('similarity', r.get('score', 0))), 3),
                "description": r.get('content', r.get('text', ''))[:300],
                "source_phase": r.get('source_phase', 'N/A')
            })
        
        return jsonify({"results": formatted_results, "status": "success"})
        
    except Exception as e:
        print(f"[ERROR] Exception in /search: {str(e)}")
        return jsonify({"error": str(e), "results": []}), 500

@app.route('/validate', methods=['POST'])
def validate_code():
    """Validates Lua code syntax"""
    if not codex_available:
        return jsonify({"error": "Codex module not loaded"}), 503

    try:
        request_data = request.json
        if not request_data or 'code' not in request_data:
            return jsonify({"error": "Missing 'code'"}), 400
            
        code = request_data.get('code', '')
        result = validate_and_reconstruct_lua(code)
        is_valid = result is not None
        
        return jsonify({
            "valid": is_valid,
            "clean_code": result if result else code,
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": str(e), "valid": False}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "ok",
        "rag_loaded": rag_available and len(rag_data) > 0,
        "codex_loaded": codex_available,
        "llm_url": LOCAL_LLM_URL,
        "model": LOCAL_LLM_MODEL
    })

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 LUA-AGENT Backend Server Starting...")
    print(f"🌍 Endpoint: http://localhost:5000")
    print(f"🔌 LLM Connected: {LOCAL_LLM_URL}")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000, use_reloader=False)