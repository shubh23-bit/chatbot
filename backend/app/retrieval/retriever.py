from pymilvus import connections, Collection
from app.ingestion.embedder import get_embedding


class Retriever:
    """
    Retrieves relevant chunks from Milvus.
    """

    def __init__(self):

        connections.connect(
            alias="default",
            host="localhost",
            port="19530"
        )

        self.collection = Collection("documents")
        self.collection.load()

    def embed_query(self, query: str):
        """
        Convert user query into vector.
        """
        return get_embedding(query)

    def search(self, query_embedding, k=5):
        """
        Perform similarity search.
        """

        results = self.collection.search(
            data=[query_embedding],
            anns_field="embedding",
            param={
                "metric_type": "COSINE"
            },
            limit=k,
            output_fields=["text"]
        )

        return results

    def retrieve(self, query: str, k=5):
        """
        Return top-k relevant chunks.
        """

        query_embedding = self.embed_query(
            query
        )

        results = self.search(
            query_embedding,
            k
        )

        contexts = []

        for hit in results[0]:
            contexts.append(
                hit.entity.get("text")
            )

        return contexts