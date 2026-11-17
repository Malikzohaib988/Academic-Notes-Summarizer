import os
from groq import Groq


def generate_ai_response(prompt: str) -> str:
    """Send a prompt to Groq and return the model's text response."""
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key or api_key == "replace_with_your_own_groq_api_key":
        raise RuntimeError(
            "GROQ_API_KEY is missing. Add your private key to the .env file."
        )

    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile").strip()
    if not model:
        raise RuntimeError("GROQ_MODEL is empty. Set a model in the .env file.")

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a careful, accurate study assistant. "
                    "Be clear, organized, and honest about missing information."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_tokens=1200,
    )

    answer = response.choices[0].message.content
    if not answer:
        return "The AI service returned an empty response."
    return answer.strip()
