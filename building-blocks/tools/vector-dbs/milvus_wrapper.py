from pymilvus import (
    connections,
    Collection,
    FieldSchema,
    CollectionSchema,
    DataType,
    utility
)
from typing import List, Any, Optional

class MilvusWrapper:
    def __init__(
        self,
        host: str = "localhost",
        port: str = "19530",
        collection_name: str = "agent_home"
    ):
        self.host = host
        self.port = port
        self.collection_name = collection_name
        self._connect()
        self._create_collection_if_not_exists()

    def _connect(self):
        if not connections.has_connection("default"):
            connections.connect(
                alias="default",
                host=self.host,
                port=self.port
            )

    def _create_collection_if_not_exists(self):
        if not utility.has_collection(self.collection_name):
            fields = [
                FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
                FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1536),
                FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=65535)
            ]
            schema = CollectionSchema(fields, description="AgentHome vector store")
            self.collection = Collection(self.collection_name, schema)
            
            index_params = {
                "index_type": "IVF_FLAT",
                "metric_type": "L2",
                "params": {"nlist": 1024}
            }
            self.collection.create_index("embedding", index_params)
        else:
            self.collection = Collection(self.collection_name)

    def add_documents(self, embeddings: List[List[float]], contents: List[str]):
        if len(embeddings) != len(contents):
            raise ValueError("Embeddings and contents must have the same length")
        
        entities = [
            {"embedding": emb, "content": content}
            for emb, content in zip(embeddings, contents)
        ]
        
        self.collection.insert(entities)
        self.collection.flush()

    def search(
        self,
        query_embedding: List[float],
        k: int = 5,
        filters: Optional[str] = None
    ) -> List[tuple]:
        self.collection.load()
        
        search_params = {
            "metric_type": "L2",
            "params": {"nprobe": 10}
        }
        
        results = self.collection.search(
            data=[query_embedding],
            anns_field="embedding",
            param=search_params,
            limit=k,
            expr=filters,
            output_fields=["content"]
        )
        
        output = []
        for hit in results[0]:
            output.append((hit.entity.get("content"), hit.distance))
        
        self.collection.release()
        return output

    def delete(self, expr: str):
        self.collection.delete(expr)
        self.collection.flush()

    def count(self) -> int:
        return self.collection.num_entities

    def drop(self):
        if utility.has_collection(self.collection_name):
            utility.drop_collection(self.collection_name)