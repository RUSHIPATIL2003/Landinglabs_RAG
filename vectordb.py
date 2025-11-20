import chromadb
from chromadb.config import Settings
from embedding import get_embedding
import time

# Persistent ChromaDB stored on disk
chroma_client = chromadb.PersistentClient(
    path="chroma_storage"
)

collection = chroma_client.get_or_create_collection(name="pdf_chunks")

def add_chunks(chunks):
    existing = collection.count()
    
    for i, chunk in enumerate(chunks, start=existing):
        emb = get_embedding(chunk)
        
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[emb]
        )
        
        time.sleep(0.05)

def retrieve_context(query, top_k=3):
    q_emb = get_embedding(query)
    results = collection.query(
        query_embeddings=[q_emb],
        n_results=top_k
    )
    return results["documents"][0]
