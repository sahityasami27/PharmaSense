from services.llm import llm

import time


def mechanism_agent(state):

    query = state["query"]

    docs = state["retrieved_docs"]

    context = "\n\n".join(
        [doc["abstract"] for doc in docs]
    )

    prompt = f"""
    You are a pharmacology mechanism expert.

    Query:
    {query}

    Research Context:
    {context}

    Explain the biological and pharmacological mechanisms involved.
    """

    start_time = time.time()

    response = llm.invoke(prompt)

    execution_time = time.time() - start_time

    print("[MechanismAgent] Analysis complete.")

    return {

        "mechanism_analysis": {
            "summary": response.content
        },

        "metrics": {
            **state.get("metrics", {}),
            "mechanism_agent_time": execution_time
        }
    }