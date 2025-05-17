from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from langchain.output_parsers import StructuredOutputParser, ResponseSchema 

# Load Groq API key
load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

model = llm

schema = [
    ResponseSchema(name='fact_1', description='fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='give 3 fact about {topic}\n{format_instruction}',
    input_variables= ['topic'],
    partial_variables={'fromat_instruction': parser.get_formate_instruction()}
)

# use of chain

chain = template | model | parser

result = chain.invoke({'topic':'Black Hole'})


print(result)

print('-------------------------------------')
print('-------------------------------------')
print('-------------------------------------')
print('-------------------------------------')

print('-------------------------------------')
# normal use 
prompt = template.invoke({'topic':'Black Hole'})

result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)