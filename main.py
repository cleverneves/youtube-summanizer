from dotenv import load_dotenv
from src.utils import read_transcript
from src.summarizer import summarize

load_dotenv()

transcript = read_transcript("transcripts/transcription.txt")
summary = summarize(transcript)

print(summary)
