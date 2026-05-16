# Mistral & Groq Prompts

Prompts optimized for Mistral AI's models (Mistral, Mixtral) and Groq's fast inference platform.

## 📋 Index

- [Model Family](#model-family)
- [Prompt Format](#prompt-format)
- [Best Practices](#best-practices)
- [Useful Prompts](#useful-prompts)

## 🚀 Model Family

### Mistral Models

| Model | Description |
|-------|-------------|
| Mistral 7B | Base model, 7B parameters |
| Mixtral 8x7B | Mixture-of-experts model |
| Mistral-Large | Advanced large model |

### Groq Platform

Groq provides ultra-fast inference for Mistral and other open-source models with LPU (Language Processing Unit) technology.

## 📝 Prompt Format

### Mistral Format

```
<s>[INST] {system_prompt}

{user_message} [/INST]
```

### Mixtral Format

```
<s>[INST] {system}

{user} [/INST] {assistant} </s><s>[INST] {user_2} [/INST]
```

## ✨ Best Practices

### 1. Clear Instructions

```
<s>[INST] You are an expert in [domain]. Please follow these guidelines:

1. Be clear and direct
2. Think step by step
3. Explain your reasoning

[task description] [/INST]
```

### 2. Provide Examples

```
<s>[INST] Here are examples of what I'm looking for:

Example 1:
Input: [X]
Output: [Y]

Example 2:
Input: [A]
Output: [B]

Now, please do the same for:
[your input] [/INST]
```

### 3. Structured Outputs

```
<s>[INST] Analyze this and provide the following in JSON format:
{
  "summary": "brief summary",
  "key_points": [list],
  "confidence": 0-1
}

Input: [your data] [/INST]
```

## 🎯 Useful Prompts

### General Assistant

```
<s>[INST] You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible.

[your question] [/INST]
```

### Code Generation

```
<s>[INST] You are an expert programmer who writes clean, efficient code.

Write a [language] program to [description]:

Requirements:
- Clean, readable code
- Well commented
- Edge case handling
- Usage examples

Please provide the code. [/INST]
```

### Writing Assistant

```
<s>[INST] You are a skilled writer and editor.

Please help me with this writing task:

Task: [description
Audience: [audience
Tone: [tone

Write: [your content need] [/INST]
```

### Problem Solving

```
<s>[INST] Let's work through this problem step by step:

Problem: [problem

Please:
1. Understand the problem
2. Break it down
3. Analyze options
4. Recommend solution
5. Explain reasoning

What should I do? [/INST]
```

### Analysis & Summary

```
<s>[INST] You are an expert analyst. Please analyze this:

[text or data

Provide:
1. Executive summary
2. Key findings
3. Insights
4. Recommendations

Use clear, concise language. [/INST]
```

## 🚀 Groq Optimization

Groq provides ultra-fast inference - leverage this for:
- Multiple prompt iterations
- Quick generation testing
- Bulk processing
- Real-time applications

### Groq Speed Tips

```
<s>[INST] Keep responses concise for fastest speed.
```

## 📚 Resources

- [Mistral Documentation](https://docs.mistral.ai/)
- [Groq Documentation](https://console.groq.com/docs)
- [Prompt Engineering](https://docs.mistral.ai/guides/prompting/)
- [Mixtral Technical Report](https://mistral.ai/news/mixtral-of-experts/)
