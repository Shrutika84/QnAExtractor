import ollama

def generate_questions(text, model="llama2"):
    """Generate questions from a given text using LLM."""
    prompt = f"Generate 5 questions from the following text:\n\n{text}"
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

def generate_answer(question, context, model="llama2"):
    """Generate an answer for a given question using context."""
    prompt = f"Answer the question based on the given context:\n\nContext: {context}\n\nQuestion: {question}"
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

if __name__ == "__main__":
    sample_text = "Machine learning is a field of artificial intelligence that enables systems to learn from data."
    questions = generate_questions(sample_text)
    print("\nGenerated Questions:\n", questions)

    for q in questions.split("\n"):
        answer = generate_answer(q, sample_text)
        print(f"\nQ: {q}\nA: {answer}")
