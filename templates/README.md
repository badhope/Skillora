# Templates
Project templates for quick agent development.

## Available Templates

| Template | Description | Use Case |
|----------|-------------|----------|
| agent-starter | Basic agent template | Simple chatbot |
| multi-agent | Multi-agent system | Collaborative agents |
| rag-system | RAG application | Knowledge-based QA |

## Usage

```bash
# Create a new agent from template
cp -r templates/agent-starter my-new-agent
cd my-new-agent
npm install
```

## Template Structure

```
template/
├── src/              # Source code
├── config/           # Configuration
├── tests/            # Test files
└── package.json      # Dependencies
```
