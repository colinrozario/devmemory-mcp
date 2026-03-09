import chromadb
import os
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VECTOR_DIR = os.path.join(BASE_DIR, "data", "vectors")
os.makedirs(VECTOR_DIR, exist_ok=True)

chroma = chromadb.Client(
    Settings(
        persist_directory=VECTOR_DIR
    )
)

collection = chroma.get_or_create_collection(
    name="project_memory"
)


def embed(text):
    return model.encode(text).tolist()


def add_vector(doc, metadata):

    embedding = embed(doc)

    collection.add(
        documents=[doc],
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[metadata["id"]]
    )

    chroma.persist()


def search_vectors(query, k=5):

    embedding = embed(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )

    return results