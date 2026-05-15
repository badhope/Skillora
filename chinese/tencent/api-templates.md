# Tencent Hunyuan API Templates

## Table of Contents

1. [API Overview](#api-overview)
2. [Authentication](#authentication)
3. [Text Completion API](#text-completion-api)
4. [Chat API](#chat-api)
5. [Embedding API](#embedding-api)
6. [Vision API](#vision-api)
7. [Code Generation API](#code-generation-api)
8. [Enterprise Integration](#enterprise-integration)
9. [Error Handling](#error-handling)
10. [Performance Optimization](#performance-optimization)

---

## API Overview

### Available Endpoints

| API | Endpoint | Description | Model |
|-----|----------|-------------|-------|
| Chat | `hunyuanapi.tencentcloudapi.com` | Conversational AI | Hunyuan series |
| Completion | `hunyuanapi.tencentcloudapi.com` | Text completion | Hunyuan series |
| Embedding | `hunyuanapi.tencentcloudapi.com` | Text vectorization | Embedding model |
| Vision | `hunyuanapi.tencentcloudapi.com` | Image understanding | Hunyuan-Vision |

### SDK Installation

```bash
# Python SDK
pip install tencentcloud-sdk-python

# Node.js SDK
npm install tencentcloud-sdk-nodejs

# Java SDK
<dependency>
    <groupId>com.tencentcloudapi</groupId>
    <artifactId>tencentcloud-sdk-java</artifactId>
</dependency>
```

---

## Authentication

### Credential Setup

```python
from tencentcloud.common import credential
from tencentcloud.common.profile import client_profile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

# Method 1: Secret ID and Secret Key
cred = credential.Credential(
    "your-secret-id",      # SecretId
    "your-secret-key"      # SecretKey
)

# Method 2: From environment variables
# Set environment variables:
# TENCENTCLOUD_SECRET_ID
# TENCENTCLOUD_SECRET_KEY
cred = credential.Credential()
```

### Client Initialization

```python
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models

client_profile_obj = client_profile.ClientProfile()
client_profile_obj.httpProfile = http_profile.HttpProfile()
client_profile_obj.httpProfile.endpoint = "hunyuanapi.tencentcloudapi.com"
client_profile_obj.signMethod = "TC3-HMAC-SHA256"

client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou", client_profile_obj)
```

---

## Text Completion API

### Basic Text Completion

```python
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models

def basic_completion(prompt, model="hunyuan-standard"):
    req = models.ChatStdRequest()
    req.Query = prompt
    
    # Model configuration
    req.Model = model
    req.Temperature = 0.7
    req.TopP = 0.8
    req.MaxTokens = 1000
    
    # Make API call
    try:
        resp = client.ChatStd(req)
        return resp
    except TencentCloudSDKException as err:
        print(f"API Error: {err}")
        return None

# Usage
result = basic_completion("用中文解释量子计算的基本原理")
print(result.Response.Choice.Message.Content)
```

### Streaming Completion

```python
import json

def streaming_completion(prompt):
    req = models.ChatStdRequest()
    req.Query = prompt
    req.Stream = True
    
    handler = req.Stream  # Get handler
    
    try:
        resp = client.ChatStd(req)
        
        # Process stream chunks
        for chunk in resp:
            if hasattr(chunk, 'Choices') and chunk.Choices:
                delta = chunk.Choices[0].Delta.Content
                print(delta, end='', flush=True)
    except TencentCloudSDKException as err:
        print(f"Error: {err}")

# Usage
streaming_completion("写一首关于春天的诗")
```

### Advanced Completion with System Prompt

```python
def completion_with_context(system_prompt, user_prompt, model="hunyuan-pro"):
    req = models.ChatStdRequest()
    
    # Build messages array
    messages = [
        {"Role": "system", "Content": system_prompt},
        {"Role": "user", "Content": user_prompt}
    ]
    
    req.Messages = messages
    req.Model = model
    req.Temperature = 0.5
    req.TopP = 0.8
    req.MaxTokens = 2000
    
    try:
        resp = client.ChatStd(req)
        return resp.Response.Choice.Message.Content
    except TencentCloudSDKException as err:
        print(f"Error: {err}")
        return None

# Usage
system = """你是一位专业的数据分析师。
- 使用简洁专业的语言
- 适当使用数据可视化建议
- 给出可执行的建议"""

user = "分析一下2024年电商行业的发展趋势"

result = completion_with_context(system, user)
print(result)
```

---

## Chat API

### Multi-turn Conversation

```python
def multi_turn_chat(messages, model="hunyuan-pro"):
    """
    messages format: [
        {"Role": "system", "Content": "..."},
        {"Role": "user", "Content": "..."},
        {"Role": "assistant", "Content": "..."},
        ...
    ]
    """
    req = models.ChatStdRequest()
    req.Messages = messages
    req.Model = model
    req.Temperature = 0.7
    
    try:
        resp = client.ChatStd(req)
        return resp.Response.Choice.Message
    except TencentCloudSDKException as err:
        print(f"Error: {err}")
        return None

# Usage
messages = [
    {"Role": "system", "Content": "你是一位微信运营专家"},
    {"Role": "user", "Content": "如何提高公众号文章的打开率？"},
    {"Role": "assistant", "Content": "提高打开率的关键在于..."},
    {"Role": "user", "Content": "那具体应该怎么写标题？"}
]

response = multi_turn_chat(messages)
print(response.Content)
```

### Chat with Function Calling

```python
def chat_with_functions(prompt, tools):
    """
    tools: list of function definitions
    """
    req = models.ChatStdRequest()
    req.Query = prompt
    req.Tools = tools
    
    try:
        resp = client.ChatStd(req)
        return resp
    except TencentCloudSDKException as err:
        print(f"Error: {err}")
        return None

# Define tools
tools = [
    {
        "Type": "function",
        "Function": {
            "Name": "get_weather",
            "Description": "获取城市天气信息",
            "Parameters": {
                "Type": "object",
                "Properties": {
                    "city": {
                        "Type": "string",
                        "Description": "城市名称，用中文"
                    }
                },
                "Required": ["city"]
            }
        }
    }
]

# Usage
response = chat_with_functions("北京今天天气怎么样？", tools)
```

### Conversation Manager Class

```python
class HunyuanConversation:
    def __init__(self, client, model="hunyuan-pro"):
        self.client = client
        self.model = model
        self.messages = []
    
    def add_system(self, content):
        self.messages.append({"Role": "system", "Content": content})
    
    def add_user(self, content):
        self.messages.append({"Role": "user", "Content": content})
    
    def add_assistant(self, content):
        self.messages.append({"Role": "assistant", "Content": content})
    
    def send(self, temperature=0.7):
        req = models.ChatStdRequest()
        req.Messages = self.messages
        req.Model = self.model
        req.Temperature = temperature
        
        try:
            resp = self.client.ChatStd(req)
            assistant_msg = resp.Response.Choice.Message
            self.add_assistant(assistant_msg.Content)
            return assistant_msg.Content
        except TencentCloudSDKException as err:
            print(f"Error: {err}")
            return None
    
    def reset(self):
        self.messages = []
    
    def get_history(self):
        return self.messages.copy()

# Usage
conv = HunyuanConversation(client, "hunyuan-pro")
conv.add_system("你是一位专业的营养师")
conv.add_user("请推荐一周的健康食谱")
response = conv.send()
print(response)
conv.add_user("早餐有什么建议？")
response = conv.send()
```

---

## Embedding API

### Generate Embeddings

```python
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models

def generate_embeddings(texts, dimension=1536):
    """
    Generate embeddings for a list of texts
    """
    req = models.EmbeddingsRequest()
    
    # Handle both single text and list
    if isinstance(texts, str):
        texts = [texts]
    
    req.Input = texts
    
    try:
        resp = client.Embeddings(req)
        return resp.Data
    except TencentCloudSDKException as err:
        print(f"Error: {err}")
        return None

# Usage - Single text
embedding = generate_embeddings("人工智能是未来的关键技术")
print(f"Dimension: {len(embedding[0].Embedding)}")

# Usage - Multiple texts
texts = [
    "机器学习是人工智能的子领域",
    "深度学习是机器学习的一种方法",
    "自然语言处理用于文本分析"
]
embeddings = generate_embeddings(texts)
```

### Semantic Search Implementation

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def semantic_search(query, documents, top_k=3):
    """
    Simple semantic search using embeddings
    """
    # Get embeddings
    query_embedding = generate_embeddings(query)[0].Embedding
    doc_embeddings = generate_embeddings(documents)
    
    # Calculate similarities
    similarities = []
    for doc_emb in doc_embeddings:
        sim = cosine_similarity(
            [query_embedding],
            [doc_emb.Embedding]
        )[0][0]
        similarities.append(sim)
    
    # Get top-k results
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = []
    for idx in top_indices:
        results.append({
            "document": documents[idx],
            "score": float(similarities[idx]),
            "index": int(idx)
        })
    
    return results

# Usage
documents = [
    "人工智能技术正在改变各行各业",
    "量子计算是一种新兴的计算范式",
    "机器学习算法可以从数据中学习",
    "区块链技术用于去中心化应用"
]

results = semantic_search("什么是机器学习", documents)
for r in results:
    print(f"[{r['score']:.4f}] {r['document']}")
```

---

## Vision API

### Image Understanding

```python
def analyze_image(image_url, prompt="描述这张图片"):
    """
    Analyze image content
    image_url: Can be URL or base64 encoded image
    """
    req = models.ChatVisionRequest()
    req.Model = "hunyuan-vision"
    req.Input = image_url
    req.Query = prompt
    
    try:
        resp = client.ChatVision(req)
        return resp.Response.Choice.Message.Content
    except TencentCloudSDKException as err:
        print(f"Error: {err}")
        return None

# Usage - Image from URL
result = analyze_image(
    "https://example.com/image.jpg",
    "详细描述这张图片的内容"
)
print(result)

# Usage - Image from file
import base64

with open("image.jpg", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode()

result = analyze_image(
    f"data:image/jpeg;base64,{image_base64}",
    "提取图片中的文字内容"
)
```

### Document OCR with Analysis

```python
def extract_and_analyze_document(image_path, doc_type="general"):
    """
    Extract text and analyze document
    """
    with open(image_path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode()
    
    req = models.ChatVisionRequest()
    req.Model = "hunyuan-vision"
    req.Input = f"data:image/jpeg;base64,{image_base64}"
    req.Query = f"""这是一个{doc_type}类型的文档。
请完成以下任务：
1. 提取所有文字内容
2. 识别文档结构
3. 提取关键信息（如金额、日期、姓名等）
4. 检查信息完整性

请用结构化格式输出结果。"""
    
    try:
        resp = client.ChatVision(req)
        return resp.Response.Choice.Message.Content
    except TencentCloudSDKException as err:
        print(f"Error: {err}")
        return None

# Usage
result = extract_and_analyze_document("invoice.jpg", "发票")
```

---

## Code Generation API

### Using Hunyuan-Code

```python
def code_generation(task, language="Python", framework=None):
    """
    Generate code using Hunyuan-Code
    """
    prompt = f"""【任务】
{task}

【编程语言】
{language}
{f'【框架/库】\n{framework}' if framework else ''}

【要求】
1. 代码完整可运行
2. 包含必要的注释
3. 错误处理完善
4. 遵循最佳实践
5. 提供使用示例

请提供代码实现。
"""
    
    req = models.ChatStdRequest()
    req.Model = "hunyuan-code"
    req.Query = prompt
    req.Temperature = 0.3  # Lower for code accuracy
    
    try:
        resp = client.ChatStd(req)
        return resp.Response.Choice.Message.Content
    except TencentCloudSDKException as err:
        print(f"Error: {err}")
        return None

# Usage
code = code_generation(
    "实现一个简单的HTTP服务器，处理GET请求",
    language="Python"
)
print(code)
```

### Code Review

```python
def review_code(code, language="Python"):
    """
    Review code and provide suggestions
    """
    prompt = f"""请审查以下{language}代码：

```{language}
{code}
```

【审查维度】
1. 代码正确性
2. 性能优化
3. 安全漏洞
4. 代码风格
5. 最佳实践

【输出格式】
使用以下结构：
## 问题列表（按严重程度）
## 代码亮点
## 改进建议
## 优化后的代码（如需要）
"""
    
    req = models.ChatStdRequest()
    req.Model = "hunyuan-code"
    req.Query = prompt
    req.Temperature = 0.3
    
    try:
        resp = client.ChatStd(req)
        return resp.Response.Choice.Message.Content
    except TencentCloudSDKException as err:
        print(f"Error: {err}")
        return None
```

---

## Enterprise Integration

### WeChat Mini Program Integration

```python
# Backend API (Node.js/Express)
const express = require('express');
const tencentcloud = require('tencentcloud-sdk-nodejs');

const HunyuanClient = tencentcloud.hunyuan.v20230901.Client;

const app = express();
app.use(express.json());

// Initialize Hunyuan client
const hunyuanClient = new HunyuanClient({
    credential: {
        secretId: process.env.TENCENT_SECRET_ID,
        secretKey: process.env.TENCENT_SECRET_KEY
    },
    region: 'ap-guangzhou'
});

app.post('/api/chat', async (req, res) => {
    try {
        const { message, sessionId } = req.body;
        
        // Retrieve conversation history from database
        const history = await getConversationHistory(sessionId);
        
        // Build messages
        const messages = [
            { Role: 'system', Content: '你是小程序智能助手' },
            ...history,
            { Role: 'user', Content: message }
        ];
        
        // Call Hunyuan
        const response = await hunyuanClient.ChatStd({
            Model: 'hunyuan-pro',
            Messages: messages
        });
        
        // Save to history
        await saveToHistory(sessionId, message, response.Response.Choice.Message.Content);
        
        res.json({
            success: true,
            data: {
                reply: response.Response.Choice.Message.Content,
                sessionId: sessionId
            }
        });
    } catch (error) {
        res.status(500).json({
            success: false,
            error: error.message
        });
    }
});
```

### Cloud Functions (SCF) Integration

```python
# Tencent Cloud Function - Python runtime
import json
from tencentcloud.common import credential
from tencentcloud.common.profile import client_profile
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models

def main_handler(event, context):
    # Get credentials from environment
    cred = credential.Credential(
        context.credentials.secretId,
        context.credentials.secretKey
    )
    
    client_profile_obj = client_profile.ClientProfile()
    client_profile_obj.httpProfile = client_profile.HttpProfile()
    client_profile_obj.httpProfile.endpoint = "hunyuanapi.tencentcloudapi.com"
    
    client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou", client_profile_obj)
    
    # Parse request
    body = json.loads(event.body) if event.body else {}
    query = body.get('query', '')
    
    # Call Hunyuan
    req = models.ChatStdRequest()
    req.Query = query
    req.Model = "hunyuan-standard"
    
    try:
        resp = client.ChatStd(req)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'result': resp.Response.Choice.Message.Content
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
```

### Integration with Tencent Cloud Database

```python
# Integration with TencentDB
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models
from tencentcloud.sqlserver.v20180328 import sqlserver_client

class ConversationDBManager:
    def __init__(self, db_client, hunyuan_client):
        self.db = db_client
        self.hunyuan = hunyuan_client
    
    def save_conversation(self, session_id, role, content):
        """Save message to database"""
        query = """
        INSERT INTO conversations (session_id, role, content, created_at)
        VALUES (?, ?, ?, GETDATE())
        """
        # Execute query with db_client
    
    def get_conversation_history(self, session_id, limit=10):
        """Retrieve recent conversation history"""
        query = f"""
        SELECT TOP {limit} role, content
        FROM conversations
        WHERE session_id = ?
        ORDER BY created_at ASC
        """
        # Execute and return
    
    def chat_with_history(self, session_id, new_message):
        """Chat with conversation history"""
        history = self.get_conversation_history(session_id)
        
        messages = [
            {"Role": "system", "Content": "你是智能助手"}
        ] + history + [
            {"Role": "user", "Content": new_message}
        ]
        
        req = models.ChatStdRequest()
        req.Messages = messages
        req.Model = "hunyuan-pro"
        
        resp = self.hunyuan.ChatStd(req)
        response_content = resp.Response.Choice.Message.Content
        
        # Save both messages
        self.save_conversation(session_id, "user", new_message)
        self.save_conversation(session_id, "assistant", response_content)
        
        return response_content
```

---

## Error Handling

### Error Code Reference

```python
ERROR_CODES = {
    'InvalidParameter': {
        'message': 'Parameter validation failed',
        'action': 'Check parameter format and types'
    },
    'InvalidCredential': {
        'message': 'Authentication failed',
        'action': 'Verify SecretId and SecretKey'
    },
    'ResourceUnavailable': {
        'message': 'Service temporarily unavailable',
        'action': 'Retry after a delay'
    },
    'RequestLimitExceeded': {
        'message': 'Rate limit exceeded',
        'action': 'Implement exponential backoff'
    },
    'UnsupportedRegion': {
        'message': 'Region not supported',
        'action': 'Use supported region: ap-guangzhou'
    },
    'InternalError': {
        'message': 'Internal server error',
        'action': 'Retry or contact support'
    }
}

def handle_api_error(error):
    """Comprehensive error handling"""
    error_code = error.code if hasattr(error, 'code') else 'Unknown'
    
    if error_code in ERROR_CODES:
        info = ERROR_CODES[error_code]
        print(f"Error: {info['message']}")
        print(f"Action: {info['action']}")
    else:
        print(f"Unexpected error: {error}")
    
    return error_code
```

### Retry Implementation

```python
import time
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

def retry_with_backoff(func, max_retries=3, base_delay=1):
    """
    Retry function with exponential backoff
    """
    for attempt in range(max_retries):
        try:
            return func()
        except TencentCloudSDKException as e:
            if attempt == max_retries - 1:
                raise
            
            # Check if retryable
            if e.code in ['InternalError', 'ResourceUnavailable']:
                delay = base_delay * (2 ** attempt)
                print(f"Retry {attempt + 1}/{max_retries} after {delay}s")
                time.sleep(delay)
            else:
                raise

# Usage
result = retry_with_backoff(lambda: client.ChatStd(req))
```

---

## Performance Optimization

### Response Caching

```python
import hashlib
import redis
import json

class HunyuanCache:
    def __init__(self, redis_client):
        self.redis = redis_client
        self.default_ttl = 3600  # 1 hour
    
    def _make_key(self, prompt, model, temperature):
        content = f"{model}:{temperature}:{prompt}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def get_cached(self, prompt, model, temperature):
        key = self._make_key(prompt, model, temperature)
        cached = self.redis.get(key)
        return json.loads(cached) if cached else None
    
    def set_cached(self, prompt, model, temperature, response, ttl=None):
        key = self._make_key(prompt, model, temperature)
        self.redis.setex(key, ttl or self.default_ttl, json.dumps(response))
    
    def cached_completion(self, prompt, model="hunyuan-standard", temperature=0.7):
        # Check cache
        cached = self.get_cached(prompt, model, temperature)
        if cached:
            return cached
        
        # Call API
        req = models.ChatStdRequest()
        req.Query = prompt
        req.Model = model
        req.Temperature = temperature
        
        resp = client.ChatStd(req)
        response = resp.Response.Choice.Message.Content
        
        # Cache result
        self.set_cached(prompt, model, temperature, response)
        
        return response
```

### Batch Processing

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def batch_completion(prompts, model="hunyuan-standard", max_workers=5):
    """
    Process multiple prompts concurrently
    """
    results = []
    
    def process_single(index, prompt):
        req = models.ChatStdRequest()
        req.Query = prompt
        req.Model = model
        req.Temperature = 0.7
        
        try:
            resp = client.ChatStd(req)
            return index, resp.Response.Choice.Message.Content, None
        except Exception as e:
            return index, None, str(e)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(process_single, i, p): i 
            for i, p in enumerate(prompts)
        }
        
        results = [None] * len(prompts)
        
        for future in as_completed(futures):
            index, content, error = future.result()
            if error:
                print(f"Task {index} failed: {error}")
            results[index] = content
    
    return results

# Usage
prompts = [
    "解释什么是人工智能",
    "分析2024年经济趋势",
    "推荐一本好书"
]

results = batch_completion(prompts, max_workers=3)
```

---

## Resources

- **API Documentation**: https://cloud.tencent.com/document/product/2710
- **SDK Downloads**: https://github.com/TencentCloud/tencentcloud-sdk-python
- **Pricing**: https://cloud.tencent.com/document/product/2710/pricing
- **Status Page**: https://status.cloud.tencent.com/

## Version History

- 2024-12: Added vision and code APIs
- 2024-11: Included enterprise integrations
- 2024-10: Initial API templates released
