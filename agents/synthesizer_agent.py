from services.llm import llm

import time


def synthesizer_agent(state):

    literature = state["literature_analysis"]["summary"]

    mechanism = state["mechanism_analysis"]["summary"]

    query = state["query"]

    prompt = f"""
    You are a senior biomedical synthesis expert.

    User Query:
    {query}

    Literature Findings:
    {literature}

    Mechanism Findings:
    {mechanism}

    Create a final consolidated biomedical research summary.
    """

    start_time = time.time()

    response = llm.invoke(prompt)

    execution_time = time.time() - start_time

    return {

        "final_response": response.content,

        "metrics": {
            **state.get("metrics", {}),
            "synthesizer_agent_time": execution_time
        }
    }