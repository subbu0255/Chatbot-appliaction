# Beginner AI Chatbot Microservice

A beginner-friendly chatbot project covering:

- REST APIs
- JSON request/response handling
- Bearer-token authentication
- Environment variables
- Basic error handling
- Async LLM API calls
- Minimal Pydantic validation
- LLM API abstraction
- Structured API responses
- Basic conversation memory
- Streamlit frontend

## Project structure

ai-chatbot/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── chat_service.py
│   ├── llm_client.py
│   ├── config.py
│   └── auth.py
├── frontend/
│   └── app.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

## Run

1. Create and activate a virtual environment.
2. Install dependencies:
   pip install -r requirements.txt
3. Copy `.env.example` to `.env`.
4. Add your Groq API key to `.env`.
5. Start FastAPI from the project root:
   uvicorn backend.main:app --reload
6. In another terminal, start Streamlit:
   streamlit run frontend/app.py
7. Open the Streamlit URL shown in the terminal.

The backend also exposes interactive API documentation at:
http://127.0.0.1:8000/docs
