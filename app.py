import streamlit as st
from rag.loader import load_files
from rag.splitter import split_docs
from rag.embeddings import create_vectorstore
from rag.chain import get_qa_chain

st.set_page_config(page_title="AI Document Assistant", layout="wide")
st.title("🤖 AI Document Assistant")

# ---------------- SESSION ----------------
if "chats" not in st.session_state:
    st.session_state.chats = {}

if "active_chat" not in st.session_state:
    st.session_state.active_chat = None

# ---------------- SIDEBAR ----------------
st.sidebar.title("💬 Conversations")

if st.sidebar.button("➕ New Chat"):
    chat_id = f"Chat {len(st.session_state.chats)+1}"
    st.session_state.chats[chat_id] = {"messages": [], "db": None}
    st.session_state.active_chat = chat_id
    st.rerun()

for cid in st.session_state.chats:
    if st.sidebar.button(cid):
        st.session_state.active_chat = cid
        st.rerun()

if st.session_state.active_chat is None:
    st.info("Start a new chat 👈")
    st.stop()

chat = st.session_state.chats[st.session_state.active_chat]

# ---------------- FILE UPLOAD ----------------
st.sidebar.markdown("---")
uploaded_files = st.sidebar.file_uploader(
    "Upload Documents",
    accept_multiple_files=True,
    type=["pdf", "txt", "docx"]
)

if uploaded_files:
    with st.sidebar:
        with st.spinner("Processing documents..."):
            docs = load_files(uploaded_files)
            chunks = split_docs(docs)
            chat["db"] = create_vectorstore(chunks)
        st.success("✅ Ready to chat!")

# ---------------- CHAT DISPLAY ----------------
for msg in chat["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- INPUT ----------------
prompt = st.chat_input("Ask something...")

if prompt:
    chat["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()

        if chat["db"]:
            qa_chain = get_qa_chain(chat["db"])
            result = qa_chain.invoke({"query": prompt})

            answer = result["result"]
            sources = result.get("source_documents", [])

            if not sources:
                answer = "I couldn't find this in the document."

        else:
            answer = "Please upload documents first."

        text = ""
        for word in answer.split():
            text += word + " "
            placeholder.markdown(text + "▌")
        placeholder.markdown(text)

    chat["messages"].append({"role": "assistant", "content": answer})