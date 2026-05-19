# Getting Started with AgentHome
Welcome to AgentHome! This guide will help you get started with building AI agents.

## Prerequisites

- Node.js (v18+) or Python (3.10+)
- Git
- OpenAI API key (or other LLM provider)

## Installation

```bash
# Clone the repository
git clone https://github.com/badhope/AgentHome.git
cd AgentHome

# Choose a template
cp -r templates/agent-starter my-first-agent
cd my-first-agent
```

## Creating Your First Agent

### Step 1: Install Dependencies

```bash
npm install
# or
pip install -r requirements.txt
```

### Step 2: Configure Environment

```env
# .env file
AGENT_NAME=MyFirstAgent
LLM_PROVIDER=openai
OPENAI_API_KEY=your-api-key-here
```

### Step 3: Run the Agent

```bash
npm run start
# or
python main.py
```

## Next Steps

1. Explore the [frameworks](../frameworks/) directory
2. Check out [production projects](../projects/)
3. Try different [templates](../templates/)
4. Read the [API documentation](api-reference/)
