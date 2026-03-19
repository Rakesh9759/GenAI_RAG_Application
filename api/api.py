from fastapi import FastAPI
from pydantic import BaseModel

from src.telemetry import init_db
from src.rag_service import ask_rag

# import your existing RAG setup code here
# load embeddings, vectorstore, qa_chain

app = FastAPI()

init_db()


class QueryRequest(BaseModel):
    query: str


@app.post("/ask")
def ask(req: QueryRequest):
    answer = ask_rag(req.query, qa_chain, vectorstore)
    return {"answer": answer}