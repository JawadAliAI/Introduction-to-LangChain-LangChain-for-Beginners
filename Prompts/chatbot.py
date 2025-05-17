from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
chat_history = [
    SystemMessage(content= 'You are helpfull assitent')
]
while True:
    user_input = input('You:')
    chat_history.append(AIMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI:', result.content)