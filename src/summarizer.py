from openai import OpenAI
from openai import AuthenticationError, RateLimitError, APIConnectionError

client = OpenAI()

PROMPT_TEMPLATE = """\
Analyze the following video transcript and provide a structured summary with:

1. **Executive Summary**: A concise overview in 3-5 sentences.
2. **Main Topics**: A bullet list of the key subjects covered.
3. **Conclusions & Takeaways**: The most important insights or lessons from the content.

Transcript:
{transcript}
"""


def summarize(transcript: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": PROMPT_TEMPLATE.format(transcript=transcript)
        }]
    )
    return response.choices[0].message.content
