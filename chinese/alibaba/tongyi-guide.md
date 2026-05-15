# Tongyi Qianwen Platform Guide

## Table of Contents

1. [Platform Overview](#platform-overview)
2. [API Integration](#api-integration)
3. [Model Selection](#model-selection)
4. [百炼 (Bailian) Platform](#百炼-bailian-platform)
5. [Enterprise Solutions](#enterprise-solutions)
6. [Prompt Optimization](#prompt-optimization)
7. [Cost Management](#cost-management)
8. [Best Practices](#best-practices)

---

## Platform Overview

Tongyi Qianwen (通义千问) is Alibaba Cloud's comprehensive AI platform that provides access to Qwen models through various interfaces, including direct API access, Model Studio, and the new Bailian (百炼) agent platform.

### Platform Components

| Component | Purpose | Access |
|-----------|---------|--------|
| DashScope API | Direct model access | api.dashscope.cn |
| Model Studio | Development environment | modelscope.cn/studio |
| 百炼 (Bailian) | AI agent platform | bailian.console.aliyun.com |
| ModelScope | Open-source models | modelscope.cn |

### Official Resources

- **Dashboard**: https://dashscope.console.aliyun.com/
- **API Docs**: https://help.aliyun.com/document_detail/2434465.html
- **Pricing**: https://help.aliyun.com/document_detail/2434471.html
- **SDK**: https://help.aliyun.com/document_detail/279819.html

---

## API Integration

### Python SDK Installation

```bash
pip install dashscope>=1.14.0
```

### Basic API Usage

```python
import os
import dashscope
from dashscope import DashScope

# Set API key
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

# Text generation
response = DashScope.call(
    model=DashScope.Models.qwen_max,
    prompt='解释什么是区块链技术',
    max_tokens=1000,
    temperature=0.7,
    top_p=0.8,
    result_format='message'
)

print(response.output.choices[0].message.content)
```

### Chat Completion API

```python
from dashscope import DashScope
from dashscope.alibabacloud_dashvector import Dataset

# Chat completion with messages
messages = [
    {'role': 'system', 'content': '你是一位专业的数据分析师。'},
    {'role': 'user', 'content': '分析一下2024年电商行业的发展趋势'}
]

response = DashScope.call(
    model=DashScope.Models.qwen_plus,
    messages=messages,
    max_tokens=2000,
    temperature=0.5,
    result_format='message'
)

print(response.output.choices[0].message.content)
```

### Streaming Response

```python
from dashscope import DashScope

response = DashScope.call(
    model=DashScope.Models.qwen_turbo,
    prompt='写一篇关于人工智能的短文',
    stream=True,
    result_format='message'
)

for chunk in response:
    if chunk.output and chunk.output.choices:
        print(chunk.output.choices[0].message.content, end='', flush=True)
```

---

## Model Selection

### Model Comparison

| Model | Context | Pricing | Speed | Quality | Use Case |
|-------|---------|---------|-------|---------|----------|
| qwen-max | 128K | $$$$ | Slow | Best | Complex reasoning |
| qwen-max-longcontext | 128K | $$$$ | Slow | Best | Long documents |
| qwen-plus | 32K | $$$ | Medium | High | Production |
| qwen-turbo | 8K | $$ | Fast | Good | Simple tasks |

### Model Selection Guide

```
【Decision Flowchart】

1. What is the maximum context needed?
   │
   ├── < 8K tokens → qwen-turbo (fastest, cheapest)
   │
   ├── 8K - 32K tokens → qwen-plus
   │
   └── > 32K tokens → qwen-max or qwen-max-longcontext

2. What is the task complexity?
   │
   ├── Simple (Q&A, classification) → qwen-turbo
   │
   ├── Medium (writing, analysis) → qwen-plus
   │
   └── Complex (reasoning, creative) → qwen-max

3. What is the quality requirement?
   │
   ├── Best possible → qwen-max
   │
   └── Good enough → qwen-plus

4. Cost consideration?
   │
   ├── Minimize cost → qwen-turbo
   │
   └── Balance cost/quality → qwen-plus
```

### Model-Specific Optimizations

#### qwen-max Optimization

```python
# Best for: Complex reasoning, creative tasks, long context
response = DashScope.call(
    model=DashScope.Models.qwen_max,
    prompt=complex_prompt,
    max_tokens=4000,  # Can go up to 8K tokens output
    temperature=0.6,  # Moderate for creative balance
    top_p=0.85,
    enable_search=False  # Disable for pure generation
)
```

#### qwen-plus Optimization

```python
# Best for: Production applications
response = DashScope.call(
    model=DashScope.Models.qwen_plus,
    prompt=production_prompt,
    max_tokens=2000,
    temperature=0.5,
    top_p=0.9
)
```

#### qwen-turbo Optimization

```python
# Best for: High-volume, simple tasks
response = DashScope.call(
    model=DashScope.Models.qwen_turbo,
    prompt=simple_prompt,
    max_tokens=1000,
    temperature=0.3,  # Lower for more deterministic
    top_p=0.95
)
```

---

## 百炼 (Bailian) Platform

### Platform Features

The Bailian (百炼) platform is Alibaba's next-generation AI agent platform that enables:

- **Visual Workflow Builder**: Drag-and-drop agent creation
- **Pre-built Templates**: Ready-to-use agent templates
- **Tool Integration**: Connect to enterprise systems
- **Knowledge Bases**: RAG implementation
- **Multi-modal Support**: Vision, audio, document understanding

### Getting Started with Bailian

```markdown
1. Access: https://bailian.console.aliyun.com/
2. Create workspace
3. Choose template or start from scratch
4. Configure tools and knowledge base
5. Test agent
6. Deploy
```

### Agent Configuration

```python
# Bailian API integration
import aliyun.bailian as bailian

# Initialize client
client = bailian.Client(
    api_key=os.getenv('BAILIAN_API_KEY'),
    workspace_id='your-workspace-id'
)

# Create agent task
task = client.create_task(
    agent_id='your-agent-id',
    input={
        'user_query': '用户的问题',
        'session_id': 'session-123',
        'context': {}
    }
)

# Get result
result = client.get_result(task_id=task.id)
```

### Pre-built Agent Templates

| Template | Use Case | Customization |
|----------|----------|---------------|
| Customer Service | FAQ, order support | Add knowledge base |
| Sales Assistant | Product recommendations | Configure products |
| HR Assistant | Policy Q&A, onboarding | Add company policies |
| Code Copilot | Code review, generation | Select languages |
| Document Analyst | Contract review, summarization | Define criteria |

---

## Enterprise Solutions

### Private Model Deployment

```markdown
【Enterprise Options】

1. **Qwen on PAI (Platform for AI)**
   - Alibaba Cloud's ML platform
   - Fully managed inference
   - VPC isolation
   - SLA guarantees

2. **Qwen on ECS**
   - Self-managed deployment
   - More control
   - Higher maintenance

3. **Qwen on ACK (Container)**
   - Kubernetes-based
   - Scalable
   - Hybrid deployment
```

### Enterprise Security

```python
# VPC endpoint configuration
response = DashScope.call(
    model=DashScope.Models.qwen_plus,
    prompt='处理敏感业务数据',
    api_base='https://dashscope-vpc.aliyuncs.com',  # VPC endpoint
    # Other parameters...
)
```

### SSO Integration

```markdown
【Enterprise SSO Setup】

1. Configure SAML/OIDC in Alibaba Cloud RAM
2. Set up identity provider (IdP)
3. Configure trust relationship
4. Assign permissions to users/groups
5. Enable SSO login for Bailian

Supported IdPs:
- Alibaba Cloud RAM
- DingTalk
- Enterprise AD (via AD FS)
```

---

## Prompt Optimization

### Token Optimization

```python
# Calculate approximate token count
def estimate_tokens(text):
    # Rough estimate: 1 token ≈ 1.5-2 Chinese characters
    # or 4 English characters
    chinese_chars = len([c for c in text if '\u4e00' <= c <= '\u9fff'])
    other_chars = len(text) - chinese_chars
    return int(chinese_chars / 1.5 + other_chars / 4)

# Optimize prompt length
def optimize_prompt(prompt, max_tokens=32000, reserved=2000):
    estimated = estimate_tokens(prompt)
    available = max_tokens - reserved
    
    if estimated > available:
        # Truncate or summarize
        return summarize_prompt(prompt, available)
    return prompt
```

### Temperature Guidelines

| Task Type | Temperature | Top P | Use Case |
|-----------|-------------|-------|----------|
| Code Generation | 0.2 - 0.4 | 0.8 | Deterministic code |
| Fact Extraction | 0.1 - 0.3 | 0.8 | Accurate facts |
| Content Writing | 0.6 - 0.8 | 0.9 | Balanced creative |
| Brainstorming | 0.8 - 1.0 | 0.95 | Creative diversity |
| Translation | 0.3 - 0.5 | 0.9 | Accurate translation |

### Prompt Templates for API

#### Structured Output

```python
def structured_completion(prompt, schema):
    """
    Generate structured output matching schema
    """
    system_prompt = f"""你是一个JSON生成器。
    
输出格式要求：
- 只输出JSON，不要其他内容
- 严格遵循以下schema：
{json.dumps(schema, indent=2, ensure_ascii=False)}

重要：
- 不要添加注释
- 不要省略任何必填字段
- 使用正确的JSON格式
"""
    
    response = DashScope.call(
        model=DashScope.Models.qwen_plus,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=2000,
        temperature=0.1,
        result_format='message'
    )
    
    return json.loads(response.output.choices[0].message.content)
```

#### Chain of Thought

```python
COT_PROMPT = """请按以下步骤分析问题：

【第一步：理解】
明确问题的核心和关键要素

【第二步：分析】
列出分析思路和依据

【第三步：解答】
给出具体答案

【第四步：验证】
检查答案的正确性

【问题】
{user_question}

请详细展示思考过程。
"""

def cot_completion(question):
    response = DashScope.call(
        model=DashScope.Models.qwen_plus,
        prompt=COT_PROMPT.format(user_question=question),
        max_tokens=2000,
        temperature=0.3
    )
    return response.output.choices[0].message.content
```

---

## Cost Management

### Cost Optimization Strategies

```markdown
【Cost Optimization Checklist】

□ Use smallest model that meets requirements
□ Implement response caching
□ Use batch processing for multiple requests
□ Optimize prompt length (remove redundancy)
□ Set appropriate max_tokens limits
□ Monitor usage patterns
□ Set budget alerts
□ Use reserved capacity for predictable usage
```

### Caching Implementation

```python
import redis
import hashlib
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cached_completion(prompt, model='qwen-turbo', ttl=3600):
    """Cache prompt completions to reduce API costs"""
    
    cache_key = hashlib.sha256(
        f"{model}:{prompt}".encode()
    ).hexdigest()
    
    # Check cache
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)
    
    # Call API
    response = DashScope.call(
        model=model,
        prompt=prompt,
        max_tokens=1000
    )
    
    result = response.output.choices[0].message.content
    
    # Store in cache
    redis_client.setex(cache_key, ttl, json.dumps(result))
    
    return result
```

### Batch Processing

```python
from concurrent.futures import ThreadPoolExecutor
import time

def batch_completion(prompts, model='qwen-turbo', max_workers=5):
    """Process multiple prompts efficiently"""
    
    results = []
    
    def process_prompt(prompt):
        try:
            response = DashScope.call(
                model=model,
                prompt=prompt,
                max_tokens=500
            )
            return response.output.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_prompt, p) for p in prompts]
        
        for future in futures:
            results.append(future.result())
    
    return results
```

---

## Best Practices

### Development Workflow

```
【Recommended Workflow】

1. Development
   ├── Start with qwen-turbo (fast iteration)
   ├── Use simple prompts first
   └── Log all inputs/outputs

2. Testing
   ├── Test with diverse inputs
   ├── Verify edge cases
   └── Compare model outputs

3. Production
   ├── Select appropriate model tier
   ├── Implement caching
   ├── Add error handling
   └── Set up monitoring

4. Optimization
   ├── Analyze cost patterns
   ├── Optimize prompts
   └── Consider fine-tuning
```

### Error Handling

```python
from dashscope import Callbacks, DashScope
from dashscope.common.error import APIError, RequestInvalidError

def robust_completion(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = DashScope.call(
                model=DashScope.Models.qwen_plus,
                prompt=prompt,
                max_tokens=1000
            )
            
            if response.status_code != 200:
                raise APIError(f"API error: {response.code}")
            
            return response.output.choices[0].message.content
            
        except (APIError, RequestInvalidError) as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)  # Exponential backoff
```

### Monitoring Setup

```python
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def monitored_completion(prompt, model):
    start_time = datetime.now()
    
    try:
        logging.info(f"[{start_time}] Starting: {model}")
        logging.info(f"Prompt length: {len(prompt)} chars")
        
        response = DashScope.call(model=model, prompt=prompt)
        
        duration = (datetime.now() - start_time).total_seconds()
        output_length = len(response.output.choices[0].message.content)
        
        logging.info(f"Completed in {duration}s, output: {output_length} chars")
        
        return response.output.choices[0].message.content
        
    except Exception as e:
        logging.error(f"Failed: {str(e)}")
        raise
```

---

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Rate limit (429) | Too many requests | Implement backoff, use queue |
| Timeout | Large context/slow model | Reduce context, use faster model |
| Invalid format | JSON/parameter error | Check API docs |
| Authentication | Invalid API key | Verify key in console |
| Model unavailable | Service issue | Check status page |

### Error Code Reference

```python
ERROR_CODES = {
    'InvalidParameter': 'Check parameter values and types',
    'MissingParameter': 'Required parameter not provided',
    'AuthenticationError': 'Verify API key validity',
    'QuotaExceeded': 'Check usage limits, consider upgrade',
    'RateLimitExceeded': 'Implement request throttling',
    'InternalError': 'Retry after delay, contact support',
    'ModelNotAvailable': 'Model may be deprecated, check docs'
}
```

---

## Resources

- **API Documentation**: https://help.aliyun.com/document_detail/2434465.html
- **SDK Reference**: https://help.aliyun.com/document_detail/279819.html
- **Model Scope**: https://modelscope.cn/
- **Pricing Calculator**: https://help.aliyun.com/document_detail/2434471.html
- **Status Page**: https://status.log.aliyun.com/

## Version History

- 2024-12: Added Bailian platform guide
- 2024-11: Updated API parameters and examples
- 2024-10: Initial comprehensive guide
