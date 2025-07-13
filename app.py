import streamlit as st
from rag_chain import get_qa_chain

st.set_page_config(page_title="Anna University RAG Bot", page_icon="🎓")

st.title("🎓 Anna University RAG Chatbot")
st.markdown("Ask anything about Anna University.")

qa_chain = get_qa_chain()

# Chat loop
if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.text_input("You:", "")

if user_input:
    result = qa_chain({"query": user_input})
    answer = result["result"]
    st.session_state["history"].append(("You", user_input))
    st.session_state["history"].append(("Bot", answer))

for speaker, msg in reversed(st.session_state["history"]):
    st.markdown(f"**{speaker}:** {msg}")
