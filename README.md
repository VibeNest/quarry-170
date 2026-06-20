# Quarry

A production-first AI Systems Engineering platform built for scale, evaluation, and operational rigor.

---

## Vision

Quarry is a continuously evolving AI platform designed to demonstrate the complete lifecycle of production machine learning systems. Rather than building scattered, disconnected toy projects, Quarry aggregates progressive complexity into a single, cohesive architecture. This approach mirrors real-world enterprise environments where systems must scale, integrate, and evolve gracefully over time.

---

## Why Quarry Exists

The AI engineering ecosystem is saturated with generic tutorial projects, single-file chat applications, and superficial one-off demonstrations. These projects often ignore the most critical aspects of real-world AI deployment: robustness, maintainability, evaluation, and observability.

Quarry exists to bridge the gap between prototype and production. It focuses strictly on the engineering rigor required to build, deploy, and maintain complex AI systems at scale, prioritizing architecture and operational maturity over quick demos.

---

## Engineering Principles

* **API First**: All core functionalities are exposed as well-defined, versioned, and documented RESTful interfaces.
* **Infrastructure First**: Data stores, compute layers, and deployment environments are treated as first-class citizens, ensuring scalable foundations.
* **Evaluation First**: Systems are built with quantitative and qualitative measurement in mind, preventing regressions and validating improvements.
* **Observability First**: Comprehensive logging, tracing, and monitoring are integrated from the start to ensure system transparency and rapid debugging.
* **Production First**: Code quality, security, and performance are prioritized, treating every iteration as a deployment-ready release candidate.

---

## Current Status

Current Version: Quarry v1

Status: Active Development

Implemented Features:
* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* Password Hashing
* PDF Upload
* PDF Parsing
* Chunking Pipeline
* Embeddings
* Semantic Retrieval

---

## Architecture Overview

```text
Client
│
▼
FastAPI
│
├── Authentication
├── Document Processing
├── Retrieval Layer
│
├── PostgreSQL
├── Redis (planned)
├── pgvector (planned)
│
└── Future AI Layer
```

---

## Tech Stack

| Technology | Purpose |
| :--- | :--- |
| FastAPI | High-performance API framework |
| PostgreSQL | Primary relational database |
| SQLAlchemy | Object Relational Mapper (ORM) |
| JWT | Secure authentication mechanism |

---

## Current Capabilities

* **Authentication**: Secure user registration and login using JSON Web Tokens (JWT) and robust password hashing.
* **Document Processing**: Ingestion pipelines for uploading and parsing PDF documents.
* **Chunking**: Strategy-based text segmentation to prepare document content for optimal vectorization.
* **Embeddings**: Transformation of textual chunks into high-dimensional vector representations.
* **Retrieval**: Semantic search capabilities to retrieve relevant context based on user queries.

---

## Quarry Evolution Roadmap

| Version | Focus | Status |
| :--- | :--- | :--- |
| v1 | Foundation | Completed |
| v2 | Production Backend | Planned |
| v3 | LLM Layer | Planned |
| v4 | Production RAG | Planned |
| v5 | Agent Infrastructure | Planned |
| v6 | Evaluation Platform | Planned |
| v7 | Learning Infrastructure | Planned |
| v8 | Research Infrastructure | Planned |
| v9 | Repository Intelligence | Planned |
| v10 | Advanced Retrieval | Planned |
| v11 | Memory Systems | Planned |
| v12 | Security & Guardrails | Planned |
| v13 | Cloud Operations | Planned |
| v14 | Observability | Planned |
| v15 | Inference Platform | Planned |

---

## Repository Structure

```text
quarry/
├── app/                  # Application code
│   ├── api/              # API endpoints
│   ├── db/               # Database setup and connections
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   ├── utils/            # Utilities and core logic
│   └── main.py           # FastAPI application entry point
├── uploads/              # Uploaded PDF storage
├── create_tables.py      # Database initialization script
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## Local Development

### Prerequisites
* Python 3.10+
* PostgreSQL running locally or via Docker

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/x2ankit/quarry.git
   cd quarry
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables (create a `.env` file):
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/quarry
   SECRET_KEY=your_secret_key_here
   ```

5. Initialize the database:
   ```bash
   python create_tables.py
   ```

### Run the Server

Start the FastAPI application:
```bash
uvicorn app.main:app --reload
```

The Swagger API documentation will be available at: `http://localhost:8000/docs`

---

## Future Directions

Quarry is architected to incrementally integrate advanced AI patterns:
* **RAG**: Implementing advanced Retrieval-Augmented Generation patterns for precise querying.
* **Agents**: Orchestrating autonomous agents to handle complex, multi-step tasks.
* **Memory**: Building stateful systems that retain context across extended user interactions.
* **Evaluation**: Creating robust pipelines to assess and score model performance continuously.
* **Observability**: Integrating full-stack tracing and telemetry for AI specific workloads.
* **Inference**: Optimizing deployment infrastructure for high-throughput, low-latency model inference.

---

## Why This Project Matters

Quarry demonstrates a comprehensive understanding of:
* **Backend Engineering**: Designing scalable and robust APIs.
* **AI Systems Engineering**: Integrating AI components into traditional backend architectures.
* **Retrieval Systems**: Building efficient vector search and chunking mechanisms.
* **Agent Systems**: Designing orchestration layers for autonomous behavior.
* **Evaluation Systems**: Implementing metrics to quantify AI system performance.
* **Deployment Engineering**: Preparing applications for production environments.
* **Inference Engineering**: Optimizing the serving of machine learning models.

---

## Roadmap Alignment

Quarry serves as the foundational artifact developed alongside a multi-phase AI Engineering roadmap, tracking the progression from foundational concepts to advanced inference engineering.

---

## Author

Ankit Arayan Tripathy

AI Engineer → AI Systems Engineer → Inference Engineer → LLM Engineer

GitHub: https://github.com/x2ankit
