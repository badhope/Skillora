import faiss
import numpy as np
from typing import List, Any, Optional

class FAISSWrapper:
    def __init__(self, dimension: int = 1536):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add_documents(self, embeddings: List[np.ndarray], documents: List[Any]):
        if len(embeddings) != len(documents):
            raise ValueError("Embeddings and documents must have the same length")
        
        embeddings_np = np.array(embeddings).astype('float32')
        self.index.add(embeddings_np)
        self.documents.extend(documents)

    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[tuple]:
        query_np = np.array([query_embedding]).astype('float32')
        distances, indices = self.index.search(query_np, k)
        
        results = []
        for i in range(k):
            if indices[0][i] < len(self.documents):
                results.append((self.documents[indices[0][i]], distances[0][i]))
        
        return results

    def save(self, filepath: str):
        faiss.write_index(self.index, filepath + ".index")
        np.save(filepath + "_documents.npy", np.array(self.documents, dtype=object))

    @classmethod
    def load(cls, filepath: str) -> 'FAISSWrapper':
        wrapper = cls()
        wrapper.index = faiss.read_index(filepath + ".index")
        wrapper.documents = list(np.load(filepath + "_documents.npy", allow_pickle=True))
        return wrapper

    def get_stats(self) -> dict:
        return {
            "total_documents": len(self.documents),
            "dimension": self.dimension,
            "index_size": self.index.ntotal
        }