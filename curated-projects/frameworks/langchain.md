# LangChain & LangGraph

## 基本信息
- **GitHub**: https://github.com/langchain-ai/langchain
- **官网**: https://langchain.com
- **⭐ Stars**: 114k+
- **语言**: Python / JavaScript
- **维护者**: LangChain AI

## 简介

LangChain 是最早专门为大语言模型构建应用开发框架的开源项目。它提供了模块化组件和链式结构，使得开发者能够轻松地将 LLMs 与其他数据源和计算资源结合起来，构建复杂的 AI 应用。

LangGraph 是 LangChain 生态的重要组成部分，用于在 LangChain 基础上支持状态化、可观测、图结构化的智能体执行流程。

## 核心特点

### LangChain
- **模块化架构** - 将复杂 LLM 应用分解为可组合的组件
- **丰富的集成** - 支持 50+ 种 LLM 提供商，多种向量数据库
- **Chain 与 Agent** - 链式调用和智能体工具调用
- **Retrieval 系统** - 完整的 RAG 支持
- **记忆管理** - 对话历史和上下文维护
- **活跃生态** - 庞大的社区和丰富的示例代码

### LangGraph
- **图状态机** - 将应用建模为有向图
- **持久化执行** - 代理可以在失败后自动恢复
- **Human-in-the-loop** - 支持人工干预
- **完整记忆系统** - 短期工作记忆 + 长期持久记忆
- **LangChain 生态集成** - 与所有 LangChain 组件兼容

## 适用场景

- RAG 应用（检索增强生成）
- 聊天机器人和对话系统
- 文档问答系统
- 内容生成工具
- 复杂多步骤工作流
- 需要持久化的生产级应用

## 快速开始

### LangChain
```bash
pip install langchain langchain-openai
```

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

llm = ChatOpenAI(model="gpt-4")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"input": "Tell me about AI agents"})
```

### LangGraph
```bash
pip install langgraph
```

```python
from typing import TypedDict, Annotated, Sequence
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

class AgentState(TypedDict):
    messages: Annotated[Sequence[Any], "add_messages"]

def agent(state):
    llm = ChatOpenAI(model="gpt-4")
    return {"messages": [llm.invoke(state["messages"])]}

graph = StateGraph(AgentState)
graph.add_node("agent", agent)
graph.set_entry_point("agent")
graph.add_edge("agent", END)

app = graph.compile()
```

## 学习资源

- [官方文档](https://python.langchain.com)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [LangSmith 调试平台](https://smith.langchain.com)
- [LangChain AI 博客](https://blog.langchain.com)
- [GitHub Examples](https://github.com/langchain-ai/langchain/tree/master/examples)

## 推荐理由

LangChain 是目前使用最广泛、生态最成熟的智能体开发框架之一。它开创了大语言模型模块化调用的范式，为后续框架奠定了基础。适合从简单到复杂的各种 LLM 应用开发。
