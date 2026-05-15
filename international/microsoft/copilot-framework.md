# Microsoft 365 Copilot Framework

The official framework for structuring effective prompts in Microsoft 365 Copilot applications, designed to maximize productivity and achieve consistent, high-quality results across the Microsoft 365 ecosystem.

## 📋 Framework Overview

The **GCES Framework** (Goal, Context, Source, Expectations) provides a structured approach to writing prompts that work effectively with Microsoft 365 Copilot's capabilities across Word, Excel, PowerPoint, Teams, Outlook, and other Microsoft 365 applications.

### Framework Components

| Component | Description | Purpose |
|-----------|-------------|---------|
| **Goal** | What you want to achieve | Defines the primary objective and desired outcome |
| **Context** | Background information | Provides necessary background, constraints, and situation |
| **Source** | Input materials | Identifies documents, files, or data to reference |
| **Expectations** | Output specifications | Specifies format, tone, length, and quality standards |

## 🎯 Goal Definition

The Goal component answers: **What do you want Copilot to do?**

### Goal Best Practices

1. **Start with an action verb**: Draft, summarize, analyze, create, compare, recommend
2. **Be specific about the output type**: Presentation, email, report, table, list
3. **Include quantity when relevant**: "3 key points", "5 recommendations"
4. **Define the purpose**: Inform, persuade, explain, update, approve

### Goal Examples

| Application | Example Goal |
|-------------|-------------|
| Word | "Draft a project charter document" |
| Excel | "Analyze the quarterly sales data" |
| PowerPoint | "Create a 10-slide executive presentation" |
| Teams | "Summarize the meeting discussion" |
| Outlook | "Draft a response to the customer inquiry" |

### Action Verbs by Category

**Creation:**
- Draft, Write, Create, Generate, Compose, Produce

**Analysis:**
- Analyze, Review, Evaluate, Assess, Examine, Compare

**Summarization:**
- Summarize, Condense, Distill, Extract, Highlight

**Transformation:**
- Rephrase, Rewrite, Convert, Transform, Format

**Communication:**
- Respond, Reply, Draft, Compose, Address

## 📖 Context Setting

The Context component answers: **What background information does Copilot need?**

### Context Elements

| Element | Description | Example |
|---------|-------------|---------|
| **Situation** | Current state or problem | "We need to address customer complaints" |
| **Audience** | Who will receive the output | "For executive leadership review" |
| **Constraints** | Limitations or requirements | "Must be completed by Friday" |
| **Background** | Relevant history or information | "Based on the merger announcement" |

### Context Examples

```
Situation: The marketing campaign exceeded budget by 15%
Audience: Board of Directors
Constraints: Must include cost reduction recommendations
Timeline: Q2 delivery

Situation: New employee onboarding process needs streamlining
Audience: HR team and new hires
Constraints: Must comply with legal requirements
Current: Existing 20-page onboarding guide
```

### Context Qualifiers

- **Audience level**: Executive, Manager, Technical, General
- **Urgency**: Immediate, Standard, Long-term
- **Confidentiality**: Public, Internal, Confidential
- **Tone**: Formal, Casual, Technical, Persuasive

## 📂 Source Identification

The Source component answers: **What materials should Copilot reference?**

### Source Types

| Source Type | Examples | How to Reference |
|-------------|----------|------------------|
| **Documents** | Word files, PDFs, presentations | File name, location, or content |
| **Data** | Excel spreadsheets, databases | Sheet name, cell ranges |
| **Communications** | Emails, Teams messages | Subject, sender, date |
| **Calendar** | Meetings, events | Meeting title, date |
| **Web** | Articles, websites | URL or topic |

### Source Specification Methods

**Direct Reference:**
```
Based on the Q3_Sales_Report.xlsx file in the Sales folder
```

**Content Extraction:**
```
Using the key findings from the attached market research document
```

**Cross-Reference:**
```
Compare the information in Project_Plan.docx with the timeline in
the Team project channel
```

**Semantic Search:**
```
Find all emails from the last month discussing budget concerns
```

### Microsoft Graph Integration

Microsoft 365 Copilot leverages Microsoft Graph to access:

- SharePoint and OneDrive documents
- Exchange emails and calendar events
- Teams chats and meeting transcripts
- Planner tasks and project data
- Directory information

## ✨ Expectation Specification

The Expectations component answers: **What should the output look like?**

### Expectation Categories

| Category | Options | Example |
|----------|---------|--------|
| **Format** | Bullet points, paragraphs, table, JSON | "Use bullet points" |
| **Length** | Specific word/page count, brief, detailed | "2-3 paragraphs" |
| **Tone** | Formal, casual, persuasive, technical | "Professional and concise" |
| **Structure** | Headings, sections, numbered lists | "Include an executive summary" |
| **Quality** | Draft, polished, review-ready | "Ready for management review" |

### Expectation Examples

```
Format: Executive summary (2 paragraphs) followed by 5 bullet points
Length: Approximately 500 words
Tone: Professional and data-driven
Structure: Introduction, Analysis, Recommendations, Conclusion
Quality: Suitable for board presentation

Format: Step-by-step instructions
Length: Detailed enough for a new team member to follow
Tone: Clear and instructional
Audience: Non-technical staff
Quality: Include examples where helpful
```

## 📝 GCES Prompt Templates

### Basic Template

```
Goal: [What you want to achieve]
Context: [Background, audience, constraints]
Source: [Documents, data, or materials to use]
Expectations: [Format, length, tone, quality requirements]
```

### Example: Word Document

```
Goal: Draft a project charter for the new customer portal initiative
Context: The project is a high priority for the company and needs executive
         approval by end of month. Audience is the executive leadership team.
Source: Use the standard project charter template and reference the requirements
        document shared in the Project Management channel
Expectations: Professional format with clear sections. Approximately 2 pages.
              Include timeline, budget estimate, and risk summary.
```

### Example: Excel Analysis

```
Goal: Analyze the regional sales performance for Q3
Context: We need to identify underperforming regions and prepare for the
         quarterly business review meeting
Source: Q3_Sales_Data.xlsx from the Finance shared drive, including all
        regional breakdowns and product categories
Expectations: Create a summary table with:
              - Total revenue by region
              - Year-over-year growth percentage
              - Top 3 performing products
              - 3 key insights with supporting data
              Format in clear, presentation-ready format
```

### Example: PowerPoint Presentation

```
Goal: Create a 12-slide presentation for the annual company all-hands meeting
Context: This is for all employees. We want to celebrate achievements,
         acknowledge challenges, and inspire enthusiasm for next year.
Source: HR annual report, Finance summary, and customer satisfaction survey results
Expectations: Visually engaging design with minimal text per slide.
              Include speaker notes for each slide.
              Structure: Opening, Company Highlights, Challenges, Strategy,
              Team Recognition, Closing
```

### Example: Teams Meeting Summary

```
Goal: Generate meeting summary with action items
Context: Weekly project sync meeting with the product development team
Source: Today's meeting transcript and any shared documents
Expectations: Include:
              - Key discussion points (bullet format)
              - Decisions made
              - Action items with owners and due dates
              - Open questions to address next meeting
              Tone: Professional, action-oriented
```

### Example: Outlook Email

```
Goal: Draft a response to a customer complaint about delayed delivery
Context: The customer has been waiting 2 weeks for their order.
         We want to apologize and offer a solution.
Source: Customer's original email and order details from the CRM system
Expectations: Professional and empathetic tone
              Acknowledge the issue, apologize, explain the cause,
              and offer a concrete resolution
              Keep it under 200 words
              Ready to send after my review
```

## 🚀 Advanced Framework Techniques

### Sequential Prompting

Break complex tasks into sequential steps:

```
Step 1: First, read and understand the attached research paper

Step 2: Then, extract the 3 main findings and supporting evidence

Step 3: Finally, draft a one-paragraph summary suitable for a
        non-technical executive audience
```

### Iterative Refinement

```
Initial Request: Draft a first version of the project timeline

Refinement: Make the timeline more aggressive to meet the
            compressed deadline

Final Adjustments: Add dependencies and resource requirements
```

### Conditional Logic

```
If the data shows revenue > target:
  - Highlight achievements in green
  - Include expansion recommendations

If the data shows revenue < target:
  - Focus on analysis of shortfalls
  - Prioritize recovery recommendations
```

## 🎓 Application-Specific Frameworks

### Microsoft Word Framework

```
Goal: Create/update [document type]
Context: Purpose, audience, deadline
Source: [Template location, reference documents]
Expectations: Length, format, required sections
Style: [Formal/Casual/Technical]
```

### Microsoft Excel Framework

```
Goal: Analyze/create/visualize [data type]
Context: Business question or problem
Source: [Spreadsheet name, data range]
Expectations: Analysis type, chart requirements, insights needed
Format: [Summary table/Detailed breakdown/Presentation-ready]
```

### Microsoft PowerPoint Framework

```
Goal: Create [presentation type] for [meeting/event]
Context: Audience, key message, time constraints
Source: [Data sources, documents, talking points]
Expectations: Number of slides, design style, include speaker notes
Structure: Opening, Main Content Sections, Closing
```

### Microsoft Teams Framework

```
Goal: [Summarize/Schedule/Prepare for] [meeting/channel discussion]
Context: Meeting topic, participants, urgency
Source: [Meeting transcript, chat history, shared files]
Expectations: Format of summary, action item format
Action Items: Include owners and due dates
```

### Microsoft Outlook Framework

```
Goal: Draft/Reply/Schedule [email/meeting]
Context: Relationship to recipient, urgency, key points
Source: [Reference emails, calendar events, attachments]
Expectations: Tone, length, call-to-action
Follow-up: [Required/not required, timeline]
```

## 📊 Enterprise Best Practices

### Prompt Optimization

1. **Be Specific**: Include exact file names, dates, and references when possible
2. **Set Clear Boundaries**: Define scope to avoid unnecessary content
3. **Provide Context**: Include business justification and strategic alignment
4. **Specify Format**: Indicate exact output structure requirements
5. **Iterate**: Start broad, then refine based on initial results

### Collaboration Workflows

**Review and Refine:**
```
Initial Draft: Copilot generates first version
Human Review: Mark up changes and feedback
Refinement: Copilot incorporates feedback
Final Polish: Human makes final adjustments
```

**Continuous Improvement:**
- Save effective prompts as templates
- Share successful prompts within teams
- Document edge cases and variations
- Track prompt effectiveness over time

### Security Considerations

- **Data Classification**: Be aware of data sensitivity when using organizational data
- **Access Permissions**: Copilot only accesses data the user has permission to view
- **Audit Trail**: Understand what data is being accessed and processed
- **Compliance**: Ensure prompts align with organizational policies
- **Confidentiality**: Avoid including sensitive data directly in prompts

## 🔒 Compliance and Governance

### Data Handling

Microsoft 365 Copilot operates within your organization's security perimeter:

| Capability | Description |
|------------|-------------|
| **Zero Data Retention** | Prompts and responses are not stored or used for AI training |
| **Access Control** | Enforces existing Microsoft 365 permission models |
| **Compliance Boundary** | Data stays within your Microsoft 365 tenant |
| **Audit Logging** | Enterprise-grade logging and reporting available |

### Regulatory Considerations

When using Copilot prompts in regulated industries:

1. **Verify Permissions**: Ensure Copilot has appropriate access to data
2. **Document Processes**: Maintain records of how Copilot is used
3. **Review Outputs**: Human review remains essential for compliance
4. **Train Users**: Ensure users understand responsible AI use

## 📚 Related Documentation

- [Microsoft 365 Copilot Documentation](https://learn.microsoft.com/en-us/microsoft-365/copilot/)
- [Prompting Best Practices](https://learn.microsoft.com/en-us/copilot/microsoft-365/copilot-prompts)
- [Security and Compliance](https://learn.microsoft.com/en-us/compliance//)
- [Microsoft Graph Documentation](https://learn.microsoft.com/en-us/graph/)

## 🔗 Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              GCES FRAMEWORK QUICK REFERENCE                 │
├─────────────────────────────────────────────────────────────┤
│ GOAL      │ What do you want? (Action + Output)            │
│           │ Example: "Summarize the quarterly report"       │
├───────────┼─────────────────────────────────────────────────┤
│ CONTEXT   │ Why and for whom? (Background + Audience)      │
│           │ Example: "For the board meeting, emphasizing"   │
├───────────┼─────────────────────────────────────────────────┤
│ SOURCE    │ What should be used? (Documents + Data)        │
│           │ Example: "Based on Q3_Sales.xlsx and the"       │
├───────────┼─────────────────────────────────────────────────┤
│ EXPECTATION│ How should it look? (Format + Tone + Length)  │
│           │ Example: "3 bullet points, executive tone"     │
└─────────────────────────────────────────────────────────────┘
```
