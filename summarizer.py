import requests
import json
import os
import glob

LOCAL_API_URL = os.getenv("LOCAL_LLM_URL", "http://localhost:8080/v1")
LOCAL_MODEL = os.getenv("LOCAL_LLM_MODEL", "Marlon81/Phi-3-mini-4k-instruct-Q5_K_M-GGUF:Q5_K_M")

def generate_structured_description(rock_data):
    rock_name = rock_data.get("rock_name", "Unknown")
    tags = ", ".join(rock_data.get("tags", []))
    raw_content = rock_data.get("raw_content", "")[:2500] 

    prompt = f"""### TASK:
Analyze the tool '{rock_name}' and return a JSON object with exactly 3 fields.

### CONSTRAINTS:
1. NO PROHIBITED WORDS: Do not use 'library', 'lib', 'package', 'module', 'wrapper', 'rock', 'software'.
2. NO REPETITIVE STARTS: Do not start any sentence with '{rock_name} is' or '{rock_name} provides'.
3. JSON STRUCTURE:
   - "phase1": Core functionality and primary technical capability.
   - "phase2": Technical focus, performance characteristics, or implementation detail.
   - "phase3": Ideal use case or target environment.
4. FORMAT: Return ONLY a valid JSON object. No markdown blocks, no extra text.

### TOOL DATA:
Name: {rock_name}
Tags: {tags}
Content: {raw_content}

### OUTPUT FORMAT EXAMPLE:
{{
  "phase1": "Accelerates file system indexing by utilizing parallel processing threads.",
  "phase2": "Leverages low-level I/O primitives to minimize memory footprint during large-scale operations.",
  "phase3": "Fits perfectly into automated backup systems where rapid change detection is mandatory."
}}

### YOUR JSON RESPONSE:"""

    try:
        payload = {
            "model": LOCAL_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "temperature": 0.2,
            "max_tokens": 400
        }
        response = requests.post(f"{LOCAL_API_URL}/chat/completions", json=payload, timeout=120)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content'].strip()
            if content.startswith("```json"):
                content = content.replace("```json", "").replace("```", "").strip()
            # Basic cleanup for some models that add text before/after JSON
            if "{" in content and "}" in content:
                content = content[content.find("{"):content.rfind("}")+1]
            return json.loads(content)
        else:
            print(f"Error for {rock_name}: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error processing {rock_name}: {e}")
        return None

def process_files():
    files = glob.glob("raw_data/*.json")
    import random
    random.shuffle(files)
    count = 0
    for file_path in files:

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if "phase1" in data:
            print(f"Skipping {data['rock_name']}, already structured.")
            continue
            
        print(f"Processing {data['rock_name']}...")
        structured_data = generate_structured_description(data)
        
        if structured_data and all(k in structured_data for k in ["phase1", "phase2", "phase3"]):
            data.update(structured_data)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Successfully updated {data['rock_name']} with structured phases.")
            count += 1
        else:
            print(f"Failed to get valid JSON for {data['rock_name']}")

if __name__ == "__main__":
    process_files()
