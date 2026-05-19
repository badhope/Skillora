# LlamaIndex Wrapper - LlamaIndex 框架包装

这是一个简化版的 LlamaIndex 集成，方便快速使用 LlamaIndex 的核心功能。

---

## 📁 目录

```
llamaindex-wrapper/
├── README.md
├── __init__.py
├── simple_query.py      # 简单查询
├── simple_rag.py        # 简单 RAG
└── simple_query_engine.py # 查询引擎
```

---

## 🚀 快速开始

### 安装依赖
```bash
pip install llama-index llama-index-agent-openai
```

### 使用示例

```python
from llamaindex_wrapper import SimpleRAG

rag = SimpleRAG(api_key="your-key")
rag.load_documents("data/")
result = rag.query("你的问题")
print(result)
```

---

## 📚 模块说明

### SimpleQuery
简单的直接查询。

### SimpleRAG
基于 LlamaIndex 的 RAG 实现。

### SimpleQueryEngine
自定义查询引擎。

---

## 🔗 相关资源

- [LlamaIndex 官方文档](https://docs.llamaindex.ai)
- [AgentHome 中的 LlamaIndex 文档](../../curated-collection/frameworks/llamaindex.md)
