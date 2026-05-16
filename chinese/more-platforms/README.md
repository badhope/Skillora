# More Chinese Platforms

Additional Chinese AI platforms including 360, Zhipu, iFlytek, and Xiaoice.

## 📋 Platforms

- [360 智脑](#360-智脑)
- [智谱 AI (Zhipu)](#智谱-ai-zhipu)
- [科大讯飞 (iFlytek)](#科大讯飞-iflytek)
- [微软小冰 (Xiaoice)](#微软小冰-xiaoice)

## 360 智脑

Powerful AI models from Qihoo 360, well-regarded for Chinese-language understanding.

### 360 Prompt Guide

```
你是一个有帮助的AI助手。请直接、准确地回答问题。
```

### Coding Assistant

```
你是一个专业的编程助手，请帮助我：

任务：[你的编程需求]
语言：[编程语言]
要求：
- 清晰的代码
- 详细的注释
- 完整的示例
```

### Content Creation

```
请帮我创作：

类型：[内容类型]
主题：[主题]
受众：[目标受众]
风格：[风格]
```

### 360 API Template

```python
# Example 360 API usage
import requests

url = "https://api.360.cn/v1/chat/completions"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "model": "360GPT-Pro",
    "messages": [
        {"role": "user", "content": "Your prompt here"}
    ]
}
response = requests.post(url, headers=headers, json=data)
```

### Official Resources

- [360 智脑平台](https://ai.360.cn/)
- [360 API 文档](https://ai.360.cn/docs)

---

## 智谱 AI (Zhipu)

GLM (General Language Model) series from Zhipu AI, one of China's leading LLM providers.

### Model Family

| Model | Description |
|-------|-------------|
| GLM-4 | Latest flagship model |
| GLM-3-Turbo | Fast, cost-effective |
| CodeLlama-GLM | Code-specialized |

### GLM Prompt Format

```
你是一个乐于助人的AI助手。

用户：[你的问题]
助手：
```

### System Prompt

```
你是智谱AI开发的智能助手，名字叫智谱清言。你要帮助用户解决各种问题，包括回答问题、编写代码、翻译文本等。
```

### Code Generation

```
你是一个编程专家。请编写以下代码：

要求：
- 语言：[Python/JavaScript/其他]
- 功能：[描述]
- 风格：[简洁/详细/其他]

请提供完整、可运行的代码。
```

### Creative Writing

```
你是一个创意写作专家。请帮我：

类型：[故事/文章/诗歌等]
主题：[主题]
风格：[风格]
长度：[长度]
```

### Zhipu API Example

```python
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="your_api_key")
response = client.chat.completions.create(
    model="glm-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Official Resources

- [智谱 AI 官网](https://www.zhipuai.cn/)
- [GLM API 文档](https://open.bigmodel.cn/dev/api)
- [智谱清言](https://chatglm.cn/)

---

## 科大讯飞 (iFlytek)

A leading Chinese AI company famous for speech recognition, now offering strong LLMs.

### Xinghuo (Spark) Models

| Model | Features |
|-------|----------|
| Spark 4.0 | Latest flagship |
| Spark Pro | Professional |
| Spark Lite | Lightweight |

### Prompt Guide

```
你是讯飞星火AI助手，请帮助用户完成以下任务。
```

### Speech-related Prompts

```
你是一个语音处理专家。请帮我：

任务：[语音识别/合成/其他]
内容：[文本内容]
```

### General Assistant

```
请帮我：[你的需求]

请详细说明，给出清晰的结果。
```

### iFlytek API Template

```python
import requests

url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
headers = {"Authorization": "Bearer YOUR_KEY"}
data = {
    "model": "spark-v3.5",
    "messages": [{"role": "user", "content": "prompt"}]
}
```

### Official Resources

- [讯飞开放平台](https://www.xfyun.cn/)
- [星火认知大模型](https://xinghuo.xfyun.cn/)
- [API 文档](https://www.xfyun.cn/doc/spark/Web.html)

---

## 微软小冰 (Xiaoice)

Microsoft's Xiaoice, specialized in emotional intelligence and conversational AI.

### Xiaoice Features

- Emotionally intelligent conversations
- Social interaction focus
- Creative content generation
- Multi-modal capabilities

### Conversation Style

```
你是小冰，一个亲切、有趣、会聊天的AI伙伴。请用轻松自然的方式对话。
```

### Creative Content

```
请帮我创作：

类型：[文案/诗歌/故事]
风格：[温馨/幽默/创意]
主题：[主题]
```

### Social Content

```
请帮我写：

平台：[微博/朋友圈/小红书]
内容：[描述]
风格：[风格]
```

### Official Resources

- [微软小冰](https://www.xiaoice.com/)
- [小冰平台](https://www.xiaoice.com/Platform)

---

## Cross-Platform Adaptation

All these Chinese platform prompts can be easily adapted from our general prompt templates with minor style adjustments for each platform's conventions.
