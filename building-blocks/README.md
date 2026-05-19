# 🧱 Building Blocks - 可拼装模块

> **这是 AgentHome 的核心！** 你可以从这里选择需要的模块，拼装成你自己的智能体项目！

---

## 📁 目录结构

```
building-blocks/
│
├── 🛠️ frameworks-integrations/      # 框架集成包装
│   ├── langchain-wrapper/          # LangChain 简单包装
│   ├── llamaindex-wrapper/         # LlamaIndex 简单包装
│   ├── crewai-wrapper/             # CrewAI 简单包装
│   └── autogen-wrapper/            # AutoGen 简单包装
│
├── 🔧 tools/                       # 通用工具
│   ├── llm-wrappers/              # LLM 包装
│   │   ├── openai_wrapper.py
│   │   └── anthropic_wrapper.py
│   │
│   ├── vector-dbs/                # 向量数据库
│   │   ├── chroma_wrapper.py
│   │   └── pinecone_wrapper.py
│   │
│   ├── memory/                    # 记忆模块
│   │   ├── buffer_memory.py
│   │   └── summary_memory.py
│   │
│   └── connectors/                # 外部服务
│       ├── search_connector.py
│       └── file_connector.py
│
└── 🚀 capabilities/               # 高级能力
    ├── rag/                       # RAG 能力
    │   └── simple_rag.py
    │
    ├── multi-agent/              # 多智能体
    │   └── simple_crew.py
    │
    ├── tool-calling/             # 工具调用
    │   └── tool_agent.py
    │
    └── workflow/                 # 工作流
        └── sequential_workflow.py
```

---

## 🚀 快速开始

### 选择模块拼装你的项目

```python
# 1. 选择 LLM 包装
from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper

# 2. 选择记忆模块
from building_blocks.tools.memory.buffer_memory import BufferMemory

# 3. 选择 RAG 能力
from building_blocks.capabilities.rag.simple_rag import SimpleRAG

# 4. 拼装
llm = OpenAIWrapper(api_key="...")
memory = BufferMemory()
rag = SimpleRAG(llm=llm, memory=memory)

# 5. 开始使用
response = rag.query("问题")
```

---

## 📋 模块列表

### 框架集成

| 模块 | 说明 | 链接 |
|------|------|------|
| LangChain Wrapper | LangChain 简化版 | [查看](frameworks-integrations/langchain-wrapper/) |
| LlamaIndex Wrapper | LlamaIndex 简化版 | [查看](frameworks-integrations/llamaindex-wrapper/) |
| CrewAI Wrapper | CrewAI 简化版 | [查看](frameworks-integrations/crewai-wrapper/) |
| AutoGen Wrapper | AutoGen 简化版 | [查看](frameworks-integrations/autogen-wrapper/) |

### 工具模块

| 模块 | 说明 | 链接 |
|------|------|------|
| OpenAI Wrapper | OpenAI API 包装 | [查看](tools/llm-wrappers/) |
| Anthropic Wrapper | Anthropic API 包装 | [查看](tools/llm-wrappers/) |
| Chroma Wrapper | Chroma DB 包装 | [查看](tools/vector-dbs/) |
| Pinecone Wrapper | Pinecone 包装 | [查看](tools/vector-dbs/) |
| Buffer Memory | 缓冲记忆 | [查看](tools/memory/) |
| Summary Memory | 摘要记忆 | [查看](tools/memory/) |

### 能力模块

| 模块 | 说明 | 链接 |
|------|------|------|
| Simple RAG | 简单 RAG 系统 | [查看](capabilities/rag/) |
| Simple Crew | 简单多智能体 | [查看](capabilities/multi-agent/) |
| Tool Agent | 工具调用代理 | [查看](capabilities/tool-calling/) |
| Sequential Workflow | 顺序工作流 | [查看](capabilities/workflow/) |

---

## 💡 使用建议

### 场景 1: 简单的聊天机器人
```
选择：
  - LLM Wrapper (OpenAI)
  - Buffer Memory
```

### 场景 2: 知识库问答
```
选择：
  - LLM Wrapper (OpenAI)
  - Vector DB (Chroma)
  - Simple RAG
```

### 场景 3: 团队协作智能体
```
选择：
  - LLM Wrapper (OpenAI)
  - Simple Crew (multi-agent)
  - Tool Calling
```

---

## 🎯 下一步

1. **查看 ready-made-agents/** - 可以直接使用的完整项目
2. **参考 templates/** - 项目模板
3. **查看 curated-collection/** - 精选项目文档

---

**💡 提示：** 每个模块都有 README，告诉你如何使用它！
