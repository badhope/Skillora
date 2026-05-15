# Qwen Model Prompt Engineering Guide

## Table of Contents

1. [Qwen Model Overview](#qwen-model-overview)
2. [System Prompt Engineering](#system-prompt-engineering)
3. [Cross-Lingual Prompts](#cross-lingual-prompts)
4. [Code Generation Prompts](#code-generation-prompts)
5. [Long Context Prompts](#long-context-prompts)
6. [Function Calling](#function-calling)
7. [Multimodal Prompts](#multimodal-prompts)
8. [Domain-Specific Templates](#domain-specific-templates)

---

## Qwen Model Overview

### Available Models

| Model | Context | Strengths | Best For |
|-------|---------|-----------|----------|
| qwen-max | 128K | Best quality, longest context | Complex reasoning |
| qwen-plus | 32K | Balanced | Production applications |
| qwen-turbo | 8K | Fast, cost-effective | Simple tasks |
| qwen-max-longcontext | 128K | Extended comprehension | Document analysis |

### Qwen2.5 Open Source Models

```markdown
Available on ModelScope and HuggingFace:
- Qwen2.5-0.5B, 1.5B, 3B, 7B, 14B, 32B, 72B
- Qwen2.5-Coder (7B, 32B) - Specialized code models
- Qwen2.5-Math (7B, 72B) - Mathematical reasoning
```

---

## System Prompt Engineering

### Core System Prompt Templates

#### Template: Professional Assistant

```
【角色】
你是一位专业的AI助手，具备广泛的知识储备和专业能力。

【核心能力】
- 信息查询和分析
- 文档撰写和编辑
- 编程和技术支持
- 问题解答和建议
- 多语言翻译

【交互原则】
1. 专业、准确、有条理
2. 主动确认用户需求
3. 复杂问题分步骤解答
4. 不知道的问题如实说明
5. 适当使用结构化表达

【输出偏好】
- 使用Markdown格式化
- 重要信息加粗或列表标注
- 代码块标注语言
- 适当举例说明
```

#### Template: Chinese Content Expert

```
【专长】
你是一位精通中文内容创作的专家，对中文互联网文化和表达方式有深入理解。

【内容类型】
- 新闻报道
- 社交媒体文案
- 营销软文
- 产品介绍
- 专业文章

【风格特点】
- 符合中文阅读习惯
- 使用流行词汇和梗（如适用）
- 情感共鸣强
- 接地气不生硬

【禁忌】
- 不使用翻译腔
- 不堆砌空洞词汇
- 不使用过时表达
- 避免敏感话题
```

#### Template: Technical Expert

```
【身份】
资深技术专家，精通多个技术领域。

【专业领域】
- 软件架构设计
- 算法和数据结构
- 云原生技术
- DevOps最佳实践
- 安全加固

【回答规范】
1. 先概述核心概念
2. 提供具体代码示例
3. 说明优缺点和适用场景
4. 指出常见误区
5. 推荐学习路径

【代码要求】
- 遵循最佳实践
- 包含注释说明
- 标注版本要求
- 说明注意事项
```

---

## Cross-Lingual Prompts

### Chinese to English Translation

```
【翻译任务】
将以下中文内容翻译为专业英文

【原文】
{input_text}

【翻译风格】
- 目标受众：{audience}
- 用途：{purpose}
- 风格：{formal/casual/technical}

【翻译要求】
1. 符合英文母语表达习惯
2. 避免中式英语思维
3. 保持专业术语准确性
4. 适当本地化文化元素
5. 保持原文语气和风格

【输出格式】
翻译后文本：
[英文内容]

术语对照表：
| 中文 | 英文 | 说明 |
|------|------|------|

如有不确定的翻译，说明备选方案。
```

### English to Chinese Translation

```
【翻译任务】
将以下英文内容翻译为地道中文

【原文】
{input_text}

【目标】
- 目标读者：{chinese_readers}
- 期望语气：{desired_tone}

【翻译原则】
1. 符合中文表达习惯
2. 适当增删（不改变原意）
3. 使用中文标点符号
4. 保持原文风格
5. 必要时添加注释

【特殊处理】
- 专有名词：[音译/保留英文/意译]
- 文化表达：[解释/意译/保留]
- 缩写词：[展开/保留]

请先说明翻译策略。
```

### Bilingual Content Creation

```
【任务】
创作中英双语内容

【主题】
{topic}

【格式要求】
1. 中文内容在前，英文翻译在后
2. 两版本意思完全对应
3. 保持各语言的地道表达
4. 使用对照格式便于阅读

【输出模板】
【中文】
[中文内容]

【English】
[English translation]

【关键词对照】
中文关键词 → English Keywords
```

### Bilingual FAQ Generation

```
【产品/服务】
{product_name}

【目标市场】
中国 + 英文市场

【任务】
为以下问题生成中英双语文档

【问题列表】
1. [问题1]
2. [问题2]
3. [问题3]

【格式】
| 中文问题 | Chinese Question |
|---------|------------------|
| 中文回答 | English Answer |

确保回答简洁，便于翻译对照。
```

---

## Code Generation Prompts

### Python Development

```
【编程任务】
{task_description}

【技术栈】
- 语言：Python {version}
- 环境：{environment}

【功能要求】
1. [具体要求1]
2. [具体要求2]
3. [具体要求3]

【质量要求】
- 遵循PEP 8规范
- 使用类型提示
- 完整的错误处理
- 包含docstring
- 可运行的代码

【输出要求】
```python
# 完整代码
```

【测试建议】
- 单元测试用例
- 边界条件测试
- 异常输入测试

请提供代码和简要说明。
```

### JavaScript/Node.js Development

```
【项目类型】
{frontend/backend/nodejs}

【任务描述】
{task_description}

【依赖要求】
- Node.js版本：{version}
- 包管理器：npm/yarn/pnpm

【技术要求】
- 异步处理最佳实践
- 错误边界处理
- 安全性考虑
- 性能优化

【输出】
1. 核心代码
2. package.json配置
3. 使用示例
4. API文档（如适用）
```

### SQL Query Optimization

```
【任务】
优化以下SQL查询

【原始SQL】
{input_sql}

【数据库】
- 类型：MySQL/PostgreSQL/Oracle
- 版本：{version}

【问题描述】
- 性能问题：{symptom}
- 数据量：{table_size}
- 索引情况：{existing_indexes}

【优化要求】
1. 提升查询性能
2. 保持功能不变
3. 解释优化原理
4. 预估效果

【输出】
- 优化后的SQL
- 索引建议
- 执行计划对比
- 注意事项
```

### Code Review Prompt

```
【代码语言】
{language}

【代码】
```{language}
{code}
```

【审查维度】
1. 功能正确性
2. 性能效率
3. 代码可读性
4. 安全漏洞
5. 最佳实践
6. 扩展性

【输出格式】
```markdown
## 问题列表

### 🔴 严重问题
[描述及修复建议]

### 🟡 建议改进
[描述及建议]

### 🟢 优点
[代码亮点]

## 总体评分
[X/10]

## 改进后的代码
```
```

---

## Long Context Prompts

### Document Analysis (30K+ tokens)

```
【任务类型】
长文档分析与理解

【文档信息】
- 文档标题：{title}
- 文档类型：{type}
- 文档长度：{length}

【分析要求】
1. **核心内容摘要**（不超过原文5%）
2. **关键信息提取**：
   - 主要观点（3-5个）
   - 重要数据（表格列出）
   - 关键人物/机构
   - 时间线
3. **结构分析**：
   - 文档逻辑框架
   - 章节关系
4. **深度理解**：
   - 隐含观点分析
   - 作者立场判断
   - 论证有效性评估

【输出格式】
- 执行摘要
- 详细分析
- 关键信息表格
- 相关问题建议

【特殊指令】
- 如有矛盾信息，标注说明
- 如有不清晰之处，指出问题
- 如发现错误，基于事实纠正
```

### Multi-Document Comparison

```
【任务】
对比分析多个文档

【文档列表】
1. {doc1_title} - {doc1_type}
2. {doc2_title} - {doc2_type}
3. {doc3_title} - {doc3_type}

【分析维度】
1. 核心观点对比
2. 数据/事实一致性
3. 立场/态度对比
4. 方法论差异
5. 结论对比

【输出要求】
1. 各文档摘要（简述）
2. 对比表格
3. 共识点分析
4. 争议点分析
5. 综合结论

请确保对比公正客观。
```

### Meeting Minutes Analysis

```
【输入】
会议纪要内容（共{length}字）

【任务】
1. 提取会议基本信息（时间、地点、参会人）
2. 汇总讨论事项
3. 识别已做决策
4. 提取行动项（负责人+截止日期）
5. 标记待跟进问题
6. 评估会议效果

【输出格式】
## 会议概况
## 核心讨论
## 决策记录
## 行动清单（表格）
## 遗留问题
## 后续建议
```

### Contract Review

```
【任务】
合同条款分析

【合同类型】
{contract_type}

【合同全文】
{contract_text}

【分析维度】
1. 合同主体资格
2. 权利义务对等性
3. 关键条款完整性
4. 潜在法律风险
5. 模糊条款识别
6. 违约责任评估
7. 争议解决条款
8. 合规性检查

【风险等级】
- 🔴 高风险：立即修改
- 🟡 中风险：需要澄清
- 🟢 低风险：可接受

【输出】
- 风险清单
- 修改建议
- 谈判要点
```

---

## Function Calling

### Tool Definition Format

```json
{
  "name": "get_weather",
  "description": "获取指定城市的天气信息",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string",
        "description": "城市名称，使用中文，如：北京、上海"
      },
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "温度单位"
      }
    },
    "required": ["city"]
  }
}
```

### Multi-Tool Agent Prompt

```
【角色】
你是智能助手，可以调用多种工具来帮助用户完成任务。

【可用工具】
1. **search_web**: 搜索互联网信息
   - 输入：搜索关键词
   - 输出：搜索结果摘要

2. **calculate**: 数学计算
   - 输入：数学表达式
   - 输出：计算结果

3. **get_date**: 获取当前日期
   - 输入：无
   - 输出：当前日期

4. **translate**: 翻译服务
   - 输入：文本 + 目标语言
   - 输出：翻译结果

【工作流程】
1. 理解用户需求
2. 确定是否需要工具
3. 选择合适的工具
4. 调用工具获取结果
5. 处理结果并回复用户

【注意事项】
- 仅调用必要的工具
- 处理工具执行失败的情况
- 必要时组合使用多个工具
- 清楚说明工具使用情况

【示例】
用户：今天北京天气怎么样？

助手：我来查询一下北京今天的天气。
[调用 search_web 工具]
根据查询结果，今天北京天气晴朗，气温15-22度。
```

### RAG System Prompt

```
【角色】
你是一个基于检索增强的问答助手。

【知识库范围】
- 公司产品信息
- 常见问题解答
- 技术文档
- 内部政策

【工作原理】
1. 先在知识库中检索相关信息
2. 基于检索结果回答问题
3. 如未找到相关信息，明确说明

【回答规范】
1. 优先使用检索到的知识
2. 注明信息来源
3. 不编造不确定的信息
4. 建议用户寻求进一步帮助（如需要）

【检索结果】
{retrieved_context}

【用户问题】
{user_question}

【回答】
```

---

## Multimodal Prompts

### Image Understanding

```
【图像内容】
请分析以下图片

【分析维度】
1. 图片类型（照片/图表/截图/设计图）
2. 主体内容描述
3. 关键细节提取
4. 图片质量评估
5. 潜在用途建议

【输出要求】
- 详细文字描述
- 结构化信息提取
- 相关建议

【如为图表】
- 数据解读
- 趋势分析
- 关键发现

请提供完整的图像分析报告。
```

### Vision + Language Task

```
【任务】
基于图片内容回答问题

【图片】
[提供图片]

【问题】
{question}

【回答要求】
1. 准确理解图片内容
2. 结合问题进行针对性分析
3. 如需补充信息，明确说明

请给出详细回答。
```

---

## Domain-Specific Templates

### E-commerce Product Description

```
【产品信息】
- 产品名称：{product_name}
- 品牌：{brand}
- 类别：{category}
- 价格：{price}
- 核心卖点：{key_features}

【目标市场】
{market}

【任务】
生成电商平台产品详情页

【内容要求】
1. 吸引眼球的标题
2. 产品卖点（bullet points）
3. 详细描述（200-500字）
4. 规格参数表
5. 买家须知
6. SEO关键词

【风格】
- 符合平台调性
- 突出差异化
- 增强购买欲望
- 建立信任感

【输出格式】
Markdown格式，便于直接使用
```

### Data Analysis Report

```
【数据源】
{describe_data_source}

【分析目标】
{analysis_objective}

【可用字段】
{field_descriptions}

【分析要求】
1. 数据概览
2. 描述性统计
3. 趋势分析
4. 关联分析
5. 异常发现
6. 结论建议

【输出要求】
- 包含数据可视化建议（文字描述图表类型）
- 表格展示关键数据
- 结论有数据支撑
```

### Marketing Campaign Brief

```
【活动信息】
- 活动名称：{campaign_name}
- 目标：{objectives}
- 目标受众：{target_audience}
- 时间：{timeline}
- 预算：{budget}

【品牌信息】
- 品牌调性：{brand_tone}
- 主色调：{colors}
- Slogan：{slogan}

【任务要求】
1. 活动主题概念
2. 核心信息
3. 渠道策略
4. 内容创意方向
5. 关键里程碑
6. KPI建议
7. 风险预案

【输出】
完整营销策划简报
```

### Legal Document Drafting

```
【文件类型】
{contract_type/document_type}

【当事人信息】
{parties_info}

【核心条款】
{key_terms}

【背景说明】
{background}

【任务】
起草完整的法律文档

【要求】
1. 使用标准法律用语
2. 条款完整无遗漏
3. 语言准确无歧义
4. 保护当事人权益
5. 便于执行和争议解决

【格式】
- 标题
- 目录
- 正文条款
- 签署栏

【免责声明】
本文件为模板参考，具体使用请咨询专业律师。
```

---

## Best Practices

1. **Be Explicit**: Clear instructions yield better results
2. **Use Structure**: Markdown and lists improve output organization
3. **Provide Examples**: Few-shot examples guide desired format
4. **Set Boundaries**: Specify what's out of scope
5. **Iterate**: Refine prompts based on outputs
6. **Context Matters**: Include relevant background
7. **Temperature Tuning**: Lower for factual, higher for creative

## Version History

- 2024-12: Added function calling and RAG templates
- 2024-11: Expanded cross-lingual content
- 2024-10: Core prompt templates released
