from langchain_huggingface import HuggingFaceEndpointEmbeddings

embedding = HuggingFaceEndpointEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

text = 'pakistan is an aisha'

vector = embedding.embed_query(text)

print(str(vector))