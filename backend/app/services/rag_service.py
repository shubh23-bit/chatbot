from app.retrieval.retriever import Retriever
from app.llm.generator import generate_answer


retriever = Retriever()


def ask_question(question: str):
    """
    Complete RAG pipeline.
    """

    contexts = retriever.retrieve(
        question,
        k=3
    )

    context = "\n\n".join(
        contexts
    )

    answer = generate_answer(
        context=context,
        question=question
    )

    return answer