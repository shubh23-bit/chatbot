from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
# Load variables from .env
load_dotenv()


llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=400,
)


def generate_answer_stream(prompt):
    """
    Yield the answer as it's generated, token-chunk by token-chunk, so the
    caller can forward text to the client immediately instead of waiting
    for the full (potentially slow, CPU-bound) generation to finish.
    """

    for chunk in llm.stream([HumanMessage(content=prompt)]):
        if chunk.content:
            yield chunk.content
