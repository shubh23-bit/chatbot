from redis import Redis

_client = None


def get_redis_client():
    global _client

    if _client is None:

        _client = Redis(
            host="localhost",
            port=6379,
            db=0,
            decode_responses=True
        )

        _client.ping()

        print("✅ Redis Connected Successfully")

    return _client


if __name__ == "__main__":

    client = get_redis_client()