from langchain_groq.chat_models import ChatGroq

# Initialize Groq LLM
llm = ChatGroq(model="deepseek-r1-distill-qwen-32b", api_key="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")

# Example query
response = llm.invoke("What is the weather in islambad pakistan?")
print(response.content)
