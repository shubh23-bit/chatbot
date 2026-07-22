import logging

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.chat import ChatRequest
from app.services.rag_service import ask_question_stream

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    logger.debug("Session ID: %s, Question: %s", request.session_id, request.question)

    return StreamingResponse(
        ask_question_stream(
            question=request.question,
            session_id=request.session_id
        ),
        media_type="text/plain"
    )
