# RAG System Template
Template for building Retrieval-Augmented Generation systems.

## Features

- Document ingestion
- Vector storage
- Semantic search
- Context-aware generation

## Quick Start

```bash
# Copy template
cp -r templates/rag-system my-rag-app
cd my-rag-app

# Install dependencies
pip install -r requirements.txt

# Ingest documents
python ingest.py --data ./documents

# Start API
python app.py
```

## Architecture

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Documents  │ -> │  Vector DB   │ -> │   LLM       │
└─────────────┘    └──────────────┘    └─────────────┘
```

## Project Structure

```
my-rag-app/
├── src/
│   ├── ingest.py          # Document ingestion
│   ├── query.py           # Query processing
│   ├── vector_store.py    # Vector DB integration
│   └── api.py             # REST API
├── documents/             # Document storage
├── tests/
├── .env
└── requirements.txt
```
