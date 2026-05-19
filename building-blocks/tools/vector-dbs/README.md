# Vector DBs - 向量数据库包装

这里提供了常用向量数据库的简化包装，方便快速集成使用。

---

## 📁 目录

```
vector-dbs/
├── README.md
├── __init__.py
├── chroma_wrapper.py    # Chroma DB
├── pinecone_wrapper.py  # Pinecone
└── base.py             # 基类
```

---

## 🚀 快速开始

### Chroma (本地)
```python
from vector_dbs.chroma_wrapper import ChromaWrapper

db = ChromaWrapper()
db.add_texts(["文档1", "文档2"])
results = db.search("查询")
```

### Pinecone (云端)
```python
from vector_dbs.pinecone_wrapper import PineconeWrapper

db = PineconeWrapper(api_key="...", index="my-index")
db.upsert([("id1", vector, {})])
results = db.query(vector)
```

---

## 📊 对比

| 数据库 | 类型 | 优点 | 适用场景 |
|--------|------|------|---------|
| Chroma | 本地/文件 | 简单易用 | 开发测试 |
| Pinecone | 云服务 | 托管、高性能 | 生产环境 |
| FAISS | 本地 | 高性能 | 大规模向量 |
