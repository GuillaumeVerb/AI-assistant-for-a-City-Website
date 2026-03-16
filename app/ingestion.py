import json
from pathlib import Path
from typing import List, Dict


REQUIRED_FIELDS = [
    "id",
    "category",
    "service",
    "title",
    "url",
    "summary",
    "content",
    "keywords",
    "contact",
    "priority",
]


def load_knowledge_base(filepath: str = "app/knowledge_base.json") -> List[Dict]:
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Knowledge base file not found: {filepath}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Knowledge base must be a list of entries.")

    return data


def validate_knowledge_entry(entry: Dict) -> bool:
    if not isinstance(entry, dict):
        return False

    if not all(field in entry for field in REQUIRED_FIELDS):
        return False

    if not isinstance(entry["keywords"], list):
        return False

    if not isinstance(entry["priority"], int):
        return False

    return True


def load_and_validate_knowledge_base(filepath: str = "app/knowledge_base.json") -> List[Dict]:
    data = load_knowledge_base(filepath)

    for entry in data:
        if not validate_knowledge_entry(entry):
            raise ValueError(f"Invalid knowledge base entry: {entry}")

    return data