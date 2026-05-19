# AgentScope

## 基本信息
- **GitHub**: https://github.com/modelscope/agentscope
- **官网**: https://modelscope.cn/agent
- **⭐ Stars**: 8k+
- **语言**: Python
- **维护者**: ModelScope

## 简介

AgentScope 是由 ModelScope 团队开发的多智能体平台，专注于为开发者提供易于使用和定制的大语言模型智能体应用开发平台。它特别强调多智能体协作、容错机制和用户友好性。

## 核心特点

### 开发友好
- **低门槛** - 简单易学的 API
- **丰富示例** - 大量可运行的示例代码
- **可视化** - 内置监控和调试工具

### 多智能体支持
- **多角色** - 支持多种智能体角色
- **协作机制** - 丰富的智能体间协作模式
- **消息传递** - 灵活的通信机制

### 生产就绪
- **容错机制** - 完善的错误处理
- **状态管理** - 持久化和恢复
- **性能优化** - 高效的资源利用

## 适用场景

- 快速原型开发
- 多智能体应用研究
- 对话系统开发
- 任务自动化
- 教育和学习
- 小型到中型项目

## 快速开始

```bash
pip install agentscope
```

```python
import agentscope
from agentscope import msghub
from agentscope.agents import DialogAgent

# 配置
agentscope.init(model="openai", api_key="your-key")

# 创建智能体
agent1 = DialogAgent(name="Alice", model="gpt-4")
agent2 = DialogAgent(name="Bob", model="gpt-4")

# 多智能体对话
with msghub(agent2) as hub:
    hub.add(agent1)
    agent1()
```

## 学习资源

- [官方文档](https://modelscope.cn/docs)
- [GitHub Examples](https://github.com/modelscope/agentscope/tree/main/examples)
- [ModelScope 社区](https://modelscope.cn/community)

## 推荐理由

AgentScope 特别适合想要快速上手多智能体开发的开发者。它的低门槛和丰富示例让学习曲线变得平缓。ModelScope 的背书也保证了项目的质量和持续发展。
