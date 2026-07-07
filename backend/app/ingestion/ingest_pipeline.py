from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pymilvus import (
    connections,
    Collection
)

from app.ingestion.embedder import embedding_model


connections.connect(
    alias="default",
    host="localhost",
    port="19530"
)


def ingest_pdf(pdf_path: str):

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(
        documents
    )

    # Load Collection
    collection = Collection(
        "documents"
    )

    collection.load()

    collection.delete(
    expr="id >= 0"
)

    collection.flush()

    texts = []
    embeddings = []

    # Generate Embeddings
    for chunk in chunks:

        texts.append(
            chunk.page_content
        )

        embedding = (
            embedding_model.get_embedding(
                chunk.page_content
            )
        )

        embeddings.append(
            embedding
        )

    # Insert into Milvus
    data = [
        texts,
        embeddings
    ]

    result = collection.insert(
        data
    )

    collection.flush()

    return {
        "pages": len(documents),
        "chunks": len(chunks),
        "inserted_ids":
        result.primary_keys[:5]
    }