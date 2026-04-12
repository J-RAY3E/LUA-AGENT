import os
import json
from datasets import load_dataset
from chunker import chunk_lua_code
from local_llm import generate_prompts

def run_pipeline(output_file="synthetic_luau_prompts.jsonl", max_samples=None):
    print("Loading dataset 'TorpedoSoftware/the-luau-stack' (Train Split)...")
    try:
        # Load dataset with streaming to avoid massive memory usage immediately
        dataset = load_dataset('TorpedoSoftware/the-luau-stack', split='train', streaming=True)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return

    count = 0
    # Append mode so it can run iteratively over time
    with open(output_file, 'a', encoding='utf-8') as f:
        for row in dataset:
            if max_samples and count >= max_samples:
                break
                
            file_content = row.get("file_content", "")
            if not file_content:
                continue
                
            # Chunk the file content into independent logical blocks
            chunks = chunk_lua_code(file_content)
            
            for chunk in chunks:
                # Basic length filters to ensure chunk is useful
                if len(chunk) < 20 or len(chunk) > 3000:
                    continue
                    
                print(f"Generating Russian prompts for chunk of {len(chunk)} characters...")
                prompts = generate_prompts(chunk)
                
                if prompts:
                    record = {
                        "code_chunk": chunk,
                        "prompt_base": prompts["prompt_base"],
                        "prompt_medium": prompts["prompt_medium"],
                        "prompt_pro": prompts["prompt_pro"]
                    }
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
                    f.flush()
                    print("  -> Success! Generated 3 Russian prompts.")
                    count += 1
                else:
                    print("  -> Failed to generate well-formed JSON from model. Skipping chunk.")
                    
                if max_samples and count >= max_samples:
                    break

if __name__ == "__main__":
    # Test setting to generate 10 samples to verify format initially
    print("Starting Synthetic Data Pipeline (Test Mode: 10 samples limit)")
    run_pipeline("test_synthetic_data.jsonl", max_samples=10)
    print("Execution complete. Check 'test_synthetic_data.jsonl' for results.")
