# LlamaIndex Framework
LlamaIndex utilities for data-centric LLM applications.

## Features

- Document loaders and parsers
- Index construction utilities
- Query engines with RAG support
- Vector store integrations

## Quick Start

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data/").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What is AI?")
print(response)
```

## Modules

- `loaders/` - Document loaders
- `indices/` - Index construction
- `query/` - Query engines
- `storage/` - Storage utilities
