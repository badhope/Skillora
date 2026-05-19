# API Reference
Application Programming Interface documentation.

## Modules

### Framework APIs
- [LangChain API](langchain.md)
- [LlamaIndex API](llamaindex.md)
- [Agent Protocol](agent-protocol.md)

### Tool APIs
- [Prompt Engine API](prompt-engine.md)
- [Vector Store API](vector-store.md)
- [Connectors API](connectors.md)

### Project APIs
- [Chat Agent API](chat-agent.md)
- [Task Agent API](task-agent.md)
- [Research Agent API](research-agent.md)

## Authentication

All APIs require authentication via API key:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.agenthome.dev/v1/agents
```

## Rate Limits

- Free tier: 100 requests/day
- Pro tier: 10,000 requests/day
- Enterprise: Custom limits

## Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Internal Server Error |
