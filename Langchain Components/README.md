# 🌟 LangChain Components

LangChain is a powerful framework for building AI applications by combining **LLMs (Large Language Models)** with various tools and logic. This guide explains the core components of LangChain and how you can use them.

---

## 🚀 1. Models
Models are the foundation of LangChain — the AI models used to process text and generate responses.

- **LLMs**: Large language models like GPT, Groq, Claude, etc.
- **Chat models**: Optimized for multi-turn conversations (like `ChatGroq`).
- **Text embedding models**: Convert text into vector representations for tasks like similarity search.

**Example:**
```python
from langchain_groq.chat_models import ChatGroq

llm = ChatGroq(model="deepseek-r1-distill-qwen-32b", api_key="your_api_key")
response = llm.invoke("What is AI?")
print(response.content)
```

---

## ✍️ 2. Prompts
Prompts are templates that format inputs for LLMs — ensuring clear, consistent instructions.

- **PromptTemplate**: Create structured prompts with variables.
- **Few-shot prompting**: Include examples in the prompt to guide model behavior.

**Example:**
```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms."
)
print(prompt.format(topic="machine learning"))
```

---

## 🔗 3. Chains
Chains combine multiple components — like models and prompts — into a single workflow. They allow you to:

- **Pass outputs from one model into another**
- **Automate multi-step processes**

**Example:**
```python
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
response = chain.run(topic="artificial intelligence")
print(response)
```

---

## 🧠 4. Memory
Memory lets AI remember information between interactions — useful for chatbots!

- **ConversationBufferMemory**: Stores previous messages.
- **ConversationSummaryMemory**: Summarizes past conversations.

**Example:**
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.save_context({"input": "Hi"}, {"output": "Hello!"})
print(memory.load_memory_variables({}))
```

---

## 🤖 5. Agents
Agents use LLMs to make decisions **in real-time** — choosing which tools to use and how to respond.

- **Tools**: Functions the agent can call (e.g., search engines, APIs).
- **Reasoning and actions**: The agent decides the next step dynamically.

**Example:**
```python
from langchain.agents import initialize_agent

agent = initialize_agent([], llm, agent="zero-shot-react-description")
response = agent.run("What is the weather in New York?")
print(response)
```

---

## 🛠️ 6. Tools
Tools are **external functionalities** your AI can use — like APIs, databases, or search engines.

- **Python functions**
- **API calls**
- **Retrieval (RAG) systems**

---

## 📚 7. Retrieval & Vector Stores
For apps like **chatbots with custom knowledge** (RAG):

- **Vector stores**: Store embeddings (like FAISS, Pinecone).
- **Retrievers**: Query stored information to give context to LLMs.

**Example:**
```python
from langchain.vectorstores import FAISS

db = FAISS.load_local("faiss_index")
results = db.similarity_search("AI definition")
print(results)
```

---

## ✅ Why use LangChain?

LangChain simplifies building complex AI apps by providing a modular structure. You can:

- **Chain tasks** (like prompt -> LLM -> API call)
- **Add memory** (like a chatbot remembering past chats)
- **Integrate tools** (like fetching data from the web)
- **Use agents** (for dynamic decision-making)

Would you like to dive deeper into **chains, memory, or agents** — or explore how to connect LangChain with AI bots? Let’s build something great! 🌟

---

## 📄 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact
- **Author**: Jawad Ali Yousafzai
- **Email**: [jawadaliyousafzai.ai@gmail.com]


