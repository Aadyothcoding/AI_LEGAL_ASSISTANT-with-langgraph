# ⚖️ AI Legal Assistant with LangGraph

An AI-powered Legal Assistant built using **LangGraph, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs)** to help users interact with legal documents, retrieve relevant information, and generate context-aware responses.

## 📌 Project Overview

The AI Legal Assistant is designed to simplify legal document analysis and information retrieval using modern Generative AI technologies. It combines document parsing, vector-based semantic search, and LangGraph-powered agent workflows to provide responses grounded in relevant legal document content.

The system uses a modular architecture that separates document processing, vector storage, retrieval, and agent orchestration.

## ✨ Key Components

- **Document Parser (`document_parser.py`):** Handles document processing and extraction of relevant textual content.
- **RAG Pipeline (`rag_pipeline.py`):** Implements the Retrieval-Augmented Generation workflow to retrieve relevant context before generating responses.
- **LangGraph Agent (`langgraph_agent.py`):** Manages AI agent workflows and coordinates the different stages of processing.
- **Vector Store (`vector_store.py`):** Handles vector embeddings and semantic document retrieval.
- **Application (`app.py`):** Main application entry point.
- **Local Testing (`run_local_test.py`):** Supports local testing of the application components.

## 🏗️ System Architecture

The application follows a modular RAG-based architecture:

1. **Document Input:** Legal documents are provided as input.
2. **Document Processing:** Documents are parsed and converted into machine-readable text.
3. **Embedding Generation:** Text is transformed into vector representations.
4. **Vector Storage:** Embeddings are stored for semantic similarity-based retrieval.
5. **Query Processing:** Users submit questions related to the legal documents.
6. **Context Retrieval:** Relevant document sections are retrieved using semantic search.
7. **Agent Orchestration:** LangGraph coordinates the processing and response-generation workflow.
8. **Response Generation:** The LLM generates context-aware responses using the retrieved information.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Agent Framework | LangGraph |
| AI Architecture | Retrieval-Augmented Generation (RAG) |
| Language Models | LLMs |
| Document Processing | Python-based document parsing |
| Vector Search | Vector Database / Vector Store |
| Dependency Management | pip |

*Specific LLM providers, embedding models, and vector database implementations depend on the project configuration.*

## 📂 Project Structure

```text
AI_LEGAL_ASSISTANT-with-langgraph/
│
├── app.py
├── document_parser.py
├── hello.py
├── langgraph_agent.py
├── rag_pipeline.py
├── requirements.txt
├── run_local_test.py
├── vector_store.py
│
└── .gitignore
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Aadyothcoding/AI_LEGAL_ASSISTANT-with-langgraph.git
cd AI_LEGAL_ASSISTANT-with-langgraph
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Configure the required API keys and model settings according to the integrations used in the project. Keep credentials in environment variables and never commit secret keys to GitHub.

### 5. Run the Application

```bash
python app.py
```

## 🧪 Testing

To execute the local testing script:

```bash
python run_local_test.py
```

## 🎯 Project Objectives

- Automate information extraction from legal documents.
- Enable semantic search across legal document collections.
- Generate context-aware responses using RAG.
- Implement structured AI agent workflows using LangGraph.
- Improve accessibility to legal information through conversational AI.

## 🔮 Future Enhancements

- Support for multiple legal document formats.
- Improved citation and source attribution for generated answers.
- Multi-agent collaboration for specialized legal tasks.
- Enhanced document summarization and clause analysis.
- Integration of additional legal knowledge sources.
- Deployment through a scalable web-based interface.

## ⚠️ Disclaimer

This project is intended for educational and informational purposes. AI-generated responses should not be considered professional legal advice. Users should consult qualified legal professionals for legal decisions.

## 👨‍💻 Author

**Aadyoth Sreeram**

GitHub: [@Aadyothcoding](https://github.com/Aadyothcoding)

---

*Built with Python, LangGraph, and Generative AI.*
