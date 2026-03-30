from langchain_openai import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA
from rag.prompts import get_prompts

def get_qa_chain(db):

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    retriever = db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 8,
            "score_threshold": 0.3
        }
    )

    map_prompt, refine_prompt = get_prompts()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type="refine",
        chain_type_kwargs={
            "question_prompt": map_prompt,
            "refine_prompt": refine_prompt,
        },
    )

    return qa_chain