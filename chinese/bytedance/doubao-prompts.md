# Doubao Model Prompt Engineering Guide

## Table of Contents

1. [Doubao Model Family](#doubao-model-family)
2. [System Prompt Templates](#system-prompt-templates)
3. [Short-Form Video Content](#short-form-video-content)
4. [Social Media Marketing](#social-media-marketing)
5. [Creative Writing](#creative-writing)
6. [E-commerce Content](#e-commerce-content)
7. [Trend Analysis](#trend-analysis)
8. [API Integration](#api-integration)
9. [Best Practices](#best-practices)

---

## Doubao Model Family

### Available Models

| Model | Context | Strengths | Best For |
|-------|---------|-----------|----------|
| doubao-pro | 32K | Top quality, complex reasoning | Enterprise creative tasks |
| doubao-general | 16K | Balanced performance | General applications |
| doubao-lite | 8K | Fast, cost-effective | High-volume simple tasks |
| doubao-emotion | 16K | Emotional intelligence | Customer interaction |

### Model Selection

```
【Selection Guide】

Creative Content (Scripts, Marketing)
└──→ doubao-pro (best quality)

General Q&A and Tasks
└──→ doubao-general (balanced)

High-Volume Simple Tasks
└──→ doubao-lite (fast, cheap)

Customer Service, Emotional Content
└──→ doubao-emotion (enhanced EQ)
```

---

## System Prompt Templates

### Template: Creative Content Expert

```
【角色】
你是一位顶尖的内容创意专家，精通各类短视频和社交媒体内容的创作。

【核心能力】
- 爆款内容策划
- 短视频脚本撰写
- 社媒文案创作
- 热点借势
- 互动话题设计

【内容风格】
- 年轻化、有活力
- 节奏明快、信息密度高
- 情感共鸣强
- 记忆点突出
- 易于传播分享

【创作原则】
1. 前3秒必须抓住注意力
2. 每句话都有存在的理由
3. 结尾留有互动钩子
4. 符合平台算法偏好
5. 考虑BGM配合

【禁忌】
- 不使用过气梗
- 不用空洞鸡汤
- 不低俗媚俗
- 不触碰敏感话题
```

### Template: Gen-Z Marketing Specialist

```
【角色】
精通Z世代文化的营销专家，深谙年轻人喜好和行为模式。

【文化理解】
- 了解网络流行语和黑话
- 熟悉二次元、游戏、电竞文化
- 理解躺平、摆烂等亚文化
- 掌握饭圈用语

【营销理念】
- 反向营销、整活营销
- 真诚不油腻
- 会玩梗、有态度
- 重视情绪价值
- 小众共鸣优于大众传播

【内容特征】
- 个性化、有态度
- 不说教、真诚沟通
- 幽默感强
- 善于制造话题
- 重视UGC互动

【平台适配】
- 小红书：真实分享种草
- B站：深度内容社区
- 抖音：娱乐碎片化
- 微博：热点话题引爆
```

### Template: E-commerce Copywriter

```
【角色】
电商内容创作专家，擅长直播带货、产品种草、详情页文案。

【内容类型】
- 直播话术
- 产品种草文
- 详情页文案
- 短视频带货脚本
- 买家秀文案

【创作技巧】
1. 痛点共鸣开场
2. 产品卖点可视化
3. 社会认同制造
4. 限时紧迫感
5. 行动指令清晰

【平台特性】
- 抖音：娱乐化种草
- 快手：老铁文化、真诚感
- 淘宝：专业种草
- 小红书：真实体验分享

【数据敏感】
- 点击率优化
- 转化率优化
- 停留时长优化
- 互动率优化
```

### Template: Entertainment Content Creator

```
【角色】
泛娱乐内容策划专家，专注于综艺、明星、游戏、电竞领域。

【内容领域】
- 娱乐热点追踪
- 明星话题策划
- 游戏攻略/前瞻
- 电竞赛事解说
- 二次元内容

【创作特点】
- 紧随热点、快速产出
- 有态度、有观点
- 粉丝视角、真爱导向
- 适度玩梗、不过度
- 尊重版权、遵守规则

【内容形式】
- 热点快评
- 深度解析
- 对比盘点
- 互动预测
- 二创同人（需授权）
```

---

## Short-Form Video Content

### TikTok/Douyin Video Script

```
【任务】
创作短视频脚本

【基本信息】
- 产品/主题：[名称]
- 视频时长：[X秒]
- 目标效果：[涨粉/带货/传播]
- 目标受众：[人群描述]

【脚本类型】
□ 剧情类
□ 种草类
□ 教程类
□ 搞笑类
□ 情感类
□ 知识类
□ 挑战类

【创作要求】
1. 前3秒：黄金开场，必须抓眼球
   - 制造悬念
   - 惊人事实
   - 冲突对比
   - 直接展示结果

2. 中间：内容展开，节奏紧凑
   - 每5秒一个小高潮
   - 避免无聊铺垫
   - 信息密度适中

3. 结尾：互动引导，促进分享
   - 提出问题引发评论
   - @相关账号
   - 挑战/模仿邀请
   - 关注引导

【风格】
- [搞笑/感人/震撼/治愈/燃/甜]
- 背景音乐建议：[类型]

【输出格式】
┌────────────────────────────────────────┐
│ ⏱️ 时间轴  │ 📝 内容/画面   │ 🎵 音效   │
├────────────────────────────────────────┤
│ 0-3秒      │              │           │
│ 3-10秒     │              │           │
│ 10-20秒    │              │           │
│ ...        │              │           │
└────────────────────────────────────────┘

[完整台词]
[拍摄建议]
[注意事项]
```

### Trending Format Adaptation

```
【任务】
将以下内容适配为抖音热门格式

【原内容】
{content}

【目标平台】
□ 抖音
□ 快手
□ TikTok
□ Instagram Reels

【选择热门格式】
□ "听劝"类 - 改变/改造型
□ 反转类 - 出人意料的结局
□ "原来如此"类 - 揭秘/科普
□ 共鸣类 - 戳中痛点
□ 炫技类 - 展示技能/才艺
□ 挑战类 - 发起互动
□ 剧情类 - 有故事性

【适配要求】
1. 开头必须强冲击
2. 控制时长节奏
3. 添加热门音效建议
4. 设计互动点
5. 添加字幕规范

请提供适配后的脚本和创作说明。
```

### Product Showcase Script

```
【产品信息】
- 产品名称：[名称]
- 品牌：[品牌]
- 价格：[价格]
- 核心卖点：[卖点1, 卖点2, 卖点3]

【脚本类型】
□ 开箱展示
□ 对比测评
□ 使用教程
□ 效果展示
□ 场景演示

【目标效果】
□ 种草安利
□ 转化带货
□ 品牌曝光

【创作框架】
1. 吸引（0-3秒）
   - [开场钩子]

2. 建立信任（3-15秒）
   - [品牌/产品背书]
   - [第一印象]

3. 核心展示（15-40秒）
   - [卖点1亮点]
   - [卖点2亮点]
   - [卖点3亮点]

4. 转化引导（最后5秒）
   - [价格/优惠信息]
   - [购买引导]

【话术特点】
- 口语化、亲切感
- 适当使用感叹词
- 避免过于推销感
- 强调真实体验

请生成完整带货脚本。
```

### "听劝" Series Script

```
【系列主题】
听劝改造类内容

【人设定位】
- 主角：[人物设定]
- 改造诉求：[诉求描述]

【脚本结构】
1. 求助开场（0-5秒）
   "大家给我看看，我这样行不行？"

2. 展示现状（5-15秒）
   展示当前状态/问题

3. 等待互动（15-30秒）
   "你们觉得哪里需要改？"

4. 采纳建议（30-60秒）
   采纳网友建议，展示变化

5. 感谢收尾（最后5秒）
   "谢谢大家的建议！"

【互动设计】
- 评论区置顶问题
- 设置投票选项
- 回应热门评论

【系列规划】
- 第1期：提出诉求
- 第2-N期：逐步改造
- 完结：最终展示

请设计完整系列内容框架。
```

---

## Social Media Marketing

### Xiaohongshu (Little Red Book) Post

```
【任务】
创作小红书种草笔记

【产品/体验】
[产品名/体验描述]

【目标】
□ 种草安利
□ 真实分享
□ 攻略教程

【内容风格】
□ 精致生活型
□ 真实测评型
□ 搞笑吐槽型
□ 专业分析型

【创作要求】

【标题】
- 字数：15-20字
- 包含关键词
- 制造好奇心
- 突出亮点

【正文结构】
1. 开头：吸引+引入（100字内）
   - 使用场景切入
   - 或直接抛出痛点

2. 主体：真实体验（300-500字）
   - 个人真实感受
   - 细节描写
   - 对比展示（before/after）
   - 优缺点客观分析

3. 结尾：总结+互动（50字内）
   - 简明总结
   - 互动问题

【标签策略】
#标签1 #标签2 #标签3 ...

【图片建议】
- 封面图：[描述]
- 内页图：[描述]

请生成完整笔记。
```

### Weibo Trend Post

```
【任务】
创作微博话题内容

【话题/热点】
{topic}

【内容类型】
□ 热点追评
□ 观点输出
□ 娱乐互动
□ 知识科普

【账号调性】
[官方/个人/IP]

【创作要求】
1. 符合账号人设
2. 符合平台调性
3. 便于互动传播
4. 适当使用emoji
5. 控制字数（长微博/短微博）

【内容结构】
- 观点明确
- 论据有力
- 结尾引导讨论

【互动设计】
- 发起投票
- 提出问题
- @相关账号
- 创建话题

请生成内容并说明发布时机建议。
```

### Community Comment Response

```
【任务】
生成评论回复模板

【平台】
□ 抖音
□ 快手
□ B站
□ 小红书

【评论类型】
□ 提问咨询
□ 正面反馈
□ 负面反馈
□ 争议言论
□ 引流 spam

【回复原则】
1. 真诚友善
2. 简洁有力
3. 符合人设
4. 引导正向互动

【生成内容】
回复话术模板 + 应对策略

请提供具体回复示例。
```

---

## Creative Writing

### Story/Narrative Generator

```
【任务】
创作故事内容

【故事类型】
□ 短篇小说
□ 连载小说
□ 剧本杀剧本
□ 漫画脚本
□ 短视频剧情

【主题】
{theme}

【风格】
□ 甜宠
□ 悬疑
□ 恐怖
□ 搞笑
□ 治愈
□ 热血
□ 虐心

【目标受众】
{audience}

【篇幅】
{length}

【特殊要求】
[any_requirements]

【创作框架】
1. 开头：设置悬念/冲突
2. 发展：推进情节
3. 高潮：矛盾爆发
4. 结尾：解决/留下悬念

【角色设定】
- 主角：[设定]
- 配角：[设定]

请提供故事大纲或完整内容。
```

### Script for Skit/Comedy

```
【任务】
创作搞笑短视频剧本

【场景数量】
{scenes}

【角色】
{characters}

【搞笑风格】
□ 无厘头
□ 反转
□ 讽刺
□ 吐槽
□ 默剧
□ 荒诞

【时长】
{duration}

【核心笑点】
{core_joke}

【创作要求】
1. 铺垫→反转→爆点结构
2. 符合平台用户喜好
3. 注意尺度把控
4. 留有互动空间

请生成完整剧本。
```

### Dialogue Generator

```
【任务】
生成对话内容

【场景】
{scene}

【角色设定】
角色A：[性格、说话风格]
角色B：[性格、说话风格]

【对话风格】
□ 俏皮互怼
□ 甜蜜暧昧
□ 搞笑吐槽
□ 深情告白

【话题】
{topic}

【输出要求】
- 对话自然流畅
- 符合角色设定
- 体现关系发展
- 有记忆点金句

请生成对话内容。
```

---

## E-commerce Content

### Product Review

```
【产品】
{product}

【Review类型】
□ 开箱测评
□ 使用体验
□ 长期追踪
□ 对比测评

【Review风格】
□ 真实客观
□ 强力种草
□ 冷静分析
□ 搞笑吐槽

【内容框架】
1. 开场（建立期待）
   - 入手原因
   - 期待点

2. 外观（视觉展示）
   - 包装
   - 设计
   - 质感

3. 功能（核心展示）
   - 核心卖点实测
   - 对比展示

4. 优缺点（客观评价）
   - 优点总结
   - 缺点坦白

5. 总结（购买建议）
   - 适合人群
   - 购买建议

请生成完整Review。
```

### Live Streaming Script

```
【直播信息】
- 产品：[产品]
- 直播时长：[X分钟]
- 主播风格：[风格]

【脚本结构】

【开场（0-3分钟）】
- 欢迎话术
- 热场互动
- 引入产品

【产品介绍（3-15分钟）】
- 痛点引入
- 产品展示
- 卖点讲解
- 使用演示

【互动环节（15-20分钟）】
- 问答互动
- 抽奖/福利
- 评论回应

【促单环节（20-25分钟）】
- 价格对比
- 限时优惠
- 库存紧迫感
- 购买引导

【结尾（25-30分钟）】
- 感谢话术
- 下场预告
- 粉丝维护

【话术技巧】
- "家人们"拉近距离
- "限时"制造紧迫
- "太划算了"强调价值
- "抢到就是赚到"激励

请生成完整直播话术。
```

### Tmall/JD Product Description

```
【任务】
创作电商平台产品详情页

【产品信息】
- 产品名：[名称]
- 品牌：[品牌]
- 卖点：[卖点列表]

【目标平台】
□ 天猫
□ 京东
□ 拼多多
□ 抖音电商

【页面结构】
1. 主图视频脚本
2. 核心卖点
3. 详情描述
4. 规格参数
5. 买家秀文案
6. FAQ

【SEO要求】
- 关键词：[关键词]
- 搜索热词：[热词]

【合规要求】
- 不夸大宣传
- 不虚假承诺
- 符合广告法

请生成完整详情页内容。
```

---

## Trend Analysis

### Trend Report Generator

```
【任务】
生成[平台]内容趋势报告

【分析范围】
- 平台：[平台]
- 时间范围：[时间段]
- 行业/品类：[品类]

【分析维度】
1. 内容形式趋势
2. 热门话题
3. 高增长赛道
4. 达人动态
5. 品牌案例

【数据来源】
- 话题热度
- 内容播放量
- 互动数据
- 搜索指数

【输出要求】
- 趋势发现
- 数据支撑
- 案例分析
- 建议启示

请生成完整趋势报告。
```

### Hot Topic Analysis

```
【任务】
分析热点话题

【话题】
{topic}

【分析要求】
1. 热度分析
   - 当前热度等级
   - 发展趋势
   - 生命周期判断

2. 用户讨论点
   - 主要讨论角度
   - 情感倾向
   - 热门评论分析

3. 借势建议
   - 内容角度推荐
   - 风险提示
   - 时机把控

4. 案例参考
   - 成功案例
   - 可借鉴点

请提供分析报告。
```

---

## API Integration

### Python SDK Usage

```python
from volcenginesdkarkruntime import Ark

# Initialize client
client = Ark(
    api_key="your-api-key",
    # Optional: specify base URL
    # base_url="https://ark.cn-beijing.volces.com/api/v3"
)

# Simple chat
response = client.chat.completions.create(
    model="doubao-pro",
    messages=[
        {"role": "user", "content": "写一个抖音短视频脚本"}
    ]
)
print(response.choices[0].message.content)

# With system prompt
response = client.chat.completions.create(
    model="doubao-pro",
    messages=[
        {"role": "system", "content": "你是一位专业的短视频创作者"},
        {"role": "user", "content": "写一个关于美食的脚本"}
    ]
)

# Streaming response
stream = client.chat.completions.create(
    model="doubao-pro",
    messages=[
        {"role": "user", "content": "讲一个有趣的故事"}
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='', flush=True)
```

### API Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| model | string | required | Model name (doubao-pro, etc.) |
| messages | array | required | Message history |
| temperature | float | 0.7 | Creativity level (0.0-1.0) |
| top_p | float | 0.9 | Nucleus sampling |
| max_tokens | int | 2000 | Max output tokens |
| stream | bool | false | Enable streaming |
| stop | array | null | Stop sequences |

### Multi-turn Conversation

```python
def multi_turn_conversation(messages, model="doubao-pro"):
    """
    Maintain conversation context
    messages: [
        {"role": "system", "content": "..."},
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."},
        ...
    ]
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7
    )
    
    assistant_message = response.choices[0].message
    messages.append({"role": "assistant", "content": assistant_message.content})
    
    return assistant_message.content, messages

# Usage
messages = [
    {"role": "system", "content": "你是一位短视频创作专家"},
    {"role": "user", "content": "我想做一个美食账号"}
]

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    
    messages.append({"role": "user", "content": user_input})
    response, messages = multi_turn_conversation(messages)
    print(f"Assistant: {response}")
```

---

## Best Practices

### Prompt Optimization Tips

```
【Effective Prompts】

✓ Be specific about format and length
✓ Include target platform
✓ Specify tone and style
✓ Provide examples when possible
✓ Include constraints/requirements

【Avoid】

✗ Vague instructions
✗ Conflicting requirements
✗ Too many constraints
✗ Missing context
✗ Outdated references
```

### Platform-Specific Tips

| Platform | Key Focus | Prompt Tips |
|----------|-----------|-------------|
| 抖音 | Entertainment first | Add BGM suggestions |
| 快手 | Authentic, real | Emphasize真实感 |
| 小红书 | Aspirational lifestyle | Focus on aesthetics |
| B站 | Quality, depth | Allow longer content |
| 微博 | Hot takes | Add opinion angles |

### Temperature Guidelines

| Task | Temperature | Rationale |
|------|-------------|-----------|
| Fact extraction | 0.2 - 0.4 | Accuracy matters |
| News summary | 0.3 - 0.5 | Neutral tone |
| Creative writing | 0.7 - 0.9 | More creative |
| Social content | 0.6 - 0.8 | Engaging |
| Marketing copy | 0.5 - 0.7 | Persuasive but coherent |

## Version History

- 2024-12: Added comprehensive social media templates
- 2024-11: Included e-commerce content prompts
- 2024-10: Core Doubao prompts released
