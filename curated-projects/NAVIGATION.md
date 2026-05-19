# AgentHome 用户导航指南

> 💡 **你是开发者吗？想要快速找到适合你的 AI Agent 框架或工具？**
> 
> 这份指南将帮助你根据自己的需求快速找到最合适的项目！

---

## 🎯 快速定位

### 🤔 你想要做什么？

#### 1️⃣ 从零开发 AI Agent 应用
**推荐**：
- **[LangChain](frameworks/langchain.md)** - 最流行，文档最全，适合初学者
- **[Dify](applications/dify.md)** - 无需代码，快速原型开发
- **[LlamaIndex](frameworks/llamaindex.md)** - 专注数据处理和 RAG

#### 2️⃣ 构建多智能体协作系统
**推荐**：
- **[MetaGPT](frameworks/metagpt.md)** - 模拟软件公司，适合复杂项目
- **[CrewAI](frameworks/crewai.md)** - 角色化团队，直观易用
- **[AutoGen](frameworks/autogen.md)** - 微软出品，企业级支持

#### 3️⃣ 快速部署 AI 应用（无需编程）
**推荐**：
- **[Coze](applications/coze.md)** - 字节跳动出品，国内首选
- **[AgentGPT](applications/agentgpt.md)** - 浏览器直接使用
- **[Dify](applications/dify.md)** - 开源自托管

#### 4️⃣ 构建对话机器人
**推荐**：
- **[Botpress](applications/botpress.md)** - 企业级开源方案
- **[Voiceflow](applications/voiceflow.md)** - 语音助手首选
- **[Coze](applications/coze.md)** - 多渠道发布

#### 5️⃣ 研究和学习 AI Agent
**推荐**：
- **[MetaGPT](frameworks/metagpt.md)** - ICLR 2024 Oral 论文实现
- **[awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)** - 精选资源列表
- **[AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)** - 微软官方教程

---

## 📊 按技术栈选择

### Python 开发者
| 优先级 | 框架 | 原因 |
|-------|------|------|
| 🥇 | LangChain/LangGraph | Python 优先，生态最全 |
| 🥈 | LlamaIndex | RAG 专用，数据处理强大 |
| 🥉 | CrewAI | 简单直观，入门快速 |

### TypeScript/JavaScript 开发者
| 优先级 | 框架 | 原因 |
|-------|------|------|
| 🥇 | LangChain.js | JavaScript 生态首选 |
| 🥈 | AutoGen | 微软出品，多语言支持 |
| 🥉 | OpenAgents | 新兴框架，协议支持 |

### 企业 / 微软技术栈
| 优先级 | 框架 | 原因 |
|-------|------|------|
| 🥇 | Semantic Kernel | 微软官方，企业级支持 |
| 🥈 | AutoGen | 微软研究院出品 |
| 🥉 | Botpress | 企业对话系统 |

---

## 🎨 按项目类型选择

### 开源框架
```
LangChain          ⭐ 114k - 最流行的 LLM 应用框架
AutoGPT           ⭐ 160k - 自主代理先驱
AutoGen           ⭐ 58k  - 微软多智能体
MetaGPT           ⭐ 47k  - 软件公司模式
CrewAI            ⭐ 20k  - 角色化团队
LlamaIndex        ⭐ 30k  - 数据与 LLM 连接
```

### 无代码平台
```
Dify              ⭐ 60k  - 开源自托管
Coze              -      - 字节跳动出品
AgentGPT          ⭐ 33k  - 浏览器直接用
Botpress          -      - 企业对话系统
Voiceflow         -      - 语音助手首选
```

---

## 🚀 快速开始路径

### 路径 1: 从零学习 AI Agent 开发
```
第1步 → 阅读 [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
第2步 → 尝试 [Dify](applications/dify.md) - 快速原型
第3步 → 学习 [LangChain](frameworks/langchain.md) - 深度理解
第4步 → 探索 [CrewAI](frameworks/crewai.md) - 多智能体
```

### 路径 2: 构建生产级应用
```
第1步 → 选择框架：LangChain 或 AutoGen
第2步 → 设计架构：参考 [LangGraph](frameworks/langgraph.md)
第3步 → 添加知识库：参考 [LlamaIndex](frameworks/llamaindex.md)
第4步 → 部署上线：使用 LangServe 或自托管
```

### 路径 3: 快速落地 AI 应用
```
第1步 → 需求分析：客服/销售/内容/数据？
第2步 → 选择平台：
  - 国内 → [Coze](applications/coze.md)
  - 国外 → [Dify](applications/dify.md) 或 Botpress
第3步 → 配置知识库和工作流
第4步 → 发布到目标平台
```

---

## 📋 常见场景推荐

| 场景 | 推荐方案 | 理由 |
|------|---------|------|
| 客服机器人 | Coze / Botpress | 无代码，多渠道 |
| 内容助手 | Dify / LangChain | RAG 支持，丰富模板 |
| 数据分析 | MetaGPT / LlamaIndex | Data Interpreter |
| 销售助手 | CrewAI / AutoGen | 多角色协作 |
| 语音助手 | Voiceflow | Alexa/Google 原生支持 |
| 自主代理 | AutoGPT | 高度自动化 |

---

## 🎓 学习资源推荐

### 免费教程
- [Microsoft AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [LangChain Academy](https://academy.langchain.com)
- [CrewAI Academy](https://academy.crewai.com)

### 视频教程
- [LangChain YouTube](https://www.youtube.com/@LangChain)
- [Dify 教程 (B站)](https://search.bilibili.com/all?keyword=Dify)

### 书籍
- 《Building LLM Applications》 (即将出版)
- 《Practical AI Agents》

---

## 🔧 工具推荐

### 开发工具
| 工具 | 用途 | 链接 |
|------|------|------|
| LangSmith | 调试和监控 | https://smith.langchain.com |
| LangFuse | 开源可观测性 | https://github.com/langfuse/langfuse |
| Weights & Biases | 实验追踪 | https://wandb.ai |

### 部署工具
| 工具 | 用途 | 链接 |
|------|------|------|
| LangServe | 模型部署 | LangChain 官方 |
| Docker | 容器化 | https://docker.com |
| Vercel | 前端部署 | https://vercel.com |

---

## 💡 常见问题

**Q: 我应该用框架还是自己写？**
> A: 快速验证想法用框架（Dify/Coze），生产级应用考虑框架（LangChain/AutoGen），需要深度定制再考虑自研。

**Q: LangChain vs LlamaIndex 选哪个？**
> A: 需要链式调用和工作流 → LangChain；专注数据处理和 RAG → LlamaIndex；两者可以结合使用。

**Q: 多智能体框架哪个好？**
> A: 简单任务 → CrewAI；复杂协作 → MetaGPT；企业级 → AutoGen。

---

## 🎯 下一步

1. **确定你的需求** - 参考上面的快速定位
2. **选择一个项目** - 点击链接查看详情
3. **阅读快速开始** - 按照文档运行示例
4. **开始你的项目** - 用学到的东西构建自己的 AI Agent

---

**🌟 祝你开发愉快！**

如果有任何问题，欢迎提交 Issue 或参与讨论！
