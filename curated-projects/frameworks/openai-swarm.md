# OpenAI Swarm

## 基本信息
- **GitHub**: https://github.com/openai/swarm
- **官网**: https://developer.openai.com/swarm
- **⭐ Stars**: 15k+
- **语言**: Python
- **维护者**: OpenAI

## 简介

OpenAI Swarm 是 OpenAI 发布的实验性多智能体编排框架，旨在简化多智能体系统的开发和编排。它通过轻量级的方式实现智能体之间的协调和交接，特别适合构建复杂的客户服务和销售工作流。

## 核心特点

### 轻量级设计
- **极简架构** - 没有复杂的依赖
- **易于理解** - 学习曲线平缓
- **快速上手** - 几行代码即可运行

### 智能体协作
- **Handoffs（交接）** - 智能体之间可以平滑交接任务
- **Context Variables** - 跨智能体共享上下文
- **动态路由** - 基于对话流动态选择智能体

### 可扩展性
- **无中心化管理** - 真正的去中心化架构
- **可组合** - 易于与其他系统集成
- **生产就绪** - 适合生产环境部署

## 适用场景

- 客户服务自动化
- 销售和潜在客户开发
- 多步骤咨询流程
- 需要角色分工的工作流
- 简单的多智能体交互
- 快速原型开发

## 快速开始

```bash
pip install openai swarm
```

```python
from swarm import Swarm, Agent

client = Swarm()

def transfer_to_sales(context):
    return sales_agent

def transfer_to_support(context):
    return support_agent

sales_agent = Agent(
    name="Sales Agent",
    instructions="You are a sales agent. Help with product inquiries.",
    functions=[transfer_to_support]
)

support_agent = Agent(
    name="Support Agent",
    instructions="You are a support agent. Help with technical issues.",
    functions=[transfer_to_sales]
)

response = client.run(
    agent=sales_agent,
    messages=[{"role": "user", "content": "I have a question about pricing."}]
)
print(response.messages[-1]["content"])
```

## 学习资源

- [官方文档](https://developer.openai.com/swarm)
- [GitHub Examples](https://github.com/openai/swarm/tree/main/examples)
- [OpenAI Cookbook](https://cookbook.openai.com)

## 推荐理由

OpenAI Swarm 是最轻量级的多智能体框架之一。它的设计理念简单直接，特别适合构建需要多角色切换的工作流。如果你想快速尝试多智能体系统，Swarm 是绝佳选择。
