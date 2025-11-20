from fastapi import FastAPI
from rag_pipeline import ask_rag

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/ask")
def ask(query: str):
    return {"answer": ask_rag(query)}
