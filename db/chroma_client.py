from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

from data.pubmed_data import fetch_pubmed


# Initialize ChromaDB
client = PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="pharma_papers"
)


# Embedding Model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Load Real PubMed Data Into ChromaDB
def load_data():

    papers = fetch_pubmed(
        query="neuroinflammation",
        max_results=20
    )

    for paper in papers:

        embedding = embedding_model.encode(
            paper["abstract"]
        ).tolist()

        collection.add(
            ids=[paper["id"]],
            documents=[paper["abstract"]],
            metadatas=[{
                "title": paper["title"]
            }],
            embeddings=[embedding]
        )

    print("Documents added to ChromaDB")


# Retrieve Relevant Documents
def retrieve_documents(query, top_k=3):

    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    retrieved = []

    for doc, meta in zip(documents, metadatas):

        retrieved.append({
            "title": meta["title"],
            "abstract": doc
        })

    return retrieved


# Run Directly
if __name__ == "__main__":

    load_data()

    query = "neuroinflammation treatment"

    results = retrieve_documents(query)

    print(results)