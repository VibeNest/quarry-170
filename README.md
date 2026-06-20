<div align="center">

# 🏗️ Quarry

**The Production-First AI Systems Platform**

*An evolving, end-to-end infrastructure for building scalable, production-ready AI and LLM systems.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## 🎯 Vision

The AI ecosystem is saturated with disconnected demos, simple RAG tutorials, and single-file notebook scripts. While these are great for learning, they fail to bridge the gap between a weekend project and a **production-ready AI system**.

**Quarry is different.** 

It is designed as a single, continuously evolving platform. Instead of building isolated applications, Quarry focuses on **systems engineering**—layering robust infrastructure, scalable backends, evaluation frameworks, and observability platforms to build true enterprise-grade AI architecture.

---

## ✨ What Makes Quarry Different

| Feature | ❌ Typical AI Project | ✅ Quarry |
| :--- | :--- | :--- |
| **Architecture** | Single-file script or notebook | Tiered, production backend |
| **Focus** | Making a demo work | Systems engineering & scalability |
| **Data Layer** | Ephemeral, in-memory | Persistent (PostgreSQL + pgvector) |
| **Evolution** | Abandoned after weekend | Continuous V1 → V15 roadmap |
| **Observability** | `print()` statements | Telemetry, logging & metrics |
| **Design** | Toy chatbot | Modular AI infrastructure |

---

## 🏛️ Engineering Principles

> [!IMPORTANT]
> Quarry is built on strict engineering standards designed for production environments.

- 🚀 **API First:** Decoupled architecture driven by clean, versioned REST/gRPC interfaces.
- 🏗️ **Infrastructure First:** Robust foundation with databases, caching, and task queues before adding intelligence.
- 🧪 **Evaluation First:** Rigorous metric-driven testing for LLM responses and retrieval accuracy.
- 📊 **Observability First:** Comprehensive logging, tracing, and telemetry across the entire pipeline.
- ⚡ **Production First:** Designed for deployment, scalability, security, and enterprise integration.

---

## 🗺️ Quarry Evolution

```mermaid
flowchart LR
    A([v1 Foundation]) --> B([v4 Production RAG])
    B --> C([v5 Agents])
    C --> D([v8 Research])
    D --> E([v11 Memory])
    E --> F([v14 Observability])
    F --> G([v15 Inference])
    
    style A fill:#2e7d32,stroke:#1b5e20,color:#fff,stroke-width:2px
    style B fill:#1565c0,stroke:#0d47a1,color:#fff,stroke-width:2px
    style C fill:#1565c0,stroke:#0d47a1,color:#fff,stroke-width:2px
    style D fill:#1565c0,stroke:#0d47a1,color:#fff,stroke-width:2px
    style E fill:#1565c0,stroke:#0d47a1,color:#fff,stroke-width:2px
    style F fill:#1565c0,stroke:#0d47a1,color:#fff,stroke-width:2px
    style G fill:#1565c0,stroke:#0d47a1,color:#fff,stroke-width:2px
```
*(Visualizing the journey from foundation to full inference platform)*

---

## ⚙️ Current Capabilities

<details open>
<summary><b>🔐 Authentication & Security</b></summary>
<br>
Secure user registration and login workflows using JWT authentication.
</details>

<details open>
<summary><b>📄 Document Processing</b></summary>
<br>
Robust pipeline for uploading, parsing, and chunking complex PDF documents.
</details>

<details open>
<summary><b>🧠 Embeddings & Intelligence</b></summary>
<br>
Automated vector embedding generation for semantic document representation.
</details>

<details open>
<summary><b>🔎 Semantic Retrieval</b></summary>
<br>
High-performance semantic search and document retrieval system.
</details>

<details open>
<summary><b>🗄️ Database Layer</b></summary>
<br>
Enterprise-grade PostgreSQL backend managed via SQLAlchemy ORM.
</details>

---

## 🏗️ Architecture

```text
┌─────────────────────────────────────────────────────────────────┐
│                           Client / UI                           │
└───────────────────────────────┬─────────────────────────────────┘
                                │ HTTP / REST
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FastAPI API Gateway                        │
│                                                                 │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐     │
│  │   Auth Layer   │  │ Document Layer │  │Retrieval Layer │     │
│  │  (JWT, RBAC)   │  │(Parse & Chunk) │  │(Embed, Search) │     │
│  └───────┬────────┘  └───────┬────────┘  └───────┬────────┘     │
└──────────┼───────────────────┼───────────────────┼──────────────┘
           │                   │                   │
           ▼                   ▼                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Data & State Layer                         │
│                                                                 │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐     │
│  │   PostgreSQL   │  │ pgvector (Plan)│  │  Redis (Plan)  │     │
│  │ (Users, Meta)  │  │(Vector Storage)│  │ (Cache/Queue)  │     │
│  └────────────────┘  └────────────────┘  └────────────────┘     │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                 AI & Inference Layer (Future)                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🧰 Technology Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Core** | `Python` | Primary programming language |
| **Framework** | `FastAPI` | High-performance async API backend |
| **Database** | `PostgreSQL` | Primary persistent data storage |
| **ORM** | `SQLAlchemy` | Database interaction and migrations |
| **Security** | `JWT` | Stateless authentication tokens |
| **Processing** | `PyMuPDF` | Fast and accurate PDF extraction |
| **Models** | `Sentence Transformers`| State-of-the-art text embeddings |
| **Validation** | `Pydantic` | Strict data validation and settings |

---

## 📈 Current Progress

**🟢 v1 Foundation** — *Complete*  
**🟡 v2 Production Backend** — *In Progress*  
**⚪ v3 LLM Layer** — *Planned*  
**⚪ v4 Production RAG** — *Planned*  

---

## 🚀 Roadmap

| Version | Focus | Status | Description |
| :--- | :--- | :--- | :--- |
| **v1** | Foundation | 🟢 Complete | Core Auth, Postgres, PDF parsing, embeddings, retrieval. |
| **v2** | Production Backend | 🟡 In Progress | Robust API architecture, error handling, clean architecture. |
| **v3** | LLM Layer | ⚪ Planned | Integration with language models for generative responses. |
| **v4** | Production RAG | ⚪ Planned | Advanced RAG techniques, hybrid search, re-ranking. |
| **v5** | Agent Infrastructure | ⚪ Planned | Multi-agent orchestration and tool use. |
| **v6** | Evaluation Platform | ⚪ Planned | Framework for testing RAG and agent performance. |
| **v7** | Learning Infrastructure | ⚪ Planned | RLHF, fine-tuning pipelines, and prompt management. |
| **v8** | Research Infrastructure | ⚪ Planned | Specialized pipelines for academic/research workflows. |
| **v9** | Repository Intelligence | ⚪ Planned | Codebase understanding and semantic code search. |
| **v10** | Advanced Retrieval | ⚪ Planned | Graph RAG, hierarchical retrieval, dynamic chunking. |
| **v11** | Memory Systems | ⚪ Planned | Long-term user memory, session context, knowledge graphs. |
| **v12** | Security & Guardrails | ⚪ Planned | Prompt injection defense, output validation, PII scrubbing. |
| **v13** | Cloud Operations | ⚪ Planned | Kubernetes manifests, CI/CD, Terraform, scalable deployments. |
| **v14** | Observability | ⚪ Planned | OpenTelemetry, Grafana, structured logging, tracing. |
| **v15** | Inference Platform | ⚪ Planned | Custom vLLM deployments, model serving, optimization. |

---

## 📂 Repository Structure

```text
quarry/
├── app/
│   ├── api/          # FastAPI route handlers and endpoints
│   ├── core/         # Config, security, and central settings
│   ├── db/           # Database sessions and migrations
│   ├── models/       # SQLAlchemy database models
│   ├── schemas/      # Pydantic schemas for data validation
│   └── services/     # Business logic (auth, docs, vectors)
├── docs/             # Extended documentation and architecture notes
├── scripts/          # Utility scripts for setup and DB management
├── tests/            # Unit and integration test suite
├── .env.example      # Environment variable template
├── requirements.txt  # Project dependencies
└── README.md         # You are here
```

---

## 🛠️ Local Development

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/x2ankit/quarry.git
   cd quarry
   ```

2. **Set up the virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Copy `.env.example` to `.env` and configure your settings:
   ```bash
   cp .env.example .env
   ```

5. **Initialize Database**
   *Ensure PostgreSQL is running locally or via Docker.*
   ```bash
   alembic upgrade head
   ```

### Run the Server

```bash
uvicorn app.main:app --reload
```

### Swagger Docs

Once running, interactive API documentation is available at:  
👉 `http://localhost:8000/docs`

---

## 🌟 Future Directions

Quarry is architected to scale into advanced AI paradigms:
- **RAG:** Moving beyond basic vector search to hybrid, contextual, and agentic RAG.
- **Agents:** Orchestrating autonomous agents capable of executing complex multi-step workflows.
- **Memory:** Implementing persistent state and semantic memory for personalized AI interactions.
- **Evaluation:** Embedding CI/CD pipelines specifically for AI performance and hallucination metrics.
- **Observability:** Granular tracing of LLM token usage, latency, and retrieve-and-read pathways.
- **Inference:** Optimizing model serving layers for low-latency, high-throughput production environments.

---

## 🎓 Why This Project Matters

Quarry is more than an application; it is a demonstration of comprehensive engineering skills across multiple domains:
- 🏗️ **Backend Engineering:** Building scalable, secure, and maintainable REST APIs.
- ⚙️ **AI Systems:** Orchestrating the complex interplay between data, vectors, and models.
- 🧠 **RAG & Agents:** Implementing cutting-edge retrieval and autonomous workflows.
- 🧪 **Evaluation & Observability:** Treating AI as measurable software engineering.
- 🚀 **Deployment & Inference:** Preparing for the realities of cloud-native ML operations.

---

## 🤝 Open Source Journey

Quarry is built with the spirit of the open-source community. It draws inspiration from industry-leading platforms like **Haystack**, **LangGraph**, and **vLLM**.

This repository serves as a foundation for deep OSS contributions, rigorous engineering growth, and preparation for high-impact initiatives like **Google Summer of Code (GSoC)**. It represents a commitment to building transparent, high-quality systems infrastructure.

---

## 👨‍💻 Author

**Ankit Arayan Tripathy**

*AI Engineer → AI Systems Engineer → Inference Engineer → LLM Engineer*

[![GitHub](https://img.shields.io/badge/GitHub-x2ankit-181717?style=for-the-badge&logo=github)](https://github.com/x2ankit)
