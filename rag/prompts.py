from langchain.prompts import PromptTemplate

def get_prompt():
    template =  """
You are an intelligent assistant.

Use the context to answer the question.

List ALL relevant information from the context.
Do not summarize only one item.

If multiple items exist, list ALL of them clearly.

If the answer requires combining multiple pieces of information
or simple reasoning (like calculating duration), do it.

Do NOT make up answers.
If unsure, say you don't know.

Context:
{context}

Question:
{question}
"""
    return PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )