from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def create_vectorstore(docs):
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(docs, embeddings)
    return db