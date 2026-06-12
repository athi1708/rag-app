# 📄 PDF Question Answering Chatbot using RAG

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions in natural language. The system retrieves relevant information from the document and generates accurate answers using Large Language Models (LLMs).

## 🚀 Features

* 📂 Upload and analyze PDF documents
* 🔍 Semantic search using vector embeddings
* 💬 Ask questions in natural language
* 🧠 Retrieval-Augmented Generation (RAG) pipeline
* ⚡ Fast and accurate document-based responses
* 📑 Supports multi-page PDF documents
* 🌐 Simple and interactive user interface

## 🛠️ Tech Stack

| Component            | Technology                        |
| -------------------- | --------------------------------- |
| Programming Language | Python                            |
| Framework            | Streamlit                         |
| LLM Orchestration    | LangChain                         |
| Vector Database      | FAISS                             |
| Embeddings           | HuggingFace Embeddings            |
| PDF Processing       | PyPDF2 / PDFPlumber               |
| AI Model             | OpenAI / Gemini / HuggingFace LLM |

## ⚙️ How It Works

User Uploads PDF
↓
Text Extraction
↓
Document Chunking
↓
Generate Embeddings
↓
Store in FAISS Vector Database
↓
User Question
↓
Relevant Chunks Retrieved
↓
LLM Generates Context-Aware Answer

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/pdf-rag-chatbot.git
cd pdf-rag-chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
pdf-rag-chatbot/
│
├── app.py
├── requirements.txt
├── data/
├── vectorstore/
└── README.md
```

## 🎯 Use Cases

* Academic Research
* Resume Analysis
* Legal Document Review
* Business Reports
* Research Papers
* Technical Documentation
* Study Materials

## 📈 Future Improvements

* Multiple PDF support
* Chat history memory
* Source citation highlighting
* Voice-based interaction
* Cloud deployment
* Advanced document summarization

## 📚 References

* LangChain Documentation
* FAISS Documentation
* Streamlit Documentation
* Hugging Face Transformers
* Retrieval-Augmented Generation (RAG)

