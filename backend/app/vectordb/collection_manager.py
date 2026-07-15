from pymilvus import (
    Collection,
    CollectionSchema,
    FieldSchema,
    DataType,
    utility
)

from app.vectordb.milvus_client import connect_to_milvus
def create_collection():

    fields = [

        FieldSchema(
            name="id",
            dtype=DataType.INT64,
            is_primary=True,
            auto_id=True
        ),

        FieldSchema(
            name="text",
            dtype=DataType.VARCHAR,
            max_length=5000
        ),

        FieldSchema(
            name="embedding",
            dtype=DataType.FLOAT_VECTOR,
            dim=1024
        )

    ]

    schema = CollectionSchema(
        fields=fields,
        description="RAG Documents"
    )

    collection = Collection(
        name=COLLECTION_NAME,
        schema=schema
    )

    print("Collection Created")

    return collection