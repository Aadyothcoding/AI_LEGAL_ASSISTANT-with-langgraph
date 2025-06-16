from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from rag_pipeline import get_rag_chain

rag_chain = get_rag_chain()

def rag_node(state):
    question = state["question"]
    answer = rag_chain.run(question)
    return {"question": question, "answer": answer}

graph_builder = StateGraph(schema={"question": str, "answer": str})
graph_builder.add_node("rag_step", RunnableLambda(rag_node))
graph_builder.set_entry_point("rag_step")
graph_builder.add_edge("rag_step", END)

legal_graph = graph_builder.compile()
