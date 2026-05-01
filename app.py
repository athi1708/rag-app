import streamlit as st
import tempfile
import os
from rag import load_and_index_pdf, get_qa_chain, ask_question

# Page config
st.set_page_config(
    page_title="DocuMind",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 DocuMind ")
st.caption("Upload a PDF and ask questions about it")

# Session state
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "pdf_loaded" not in st.session_state:
    st.session_state.pdf_loaded = False

# Sidebar - PDF Upload
with st.sidebar:
    st.header("📄 Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None and not st.session_state.pdf_loaded:
        with st.spinner("Reading and indexing PDF..."):
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name

            # Load and index
            vectorstore = load_and_index_pdf(tmp_path)
            st.session_state.qa_chain = get_qa_chain(vectorstore)
            st.session_state.pdf_loaded = True
            os.unlink(tmp_path)

        st.success("✅ PDF indexed! Ask your questions.")

    if st.session_state.pdf_loaded:
        if st.button("🔄 Upload New PDF"):
            st.session_state.qa_chain = None
            st.session_state.chat_history = []
            st.session_state.pdf_loaded = False
            st.rerun()

    st.divider()
    st.markdown("**How it works:**")
    st.markdown("1. Upload a PDF\n2. Ask any question\n3. Get AI answers from the document")

# Chat area
if not st.session_state.pdf_loaded:
    st.info("👈 Please upload a PDF from the sidebar to get started.")
else:
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask a question about your document..."):
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = ask_question(st.session_state.qa_chain, prompt)
                st.markdown(answer)
                st.session_state.chat_history.append({"role": "assistant", "content": answer})