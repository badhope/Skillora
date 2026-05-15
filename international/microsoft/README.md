# Microsoft Copilot Prompts

Comprehensive collection of prompts optimized for Microsoft Copilot, including Microsoft 365 Copilot, Bing Chat Enterprise, and Windows Copilot integration.

## 📑 Index

- [Microsoft 365 Copilot Framework](./copilot-framework.md)
- [Microsoft 365 Apps Prompts](./m365-prompts.md)

## 🔗 Official Resources

- [Microsoft Copilot Documentation](https://learn.microsoft.com/en-us/copilot/)
- [Microsoft 365 Copilot Documentation](https://learn.microsoft.com/en-us/microsoft-365/copilot/)
- [Microsoft Copilot in Windows](https://learn.microsoft.com/en-us/windows/copilot/)
- [Bing Chat Enterprise](https://learn.microsoft.com/en-us/microsoft-365/copilot/bing-chat-enterprise)
- [Microsoft Copilot for Sales](https://learn.microsoft.com/en-us/copilot/sales/)
- [Microsoft Copilot for Service](https://learn.microsoft.com/en-us/copilot/customer-service/)

## 🎯 Quick Reference

### Copilot Product Family

| Product | Primary Use Case | Context |
|---------|------------------|---------|
| Microsoft 365 Copilot | Workplace productivity | Integrates with Word, Excel, PowerPoint, Teams, Outlook, and more |
| Bing Chat Enterprise | General web and work search | Web search with commercial data protection |
| Windows Copilot | System-level assistance | Windows 11 integration for system settings and actions |
| Copilot in Edge | Web browsing assistance | Sidebar integration in Microsoft Edge |
| Copilot for Sales | Sales productivity | Integrates with CRM and sales tools |
| Copilot for Service | Customer service | Agent assistance for service desk scenarios |

### Microsoft 365 Copilot Apps

| Application | Key Capabilities |
|-------------|------------------|
| Word | Draft, summarize, rewrite documents |
| Excel | Analyze data, create formulas, generate charts |
| PowerPoint | Create presentations from content, design suggestions |
| Teams | Meeting summaries, chat assistance, recaps |
| Outlook | Email drafting, inbox management, scheduling |
| OneNote | Meeting notes, research synthesis |
| Loop | Collaborative workspace assistance |

## 📊 Prompt Structure

Microsoft 365 Copilot prompts typically follow a structured format:

```
[Action/Verb] + [Subject/Topic] + [Context/Format] + [Audience/Recipient]
```

### Example Patterns

**Basic Pattern:**
```
Summarize the key points from this document
```

**Extended Pattern:**
```
Create a 5-slide presentation summarizing the Q3 sales report.
The presentation should be suitable for executive leadership.
Include: revenue trends, regional performance, and recommendations.
```

**Framework-Based Pattern (GCES):**
```
Goal: What do you want to achieve?
Context: What background information is needed?
Source: What data/files should be referenced?
Expectations: What format and tone should the output have?
```

## 🔥 Popular Prompts

### Document Creation

```
Draft a project proposal for [project name] based on the meeting
notes in [document location]. Include timeline, budget estimates,
and risk assessment sections.
```

```
Create a professional email response to [customer inquiry] that:
- Acknowledges their concerns
- Provides a solution
- Maintains a helpful tone
```

### Data Analysis

```
Analyze the sales data in [spreadsheet] and identify:
- Top 5 performing products
- Underperforming regions
- Seasonal trends
- Recommendations for improvement
```

### Meeting Management

```
Summarize the key decisions and action items from today's
[Team Name] meeting. Assign owners to each action item.
```

### Content Summarization

```
Provide a concise summary of [document/article] highlighting:
- Main conclusions
- Key supporting evidence
- Implications for [your team/project]
```

## 🔧 Advanced Techniques

### Chain-of-Thought Prompting

```
First, identify the main topic and scope of [document].
Then, extract the 3 most important findings.
Finally, suggest 2-3 actionable recommendations based on these findings.
```

### Role-Based Prompting

```
As a financial analyst, review [document] and provide:
1. Risk assessment
2. Compliance review
3. Recommendations for management
```

### Comparative Analysis

```
Compare [Document A] and [Document B] to identify:
- Areas of alignment
- Conflicts or contradictions
- Gaps in coverage
```

## 📱 Microsoft 365 Copilot Availability

### Licensing Requirements

| Product | Minimum License |
|---------|-----------------|
| Microsoft 365 Copilot | Microsoft 365 E3/E5, Office 365 E3/E5 |
| Bing Chat Enterprise | Microsoft 365 E3/E5, Business Standard/Premium |
| Windows Copilot | Windows 11 with Copilot |

### Enterprise Features

- **Commercial Data Protection**: Chat data is not stored or used for AI training
- **Grounded in Microsoft Graph**: Access to organizational data with permissions
- **Enterprise Search**: Natural language queries across SharePoint, OneDrive, and other sources
- **Compliance Integration**: Works within existing Microsoft Purview policies

## 🔒 Security and Compliance

Microsoft 365 Copilot inherits enterprise security features:

- **Data Security**: Built on Microsoft 365's comprehensive security model
- **Privacy**: Individual user data is protected under Microsoft's privacy commitments
- **Compliance**: Supports regulatory requirements including GDPR, HIPAA, SOC, and more
- **Access Control**: Integrated with Azure Active Directory and Microsoft Purview
- **Audit Capabilities**: Activity logging and reporting through Microsoft Purview

## 🤝 Related Collections

- [OpenAI Prompts](../openai/README.md)
- [Anthropic Prompts](../anthropic/README.md)
- [Google Gemini Prompts](../google/README.md)

## 📚 Additional Resources

- [Microsoft Learn - Copilot](https://learn.microsoft.com/en-us/training/copilot/)
- [Microsoft 365 Copilot Community](https://techcommunity.microsoft.com/t5/microsoft-365-copilot/bd-p/M365Copilot)
- [Copilot Adoption Resources](https://adoption.microsoft.com/copilot/)

## Contributing

Please follow the contribution guidelines in the main README when adding new prompts.
