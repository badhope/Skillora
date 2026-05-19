# 🏠 AgentHome - AI Agent Development Toolkit

> **Build AI Agents Like Building Blocks!**
> 
> AgentHome is a comprehensive toolkit for AI agent development, covering from low-level components to high-level applications. You can:
> 1. **Selective Assembly** - Choose modules from building-blocks to assemble your own agent
> 2. **Ready-to-use** - Pick complete projects from ready-made-agents
> 3. **Reference & Learn** - Explore documentation of well-known projects in curated-collection

---

<!-- LANGUAGE SWITCH -->
<div align="right">
  <a href="#chinese-version" style="padding: 4px 8px; background: #f0f0f0; border-radius: 4px; text-decoration: none;">中文</a>
  <a href="#english-version" style="padding: 4px 8px; background: #4a90d9; color: white; border-radius: 4px; text-decoration: none; margin-left: 4px;">English</a>
</div>

---

## 🎯 Why Choose AgentHome?

| Traditional Approach | AgentHome Approach |
|---------------------|-------------------|
| 😕 Start from scratch, write everything yourself | 🧱 Modular, pick only what you need |
| 📚 Search everywhere, unsure what to choose | 📋 Well-organized, clear categorization |
| 🚫 Hard to find good ready-made projects | 🚀 Complete projects ready to use |

---

## 📁 Complete Directory Structure

```
AgentHome/
│
├── 🌟 curated-collection/          # Curated Project Docs (External Projects)
│   ├── frameworks/               # Framework Documentation
│   ├── applications/             # Application Documentation
│   ├── resources/                # Learning Resources
│   ├── NAVIGATION.md            # User Navigation (Must Read!)
│   └── README.md
│
├── 🧱 building-blocks/            # ⭐ Assemblable Modules (Core!)
│   ├── frameworks-integrations/  # Framework Integration Wrappers
│   │   ├── langchain-wrapper/
│   │   ├── llamaindex-wrapper/
│   │   ├── crewai-wrapper/
│   │   └── autogen-wrapper/
│   │
│   ├── tools/                    # General Tools
│   │   ├── llm-wrappers/        # LLM Wrappers (OpenAI, Anthropic, etc.)
│   │   ├── vector-dbs/          # Vector Databases (Chroma, Pinecone, FAISS)
│   │   ├── memory/              # Memory Modules (Buffer, Long-term)
│   │   ├── connectors/          # External Connectors (Web, File, Search)
│   │   ├── translation/         # Translation Services
│   │   └── text-processing/     # Text Processing Tools
│   │
│   └── capabilities/             # Advanced Capabilities
│       ├── rag/                 # RAG Systems
│       ├── multi-agent/         # Multi-Agent Systems
│       ├── tool-calling/        # Tool Calling
│       └── workflow/            # Workflow Management
│
├── 🚀 ready-made-agents/          # ⭐ Ready-to-run Projects
│   ├── chat-assistant/          # Chat Assistant
│   ├── research-agent/          # Research Agent
│   ├── customer-support/        # Customer Support Bot
│   └── task-automation/         # Task Automation
│
├── 📋 templates/                  # Project Templates
├── 🔧 configs/                    # Configuration Files
├── 📚 docs/                       # Documentation
└── README.md                     # This File
```

---

## 🚀 Two Ways to Use

### Method 1: Selective Assembly (Recommended)

Choose modules from `building-blocks/` to assemble your own project:

```python
# Example: Build a chatbot with RAG

# 1. Choose LLM wrapper
from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper

# 2. Choose memory module
from building_blocks.tools.memory.buffer_memory import BufferMemory

# 3. Choose RAG capability
from building_blocks.capabilities.rag.simple_rag import SimpleRAG

# 4. Assemble!
llm = OpenAIWrapper(api_key="...")
memory = BufferMemory()
rag = SimpleRAG(llm=llm, memory=memory)

# 5. Use!
rag.add_document("your_knowledge_document.pdf")
response = rag.query("your question?")
```

### Method 2: Use Ready-made Projects

Pick a complete project from `ready-made-agents/`:

```bash
# Choose chat assistant
cd ready-made-agents/chat-assistant
pip install -r requirements.txt
python main.py

# Or choose research agent
cd ready-made-agents/research-agent
pip install -r requirements.txt
python main.py
```

---

## 🎯 Quick Start

### Step 1: Choose Your Path

| You Want to... | Recommended Path |
|----------------|------------------|
| Quick Experience | `ready-made-agents/chat-assistant` |
| Document Processing | `ready-made-agents/research-agent` |
| Build Custom Agent | `building-blocks/` |
| Learn & Explore | `curated-collection/NAVIGATION.md` |

### Step 2: Get Started

```bash
# Clone the repository
git clone https://github.com/badhope/AgentHome.git
cd AgentHome

# Option A: Use ready-made project (Recommended)
cd ready-made-agents/chat-assistant
pip install -r requirements.txt
python main.py

# Option B: Build your own
cd ..
# Explore building-blocks to select modules
```

---

## 📊 Components Overview

### 1. 🧱 building-blocks (Assemblable Modules)

**Core Value:** Provide reusable code modules for selective assembly

**Includes:**
- `tools/` - Basic tools (LLM wrappers, memory, vector databases, connectors)
- `capabilities/` - Advanced capabilities (RAG, multi-agent, tool calling, workflow)
- `frameworks-integrations/` - Framework wrappers (LangChain, LlamaIndex, etc.)

**Use Case:** Custom development without starting from scratch

---

### 2. 🚀 ready-made-agents (Complete Projects)

**Core Value:** Full ready-to-run projects, use directly or modify

**Includes:**
- `chat-assistant/` - Simple chat assistant
- `research-agent/` - Knowledge-based Q&A system
- `customer-support/` - Customer support bot
- `task-automation/` - Task automation agent

**Use Case:** Quick deployment without assembly

---

### 3. 🌟 curated-collection (Curated Projects)

**Core Value:** Documentation and links to well-known projects

**Includes:**
- `frameworks/` - Docs for LangChain, AutoGen, CrewAI, MetaGPT, etc.
- `applications/` - Docs for AutoGPT, Dify, Coze, etc.
- `NAVIGATION.md` - User navigation guide

**Use Case:** Explore industry best practices and projects

---

## 💡 Usage Guide

### Scenario 1: Build a Customer Support Bot

**Recommended Path:**
1. Check `ready-made-agents/customer-support/` - Ready-made solution
2. Or build from `building-blocks/`:
   - Choose LLM wrapper
   - Choose memory module
   - Choose RAG (if knowledge base needed)

### Scenario 2: Build a Research Assistant

**Recommended Path:**
1. Use `ready-made-agents/research-agent/` - Ready-made
2. Modify or build your own based on it

### Scenario 3: Explore Frameworks

**Recommended Path:**
1. Check `curated-collection/NAVIGATION.md`
2. Choose frameworks based on your needs

---

## 📖 More Resources

- **User Navigation** - [NAVIGATION.md](curated-collection/NAVIGATION.md)
- **Assemblable Modules** - [building-blocks/](building-blocks/)
- **Ready-made Projects** - [ready-made-agents/](ready-made-agents/)
- **Curated Collection** - [curated-collection/](curated-collection/)

---

## 🤝 Contributing

Welcome to contribute:
1. Add new building-blocks
2. Add new ready-made-agents
3. Improve documentation
4. Report issues

---

## 📜 License

MIT License

---

**🎉 Start building AI agents like building blocks now!**

---

<a id="chinese-version"></a>

# 🏠 AgentHome - 智能体开发工具库

> **你可以像搭积木一样开发智能体！**
> 
> AgentHome 是一个集成了从底层到高级的完整 AI 智能体开发工具库。你可以：
> 1. **选择性拼装** - 从 building-blocks 选择需要的模块自己组装
> 2. **直接使用** - 从 ready-made-agents 选择完整的项目直接使用
> 3. **参考学习** - 从 curated-collection 查看知名项目的文档

---

<div align="right">
  <a href="#chinese-version" style="padding: 4px 8px; background: #4a90d9; color: white; border-radius: 4px; text-decoration: none;">中文</a>
  <a href="#english-version" style="padding: 4px 8px; background: #f0f0f0; border-radius: 4px; text-decoration: none; margin-left: 4px;">English</a>
</div>

---

## 🎯 为什么选择 AgentHome？

| 传统方式 | AgentHome 方式 |
|---------|---------------|
| 😕 从零开始，一切都要自己写 | 🧱 模块化，选择你需要的模块 |
| 📚 到处找资料，不知道选什么 | 📋 分门别类，目录清晰 |
| 🚫 找不到现成的好项目 | 🚀 完整项目直接用 |

---

## 📁 完整目录结构

```
AgentHome/
│
├── 🌟 curated-collection/          # 精选项目文档（外部项目）
│   ├── frameworks/               # 知名框架文档
│   ├── applications/             # 知名应用文档
│   ├── resources/                # 学习资源
│   ├── NAVIGATION.md            # 用户导航（必读！）
│   └── README.md
│
├── 🧱 building-blocks/            # ⭐ 可拼装的模块（核心！）
│   ├── frameworks-integrations/  # 框架集成包装
│   │   ├── langchain-wrapper/
│   │   ├── llamaindex-wrapper/
│   │   ├── crewai-wrapper/
│   │   └── autogen-wrapper/
│   │
│   ├── tools/                    # 通用工具
│   │   ├── llm-wrappers/        # LLM 包装（OpenAI、Anthropic 等）
│   │   ├── vector-dbs/          # 向量数据库（Chroma、Pinecone、FAISS）
│   │   ├── memory/              # 记忆模块（缓冲、长期记忆）
│   │   ├── connectors/          # 外部连接器（网页、文件、搜索）
│   │   ├── translation/         # 翻译服务
│   │   └── text-processing/     # 文本处理工具
│   │
│   └── capabilities/             # 高级能力
│       ├── rag/                 # RAG 系统
│       ├── multi-agent/         # 多智能体系统
│       ├── tool-calling/        # 工具调用
│       └── workflow/            # 工作流管理
│
├── 🚀 ready-made-agents/          # ⭐ 完整的可运行项目
│   ├── chat-assistant/          # 聊天助手
│   ├── research-agent/          # 研究助手
│   ├── customer-support/        # 客服机器人
│   └── task-automation/         # 任务自动化
│
├── 📋 templates/                  # 项目模板
├── 🔧 configs/                    # 配置文件
├── 📚 docs/                       # 文档
└── README.md                     # 本文件
```

---

## 🚀 两种使用方式

### 方式 1：选择性拼装（推荐）

从 `building-blocks/` 选择需要的模块，自己组装成项目：

```python
# 示例：构建一个带 RAG 的聊天机器人

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
rag.add_document("your_knowledge_document.pdf")
response = rag.query("your question?")
```

### 方式 2：直接使用完整项目

从 `ready-made-agents/` 选择一个完整项目直接使用：

```bash
# 选择聊天助手
cd ready-made-agents/chat-assistant
pip install -r requirements.txt
python main.py

# 或者选择研究助手
cd ready-made-agents/research-agent
pip install -r requirements.txt
python main.py
```

---

## 🎯 快速开始

### 步骤 1：选择你的需求

| 你想要... | 推荐路径 |
|----------|---------|
| 快速体验 | `ready-made-agents/chat-assistant` |
| 处理文档 | `ready-made-agents/research-agent` |
| 自己拼装 | `building-blocks/` |
| 参考学习 | `curated-collection/NAVIGATION.md` |

### 步骤 2：开始使用

```bash
# 克隆仓库
git clone https://github.com/badhope/AgentHome.git
cd AgentHome

# 方式 A：使用现成项目（推荐）
cd ready-made-agents/chat-assistant
pip install -r requirements.txt
python main.py

# 方式 B：自己拼装
cd ..
# 查看 building-blocks 选择模块
```

---

## 📊 各部分说明

### 1. 🧱 building-blocks（可拼装模块）

**核心价值：** 提供可复用的代码模块，你可以选择性拼装

**包含：**
- `tools/` - 基础工具（LLM 包装、记忆、向量库、连接器）
- `capabilities/` - 高级能力（RAG、多智能体、工具调用、工作流）
- `frameworks-integrations/` - 框架包装（LangChain、LlamaIndex 等）

**使用场景：** 你需要定制化开发，不想从零开始

---

### 2. 🚀 ready-made-agents（完整项目）

**核心价值：** 完整的可运行项目，直接使用或修改

**包含：**
- `chat-assistant/` - 简单聊天助手
- `research-agent/` - 带知识库的问答系统
- `customer-support/` - 客服机器人
- `task-automation/` - 任务自动化

**使用场景：** 你想快速落地，不想自己拼装

---

### 3. 🌟 curated-collection（精选项目）

**核心价值：** 收集知名项目的文档和链接

**包含：**
- `frameworks/` - LangChain、AutoGen、CrewAI、MetaGPT 等文档
- `applications/` - AutoGPT、Dify、Coze 等文档
- `NAVIGATION.md` - 用户导航指南

**使用场景：** 你想了解行业里都有什么好项目

---

## 💡 使用指南

### 场景 1：我要做一个客服机器人

**推荐路径：**
1. 看 `ready-made-agents/customer-support/` - 有现成的
2. 或者从 `building-blocks/` 自己拼装：
   - 选 LLM 包装
   - 选记忆模块
   - 选 RAG（如果需要知识库）

### 场景 2：我要做一个研究助手

**推荐路径：**
1. 用 `ready-made-agents/research-agent/` - 现成的
2. 修改它或参考它自己做

### 场景 3：我想了解有什么好框架

**推荐路径：**
1. 看 `curated-collection/NAVIGATION.md`
2. 根据需求选择框架

---

## 📖 更多资源

- **用户导航** - [NAVIGATION.md](curated-collection/NAVIGATION.md)
- **拼装模块** - [building-blocks/](building-blocks/)
- **现成项目** - [ready-made-agents/](ready-made-agents/)
- **精选项目** - [curated-collection/](curated-collection/)

---

## 🤝 贡献

欢迎贡献：
1. 添加新的 building-blocks
2. 添加新的 ready-made-agents
3. 完善文档
4. 报告问题

---

## 📜 License

MIT License

---

**🎉 现在开始，你可以像搭积木一样开发智能体了！**