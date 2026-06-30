from fastapi import FastAPI
from pydantic import BaseModel
from app.services.rag_service import ask_question

app = FastAPI(
    title="RAG Chatbot API",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "RAG Chatbot Backend Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    answer = ask_question(
        request.question
    )

    return {
        "answer": answer
    }