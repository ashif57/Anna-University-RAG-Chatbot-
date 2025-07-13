
---

```markdown
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

> *(Add screenshots here of Streamlit UI and sample conversations)*

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

```

annauniv-rag-bot/
│
├── .env                         # API key for OpenRouter
├── requirements.txt             # Python dependencies
│
├── data/
│   └── anna\_university.txt      # Knowledge base file
│
├── vectorstore/                 # ChromaDB persistent storage
│
├── ingest.py                    # Split and embed `.txt` into ChromaDB
├── rag\_chain.py                 # LLM + Retriever Chain definition
└── app.py                       # Streamlit UI to chat with the bot

````

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ashif57/annauniv-rag-bot.git
cd annauniv-rag-bot
````

### 2. Create `.env` File

```env
API_KEY=your_openrouter_api_key
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Vector Store

```bash
python ingest.py
```

### 5. Launch Streamlit App

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. `ingest.py` loads the `.txt` file, splits it into chunks, embeds using HuggingFace, and saves to Chroma.
2. `rag_chain.py` loads the vector store and sets up a `RetrievalQA` chain using LangChain.
3. `app.py` runs a Streamlit UI for chatting with the bot.
4. OpenRouter LLM (e.g., DeepSeek) generates responses using the retrieved chunks as context.

---

## 🧪 Example Queries

```text
- Who was Anna University named after?
- What are the main departments in CEG Campus?
- Tell me about Anna University’s research centers.
- What rankings has Anna University received?
- Who are some famous alumni of Anna University?
```

---

## 📌 Limitations

* Requires accurate and well-structured `.txt` data.
* Currently supports only one knowledge base file.
* DeepSeek is used in free-tier mode; performance may vary.

---

## ✅ Future Improvements

* Support for multiple file types (PDF, CSV, etc.)
* Add memory and chat history
* Add source citation display
* Use other OpenRouter models dynamically

---

## 🙏 Acknowledgements

* [LangChain](https://github.com/langchain-ai/langchain)
* [OpenRouter API](https://openrouter.ai/)
* [HuggingFace Transformers](https://huggingface.co/)
* [ChromaDB](https://www.trychroma.com/)
* [Streamlit](https://streamlit.io)

---



## 👨‍💻 Author


GitHub: [@ashif57](https://github.com/ashif57)

```
