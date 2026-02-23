from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.main import app_graph

api = FastAPI(title="Compliance Agentic RAG")

class Query(BaseModel):
    question: str

@api.post("/ask")
def ask(query: Query):
    result = app_graph.invoke({
        "question": query.question,
        "documents": [],
        "answer": "",
        "retry_count": 0
    })
    return {"answer": result["answer"]}

api.mount("/static", StaticFiles(directory="ui"), name="static")

@api.get("/")
def serve_ui():
    return FileResponse("ui/index.html")