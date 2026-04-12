from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import sys
import json

load_dotenv()

app = Flask(__name__)
CORS(app)

# Import dari LUA-AGENT
try:
    from rag_module.vector_engine import load_data, get_index, search
    from codex_module.llm_coder import extract_structured_code
    from codex_module.ast_lua_parser import validate_and_reconstruct_lua
    print("✓ Successfully imported LUA-AGENT modules")
except ImportError as e:
    print(f"✗ Error importing modules: {e}")
    sys.exit(1)

# Config
LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://127.0.0.1:1234/v1")

print(f"LM Studio URL: {LM_STUDIO_URL}")

# Load RAG data at startup
print("Loading RAG data...")
try:
    data = load_data()
    index = get_index(data)
    print(f"✓ Loaded {len(data)} fragments from LUA-AGENT database")
except Exception as e:
    print(f"✗ Error loading RAG data: {e}")
    data = []
    index = None

# ===== API ENDPOINTS =====

@app.route('/generate', methods=['POST'])
def generate_code():
    """Generate Lua code dengan RAG context"""
    try:
        request_data = request.json
        prompt = request_data.get('prompt', '')
        use_rag = request_data.get('use_rag', True)
        
        print(f"Generating code for: {prompt}")
        
        # Get RAG context
        rag_context = ""
        if use_rag and data and index:
            print("Fetching RAG context...")
            results = search(prompt, index, data, k=3)
            rag_context = "\nRelevant Lua libraries:\n"
            for r in results:
                rag_context += f"- {r['rock_id']}: {r['content'][:100]}\n"
        
        # Combine prompt dengan RAG context
        full_prompt = prompt
        if rag_context:
            full_prompt = f"{prompt}\n{rag_context}"
        
        # Generate code dengan LM Studio
        code_result = extract_structured_code(full_prompt, language="lua")
        
        if not code_result:
            return jsonify({
                "error": "Code generation failed",
                "code": "-- Error: Could not generate code"
            }), 500
        
        code = code_result.get('code', '')
        libraries = code_result.get('libraries', {})
        functions = code_result.get('functions', {})
        
        # Validate Lua syntax
        validated = validate_and_reconstruct_lua(code)
        
        return jsonify({
            "code": validated or code,
            "libraries": libraries,
            "functions": functions,
            "syntax_valid": validated is not None,
            "status": "success"
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            "error": str(e),
            "code": f"-- Error: {str(e)}"
        }), 500

@app.route('/search', methods=['POST'])
def search_libraries():
    """Search Lua libraries dari RAG database"""
    try:
        request_data = request.json
        query = request_data.get('query', '')
        k = request_data.get('k', 5)
        
        print(f"Searching for: {query}")
        
        if not data or not index:
            return jsonify({
                "error": "RAG data not loaded",
                "results": []
            }), 500
        
        # Search
        results = search(query, index, data, k=k)
        
        formatted = []
        for r in results:
            formatted.append({
                "library_name": r['rock_id'],
                "similarity_score": round(r['similarity'], 3),
                "description": r['content'][:300],
                "source_phase": r['source_phase']
            })
        
        return jsonify({
            "results": formatted,
            "status": "success"
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            "error": str(e),
            "results": []
        }), 500

@app.route('/validate', methods=['POST'])
def validate_code():
    """Validate Lua syntax"""
    try:
        request_data = request.json
        code = request_data.get('code', '')
        
        print("Validating Lua code...")
        
        result = validate_and_reconstruct_lua(code)
        
        return jsonify({
            "valid": result is not None,
            "clean_code": result or code,
            "status": "success"
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            "error": str(e),
            "valid": False
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        "status": "ok",
        "rag_loaded": data is not None and len(data) > 0,
        "lm_studio_url": LM_STUDIO_URL
    })

if __name__ == '__main__':
    print("\n" + "="*50)
    print("LUA-AGENT Backend Server")
    print("="*50)
    print("Starting on http://localhost:5000")
    print("="*50 + "\n")
    app.run(debug=True, port=5000, use_reloader=False)