from langchain_community.document_loaders import PyPDFLoader

# Use raw string (r"...") or double backslashes in Windows paths
file_path = r"E:\langchain_project\Doc Loaders\Elon-Musk-book-_-Jeroen-Van-Raemdonck-_-ChatGPT.docx.pdf"

# Initialize loader
loader = PyPDFLoader(file_path)

# Load the PDF into document chunks
docs = loader.load()

# Print number of chunks (usually one per page)
print(f"Total chunks/pages loaded: {len(docs)}")
