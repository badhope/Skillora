# Anthropic SDK

## 基本信息
- **GitHub**: https://github.com/anthropics/anthropic-sdk-python
- **官网**: https://docs.anthropic.com/en/api/getting-started
- **⭐ Stars**: 2k+
- **语言**: Python / TypeScript
- **维护者**: Anthropic

## 简介

Anthropic SDK 是官方的 Claude API 客户端库，提供对 Claude 模型的直接访问。支持 Messages API、工具调用、文件上传等功能。

## 核心特点

### 官方支持
- **Messages API**: 完整的对话功能
- **工具调用**: 支持函数调用
- **文件上传**: 支持多模态输入
- **流式输出**: 实时响应

### 平台支持
- **直接 API**: Anthropic 官方 API
- **AWS Bedrock**: 通过 Bedrock 调用
- **Google Vertex AI**: 通过 Vertex AI 调用

### 功能完整
- Token 计数
- 消息批处理
- 错误处理
- TypeScript 类型支持

## 适用场景

- 需要直接调用 Claude 的应用
- 构建基于 Claude 的聊天机器人
- 需要访问 Claude 特有功能

## 快速开始

```bash
pip install anthropic
```

```python
from anthropic import Anthropic

client = Anthropic(api_key="your-key")

message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude!"}]
)

print(message.content[0].text)
```

### 工具调用
```python
from anthropic import Anthropic, Tool

client = Anthropic()

response = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1024,
    tools=[
        Tool(
            name="search",
            description="搜索网络信息",
            input_schema={
                "type": "object",
                "properties": {"query": {"type": "string"}}
            }
        )
    ],
    messages=[{"role": "user", "content": "今天天气怎么样？"}]
)
```

## 学习资源

- [官方文档](https://docs.anthropic.com/en/api/getting-started)
- [Cookbooks](https://github.com/anthropics/claude-cookbooks)
- [API 参考](https://docs.anthropic.com/en/api/messages)

## 推荐理由

如果你需要使用 Claude 模型，这是官方推荐的 SDK。它提供了最完整的功能和最佳的性能。
