# Knowledge Base
Knowledge management system for AI agents.

## Features

- Document ingestion
- Semantic search
- Knowledge graph construction
- Context management

## Quick Start

```typescript
import { KnowledgeBase } from './knowledge-base';

const kb = new KnowledgeBase();

await kb.ingest('documents/');
const context = await kb.retrieve('What is LangChain?', { maxTokens: 2000 });
```

## Modules

- `ingestion/` - Document ingestion
- `retrieval/` - Context retrieval
- `graph/` - Knowledge graph
- `storage/` - Persistence layer
