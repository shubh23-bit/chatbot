from app.memory.redis_client import get_redis_client
import json

MAX_STORE_MESSAGES = 20      # Redis me maximum messages
MAX_CONTEXT_MESSAGES = 4     # LLM ko sirf itne messages


def save_message(session_id: str, role: str, content: str):

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

    # Keep only latest messages
    history = history[-MAX_STORE_MESSAGES:]

    client.set(
        key,
        json.dumps(history)
    )


def get_history(session_id: str):

    client = get_redis_client()

    key = f"chat:{session_id}"

    history = client.get(key)

    if history:
        history = json.loads(history)

        # Only last few messages are sent to LLM
        return history[-MAX_CONTEXT_MESSAGES:]

    return []


def clear_history(session_id: str):

    client = get_redis_client()

    key = f"chat:{session_id}"

    client.delete(key)