from app.ingestion.embedder import get_embedding
from app.vectordb.collection_manager import get_collection


class Retriever:
    """
    Retrieves relevant chunks from Milvus.
    """

    def __init__(self):
        self.collection = get_collection()

    def embed_query(self, query: str):
        """
        Convert user query into embedding.
        """
        return get_embedding(query)

    def search(self, query_embedding, k=1):
        """
        Perform similarity search.
        """
        results = self.collection.search(
            data=[query_embedding],
            anns_field="embedding",
            param={
                "metric_type": "COSINE",
                "params": {
                    "ef": 64
                }
            },
            limit=k,
            output_fields=["text"]
        )

        return results

    def retrieve(self, query: str, k=1):
        """
        Return top-k relevant chunks.
        """

        query_embedding = self.embed_query(query)

        results = self.search(
            query_embedding,
            k
        )

        contexts = []   # ✅ Yahin banana hai

        print("=" * 80)
        print("RESULT COUNT:", len(results[0]))
        print("=" * 80)

        for i, hit in enumerate(results[0], start=1):

            text = hit.entity.get("text")

            print(f"\nChunk {i}")
            print("Score :", hit.score)
            print("TEXT :", repr(text))

            if text:
                contexts.append(text)

        print("=" * 80)
        print("RETURNING CONTEXTS")
        print(contexts)
        print("=" * 80)

        return contexts


if __name__ == "__main__":

    retriever = Retriever()

    contexts = retriever.retrieve(
        "What is remote work policy?",
        k=3
    )

    print("\nRetrieved Chunks")
    print("=" * 80)

    for i, context in enumerate(contexts, start=1):
        print(f"\nChunk {i}")
        print("-" * 60)
        print(context)