from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(Model = 'claude-3-5')

result = model.invoke("Who is he?")

print(result)