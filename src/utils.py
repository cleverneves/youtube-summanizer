import os


def read_transcript(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Transcript file not found: '{file_path}'")

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip()

    if not content:
        raise ValueError(f"Transcript file is empty: '{file_path}'")

    return content


def save_summary(transcript_path: str, summary: str) -> str:
    os.makedirs("outputs", exist_ok=True)
    base_name = os.path.splitext(os.path.basename(transcript_path))[0]
    output_path = os.path.join("outputs", f"{base_name}_summary.txt")
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(summary)
    return output_path
