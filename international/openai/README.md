# OpenAI (GPT Series) Prompts

Comprehensive collection of prompts optimized for OpenAI's GPT models including ChatGPT, GPT-4, and the API.

## 📑 Index

- [Best Practices Guide](./best-practices.md)
- [System Prompts](./system-prompts.md)
- [API Templates](./api-templates.md)
- [Code Generation](./code-generation.md)
- [Writing Prompts](./writing-prompts.md)
- [Analysis & Reasoning](./analysis-reasoning.md)

## 🔗 Official Resources

- [OpenAI Platform Documentation](https://platform.openai.com/docs)
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [API Reference](https://platform.openai.com/docs/api-reference)

## 🎯 Quick Reference

### Model Selection Guide

| Use Case | Recommended Model | Context Length |
|----------|------------------|----------------|
| Simple tasks | GPT-3.5 Turbo | 16K tokens |
| Complex reasoning | GPT-4 | 8K / 32K tokens |
| Long documents | GPT-4 Turbo | 128K tokens |
| Cost optimization | GPT-3.5 Turbo | 16K tokens |

### Temperature Settings

| Task | Temperature | Creativity Level |
|------|-------------|------------------|
| Code generation | 0 - 0.2 | Low |
| Factual answers | 0 - 0.3 | Low |
| General writing | 0.5 - 0.7 | Medium |
| Creative writing | 0.7 - 1.0 | High |

### System Prompt Best Practices

1. **Be explicit** about the role and expertise
2. **Specify output format** when needed
3. **Include constraints** and limitations
4. **Provide examples** for complex tasks
5. **Use delimiters** for structured input

## 📊 Prompt Format Example

```markdown
# Basic Format
System: [Role definition and context]
User: [Specific task or question]

# Advanced Format with Examples
System: You are a [role] with [expertise]. Follow these rules:
1. [Rule 1]
2. [Rule 2]

User: [Task]
[Context/Input]

# Few-Shot Example Format
System: [Task description]

Example 1:
Input: [Example input]
Output: [Expected output]

User: [Your input]
```

## 🔥 Popular Prompts

### Code Generation

```
You are an expert [programming language] developer.
Write clean, efficient, and well-documented code that:
- Follows best practices
- Includes error handling
- Is optimized for performance

Write a function that [description]
```

### Writing Assistant

```
You are a professional [writing type] specialist.
Your task: [specific writing goal]
Tone: [formal/casual/technical]
Audience: [target audience]
Length: [word count or level of detail]

Write [specific content type] about [topic]
```

### Data Analysis

```
You are a data analyst with expertise in [domain].
Analyze the following data and provide:
1. Key insights
2. Statistical summary
3. Visualizations (if applicable)
4. Recommendations

Data: [your data]
```

## 🔧 Advanced Techniques

### Chain-of-Thought Prompting

```markdown
You are a logical reasoning assistant. For complex problems:
1. Break down the problem into steps
2. Show your reasoning for each step
3. Provide the final answer with confidence level

Problem: [user's problem]
```

### Role-Based Prompting

```markdown
You are [Professional Role] with [X years] of experience in [field].
Your characteristics:
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]

When responding, always [specific behavior]
```

### Structured Output

```markdown
Analyze [input] and respond in this JSON format:
{
  "summary": "brief summary",
  "key_points": ["point 1", "point 2"],
  "confidence": 0.0-1.0,
  "recommendations": ["rec 1", "rec 2"]
}

Input: [user's input]
```

## 📚 Featured Collections

- [Awesome Prompt Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering)
- [ChatGPT Prompts Collection](https://github.com/f/awesome-chatgpt-prompts)
- [GPT-4 Prompts & Use Cases](https://github.com/ai-boost/awesome-prompts)

## 🤝 Contributing

Please follow the contribution guidelines in the main README when adding new prompts.
