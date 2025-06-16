import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from io import BytesIO

def extract_text_from_pdf(pdf_bytes):
    reader = PyPDF2.PdfReader(BytesIO(pdf_bytes))
    return " ".join(page.extract_text() or "" for page in reader.pages)

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(text)
