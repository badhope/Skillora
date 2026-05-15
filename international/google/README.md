# Google Gemini Prompts

Comprehensive collection of prompts optimized for Google's Gemini models, including Gemini Ultra, Gemini Pro, Gemini Flash, and Gemini Nano.

## 📑 Index

- [Best Practices Guide](./best-practices.md)
- [Prompt Collection](./gemini-prompts.md)
- [Agentic Workflows](./agentic-workflows.md)
- [API Templates](./api-templates.md)

## 🔗 Official Resources

- [Google AI for Developers](https://ai.google.dev/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Gemini API Reference](https://ai.google.dev/reference/rest)
- [Google AI Studio](https://aistudio.google.com/)
- [Vertex AI Gemini](https://cloud.google.com/vertex-ai/generative-ai/docs)
- [Gemini Model Specifications](https://ai.google.dev/models/gemini)

## 🎯 Quick Reference

### Model Selection Guide

| Use Case | Recommended Model | Context Length | Key Strengths |
|----------|------------------|----------------|----------------|
| Complex reasoning | Gemini Ultra | 32K tokens | Advanced reasoning, multimodal |
| General purpose | Gemini Pro | 32K tokens | Balanced performance |
| Fast responses | Gemini Flash | 1M tokens | Speed, cost efficiency |
| On-device tasks | Gemini Nano | Built-in | Privacy, offline capability |

### Generation Configuration

| Task | Temperature | Top-P | Max Output |
|------|-------------|-------|-----------|
| Code generation | 0.0 - 0.2 | 0.95 | 8192 tokens |
| Factual responses | 0.0 - 0.3 | 0.95 | 2048 tokens |
| Creative writing | 0.7 - 0.9 | 0.95 | 8192 tokens |
| Structured output | 0.0 - 0.1 | 0.95 | 4096 tokens |

### Gemini-Specific Features

1. **Multimodal Understanding**: Process text, images, audio, video, and PDFs natively
2. **Long Context Window**: Gemini Flash supports up to 1M tokens
3. **Grounded Responses**: Connect to Google Search and your data sources
4. **Function Calling**: Execute code and call external APIs
5. **Built-in Safety**: Google's safety filters and content classification

## 📊 Prompt Format Example

### Basic Format

```
System: [Role definition and context]
User: [Specific task or question]
```

### Advanced Format with Instructions

```
You are a {role} with {expertise}.
Follow these instructions:
1. {Instruction 1}
2. {Instruction 2}

Task: {description}
Context: {additional context}
```

### Multimodal Format

```
Analyze this image and provide insights:
[Insert image]

Based on the image content:
- {Question 1}
- {Question 2}
```

### Structured Output Format

```
Analyze the following text and respond in JSON format:
{
  "summary": "brief summary under 50 words",
  "sentiment": "positive|negative|neutral",
  "key_points": ["point 1", "point 2", "point 3"],
  "confidence_score": 0.0-1.0
}

Input: {your text}
```

### Chain-of-Thought Format

```
Solve this problem step by step:
1. First, identify what we're solving for
2. Break down the problem into components
3. Work through each component systematically
4. Combine the results
5. Verify the solution

Problem: {user's problem}
```

## 🔥 Popular Prompts

### Multimodal Analysis

```
Examine this image(s) carefully and provide:
1. Detailed description of the content
2. Key elements and their significance
3. Context or setting (if identifiable)
4. Any text or data present
5. Insights or observations

[Image input]
```

### Code Generation

```
You are an expert {language} developer.
Write clean, efficient, and well-documented code that:
- Follows best practices and idiomatic style
- Includes comprehensive error handling
- Is optimized for performance
- Has clear inline comments

Task: {description}
Requirements:
- {requirement 1}
- {requirement 2}
```

### Data Extraction

```
Extract structured information from the following content:

Target fields:
- Field 1: {description}
- Field 2: {description}
- Field 3: {description}

Output format: JSON

Source: {your content}
```

### Document Summarization

```
Summarize the following document:

Requirements:
- Maximum length: {X} words
- Include key findings and main points
- Highlight actionable insights
- Preserve technical accuracy

Document:
{content}
```

## 🔧 Advanced Techniques

### Grounding with Google Search

```
Answer the question using your knowledge and current information:

Query: {user question}

Instructions:
- Provide accurate, up-to-date information
- Cite sources when available
- Distinguish between established facts and speculation
- Acknowledge uncertainty when appropriate
```

### Function Calling

```
For complex tasks, use function calling to:
- Execute Python code for calculations
- Access external APIs
- Process files and data
- Perform system operations

Define your function schema and let Gemini call it appropriately.
```

### Few-Shot Learning

```
Task: {task description}

Example 1:
Input: {example input 1}
Output: {expected output 1}

Example 2:
Input: {example input 2}
Output: {expected output 2}

Your turn:
Input: {your input}
```

### ReAct (Reasoning + Acting)

```
For complex problems:
1. Think through the problem step by step
2. Identify what information you need
3. Determine the best approach
4. Execute your solution
5. Verify the results

Problem: {user's problem}
```

## 📚 Featured Collections

- [Gemini API Cookbook](https://ai.google.dev/docs/gemini-cookbook)
- [Google AI Samples](https://github.com/google/generative-ai-android)
- [Vertex AI Samples](https://cloud.google.com/vertex-ai/docs/generative-ai/code-samples)
- [Awesome Gemini](https://github.com/g瞪着啥/awesome-gemini)

## 🤝 Contributing

Please follow the contribution guidelines in the main README when adding new prompts.
