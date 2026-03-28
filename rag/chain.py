from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

def get_qa_chain(db):

    retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 8}   # ⬅️ increase from 3 → 8
)

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",   # IMPORTANT
        return_source_documents=True
    )