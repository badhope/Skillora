# Claude Best Practices

Comprehensive guide to effective prompt engineering for Anthropic Claude models, covering XML tags, chain-of-thought, Constitutional AI, and advanced techniques.

## 🎯 Core Principles

### 1. Use XML Tags for Structure

Claude is trained to recognize and respond well to XML tags.

**Recommended Structure:**

```xml
<system>
[Role definition and global instructions]
</system>

<task>
[Primary task or question]
</task>

<context>
[Relevant background information]
</context>

<constraints>
[Requirements, limitations, or guidelines]
</constraints>

<examples>
[Sample inputs and expected outputs]
</examples>
```

**Example:**

```xml
<task>
Review the following code for security vulnerabilities.
</task>

<context>
Language: Python
Framework: Django 4.2
Code Purpose: User authentication module
</context>

<constraints>
Focus specifically on:
- SQL injection risks
- XSS vulnerabilities
- Authentication bypass
- Password storage security
</constraints>
```

### 2. Be Specific and Direct

**DO:**
- State exactly what you want
- Specify the output format
- Include relevant constraints
- Provide context upfront
- Use numbered lists for multi-step tasks

**DON'T:**
- Use vague instructions
- Leave important details implicit
- Assume Claude knows your preferences
- Mix multiple unrelated requests

### 3. Break Down Complex Tasks

Complex tasks should be broken into clear steps:

```xml
<task>
Complete this task in the following steps:

Step 1: [First action]
Step 2: [Second action]
Step 3: [Third action]
Step 4: [Final action]

Task: [Detailed task description]
</task>
```

## 🧠 Chain-of-Thought Prompting

### When to Use Chain-of-Thought

Chain-of-thought is most effective for:

- Complex reasoning problems
- Multi-step calculations
- Logical deduction tasks
- Debugging and problem diagnosis
- Strategic planning and analysis

### Basic Chain-of-Thought Template

```xml
<task>
Think through this problem step by step. For each step:
1. Identify what needs to be solved
2. Show your reasoning
3. Execute the step
4. Verify before moving on

Problem: [Your problem]

Provide your complete reasoning, then give your final answer.
</task>
```

### Extended Thinking Mode

Claude 3.5 Sonnet and newer models support extended thinking:

```xml
<task>
This is a complex problem that requires careful analysis. Work through the problem thoroughly, considering multiple angles and edge cases. Show your complete reasoning process.

Problem: [Complex problem description]

After your analysis, provide:
- Your reasoning path
- Key considerations
- Final recommendation with confidence level
</task>
```

### Chain-of-Thought Examples

**Mathematical Problem:**

```xml
<task>
Solve this problem by showing your work at each step.

Problem: If a train leaves Station A at 9:00 AM traveling 60 mph, and another train leaves Station B at 9:30 AM traveling 80 mph, and the stations are 200 miles apart, at what time will the trains meet?

For each calculation step:
- State the equation or logic
- Show the computation
- Verify the intermediate result
</task>
```

**Logical Deduction:**

```xml
<task>
Solve this logic puzzle step by step, showing your reasoning for each deduction.

Puzzle: Three houses are next to each other. The red house is to the left of the middle house. The blue house is at the right end. The green house is next to the red house.

Question: In what order are the houses arranged?

For each deduction:
1. State what you know
2. Show what this implies
3. Eliminate possibilities
4. Reach the conclusion
</task>
```

## 📜 Constitutional AI

Constitutional AI (CAI) is Anthropic's approach to making AI systems safer and more aligned. It involves having the AI critique and revise its own outputs based on a set of principles.

### Constitutional AI Principles

```xml
<system>
Follow these principles when responding:

1. Harmlessness: Do not generate content that could cause harm to people or society

2. Helpfulness: Provide genuinely useful assistance that addresses the user's needs

3. Honesty: Be truthful, acknowledge uncertainty, and avoid deception

4. Transparency: Be clear about your limitations and assumptions

5. Fairness: Avoid bias and treat all perspectives fairly

Critique your response against these principles before providing it.
</system>
```

### Self-Critique Template

```xml
<task>
Answer the following question, then critique your own response.

Question: [Your question]

After providing your answer, include a critique section:
- Potential issues with my response
- Ways to improve accuracy
- Limitations or uncertainties
- Alternative perspectives to consider
</task>
```

### Harmlessness Testing

```xml
<task>
Before responding to this request, evaluate it against these criteria:

1. Could this request lead to harm if fulfilled?
2. Does it violate legal or ethical guidelines?
3. Could it enable dangerous, illegal, or malicious activities?

Request: [User's request]

If the request is safe, proceed with a helpful response.
If there are concerns, explain them clearly and offer a safe alternative.
</task>
```

## 🏷️ XML Tags Best Practices

### Standard Tag Categories

| Tag | Purpose | When to Use |
|-----|---------|-------------|
| `<system>` | Global instructions, role definition | Always at the top |
| `<task>` | Primary request or question | Always required |
| `<context>` | Background information | When context helps |
| `<constraints>` | Requirements, limitations | When boundaries matter |
| `<examples>` | Sample inputs/outputs | For consistency |
| `<output_format>` | Expected response structure | When format is important |
| `<persona>` | Character/voice definition | For creative tasks |
| `<reminder>` | Important notes | To emphasize key points |

### Nested Tags

```xml
<task>
Perform a comprehensive code review.
</task>

<context>
<technology>
- Language: TypeScript
- Framework: React 18
- Testing: Jest
- Purpose: E-commerce application
</technology>

<codebase>
- 15 components
- 3 custom hooks
- Authentication module
- Payment integration
</codebase>
</context>

<constraints>
Review focus areas:
- Performance optimization
- Security vulnerabilities
- Type safety
- Error handling
</constraints>
```

### Tag Styling

Claude responds well to consistent tag styling:

```xml
<!-- Use lowercase tags for clarity -->
<task>Not <TASK> or <Task></task>

<!-- Be consistent throughout -->
<context>
  <relevant_info>...</relevant_info>
</context>

<!-- Don't overuse tags - keep it practical -->
```

## 📋 Practical Templates

### Code Review Template

```xml
<task>
Perform a comprehensive code review for the following code.

Language: [Programming language]
Purpose: [What the code does]
</task>

<code>
[Paste code here]
</code>

<focus_areas>
1. Code quality and readability
2. Performance issues
3. Security vulnerabilities
4. Best practice compliance
5. Testing coverage
</focus_areas>

<output_format>
Provide your review in this format:

## Summary
[Overall assessment]

## Strengths
[What was done well]

## Issues Found
| Severity | Location | Issue | Recommendation |
|----------|----------|-------|----------------|

## Suggested Improvements
[Practical suggestions with code examples]
</output_format>
```

### Meeting Summarizer Template

```xml
<task>
Analyze this meeting transcript and create a structured summary.

Transcript:
[Paste transcript]

<output_format>
Format your response as:

## Executive Summary
[2-3 sentences on key outcomes]

## Attendees
[Names or roles if mentioned]

## Key Discussion Points
1. [Point 1]
2. [Point 2]
3. [Point 3]

## Decisions Made
- [Decision 1]
- [Decision 2]

## Action Items
| Task | Owner | Due Date |
|------|-------|----------|

## Open Questions
- [Question 1]
- [Question 2]

## Next Steps
[What happens next]
</output_format>
```

### Data Analysis Template

```xml
<task>
Perform a comprehensive analysis of the provided data.

Data Source: [Description]
Analysis Type: [Descriptive/Diagnostic/Predictive]
Key Questions:
1. [Question 1]
2. [Question 2]
3. [Question 3]
</task>

<data>
[Paste or describe data]
</data>

<deliverables>
- Summary statistics
- Key patterns and trends
- Anomalies or outliers
- Insights and recommendations
- Suggested visualizations
</deliverables>

<output_format>
Return in this structure:
1. Executive Summary
2. Data Overview
3. Analysis Results
4. Key Findings
5. Recommendations
6. Limitations
</output_format>
```

## ⚡ Optimization Tips

### Response Quality

| Issue | Solution |
|-------|----------|
| Too verbose | Add: "Keep responses concise and focused" |
| Missing details | Add: "Include specific examples and evidence" |
| Wrong format | Specify: "Return as JSON" or "Use bullet points" |
| Factual errors | Add: "Only use information provided above" |
| Inconsistent tone | Define: "Tone: [formal/casual/technical]" |

### Token Optimization

1. **Be specific early**: Put key instructions in `<task>` tag
2. **Use constraints**: Limit scope to reduce unnecessary elaboration
3. **Combine related requests**: Batch similar tasks
4. **Specify output length**: "In 3 sentences" or "Under 100 words"
5. **Remove redundant context**: Only include what's relevant

### Handling Edge Cases

```xml
<task>
[Your main task]

Edge Case Handling:
- If information is missing: [How to handle]
- If the request is unclear: [Fallback behavior]
- If I cannot complete the request: [Error format]

Boundary Constraints:
- Do not exceed [specific limit]
- Stop if [condition is met]
- Clarify before proceeding if [situation occurs]
</task>
```

## 🔄 Advanced Patterns

### Multi-Agent Coordination

```xml<system>
You are a team lead coordinating multiple specialists. Your role is to:
1. Understand the overall task
2. Assign appropriate specialists
3. Synthesize their responses
4. Ensure consistency and completeness
</system>

<task>
[Complex task that benefits from multiple perspectives]

<specialists>
- Technical Expert: [Focus area]
- Creative Strategist: [Focus area]
- Quality Assurance: [Focus area]
</specialists>

Coordinate their input and provide a unified response.
</task>
```

### Iterative Refinement

```xml
<task>
Create an initial version of [what you need].

Then, critique your own work:
1. What could be improved?
2. What might be missing?
3. How could it be more effective?

Based on the critique, create an improved version.
</task>
```

### Comparative Analysis

```xml
<task>
Compare [Subject A] and [Subject B] across these dimensions:

Dimensions:
1. [Dimension 1]
2. [Dimension 2]
3. [Dimension 3]
4. [Dimension 4]
5. [Dimension 5]

Format:
1. Comparison table
2. Analysis for each dimension
3. Overall assessment
4. Recommendations

Subjects:
A: [Description]
B: [Description]
</task>
```

## 🎯 Claude-Specific Recommendations

### Strengths to Leverage

- **Long context**: Use extensive examples and context
- **Nuanced reasoning**: Pose complex, multi-faceted questions
- **Code understanding**: Include full code snippets, not summaries
- **Writing quality**: Ask for multiple drafts or variations

### Common Pitfalls to Avoid

- **Under-specifying**: Claude works better with clear instructions
- **Over-complicating**: Simple, direct prompts often work best
- **Ignoring XML tags**: Structured input improves consistency
- **Forgetting constraints**: Explicit limits help control outputs

### Best Model Selection

| Use Case | Recommended Model | Why |
|----------|------------------|-----|
| Simple Q&A | Claude 3 Haiku | Fast, cost-effective |
| Complex reasoning | Claude 3 Opus | Best performance |
| Balanced tasks | Claude 3 Sonnet | Speed/intelligence balance |
| Extended thinking | Claude 3.5 Sonnet | Enhanced reasoning |

## 🔗 Related Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Claude API Reference](https://docs.anthropic.com/claude/reference)
- [Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
