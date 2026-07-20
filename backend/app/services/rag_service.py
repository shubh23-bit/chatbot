from app.retrieval.retriever import Retriever

from app.memory.memory_manager import (
    get_history,
    save_message
)

from app.prompt.prompt_builder import (
    build_prompt
)

from app.llm.generator import (
    generate_answer
)


retriever = Retriever()


def ask_question(
    question: str,
    session_id: str
) -> str:

    # Step 1
    history = get_history(session_id)

    # Step 2
    contexts = retriever.retrieve(
        question,
        k=3
    )

    context = "\n\n".join(contexts)

    # Step 3
    prompt = build_prompt(
        history,
        context,
        question
    )

    # Step 4
    answer = generate_answer(
        prompt
    )

    # Step 5
    save_message(
        session_id,
        "user",
        question
    )

    save_message(
        session_id,
        "assistant",
        answer
    )

    return answer