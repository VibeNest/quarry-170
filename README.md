# Quarry

Quarry is an AI Knowledge Infrastructure Platform providing the foundational data layer for document ingestion, dense vector embedding, and semantic search.

---

## 1. Why Quarry Exists

Building reliable generative AI applications requires robust document ingestion, consistent chunking strategies, and low-latency semantic retrieval. Existing off-the-shelf vector database wrappers often couple infrastructure too tightly with orchestration logic. Quarry decouples these concerns, providing a dedicated, API-first service exclusively for document intelligence and vector retrieval. This architectural separation guarantees that engineering teams retain complete control over their RAG (Retrieval-Augmented Generation) pipelines and multi-tenant data isolation.

## 2. Design Principles

- **API-First**: All system capabilities are exposed via strict, statically-typed REST endpoints.
- **Stateless Orchestration**: The API layer remains stateless; all state is durably persisted, allowing horizontal scalability.
- **Deterministic Processing**: Document chunking and embedding pipelines must yield predictable, testable outputs.
- **Relational Integrity First**: Before introducing specialized vector indexes, relational mapping (User -> Document -> Chunk) is enforced via a standard RDBMS to ensure strict access control and data integrity.

---

## 3. Current State

Quarry v1 is a functional, single-node document retrieval engine. It provides the core end-to-end pipeline required to securely upload a document, extract its text, compute dense vector representations, and query the resulting index.

**Supported Capabilities:**
- **Authentication**: Stateless, JWT-based bearer token authentication.
- **Document Ingestion**: Synchronous PDF parsing and text extraction.
- **Text Processing**: Deterministic sliding-window chunking logic.
- **Vector Generation**: In-memory dense embedding computation using local transformer models.
- **Semantic Search**: Similarity matching against processed chunks for contextual retrieval.

---

## 4. Future Vision

Quarry will evolve from a synchronous, single-node API into a distributed, highly observable infrastructure component capable of supporting asynchronous ingestion pipelines, hybrid search workloads, and autonomous agents at enterprise scale.

### Planned Stack Evolution
- **Caching & Queues**: Introduction of Redis for rate limiting and asynchronous task queues (e.g., Celery) to handle massive document ingestion workloads.
- **Vector Indexing**: Native `pgvector` integration, migrating from basic similarity search to optimized HNSW/IVFFlat indexes.
- **Observability**: Implementation of OpenTelemetry for distributed tracing, Prometheus for metrics, and Grafana for dashboards.
- **Deployment**: Containerization via Docker, orchestration via Kubernetes (Helm), and infrastructure as code via Terraform.

---

## 5. System Architecture Flow

```mermaid
graph TD
    Client[Client Application] -->|Auth Token| API[FastAPI Gateway]
    Client -->|PDF Upload| API
    Client -->|Search Query| API
    
    subgraph Core Services
        API -->|Raw File| PDFParser[PDF Extraction Service]
        PDFParser -->|Extracted Text| Chunker[Chunking Engine]
        Chunker -->|Text Chunks| Embedder[Embedding Pipeline]
        Embedder -->|Dense Vectors| Retrieval[Retrieval Service]
    end
    
    subgraph Persistence Layer
        API --> DB[(PostgreSQL)]
        Embedder --> DB
        Retrieval --> DB
    end
```

---

## 6. Current Technology Stack

**API & Routing**
- **FastAPI**: High-performance ASGI web framework.
- **Pydantic**: Strict data validation and schema serialization.

**Data & Persistence**
- **PostgreSQL**: Primary relational datastore.
- **SQLAlchemy**: Object-Relational Mapper.
- **psycopg2**: PostgreSQL database adapter.

**Security**
- **python-jose**: JWT signing and cryptographic verification.
- **passlib**: Password hashing (bcrypt).

**Document Intelligence**
- **PyMuPDF**: Robust PDF parsing and text extraction.
- **sentence-transformers**: HuggingFace model integration for generating dense vector embeddings.

---

## 7. Architecture Decisions

- **Why FastAPI?** 
  Chosen for its native asynchronous support, auto-generated OpenAPI schemas, and seamless Pydantic integration, which drastically reduces input validation boilerplate and prevents malformed data from reaching the service layer.
- **Why PostgreSQL?** 
  We prioritize strict relational integrity for multi-tenant isolation. Vector support will be layered on top of this stable foundation via `pgvector` rather than adopting a disconnected, specialized vector database, reducing operational complexity.
- **Why JWT?** 
  Stateless, cryptographically verifiable tokens allow the API layer to scale horizontally without requiring a distributed session store for v1.
- **Why Embeddings (Sentence-Transformers)?** 
  Dense vector retrieval significantly outperforms traditional BM25/keyword search for semantic intent matching, which is non-negotiable for RAG pipelines. Local `sentence-transformers` execution enables deterministic testing without immediate dependency on external API providers.

---

## 8. Roadmap by Quarry Versions

### v1.x: Core Foundation (Current)
- JWT Authentication & RBAC groundwork.
- Synchronous Document Upload & PDF Parsing.
- Local Embedding Generation & Basic Retrieval.

### v2.x: Scale & Performance
- Asynchronous task queues for document processing (Redis).
- Native vector search indexing using `pgvector`.
- Streaming responses for chat retrieval endpoints.

### v3.x: Advanced Retrieval
- Hybrid Search (Dense Vectors + Sparse/BM25).
- Neural Reranking integration (e.g., Cohere or Cross-Encoders).
- Provider integrations (OpenAI, Anthropic, Gemini).

### v4.x: Enterprise Operations
- Deep observability (OpenTelemetry distributed tracing).
- Agentic workflow support (tool use and routing integration).
- High availability deployment manifests (Docker, Kubernetes).

---

## 9. Local Development Setup

**1. Environment Setup**
Clone the repository and initialize your virtual environment:
```bash
git clone https://github.com/x2ankit/quarry.git
cd quarry
python -m venv venv
source venv/bin/activate  # Windows: `venv\Scripts\activate`
pip install -r requirements.txt
```

**2. Configuration**
Define your environment variables in a root `.env` file:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/quarry
SECRET_KEY=your_cryptographic_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**3. Database Initialization**
Generate the relational schemas against your local PostgreSQL instance:
```bash
python create_tables.py
```

**4. Server Execution**
Launch the ASGI server:
```bash
uvicorn app.main:app --reload
```
API Documentation and OpenAPI spec available at `http://localhost:8000/docs`.

---
*License: No license specified*
