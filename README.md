# PDF Q&A — Retrieval-Augmented Generation Chatbot

Ask natural-language questions about any PDF and get answers grounded in the document itself — not the model's memory. Upload a file, and the app retrieves the most relevant passages before generating a response, so answers stay traceable back to the source text instead of drifting into hallucination.

**Live demo:** [rag-app-jhp6uegy3xyubvdbf4qpfj.streamlit.app](https://rag-app-jhp6uegy3xyubvdbf4qpfj.streamlit.app/)

---

## Why RAG instead of just prompting an LLM with the PDF text?

Pasting an entire PDF into a prompt breaks down fast — long documents blow past context limits, and even when they fit, models tend to skim rather than reason precisely over every page. This app instead:

1. Splits the document into overlapping chunks small enough to embed accurately
2. Converts each chunk into a vector and indexes it in FAISS for fast similarity search
3. At query time, retrieves only the chunks most relevant to the question
4. Passes just those chunks — not the whole document — to the LLM as context

The result is faster, cheaper, and more accurate than naive "stuff the whole PDF in the prompt" approaches, and it scales to documents far longer than any single context window.

## How it works

```
PDF upload
    │
    ▼
Text extraction (PyPDF2 / pdfplumber)
    │
    ▼
Chunking (overlapping text splits)
    │
    ▼
Embedding (HuggingFace sentence embeddings)
    │
    ▼
FAISS vector store (similarity search index)
    │
    ▼
User question ──▶ Top-k relevant chunks retrieved
    │
    ▼
LLM generates an answer grounded in those chunks
    │
    ▼
Answer displayed in the Streamlit UI
```

## Features

- Upload any PDF and query it in plain English
- Semantic search over document chunks via FAISS — retrieval is based on meaning, not keyword matching
- Multi-page document support
- Swappable LLM backend (OpenAI, Gemini, or a HuggingFace-hosted model)
- Simple, single-page Streamlit interface — no setup required for end users beyond opening the link

## Tech stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| UI | Streamlit |
| Orchestration | LangChain |
| Vector store | FAISS |
| Embeddings | HuggingFace sentence-transformers |
| PDF parsing | PyPDF2 / pdfplumber |
| LLM | OpenAI / Gemini / HuggingFace-hosted model |

## Project structure

```
rag-app/
├── app.py              # Streamlit UI — file upload, chat interface, response rendering
├── rag.py              # Core RAG pipeline: chunking, embedding, FAISS indexing, retrieval, generation
├── requirements.txt     # Python dependencies
└── README.md
```

## Running it locally

**Prerequisites:** Python 3.10+, and an API key for whichever LLM backend you configure in `rag.py`.

```bash
git clone https://github.com/athi1708/rag-app.git
cd rag-app
pip install -r requirements.txt
streamlit run app.py
```

The app opens at `http://localhost:8501`. Upload a PDF from the sidebar, wait for it to be chunked and indexed, then ask questions in the chat box.

## Known limitations

- Answer quality depends on chunk size/overlap — very short or fragmented paragraphs can hurt retrieval precision
- Scanned/image-only PDFs without embedded text will not extract correctly (no OCR step yet)
- No persistent vector store — each session re-embeds the uploaded document from scratch

## Possible next steps

- Add OCR fallback (e.g., Tesseract) for scanned documents
- Cache embeddings per document hash to avoid re-indexing on repeat uploads
- Add source-passage highlighting so answers link back to the exact page/paragraph used

## References

- [LangChain Documentation](https://python.langchain.com/)
- [FAISS Documentation](https://faiss.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* NeurIPS.
