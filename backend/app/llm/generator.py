from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0,
    # Bounds worst-case latency: without a cap, a rambling model can
    # keep generating well past a useful answer length.
    num_predict=400
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
