import os
import sys
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wiki import llm_client, tools
from . import validator

MAX_RETRY_ATTEMPTS = 3

def _extract_keywords(request: str) -> list:
    text = request.lower()
    
    stopwords = {
        "how", "to", "for", "in", "of", "on", "at", "by", "with", "without",
        "and", "or", "but", "so", "if", "then", "else", "when", "where",
        "what", "why", "who", "which", "is", "are", "was", "were", "be", "been",
        "do", "does", "did", "doing", "have", "has", "having", "can", "could",
        "will", "would", "should", "may", "might", "a", "an", "the", "this",
        "that", "these", "those", "some", "any", "no", "very", "just", "please",
        "help", "me", "my", "your", "code", "lua", "function", "make", "create",
        "script", "example", "show", "write", "generate", "build", "implement",
        "variable", "value", "number", "string", "data", "result", "list", "item"
    }
    
    words = re.findall(r"[a-z0-9_]{3,}", text)
    keywords = [w for w in words if w not in stopwords]
    
    seen = set()
    unique_keywords = []
    for kw in keywords:
        if kw not in seen:
            seen.add(kw)
            unique_keywords.append(kw)
    
    result = unique_keywords[:5]
    
    if not result:
        result = [w for w in words if len(w) > 3][:3]
    
    return result


def _fetch_wiki_context(keywords: list) -> list:
    context_docs = []
    seen_files = set()
    
    for keyword in keywords:
        if len(context_docs) >= 8 and len(keywords) > 1:
            break
            
        results = tools.search_wiki(keyword)
        if not results:
            continue

        for doc in results:
            file_path = doc.get("file", "")
            if not file_path or file_path in seen_files:
                continue
            
            seen_files.add(file_path)
            page_name = os.path.splitext(os.path.basename(file_path))[0]
            content = tools.read_wiki_page(page_name)
            
            if content:
                context_docs.append({
                    "name": page_name,
                    "content": content[:3000],
                })
                
            if len(context_docs) >= 8:
                break
        
        if len(context_docs) >= 8:
            break
    
    return context_docs


def generate_code(request: str, plan_result: dict = None, context_docs: list = None):
    if not context_docs:
        keywords = _extract_keywords(request)
        context_docs = _fetch_wiki_context(keywords)

    current_attempt = 0
    raw_code = ""

    while current_attempt < MAX_RETRY_ATTEMPTS:
        current_attempt += 1

        raw_code = _generate_raw_code_internal(request, plan_result or {}, context_docs)

        if not raw_code:
            break

        cleaned_code = validator.validate_and_reconstruct_lua(raw_code)

        if cleaned_code:
            return cleaned_code

        if current_attempt == MAX_RETRY_ATTEMPTS:
            return raw_code

        correction_prompt = f"""
You are a Lua expert. The previous code generation resulted in a SYNTAX ERROR.
The original request was: "{request}"

The generated code that caused the error:
{raw_code}

Please provide ONLY the corrected Lua code block inside ```lua ... ```.
Do NOT include explanations. Fix the syntax errors only.
Ensure the code follows standard Lua 5.5 practices.
"""
        correction_response = llm_client.chat(correction_prompt, temperature=0.2, max_tokens=2048)

        match = re.search(r"```lua\s*(.*?)\s*```", correction_response, re.DOTALL | re.IGNORECASE)
        raw_code = match.group(1).strip() if match else correction_response.strip()

    return raw_code


def _generate_raw_code_internal(request: str, plan_result: dict, context_docs: list = None):
    evidence_str = ""
    
    if context_docs:
        for doc in context_docs:
            name = doc['name']
            content = doc['content']
            evidence_str += f"\n--- DOCUMENTATION: {name} ---\n{content}\n"

    steps_str = "\n".join([f"- {step}" for step in plan_result.get("steps", [])])
    modules_str = ", ".join(plan_result.get("required_modules", []))

    system_prompt = """
You are an advanced Lua coding assistant.

CRITICAL INSTRUCTIONS:
1. Output ONLY the code block in ```lua ... ```. No markdown outside the code block.
2. Use standard Lua 5.5 best practices.
3. Always end with 'return <expression>' if a result is expected.
"""

    user_prompt = f"""
Task: {request}
Plan: {steps_str if steps_str else "No specific plan provided."}
Modules: {modules_str if modules_str else "Standard"}

Context:
{evidence_str if evidence_str else "None"}

Write the code now.
"""

    raw_response = llm_client.chat(system=system_prompt, prompt=user_prompt, temperature=0.2, max_tokens=2048)

    match = re.search(r"```lua\s*(.*?)\s*```", raw_response, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else raw_response.strip()


def save_code(code: str, filename: str, directory="projects"):
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    return filepath