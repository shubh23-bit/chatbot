from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(
    model="phi3:mini",
    temperature=0
)

def generate_answer(prompt):

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return response.content