from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Creates embeddings using BGE model.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-large-en-v1.5"
        )

    def get_embedding(self, text: str):
        return self.model.encode(text).tolist()
 

embedding_model = EmbeddingModel()


def get_embedding(text: str):
    return embedding_model.get_embedding(text)