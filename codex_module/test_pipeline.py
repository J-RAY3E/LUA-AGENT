import sys
import numpy as np
import ast
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

from llm_coder import extract_structured_code
from ast_python_parser import validate_and_get_python_ast

def analyze_usage(code: str, target_libs: list) -> dict:
    usage = {lib: 0 for lib in target_libs}
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in usage:
                usage[node.id] += 1
            # Sometimes usage is like csv.reader where value is Name(id='csv')
            elif isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id in usage:
                usage[node.value.id] += 1
    except SyntaxError:
        for lib in target_libs:
            usage[lib] = code.count(lib)
    
    # Base fallback
    for lib in usage:
        if usage[lib] == 0 and lib in code:
            usage[lib] = 1
    return usage

def softmax(x, temperature=0.1):
    x = np.array(x)
    e_x = np.exp((x - np.max(x)) / temperature)
    return e_x / e_x.sum(axis=0)

def execute_pipeline(user_prompt: str):
    print("Step 1: Extracting Python Code via LLM (DeepSeek-Coder-V2)...")
    json_result = extract_structured_code(user_prompt, language="python")
    
    if not json_result:
        print("Pipeline Failed at Step 1.")
        return None
        
    print("\n✅ Step 1 Successful! JSON generated correctly.")
    
    # Init RAG semantic search matching
    print("\nInitializing RAG Engine for Semantic Matching...")
    import os
    import sys
    rag_module_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rag_module')
    if rag_module_path not in sys.path:
        sys.path.append(rag_module_path)
    from vector_engine import load_data, get_index, search
    
    rag_data = load_data()
    rag_index = get_index(rag_data) if rag_data else None

    print("\nLibraries Requested & Semantic RAG Mathing:")
    matched_libraries = {}
    for lib, desc in json_result.get("libraries", {}).items():
        if rag_index and rag_data:
            query = f"{lib} - {desc}"
            results = search(query, rag_index, rag_data, k=1)
            if results:
                best_match = results[0]["rock_id"]
                score = float(results[0]["similarity"])
                matched_libraries[lib] = {
                    "matched_lua_rock": best_match,
                    "confidence": score,
                    "original_desc": desc
                }
                print(f"    [RAG Match] Lua Library => {best_match} (Confidence: {score:.4f})")
            else:
                print("    [RAG Match] No matches found.")

    raw_code = json_result.get("code", "").replace('\r', '')

    # Step 1: usage
    usage = analyze_usage(raw_code, list(matched_libraries.keys()))

    # Step 2: filtrar
    filtered = {
        lib: data for lib, data in matched_libraries.items()
        if usage.get(lib, 0) > 0
    }

    # Step 3: re-rank
    alpha = 0.5
    for lib, data in filtered.items():
        freq = usage.get(lib, 0)
        data["adjusted_score"] = float(data["confidence"] * (1 + alpha * np.log1p(freq)))

    # Step 4: normalizar
    if filtered:
        scores = [d["adjusted_score"] for d in filtered.values()]
        probs = softmax(scores, temperature=0.1)

        # asignar prob
        for (lib, data), p in zip(filtered.items(), probs):
            data["prob"] = float(p)
            
    print("\nStep 2: Passing raw python code to AST validator...")
    python_ast = validate_and_get_python_ast(raw_code)
    
    if python_ast:
        print("\n✅ Step 2 Successful! Code valid and parsed into Python AST.")
        return {
            "ast": python_ast,
            "matched_lua_libraries": filtered,
            "extracted_functions": json_result.get("functions", {})
        }
    else:
        print("Pipeline Failed at Step 2.")
        return None

if __name__ == "__main__":
    test_prompt = "quiero que me hagas un script para leer datos tabulares y exponer una api web simple"
    print(f"Testing with natural prompt: '{test_prompt}'\n")
    
    output = execute_pipeline(test_prompt)
    
    print("\n" + "="*50)
    print("======== FINAL PIPELINE OUTPUT DICTIONARY ========")
    print("="*50 + "\n")
    if output:
        import json
        
        # Save to file
        output_file = "pipeline_output.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4)
            
        print(f"✅ Success! Pipeline output successfully saved to: {output_file}")
        print("\nPreview of output:")
        print(json.dumps(output, indent=4)[:500] + "\n... (truncated, see file for full output)")
    else:
        print("Pipeline failed to return a valid output.")
