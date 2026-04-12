import os
import json
import requests

# Set your local LLM API URL here. Assuming Ollama/LiteLLM standard OpenAI compatible endpoint.
LOCAL_API_URL = os.getenv("LOCAL_LLM_URL", "http://localhost:11434/v1") 
LOCAL_MODEL = os.getenv("LOCAL_LLM_MODEL", "deepseek-coder-v2")

def generate_prompts(code_chunk):
    """
    Generates 3 Russian prompts (base, medium, pro) for a given Lua code chunk.
    """
    prompt = f"""### TASK:
Act as a reverse-engineering AI. Analyze the following Lua/Luau code chunk and generate 3 prompts that would instruct a model to generate this exact code.
CRITICAL CONSTRAINT: ALL 3 GENERATED PROMPTS MUST BE IN RUSSIAN LANGUAGE ONLY.

### LEVELS:
1. "prompt_base": Very detailed and specific instruction in Russian. Mention any local functions, mathematics, variables, or structure explicitly.
2. "prompt_medium": A medium level, human-like instruction in Russian. Like a user story describing the logic.
3. "prompt_pro": A raw, abstract, and direct command in Russian (e.g., "Implement an addition function").

### FORMAT:
Return ONLY a valid JSON object with the exact keys. Do not include markdown blocks like ```json.
Do not add any text before or after the JSON.

### CODE TO REVERSE ENGINEER:
```lua
{code_chunk}
```

### OUTPUT FORMAT EXAMPLE:
{{
  "prompt_base": "Напишите функцию на Lua...",
  "prompt_medium": "Создайте скрипт, который...",
  "prompt_pro": "Реализуйте..."
}}

### YOUR JSON RESPONSE:"""

    try:
        payload = {
            "model": LOCAL_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "temperature": 0.3, # Low temp for structured JSON and stable language output
            "max_tokens": 1024
        }
        
        response = requests.post(f"{LOCAL_API_URL}/chat/completions", json=payload, timeout=120)
        
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content'].strip()
            
            # Clean possible markdown wrap around JSON
            if content.startswith("```json"):
                content = content.replace("```json", "").replace("```", "").strip()
            elif content.startswith("```"):
                content = content.replace("```", "").strip()
                
            if "{" in content and "}" in content:
                content = content[content.find("{"):content.rfind("}")+1]
                
            try:
                data = json.loads(content)
                # Validate keys
                if all(k in data for k in ["prompt_base", "prompt_medium", "prompt_pro"]):
                    return data
            except json.JSONDecodeError:
                print("[Error] Failed to parse JSON from response.")
                return None
        else:
            print(f"[Error] API Response {response.status_code}: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[Error] Request to LLM failed: {e}")
        return None
    
    return None
