from app.config import LLM_MODE

if LLM_MODE == "mock":
    from app.llm_mock import ask_llm
elif LLM_MODE == "real":
    from app.llm_real import ask_llm
else:
    raise ValueError(
        f"Invalid LLM_MODE='{LLM_MODE}'. Use 'mock' or 'real'."
    )