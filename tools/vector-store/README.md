# Vector Store
Unified interface for vector database integrations.

## Supported Databases

| Database | Status |
|----------|--------|
| Pinecone | ✅ |
| Chroma | ✅ |
| FAISS | ✅ |
| Milvus | ✅ |
| Weaviate | 🚧 |

## Quick Start

```typescript
import { VectorStore } from './vector-store';

const store = new VectorStore({
  provider: 'pinecone',
  apiKey: process.env.PINECONE_API_KEY
});

await store.connect();
await store.insert('document-id', [0.1, 0.2, 0.3], { title: 'AI Agents' });
const results = await store.query([0.1, 0.2, 0.3], { topK: 5 });
```

## Modules

- `providers/` - Database providers
- `index/` - Index management
- `query/` - Query utilities
- `schema/` - Data schemas
