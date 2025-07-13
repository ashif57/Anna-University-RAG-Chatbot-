from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings

# Load your .txt file
loader = TextLoader("data/anna.txt", encoding="utf-8")
documents = loader.load()

# Split text into chunks
splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
docs = splitter.split_documents(documents)

# Use HuggingFace embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Save to Chroma vectorstore
vectorstore = Chroma.from_documents(
    docs, embedding, persist_directory="vectorstore"
)
vectorstore.persist()

print("✅ Ingested using HuggingFace embeddings and saved to ChromaDB.")
