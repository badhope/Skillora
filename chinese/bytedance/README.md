# ByteDance AI Prompt Collection

## Overview

This directory contains comprehensive prompt collections for ByteDance's AI products, focusing on **Doubao** (豆包) models and ByteDance's AI platform. ByteDance is the company behind TikTok (Douyin) and Toutiao, and has emerged as a major player in the AI space with their Doubao large language model and火山引擎 (Volcengine) AI platform.

## Contents

| File | Description |
|------|-------------|
| [README.md](./README.md) | This overview document |
| [doubao-prompts.md](./doubao-prompts.md) | Doubao-specific prompts and best practices |

## ByteDance AI Products Covered

### Doubao Models
- Doubao-pro - Enterprise flagship model
- Doubao-general - General purpose model
- Doubao-lite - Cost-optimized version
- Doubao-emotion - Emotional intelligence enhanced
- Vision models - Image understanding

### ByteDance AI Platform (火山引擎)
- 火山方舟 (VolcEngine Ark)
- Model Serving
- Fine-tuning Services
- AI Application Platform

## Official Documentation Links

- **Doubao Official**: https://www.doubao.com/
- **火山引擎 (Volcengine)**: https://www.volcengine.com/
- **方舟平台 (Ark)**: https://www.volcengine.com/product/ark
- **API Documentation**: https://www.volcengine.com/docs/82379/1263482
- **Console**: https://console.volcengine.com/

## Key Characteristics

### Model Strengths
- **Social Media Mastery**: Deep understanding of TikTok/Douyin content culture
- **Creative Content**: Excellent for short-form video scripts, social media content
- **Entertainment Focus**: Strong performance on entertainment-related tasks
- **Trend Awareness**: Up-to-date knowledge of internet trends and viral content
- **Multimodal**: Native support for video, image, and text

### Unique Features
- **Trend Integration**: Models trained on trending content patterns
- **Youth-oriented**: Better understanding of Gen-Z language and culture
- **Creative Excellence**: Specialized for creative content generation
- **Creator-focused**: Tools designed for content creators

### Best Use Cases
- Short-form video content (TikTok/Douyin/YouTube Shorts)
- Social media marketing
- Influencer content strategy
- Trend analysis
- Gen-Z targeted content
- Entertainment industry applications
- Creative writing

## Quick Start

### Python SDK

```python
 volcenginesdkarkruntime = volcenginesdkarkruntime

# Initialize client
client = volcenginesdkarkruntime.Ark(
    api_key="your-api-key"
)

# Simple chat
response = client.chat.completions.create(
    model="doubao-pro",
    messages=[
        {"role": "user", "content": "帮我写一个短视频脚本"}
    ]
)
print(response.choices[0].message.content)
```

---

## Cross-Platform Adaptation Notes

When adapting prompts from other platforms to ByteDance Doubao:

1. **Creative Focus**: Emphasize creative and engaging content
2. **Trend Awareness**: Leverage up-to-date knowledge of internet culture
3. **Short-form First**: Optimize for short, punchy content
4. **Gen-Z Language**: Doubao understands youth culture better
5. **Video Scripts**: Excellent for video content creation

### Platform Integration

| Platform | Doubao Strength | Best Prompts |
|----------|-----------------|--------------|
| TikTok | Short video scripts | Trendy, viral content |
| Douyin | E-commerce + entertainment | Product showcases |
| Toutiao | News content | Article generation |
| Xiaohongshu | Lifestyle content | Reviews, recommendations |

## Version History

- 2024-12: Added Doubao Pro and creative templates
- 2024-11: Included short-form video prompts
- 2024-10: Initial Doubao collection released
