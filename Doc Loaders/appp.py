import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from chatbot_db import init_db, add_user, save_message, get_chat_history
import os

# Initialize DB and Streamlit page
init_db()
st.set_page_config(page_title="Multi-User Agentic Chatbot with Memory & NLP")
st.title("🧠 Multi-User Agentic Chatbot")

# User login
username = st.text_input("Enter your username:")
if username:
    add_user(username)
    st.success(f"Welcome, {username}!")

# Initialize session state variables
if 'urls' not in st.session_state:
    st.session_state.urls = []
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None
if 'qa_chain' not in st.session_state:
    st.session_state.qa_chain = None
if 'memory' not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Sidebar menu
menu = st.sidebar.radio("Menu", ["Add URLs", "Chatbot", "Chat History", "Summarize"])

# Function to rephrase LLM answers for naturalness
def rephrase_answer(answer: str) -> str:
    prompt = PromptTemplate(
        input_variables=["answer"],
        template=(
            "Rewrite the following answer to be more natural and conversational. "
            "Remove phrases like 'in the context' or similar.\n\n"
            "Answer: {answer}\n\nRewritten Answer:"
        )
    )
    llm = ChatOpenAI(temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(answer=answer)

# Handle "Add URLs" menu
if menu == "Add URLs":
    st.header("Add URLs to Load Content")
    url = st.text_input("Enter a URL:")
    if st.button("Add URL") and url.strip():
        st.session_state.urls.append(url.strip())
        st.success(f"Added: {url.strip()}")

    if st.button("Load URLs"):
        loader = UnstructuredURLLoader(urls=st.session_state.urls)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)

        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(chunks, embeddings)
        vectorstore.save_local("faiss_index")
        st.session_state.vectorstore = vectorstore

        retriever = vectorstore.as_retriever()
        llm = ChatOpenAI(temperature=0)
        st.session_state.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            memory=st.session_state.memory,
            return_source_documents=False
        )
        st.success("Content loaded! Switch to Chatbot tab.")

# Handle "Chatbot" menu
elif menu == "Chatbot":
    st.header("🤖 Chat with Your Content")

    # Load existing FAISS index if chain not initialized
    if not st.session_state.qa_chain:
        if os.path.exists("faiss_index"):
            st.session_state.vectorstore = FAISS.load_local("faiss_index", OpenAIEmbeddings())
            retriever = st.session_state.vectorstore.as_retriever()
            llm = ChatOpenAI(temperature=0)
            st.session_state.qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                retriever=retriever,
                memory=st.session_state.memory,
                return_source_documents=False
            )

    if st.session_state.qa_chain:
        # Display previous chat history
        for role, msg in get_chat_history(username):
            st.chat_message(role).markdown(msg)

        user_input = st.chat_input("Ask something...")
        if user_input:
            st.chat_message("user").markdown(user_input)
            save_message(username, "user", user_input)

            # Get answer from retrieval QA chain
            raw_answer = st.session_state.qa_chain.run(user_input)

            # Rephrase answer for naturalness
            answer = rephrase_answer(raw_answer)

            st.chat_message("assistant").markdown(answer)
            save_message(username, "assistant", answer)

# Handle "Chat History" menu
elif menu == "Chat History":
    st.header("📜 Your Past Chat History")
    history = get_chat_history(username)
    if history:
        for role, msg in history:
            st.markdown(f"**{role.capitalize()}:** {msg}")
    else:
        st.info("No chat history yet.")

# Handle "Summarize" menu
elif menu == "Summarize":
    st.header("📝 Summarize Documents or Chat History")

    llm = ChatOpenAI(temperature=0.3)
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following text briefly and clearly:\n\n{text}"
    )
    summarization_chain = LLMChain(llm=llm, prompt=prompt)

    if st.button("Summarize Loaded Documents"):
        if st.session_state.vectorstore:
            docs = st.session_state.vectorstore.docstore._dict.values()
            combined_text = "\n".join([doc.page_content for doc in docs])
            summary = summarization_chain.run(text=combined_text)
            st.write("### Summary of loaded documents:")
            st.write(summary)
        else:
            st.warning("No documents loaded.")

    if st.button("Summarize Chat History"):
        history = get_chat_history(username)
        if history:
            combined_chat = "\n".join([f"{role}: {msg}" for role, msg in history])
            summary = summarization_chain.run(text=combined_chat)
            st.write("### Summary of your chat history:")
            st.write(summary)
        else:
            st.warning("No chat history found.")
