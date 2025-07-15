
---

```markdown
# 🎓 Anna University RAG Chatbot

An AI-powered Streamlit chatbot that uses **Retrieval-Augmented Generation (RAG)** to answer questions about Anna University using a structured `.txt` knowledge base. Built with **LangChain**, **HuggingFace Embeddings**, **ChromaDB** for vector retrieval, and the **OpenRouter API (DeepSeek model)** for contextual, high-quality responses.

---

## 🚀 Live Demo

🔗 [Live Chatbot ](https://anna-university-rag-chatbot.onrender.com)  


---

## 🧠 Features

- 📖 Load and index `.txt` knowledge base about Anna University
- 💬 Ask natural language questions and receive relevant answers
- 🔍 Fast vector search with ChromaDB and HuggingFace Embeddings
- 🤖 Powered by DeepSeek LLM via OpenRouter API
- 🔗 LangChain for structured RAG pipelines
- 🌐 Streamlit UI for easy and interactive access

---

## 🖼️ Screenshots

> *(Add screenshots of Streamlit UI and sample Q&A responses here)*

---

## 🧱 Tech Stack

| Layer         | Tool / Library                                         |
|---------------|--------------------------------------------------------|
| LLM           | [DeepSeek via OpenRouter API](https://openrouter.ai)  |
| Vector Store  | [ChromaDB](https://www.trychroma.com/)                |
| Embeddings    | HuggingFace (`all-MiniLM-L6-v2`)                      |
| RAG Framework | [LangChain](https://www.langchain.com/)               |
| UI            | [Streamlit](https://streamlit.io)                     |
| Dev Tools     | Python, dotenv, sentence-transformers                 |

---

## 📂 File Structure

```
annauniv-rag-bot/
│
├── .env                         # API key for OpenRouter
├── requirements.txt             # Python dependencies
│
├── data/
│   └── anna_university.txt      # Knowledge base file
│
├── vectorstore/                 # ChromaDB persistent storage
│
├── ingest.py                    # Load and embed `.txt` data
├── rag_chain.py                 # RAG pipeline setup using LangChain
└── app.py                       # Streamlit app entry point
```

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ashif57/annauniv-rag-bot.git
cd annauniv-rag-bot
```

### 2. Set Up Environment Variables

Create a `.env` file and add your OpenRouter API key:

```env
API_KEY=your_openrouter_api_key
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the Vector Store

```bash
python ingest.py
```

### 5. Launch the Streamlit App

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. `ingest.py` splits the `.txt` knowledge base into chunks and generates embeddings using HuggingFace.
2. Embeddings are stored in a local ChromaDB vector store.
3. `rag_chain.py` sets up a `RetrievalQA` chain using LangChain and DeepSeek LLM via OpenRouter.
4. `app.py` hosts a Streamlit interface for querying the bot in real time.

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

- ⚠️ Requires clean, well-structured `.txt` files for accuracy
- 📄 Currently supports only one knowledge base file at a time
- 🌐 Dependent on free-tier OpenRouter models (performance may vary)

---

## ✅ Future Improvements

- 🗂️ Multi-file support (PDFs, CSVs, etc.)
- 🧠 Add conversational memory and chat history
- 📚 Show source context or references
- 🔄 Option to choose among multiple LLM models

---

## 🙏 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenRouter API](https://openrouter.ai/)
- [HuggingFace Transformers](https://huggingface.co/)
- [ChromaDB](https://www.trychroma.com/)
- [Streamlit](https://streamlit.io)

---


---

## 👨‍💻 Author

**Your Name** – [AshifNavheed.ai](https://your-portfolio.com)  
GitHub: [@ashif57](https://github.com/ashif57)

```

