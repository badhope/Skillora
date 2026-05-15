# Baidu AI Prompt Collection

## Overview

This directory contains comprehensive prompt collections for Baidu's AI products, focusing on **ERNIE Bot** and **Wenxin Qianfan** platforms. Baidu is China's leading search engine and AI company, with ERNIE (Enhanced Representation through Knowledge Integration) being their flagship large language model.

## Contents

| File | Description |
|------|-------------|
| [README.md](./README.md) | This overview document |
| [ernie-prompts.md](./ernie-prompts.md) | Prompts optimized for ERNIE Bot interactions |
| [wenxin-guide.md](./wenxin-guide.md) | Wenxin Qianfan platform-specific best practices |

## Baidu AI Products Covered

### ERNIE Bot
- ERNIE 4.0 - Latest generation with advanced reasoning capabilities
- ERNIE 3.5 - Production-ready model with strong performance
- ERNIE Lite - Cost-effective option for simpler tasks

### Wenxin Qianfan
- Enterprise-level AI development platform
- Model fine-tuning capabilities
- API integration tools
- Custom model deployment

## Official Documentation Links

- **ERNIE Bot Official**: https://yiyan.baidu.com/
- **Wenxin Qianfan**: https://qianfan.ai.baidu.com/
- **API Documentation**: https://cloud.baidu.com/doc/WENXINWORKSHOP/
- **Developer Console**: https://console.bce.baidu.com/

## Key Characteristics

### Chinese Language Optimization
Baidu's models are specifically trained with:
- Extensive Chinese corpus including classical literature
- Modern internet Chinese (websites, social media)
- Domain-specific Chinese terminology
- Regional dialect variations

### Strengths
- Superior Chinese language understanding and generation
- Strong knowledge base covering Chinese culture and history
- Excellent for tasks requiring Chinese context
- Good integration with Baidu services (search, maps, cloud)

### Best Use Cases
- Chinese content creation and translation
- Business documents in Chinese markets
- Technical documentation for Chinese audiences
- Cultural and historical queries
- Integration with Baidu ecosystem

## Quick Start

```python
# Wenxin Qianfan API Example
import qianfan

# Initialize the client
client = qianfan.Qianfan(
    ak="your-access-key",
    sk="your-secret-key"
)

# Call ERNIE Bot
response = client.ChatCompletion.create(
    model="ernie-4.0-8k",
    messages=[
        {"role": "user", "content": "请用中文解释量子计算的基本原理"}
    ]
)
```

## Cross-Platform Adaptation Notes

When adapting prompts from other platforms to Baidu:

1. **Language Priority**: Explicitly request Chinese output when needed
2. **Cultural Context**: Baidu models understand Chinese cultural references better
3. **Length Expectations**: Chinese output tends to be more concise than English
4. **System Prompts**: Use role-based system prompts for better results
5. **Temperature Settings**: Lower temperature (0.3-0.5) for factual queries, higher for creative

## Version History

- 2024-12: Initial collection with ERNIE 4.0 and Wenxin Qianfan support
