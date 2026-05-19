# LangChain Wrapper - LangChain 框架包装

这是一个简化版的 LangChain 集成，方便快速使用 LangChain 的核心功能。

---

## 📁 目录

```
langchain-wrapper/
├── README.md
├── __init__.py
├── simple_chain.py      # 简单链式调用
├── simple_agent.py      # 简单智能体
└── simple_rag.py       # 简单 RAG
```

---

## 🚀 快速开始

### 安装依赖
```bash
pip install langchain langchain-openai
```

### 使用示例

```python
from langchain_wrapper import SimpleChain

chain = SimpleChain(
    model_name="gpt-4",
    api_key="your-key"
)

result = chain.invoke("解释什么是人工智能")
print(result)
```

---

## 📚 模块说明

### SimpleChain
简单的链式调用，适合基本的 LLM 应用。

### SimpleAgent
带工具调用能力的简单智能体。

### SimpleRAG
基于 LangChain 的 RAG 实现。

---

## 🔗 相关资源

- [LangChain 官方文档](https://python.langchain.com)
- [AgentHome 中的 LangChain 文档](../../curated-collection/frameworks/langchain.md)
