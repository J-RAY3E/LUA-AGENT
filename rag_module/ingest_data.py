import json
import glob
import os

def prepare_rag_data():
    raw_files = glob.glob("raw_data/*.json")
    master_index = []

    print(f"Ingesting from {len(raw_files)} files...\n")

    skipped = 0
    for file_path in raw_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Only process if phases exist
            if "phase1" not in data:
                skipped += 1
                continue

            rock_name = data["rock_name"]

            # ── Individual phase documents ──
            for p_key in ["phase1", "phase2", "phase3"]:
                original_text = data[p_key]

                # Mask rock name to prevent name-bias in semantic search
                masked_text = original_text
                masked_text = masked_text.replace(rock_name, "This tool")
                masked_text = masked_text.replace(rock_name.lower(), "this tool")
                masked_text = masked_text.replace(rock_name.upper(), "THIS TOOL")
                # Also mask common variations (e.g. "lua-csv" -> "this tool")
                for variant in [f"lua-{rock_name}", f"lua_{rock_name}", f"{rock_name}.lua"]:
                    masked_text = masked_text.replace(variant, "this tool")

                doc = {
                    "rock_id": rock_name,
                    "content": original_text,
                    "semantic_content": masked_text,
                    "source_phase": p_key,
                    "tags": data.get("tags", []),
                    "url": data.get("source", ""),
                }
                master_index.append(doc)

            # ── Combined document (all 3 phases) ──
            combined = f"{data['phase1']}. {data['phase2']}. {data['phase3']}"
            combined_masked = combined
            combined_masked = combined_masked.replace(rock_name, "This tool")
            combined_masked = combined_masked.replace(rock_name.lower(), "this tool")

            master_index.append({
                "rock_id": rock_name,
                "content": combined,
                "semantic_content": combined_masked,
                "source_phase": "combined",
                "tags": data.get("tags", []),
                "url": data.get("source", ""),
            })

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    with open("master_index.json", "w", encoding="utf-8") as f:
        json.dump(master_index, f, indent=2, ensure_ascii=False)

    libs_processed = len(master_index) // 4  # 3 phases + 1 combined per lib
    print(f"Master Index created: {len(master_index)} fragments from ~{libs_processed} libraries")
    if skipped:
        print(f"Skipped {skipped} files without phases (run summarizer.py first)")


if __name__ == "__main__":
    prepare_rag_data()
