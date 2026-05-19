# Agent Protocol
Lightweight communication protocol for AI agents.

## Features

- RESTful API for agent communication
- WebSocket support for real-time interactions
- Message routing and dispatching
- Status tracking and monitoring

## Protocol Specification

### Message Format
```json
{
  "id": "message-uuid",
  "type": "task",
  "content": {
    "action": "execute",
    "parameters": {}
  },
  "metadata": {
    "timestamp": "2024-01-01T00:00:00Z",
    "agent_id": "agent-123"
  }
}
```

## Modules

- `server/` - Protocol server implementation
- `client/` - Client SDK
- `messages/` - Message schemas
- `routing/` - Message routing logic
