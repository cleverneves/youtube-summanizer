import sys
from dotenv import load_dotenv
from openai import AuthenticationError, RateLimitError, APIConnectionError
from src.utils import read_transcript, save_summary
from src.summarizer import summarize

load_dotenv()

TRANSCRIPT_PATH = "transcripts/transcription.txt"


def main() -> None:
    try:
        transcript = read_transcript(TRANSCRIPT_PATH)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        summary = summarize(transcript)
    except AuthenticationError:
        print("Error: Invalid OpenAI API key. Check your .env file.")
        sys.exit(1)
    except RateLimitError:
        print("Error: OpenAI rate limit reached. Please wait and try again.")
        sys.exit(1)
    except APIConnectionError:
        print("Error: Could not connect to OpenAI API. Check your internet connection.")
        sys.exit(1)

    output_path = save_summary(TRANSCRIPT_PATH, summary)

    print(summary)
    print(f"\nSummary saved to: {output_path}")


if __name__ == "__main__":
    main()
