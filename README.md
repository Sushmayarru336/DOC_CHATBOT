# 🤖 DOC_CHATBOT

A ChatBot-style document chatbot built with **Streamlit + LangChain + OpenAI**.

---

## 🚀 Features

* Upload PDF / DOCX / TXT
* Chat with documents
* Multi-chat UI (like ChatGPT)
* Hallucination-resistant answers
* Modular architecture

---

## 🧠 Tech Stack

* Streamlit
* LangChain (latest modular version)
* OpenAI
* ChromaDB

---

## 📦 Setup

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key

```bash
export OPENAI_API_KEY=your_key
```

---

## ▶️ Run

```bash
streamlit run app.py
```

---

## 📌 Highlights

* Uses **Refine Chain** (better than basic RAG)
* Answers only from document
* Works with any document type

---

## 💡 Learnings

* RAG needs proper retrieval tuning
* LLMs hallucinate without grounding
* Modular design improves scalability

---
