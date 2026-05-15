# Tencent AI Prompt Collection

## Overview

This directory contains comprehensive prompt collections for Tencent's AI products, focusing on **Hunyuan** (混元) models and Tencent Cloud AI services. Tencent is one of China's largest technology companies, and their Hunyuan large language model represents their entry into the LLM space with strong enterprise integration capabilities.

## Contents

| File | Description |
|------|-------------|
| [README.md](./README.md) | This overview document |
| [hunyuan-guide.md](./hunyuan-guide.md) | Hunyuan-specific prompts and best practices |
| [api-templates.md](./api-templates.md) | API usage examples and templates |

## Tencent AI Products Covered

### Hunyuan Models
- Hunyuan-pro - Enterprise flagship model
- Hunyuan-standard - Balanced performance
- Hunyuan-lite - Cost-optimized option
- Hunyuan-code - Code specialized model
- Vision models - Image understanding

### Tencent Cloud AI Services
- Tencent Cloud AI Lab
- Cloud AI Platform (TI-ONE)
- Intelligent Speech Platform
- OCR and Document Recognition
- Face Recognition
- TI-Planet (AI Application Platform)

## Official Documentation Links

- **Hunyuan Official**: https://hunyuan.cloud.tencent.com/
- **Tencent Cloud AI**: https://cloud.tencent.com/product/ai
- **API Documentation**: https://cloud.tencent.com/document/product/2710
- **Console**: https://console.cloud.tencent.com/
- **Pricing**: https://cloud.tencent.com/product/2710/pricing

## Key Characteristics

### Model Strengths
- **WeChat Integration**: Direct integration potential with WeChat ecosystem
- **Tencent Ecosystem**: Strong ties to Tencent services (WeChat, QQ, Tencent Games)
- **Gaming AI**: Specialized models for gaming applications
- **Enterprise Ready**: Built for business applications
- **Multimodal**: Vision, speech, and text capabilities

### Unique Features
- **Domain Adaptation**: Pre-trained on Tencent's proprietary data
- **Gaming Specialization**: Strong performance for gaming-related tasks
- **Social Content**: Good understanding of Chinese social media culture
- **Enterprise Security**: Compliance with enterprise security requirements

### Best Use Cases
- WeChat Mini Program AI features
- Gaming NPC dialogue and moderation
- Social media content analysis
- Enterprise business applications
- Integration with Tencent Cloud services
- Chinese market business communications

## Quick Start

### Python SDK

```python
import TencentCloud from '@tencentcloud/tencentcloud-sdk-nodejs'

# Initialize client
client = new TencentCloud.hunyuan_v20230901.Client({
    credential: {
        secretId: 'your-secret-id',
        secretKey: 'your-secret-key',
    },
    region: 'ap-guangzhou',
})

# Call Hunyuan
async function main() {
    const response = await client.ChatStd({
        Query: '解释人工智能在教育领域的应用'
    })
    console.log(response)
}
```

---

## Cross-Platform Adaptation Notes

When adapting prompts from other platforms to Tencent Hunyuan:

1. **Ecosystem Focus**: Emphasize Tencent-specific integrations when relevant
2. **Social Content**: Good for WeChat Moments, QQ discussions
3. **Gaming Context**: Leverage gaming-related capabilities
4. **WeChat Integration**: Native support for Mini Program scenarios
5. **Tencent Cloud Services**: Easy integration with other Tencent Cloud products

### Parameter Mapping

| Concept | Other Platforms | Hunyuan | Notes |
|---------|----------------|---------|-------|
| Temperature | temperature | Temperature | 0.0-1.0 |
| Max tokens | max_tokens | MaxToken | Output limit |
| System prompt | system_prompt | GroupId | Chat group context |
| Streaming | stream | Stream | Boolean flag |

## Version History

- 2024-12: Added Hunyuan Pro and enterprise templates
- 2024-11: Included code-specialized prompts
- 2024-10: Initial release with core Hunyuan models
