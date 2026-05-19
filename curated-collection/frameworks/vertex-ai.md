# Google Vertex AI

## 基本信息
- **官网**: https://cloud.google.com/vertex-ai
- **GitHub**: https://github.com/googleapis/python-aiplatform
- **⭐ Stars**: 1.5k+
- **语言**: Python / Java / Node.js / Go
- **维护者**: Google

## 简介

Vertex AI 是 Google Cloud 的机器学习平台，提供完整的 AI 开发和部署能力。支持训练、调优、部署和监控机器学习模型。

## 核心特点

### 模型支持
- **Google 模型**: Gemini 系列模型
- **开源模型**: Llama、Mistral 等
- **自定义模型**: 训练和部署自己的模型

### 部署选项
- **在线预测**: 实时 API 调用
- **批量预测**: 大规模数据处理
- **边缘部署**: 设备端推理

### 管理功能
- **模型版本控制**
- **监控和日志**
- **A/B 测试**
- **自动扩缩容**

## 适用场景

- 企业级 AI 应用
- 需要大规模部署
- 需要与 Google Cloud 集成

## 快速开始

```bash
pip install google-cloud-aiplatform
```

```python
from vertexai.preview.generative_models import GenerativeModel

model = GenerativeModel("gemini-pro")
response = model.generate_content("Hello, Gemini!")
print(response.text)
```

### 流式响应
```python
for chunk in model.generate_content("写一首诗", stream=True):
    print(chunk.text)
```

## 学习资源

- [官方文档](https://cloud.google.com/vertex-ai/docs)
- [GitHub Examples](https://github.com/GoogleCloudPlatform/generative-ai)
- [教程](https://cloud.google.com/vertex-ai/docs/get-started)

## 推荐理由

如果你在 Google Cloud 上构建应用，Vertex AI 是最佳选择。它提供了完整的 ML 生命周期管理能力。
