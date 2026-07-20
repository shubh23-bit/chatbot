from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="phi3:mini"
)


def generate_answer(prompt: str) -> str:
    """
    Sends the prompt to the LLM
    and returns a plain string.
    """

    response = llm.invoke(prompt)

    if hasattr(response, "content"):
        return response.content

    return str(response)