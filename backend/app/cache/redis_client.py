import redis

client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

print(
    "Connected:",
    client.ping()
)

client.set(
    "name",
    "Shubham"
)

print(
    client.get("name")
)

client.delete(
    "name"
)

print(
    client.get("name")
)