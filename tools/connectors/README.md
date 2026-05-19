# Connectors
External service connectors for AI agents.

## Available Connectors

| Service | Category | Status |
|---------|----------|--------|
| GitHub | Code | ✅ |
| Slack | Communication | ✅ |
| Notion | Productivity | ✅ |
| Gmail | Email | ✅ |
| Calendar | Scheduling | 🚧 |
| Trello | Project Management | ✅ |

## Quick Start

```typescript
import { GitHubConnector, SlackConnector } from './connectors';

const github = new GitHubConnector({ token: process.env.GITHUB_TOKEN });
const repos = await github.getRepositories('badhope');

const slack = new SlackConnector({ token: process.env.SLACK_TOKEN });
await slack.sendMessage('#general', 'Hello from Agent!');
```

## Modules

- `github/` - GitHub integration
- `slack/` - Slack integration
- `notion/` - Notion integration
- `email/` - Email connectors
