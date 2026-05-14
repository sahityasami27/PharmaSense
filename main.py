from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from langgraph.graph import StateGraph, END

from schemas.state import PharmaState

from agents.literature_agent import literature_agent
from agents.mechanism_agent import mechanism_agent

import time


# FastAPI App
app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request Schema
class QueryRequest(BaseModel):
    query: str


# Build Workflow Graph
workflow = StateGraph(PharmaState)

workflow.add_node(
    "literature_agent",
    literature_agent
)

workflow.add_node(
    "mechanism_agent",
    mechanism_agent
)

workflow.set_entry_point(
    "literature_agent"
)

workflow.add_edge(
    "literature_agent",
    "mechanism_agent"
)

workflow.add_edge(
    "mechanism_agent",
    END
)

workflow = workflow.compile()


# API Route
@app.post("/analyze")
def analyze(request: QueryRequest):

    initial_state = {

        "query": request.query,

        "retrieved_docs": [],

        "literature_analysis": {},

        "mechanism_analysis": {},

        "metrics": {},

        "final_response": ""
    }

    start_time = time.time()

    result = workflow.invoke(initial_state)

    total_time = time.time() - start_time

    # Preserve existing metrics
    result["metrics"]["total_pipeline_time"] = total_time

    return result