# Semantic Kernel

## 基本信息
- **GitHub**: https://github.com/microsoft/semantic-kernel
- **官网**: https://learn.microsoft.com/en-us/semantic-kernel
- **⭐ Stars**: 23k+
- **语言**: C# / Python / JavaScript
- **维护者**: Microsoft

## 简介

Semantic Kernel 是微软出品的开源 SDK，用于将 AI 大语言模型与传统编程语言集成。它提供了轻量级的混合 AI 应用开发框架，支持提示词模板、链式调用、插件系统等功能。特别适合与微软生态系统集成。

## 核心特点

- **多语言支持** - 支持 C#、Python、JavaScript
- **微软生态集成** - 与 Azure、Teams、Office 等深度集成
- **插件系统** - 丰富的插件生态系统
- **提示词工程** - 支持提示词模板和管理
- **链式调用** - 支持函数链式调用
- **记忆管理** - 对话历史和上下文管理
- **Semantic Memory** - 语义记忆功能

## 适用场景

- 企业级 AI 应用
- 与微软生态系统集成
- 办公自动化
- 业务流程增强
- 跨平台 AI 应用开发
- 生产级应用部署

## 快速开始

### C#
```bash
dotnet add package Microsoft.SemanticKernel
```

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;

var builder = Kernel.CreateBuilder();
builder.Services.AddOpenAIChatCompletion(
    "gpt-4",
    "your-api-key"
);

var kernel = builder.Build();

var result = await kernel.InvokePromptAsync(
    "What is Semantic Kernel?"
);
Console.WriteLine(result);
```

### Python
```bash
pip install semantic-kernel
```

```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

kernel = sk.Kernel()
kernel.add_chat_service(
    "chat-gpt",
    OpenAIChatCompletion("gpt-4", "your-api-key")
)

prompt = "What is Semantic Kernel?"
response = await kernel.invoke_prompt(prompt)
print(response)
```

## 学习资源

- [官方文档](https://learn.microsoft.com/en-us/semantic-kernel)
- [GitHub Examples](https://github.com/microsoft/semantic-kernel/tree/main/samples)
- [Semantic Kernel Blog](https://devblogs.microsoft.com/semantic-kernel)
- [Microsoft Learn](https://learn.microsoft.com/en-us/training/paths/semantic-kernel/)
- [YouTube 教程](https://www.youtube.com/@MicrosoftDeveloper)

## 推荐理由

Semantic Kernel 是微软官方出品，拥有企业级的支持和文档。它的多语言支持和与微软生态的深度集成使其特别适合企业级应用开发。如果你正在使用 Azure、Office、Teams 等微软产品，Semantic Kernel 是绝佳选择。
