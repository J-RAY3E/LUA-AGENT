import requests
import json
import os
import re

LOCAL_API_URL = os.getenv("LOCAL_LLM_URL", "http://127.0.0.1:8080/v1")
LOCAL_MODEL = os.getenv("LOCAL_LLM_MODEL", "bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF:Q3_K_S")

def extract_structured_code(prompt: str, language: str = "lua") -> dict:
    """
    Sends a request to DeepSeek-Coder to generate clean code and dictionary-style 
    documentation for libraries and functions.
    """
    
    system_prompt = f"""You are an elite {language.capitalize()} software engineer.
Your task is to write code according to the user's request. 

### STRICT RULES:
1. Provide the output STRICTLY as a valid JSON object.
2. The "code" field MUST NOT contain any comments (no //, no #, no --). The code must be completely clean because it will be parsed by an AST.
3. The "libraries" field MUST be a dictionary mapping the library name to its documented purpose.
4. The "functions" field MUST be a dictionary mapping the function name to its documented logic.
5. ANY NEWLINES inside strings MUST be correctly escaped as \\n to ensure valid JSON format.

### REQUIRED JSON STRUCTURE:
{{
  "code": "<source code without comments>",
  "libraries": {{
    "lib_name_1": "Description of why this library is needed."
  }},
  "functions": {{
    "func_name_1": "Description of the logic of this function."
  }}
}}

No markdown formatting outside the JSON block. Do not wrap the JSON in ```json."""

    payload = {
        "model": LOCAL_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "temperature": 0.1,  # Low temperature for strict structural adherence
        "max_tokens": 4000
    }

    print("Requesting code generation from LLM...")
    try:
        response = requests.post(f"{LOCAL_API_URL}/chat/completions", json=payload, timeout=300)
        
        if response.status_code == 200:
            message = response.json()['choices'][0]['message']
            content = (message.get('content') or '').strip()
            
            # DeepSeek-R1 models put their thinking in reasoning_content
            # and the actual answer in content. If content is empty,
            # try to extract JSON from reasoning_content as fallback.
            if not content:
                reasoning = (message.get('reasoning_content') or '').strip()
                if reasoning:
                    print("Note: Using reasoning_content (R1 thinking model detected)")
                    content = reasoning
            
            if not content:
                print("No content received from LLM.")
                return None
            
            # Strip <think>...</think> tags if present (R1 format)
            content_clean = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
            if not content_clean:
                content_clean = content  # fallback to full content if stripping removed everything
            
            # Use regex to extract JSON if the model ignores the "no markdown" rule
            match = re.search(r'\{.*\}', content_clean, re.DOTALL)
            if match:
                clean_json = match.group(0)
                try:
                    data = json.loads(clean_json, strict=False)
                    return data
                except json.JSONDecodeError as e:
                    print(f"Failed to parse JSON. Error: {e}")
                    print("Raw Content:", clean_json[:500])
            else:
                print("No JSON block found in response.")
                print("Raw Content:", content_clean[:500])
        else:
            print(f"Error {response.status_code}: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to local LLM server at", LOCAL_API_URL)
    except Exception as e:
        print(f"Unexpected error: {e}")
        
    return None

if __name__ == "__main__":
    # Test case to verify the prompt structure
    test_request = "Create a Python script that reads a CSV file and calculates the sum of a column named 'price'. Export the functions for future use."
    print(f"Testing with prompt: '{test_request}'\n")
    
    result = extract_structured_code(test_request, language="python")
    
    if result:
        print("====== PARSED OUTPUT ======")
        print("\n[LIBRARIES]")
        for lib, desc in result.get("libraries", {}).items():
            print(f" - {lib}: {desc}")
            
        print("\n[FUNCTIONS]")
        for func, desc in result.get("functions", {}).items():
            print(f" - {func}: {desc}")
            
        print("\n[CLEAN CODE]")
        print(result.get("code", ""))
        print("===========================")
