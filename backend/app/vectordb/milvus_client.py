# from pymilvus import (
#     connections,
#     utility,
#     FieldSchema,
#     CollectionSchema,
#     DataType,
#     Collection
# )
# connections.connect(
#     alias="default",
#     host="localhost",
#     port="19530"
# )

# COLLECTION_NAME = "documents"



# if utility.has_collection(COLLECTION_NAME):

#     print("Collection already exists")
#     collection = Collection(COLLECTION_NAME)

# else:

#     fields = [

#         FieldSchema(
#             name="id",
#             dtype=DataType.INT64,
#             is_primary=True,
#             auto_id=True
#         ),

#         FieldSchema(
#             name="text",
#             dtype=DataType.VARCHAR,
#             max_length=5000
#         ),

#         FieldSchema(
#             name="embedding",
#             dtype=DataType.FLOAT_VECTOR,
#             dim=1024  
#         )
       


#     ]

#     schema = CollectionSchema(
#         fields=fields,
#         description="RAG Documents Collection"
#     )

#     collection = Collection(
#         name=COLLECTION_NAME,
#         schema=schema
#     )

#     print("Collection Created Successfully")


# index_params = {
#     "metric_type": "COSINE",
#     "index_type": "HNSW",
#     "params": {
#         "M": 16,
#         "efConstruction": 200
#     }
# }

# # Create index only if not exists

# if len(collection.indexes) == 0:

#     collection.create_index(
#         field_name="embedding",
#         index_params=index_params
#     )

#     print("Index Created Successfully")

# else:

#     print("Index Already Exists")



# collection.load()

# print("Collection Loaded Successfully")
from pymilvus import connections


def connect_to_milvus():

    connections.connect(
        alias="default",
        host="localhost",
        port="19530"
    )

    print("Milvus Connected Successfully")