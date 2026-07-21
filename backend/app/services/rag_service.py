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
    contexts = [
    c.strip()
    for c in contexts
    if c and c.strip()
]

    if not contexts:
        return "I couldn't find this information in the uploaded document."

    context = "\n\n".join(contexts)

    # Step 3
    print("=" * 100)
    print("CONTEXT TYPE :", type(context))
    print("CONTEXT LENGTH :", len(context))
    print("CONTEXT VALUE :")
    print(repr(context))
    print("=" * 100)
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
