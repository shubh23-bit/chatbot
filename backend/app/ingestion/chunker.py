from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

BASE_DIR = Path(__file__).resolve().parent.parent.parent
pdf_path = BASE_DIR / "data" / "hrPolicy.pdf"

loader = PyPDFLoader(str(pdf_path))
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")
print("\nFirst Chunk:\n")
print(chunks[0].page_content)