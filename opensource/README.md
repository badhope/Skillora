# Open Source Prompt Collections

Curated prompts from the most popular and influential open-source prompt engineering repositories.

## 📚 Featured Repositories

### Top GitHub Repositories

| Repository | Stars | Language | Focus | Link |
|------------|-------|----------|-------|------|
| dair-ai/Prompt-Engineering-Guide | 50k+ | Multi | Comprehensive guide | [Visit](https://github.com/dair-ai/Prompt-Engineering-Guide) |
| PlexPt/awesome-chatgpt-prompts-zh | 50k+ | Chinese | Chinese prompts | [Visit](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) |
| f/awesome-chatgpt-prompts | 30k+ | English | Role-based prompts | [Visit](https://github.com/f/awesome-chatgpt-prompts) |
| promptslab/Awesome-Prompt-Engineering | 5.9k | Multi | Engineering resources | [Visit](https://github.com/promptslab/Awesome-Prompt-Engineering) |
| ai-boost/awesome-prompts | 3.2k | Multi | Engineering focus | [Visit](https://github.com/ai-boost/awesome-prompts) |
| langgptai/awesome-claude-prompts | 5.1k | Multi | Claude collection | [Visit](https://github.com/langgptai/awesome-claude-prompts) |

## 📖 Index

- [Awesome Prompt Engineering](#awesome-prompt-engineering)
- [ChatGPT Role Prompts](#chatgpt-role-prompts)
- [Claude Prompts](#claude-prompts)
- [Engineering Prompts](#engineering-prompts)
- [Community Collections](#community-collections)

## 🎯 Awesome Prompt Engineering

Curated resources from [promptslab/Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering)

### Papers & Research

#### Chain-of-Thought Prompting

```
You are a reasoning assistant. When solving complex problems:

1. Break down the problem into smaller steps
2. Show your work for each step
3. Explain your reasoning
4. Verify your answer before concluding

Think step by step about the following problem:
[Insert problem here]
```

#### Zero-Shot Prompting

```
Task: [Describe the task clearly]

Instructions:
- Provide a direct response
- Focus on accuracy
- Be concise

Input: [Your input]
```

### Techniques Overview

| Technique | Use Case | Example |
|-----------|----------|---------|
| Zero-Shot | Simple, direct tasks | Classification, basic Q&A |
| Few-Shot | Pattern matching | Translation, formatting |
| Chain-of-Thought | Complex reasoning | Math, logic problems |
| Tree of Thoughts | Exploration | Creative writing, planning |

## 💬 ChatGPT Role Prompts

From [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)

### Linux Terminal

```
I want you to act as a Linux terminal. I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. Do not write explanations. Do not type commands unless I instruct you to do so.

My first command is: [command]
```

### English Translator

```
I want you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences into more beautiful and elegant, upper level English words and sentences. Keep the meaning same. Do not explain the corrections.

My sentence is: [sentence]
```

### Position Interviewer

```
I want you to act as an interviewer. I will be the candidate and you will ask me interview questions for the position. I want you to only reply with the interview question. And nothing else. Do not write explanations. Wait for my answers.

Position: [position name]
```

### JavaScript Console

```
I want you to act as a javascript console. I will type commands and you will reply with what the javascript console should output. I want you to only reply with the terminal output inside one unique code block, and nothing else. Do not write explanations. Do not type commands unless I instruct you to do so.

My first command is: [command]
```

### SQL Terminal

```
I want you to act as a SQL terminal. I will type commands and you will reply with what the SQL terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. Do not write explanations. Do not type commands unless I instruct you to do so.

My first command is: [SQL command]
```

### Emoji Translator

```
I want you to translate the sentences I wrote into emojis. I will write the sentence, and you will express it with emojis. I want you to write only with emojis. Do not explain.

My sentence is: [sentence]
```

### Fill in the Blank

```
I want you to act as a fill-in-the-blank worksheet creator for students. When I share a topic, you will create a worksheet with the following format:
- Topic: [topic]
- Format: [format]
- Questions: [number of questions]

Make sure the questions are interesting and educational.

Topic: [topic]
```

## 🎭 Chinese Prompts

From [PlexPt/awesome-chatgpt-prompts-zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)

### Linux Terminal

```
我想让你充当Linux终端。我会输入命令，你会回复终端应展示的内容。我希望你只在一个唯一的代码块内回复终端输出，什么都不要说。不要写解释。除非我让你这样做。

我的第一个命令是：pwd
```

### English Translator & Improver

```
我想让你充当英语翻译员、拼写纠正员和改进员。我会用任何语言和你说话，你会检测语言，翻译它，并用我文本的修正和改进版本用英语回答。我希望我的表达方式更加优雅和高级。保持意思相同。

我的句子是：今天天气怎么样？
```

### Front-end Interpreter

```
我想让你充当前端开发专家。我将提供一些关于网页、网页应用等的具体信息，你的任务是用HTML、CSS、JavaScript、React等前端技术栈来构建它们。首先创建一个包含以下内容的卡片组件：

- [具体描述]

描述应该包含以下内容：
- [具体技术要求]

也可以添加适当的动画和样式。

我的第一个请求是：创建一个加载动画
```

### Poem Creator

```
我想让你扮演一个诗人。你要创作有深刻含义的诗歌，诗歌要有情感、有张力。我会在同一行中给出主题，你要用象征手法和浪漫手法来写诗。

我的主题是：爱情
```

### Career Advisor

```
我想让你担任职业顾问。我会告诉你一个想要从事行业的人的信息，你的任务是就他们的职业发展提出建议。仔细研究该行业，给出该行业具体岗位的发展路径。要求信息真实可靠。

我的行业是：人工智能
```

### Mental Health Advisor

```
你是一个具有同理心的心理健康顾问。当一个人向你倾诉心理健康问题时，你需要：
1. 用温暖的语气回应
2. 提供理解和支持
3. 给出实用的自助建议
4. 必要时建议寻求专业帮助
5. 避免使用专业术语

用户的问题是：[问题]
```

## 💻 Engineering Prompts

From [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts)

### Code Generation

```
Generate [programming language] code for [specific task].
Requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

Example input: [input]
Expected output: [output]
```

### Test Generation

```
Create comprehensive tests for the following code:
[code]

Test framework: [framework name]
Coverage requirements:
- Unit tests for all functions
- Edge case handling
- Error conditions
```

### API Design

```
Design a RESTful API for [use case] with the following requirements:

1. Resources: [list resources]
2. Operations: [CRUD operations needed]
3. Authentication: [auth method]
4. Rate limiting: [limits if any]

Provide:
- Endpoint definitions
- Request/response formats
- Error handling
- Authentication flow
```

## 🔧 Community Collections

### Domain-Specific Prompts

#### Medical/Healthcare

```
You are a medical professional. Provide health information for:

Topic: [medical topic]
Patient context: [relevant patient information]
Purpose: [educational/consultation/self-care]

Guidelines:
- Evidence-based information only
- Include appropriate disclaimers
- Recommend professional consultation when needed
```

#### Legal

```
You are a legal professional providing general legal information.

Query type: [contract/review/advice/information]
Jurisdiction: [legal jurisdiction]
Context: [relevant context]

Important notes:
- This is general information, not legal advice
- Consult a licensed attorney for specific legal matters
```

#### Financial

```
You are a financial advisor providing general financial information.

Topic: [investment/tax/retirement/ budgeting]
Risk tolerance: [risk profile]
Time horizon: [time frame]

Disclaimer: This is general information, not financial advice.
```

## 🌐 Cross-Platform Collections

### PromptHub Curated

These prompts have been tested and adapted across multiple platforms:

| Prompt | OpenAI | Claude | Gemini | Baidu | Alibaba |
|--------|--------|--------|--------|-------|---------|
| Code Review | ✅ | ✅ | ✅ | ✅ | ✅ |
| Content Writing | ✅ | ✅ | ✅ | ✅ | ✅ |
| Data Analysis | ✅ | ✅ | ✅ | ✅ | ✅ |
| Translation | ✅ | ✅ | ✅ | ✅ | ✅ |
| Creative Writing | ✅ | ✅ | ✅ | ✅ | ✅ |

## 🤝 Contributing to Collections

When adding prompts from open-source repositories:

1. **Credit the source** - Include reference to original repository
2. **Test across platforms** - Verify compatibility
3. **Document adaptations** - Note any platform-specific changes
4. **Follow format** - Use standard prompt template

### Contribution Template

```markdown
---
title: "Prompt Title"
source: "Original Repository"
original_link: "https://github.com/..."
adapted_by: "Your Name"
platforms: [OpenAI, Claude, Gemini]
---

## Original Prompt

[Original prompt content]

## Platform Adaptations

### OpenAI
[Adapted version for OpenAI]

### Claude
[Adapted version for Claude]

## Notes
[Any additional context or testing notes]
```

## 📚 Learning Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Lil'Log Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)
- [Brex's Prompt Engineering Guide](https://github.com/brexhq/prompt-engineering)
- [Learn Prompting](https://learnprompting.org/)

## 🔄 Sync Status

| Repository | Last Synced | Status |
|------------|-------------|--------|
| dair-ai/Prompt-Engineering-Guide | 2026-05-15 | ✅ Up to date |
| PlexPt/awesome-chatgpt-prompts-zh | 2026-05-15 | ✅ Up to date |
| f/awesome-chatgpt-prompts | 2026-05-15 | ✅ Up to date |
| promptslab/Awesome-Prompt-Engineering | 2026-05-15 | ✅ Up to date |
| ai-boost/awesome-prompts | 2026-05-15 | ✅ Up to date |
