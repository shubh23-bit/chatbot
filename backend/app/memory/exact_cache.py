from app.memory.redis_client import get_redis_client
import re
def normalize_question(question: str) -> str:
    question = question.strip().lower()

    question = re.sub(r"\s+", " ", question)

    return question
def get_cache_key(question: str) -> str:
    normalized_question = normalize_question(question)

    return f"qa:{normalized_question}"
def get_cached_answer(question: str):

    client = get_redis_client()

    key = get_cache_key(question)

    answer = client.get(key)

    return answer
def save_cached_answer(
    question: str,
    answer: str
):

    client = get_redis_client()

    key = get_cache_key(question)

    client.setex(
    key,
    86400,
    answer
)