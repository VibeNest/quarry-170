# Quarry

AI Knowledge Infrastructure Platform

## Overview

Quarry is a production-grade AI Knowledge Infrastructure Platform designed to process, store, and semantically retrieve document data. 

It solves the foundational challenge of building scalable Agentic workflows by providing a robust, high-performance pipeline for document ingestion, dense vector embedding, and semantic search. The long-term vision is to evolve Quarry into a comprehensive ecosystem that natively supports hybrid search, reranking, observability, and advanced AI agents.

## Features

* **JWT Authentication**: Secure user authentication and authorization using JSON Web Tokens.
* **PDF Upload**: Scalable ingestion for PDF documents.
* **Document Processing**: Automated text extraction and intelligent chunking of document contents.
* **Embedding Generation**: Dense vector representation of document chunks using transformer models.
* **Retrieval Pipeline**: High-performance semantic search to retrieve the most relevant context.

## Architecture

Quarry is architected around Domain-Driven Design principles using a modern Python backend stack:
* **API Layer**: FastAPI endpoints handling routing, validation, and serialization.
* **Service Utilities**: Modular pipelines for PDF parsing, text chunking, and embedding generation.
* **Data Access**: SQLAlchemy ORM for relational mapping and database session management.
* **Storage**: PostgreSQL database supporting complex relationships between Users, Documents, and embedded Chunks.

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT (python-jose, passlib)
* Pydantic
* Python
* PyMuPDF
* sentence-transformers

## Project Structure

```text
app/
├── api/
│   ├── auth.py
│   ├── chat.py
│   ├── documents.py
│   ├── health.py
│   └── upload.py
├── db/
│   ├── database.py
│   └── dependencies.py
├── models/
│   ├── chunk.py
│   ├── document.py
│   ├── user.py
│   └── __init__.py
├── schemas/
│   ├── chat.py
│   ├── document.py
│   └── user.py
├── utils/
│   ├── chunking.py
│   ├── embedding.py
│   ├── pdf.py
│   ├── retrieval.py
│   └── security.py
├── main.py
└── __init__.py
```

## Local Setup

1. Clone the repository and navigate into the directory:
```bash
git clone https://github.com/x2ankit/quarry.git
cd quarry
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Or `venv\Scripts\activate` on Windows
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the PostgreSQL database schemas:
```bash
python create_tables.py
```

5. Launch the local development server:
```bash
uvicorn app.main:app --reload
```

## Environment Variables

Configure the following environment variables in a `.env` file at the project root:

* `DATABASE_URL`: Connection string for PostgreSQL (e.g., `postgresql://user:password@localhost:5432/quarry`)
* `SECRET_KEY`: Cryptographic key used for signing JSON Web Tokens.
* `ALGORITHM`: Hashing algorithm for JWT (e.g., `HS256`).
* `ACCESS_TOKEN_EXPIRE_MINUTES`: Expiration time for authentication tokens.

## API Overview

* `/api/auth`: User registration, login, and token generation endpoints.
* `/api/upload`: Endpoints for uploading and ingesting PDF documents.
* `/api/documents`: Endpoints for managing and inspecting processed documents.
* `/api/chat`: Endpoints for semantic search and retrieval queries against the document base.
* `/health`: System health and readiness probes.

## Current Roadmap

**Quarry v2 — Knowledge Retrieval Foundation**

Completed:
* Authentication
* Document Upload
* Embeddings
* Retrieval

Upcoming:
* Redis
* pgvector
* Hybrid Search
* Reranking
* Evaluation
* Agents
* Observability
* Deployment

## Development Status

Quarry is currently in active development, progressing towards the v2 release milestone. The core infrastructure for document processing and retrieval is stable, while caching, advanced search capabilities, and production deployment mechanisms are actively being engineered.

## License

No license specified
