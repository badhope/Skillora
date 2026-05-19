# Microsoft AutoGen

## 基本信息
- **GitHub**: https://github.com/microsoft/autogen
- **官网**: https://microsoft.github.io/autogen
- **⭐ Stars**: 58.1k+
- **语言**: Python / .NET
- **维护者**: Microsoft Research

## 简介

AutoGen 是由微软研究院创建的多智能体框架，它通过对话模式来建模 LLM 应用。代理通过结构化对话进行交互——双人聊天、群组聊天等。它是早期探索多智能体协作的先驱框架之一。

## 核心特点

- **对话驱动架构** - 将 LLM 应用建模为多智能体之间的对话
- **多样化聊天模式** - 支持双人聊天、群组聊天等多种对话模式
- **Human-in-the-loop** - 内置人类参与功能
- **.NET 支持** - 同时支持 Python 和 .NET
- **AutoGen Studio** - 无代码 Studio 选项
- **工具集成** - 丰富的工具调用和扩展机制
- **MCP 协议支持** - 有限的 MCP 协议支持

## 适用场景

- 多智能体协作系统
- 对话式应用开发
- 需要人类参与的工作流
- 企业级 AI 应用
- 研究和原型开发

## 快速开始

```bash
pip install pyautogen
```

```python
import os
from autogen import ConversableAgent

# 配置代理
assistant = ConversableAgent(
    name="assistant",
    system_message="You are a helpful AI assistant.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]}
)

user_proxy = ConversableAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "coding", "use_docker": False}
)

# 启动对话
chat_result = user_proxy.initiate_chat(
    assistant,
    message="Tell me a joke about AI agents."
)
```

## 学习资源

- [官方文档](https://microsoft.github.io/autogen/docs/Getting-Started)
- [AutoGen 教程](https://microsoft.github.io/autogen/docs/tutorial/introduction)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [GitHub Examples](https://github.com/microsoft/autogen/tree/main/samples)
- [研究论文](https://arxiv.org/abs/2308.08155)

## 推荐理由

AutoGen 是微软研究院的重要成果，拥有成熟的技术积累和企业级支持。它的对话模式对于构建多智能体协作系统非常直观。适合想要探索多智能体协作的开发者，特别是与微软生态系统集成的场景。
