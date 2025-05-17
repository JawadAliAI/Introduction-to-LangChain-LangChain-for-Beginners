from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# Load Groq API key
load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

# Prompt templates
template1 = PromptTemplate(
    template='Write a detailed Report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text:\n{text}',
    input_variables=['text']
)

# Output parser
parser = StrOutputParser()

# Combine into a chain
chain = template1 | llm | parser | template2 | llm | parser

# Run the chain
result = chain.invoke({'topic': 'Black Hole'})

# Print final summary
print(result)
