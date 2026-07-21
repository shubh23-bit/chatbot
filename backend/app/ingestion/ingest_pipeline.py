from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.ingestion.embedder import embedding_model
from app.vectordb.collection_manager import get_collection


def ingest_pdf(pdf_path: str):

    # -------------------------
    # Load PDF
    # -------------------------
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # -------------------------
    # Chunk Documents
    # -------------------------
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]
)

    chunks = splitter.split_documents(
        documents
    )

    # -------------------------
    # Get Milvus Collection
    # -------------------------
    collection = get_collection()

    # -------------------------
    # Remove Old Data
    # -------------------------
    collection.delete(
        expr="id >= 0"
    )

    collection.flush()

    texts = []
    embeddings = []

    # -------------------------
    # Generate Embeddings
    # -------------------------
    for chunk in chunks:

        texts.append(chunk.page_content)

        embedding = embedding_model.get_embedding(
            chunk.page_content
        )

        embeddings.append(embedding)

    # -------------------------
    # Insert into Milvus
    # -------------------------
    data = [
        texts,
        embeddings
    ]

    result = collection.insert(data)

    collection.flush()

    return {
        "pages": len(documents),
        "chunks": len(chunks),
        "inserted_ids": result.primary_keys[:5]
    }


