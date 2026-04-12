import sys
import json
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from llm_extractor import LLMExtractor
from chunker import Chunk

def run_test():
    extractor = LLMExtractor()
    
    test_text = """
### Library: StringUtils
This library provides helpful string tools.

#### `StringUtils.split(str, sep)`
Splits the string `str` using the separator `sep`.
If `sep` is not provided, it defaults to a space.
Returns: A table containing the split sub-strings, and the total count.

#### `StringUtils.to_uppercase(str)`
Converts all characters in `str` to uppercase format.
Returns: The uppercase string.
    """
    
    test_chunk = Chunk(
        source_file="StringUtils/README.md",
        section_header="### Library: StringUtils",
        text=test_text,
        line_range=(1, 15),
        rock_id="TestRock/1.0"
    )
    
    print("Testing extraction on chunk...")
    print("--------------------------------------------------")
    print("RAW INPUT CHUNK:")
    print(test_text.strip())
    print("--------------------------------------------------")
    print("Waiting for LLM...\n")
    
    results = extractor.extract(test_chunk)
    
    print("--------------------------------------------------")
    print("LLM PARSED RESULT:")
    print("--------------------------------------------------")
    if results:
        print(json.dumps(results, indent=4))
        
        # Save payload to file for inspection
        with open("llm_extractor_output.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
        print("\n✅ Successfully saved to: llm_extractor_output.json")
    else:
        print("Failed to parse anything. Received empty list.")

if __name__ == "__main__":
    run_test()
