chat_history = []

def add_user_message(message: str):

    chat_history.append(
        {
            "role": "user",
            "content": message
        }
    )
def add_assistant_message(message: str):

    chat_history.append(
        {
            "role": "assistant",
            "content": message
        }
    )
def format_chat_history():

    history = ""

    for message in chat_history:

        history += (
            f"{message['role'].capitalize()}:\n"
            f"{message['content']}\n\n"
        )

    return history