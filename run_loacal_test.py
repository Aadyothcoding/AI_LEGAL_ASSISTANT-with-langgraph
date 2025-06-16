from document_parser import extract_text_from_pdf, split_text
from vector_store import create_vector_store
from rag_pipeline import run_rag_pipeline

def main():
    print("📄 AI Legal Assistant (CLI Version)")
    file_path = input("Enter path to PDF (e.g., sample_documents/contract.pdf): ")

    try:
        with open(file_path, "rb") as f:
            pdf = f.read()

        # Extract and process
        text = extract_text_from_pdf(pdf)
        chunks = split_text(text)
        create_vector_store(chunks)
        print(f"✅ Parsed and stored {len(chunks)} chunks in ChromaDB.")

        # Ask a question
        while True:
            query = input("\nAsk a legal question (or type 'exit' to quit): ")
            if query.lower() == "exit":
                break
            answer = run_rag_pipeline(query)
            print(f"\n🧠 Answer:\n{answer}")

    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
