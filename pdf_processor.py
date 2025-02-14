
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

if __name__ == "__main__":
    pdf_path = "data/Lecture_notes_module_3.pdf"  # Replace with your PDF file path
    text = extract_text_from_pdf(pdf_path)
    print(text[:500])  # Display first 500 characters
