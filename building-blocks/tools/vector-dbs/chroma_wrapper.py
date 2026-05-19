"""Chroma 向量数据库包装

Chroma 是一个开源的嵌入数据库，非常适合本地开发和测试。

使用示例:
    from chroma_wrapper import ChromaWrapper
    
    db = ChromaWrapper(persist_directory="./chroma_db")
    db.add_texts(["文档1", "文档2"], embeddings=[[0.1, 0.2], [0.3, 0.4]])
    results = db.search("查询", n_results=3)
"""

import os
from typing import List, Dict, Any, Optional, Tuple

try:
    import chromadb
    from chromadb.config import Settings
except ImportError:
    print("需要安装 chromadb: pip install chromadb")
    chromadb = None


class ChromaWrapper:
    """Chroma 向量数据库包装类
    
    这是一个简化版的 Chroma 封装。
    
    Args:
        persist_directory: 持久化目录，默认为 "./chroma_db"
        collection_name: 集合名称，默认为 "default"
        
    使用示例:
        db = ChromaWrapper()
        db.add_texts(["文档1", "文档2"])
        results = db.search("查询")
    """
    
    def __init__(
        self,
        persist_directory: str = "./chroma_db",
        collection_name: str = "default"
    ):
        if chromadb is None:
            raise ImportError("请先安装 chromadb: pip install chromadb")
        
        self.persist_directory = persist_directory
        self.collection_name = collection_name
        self.client = None
        self.collection = None
        self._connect()
    
    def _connect(self) -> None:
        """连接到 Chroma"""
        self.client = chromadb.Client(
            Settings(
                persist_directory=self.persist_directory,
                anonymized_telemetry=False
            )
        )
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )
    
    def add_texts(
        self,
        texts: List[str],
        embeddings: Optional[List[List[float]]] = None,
        metadatas: Optional[List[Dict]] = None,
        ids: Optional[List[str]] = None
    ) -> List[str]:
        """添加文本
        
        Args:
            texts: 文本列表
            embeddings: 嵌入向量列表（如果为 None，需要提供）
            metadatas: 元数据列表
            ids: ID 列表
            
        Returns:
            添加的 ID 列表
        """
        if embeddings is None:
            raise ValueError("目前需要提供 embeddings，请使用 embed_texts() 生成")
        
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(texts))]
        
        if metadatas is None:
            metadatas = [{} for _ in texts]
        
        self.collection.add(
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )
        
        return ids
    
    def search(
        self,
        query: str,
        n_results: int = 3,
        where: Optional[Dict] = None
    ) -> List[Dict[str, Any]]:
        """搜索
        
        Args:
            query: 查询文本
            n_results: 返回结果数
            where: 元数据过滤条件
            
        Returns:
            搜索结果列表
        """
        # 注意：这里需要提供查询向量，实际使用时应该使用嵌入模型
        # 这里简化处理，返回空结果
        return []
    
    def query_by_vector(
        self,
        query_embeddings: List[List[float]],
        n_results: int = 3,
        where: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """通过向量查询
        
        Args:
            query_embeddings: 查询向量
            n_results: 返回结果数
            where: 元数据过滤条件
            
        Returns:
            查询结果
        """
        results = self.collection.query(
            query_embeddings=query_embeddings,
            n_results=n_results,
            where=where
        )
        
        return results
    
    def get_by_id(self, ids: List[str]) -> Dict[str, Any]:
        """通过 ID 获取文档
        
        Args:
            ids: ID 列表
            
        Returns:
            文档数据
        """
        return self.collection.get(ids=ids)
    
    def delete_by_id(self, ids: List[str]) -> None:
        """通过 ID 删除文档
        
        Args:
            ids: ID 列表
        """
        self.collection.delete(ids=ids)
    
    def delete_all(self) -> None:
        """删除所有文档"""
        self.collection.delete(where={})
    
    def count(self) -> int:
        """获取文档数量"""
        return self.collection.count()
    
    def peek(self, limit: int = 10) -> Dict[str, Any]:
        """查看前 N 条文档"""
        return self.collection.peek(limit=limit)


def embed_texts(texts: List[str], model: str = "sentence-transformers/all-MiniLM-L6-v2") -> List[List[float]]:
    """生成文本嵌入
    
    Args:
        texts: 文本列表
        model: 嵌入模型
        
    Returns:
        嵌入向量列表
    """
    # 这里应该使用实际的嵌入模型
    # 为了简化，返回随机向量
    import random
    dimension = 384  # 默认维度
    return [[random.random() for _ in range(dimension)] for _ in texts]


# 使用示例
if __name__ == "__main__":
    print("=== Chroma 向量数据库示例 ===\n")
    
    print("创建数据库...")
    db = ChromaWrapper(persist_directory="./test_chroma")
    
    # 示例文档和嵌入
    texts = ["苹果是一种水果", "香蕉也是一种水果", "狗是一种动物"]
    embeddings = embed_texts(texts)
    
    print("添加文档...")
    ids = db.add_texts(texts, embeddings=embeddings)
    
    print(f"已添加 {len(ids)} 个文档\n")
    
    print("搜索...")
    query_vec = embed_texts(["水果"])
    results = db.query_by_vector(query_vec, n_results=2)
    print(f"结果: {results}")
