from dotenv import load_dotenv
from src.utils import read_transcript, save_summary
from src.summarizer import summarize

load_dotenv()

TRANSCRIPT_PATH = "transcripts/transcription.txt"

transcript = read_transcript(TRANSCRIPT_PATH)
summary = summarize(transcript)

output_path = save_summary(TRANSCRIPT_PATH, summary)

print(summary)
print(f"\nSummary saved to: {output_path}")
