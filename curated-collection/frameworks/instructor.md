# Instructor

## 基本信息
- **GitHub**: https://github.com/jxnl/instructor
- **官网**: https://python.useinstructor.com
- **⭐ Stars**: 26k+
- **语言**: Python / TypeScript
- **维护者**: Jason Liu

## 简介

Instructor 是一个结构化输出库，让 LLM 输出符合 Pydantic 模型。它支持多种 LLM 提供商，提供自动重试、验证和流式输出功能。

## 核心特点

### 结构化输出
- **Pydantic 集成**: 自动验证和解析
- **自动重试**: 输出不符合模型时自动重试
- **流式输出**: 支持边生成边验证

### 多提供商支持
- OpenAI
- Anthropic Claude
- Google Gemini
- Cohere
- LlamaIndex
- LangChain

### 功能扩展
- **函数调用**: 自动生成工具调用
- **并行处理**: 批量生成
- **缓存**: 结果缓存

## 适用场景

- 需要结构化输出的应用
- 表单填写和数据提取
- API 参数验证
- 数据分析和处理

## 快速开始

```bash
pip install instructor
```

```python
from instructor import patch
from pydantic import BaseModel
from openai import OpenAI

client = patch(OpenAI())

class User(BaseModel):
    name: str
    age: int
    email: str

user = client.chat.completions.create(
    model="gpt-4",
    response_model=User,
    messages=[
        {"role": "user", "content": "Extract: John is 30 years old and his email is john@example.com"}
    ]
)

print(user.name)  # John
print(user.age)   # 30
```

### Anthropic 支持
```python
from anthropic import Anthropic
from instructor import patch

client = patch(Anthropic())

result = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1024,
    response_model=MyModel,
    messages=[{"role": "user", "content": "Your prompt"}]
)
```

## 学习资源

- [官方文档](https://python.useinstructor.com)
- [GitHub Examples](https://github.com/jxnl/instructor/tree/main/examples)
- [YouTube Tutorial](https://www.youtube.com/watch?v=HAn9vnJy6S4)

## 推荐理由

Instructor 是处理 LLM 结构化输出的最佳工具之一。它的自动重试和验证功能大大简化了开发流程。
