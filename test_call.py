from app.config import LLM_MODE
from app.llm import ask_llm

if __name__ == "__main__":
    print("LLM_MODE =", LLM_MODE)

    question = "Comment refaire une carte d'identité ?"
    result = ask_llm(question)

    print("QUESTION :", question)
    print("RESULT :", result.model_dump())