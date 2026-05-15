# Alibaba AI Prompt Collection

## Overview

This directory contains comprehensive prompt collections for Alibaba's AI products, focusing on **Qwen** models and the **Tongyi Qianwen** platform. Alibaba Cloud is the cloud computing arm of Alibaba Group, and Qwen represents their state-of-the-art large language model series.

## Contents

| File | Description |
|------|-------------|
| [README.md](./README.md) | This overview document |
| [qwen-prompts.md](./qwen-prompts.md) | Prompts optimized for Qwen model interactions |
| [tongyi-guide.md](./tongyi-guide.md) | Tongyi Qianwen platform-specific best practices |

## Alibaba AI Products Covered

### Qwen Models
- Qwen-Max - Flagship model with longest context
- Qwen-Plus - Balanced performance and cost
- Qwen-Turbo - High-speed inference
- Qwen2.5 series - Open-source models (Qwen2.5-72B, etc.)
- Qwen-Audio - Multimodal audio understanding

### Tongyi Qianwen Platform
- Model Studio - Development and deployment platform
- API services - Direct model access
- Enterprise solutions - Custom AI applications
-百炼 ( Bailian ) - AI agent platform

## Official Documentation Links

- **Tongyi Qianwen**: https://tongyi.aliyun.com/
- **Qwen Official**: https://qwenlm.github.io/
- **API Documentation**: https://help.aliyun.com/document_detail/2434465.html
- **DashScope (API Platform)**: https://dashscope.console.aliyun.com/
- **Model Gallery**: https://modelscope.cn/

## Key Characteristics

### Model Strengths
- Excellent multilingual capabilities (Chinese ↔ English)
- Strong code generation and reasoning
- Long context understanding (up to 128K tokens)
- Open-source availability (Qwen2.5 series)
- Cost-effective pricing

### Unique Features
- **Long Context**: Qwen-Max supports 128K context length
- **Open Source**: Qwen2.5 models available on ModelScope
- **Multimodal**: Vision, audio, and code capabilities
- **Function Calling**: Native support for tool use

### Best Use Cases
- Cross-lingual content (Chinese ↔ English)
- Code generation and debugging
- Long document analysis
- Complex reasoning tasks
- Integration with Alibaba Cloud services

## Quick Start

### Python SDK

```python
import os
from dashscope import DashScope

# Set API key
os.environ['DASHSCOPE_API_KEY'] = 'your-api-key'

# Simple completion
response = DashScope.call(
    model='qwen-max',
    prompt='解释什么是云计算',
    max_tokens=1000
)
print(response.output.text)
```

### API Call Example

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "qwen-max",
    "input": {
      "prompt": "用中文写一首关于春天的诗"
    },
    "parameters": {
      "max_tokens": 500,
      "temperature": 0.8
    }
  }'
```

---

## Cross-Platform Adaptation Notes

When adapting prompts from other platforms to Qwen:

1. **Context Length**: Take advantage of 128K context for comprehensive prompts
2. **System Prompts**: Qwen responds well to detailed system prompts
3. **Code Generation**: Built-in code expertise - no need for specialized prompts
4. **Language Mixing**: Qwen handles Chinese-English mixing well
5. **Tool Use**: Native function calling support for agentic workflows

### Parameter Adjustments

| Other Platform | Qwen Equivalent | Notes |
|----------------|-----------------|-------|
| max_tokens | max_tokens | Same parameter |
| temperature | temperature | 0.7 typical default |
| top_p | top_p | 0.8-0.95 recommended |
| - | top_k | Additional filtering option |

## Version History

- 2024-12: Added Qwen2.5 and long context prompts
- 2024-11: Included function calling examples
- 2024-10: Initial collection with core Qwen models
