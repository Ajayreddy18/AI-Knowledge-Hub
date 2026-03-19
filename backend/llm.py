import ollama
from transformers import pipeline


generator = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

def generate_answer(context, query):

    prompt = f"""
You are an AI assistant.

Your task is to answer the question ONLY using the given context.

DO NOT generate questions.
DO NOT add extra information.
ONLY give a clear, direct answer.

Context:
{context}

Question:
{query}

Final Answer:
"""

    result = generator(prompt, max_new_tokens=150)

    text = result[0]["generated_text"]

    # Extract only final answer
    answer = text.split("Final Answer:")[-1].strip()

    return answer