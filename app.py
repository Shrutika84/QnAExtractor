import streamlit as st
from pdf_processor import extract_text_from_pdf
from qna_generator import generate_questions, generate_answer

st.title("📄 PDF Question-Answer Generator")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with open("data/uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF Uploaded Successfully!")

    # Extract text
    text = extract_text_from_pdf("data/uploaded.pdf")
    st.text_area("Extracted Text", text[:500], height=150)

    if st.button("Generate Questions"):
        questions = generate_questions(text[:1000])  
        st.write(questions)

        for q in questions.split("\n"):
            answer = generate_answer(q, text[:1000])
            st.write(f"**Q:** {q}")
            st.write(f"**A:** {answer}")
