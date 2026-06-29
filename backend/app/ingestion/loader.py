from langchain_community.document_loaders import PyPDFLoader

pdf_path = "../../data/milvus.pdf"
loader = PyPDFLoader(pdf_path)
documents = loader.load()

print(f"Total Pages: {len(documents)}")
print("\nFirst Page Content:\n")
print(documents[0].page_content[:500])