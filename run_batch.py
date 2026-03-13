import json
from app.llm import ask_llm
from app.utils import save_json


def load_questions(filepath: str) -> list[str]:
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    questions = load_questions("tests/sample_questions.json")
    results = []

    for question in questions:
        try:
            answer = ask_llm(question)
            results.append(
                {
                    "question": question,
                    "answer": answer,
                    "status": "success"
                }
            )
        except Exception as exc:
            results.append(
                {
                    "question": question,
                    "answer": None,
                    "status": "error",
                    "error": str(exc)
                }
            )

    save_json(results, "data/outputs/batch_results.json")
    print("Batch run complete.")