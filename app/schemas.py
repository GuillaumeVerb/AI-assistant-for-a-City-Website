from pydantic import BaseModel


class UserQuestion(BaseModel):
    question: str


class AssistantResponse(BaseModel):
    intent: str
    category: str
    answer: str
    suggested_service: str
    suggested_url: str
    confidence: float