import json
from pathlib import Path


def load_knowledge_base(filepath: str = "app/knowledge_base.json") -> list:
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Knowledge base file not found: {filepath}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    

def validate_knowledge_entry(entry: dict) -> bool:
    required_fields = [
        "id",
        "category",
        "service",
        "title",
        "url",
        "summary",
        "content",
        "keywords",
        "contact",
        "priority"
    ]

    return all(field in entry for field in required_fields)

def load_and_validate_knowledge_base(filepath: str = "app/knowledge_base.json") -> list:
    data = load_knowledge_base(filepath)

    for entry in data:
        if not validate_knowledge_entry(entry):
            raise ValueError(f"Invalid knowledge base entry: {entry}")

    return data