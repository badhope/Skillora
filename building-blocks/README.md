# 🧱 Building Blocks - 可拼装模块

> **这是 AgentHome 的核心！** 你可以从这里选择需要的模块，拼装成你自己的智能体项目！

---

## 📁 目录结构

```
building-blocks/
│
├── 🛠️ frameworks-integrations/      # ⭐ 框架集成包装
│   ├── langchain-wrapper/          # LangChain 包装
│   │   ├── simple_chain.py         # 简单链式调用
│   │   ├── simple_agent.py         # 简单智能体
│   │   └── simple_rag.py           # 简单 RAG
│   │
│   ├── llamaindex-wrapper/         # LlamaIndex 包装
│   │   ├── simple_rag.py           # 简单 RAG
│   │   └── simple_query.py         # 简单查询
│   │
│   ├── crewai-wrapper/             # CrewAI 包装
│   │   └── simple_crew.py          # 简单多智能体团队
│   │
│   └── autogen-wrapper/            # AutoGen 包装
│       └── simple_chat.py          # 简单多智能体对话
│
├── 🔧 tools/                       # ⭐ 通用工具
│   ├── llm-wrappers/              # ⭐ LLM 包装
│   │   └── openai_wrapper.py       # OpenAI API 包装
│   │
│   ├── vector-dbs/                 # ⭐ 向量数据库
│   │   ├── chroma_wrapper.py       # Chroma DB
│   │   └── pinecone_wrapper.py    # Pinecone
│   │
│   ├── memory/                     # ⭐ 记忆模块
│   │   └── buffer_memory.py        # 缓冲记忆
│   │
│   └── connectors/                  # ⭐ 外部服务连接器
│       ├── search_connector.py     # 搜索连接器
│       ├── file_connector.py       # 文件连接器
│       └── web_connector.py        # 网页连接器
│
└── 🚀 capabilities/                 # ⭐ 高级能力
    ├── rag/                       # RAG 能力
    │   └── simple_rag.py          # 简单 RAG
    │
    └── multi-agent/              # 多智能体
        └── simple_crew.py        # 简单多智能体团队
```

---

## 🚀 快速开始

### 方式 1：选择性拼装

```python
# 1. 选择 LLM 包装
from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper

# 2. 选择记忆模块
from building_blocks.tools.memory.buffer_memory import BufferMemory

# 3. 选择 RAG 能力
from building_blocks.capabilities.rag.simple_rag import SimpleRAG

# 4. 拼装！
llm = OpenAIWrapper(api_key="...")
memory = BufferMemory()
rag = SimpleRAG(llm=llm, memory=memory)

# 5. 使用！
rag.add_document("你的知识文档")
response = rag.query("你的问题")
```

### 方式 2：使用框架包装

```python
# LangChain 包装
from building_blocks.frameworks_integrations.langchain_wrapper import SimpleChain
chain = SimpleChain(api_key="...")

# LlamaIndex 包装
from building_blocks.frameworks_integrations.llamaindex_wrapper import SimpleRAG
rag = SimpleRAG(api_key="...")

# CrewAI 包装
from building_blocks.frameworks_integrations.crewai_wrapper import SimpleCrew
crew = SimpleCrew(api_key="...")
```

---

## 📋 模块列表

### 🛠️ 框架集成（4个）

| 模块 | 说明 | 文件 |
|------|------|------|
| **LangChain Wrapper** | LangChain 简化版，包含 Chain、Agent、RAG | [查看](frameworks-integrations/langchain-wrapper/) |
| **LlamaIndex Wrapper** | LlamaIndex 简化版，包含 RAG 和 Query | [查看](frameworks-integrations/llamaindex-wrapper/) |
| **CrewAI Wrapper** | CrewAI 简化版，多智能体团队 | [查看](frameworks-integrations/crewai-wrapper/) |
| **AutoGen Wrapper** | AutoGen 简化版，多智能体对话 | [查看](frameworks-integrations/autogen-wrapper/) |

### 🔧 工具模块（4类）

| 模块 | 说明 | 状态 |
|------|------|------|
| **OpenAI Wrapper** | OpenAI API 包装 | ✅ 可用 |
| **Chroma Wrapper** | Chroma 向量数据库 | ✅ 可用 |
| **Pinecone Wrapper** | Pinecone 向量数据库 | ✅ 可用 |
| **Buffer Memory** | 对话缓冲记忆 | ✅ 可用 |
| **Search Connector** | 网络搜索连接器 | ✅ 可用 |
| **File Connector** | 文件读写连接器 | ✅ 可用 |
| **Web Connector** | 网页抓取连接器 | ✅ 可用 |

### 🚀 高级能力（2个）

| 模块 | 说明 | 状态 |
|------|------|------|
| **Simple RAG** | 简单检索增强生成 | ✅ 可用 |
| **Simple Crew** | 简单多智能体团队 | ✅ 可用 |

---

## 💡 使用建议

### 场景 1: 简单的聊天机器人
```
选择：
  - LLM Wrapper (OpenAI) ✅
  - Buffer Memory ✅
```

### 场景 2: 知识库问答
```
选择：
  - LLM Wrapper (OpenAI) ✅
  - Vector DB (Chroma) ✅
  - Simple RAG ✅
```

### 场景 3: 团队协作智能体
```
选择：
  - LLM Wrapper (OpenAI) ✅
  - Simple Crew ✅
```

### 场景 4: 带搜索的智能体
```
选择：
  - LLM Wrapper (OpenAI) ✅
  - Search Connector ✅
  - File Connector ✅
```

---

## 📦 安装依赖

```bash
# 基础依赖
pip install openai

# LangChain 相关
pip install langchain langchain-openai langchain-community

# LlamaIndex 相关
pip install llama-index llama-index-llms-openai

# CrewAI
pip install crewai crewai-tools

# 向量数据库
pip install chromadb
pip install pinecone-client

# 连接器
pip install requests duckduckgo-search
```

---

## 🎯 下一步

1. **查看 ready-made-agents/** - 可以直接使用的完整项目
2. **参考 templates/** - 项目模板
3. **查看 curated-collection/** - 精选项目文档

---

**💡 提示：** 每个模块都有详细的使用示例！
