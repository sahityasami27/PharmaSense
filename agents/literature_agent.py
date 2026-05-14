from db.chroma_client import retrieve_documents
from services.llm import llm

import time


def literature_agent(state):

    query = state["query"]

    print("[LiteratureAgent] Retrieving documents...")

    docs = retrieve_documents(query)

    context = "\n\n".join(
        [doc["abstract"] for doc in docs]
    )

    prompt = f"""
    You are a biomedical research analyst.

    Query:
    {query}

    Research Context:
    {context}

    Summarize the key biomedical findings.
    """

    start_time = time.time()

    response = llm.invoke(prompt)

    execution_time = time.time() - start_time

    print("[LiteratureAgent] Analysis complete.")

    return {

        "retrieved_docs": docs,

        "literature_analysis": {
            "summary": response.content
        },

        "metrics": {
            **state.get("metrics", {}),
            "literature_agent_time": execution_time
        }
    }