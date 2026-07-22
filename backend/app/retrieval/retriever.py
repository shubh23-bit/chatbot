import logging

from app.ingestion.embedder import get_query_embedding
from app.vectordb.collection_manager import get_collection

logger = logging.getLogger(__name__)

# Cosine similarity below this is treated as "not actually relevant" so the
# LLM doesn't get handed unrelated chunks as if they were ground truth.
# Tune based on real query logs if answers still look off.
MIN_SIMILARITY_SCORE = 0.35


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
        return get_query_embedding(query)

    def search(self, query_embedding, k=5):
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
            output_fields=["text", "page", "source"]
        )

        return results

    def retrieve(self, query: str, k=5):
        """
        Return up to k relevant chunks as
        [{"text", "page", "source", "score"}, ...], dropping hits below
        MIN_SIMILARITY_SCORE.
        """

        query_embedding = self.embed_query(query)
        results = self.search(query_embedding, k)

        contexts = []

        for hit in results[0]:
            if hit.score < MIN_SIMILARITY_SCORE:
                continue

            text = hit.entity.get("text")

            if not text:
                continue

            contexts.append({
                "text": text,
                "page": hit.entity.get("page"),
                "source": hit.entity.get("source"),
                "score": hit.score
            })

        logger.debug("Retrieved %d chunk(s) above threshold for query=%r", len(contexts), query)

        return contexts
