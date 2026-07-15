from pymilvus import connections, Collection

connections.connect(
    alias="default",
    host="localhost",
    port="19530"
)

collection = Collection("documents")
collection.load()

results = collection.query(
    expr="id >= 0",
    output_fields=["text","embedding"],
    limit=5
)

for row in results:
    print(row)
# from pymilvus import connections, utility

# connections.connect(
#     alias="default",
#     host="localhost",
#     port="19530"
# )

# print(utility.list_collections())