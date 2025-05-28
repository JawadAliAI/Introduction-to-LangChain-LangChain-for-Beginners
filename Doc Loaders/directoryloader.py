from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'books',
    glob= '*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.load()
