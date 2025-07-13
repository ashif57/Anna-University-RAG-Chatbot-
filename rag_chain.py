import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

load_dotenv()

def get_qa_chain():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory="vectorstore",
        embedding_function=embedding
    )
    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        openai_api_key=os.getenv("API_KEY"),
        model="deepseek/deepseek-r1-0528-qwen3-8b:free",
        temperature=0.3
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    return qa
