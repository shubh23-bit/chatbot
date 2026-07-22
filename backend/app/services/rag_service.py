import logging

from app.retrieval.retriever import Retriever
from app.memory.exact_cache import (
    get_cached_answer,
    save_cached_answer
)

from app.memory.memory_manager import (
    get_history,
    save_message
)

from app.prompt.prompt_builder import (
    build_prompt
)

from app.llm.generator import (
    generate_answer_stream
)


logger = logging.getLogger(__name__)

retriever = Retriever()


def _format_context(contexts):
    """
    Turn retrieved chunks into the text block handed to the LLM, tagging
    each one with its source page so the model can ground its answer
    (and so mismatched/irrelevant chunks are easier to spot in logs).
    """

    blocks = []

    for c in contexts:
        page = c.get("page")
        label = f"[Page {page + 1}]" if isinstance(page, int) and page >= 0 else ""
        blocks.append(f"{label} {c['text']}".strip())

    return "\n\n".join(blocks)


def ask_question_stream(question: str, session_id: str):
    """
    Yield the answer to `question` piece by piece as it's generated, so the
    API layer can stream it straight to the client instead of blocking for
    the full (CPU-bound, potentially slow) generation. Cache + history are
    saved once the full answer has been assembled.
    """

    # ==================================================
    # Step 1 : Check Exact Cache
    # ==================================================

    cached_answer = get_cached_answer(question)

    if cached_answer:

        logger.debug("Cache hit for question=%r", question)

        save_message(session_id, "user", question)
        save_message(session_id, "assistant", cached_answer)

        yield cached_answer
        return

    logger.debug("Cache miss for question=%r", question)

    # ==================================================
    # Step 2 : Load Chat History
    # ==================================================

    history = get_history(session_id)

    # ==================================================
    # Step 3 : Retrieve Relevant Chunks
    # ==================================================

    contexts = retriever.retrieve(question, k=5)

    if not contexts:
        answer = "I couldn't find this information in the uploaded document."

        save_message(session_id, "user", question)
        save_message(session_id, "assistant", answer)

        yield answer
        return

    context = _format_context(contexts)

    logger.debug("Retrieved context (%d chars): %r", len(context), context)

    # ==================================================
    # Step 4 : Build Prompt
    # ==================================================

    prompt = build_prompt(history, context, question)

    # ==================================================
    # Step 5 : Generate + Stream Answer
    # ==================================================

    full_answer = ""

    for piece in generate_answer_stream(prompt):
        full_answer += piece
        yield piece

    # ==================================================
    # Step 6 : Save Answer in Cache + Chat History
    # ==================================================

    save_cached_answer(question, full_answer)

    save_message(session_id, "user", question)
    save_message(session_id, "assistant", full_answer)
