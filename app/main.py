from app.ingestion.loader import load_documents
from app.ingestion.splitter import split_documents
from app.ingestion.vectorstore import create_vectorstore
from app.graph.workflow import build_workflow

def initialize():
    docs = load_documents("data/BFSI_Compliance_Manual.pdf")
    split_docs = split_documents(docs)
    vectorstore = create_vectorstore(split_docs)
    retriever = vectorstore.as_retriever()
    return build_workflow(retriever)

app_graph = initialize()

if __name__ == "__main__":
    question = input("Ask compliance question: ")

    result = app_graph.invoke({
        "question": question,
        "documents": [],
        "answer": "",
        "retry_count": 0
    })

    print("\nFinal Answer:\n")
    print(result["answer"])