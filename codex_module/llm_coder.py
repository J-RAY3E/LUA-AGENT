import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

LOCAL_LLM_URL = os.getenv("LOCAL_LLM_URL", "http://127.0.0.1:8080/v1")
LOCAL_LLM_MODEL = os.getenv("LOCAL_LLM_MODEL", "qwen2.5-coder-7b-instruct-gguf")

def chat_local_llm(messages, temperature=0.2, max_tokens=2048):
    """
    Sends a chat request to the local LLM.
    """
    url = f"{LOCAL_LLM_URL}/chat/completions"
    payload = {
        "model": LOCAL_LLM_MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"[LLM] Connection error: {e}")
        return f"-- Error: LLM connection failed: {e}"

def extract_raw_lua_code(prompt_text: str) -> str:
    """
    Generates exact Lua code using a segmenting (Chain of Thought) approach for the Qwen Coder model.
    """
    
    # SYSTEM PROMPT forces the model to PLAN FIRST, THEN WRITE.
    system_prompt = (
        "You are an expert Lua and C-API Developer operating in a strict codebase.\n"
        "You are provided with perfect, entity-level Documentation retrieved from the Wiki.\n"
        "You MUST solve the user's prompt by taking these exact steps:\n"
        "1. Start your response with a brief technical outline inside a block like `// PLAN: ...`.\n"
        "2. Review the Technical Context provided in the prompt to ensure exact signature compliance.\n"
        "3. Output the fully functional Lua code wrapped in ```lua ... ``` blocks.\n"
        "4. DO NOT write unrelated tutorial text outside the PLAN and CODE blocks.\n"
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt_text}
    ]
    
    # Call the model
    print("  [Codex] Requesting code generation (This may take a moment)...")
    raw_response = chat_local_llm(messages)
    
    if raw_response.startswith("-- Error"):
        return raw_response
        
    # Extract only the code inside the ```lua blocks to keep it clean.
    import re
    code_blocks = re.findall(r"```lua\n(.*?)\n```", raw_response, re.DOTALL)
    
    if code_blocks:
        # Join all generated lua blocks (in case it segmented functions)
        return "\n\n".join(code_blocks)
    elif "```" in raw_response:
        # Fallback if the model forgot 'lua' tag
        fallback = re.findall(r"```\n(.*?)\n```", raw_response, re.DOTALL)
        if fallback:
            return "\n\n".join(fallback)
            
    # If no blocks found, return the raw response, hoping it's pure code.
    return raw_response
