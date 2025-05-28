from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="Answer the following question \n{Question} From the Following text -\n{text}",
    input_variables=['Question', 'text']
)

model = ChatOpenAI()

parser = StrOutputParser()

url = 'https://clickmedialab.com/'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({
    'Question': 'what is media click lab',  # capital Q to match prompt
    'text': docs[0].page_content
})

print(result)
