import requests
import json
import os
import re

LOCAL_API_URL = os.getenv("LOCAL_LLM_URL", "http://127.0.0.1:1234/v1")
LOCAL_MODEL = os.getenv("LOCAL_LLM_MODEL", "deepseek-r1-distill-qwen-1.5b")

def extract_structured_code(prompt: str, language: str = "lua") -> dict:
    # Default return jika terjadi kegagalan total
    fallback = {
        "code": "-- Error: Failed to parse LLM output",
        "libraries": {},
        "functions": {}
    }
    
    system_prompt = f"""You are an elite {language.capitalize()} developer. 
Return ONLY a valid JSON object. No markdown, no backticks, no text before/after JSON.
Format:
{{
  "code": "source code here",
  "libraries": {{}},
  "functions": {{}}
}}"""

    payload = {
        "model": LOCAL_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0,
        "max_tokens": 2048
    }

    try:
        response = requests.post(f"{LOCAL_API_URL}/chat/completions", json=payload, timeout=60)
        if response.status_code != 200:
            return fallback

        content = response.json()['choices'][0]['message'].get('content', '')
        
        # 1. Bersihkan tag thinking (<think>...</think>)
        content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()

        # 2. STRATEGI GREEDY: Mencari { paling awal sampai } paling akhir
        # Ini akan membuang teks "Extra data" yang muncul di bawah JSON
        match = re.search(r'(\{.*\})', content, re.DOTALL)
        
        if not match:
            # Jika tidak ketemu kurung kurawal, kirim teks mentah sebagai kode
            return {"code": content, "libraries": {}, "functions": {}}

        json_str = match.group(1)

        # 3. PEMBERSIHAN KHUSUS DEEPSEEK
        # Ganti backticks (`) yang sering terselip di dalam value JSON
        json_str = json_str.replace('`', '"')
        
        # Hapus komentar // yang merusak standar JSON
        json_str = re.sub(r'//.*', '', json_str)

        try:
            # Gunakan strict=False untuk mentoleransi tab/newline fisik
            return json.loads(json_str, strict=False)
        except json.JSONDecodeError:
            # Jika masih gagal, lakukan pembersihan newline agresif
            try:
                # Ganti newline sungguhan menjadi literal \n
                json_str = re.sub(r'\n', '\\n', json_str)
                # Perbaiki struktur penutup yang mungkin ikut rusak
                json_str = json_str.replace('}\\n', '}').replace('",\\n', '",')
                return json.loads(json_str, strict=False)
            except:
                # Jika tetap gagal, ambil field 'code' secara manual menggunakan regex
                code_match = re.search(r'"code":\s*"(.*?)"', json_str, re.DOTALL)
                code_val = code_match.group(1) if code_match else content
                return {"code": code_val, "libraries": {}, "functions": {"error": "JSON partially parsed"}}

    except Exception as e:
        print(f"Final Fallback Error: {e}")
        return fallback