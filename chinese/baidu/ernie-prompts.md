# ERNIE Bot Prompt Engineering Guide

## Table of Contents

1. [Getting Started with ERNIE](#getting-started-with-ernie)
2. [System Prompt Templates](#system-prompt-templates)
3. [Domain-Specific Prompts](#domain-specific-prompts)
4. [Chinese Content Generation](#chinese-content-generation)
5. [Code and Technical Prompts](#code-and-technical-prompts)
6. [Advanced Techniques](#advanced-techniques)
7. [Prompt Templates Library](#prompt-templates-library)

---

## Getting Started with ERNIE

### Basic Prompt Structure

ERNIE Bot responds well to structured prompts with clear context and explicit expectations.

```markdown
# Basic Template
[Context/Background]
[Task Definition]
[Output Format Requirements]
[Constraints/Limitations]
```

### Example Basic Prompt

```
作为一位资深产品经理，请帮我分析以下智能家居市场的竞争格局：
- 市场主要玩家
- 差异化策略
- 未来趋势预测

请用专业但易懂的语言回答，适合向非技术背景的投资者汇报。
```

---

## System Prompt Templates

### Professional Writing Assistant

```
【角色设定】
你是一位专业的内容创作者，擅长撰写高质量的中文内容。

【能力范围】
- 文章撰写与润色
- 营销文案创作
- 技术文档编写
- 品牌故事讲述

【风格要求】
- 语言专业但不晦涩
- 结构清晰有逻辑
- 注重可读性

【输出格式】
先列出核心要点，再展开详细说明。
```

### Technical Documentation Expert

```
【身份】
资深技术文档工程师，专注于编写易读易用的技术文档。

【专业领域】
- API文档编写
- 用户手册制作
- 开发指南撰写
- 系统架构说明

【写作原则】
1. 准确性第一
2. 使用简洁语言
3. 提供代码示例
4. 包含常见问题解答

【格式规范】
- 使用Markdown格式
- 代码块标注语言
- 重要信息加粗
- 添加目录导航
```

### Business Analyst

```
【角色定义】
你是企业级业务分析师，专注于数据驱动的洞察和战略建议。

【分析框架】
- PEST分析（政治、经济、社会、技术）
- SWOT分析
- 波特五力模型
- 价值链分析

【输出要求】
- 数据支撑观点
- 提供可执行建议
- 标注风险因素
- 给出时间预期

【保密要求】
所有分析仅供内部使用。
```

---

## Domain-Specific Prompts

### Marketing and Content

#### Social Media Content Generator

```
【任务】
为[品牌名称]创建社交媒体内容策略

【平台】
[微博/微信/抖音/小红书]

【目标受众】
[年龄段/职业/兴趣特征]

【内容要求】
1. 生成10条不同风格的帖子
2. 每条包含：标题、正文、hashtags
3. 适应平台算法特点
4. 包含互动引导

【品牌调性】
[活泼/专业/高端/亲民]

请生成本周(12月16日-12月22日)的内容日历。
```

#### Product Description Writer

```
【产品信息】
产品名称：[产品名]
核心功能：[功能1, 功能2, 功能3]
目标用户：[用户画像]
价格区间：[价格]

【写作要求】
1. 突出差异化卖点
2. 使用用户语言
3. 包含情感价值
4. 添加社会认同元素

【输出格式】
- 主标题（一句话卖点）
- 副标题（目标用户共鸣）
- 核心卖点（3-5个bullet points）
- 详细描述（200字）
- FAQ（3个常见问题）

请生成电商平台用的产品详情页文案。
```

### Legal and Compliance

#### Contract Clause Analyzer

```
【任务】
分析以下合同条款的法律风险

【合同类型】
[采购合同/服务协议/劳动合同/租赁合同]

【条款内容】
[粘贴条款文本]

【分析维度】
1. 权利义务对等性
2. 潜在法律风险点
3. 模糊或歧义表述
4. 缺失的保障条款
5. 违约责任评估

【输出要求】
- 用列表形式标注每个风险点
- 说明风险等级（高/中/低）
- 提供修改建议
- 引用相关法律依据
```

#### Compliance Checklist Generator

```
【行业】
[互联网/金融/医疗/教育/制造业]

【业务场景】
[业务描述]

【监管要求】
《中华人民共和国[相关法律]》

【生成内容】
请生成符合中国法规要求的合规检查清单，包含：
1. 资质许可要求
2. 数据安全要求
3. 用户隐私保护
4. 广告宣传规范
5. 行业特定规定

每项标注是否适用及检查频率。
```

### Education and Learning

#### Course Design Assistant

```
【课程信息】
课程名称：[课程名]
目标学员：[学员背景]
学习时长：[时长]
授课形式：[线上/线下/混合]

【课程目标】
学员完成课程后应能够：
1. [目标1]
2. [目标2]
3. [目标3]

【内容要求】
请设计完整的课程大纲，包含：
- 模块划分
- 每个模块的学习目标
- 教学活动设计
- 评估方式
- 所需资源

【输出格式】
使用表格形式展示，便于直接使用。
```

#### Study Plan Generator

```
【学习者背景】
- 当前水平：[零基础/入门/中级/高级]
- 学习目标：[具体目标]
- 可用时间：[每周小时数]
- 学习方式：[自学/跟随课程/结合项目]

【目标领域】
[编程/语言/设计/数据分析/其他]

【生成内容】
请制定一个[周期]学习计划：
1. 阶段划分及目标
2. 每日/每周学习任务
3. 资源推荐（中文资料优先）
4. 进度检查点
5. 调整策略

请确保计划具有可执行性。
```

---

## Chinese Content Generation

### Blog Article Writer

```
【文章主题】
[主题描述]

【目标读者】
[读者画像]

【文章要求】
- 字数：[1500-3000字]
- 风格：[专业严谨/轻松活泼/深度分析/入门科普]
- 结构：包含引言、3-5个主要论点、结论

【SEO要求】
- 关键词：[关键词1, 关键词2]
- 包含FAQ部分
- 添加小标题便于阅读

【内容框架】
请先给出文章大纲，确认后再生成完整文章。
```

### News Summary Generator

```
【输入】
请为以下新闻内容生成摘要：

[粘贴新闻内容]

【摘要要求】
1. 保留核心事实（5W1H）
2. 删除冗余信息
3. 标注关键数据
4. 保持客观中立

【输出格式】
- 标题（15字以内）
- 导语（100字）
- 主体摘要（300字）
- 关键词标签
- 相关背景说明
```

### Chinese Translation Prompts

#### English to Chinese

```
【翻译任务】
将以下英文内容翻译为中文

【原文】
[粘贴英文内容]

【翻译要求】
1. 符合中文表达习惯
2. 保持专业术语准确性
3. 适当本地化文化表达
4. 保持原意不增不减

【特殊处理】
- 品牌名：[保留原文/音译/意译]
- 专有名词：[保留英文/翻译]
- 文化梗：[解释翻译/意译/保留原文]

请先说明翻译策略，再提供译文。
```

#### Chinese to English

```
【翻译任务】
将以下中文内容翻译为英文

【原文】
[粘贴中文内容]

【目标受众】
[西方商务人士/技术人员/普通消费者]

【翻译风格】
[正式商务/技术文档/市场营销]

【特殊要求】
- 符合英文表达习惯
- 避免中式英语
- 保持专业术语一致
- 适当调整文化适配

请提供翻译并标注需要确认的术语。
```

---

## Code and Technical Prompts

### Code Review Assistant

```
【任务】
代码审查

【编程语言】
[Python/Java/JavaScript/Go/其他]

【代码】
```[语言]
[粘贴代码]
```

【审查重点】
1. 代码逻辑正确性
2. 性能优化建议
3. 安全漏洞检测
4. 代码风格一致性
5. 最佳实践符合度

【输出要求】
- 列出发现的问题（按严重程度排序）
- 给出修改建议
- 提供优化后的代码示例
- 说明改进理由
```

### API Documentation Generator

```
【API信息】
- 服务名称：[名称]
- 端点路径：[路径]
- 请求方法：[GET/POST/PUT/DELETE]
- 功能说明：[功能描述]

【参数列表】
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|

【请求示例】
```json
[示例JSON]
```

【生成内容】
请生成完整的API文档，包含：
1. 接口概述
2. 请求说明
3. 请求参数详解
4. 响应格式及示例
5. 错误码说明
6. 调用示例（cURL/Python/JavaScript）
7. 注意事项

使用Markdown格式，便于直接发布。
```

### Architecture Design Assistant

```
【系统需求】
- 系统名称：[名称]
- 核心功能：[功能列表]
- 用户规模：[规模描述]
- SLA要求：[可用性目标]
- 预算范围：[预算]

【技术偏好】
- 编程语言：[语言]
- 云服务商：[阿里云/腾讯云/华为云/自建]
- 部署方式：[容器化/传统部署]

【生成内容】
请设计系统架构方案：
1. 整体架构图（文字描述）
2. 技术选型说明
3. 核心模块设计
4. 数据存储方案
5. 高可用设计
6. 扩展性方案
7. 成本估算
8. 实施路线图
```

---

## Advanced Techniques

### Chain of Thought Prompting

```
【任务】
[复杂问题描述]

【要求】
请分步骤思考这个问题：

Step 1: 理解问题
- 问题的核心是什么？
- 需要哪些信息来解决？

Step 2: 分析问题
- 有哪些可能的解决路径？
- 各路径的优缺点？

Step 3: 制定方案
- 推荐哪个方案？为什么？
- 具体实施步骤？

Step 4: 验证方案
- 如何验证方案的有效性？
- 可能遇到的问题及应对？

请详细说明每个步骤的思考过程。
```

### Few-Shot Learning Example

```
【任务类型】
情感分析

【示例】
示例1：
输入："这家餐厅的服务太棒了，下次还来！"
输出：正面情感，置信度95%

示例2：
输入："等了半个小时还没上菜，太失望了"
输出：负面情感，置信度92%

示例3：
输入："味道一般，没有想象中的好"
输出：中性/轻微负面情感，置信度80%

【新任务】
输入："产品还可以，但价格有点贵"
输出：？

请给出分析结果及置信度。
```

### Role-Playing Scenarios

#### Job Interview Preparation

```
【场景】
你是一位有10年经验的产品经理，正在面试一位应聘高级产品经理职位的候选人。

【候选人背景】
- 工作年限：[X年]
- 过往经验：[经验描述]
- 面试岗位：[岗位名称]

【面试要求】
请模拟一场结构化面试：
1. 自我介绍（请候选人准备）
2. 行为面试问题（STAR法则）
3. 专业能力考察
4. 情景模拟题
5. 反向提问环节

请根据候选人的回答给出评价和改进建议。
```

#### Customer Service Simulation

```
【场景】
你是电商平台的智能客服，用户咨询订单问题。

【系统能力】
- 可查询订单状态
- 可办理退款退货
- 可修改收货地址（未发货前）
- 可提供优惠券
- 可转人工服务

【对话要求】
1. 使用友好的语言风格
2. 主动确认用户需求
3. 提供清晰的解决方案
4. 结束时总结关键信息
5. 保持耐心和礼貌

请开始与用户的对话。
用户：[用户的第一个问题]
```

---

## Prompt Templates Library

### Template 1: Meeting Summary

```
【输入】
会议主题：[主题]
会议时间：[时间]
参会人员：[人员名单]
会议内容：[会议要点]

【任务】
生成会议纪要

【输出要求】
- 会议基本信息
- 讨论事项汇总
- 决策记录
- 行动项（负责人+截止日期）
- 下次会议安排

请用表格形式呈现行动项。
```

### Template 2: Competitive Analysis

```
【任务】
进行[行业]市场竞争分析

【目标公司】
[公司A, 公司B, 公司C]

【分析维度】
1. 产品功能对比
2. 定价策略
3. 市场定位
4. 技术实力
5. 用户口碑
6. 营销策略

【输出格式】
使用对比表格 + 详细分析报告
```

### Template 3: Decision Matrix

```
【任务】
使用决策矩阵分析[决策问题]

【可选方案】
- 方案A：[描述]
- 方案B：[描述]
- 方案C：[描述]

【评估维度】
| 维度 | 权重 | 方案A | 方案B | 方案C |
|------|------|-------|-------|-------|

【任务】
1. 补充评估维度的权重（总和100%）
2. 对每个方案在各维度打分（1-10）
3. 计算加权得分
4. 给出推荐结论

请先确认评估维度和权重设置。
```

### Template 4: Troubleshooting Guide

```
【产品/系统】
[产品/系统名称]

【问题描述】
[用户报告的问题]

【诊断要求】
请生成故障排查指南：
1. 可能原因列表
2. 排查步骤（按可能性排序）
3. 每步的判断标准
4. 解决方案
5. 预防措施

【输出格式】
流程图 + 详细步骤说明
```

### Template 5: Training Material Outline

```
【培训主题】
[主题]

【目标受众】
[受众描述]

【培训时长】
[时长]

【知识基础】
[受众已掌握的知识]

【任务】
生成培训材料大纲

【输出要求】
1. 课程目标
2. 模块划分
3. 每个模块的：
   - 学习目标
   - 核心内容
   - 教学活动
   - 练习题目
4. 评估方式
5. 资源清单
```

---

## Best Practices Summary

1. **Be Specific**: Clear context leads to better outputs
2. **Use Role Assignment**: Role-playing improves response quality
3. **Structure Output**: Specify format requirements upfront
4. **Chinese First**: For Chinese tasks, use Chinese prompts
5. **Iterate**: Refine prompts based on initial responses
6. **Test Edge Cases**: Verify prompts handle variations well
7. **Document Variations**: Track what works for different scenarios

## Version History

- 2024-12: Added advanced prompting techniques
- 2024-11: Included more domain-specific templates
- 2024-10: Initial release with core prompt templates
