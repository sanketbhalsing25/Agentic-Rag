from langgraph.graph import StateGraph, END
from app.graph.state import GraphState
from app.graph.nodes import retrieve, generate, grade

def build_workflow(retriever):

    workflow = StateGraph(GraphState)

    workflow.add_node("retrieve", lambda state: retrieve(state, retriever))
    workflow.add_node("generate", generate)

    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "generate")

    workflow.add_conditional_edges(
        "generate",
        grade,
        {
            "good": END,
            "bad": "retrieve"
        }
    )

    return workflow.compile()