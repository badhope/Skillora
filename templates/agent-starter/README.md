# Agent Starter Template
Basic template for creating AI agents.

## Features

- Basic agent structure
- Configuration management
- Logging setup
- Health check endpoints

## Quick Start

```bash
# Copy template
cp -r templates/agent-starter my-agent
cd my-agent

# Install dependencies
npm install

# Start agent
npm run start
```

## Project Structure

```
my-agent/
├── src/
│   ├── agent.ts          # Agent implementation
│   ├── config.ts         # Configuration
│   ├── handlers/         # Request handlers
│   └── utils/            # Utilities
├── tests/                # Test files
├── .env                  # Environment variables
└── package.json          # Dependencies
```

## Configuration

```env
AGENT_NAME=MyAgent
LLM_PROVIDER=openai
OPENAI_API_KEY=your-api-key
```
