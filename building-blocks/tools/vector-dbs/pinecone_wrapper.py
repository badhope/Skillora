"""Pinecone 向量数据库包装

Pinecone 是一个托管的向量数据库服务，适合生产环境使用。

使用示例:
    from pinecone_wrapper import PineconeWrapper
    
    db = PineconeWrapper(api_key="...", index="my-index")
    db.upsert([("id1", [0.1, 0.2], {"text": "文档1"})])
    results = db.query([0.1, 0.2], top_k=3)
"""

import os
from typing import List, Dict, Any, Optional

try:
    import pinecone
except ImportError:
    print("需要安装 pinecone-client: pip install pinecone-client")
    pinecone = None


class PineconeWrapper:
    """Pinecone 向量数据库包装类
    
    这是一个简化版的 Pinecone 封装。
    
    Args:
        api_key: Pinecone API Key
        index_name: 索引名称
        environment: 环境，默认为 "us-east-1-aws"
        dimension: 向量维度，默认为 1536
        
    使用示例:
        db = PineconeWrapper(api_key="...", index="my-index")
        db.upsert([("id1", [0.1, 0.2], {"text": "文档1"})])
        results = db.query([0.1, 0.2], top_k=3)
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        index_name: str = "default",
        environment: str = "us-east-1-aws",
        dimension: int = 1536
    ):
        if pinecone is None:
            raise ImportError("请先安装 pinecone-client: pip install pinecone-client")
        
        api_key = api_key or os.getenv("PINECONE_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key 或设置 PINECONE_API_KEY 环境变量")
        
        self.api_key = api_key
        self.index_name = index_name
        self.environment = environment
        self.dimension = dimension
        
        # 初始化 Pinecone
        pinecone.init(api_key=api_key, environment=environment)
        
        # 获取或创建索引
        self.index = self._get_or_create_index()
    
    def _get_or_create_index(self):
        """获取或创建索引"""
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(
                index_name,
                dimension=self.dimension,
                metric="cosine"
            )
        
        return pinecone.Index(index_name)
    
    def upsert(
        self,
        vectors: List[tuple]
    ) -> None:
        """插入或更新向量
        
        Args:
            vectors: 向量列表，每个元素为 (id, vector, metadata) 元组
        """
        self.index.upsert(vectors=vectors)
    
    def query(
        self,
        vector: List[float],
        top_k: int = 10,
        filter_dict: Optional[Dict] = None,
        include_metadata: bool = True
    ) -> Dict[str, Any]:
        """查询相似向量
        
        Args:
            vector: 查询向量
            top_k: 返回结果数
            filter_dict: 过滤条件
            include_metadata: 是否包含元数据
            
        Returns:
            查询结果
        """
        return self.index.query(
            vector=vector,
            top_k=top_k,
            filter=filter_dict,
            include_metadata=include_metadata
        )
    
    def fetch(self, ids: List[str]) -> Dict[str, Any]:
        """获取指定 ID 的向量
        
        Args:
            ids: ID 列表
            
        Returns:
            向量数据
        """
        return self.index.fetch(ids=ids)
    
    def delete(
        self,
        ids: Optional[List[str]] = None,
        delete_all: bool = False,
        filter_dict: Optional[Dict] = None
    ) -> None:
        """删除向量
        
        Args:
            ids: ID 列表
            delete_all: 删除所有
            filter_dict: 过滤条件
        """
        if delete_all:
            self.index.delete(delete_all=True)
        elif ids:
            self.index.delete(ids=ids)
        elif filter_dict:
            self.index.delete(filter=filter_dict)
    
    def describe_index_stats(self) -> Dict[str, Any]:
        """获取索引统计信息"""
        return self.index.describe_index_stats()


# 使用示例
if __name__ == "__main__":
    print("=== Pinecone 向量数据库示例 ===\n")
    
    print("注意：需要有效的 Pinecone API Key 才能运行\n")
    
    # 示例：
    # db = PineconeWrapper(api_key="your-key", index_name="test")
    # db.upsert([("id1", [0.1] * 1536, {"text": "文档1"})])
    # results = db.query([0.1] * 1536, top_k=3)
    # print(f"结果: {results}")
