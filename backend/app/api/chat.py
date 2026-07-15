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
def chat(
    request: ChatRequest
):
    print(request.session_id)
    print(request.question)
    answer = ask_question(
        request.question
    )

    return ChatResponse(
        answer=answer
    )