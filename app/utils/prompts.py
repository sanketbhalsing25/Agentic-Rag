def answer_prompt(context: str, question: str):
    return f"""
You are a compliance assistant.
Answer ONLY from the provided context.

Context:
{context}

Question:
{question}
"""

def grading_prompt(answer: str):
    return f"""
Check whether the answer is grounded in retrieved context.
If grounded say GOOD.
If hallucinated say BAD.

Answer:
{answer}
"""