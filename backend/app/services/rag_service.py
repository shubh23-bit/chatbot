from app.retrieval.retriever import Retriever
from app.llm.generator import generate_answer


retriever = Retriever()


def ask_question(question: str):
    """
    Execute the complete RAG pipeline.

    Steps:
    1. Retrieve relevant chunks from Milvus.
    2. Combine retrieved chunks into context.
    3. Send context + question to the LLM.
    4. Return the generated answer.
    """

    # Retrieve top matching chunks
    contexts = retriever.retrieve(
        question,
        k=3
    )

    # Build context for the LLM
    context = "\n\n".join(contexts)

    # Generate answer
    answer = generate_answer(
        context=context,
        question=question
    )

    return answer