import sys
import time
from rag_module.vector_engine import load_data, get_index, search
from codex_module.llm_coder import extract_raw_lua_code

def test_roblox_capabilities():
    print("======================================================")
    print(" GAME DEV TEST: ROBLOX / LUAU LOGIC                   ")
    print("======================================================\n")
    
    # 1. Initialize RAG
    print("[INIT] Loading Lexical RAG data...")
    rag_data = load_data()
    rag_index = get_index(rag_data)
    print(f"       -> Loaded {len(rag_data)} entities in cache.\n")
    
    # Roblox Prompt
    prompt = (
        "Create a Roblox script (Luau) that detects when a player touches a Part. "
        "The script should change the Part's Color to Red, wait for 2 seconds, "
        "and then change it back to its original color. Use the Task library."
    )
    
    print(f"  PROMPT: {prompt}\n")
    
    # Search
    results = search(prompt, rag_index, rag_data, k=3)
    rag_context = ""
    found_entities = []
    if results:
        for r in results:
            found_entities.append(r.get('rock_id', 'unknown'))
            rag_context += f"--- START ENTITY: {r.get('rock_id')} ---\n{r.get('content')}\n--- END ENTITY ---\n\n"
    
    print(f"  [RAG] Injected Lexical Entities: {found_entities}")
    if not found_entities:
        print("  [NOTE] No Roblox entities found in Wiki. The model will rely on its base training.")
        
    full_prompt = (
        f"Task: {prompt}\n\n"
        "Requirements:\n"
        "1. Write valid Roblox Luau code.\n"
        "2. Output code inside ```lua blocks.\n"
        f"Technical Context from Wiki:\n{rag_context if rag_context else 'No specific Roblox docs found in local wiki.'}\n"
    )
    
    # Invoke LLM
    print(f"  [LLM] Generating Roblox script...")
    start_time = time.time()
    generated_code = extract_raw_lua_code(full_prompt)
    elapsed = time.time() - start_time
    
    print("\n  ==== MODEL RESPONSE ====")
    print(f"  (Generated in {elapsed:.2f} seconds)\n")
    print(generated_code)

if __name__ == "__main__":
    test_roblox_capabilities()
