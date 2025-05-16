from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model= 'text-embedding-3-large', dimensions=32)

print(embedding.embed_query('Islambad is the capital of pakistan'))