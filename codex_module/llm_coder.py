import requests
import re
import os

# Configuration
LOCAL_API_URL = os.getenv("LOCAL_LLM_URL", "http://127.0.0.1:1234/v1")
LOCAL_MODEL = os.getenv("LOCAL_LLM_MODEL", "deepseek-r1-distill-qwen-1.5b")

def extract_raw_lua_code(prompt: str) -> str:
    """
    Sends a prompt to the local LLM and extracts ONLY the raw Lua code.
    Removes Markdown blocks, thinking tags, and extra text.
    Returns a clean string ready for insertion into an editor.
    """
    system_prompt = """You are an expert Lua developer.
Your task is to write Lua code based on the user's request.

CRITICAL RULES:
1. Return ONLY the raw Lua code.
2. DO NOT wrap the code in JSON.
3. DO NOT use Markdown code blocks (no ```lua or ```).
4. DO NOT add explanations before or after the code.
5. Include concise inline comments ('--') for clarity.
6. Start directly with 'local' or 'function'."""

    payload = {
        "model": LOCAL_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1, # Low temperature for consistent code
        "max_tokens": 1024
    }

    try:
        # Send request to LM Studio
        response = requests.post(f"{LOCAL_API_URL}/chat/completions", json=payload, timeout=60)
        
        if response.status_code != 200:
            return f"-- Error: API Request Failed (Status {response.status_code})"

        # Extract raw content
        raw_content = response.json()['choices'][0]['message'].get('content', '')
        
        #CLEANING PROCESS 
        # 1. Remove <think> tags (Specific to DeepSeek R1 models)
        clean_content = re.sub(r'<think>.*?</think>', '', raw_content, flags=re.DOTALL)
        
        # 2. Remove Markdown code blocks if the model ignores instructions
        clean_content = re.sub(r'^```lua\s*', '', clean_content, flags=re.MULTILINE)
        clean_content = re.sub(r'^```\s*', '', clean_content, flags=re.MULTILINE)
        clean_content = re.sub(r'\s*```$', '', clean_content, flags=re.MULTILINE)
        
        # 3. Strip leading/trailing whitespace
        clean_content = clean_content.strip()
        
        # 4. Final check: If empty, return error
        if not clean_content:
            return "-- Error: LLM returned empty content"
            
        return clean_content

    except requests.exceptions.ConnectionError:
        return "-- Error: Could not connect to LM Studio. Is it running?"
    except Exception as e:
        print(f"Error in llm_coder: {e}")
        return f"-- Error: {str(e)}"

def extract_structured_code(prompt: str, language: str = "lua") -> dict:
    """
    Wrapper for backward compatibility with app.py if it still expects a dict.
    However, for best results, use extract_raw_lua_code directly.
    """
    code = extract_raw_lua_code(prompt)
    return {
        "code": code,
        "libraries": [],
        "functions": [],
        "is_raw": True
    }