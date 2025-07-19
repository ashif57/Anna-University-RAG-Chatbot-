

```markdown
# 🎓 Anna University RAG Chatbot

An AI-powered chatbot that answers factual questions about **Anna University** using Retrieval-Augmented Generation (RAG).  
It processes a `.txt` file knowledge base and responds using OpenRouter LLMs via LangChain.

---

## 🔗 Live Demo

👉 [Click to Try the Bot](https://anna-university-rag-chatbot.onrender.com)  


---

## 🧠 How It Works

- 🔍 Extracts embeddings from a `.txt` file containing university info
- 🧠 Stores vectors in **ChromaDB**
- 💬 Uses **LangChain** with **OpenRouter API** to answer natural language queries
- 🖼️ Displays via **Streamlit UI**

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- OpenRouter API
- Sentence Transformers (MiniLM)
- dotenv

---

## ✅ Features

- ❓ Ask any factual question about Anna University
- 🔎 Text-based RAG retrieval from a `.txt` file
- 🔐 Secure API key via `.env` (excluded from Git)
- 📦 Easily deployable on platforms like Render, Railway, or Replit

## 🧪 Sample Questions

These are some of the questions the chatbot answers correctly:

### ❓ What are the research centers available at Anna University?
![Screenshot 1](https://raw.githubusercontent.com/ashif57/Anna-University-RAG-Chatbot-/main/screenshots/question1.png)

### ❓ What are the admission exams for PG programs?
![Screenshot 2](https://raw.githubusercontent.com/ashif57/Anna-University-RAG-Chatbot-/main/screenshots/question2.png)

### ❓ Is Anna University NAAC accredited?
![Screenshot 3](https://raw.githubusercontent.com/ashif57/Anna-University-RAG-Chatbot-/main/screenshots/question3.png)

### ❓ Who is the founder of Anna University?
![Screenshot 4](https://raw.githubusercontent.com/ashif57/Anna-University-RAG-Chatbot-/main/screenshots/question4.png)

### ❓ When was Anna University established?
![Screenshot 5](https://raw.githubusercontent.com/ashif57/Anna-University-RAG-Chatbot-/main/screenshots/question5.png)


## 📁 Project Structure

```

Anna-University-RAG-Chatbot-/
├── app.py                 # Streamlit app UI
├── ingest.py              # Embedding script
├── rag\_chain.py           # LangChain pipeline logic
├── data/
│   └── anna\_university.txt
├── vectorstore/           # Stores ChromaDB vectors (auto-generated)
├── .env                   # Contains OpenRouter API key (not committed)
├── requirements.txt       # Python dependencies
├── screenshots/           # Demo images for README
└── README.md

````

---

## 🚀 Local Development

```bash
# 1. Clone the repo
git clone https://github.com/ashif57/Anna-University-RAG-Chatbot-.git
cd Anna-University-RAG-Chatbot-

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your OpenRouter API key
echo "API_KEY=your_openrouter_key_here" > .env

# 5. Run embedding script (only once)
python ingest.py

# 6. Launch the Streamlit app
streamlit run app.py
````

---

## 🙌 Acknowledgements

* [OpenRouter API](https://openrouter.ai)
* [LangChain](https://www.langchain.com/)
* [ChromaDB](https://www.trychroma.com/)
* [Streamlit](https://streamlit.io/)

```

---

(`Built with ❤️ by Ashif`) 
```
