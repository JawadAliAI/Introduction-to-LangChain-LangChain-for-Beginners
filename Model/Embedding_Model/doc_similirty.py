from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Artificial Intelligence enables machines to mimic human intelligence.",
    "Deep learning is a subset of AI that uses neural networks.",
    "AI is widely used in healthcare for diagnostics and drug discovery.",
    "Natural Language Processing helps computers understand human language.",
    "Machine learning allows systems to improve performance from data."
]

query = "How do computers learn from data?"

# Generate embeddings
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Calculate cosine similarity
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Find the most similar document
index, score = sorted(list(enumerate(scores)), key=lambda x: x[-1], reverse=True)[0]

print("Most relevant document:", documents[index])
print("Similarity Score:", score)
