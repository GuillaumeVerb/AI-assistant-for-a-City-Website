from fastapi import FastAPI, HTTPException
from app.llm import ask_llm
from app.schemas import UserQuestion, AssistantResponse
from app.config import LLM_MODE

app = FastAPI(
    title="AI Assistant for a City Website",
    description="A simple AI assistant API for city-related citizen questions.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "City AI Assistant API is running",
        "docs_url": "/docs",
        "version": "0.1.0",
        "mode": LLM_MODE
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/ask", response_model=AssistantResponse)
def ask_city_assistant(payload: UserQuestion):
    try:
        return ask_llm(payload.question)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Internal error: {exc}")