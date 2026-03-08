import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

chroma = chromadb.Client(
    Settings(
        persist_directory="data/vectors"
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