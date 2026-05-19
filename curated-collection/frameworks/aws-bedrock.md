# AWS Bedrock

## 基本信息
- **官网**: https://aws.amazon.com/bedrock/
- **文档**: https://docs.aws.amazon.com/bedrock/
- **语言**: Python / JavaScript / Java / Go
- **维护者**: AWS

## 简介

AWS Bedrock 是一项完全托管的服务，提供对多种基础模型（FM）的访问。你可以通过 API 调用来自 Anthropic、Cohere、Meta、Stability AI 等提供商的模型。

## 核心特点

### 模型提供商
- **Anthropic**: Claude 3 系列
- **Cohere**: Command、Embed 模型
- **Meta**: Llama 3 系列
- **Stability AI**: Stable Diffusion
- **Amazon**: Titan 系列

### 安全与合规
- **数据隐私**: 你的数据不会用于训练
- **SOC 合规**: 符合 SOC 标准
- **加密**: 静态和传输中加密

### 企业功能
- **私有 VPC 访问**
- **IAM 集成**
- **CloudWatch 监控**
- **API Gateway 集成**

## 适用场景

- 需要企业级安全性
- 已在 AWS 生态中
- 需要多种模型选择

## 快速开始

```bash
pip install boto3
```

```python
import boto3
import json

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.invoke_model(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": "Hello"}]
    })
)

result = json.loads(response['body'].read())
print(result['content'][0]['text'])
```

## 学习资源

- [官方文档](https://docs.aws.amazon.com/bedrock/)
- [开发指南](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html)
- [示例代码](https://github.com/aws-samples/aws-bedrock-samples)

## 推荐理由

如果你在 AWS 上运行应用，Bedrock 是最便捷的 LLM 访问方式。它提供了多种模型选择和企业级安全性。
