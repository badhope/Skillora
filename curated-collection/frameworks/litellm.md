# litellm

## 基本信息
- **GitHub**: https://github.com/BerriAI/litellm
- **官网**: https://docs.litellm.ai
- **⭐ Stars**: 44.9k+
- **语言**: Python
- **维护者**: BerriAI

## 简介

litellm 是一个统一的 LLM API 网关，支持调用 100+ LLM 服务商的 API，全部使用 OpenAI 格式。它提供了成本跟踪、负载均衡、日志记录等企业级功能。

## 核心特点

### 统一 API
- **支持 100+ LLM**: OpenAI、Anthropic、Bedrock、VertexAI、Azure、Cohere、HuggingFace 等
- **OpenAI 格式**: 所有 API 都转换为 OpenAI 格式
- **统一调用**: 一行代码切换不同模型

### 企业级功能
- **成本跟踪**: 实时监控 API 费用
- **负载均衡**: 自动路由到最优后端
- **防护栏**: 内容过滤和安全检查
- **日志记录**: 完整的请求日志

### 部署方式
- **代理模式**: 运行本地代理服务器
- **SDK 模式**: 直接调用
- **Docker 部署**: 容器化支持

## 适用场景

- 多 LLM 服务商管理
- 企业级 LLM 应用
- 需要成本控制的场景
- 需要统一 API 的项目

## 快速开始

```bash
pip install litellm
```

```python
from litellm import completion

# 调用 OpenAI
response = completion(model="gpt-4", messages=[{"role": "user", "content": "Hello"}])

# 调用 Anthropic
response = completion(model="claude-3-opus", messages=[{"role": "user", "content": "Hello"}])

# 调用 Bedrock
response = completion(model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0", messages=[{"role": "user", "content": "Hello"}])
```

### 代理模式
```bash
litellm --model-list /path/to/models.json
```

## 学习资源

- [官方文档](https://docs.litellm.ai)
- [GitHub Examples](https://github.com/BerriAI/litellm/tree/main/examples)
- [Discord 社区](https://discord.gg/litellm)

## 推荐理由

litellm 是企业级 LLM 应用的必备工具。它的统一 API 抽象让你可以轻松切换不同的 LLM 服务商，同时提供了完善的企业级功能。如果你需要管理多个 LLM 后端，litellm 是最佳选择。
