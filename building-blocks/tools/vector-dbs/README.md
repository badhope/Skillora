# Vector DBs - Vector Database Wrappers

Simplified wrappers for popular vector databases, making integration quick and easy.

---

## 📁 Directory Structure

```
vector-dbs/
├── README.md
├── __init__.py
├── chroma_wrapper.py    # Chroma DB (Local/File-based)
├── pinecone_wrapper.py  # Pinecone (Cloud)
├── faiss_wrapper.py     # FAISS (Local High-performance)
├── milvus_wrapper.py    # Milvus (Cloud/On-premise)
└── base.py             # Base Class
```

---

## 🚀 Quick Start

### Chroma (Local)
```python
from vector_dbs.chroma_wrapper import ChromaWrapper

db = ChromaWrapper()
db.add_texts(["Document 1", "Document 2"])
results = db.search("query")
```

### Pinecone (Cloud)
```python
from vector_dbs.pinecone_wrapper import PineconeWrapper

db = PineconeWrapper(api_key="...", index="my-index")
db.upsert([("id1", vector, {})])
results = db.query(vector)
```

### FAISS (Local)
```python
from vector_dbs.faiss_wrapper import FAISSWrapper

db = FAISSWrapper(dimension=1536)
db.add_documents(embeddings, documents)
results = db.search(query_embedding)
```

### Milvus (Cloud/On-premise)
```python
from vector_dbs.milvus_wrapper import MilvusWrapper

db = MilvusWrapper(host="localhost", port="19530")
db.add_documents(embeddings, contents)
results = db.search(query_embedding)
```

---

## 📊 Comparison

| Database | Type | Advantages | Use Case |
|----------|------|------------|----------|
| Chroma | Local/File | Easy to use, no setup | Development, testing |
| Pinecone | Cloud | Managed, high-performance | Production |
| FAISS | Local | Ultra-fast, memory-efficient | Large-scale vectors |
| Milvus | Cloud/On-prem | Scalable, enterprise-grade | Enterprise applications |