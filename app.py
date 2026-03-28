import streamlit as st
import os
from rag.loader import load_documents
from rag.chain import get_qa_chain

st.set_page_config(page_title="Doc Chat", layout="wide")
st.title("🤖 ChatGPT-Style Document Assistant")

os.environ["OPENAI_API_KEY"] = st.secrets.get("OPENAI_API_KEY", "")

# ---------------- SESSION ----------------

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "active_chat" not in st.session_state:
    st.session_state.active_chat = None

if "chat_counter" not in st.session_state:
    st.session_state.chat_counter = 1

if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0

# ---------------- SIDEBAR ----------------

st.sidebar.title("📂 Upload Documents")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF / TXT / DOCX",
    accept_multiple_files=True,
    key=f"upload_{st.session_state.uploader_key}"
)

status = st.sidebar.empty()

st.sidebar.markdown("---")
st.sidebar.title("💬 Conversations")

for chat_id, chat in st.session_state.chats.items():
    if st.sidebar.button(chat["title"], key=chat_id):
        st.session_state.active_chat = chat_id
        st.rerun()

st.sidebar.markdown("---")

col1, col2 = st.sidebar.columns(2)

# ➕ NEW CHAT
if col1.button("➕ New Chat"):
    chat_id = f"chat_{st.session_state.chat_counter}"

    st.session_state.chats[chat_id] = {
        "title": f"Chat {st.session_state.chat_counter}",
        "messages": [],
        "db": None
    }

    st.session_state.active_chat = chat_id
    st.session_state.chat_counter += 1
    st.session_state.uploader_key += 1

    st.rerun()

# 🔄 RESET CHAT
if col2.button("🔄 Reset Chat"):
    if st.session_state.active_chat:
        chat = st.session_state.chats[st.session_state.active_chat]
        chat["messages"] = []
        chat["db"] = None
        st.session_state.uploader_key += 1
        st.rerun()

# ---------------- NO CHAT ----------------

if st.session_state.active_chat is None:
    st.info("Click 'New Chat' to start")
    st.stop()

chat = st.session_state.chats[st.session_state.active_chat]

# ---------------- LOAD DOC ----------------

if uploaded_files and chat["db"] is None:
    status.markdown("⏳ Processing documents...")

    with st.spinner("Processing..."):
        chat["db"] = load_documents(uploaded_files)

    st.rerun()

if chat["db"] is not None:
    status.markdown("✅ Documents ready — start chatting!")

# ---------------- DISPLAY CHAT ----------------

for msg in chat["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- INPUT ----------------

prompt = st.chat_input("Ask a question...")

if prompt:

    # prevent duplicate input
    if len(chat["messages"]) == 0 or chat["messages"][-1]["content"] != prompt:

        chat["messages"].append({"role": "user", "content": prompt})

        # auto title
        if len(chat["messages"]) == 1:
            chat["title"] = prompt[:30]

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            if chat["db"]:
                qa_chain = get_qa_chain(chat["db"])
                result = qa_chain({"query": prompt})
                answer = result["result"]
            else:
                answer = "Please upload documents first."

            st.markdown(answer)

        chat["messages"].append({"role": "assistant", "content": answer})





