import streamlit as st
from langchain.document_loaders import UnstructuredURLLoader
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

st.title("AGENTIC CHATBOT")

# Initialize session state variables
if 'urls' not in st.session_state:
    st.session_state.urls = []
if 'context' not in st.session_state:
    st.session_state.context = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'chain' not in st.session_state:
    st.session_state.chain = None
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False

# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["Enter Links", "Chatbot", "Check Links"])

if menu == "Enter Links":
    st.header("Enter URLs")
    url = st.text_input("Enter a URL to add:")

    if st.button("Add URL"):
        if url.strip():
            st.session_state.urls.append(url.strip())
            st.success(f"Added URL: {url.strip()}")

    if st.session_state.urls:
        st.markdown("### URLs added so far:")
        for i, u in enumerate(st.session_state.urls, 1):
            st.write(f"{i}. {u}")

    if st.button("Load URLs and Start Chatbot"):
        if st.session_state.urls:
            loader = UnstructuredURLLoader(urls=st.session_state.urls)
            docs = loader.load()
            combined_text = "\n".join([d.page_content for d in docs])
            st.session_state.context = combined_text
            
            prompt = PromptTemplate(
                input_variables=["context", "question"],
                template="Use the following context to answer the question:\n{context}\n\nQuestion: {question}\nAnswer:"
            )
            llm = OpenAI(temperature=0)
            st.session_state.chain = LLMChain(llm=llm, prompt=prompt)
            
            st.session_state.data_loaded = True
            st.success("Data loaded! Switch to 'Chatbot' menu to start chatting.")

elif menu == "Chatbot":
    st.header("Chatbot")

    if not st.session_state.data_loaded:
        st.warning("Please load URLs first under 'Enter Links' menu.")
    else:
        question = st.text_input("Ask a question (type 'exit' to reset):")
        if question:
            if question.lower() == "exit":
                st.session_state.urls = []
                st.session_state.context = ""
                st.session_state.chat_history = []
                st.session_state.chain = None
                st.session_state.data_loaded = False
                st.experimental_rerun()
            else:
                answer = st.session_state.chain.run(
                    context=st.session_state.context,
                    question=question
                )
                st.session_state.chat_history.append(("You", question))
                st.session_state.chat_history.append(("Bot", answer))

        # Display chat history
        for speaker, text in st.session_state.chat_history:
            if speaker == "You":
                st.markdown(f"**You:** {text}")
            else:
                st.markdown(f"**Bot:** {text}")

elif menu == "Check Links":
    st.header("Check Added URLs")
    if st.session_state.urls:
        for i, u in enumerate(st.session_state.urls, 1):
            st.write(f"{i}. {u}")
    else:
        st.info("No URLs added yet.")
