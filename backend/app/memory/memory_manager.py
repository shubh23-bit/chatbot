from app.memory.redis_client import get_redis_client
import json


def save_message(
    session_id: str,
    role: str,
    content: str
):

    client = get_redis_client()

    key = f"chat:{session_id}"

    history = client.get(key)

    if history:

        history = json.loads(history)

    else:

        history = []

    history.append(
        {
            "role": role,
            "content": content
        }
    )

    client.set(
        key,
        json.dumps(history)
    )
def get_history(
    session_id: str
):

    client = get_redis_client()

    key = f"chat:{session_id}"

    history = client.get(key)

    if history:

        return json.loads(history)

    return []
def clear_history(
    session_id: str
): 

    client = get_redis_client()

    key = f"chat:{session_id}"

    client.delete(key)

if __name__ == "__main__":

    session = "demo123"

    save_message(
        session,
        "user",
        "Hi"
    )

    save_message(
        session,
        "assistant",
        "Hello!"
    )

    save_message(
        session,
        "user",
        "What is Python?"
    )

    history = get_history(session)

    print(history)