from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content='You are a helpfull assistent'),
    HumanMessage(content='Tell me About Langchain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)