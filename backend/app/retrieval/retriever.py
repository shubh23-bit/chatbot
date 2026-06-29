from pymilvus import(
    connections,Collection
)
from app.ingestion.embedder import get_embedding

class Retriever:
    def __init__(self):
        #connect milvs

        connections.connect(
            alias="default",
            host="localhost",
            port="19530"
        )
        #load collection
        self.collection=Collection("documents")
        self.collection.load()
        print("Retriever Initialized Successfully")
    
    def embed_query(self,query:str):
        embedding=get_embedding(query)

        
        print("Query :", query)
        print("Type :", type(embedding))
        print("Length :", len(embedding))
        print("First Value Type :", type(embedding[0]))

        return embedding

    def search(self, query_embedding, k=5):

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
if __name__ == "__main__":

    retriever = Retriever()
    query = "What is Remote Work Policy?"
    embedding = retriever.embed_query(query)
    results = retriever.search(
        embedding,
        k=3
    )

    for hit in results[0]:

        print("=" * 50)
        print("Score :", hit.score)
        print("Text :")
        print(hit.entity.get("text"))