from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.chat import router as chat_router
from app.api.upload import router as upload_router
from app.db.database import Base, engine
from app.db import models  # noqa: F401  (registers models on Base before create_all)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RAG Chatbot API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://glistening-elf-e3feb5.netlify.app",
    ],
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):\d+",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "message": "RAG Chatbot Backend Running"
    }