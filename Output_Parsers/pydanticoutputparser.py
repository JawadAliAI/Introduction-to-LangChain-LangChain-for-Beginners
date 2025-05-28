from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


# Load Groq API key
load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

model = llm

class Person(BaseModel):
    name: str = Field(description= 'Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city person belong to')


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age, and city of a fictional {place} person:\n{format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.invoke({'place':'pakistan'})
print(prompt)

result =  model.invoke(prompt)

final_result =  parser.parse(result.content)
print(final_result)