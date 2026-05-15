# Wenxin Qianfan Platform Guide

## Table of Contents

1. [Platform Overview](#platform-overview)
2. [Getting Started](#getting-started)
3. [API Integration](#api-integration)
4. [Model Selection Guide](#model-selection-guide)
5. [Fine-tuning Best Practices](#fine-tuning-best-practices)
6. [Enterprise Use Cases](#enterprise-use-cases)
7. [Prompt Engineering for Qianfan](#prompt-engineering-for-qianfan)
8. [Security and Compliance](#security-and-compliance)

---

## Platform Overview

Wenxin Qianfan (文心千帆) is Baidu's enterprise-level AI development platform that provides access to ERNIE models through APIs, with additional features for custom model training and deployment.

### Key Features

| Feature | Description |
|---------|-------------|
| Model-as-a-Service | Pre-trained ERNIE models via API |
| Fine-tuning | Custom model training with proprietary data |
| Prompt Engineering | Visual prompt studio for non-coders |
| Embedding | Text embedding and similarity search |
| RAG Framework | Retrieval-augmented generation support |

### Platform URL

- **Console**: https://console.bce.baidu.com/qianfan
- **API Documentation**: https://cloud.baidu.com/doc/WENXINWORKSHOP/
- **Pricing**: https://cloud.baidu.com/doc/WENXINWORKSHOP/s/zQn2krabb

---

## Getting Started

### Account Setup

```markdown
1. Register Baidu Cloud account at https://login.bce.baidu.com/
2. Complete enterprise verification (required for API access)
3. Navigate to Wenxin Qianfan console
4. Create an application to get API credentials
5. Generate Access Key and Secret Key
```

### Prerequisites

```python
# Required Python packages
pip install qianfan>=0.3.0
```

---

## API Integration

### Python SDK Quick Start

```python
import qianfan

# Initialize with credentials
qianfan.Qianfan(
    ak="your-access-key",
    sk="your-secret-key"
)

# Simple chat completion
response = qianfan.ChatCompletion().do(
    model="ernie-4.0-8k",
    messages=[
        {"role": "user", "content": "请解释什么是大语言模型"}
    ]
)

print(response['result'])
```

### Advanced API Configuration

```python
import qianfan

# Configure with advanced parameters
client = qianfan.ChatCompletion(
    model="ernie-4.0-8k",
    temperature=0.7,
    top_p=0.8,
    penalty_score=1.0,
    stream=False
)

# Multi-turn conversation
messages = [
    {"role": "system", "content": "你是一位专业的金融分析师。"},
    {"role": "user", "content": "分析一下2024年中国新能源汽车市场的发展趋势"},
    {"role": "assistant", "content": "根据最新数据..."},
    {"role": "user", "content": "那2025年呢？"}
]

response = client.do(messages=messages)
```

### API Parameters Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| model | string | required | Model name (ernie-4.0-8k, etc.) |
| temperature | float | 0.8 | Creativity level (0.0-1.0) |
| top_p | float | 0.8 | Nucleus sampling threshold |
| penalty_score | float | 1.0 | Repetition penalty (1.0-2.0) |
| stream | bool | false | Enable streaming responses |
| max_tokens | int | 2048 | Maximum response length |

---

## Model Selection Guide

### Available Models

| Model | Context | Best For | Pricing Tier |
|-------|--------|----------|--------------|
| ERNIE-4.0-8K | 8K tokens | Complex reasoning, creative tasks | Premium |
| ERNIE-4.0-4K | 4K tokens | Balanced performance | Standard |
| ERNIE-3.5-8K | 8K tokens | Production applications | Standard |
| ERNIE-3.5-4K | 4K tokens | Fast responses | Economy |
| ERNIE-Lite-8K | 8K tokens | Simple tasks, high volume | Low |
| ERNIE-Speed-8K | 8K tokens | High-speed processing | Low |

### Model Selection Criteria

```
【Decision Framework】

Step 1: Assess Task Complexity
├── Simple Q&A / Classification → ERNIE-Lite
├── Standard content generation → ERNIE-3.5-4K
├── Complex reasoning / Long context → ERNIE-4.0
└── Code generation / Analysis → ERNIE-4.0-8K

Step 2: Check Context Requirements
├── < 2K tokens → Any model
├── 2K - 4K tokens → 4K+ models
└── > 4K tokens → 8K models

Step 3: Consider Latency Needs
├── Real-time chat → ERNIE-Speed / ERNIE-Lite
├── Background processing → ERNIE-3.5 or ERNIE-4.0
└── Batch processing → Choose based on complexity

Step 4: Evaluate Cost Constraints
├── Budget-sensitive → ERNIE-Lite
├── Balanced → ERNIE-3.5
└── Premium quality required → ERNIE-4.0
```

---

## Fine-tuning Best Practices

### When to Fine-tune

```
【Fine-tuning Recommended When】
✓ Need domain-specific terminology expertise
✓ Consistent output format required
✓ Task-specific patterns to learn
✓ Improving cost-efficiency for specific use cases

【Fine-tuning NOT Recommended When】
✗ General-purpose tasks (use base model)
✗ Limited training data available
✗ Rapidly changing requirements
✗ One-off or experimental projects
```

### Fine-tuning Process

```python
# Step 1: Prepare training data
# Format: JSONL with prompt-response pairs
training_data = [
    {
        "prompt": "用户问题: 如何申请营业执照？\n\n回答:",
        "response": "申请营业执照的流程如下..."
    },
    # More training examples...
]

# Step 2: Upload dataset
import qianfan

dataset_id = qianfan.Dataset().create_from_df(
    dataset_type=qianfan.DatasetType.MultiTurn,
    files=["./training_data.jsonl"]
)

# Step 3: Create fine-tuning job
job = qianfan.FineTune().create(
    name="customer-service-v1",
    dataset_id=dataset_id,
    base_model="ernie-3.5-4k",
    train_config={
        "epoch": 10,
        "learning_rate": 2e-5,
        "batch_size": 16
    }
)

# Step 4: Monitor training progress
status = qianfan.FineTune().get(job_id=job["job_id"])

# Step 5: Deploy model
endpoint = qianfan.Model().deploy(
    model_id=job["model_id"],
    name="customer-service-endpoint"
)
```

### Training Data Guidelines

| Guideline | Requirement |
|-----------|-------------|
| Minimum samples | 100 pairs (recommended: 500+) |
| Quality over quantity | Remove noisy, inconsistent data |
| Format consistency | Follow JSONL format strictly |
| Diversity | Cover various scenarios and edge cases |
| Review | Human review of training samples |

---

## Enterprise Use Cases

### Use Case 1: Intelligent Customer Service

```python
# Customer Service Bot Prompt Template
SYSTEM_PROMPT = """你是[公司名称]的智能客服助手。

【能力范围】
- 解答产品相关问题
- 引导用户使用服务
- 处理常见投诉
- 转接人工服务

【禁止行为】
- 不提供虚假信息
- 不承诺未确定的事项
- 不讨论竞品缺点
- 不泄露用户隐私

【回答原则】
1. 先理解问题，再回答
2. 使用简洁易懂的语言
3. 重要信息加粗提示
4. 结尾询问是否还有其他问题
"""

# Implementation
def handle_customer_inquiry(query, user_context=None):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    
    if user_context:
        context = f"\n\n【用户信息】\n{user_context}"
        messages.append({"role": "user", "content": query + context})
    else:
        messages.append({"role": "user", "content": query})
    
    response = qianfan.ChatCompletion().do(
        model="ernie-3.5-8k",
        messages=messages,
        temperature=0.5
    )
    
    return response['result']
```

### Use Case 2: Document Intelligence

```python
# Document Analysis Prompt
DOC_ANALYSIS_PROMPT = """分析以下文档内容，提取关键信息。

【分析要求】
1. 文档类型识别
2. 核心内容摘要（不超过500字）
3. 关键数据提取（表格形式）
4. 重要时间节点
5. 涉及的人物/机构
6. 文档风险等级（高/中/低）

【输出格式】
按要求格式输出，重要信息使用标记。
"""

def analyze_document(doc_content, doc_type="auto"):
    prompt = f"【文档类型】{doc_type}\n\n【文档内容】\n{doc_content}"
    
    response = qianfan.ChatCompletion().do(
        model="ernie-4.0-8k",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    return response['result']
```

### Use Case 3: Code Generation Assistant

```python
# Code Assistant Configuration
CODE_ASSISTANT_PROMPT = """你是一位专业的Python开发工程师。

【编程规范】
- 遵循PEP 8规范
- 使用类型提示(type hints)
- 添加必要的注释
- 包含错误处理

【输出要求】
1. 提供完整可运行的代码
2. 包含使用示例
3. 说明输入输出
4. 列出依赖库
5. 标注注意事项
"""

def generate_code(task_description, language="Python"):
    prompt = f"【编程语言】{language}\n\n【任务描述】\n{task_description}"
    
    response = qianfan.ChatCompletion().do(
        model="ernie-4.0-8k",
        messages=[
            {"role": "system", "content": CODE_ASSISTANT_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    return response['result']
```

---

## Prompt Engineering for Qianfan

### Temperature Guidelines

| Use Case | Recommended Temperature | Rationale |
|----------|-------------------------|-----------|
| Code generation | 0.2 - 0.4 | Need deterministic, correct output |
| Factual Q&A | 0.3 - 0.5 | Balance accuracy and variety |
| Content writing | 0.6 - 0.8 | Creative but focused |
| Brainstorming | 0.8 - 1.0 | Maximize creative diversity |
| Translation | 0.3 - 0.5 | Preserve accuracy |

### Prompt Templates for Qianfan

#### Template: Structured Output

```python
STRUCTURED_OUTPUT_PROMPT = """【任务】
{user_task}

【输出格式要求】
严格按照以下JSON格式输出，不要包含其他内容：
```json
{{
    "result": "主要结果",
    "confidence": 0.95,
    "details": [
        {{"key": "value"}}
    ],
    "metadata": {{
        "processing_time": "快速"
    }}
}}
```

请确保JSON格式正确，可被解析。
"""

def structured_completion(task):
    response = qianfan.ChatCompletion().do(
        model="ernie-3.5-8k",
        messages=[{"role": "user", "content": STRUCTURED_OUTPUT_PROMPT.format(user_task=task)}],
        temperature=0.3,
        response_format="json"  # If supported
    )
    return response['result']
```

#### Template: Chain of Thought

```python
COT_PROMPT_TEMPLATE = """【问题】
{question}

【要求】
请按以下步骤分析，不要直接给出答案：

第1步：理解问题
- 问题的核心是什么？
- 需要用到哪些知识？

第2步：分析思路
- 列出分析步骤
- 说明每步的依据

第3步：执行计算（如涉及）
- 展示计算过程

第4步：验证答案
- 如何确认答案正确？

请详细展示思考过程。
"""
```

---

## Security and Compliance

### Data Handling Guidelines

```
【数据分类 and 处理】

Class A - Never Send to API:
├── Personal identity information (身份证号)
├── Financial account numbers
├── Medical records
└── Passwords and credentials

Class B - Anonymize Before Sending:
├── Names → Replace with [姓名]
├── Company names → Replace with [公司]
├── Locations → General region only
└── Dates → Relative time references

Class C - Can Send with Consent:
├── Business discussions
├── General product feedback
└── Aggregated analytics
```

### Enterprise Security Checklist

```markdown
【Security Checklist】
□ API credentials stored securely (not in code)
□ Enable VPC endpoint for API access
□ Implement request rate limiting
□ Set up usage monitoring and alerts
□ Define data retention policies
□ Configure access permissions (RBAC)
□ Enable audit logging
□ Regular security reviews
```

### Compliance Considerations

| Regulation | Requirement | Implementation |
|------------|-------------|----------------|
| PIPL | Data minimization | Send only necessary data |
| Cybersecurity Law | Data localization | Use CN region endpoints |
| MLPS | Security assessment | Document data flows |
| GDPR (if applicable) | Consent tracking | Implement consent management |

---

## Performance Optimization

### Caching Strategies

```python
import hashlib
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_prompt_hash(prompt):
    return hashlib.md5(prompt.encode()).hexdigest()

def cached_completion(prompt, model="ernie-3.5-4k"):
    cache_key = cached_prompt_hash(prompt)
    
    # Check cache first
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)
    
    # Call API
    response = qianfan.ChatCompletion().do(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Store in cache (with TTL)
    redis_client.setex(cache_key, 3600, json.dumps(response))
    
    return response
```

### Batch Processing

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def batch_completion(prompts, model="ernie-3.5-4k", batch_size=10):
    results = []
    
    for i in range(0, len(prompts), batch_size):
        batch = prompts[i:i + batch_size]
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(
                    qianfan.ChatCompletion().do,
                    model=model,
                    messages=[{"role": "user", "content": p}]
                )
                for p in batch
            ]
            
            batch_results = [f.result()['result'] for f in futures]
            results.extend(batch_results)
    
    return results
```

---

## Troubleshooting

### Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Slow response | High traffic / Large context | Use smaller model or reduce context |
| Inconsistent output | High temperature | Lower temperature to 0.3-0.5 |
| Truncated response | Max tokens limit | Increase max_tokens parameter |
| API errors | Invalid credentials | Verify AK/SK in console |
| Rate limit | Too many requests | Implement exponential backoff |

### Error Code Reference

| Error Code | Description | Action |
|------------|-------------|--------|
| 100 | Invalid parameter | Check parameter values |
| 110 | Authentication failed | Verify credentials |
| 111 | Insufficient quota | Check billing/limits |
| 114 | Request too large | Reduce input size |
| 336001 | Rate limit exceeded | Add delay between requests |
| 336002 | Context length exceeded | Shorten conversation |

---

## Best Practices Summary

1. **Start Simple**: Begin with base models before fine-tuning
2. **Monitor Costs**: Use appropriate model tiers for task complexity
3. **Implement Fallbacks**: Have backup models for critical applications
4. **Cache Common Queries**: Reduce API costs for repeated questions
5. **Log Everything**: Maintain audit trail for debugging and compliance
6. **Test Regularly**: Verify outputs meet quality standards
7. **Stay Updated**: Check for new model versions and features

## Resources

- **Documentation**: https://cloud.baidu.com/doc/WENXINWORKSHOP/
- **API Explorer**: https://console.bce.baidu.com/qianfan/ais/console/onlineTest
- **Pricing Calculator**: https://cloud.baidu.com/doc/WENXINWORKSHOP/s/zQn2krabb
- **Support**: https://console.bce.baidu.com/support/

## Version History

- 2024-12: Added fine-tuning best practices
- 2024-11: Updated API parameters and examples
- 2024-10: Initial comprehensive guide
