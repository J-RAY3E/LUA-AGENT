import sys
from rag_module.vector_engine import load_data, get_index, search
from codex_module.llm_coder import extract_raw_lua_code

def test_hard_generation():
    print("========================================")
    print(" HARD TEST: Codex Module + Lexical RAG  ")
    print("========================================\n")
    
    # 1. Initialize RAG
    print("[1] Loading Lexical RAG data...")
    rag_data = load_data()
    rag_index = get_index(rag_data)
    print(f"    -> Loaded {len(rag_data)} entities in cache.\n")
    
    # 2. Hard Prompt
    prompt = (
        "Write a robust custom memory allocator in C that complies with the `lua_Alloc` signature. "
        "Create a state using `lua_newstate` passing your allocator block. "
        "Then manually interact with the state by creating a string object with `lua_pushstring` and "
        "use `luaL_addgsub` to replace a string. Finally, close the state properly."
    )
    print(f"[2] PROMPT: \n    {prompt}\n")
    
    # 3. Simulate Backend Search (app.py)
    print("[3] Searching Wiki Entities...")
    results = search(prompt, rag_index, rag_data, k=4)
    rag_context = ""
    if results:
        for r in results:
            content = r.get('content', '')
            rock_id = r.get('rock_id', 'unknown')
            rag_context += f"--- START ENTITY: {rock_id} ---\n{content}\n--- END ENTITY ---\n\n"
        print(f"    -> Injected entities: {[r.get('rock_id') for r in results]}\n")
    else:
        print("    -> No RAG context found.\n")
        
    full_prompt = (
        f"Task: {prompt}\n\n"
        "Requirements:\n"
        "1. Write valid code.\n"
        "2. Return ONLY the raw code string.\n"
        f"Technical Context:\n{rag_context}\n"
    )
    
    # 4. Invoke LLM Coder
    print("[4] Generating CoT Code via Local Qwen-Coder...")
    generated_code = extract_raw_lua_code(full_prompt)
    
    print("\n========================================")
    print("             MODEL RESPONSE             ")
    print("========================================")
    print(generated_code)
    print("========================================")

if __name__ == "__main__":
    test_hard_generation()
