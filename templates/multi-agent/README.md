# Multi-Agent Template
Template for building multi-agent systems.

## Features

- Agent coordination
- Task delegation
- Communication channels
- Performance monitoring

## Quick Start

```bash
# Copy template
cp -r templates/multi-agent my-multi-agent
cd my-multi-agent

# Install dependencies
npm install

# Start agents
npm run start
```

## Architecture

```
┌─────────────────────────────────────────────┐
│              Orchestrator                   │
├──────────────┬──────────────┬──────────────┤
│   Agent A    │   Agent B    │   Agent C    │
│  (Specialist)│  (Generalist)│  (Expert)    │
└──────────────┴──────────────┴──────────────┘
```

## Project Structure

```
my-multi-agent/
├── src/
│   ├── orchestrator.ts    # Coordinator
│   ├── agents/            # Agent implementations
│   ├── channels/          # Communication channels
│   └── monitor/           # Monitoring
├── tests/
├── .env
└── package.json
```
