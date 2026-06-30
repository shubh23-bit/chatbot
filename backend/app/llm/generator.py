from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="phi3:mini"
)


def generate_answer(context: str, question: str):

    prompt = f"""
You are an AI assistant.

Answer ONLY from the provided context.

If the answer is not found in the context,
say:
"I could not find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response