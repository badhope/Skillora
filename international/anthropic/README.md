# Anthropic Claude Prompts

Comprehensive collection of prompts optimized for Anthropic's Claude models including Claude 3 Opus, Sonnet, and Haiku, covering the API, Claude.ai, and Claude for Work.

## 📑 Index

- [Best Practices Guide](./best-practices.md)
- [System Prompts](./system-prompts.md)

## 🔗 Official Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Claude API Documentation](https://docs.anthropic.com/claude/reference)
- [Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Developer Console](https://console.anthropic.com)

## 🎯 Quick Reference

### Model Selection Guide

| Use Case | Recommended Model | Context Length | Strengths |
|----------|------------------|----------------|-----------|
| Complex reasoning | Claude 3 Opus | 200K tokens | Best for nuanced tasks, research, coding |
| Balanced performance | Claude 3 Sonnet | 200K tokens | Excellent speed and intelligence balance |
| High volume tasks | Claude 3 Haiku | 200K tokens | Fastest, most cost-effective |
| Extended thinking | Claude 3.5 Sonnet | 200K tokens | Enhanced reasoning with extended thinking |

### Claude-Specific Features

#### XML Tag Structure

Claude excels when prompts are wrapped in XML tags for clear structure:

```xml
<task>
[Your specific task or question]
</task>

<context>
[Relevant background information]
</context>

<constraints>
[Requirements or limitations]
</constraints>

<examples>
[Sample inputs and expected outputs]
</examples>
```

#### Thinking Mode

Claude can use extended thinking to work through complex problems:

```
<thinking>
[Claude's internal reasoning process - not shown to user]
</thinking>

<response>
[Final response to the user]
</response>
```

### Temperature Settings

| Task | Temperature | Use Case |
|------|-------------|----------|
| Precise, deterministic | 0 - 0.2 | Code generation, factual answers |
| Balanced | 0.2 - 0.5 | General assistance, explanations |
| Creative, flexible | 0.5 - 0.7 | Writing, brainstorming |
| Highly creative | 0.7 - 1.0 | Creative content, games |

## 📊 Claude Prompt Format

### Basic Format

```xml
<system>
You are [role] with expertise in [domain]. Your task is to [specific goal].
</system>

<task>
[User's specific request]
</task>
```

### Advanced Format with XML Tags

```xml
<system>
You are a [professional role] with [X years] of experience in [field].

Your characteristics:
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]

When responding, always:
1. [Behavior 1]
2. [Behavior 2]
3. [Behavior 3]
</system>

<task>
[Detailed task description]
</task>

<context>
[Background information, constraints, or domain knowledge]
</context>

<output_format>
[Expected format for the response]
</output_format>

<examples>
Example 1:
Input: [Example input]
Output: [Expected output]
</examples>
```

## 🔥 Popular Prompts

### Code Generation

```xml
<task>
Write clean, efficient [programming language] code that:
- Follows best practices and modern conventions
- Includes comprehensive error handling
- Is optimized for performance and readability
- Contains inline documentation

Create a [function/class/module] that [specific functionality].
</task>

<constraints>
- Use [specific library/framework] if applicable
- Ensure compatibility with [version/environment]
- Follow [style guide/naming conventions]
</constraints>
```

### Writing Assistant

```xml
<task>
You are a professional [writing type] specialist.

Your task: [specific writing goal]
Tone: [formal/casual/technical/conversational]
Audience: [target audience description]
Length: [word count or level of detail]

Write [specific content type] about [topic].

Requirements:
1. [Specific requirement]
2. [Specific requirement]
3. [Specific requirement]
</task>
```

### Data Analysis

```xml
<task>
Analyze the following data and provide:
1. Key insights and patterns
2. Statistical summary
3. Anomalies or outliers
4. Recommendations based on findings

Data Source: [Description of the data]
Analysis Type: [Descriptive/Diagnostic/Predictive]

Data:
[Paste or describe data here]
</task>

<output_format>
Format the response with:
- Executive summary
- Detailed analysis
- Supporting visualizations (if applicable)
- Actionable recommendations
</output_format>
```

## 🔧 Advanced Techniques

### Constitutional AI Approach

```xml
<system>
Follow these principles (Constitutional AI):
1. Harmlessness: Avoid generating harmful, unethical, or dangerous content
2. Helpfulness: Provide useful and relevant assistance
3. Honesty: Be truthful and acknowledge limitations
4. Transparency: Be clear about uncertainty and assumptions

Critique your own response to ensure it meets these principles.
</system>

<task>
[Your task here]
</task>
```

### Chain-of-Thought with XML Tags

```xml
<task>
Solve this problem step by step, showing your reasoning:

Problem: [User's problem]

For each step:
1. Identify what needs to be solved
2. Show your reasoning process
3. Execute the step
4. Verify the result before moving on

Final Answer: [Your solution with confidence level]
</task>
```

### Structured Output

```xml
<task>
Analyze [input] and respond in this JSON format:

{
  "summary": "Brief summary of findings",
  "key_points": ["Point 1", "Point 2", "Point 3"],
  "analysis": {
    "strengths": ["Strength 1", "Strength 2"],
    "weaknesses": ["Weakness 1", "Weakness 2"]
  },
  "confidence": 0.0-1.0,
  "recommendations": ["Recommendation 1", "Recommendation 2"]
}

Input: [Your input here]
</task>
```

## 🤝 Cross-Platform Adaptation

### From OpenAI Prompts

When adapting OpenAI prompts for Claude:

1. **Add XML tags**: Wrap sections in `<task>`, `<context>`, `<system>` tags
2. **Be explicit about reasoning**: Claude benefits from clear step-by-step instructions
3. **Include constraints**: Specify boundaries and requirements clearly
4. **Use examples**: Few-shot examples improve consistency

### From Claude to Other Platforms

Claude prompts can be adapted for:
- OpenAI models: Remove XML tags, use plain text formatting
- Google Gemini: Keep structured format, adjust for Gemini's strengths
- Local models: Simplify complex instructions, reduce token count

## 📚 Featured Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Claude API Reference](https://docs.anthropic.com/claude/reference)
- [Prompt Library](https://docs.anthropic.com/claude/docs/prompt-library)
- [Example Prompts](https://github.com/anthropics/anthropic-cookbook)

## 🤝 Contributing

Please follow the contribution guidelines in the main README when adding new prompts.
