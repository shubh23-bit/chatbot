from sentence_transformers import SentenceTransformer

# BAAI/bge-* models are asymmetric: queries need this instruction prefix to
# land in the same embedding neighborhood as passages, but passages
# themselves must stay unprefixed. Skipping this on the query side is a
# known cause of poor retrieval accuracy with BGE models.
QUERY_INSTRUCTION = "Represent this sentence for searching relevant passages: "


class EmbeddingModel:
    """
    Creates embeddings using BGE model.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-large-en-v1.5"
        )

    def get_embedding(self, text: str):
        """
        Embed a document chunk (no instruction prefix).
        """
        return self.model.encode(text).tolist()

    def get_query_embedding(self, text: str):
        """
        Embed a user query (with the BGE retrieval instruction prefix).
        """
        return self.model.encode(QUERY_INSTRUCTION + text).tolist()


embedding_model = EmbeddingModel()


def get_embedding(text: str):
    return embedding_model.get_embedding(text)


def get_query_embedding(text: str):
    return embedding_model.get_query_embedding(text)