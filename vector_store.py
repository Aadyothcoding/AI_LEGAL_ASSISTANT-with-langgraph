import os
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

EMBED_MODEL = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_vector_store(chunks, persist_directory="chroma_db"):
    db = Chroma.from_texts(chunks, EMBED_MODEL, persist_directory=persist_directory)
    db.persist()
    return db

def load_vector_store(persist_directory="chroma_db"):
    return Chroma(persist_directory=persist_directory, embedding_function=EMBED_MODEL)
