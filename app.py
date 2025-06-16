import streamlit as st
from document_parser import extract_text_from_pdf, split_text
from vector_store import create_vector_store, load_vector_store
from rag_pipeline import run_rag_pipeline

st.set_page_config(page_title="AI Legal Document Assistant", layout="centered")
st.title("📚 AI Legal Document Assistant")

# Upload legal document
pdf = st.file_uploader("Upload a legal document (PDF)", type=["pdf"])

if pdf is not None:
    st.success("✅ PDF uploaded.")

    # Extract and chunk text
    raw_text = extract_text_from_pdf(pdf)
    chunks = split_text(raw_text)
    st.info(f"📄 Extracted and split document into {len(chunks)} chunks.")

    # Store in Chroma vector DB
    create_vector_store(chunks)
    st.success("📦 Embeddings stored in ChromaDB.")

    # Input for legal question
    query = st.text_input("🔎 Ask a legal question:")

    if query:
        # Run RAG pipeline with Groq + ChromaDB
        answer = run_rag_pipeline(query)
        st.write("🧠 **Answer:**")
        st.success(answer)

else:
    st.info("Please upload a PDF to begin.")
