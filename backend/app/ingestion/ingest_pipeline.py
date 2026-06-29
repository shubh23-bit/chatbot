from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pymilvus import Collection

# from app.ingestion.embedder import get_embedding
from embedder import embedding_model
from pymilvus import (
    connections,
    Collection
)

connections.connect(
    alias="default",
    host="localhost",
    port="19530"
)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
pdf_path = BASE_DIR / "data" / "milvus.pdf"

loader = PyPDFLoader(str(pdf_path))
documents = loader.load()
print(f"Total Pages: {len(documents)}")




splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)
print(f"Total Chunks: {len(chunks)}")




collection = Collection("documents")
collection.load()




texts = []
embeddings = []

for chunk in chunks:

    texts.append(chunk.page_content)
    embedding = embedding_model.get_embedding(
    chunk.page_content
)

    

    embeddings.append(embedding)

print("Embeddings Generated")




data = [
    texts,
    embeddings
]

result = collection.insert(data)

collection.flush()
print("Data Inserted Successfully")
print(result.primary_keys[:5])