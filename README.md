# AI Assistant for a City Website — V0

## Overview
This project is a simple AI assistant prototype designed to help citizens navigate a city or municipality website more easily. It takes a user question, identifies the likely intent and service category, returns a short structured answer, and suggests the most relevant city service and page. The current version is intentionally simple: it supports a `mock` mode for local development, it can support a `real` mode for LLM-based testing, it exposes the assistant through a FastAPI API, and it returns structured outputs using Pydantic.

## Problem
City and municipal websites often contain useful information, but users may struggle to find the right page or service quickly. Typical questions include:
- How do I renew my ID card?
- How do I register my child for school?
- How do I report a road issue?
- Where can I find city hall opening hours?

This project explores how a simple AI assistant can improve access to public information through structured routing and short answers.

## Current Scope
The current V0 can:
- receive a citizen-style question
- identify an intent
- classify the question into a city-related category
- generate a short answer
- suggest a relevant service
- suggest a related URL
- expose the logic through a FastAPI endpoint

Example output fields:
- `intent`
- `category`
- `answer`
- `suggested_service`
- `suggested_url`
- `confidence`

## Tech Stack
- Python
- FastAPI
- Pydantic
- JSON
- Uvicorn
- mock / real LLM switching

## Project Structure
```text
city-ai-assistant/
├── app/
│   ├── config.py
│   ├── llm.py
│   ├── llm_mock.py
│   ├── llm_real.py
│   ├── main.py
│   ├── schemas.py
│   ├── utils.py
│   └── city_data.json
├── data/
│   └── outputs/
├── tests/
│   └── sample_questions.json
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── run_batch.py
└── test_call.py
```

## How It Works
The assistant currently follows a simple flow:
1. A user sends a question
2. The system routes it to the configured backend (`mock` or `real`)
3. The backend returns a structured response
4. The API exposes the result through `/ask`

This keeps the architecture simple while making the project easy to extend later.

## Running the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure environment
Example `.env` for mock mode:
```bash
LLM_MODE=mock
OPENAI_MODEL=gpt-4o-mini
```

Example `.env` for real mode:
```bash
LLM_MODE=real
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o-mini
```

### 3. Run the API
```bash
uvicorn app.main:app --reload --port 8001
```

### 4. Open Swagger UI
Open in your browser:
```text
http://127.0.0.1:8001/docs
```

## Example Request
```json
{
  "question": "How do I renew my ID card?"
}
```

## Example Response
```json
{
  "intent": "demarche_administrative",
  "category": "etat_civil",
  "answer": "Pour refaire une carte d'identité, consultez le service état civil.",
  "suggested_service": "Carte d'identité",
  "suggested_url": "/etat-civil/carte-identite",
  "confidence": 0.93
}
```

## Available API Endpoints
### `GET /`
Basic root endpoint with API information.

### `GET /health`
Simple health check endpoint.

### `POST /ask`
Main assistant endpoint. Receives a user question and returns a structured response.

## Development Modes
### Mock mode
Used for local development and architecture testing without depending on an external LLM API.

### Real mode
Used to test the same interface with a real language model.

This design makes it easy to switch between local prototyping and real model validation.

## Limitations
This is still a V0 prototype. Current limitations include:
- no real website ingestion yet
- no RAG or retrieval layer
- no source citation
- limited local service dataset
- simplified routing logic
- no frontend yet

## Next Steps
Planned improvements for future versions:
- ingest real city website content
- add retrieval / RAG
- improve service routing
- add source references
- improve fallback handling
- build a simple frontend
- extend the evaluation dataset

## Why This Project Matters
This project is not just a chatbot demo. It is an early prototype of a structured AI assistant designed around:
- a real public-information use case
- clear input/output contracts
- simple but reusable architecture
- progressive evolution from mock logic to real LLM integration

## Author
Built as part of an AI Builder / AI Engineer learning roadmap focused on practical systems, structured outputs, APIs, and real-world use cases.

