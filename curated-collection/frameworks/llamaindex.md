# LlamaIndex & LlamaAgents

## 基本信息
- **GitHub (LlamaIndex)**: https://github.com/run-llama/llama_index
- **GitHub (LlamaAgents)**: https://github.com/run-llama/llama-agents
- **官网**: https://www.llamaindex.ai
- **⭐ Stars**: 30k+
- **语言**: Python
- **维护者**: LlamaIndex 团队

## 简介

LlamaIndex（原名 GPT Index）是一个专注于数据与 LLM 连接的框架。它提供灵活的索引和检索功能，支持多种数据源（数据库、文档、API 等）的整合，是构建 RAG（检索增强生成）应用的最佳选择之一。

LlamaAgents 是 LlamaIndex 生态系统的新成员，用于构建多智能体系统。

## 核心特点

### LlamaIndex
- **数据连接** - 支持多种数据源的整合
- **灵活索引** - 提供多种索引类型（向量、列表、树等）
- **检索增强** - 强大的 RAG 支持
- **文档加载** - 支持多种文档格式
- **查询引擎** - 丰富的查询模式
- **工具集成** - 与 LangChain 等生态系统兼容

### LlamaAgents
- **分布式服务架构** - 每个代理都是独立运行的微服务
- **标准化 API** - 通过中央控制平面协调代理
- **显式编排流程** - 开发者可以直接定义代理间的交互顺序
- **易于部署** - 独立启动、扩展和监控每个代理
- **可观测性** - 内置工具监控系统和每个代理的质量和性能

## 适用场景

- 知识库问答系统
- 文档管理与检索
- 企业 RAG 应用
- 多智能体协作系统
- 数据密集型 LLM 应用
- 生产级多代理系统

## 快速开始

### LlamaIndex
```bash
pip install llama-index llama-index-agent-openai
```

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# 加载文档
documents = SimpleDirectoryReader("data/").load_data()

# 创建索引
index = VectorStoreIndex.from_documents(documents)

# 创建查询引擎
query_engine = index.as_query_engine()

# 查询
response = query_engine.query("What is RAG?")
print(response)
```

### LlamaAgents
```bash
pip install llama-agents llama-index-agent-openai
```

```python
from llama_agents import AgentService, ControlPlaneServer, SimpleMessageQueue
from llama_index.agent.openai import OpenAIAgent

# 创建消息队列
message_queue = SimpleMessageQueue()

# 创建控制平面
control_plane = ControlPlaneServer(
    message_queue=message_queue,
    host="localhost",
    port=8000
)

# 创建代理服务
agent = OpenAIAgent.from_tools(...)
agent_service = AgentService(
    agent=agent,
    message_queue=message_queue,
    host="localhost",
    port=8001
)
```

## 学习资源

- [LlamaIndex 文档](https://docs.llamaindex.ai)
- [LlamaAgents 文档](https://docs.llamaindex.ai/en/stable/llama_agents/)
- [LlamaIndex 博客](https://www.llamaindex.ai/blog)
- [GitHub Examples](https://github.com/run-llama/llama_index/tree/main/examples)
- [LlamaHub](https://llamahub.ai) - 组件库

## 推荐理由

LlamaIndex 专注于数据与 LLM 的连接，是构建 RAG 应用的首选。它的索引和检索功能非常强大。LlamaAgents 进一步扩展了这一能力，支持构建生产级的多智能体系统。如果你的应用主要涉及数据处理和知识检索，LlamaIndex 是最佳选择。
