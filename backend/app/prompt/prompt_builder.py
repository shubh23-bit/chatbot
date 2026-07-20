def build_prompt(
    history,
    context,
    question
):
    """
    Builds the final prompt for the LLM.
    """

    history_text = ""

    for message in history:

        role = message["role"].capitalize()

        content = message["content"]

        history_text += f"{role}: {content}\n"

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the retrieved context.

If the answer is not present in the context,
say "I don't know."

=========================
Conversation History
=========================

{history_text}

=========================
Retrieved Context
=========================

{context}

=========================
Current Question
=========================

{question}

=========================
Answer
=========================
"""

    return prompt