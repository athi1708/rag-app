import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

def load_and_index_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

def get_qa_chain(vectorstore):
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        api_key=os.getenv("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"),
        temperature=0.2
    )

    prompt = ChatPromptTemplate.from_template("""
    Answer the question based only on the context below.
    If you don't know the answer, say "I don't know".

    Context: {context}
    Question: {question}
    """)

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

def ask_question(qa_chain, question):
    return qa_chain.invoke(question)