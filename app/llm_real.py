from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is missing. Add it to your .env file or switch LLM_MODE to mock."
    )

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_llm(question: str) -> str:
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    try:
        response = client.responses.create(
            model=OPENAI_MODEL,
            input=question.strip()
        )
        return response.output_text
    except Exception as exc:
        raise RuntimeError(f"LLM call failed: {exc}") from exc