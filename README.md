# 🎓 Anna University RAG Chatbot

An AI-powered Streamlit chatbot that uses Retrieval-Augmented Generation (RAG) to answer questions about Anna University based on a structured `.txt` knowledge base. This project utilizes LangChain, HuggingFace Embeddings, ChromaDB for vector search, and OpenRouter API (DeepSeek model) for generating accurate, contextual answers.

---

## 🚀 Live Demo

🔗 [Live Link](#)  

---

## 🧠 Features

- 📖 Load and index a `.txt` knowledge base about Anna University
- 💬 Ask questions in natural language and get relevant, grounded answers
- 🔍 Uses LangChain with ChromaDB for vector retrieval
- 🤖 Powered by DeepSeek LLM via OpenRouter API
- 🧠 HuggingFace Sentence-Transformers for free and fast embedding
- 🌐 Streamlit web interface for interactive chatting

---

## 🖼️ Screenshots

> 

---

## 🧱 Tech Stack

| Layer             | Tool / Library                                       |
|------------------|-------------------------------------------------------|
| LLM               | [DeepSeek via OpenRouter API](https://openrouter.ai) |
| Vector DB         | [ChromaDB](https://www.trychroma.com/)               |
| Embeddings        | HuggingFace (`all-MiniLM-L6-v2`)                     |
| RAG Framework     | [LangChain](https://www.langchain.com/)              |
| UI                | [Streamlit](https://streamlit.io)                    |
| Dev Tools         | Python, dotenv, sentence-transformers                |

---

## 📂 File Structure
annauniv-rag-bot/
│
├── .env                         # Contains the OpenRouter API key
├── requirements.txt             # Lists all Python dependencies
│
├── data/
│   └── anna_university.txt      # Knowledge base in plain text format
│
├── vectorstore/                 # Directory where Chroma stores vector data
│
├── ingest.py                    # Script to load, split, embed, and store the text in ChromaDB
├── rag_chain.py                 # LangChain setup with retriever + LLM (DeepSeek via OpenRouter)
└── app.py                       # Streamlit app for chatbot UI

