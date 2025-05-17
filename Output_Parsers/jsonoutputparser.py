from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os

# Load environment variables
load_dotenv()

# Define the parser
parser = JsonOutputParser()

# Define the prompt
template = PromptTemplate(
    template='Give me 5 facts about {topic} \n{format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# Define the Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"  # Or "llama3-8b-8192", "mixtral"
)

# Build the chain
chain = template | llm | parser

# Run it
result = chain.invoke({'topic': 'black hole'})
print(result)
