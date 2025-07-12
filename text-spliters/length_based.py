from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 10,
    chunk_overlap = 2,
    separator=''
)

result = splitter.split_documents(docs)

print(result[0])