from fastapi import FastAPI

app = FastAPI(
    title="RAG Chatbot API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "RAG Chatbot Backend Running"
    }
