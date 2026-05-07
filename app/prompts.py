def build_prompt(context, question):

    prompt = f"""
You are a document question-answering assistant.

Answer the question ONLY using the provided document context.

Rules:
- Be concise and accurate
- Do not invent information
- If answer is missing, say:
  "I could not find this information in the document."

Document Context:
{context}

Question:
{question}

Answer:
"""

    return prompt