from uuid import uuid4

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from backend.auth import verify_token
from backend.chat_service import ChatService


app = FastAPI(
    title="AI Chatbot API",
    description="Beginner AI Chatbot Microservice",
    version="1.0.0"
)

chat_service = ChatService()

# Simple in-memory conversation storage.
# This is for learning only; it resets when the server restarts.
conversations = {}


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
    conversation_id: str


@app.get("/")
async def home():
    return {"message": "AI Chatbot API is running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    authenticated: bool = Depends(verify_token)
):
    if not request.message.strip():
        raise HTTPException(
            status_code=422,
            detail="Message cannot be empty"
        )

    try:
        conversation_id = (
            request.conversation_id
            or str(uuid4())
        )

        history = conversations.get(
            conversation_id,
            []
        )

        answer = await chat_service.get_response(
            request.message,
            history
        )

        history.append(
            {
                "role": "user",
                "content": request.message
            }
        )

        history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        conversations[conversation_id] = history

        return ChatResponse(
            answer=answer,
            conversation_id=conversation_id
        )

    except Exception as e:
        print("Error:", e)

        raise HTTPException(
            status_code=503,
            detail="AI service is currently unavailable"
        )
