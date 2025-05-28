from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
import os

# Load environment variables
load_dotenv()

# Create prompt template
prompt1 = PromptTemplate(
    template='Generate a detiled repont on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 poniter summery from the following text \n {text}',
    input_variables=['text']
)

# Load Groq LLM
model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

parser =  StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'Tell me about Media click lab inc. and about the ceo'})

print(result)




