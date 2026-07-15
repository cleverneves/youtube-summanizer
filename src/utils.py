import os


def read_transcript(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def save_summary(transcript_path: str, summary: str) -> str:
    base_name = os.path.splitext(os.path.basename(transcript_path))[0]
    output_path = os.path.join("outputs", f"{base_name}_summary.txt")
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(summary)
    return output_path
