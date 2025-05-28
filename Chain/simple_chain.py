from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
import os

# Load environment variables
load_dotenv()

# Create prompt template
prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

# Load Groq LLM
model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

# Output parser
parser = StrOutputParser()

# Create the chain
chain = prompt | model | parser

# Invoke the chain
output = chain.invoke({"topic": "artificial intelligence"})

chain.get_graph().print_ascii()

