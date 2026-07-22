from pymilvus import (
    Collection,
    CollectionSchema,
    FieldSchema,
    DataType,
    utility
)

from app.vectordb.milvus_client import connect_to_milvus
COLLECTION_NAME = "documents"
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
            name="page",
            dtype=DataType.INT64
        ),

        FieldSchema(
            name="source",
            dtype=DataType.VARCHAR,
            max_length=500
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
def create_index(collection):

    index_params = {
        "metric_type": "COSINE",
        "index_type": "HNSW",
        "params": {
            "M": 16,
            "efConstruction": 200
        }
    }

    if len(collection.indexes) == 0:

        collection.create_index(
            field_name="embedding",
            index_params=index_params
        )

        print("Index Created Successfully")

    else:

        print("Index Already Exists")
def load_collection(collection):

    collection.load()

    print("Collection Loaded Successfully")
def get_collection():
    connect_to_milvus()

    if utility.has_collection(COLLECTION_NAME):
        collection = Collection(COLLECTION_NAME)

        existing_fields = {field.name for field in collection.schema.fields}
        required_fields = {"page", "source"}

        if not required_fields.issubset(existing_fields):
            # Older collection created before page/source metadata was
            # added. Every ingest already wipes and re-inserts all data
            # (see ingest_pipeline.collection.delete), so dropping here
            # loses nothing that a re-upload wouldn't already replace.
            print("Old collection schema detected, recreating collection")
            utility.drop_collection(COLLECTION_NAME)
            collection = create_collection()
            create_index(collection)
    else:
        collection = create_collection()
        create_index(collection)

    load_collection(collection)
    return collection
