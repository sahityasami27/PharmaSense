# PharmaSense

> Agentic AI-powered biomedical research intelligence platform using real-time scientific retrieval, semantic search, and multi-agent orchestration.

---

## Demo

Frontend: <https://pharma-sense-swart.vercel.app/>

Backend API Docs:
http://127.0.0.1:8000/docs

## Overview

PharmaSense is a full-stack Agentic GenAI system designed to automate biomedical literature analysis using:

* Real-time PubMed retrieval
* Retrieval-Augmented Generation (RAG)
* Multi-agent orchestration with LangGraph
* Semantic vector retrieval with ChromaDB
* LLM-powered biomedical reasoning using Groq
* Full-stack deployment with FastAPI + Next.js

The platform dynamically fetches biomedical research papers, retrieves semantically relevant literature, orchestrates multiple AI agents, and synthesizes structured scientific insights.

Unlike traditional single-prompt AI applications, PharmaSense uses coordinated agent workflows and graph-based execution to simulate modular scientific reasoning pipelines.

---

# Core Features

## Multi-Agent Architecture

PharmaSense uses specialized AI agents with distinct responsibilities.

### Literature Agent

* Retrieves biomedical literature
* Extracts scientific findings
* Summarizes relevant evidence

### Mechanism Agent

* Analyzes biological pathways
* Explains molecular mechanisms
* Identifies therapeutic interactions

### Synthesizer Agent

* Combines outputs from multiple agents
* Produces consolidated biomedical reasoning
* Generates final structured responses

The orchestration layer is built using:

* LangGraph
* Stateful workflow execution
* Shared memory propagation
* Graph-based task routing

---

## Real-Time Biomedical Retrieval

Instead of using static datasets, PharmaSense dynamically retrieves live scientific literature from PubMed.

### Pipeline Flow

```text
User Query
    ↓
Live PubMed Retrieval
    ↓
Embedding Generation
    ↓
ChromaDB Vector Storage
    ↓
Semantic Retrieval
    ↓
Parallel Agent Execution
    ↓
Response Synthesis
```

This enables:

* Query-adaptive retrieval
* Real-time scientific analysis
* Continuously updated biomedical context
* Semantic search across scientific literature

---

## Retrieval-Augmented Generation (RAG)

PharmaSense implements a dynamic RAG pipeline using:

* Sentence Transformer embeddings
* ChromaDB vector search
* Context-aware retrieval
* Query-adaptive ingestion
* LLM-powered biomedical reasoning

Embeddings are generated dynamically and stored in persistent vector memory for semantic retrieval.

---

## Parallel Agent Execution

The platform supports concurrent agent workflows to reduce latency and improve throughput.

Using LangGraph:

* Literature analysis
* Mechanism analysis

can execute simultaneously before synthesis.

### Benefits

* Reduced response latency
* Improved orchestration efficiency
* Scalable agent coordination
* Faster biomedical analysis

---

# Tech Stack

| Layer           | Technologies                     |
| --------------- | -------------------------------- |
| Frontend        | Next.js, TypeScript, TailwindCSS |
| Backend         | FastAPI, Python                  |
| Agent Framework | LangGraph                        |
| LLM Framework   | LangChain                        |
| Vector Database | ChromaDB                         |
| Embeddings      | SentenceTransformers             |
| LLM Provider    | Groq (Llama 3.3 70B)             |
| Scientific Data | PubMed                           |
| Observability   | LangSmith                        |

---

# System Architecture

```text
                    ┌────────────────────┐
                    │    User Query      │
                    └─────────┬──────────┘
                              ↓
                 ┌────────────────────────┐
                 │   PubMed Retrieval     │
                 └─────────┬──────────────┘
                           ↓
                ┌─────────────────────────┐
                │  ChromaDB Vector Store  │
                └─────────┬───────────────┘
                          ↓
          ┌──────────────────────────────────┐
          │      LangGraph Orchestration     │
          └───────┬───────────────┬──────────┘
                  ↓               ↓
      ┌────────────────┐  ┌────────────────┐
      │ Literature     │  │ Mechanism      │
      │ Agent          │  │ Agent          │
      └────────┬───────┘  └───────┬────────┘
               ↓                  ↓
          ┌────────────────────────────┐
          │     Synthesizer Agent      │
          └────────────┬───────────────┘
                       ↓
             ┌──────────────────┐
             │ Final Response   │
             └──────────────────┘
```

---

# Performance Metrics

PharmaSense tracks:

* Agent execution latency
* Total orchestration pipeline time
* Retrieval statistics
* Workflow traces using LangSmith

### Example Metrics

```text
Retrieved Papers: 3
Literature Agent Time: 2.70s
Mechanism Agent Time: 4.39s
Total Pipeline Time: 7.27s
```

---

# Example Query

```text
Analyze aspirin for neuroinflammation
```

The system:

* Retrieves live biomedical papers
* Performs semantic retrieval
* Orchestrates specialized AI agents
* Synthesizes molecular insights
* Returns structured biomedical analysis

---

# Project Structure

```text
pharmaSense/
│
├── agents/
├── data/
├── db/
├── frontend/
├── schemas/
├── services/
├── chroma_db/
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <https://github.com/sahityasami27/PharmaSense>
cd pharmaSense
```

---

# Backend Setup

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---
---

# Run Backend

```bash
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

# Future Improvements

* Streaming agent responses
* Redis caching
* PDF biomedical ingestion
* Citation generation
* Autonomous planning agents
* Cloud deployment on Google Cloud Run
* Authentication and rate limiting

---

# Why PharmaSense?

PharmaSense explores how Agentic AI systems can augment biomedical research workflows through:

* Multi-agent coordination
* Semantic scientific retrieval
* Graph-based orchestration
* Real-time AI-assisted reasoning

The project demonstrates production-style Agentic AI engineering beyond simple chatbot architectures.

---

# Author

Built by Sahitya Samineni.
