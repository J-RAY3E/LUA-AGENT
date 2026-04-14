import sys
import time
from rag_module.vector_engine import load_data, get_index, search
from codex_module.llm_coder import extract_raw_lua_code

def test_sota_capabilities():
    print("======================================================")
    print(" SOTA VALIDATION SUITE: RAG + CODEX MODULE TESTING    ")
    print("======================================================\n")
    
    # 1. Initialize RAG
    print("[INIT] Loading Lexical RAG data...")
    rag_data = load_data()
    rag_index = get_index(rag_data)
    print(f"       -> Loaded {len(rag_data)} entities in cache.\n")
    
    tests = [
        {
            "name": "TEST 1: Safe Stack & Closures",
            "prompt": "Create a C wrapper for a Lua function using `lua_pushcclosure`. Before pushing, ensure the stack has enough space using `lua_checkstack`. Handle any failure gracefully."
        },
        {
            "name": "TEST 2: Metatable Object Orientation",
            "prompt": "Implement a custom userdata type. Use `luaL_newmetatable` to create a metatable, and map its `__index` metamethod back to itself using `lua_pushvalue` and `lua_settable`."
        },
        {
            "name": "TEST 3: Advanced Iteration & Error Handling",
            "prompt": "Iterate through a table at an absolute index using `lua_absindex` and `lua_next`. If an error occurs, properly throw a Lua error with `lua_error`."
        }
    ]
    
    for i, test in enumerate(tests):
        print(f"\n######################################################")
        print(f" RUNNING {test['name']}")
        print(f"######################################################")
        print(f"  PROMPT: {test['prompt']}\n")
        
        # Search
        results = search(test['prompt'], rag_index, rag_data, k=3)
        rag_context = ""
        found_entities = []
        if results:
            for r in results:
                content = r.get('content', '')
                rock_id = r.get('rock_id', 'unknown')
                found_entities.append(rock_id)
                rag_context += f"--- START ENTITY: {rock_id} ---\n{content}\n--- END ENTITY ---\n\n"
        print(f"  [RAG] Injected Lexical Entities: {found_entities}")
        
        full_prompt = (
            f"Task: {test['prompt']}\n\n"
            "Requirements:\n"
            "1. Write highly accurate C/Lua code based on the technical context provided.\n"
            "2. Output the fully functional code wrapped in ```c or ```lua blocks.\n"
            f"Technical Context:\n{rag_context}\n"
        )
        
        # Invoke LLM
        print(f"  [LLM] Generating logical CoT response...")
        start_time = time.time()
        generated_code = extract_raw_lua_code(full_prompt)
        elapsed = time.time() - start_time
        
        print("\n  ==== MODEL RESPONSE ====")
        print(f"  (Generated in {elapsed:.2f} seconds)\n")
        print(generated_code)
        
        # Add a short delay to prevent socket overload
        time.sleep(2)

if __name__ == "__main__":
    test_sota_capabilities()
