from langchain_core.prompts import PromptTemplate

def get_prompts():

    # LangChain's refine chain requires `context_str` (not `context`) for the initial prompt
    map_prompt = PromptTemplate(
        template="""
        Use the following context to answer the question.

        Context:
        {context_str}

        Question:
        {question}

        Answer:
        """,
        input_variables=["context_str", "question"],
    )

    # LangChain's refine chain requires `context_str` (not `context`) and `existing_answer`
    refine_prompt = PromptTemplate(
        template="""
        You are a document assistant.

        Improve the existing answer using the new context below.

        Rules:
        - Combine all useful information
        - Give complete answer
        - Do NOT guess
        - If not found, keep previous answer

        Existing Answer:
        {existing_answer}

        New Context:
        {context_str}

        Question:
        {question}

        Updated Answer:
        """,
        input_variables=["existing_answer", "context_str", "question"],
    )

    return map_prompt, refine_prompt