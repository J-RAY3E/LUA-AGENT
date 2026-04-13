"""
query.py — Query interface for the Wiki Brain.

Answers complex questions against the compiled wiki.
The knowledge is already synthesized — not re-derived from raw chunks each time.
"""

import os
import json
from typing import List, Optional

from . import llm_client
from . import tools


def query(question: str, max_context_pages: int = 8,
          save_answer: bool = False) -> str:
    """
    Ask a question against the compiled wiki.

    Flow:
      1. Search the wiki for pages relevant to the question.
      2. Collect the top matching pages as context.
      3. Send the question + context to the LLM.
      4. Optionally save a good answer as a new wiki page.

    Args:
        question: The natural-language question.
        max_context_pages: Max number of wiki pages to include as context.
        save_answer: If True, save the answer as a new wiki concept page.

    Returns:
        The LLM's answer as a string.
    """
    print(f"\n  [?] Query: {question}")

    # Step 1: Search for relevant wiki pages
    # Extract key terms from the question for search
    search_terms = _extract_search_terms(question)
    print(f"    Search terms: {search_terms}")

    # Gather context from matching pages
    context_pages = []
    seen_files = set()

    for term in search_terms:
        matches = tools.search_wiki(term)
        for match in matches:
            fname = match["file"]
            if fname not in seen_files and len(context_pages) < max_context_pages:
                seen_files.add(fname)
                # Read the full page
                page_name = os.path.splitext(os.path.basename(fname))[0]
                content = tools.read_wiki_page(page_name)
                if content:
                    context_pages.append({
                        "file": fname,
                        "content": content[:2000],  # Cap per page
                    })

    # Also add a directory listing for additional context
    wiki_files = tools.list_wiki_files()
    directory_context = (
        f"Available entities: {', '.join(wiki_files.get('entities', []))}\n"
        f"Available concepts: {', '.join(wiki_files.get('concepts', []))}\n"
    )

    # Step 2: Build the prompt
    if context_pages:
        pages_text = "\n\n---\n\n".join(
            [f"### {p['file']}\n{p['content']}" for p in context_pages]
        )
        prompt = (
            f"You are a Lua knowledge expert. Answer the following question "
            f"using ONLY the wiki pages provided below.\n\n"
            f"If the answer is not in the wiki, say so clearly.\n\n"
            f"## Wiki Context\n{pages_text}\n\n"
            f"## Wiki Index\n{directory_context}\n\n"
            f"## Question\n{question}\n\n"
            f"## Answer"
        )
    else:
        prompt = (
            f"You are a Lua knowledge expert. The wiki has no pages matching "
            f"this question. Based on the wiki index below, suggest what "
            f"sources should be added to answer this question.\n\n"
            f"## Wiki Index\n{directory_context}\n\n"
            f"## Question\n{question}\n\n"
            f"## Answer"
        )

    print(f"    Context: {len(context_pages)} page(s)")

    # Step 3: Get the answer
    answer = llm_client.chat(prompt, temperature=0.2, max_tokens=1500)

    # Step 4: Optionally save as a wiki concept
    if save_answer and answer and len(answer) > 50:
        # Generate a page name from the question
        short_name = _question_to_page_name(question)
        content = (
            f"# {question}\n\n"
            f"**Type**: Query Answer  \n"
            f"**Question**: {question}  \n\n"
            f"## Answer\n{answer}\n\n"
            f"## Sources\n"
            + "\n".join([f"- [[{os.path.splitext(os.path.basename(p['file']))[0]}]]"
                         for p in context_pages])
            + "\n"
        )
        tools.write_draft(short_name, content, category="concepts")
        print(f"    [SAVED] Answer saved as draft: concepts/{short_name}")

    print(f"    [OK] Answer: {answer[:120]}...")
    return answer


def _extract_search_terms(question: str) -> List[str]:
    """
    Extract meaningful search terms from a question.
    Filters out common stop words.
    """
    stop_words = {
        "what", "how", "does", "is", "are", "do", "the", "a", "an",
        "in", "on", "at", "to", "for", "of", "with", "can", "could",
        "would", "should", "which", "where", "when", "who", "why",
        "this", "that", "these", "those", "it", "its", "and", "or",
        "but", "not", "from", "by", "was", "were", "been", "has",
        "have", "had", "will", "shall", "may", "might", "i", "me",
        "my", "we", "our", "you", "your", "they", "them", "their",
    }
    words = question.lower().split()
    terms = [w.strip("?.,!;:") for w in words if w.strip("?.,!;:") not in stop_words]
    # Also search for bigrams (two-word combos)
    bigrams = [f"{terms[i]} {terms[i+1]}" for i in range(len(terms) - 1)]

    # Return unique terms, longest first (bigrams tend to be more specific)
    all_terms = list(dict.fromkeys(bigrams + terms))
    return all_terms[:10]  # Cap at 10 terms


def _question_to_page_name(question: str) -> str:
    """Convert a question to a safe wiki page name."""
    import re
    name = question.lower()[:60]
    name = re.sub(r"[^a-z0-9\s]", "", name)
    name = re.sub(r"\s+", "-", name).strip("-")
    return f"query-{name}"
