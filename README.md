# 🤖 AI Document Assistant - DOC_CHATBOT (ChatGPT-style RAG App)

A **production-ready AI document chatbot** built using **Streamlit + LangChain + OpenAI**, designed to answer questions from uploaded documents with **no hallucination**.

---

## 🚀 Features

* 📂 Upload PDF / TXT / DOCX files
* 💬 Chat with your documents
* 🧠 Multi-chat support (ChatGPT-style sidebar)
* 🔍 Context-aware answers using RAG
* ❌ Hallucination-resistant (strict prompting)
* 📄 Source-based answering
* ⚡ Clean modular architecture

---

## 🧠 How It Works

This app uses **Retrieval-Augmented Generation (RAG)**:

1. Documents are split into chunks
2. Converted into embeddings
3. Stored in a vector database (ChromaDB)
4. User query retrieves relevant chunks
5. LLM generates answer ONLY from context

---

## 🏗️ Project Structure

```
doc-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── chain.py
│   └── prompts.py
```

---

## ⚙️ Installation

```bash
git clone <your-repo>
cd doc-chatbot
pip install -r requirements.txt
```

---

## 🔑 Set API Key

```bash
export OPENAI_API_KEY="your_api_key"
```

(Windows PowerShell)

```powershell
setx OPENAI_API_KEY "your_api_key"
```

---

## ▶️ Run App

```bash
streamlit run app.py
```

---

## ⚠️ Important Notes

* The app **does NOT guess answers**

* If information is not in document → it says:

  > "I couldn't find this in the document."

* Uses **Refine Chain** for better full-document understanding

---

## 🧪 Tech Stack

* Streamlit
* LangChain
* OpenAI GPT
* ChromaDB

---

## 💡 Key Highlights

* Designed to reduce hallucination
* Modular & scalable architecture
* Works with ANY document (not just resumes)

---

## 📌 Future Improvements

* PDF highlighting
* Confidence score
* Hybrid search (keyword + semantic)
* UI improvements

---

## 🙌 Author - Sushma Yarru

Built as a hands-on project to understand **real-world RAG systems** and LLM limitations.

---
