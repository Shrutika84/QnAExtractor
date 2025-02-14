import os
from pdf_processor import extract_text_from_pdf
from qna_generator import generate_questions, generate_answer


def main(pdf_path):
    if not os.path.exists(pdf_path):
        print("File not found:", pdf_path)
        return

    print("\n📄 Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    print("\n Generating questions...")
    questions = generate_questions(text[:1000])  # Limiting input to avoid long prompts
    print("\nGenerated Questions:\n", questions)

    print("\n Generating answers...")
    for q in questions.split("\n"):
        answer = generate_answer(q, text[:1000])  # Context limited for better accuracy
        print(f"\nQ: {q}\nA: {answer}")


if __name__ == "__main__":
    pdf_path = r"C:\Users\shrut\Documents\LLM\QnAGenerator\QnA System\data\test_qnaforge.pdf" 
    main(pdf_path)
