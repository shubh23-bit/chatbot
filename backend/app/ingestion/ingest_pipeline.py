import logging
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.ingestion.embedder import embedding_model
from app.vectordb.collection_manager import get_collection
from app.ingestion.text_cleaner import (
    clean_for_chunking,
    clean_for_storage,
    is_table_of_contents
)

logger = logging.getLogger(__name__)

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


def _build_page_indexed_text(documents):
    """
    Join all page texts into one string, remembering at which character
    offset each page starts. Chunking the whole document at once (instead
    of page-by-page) lets a chunk span a page break instead of being cut
    off at it.
    """

    full_text = ""
    page_offsets = []  # list of (start_offset, page_number)

    for doc in documents:
        page_offsets.append((len(full_text), doc.metadata.get("page")))
        full_text += doc.page_content + "\n\n"

    return full_text, page_offsets


def _locate_chunks(full_text, chunk_texts):
    """
    Find where each chunk starts inside full_text, so it can be tagged
    with the page it came from. Search position only moves forward to the
    start of the previous match (not past it), since chunk_overlap means
    consecutive chunks can start before the previous one ends.
    """

    offsets = []
    cursor = 0

    for chunk in chunk_texts:
        idx = full_text.find(chunk, cursor)
        if idx == -1:
            idx = full_text.find(chunk)
        if idx == -1:
            idx = cursor

        offsets.append(idx)
        cursor = idx

    return offsets


def _page_for_offset(offset, page_offsets):
    page = page_offsets[0][1]

    for start, page_number in page_offsets:
        if start <= offset:
            page = page_number
        else:
            break

    return page


def ingest_pdf(pdf_path: str):

    source_name = Path(pdf_path).name

    # -------------------------
    # Load PDF
    # -------------------------
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # -------------------------
    # Clean pages + drop Table of Contents pages
    # -------------------------
    filtered_documents = []

    for doc in documents:
        cleaned_text = clean_for_chunking(doc.page_content)

        if is_table_of_contents(cleaned_text):
            logger.info("Skipping TOC page: %s", doc.metadata.get("page"))
            continue

        doc.page_content = cleaned_text
        filtered_documents.append(doc)

    documents = filtered_documents

    # -------------------------
    # Chunk across the whole document (not per-page) so a chunk can span
    # a page break, then map each chunk back to its source page.
    # -------------------------
    full_text, page_offsets = _build_page_indexed_text(documents)

    chunk_texts = splitter.split_text(full_text)
    chunk_offsets = _locate_chunks(full_text, chunk_texts)

    # -------------------------
    # Get Milvus Collection
    # -------------------------
    collection = get_collection()

    # -------------------------
    # Remove Old Data
    # -------------------------
    collection.delete(expr="id >= 0")
    collection.flush()

    # -------------------------
    # Generate Embeddings
    # -------------------------
    texts = []
    pages = []
    sources = []
    embeddings = []

    for chunk_text, offset in zip(chunk_texts, chunk_offsets):
        cleaned_text = clean_for_storage(chunk_text)

        if not cleaned_text:
            continue

        page_number = _page_for_offset(offset, page_offsets)

        texts.append(cleaned_text)
        pages.append(page_number if page_number is not None else -1)
        sources.append(source_name)
        embeddings.append(embedding_model.get_embedding(cleaned_text))

    # -------------------------
    # Insert into Milvus
    # (field order must match the schema, excluding the auto_id "id")
    # -------------------------
    data = [
        texts,
        pages,
        sources,
        embeddings
    ]

    result = collection.insert(data)
    collection.flush()

    return {
        "pages": len(documents),
        "chunks": len(texts),
        "inserted_ids": result.primary_keys[:5]
    }
