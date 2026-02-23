from app.config import get_llm
from app.utils.prompts import answer_prompt, grading_prompt

llm = get_llm()

def retrieve(state, retriever):
    docs = retriever.invoke(state["question"])
    return {
        "documents": docs,
        "retry_count": state["retry_count"] + 1
    }

def generate(state):
    context = "\n".join([doc.page_content for doc in state["documents"]])
    prompt = answer_prompt(context, state["question"])
    response = llm.invoke(prompt)
    return {"answer": response.content}

def grade(state):
    result = llm.invoke(grading_prompt(state["answer"])).content

    if "GOOD" in result:
        return "good"

    if state["retry_count"] >= 2:
        return "good"   # stop retry after 2 attempts

    return "bad"