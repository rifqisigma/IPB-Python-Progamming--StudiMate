import os
import pdfplumber
from docx import Document


BASE_DIR = "./read-file" 


def read_text_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def read_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text

def read_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def load_file(filename):
    # Gabungkan folder + nama file
    path = os.path.join(BASE_DIR, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"File tidak ditemukan: {path}")

    ext = os.path.splitext(path)[1].lower()

    if ext in [".txt", ".py"]:
        return read_text_file(path)
    elif ext == ".pdf":
        return read_pdf(path)
    elif ext == ".docx":
        return read_docx(path)
    else:
        raise ValueError("Format tidak didukung.")


