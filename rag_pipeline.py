from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq  # ✅ Correct import
from vector_store import load_vector_store
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="LLaMA3-8b-8192",  # You can also try "LLaMA3-70b-8192" if needed
    temperature=0.2
)

def run_rag_pipeline(query):
    # Load vector store
    db = load_vector_store()

    # Create RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(search_kwargs={"k": 4}),
        return_source_documents=False
    )

    # Run query
    result = qa_chain.run(query)
    return result
