from openai import OpenAI

client = OpenAI()


def summarize(transcript: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"Summarize the following video transcript.:\n{transcript}"
        }]
    )
    return response.choices[0].message.content
