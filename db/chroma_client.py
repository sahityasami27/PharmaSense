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


# Dynamically Ingest Papers Based On User Query
def ingest_query_papers(query, max_results=10):

    papers = fetch_pubmed(
        query=query,
        max_results=max_results
    )

    existing = collection.get()

    existing_ids = set(existing["ids"])

    added_count = 0

    for paper in papers:

        # Skip duplicate papers
        if paper["id"] in existing_ids:
            continue

        # Skip empty abstracts
        if not paper["abstract"]:
            continue

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

        added_count += 1

    print(f"Ingested {added_count} new papers.")


# Retrieve Relevant Documents
def retrieve_documents(query, top_k=3):

    # Fetch + Store Latest Relevant Papers
    ingest_query_papers(query)

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


# Direct Testing
if __name__ == "__main__":

    query = "aspirin neuroinflammation"

    results = retrieve_documents(query)

    print(results)