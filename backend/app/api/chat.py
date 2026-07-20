from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest,
    ChatResponse
)

from app.services.rag_service import ask_question


router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    print("Session ID:", request.session_id)
    print("Question:", request.question)

    answer = ask_question(
        question=request.question,
        session_id=request.session_id
    )

    return ChatResponse(
        answer=answer
    )