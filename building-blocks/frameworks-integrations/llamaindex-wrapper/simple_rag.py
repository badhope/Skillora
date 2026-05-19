"""LlamaIndex RAG 模块

基于 LlamaIndex 的检索增强生成（RAG）实现。

使用示例:
    from llamaindex_wrapper import SimpleRAG
    
    rag = SimpleRAG(api_key="...")
    rag.load_documents("data/")  # 或传入字符串列表
    result = rag.query("问题")
"""

import os
from typing import Optional, List, Dict, Any

try:
    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Document
    from llama_index.core.retrievers import VectorIndexRetriever
    from llama_index.core.query_engine import RetrieverQueryEngine
    from llama_index.llms.openai import OpenAI
except ImportError:
    print("需要安装: pip install llama-index llama-index-llms-openai")
    VectorStoreIndex = None


class SimpleRAG:
    """简单的 RAG 类
    
    基于 LlamaIndex 的检索增强生成实现。
    
    Args:
        api_key: OpenAI API Key
        model_name: 模型名称，默认为 "gpt-4"
        
    使用示例:
        rag = SimpleRAG(api_key="...")
        rag.load_documents(["文档1", "文档2"])
        result = rag.query("问题")
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gpt-4"
    ):
        if VectorStoreIndex is None:
            raise ImportError("请先安装: pip install llama-index llama-index-llms-openai")
            
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key 或设置 OPENAI_API_KEY 环境变量")
        
        # 初始化 LLM
        self.llm = OpenAI(
            model=model_name,
            api_key=api_key
        )
        
        # 索引和查询引擎
        self.index = None
        self.query_engine = None
        self.documents: List[Document] = []
    
    def load_documents_from_strings(
        self,
        texts: List[str],
        metadatas: Optional[List[Dict]] = None
    ) -> None:
        """从字符串列表加载文档
        
        Args:
            texts: 文档文本列表
            metadatas: 可选的元数据列表
        """
        documents = []
        for i, text in enumerate(texts):
            metadata = metadatas[i] if metadatas and i < len(metadatas) else {}
            doc = Document(text=text, metadata=metadata)
            documents.append(doc)
        
        self.documents.extend(documents)
        self._build_index()
    
    def load_documents_from_directory(
        self,
        directory: str,
        extensions: Optional[List[str]] = None
    ) -> None:
        """从目录加载文档
        
        Args:
            directory: 目录路径
            extensions: 文件扩展名列表，如 [".txt", ".pdf", ".md"]
        """
        reader = SimpleDirectoryReader(
            directory,
            file_extensions=extensions
        )
        documents = reader.load_data()
        self.documents.extend(documents)
        self._build_index()
    
    def _build_index(self) -> None:
        """构建索引"""
        if not self.documents:
            return
        
        self.index = VectorStoreIndex.from_documents(self.documents)
        self.query_engine = self.index.as_query_engine(
            llm=self.llm
        )
    
    def query(self, question: str) -> str:
        """查询
        
        Args:
            question: 问题
            
        Returns:
            答案
        """
        if not self.query_engine:
            return "请先加载文档"
        
        response = self.query_engine.query(question)
        return str(response)
    
    def retrieve(self, query: str, top_k: int = 3) -> List[Any]:
        """检索相关文档
        
        Args:
            query: 查询文本
            top_k: 返回结果数
            
        Returns:
            相关文档列表
        """
        if not self.index:
            return []
        
        retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=top_k
        )
        
        nodes = retriever.retrieve(query)
        return nodes
    
    def get_document_count(self) -> int:
        """获取文档数量"""
        return len(self.documents)
    
    def clear_documents(self) -> None:
        """清空文档"""
        self.documents = []
        self.index = None
        self.query_engine = None


# 使用示例
if __name__ == "__main__":
    print("=== LlamaIndex RAG 示例 ===\n")
    
    # 示例文档
    documents = [
        "Python 是一种高级编程语言。",
        "Python 广泛应用于数据分析、人工智能和 Web 开发。",
        "JavaScript 主要用于网页前端开发。",
        "TypeScript 是 JavaScript 的类型化超集。"
    ]
    
    print("创建 RAG 系统...")
    rag = SimpleRAG()
    
    print("加载文档...")
    rag.load_documents_from_strings(documents)
    
    print(f"已加载 {rag.get_document_count()} 个文档\n")
    
    print("查询...")
    result = rag.query("Python 有什么应用？")
    print(f"结果: {result}")
