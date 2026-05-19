# AgentHome 项目配置文件

本目录包含 AgentHome 项目的配置文件和模板，帮助开发者快速配置和使用不同的框架。

---

## 📁 目录结构

```
configs/
├── README.md                    # 本文件
├── langchain/                   # LangChain 配置示例
│   ├── basic.yaml
│   ├── rag.yaml
│   └── agent.yaml
├── crewai/                      # CrewAI 配置示例
│   └── crew.yaml
├── autogen/                     # AutoGen 配置示例
│   └── multi-agent.yaml
├── metagpt/                     # MetaGPT 配置示例
│   └── software-company.yaml
└── templates/                   # 通用模板
    ├── agent-config.yaml
    └── project-structure.yaml
```

---

## 🚀 快速使用

### LangChain 配置

```yaml
# configs/langchain/basic.yaml
llm:
  provider: openai
  model: gpt-4
  temperature: 0.7
  api_key: ${OPENAI_API_KEY}

memory:
  type: buffer
  window_size: 10

tools:
  - name: search
    type: TavilySearch
  - name: calculator
    type: Calculator

retrieval:
  vector_store: pinecone
  index_name: my-index
```

### CrewAI 配置

```yaml
# configs/crewai/crew.yaml
agents:
  - role: Research Analyst
    goal: Find the most relevant information
    backstory: You are an expert researcher
    
  - role: Content Writer
    goal: Write high-quality content
    backstory: You are an experienced writer

tasks:
  - description: Research AI trends
    expected_output: Research report
    agent: research_analyst
    
  - description: Write article
    expected_output: 1000-word article
    agent: content_writer
    dependencies: [research_task]

process:
  type: sequential  # or hierarchical

verbose: true
```

### MetaGPT 配置

```yaml
# configs/metagpt/software-company.yaml
roles:
  - product_manager
  - architect
  - project_manager
  - engineer
  - qa_engineer

sop:
  mode: software_company
  include_resources: true

llm:
  model: gpt-4-turbo
  temperature: 0.7

investment:
  mode: auto
  budget: 100

max_rely:
  round: 5
```

---

## 📝 配置模板

### 通用 Agent 配置

```yaml
# configs/templates/agent-config.yaml
agent:
  name: "MyAgent"
  description: "Agent description"
  
  llm:
    provider: "openai"  # openai, anthropic, local, etc.
    model: "gpt-4"
    temperature: 0.7
    max_tokens: 2000
    
  memory:
    type: "buffer"  # buffer, vector, summary
    window_size: 10
    max_tokens: 10000
    
  tools:
    - name: "search"
      enabled: true
    - name: "calculator"
      enabled: true
      
  prompts:
    system: "You are a helpful assistant."
    
  constraints:
    max_iterations: 10
    timeout_seconds: 300
    
  output:
    format: "text"  # text, json, markdown
```

---

## 🔧 环境变量模板

创建 `.env.example` 文件：

```bash
# LLM Providers
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key

# Vector Databases
PINECONE_API_KEY=your-pinecone-key
PINECONE_ENV=us-east-1

# Search Tools
TAVILY_API_KEY=your-tavily-key

# Deployment
DEPLOYMENT_ENV=production
API_PORT=8000
```

---

## 📦 Docker Compose 模板

```yaml
# docker-compose.yml
version: '3.8'

services:
  agent:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./data:/app/data
      
  vector-db:
    image: chromadb/chroma
    ports:
      - "8001:8000"
    volumes:
      - ./chromadb:/app/chromadb
```

---

## 🎯 配置最佳实践

1. **环境变量** - 不要在代码中硬编码 API Key
2. **版本控制** - 将配置模板加入 Git，但排除敏感信息
3. **配置分离** - 开发、测试、生产环境使用不同配置
4. **文档化** - 为每个配置项添加注释说明

---

## 🔗 相关资源

- [LangChain 配置文档](https://python.langchain.com/docs)
- [CrewAI 配置文档](https://docs.crewai.com)
- [AutoGen 配置文档](https://microsoft.github.io/autogen)
- [MetaGPT 配置文档](https://docs.deepwisdom.ai/main/en/)
