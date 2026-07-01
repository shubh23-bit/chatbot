from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router

app = FastAPI(
    title="RAG Chatbot API",
    version="1.0.0"
)

# Enable React Frontend Access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "RAG Chatbot Backend Running"
    }