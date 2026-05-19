# OpenAgents

## 基本信息
- **GitHub**: https://github.com/xlang-ai/openagents
- **官网**: https://openagents.org
- **⭐ Stars**: 8k+
- **语言**: Python / TypeScript
- **维护者**: XLang Research

## 简介

OpenAgents 是一个开放的多智能体平台，原生支持 MCP（Model Context Protocol）和 A2A（Agent-to-Agent）协议。它专注于智能体的互操作性和规模化部署，让智能体可以在网络中持久运行和协作。

## 核心特点

### 协议支持
- **原生 MCP** - 支持 Model Context Protocol
- **原生 A2A** - 支持 Agent-to-Agent 通信协议
- **协议桥接** - 连接不同协议的智能体

### 网络架构
- **持久化网络** - 智能体可以在网络中持久运行
- **规模化** - 支持大规模智能体网络
- **服务发现** - 自动发现和连接其他智能体

### 平台特性
- **Web 界面** - 直观的智能体管理界面
- **API 优先** - 完整的 API 支持
- **可观测性** - 内置监控和日志
- **多模型支持** - 支持多种 LLM

## 适用场景

- 智能体生态系统构建
- 需要互操作性的复杂系统
- 大规模多智能体部署
- 研究和实验
- 企业级智能体网络
- 跨平台智能体协作

## 快速开始

```bash
# 克隆并安装
git clone https://github.com/xlang-ai/openagents.git
cd openagents
pip install -e .
```

```bash
# 启动后端
cd openagents/backend
uvicorn main:app --reload

# 启动前端
cd openagents/frontend
npm install && npm run dev
```

## Docker 部署
```bash
cd openagents
docker compose up
```

## 学习资源

- [官方文档](https://openagents.org/docs)
- [GitHub Wiki](https://github.com/xlang-ai/openagents/wiki)
- [研究论文](https://arxiv.org/abs/2308.03688)
- [Discord 社区](https://discord.gg/openagents)

## 推荐理由

OpenAgents 是面向未来的多智能体平台，原生支持最新的 MCP 和 A2A 协议。如果你正在构建智能体生态系统或需要大规模多智能体协作，OpenAgents 提供了最佳的基础设施和协议支持。
