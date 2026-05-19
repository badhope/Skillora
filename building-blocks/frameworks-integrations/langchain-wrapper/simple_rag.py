"""LangChain RAG 模块

基于 LangChain 的检索增强生成（RAG）实现。

使用示例:
    from langchain_wrapper import SimpleRAG
    
    rag = SimpleRAG(api_key="...")
    rag.add_documents(["文档1", "文档2"])
    result = rag.query("问题")
"""

import os
from typing import Optional, List, Dict, Any

try:
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import Chroma
    from langchain.chains import RetrievalQA
    from langchain.prompts import PromptTemplate
except ImportError:
    print("需要安装: pip install langchain langchain-openai langchain-community")
    OpenAIEmbeddings = None


class SimpleRAG:
    """简单的 RAG 类
    
    基于 LangChain 的检索增强生成实现。
    
    Args:
        api_key: OpenAI API Key
        model_name: 模型名称，默认为 "gpt-4"
        embedding_model: 嵌入模型，默认为 "text-embedding-ada-002"
        persist_directory: 向量数据库持久化目录
        
    使用示例:
        rag = SimpleRAG(api_key="...")
        rag.add_documents(["关于 Python 的文档", "关于 JavaScript 的文档"])
        result = rag.query("Python 和 JavaScript 有什么区别？")
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gpt-4",
        embedding_model: str = "text-embedding-ada-002",
        persist_directory: Optional[str] = None
    ):
        if OpenAIEmbeddings is None:
            raise ImportError("请先安装: pip install langchain langchain-openai langchain-community")
            
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key 或设置 OPENAI_API_KEY 环境变量")
        
        # 初始化 LLM
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=0,
            api_key=api_key
        )
        
        # 初始化嵌入模型
        self.embeddings = OpenAIEmbeddings(
            model=embedding_model,
            api_key=api_key
        )
        
        # 文本分割器
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )
        
        # 向量存储
        self.persist_directory = persist_directory
        self.vectorstore = None
        self.retriever = None
        
        # QA 链
        self.qa_chain = None
        
        # 默认提示词
        self.prompt_template = PromptTemplate(
            template="""使用以下上下文来回答问题。如果上下文中没有相关信息，请说明你不知道。

上下文:
{context}

问题: {question}

回答:""",
            input_variables=["context", "question"]
        )
    
    def add_documents(self, documents: List[str], metadatas: Optional[List[Dict]] = None) -> None:
        """添加文档
        
        Args:
            documents: 文档列表
            metadatas: 可选的元数据列表
        """
        # 分割文档
        texts = self.text_splitter.create_documents(documents, metadatas=metadatas)
        
        # 创建或更新向量存储
        if self.vectorstore is None:
            self.vectorstore = Chroma.from_documents(
                documents=texts,
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )
        else:
            self.vectorstore.add_documents(texts)
        
        # 重新创建检索器
        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 3}
        )
        
        # 重新创建 QA 链
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt_template}
        )
    
    def query(self, question: str, k: int = 3) -> Dict[str, Any]:
        """查询
        
        Args:
            question: 问题
            k: 检索的文档数
            
        Returns:
            包含答案和相关文档的字典
        """
        if not self.qa_chain:
            return {
                "result": "请先添加文档",
                "source_documents": []
            }
        
        result = self.qa_chain({"query": question})
        
        return {
            "result": result["result"],
            "source_documents": result.get("source_documents", [])
        }
    
    def query_with_source(self, question: str, k: int = 3) -> str:
        """查询并返回带来源的结果
        
        Args:
            question: 问题
            k: 检索的文档数
            
        Returns:
            带来源的答案
        """
        result = self.query(question, k)
        
        # 格式化输出
        output = result["result"]
        
        if result["source_documents"]:
            output += "\n\n参考来源:\n"
            for i, doc in enumerate(result["source_documents"], 1):
                content = doc.page_content[:100]
                output += f"{i}. {content}...\n"
        
        return output
    
    def similarity_search(self, query: str, k: int = 3) -> List[Any]:
        """相似性搜索
        
        Args:
            query: 查询文本
            k: 返回结果数
            
        Returns:
            相似文档列表
        """
        if not self.vectorstore:
            return []
        
        return self.vectorstore.similarity_search(query, k=k)
    
    def delete_collection(self) -> None:
        """删除向量集合"""
        if self.vectorstore:
            self.vectorstore.delete_collection()
            self.vectorstore = None
            self.retriever = None
            self.qa_chain = None


# 使用示例
if __name__ == "__main__":
    print("=== LangChain RAG 示例 ===\n")
    
    # 示例文档
    documents = [
        "Python 是一种高级编程语言，由 Guido van Rossum 创建。",
        "Python 支持多种编程范式，包括面向对象、函数式和过程式编程。",
        "JavaScript 是一种脚本语言，主要用于网页开发。",
        "JavaScript 可以在浏览器中运行，也可以在服务器端使用 Node.js 运行。"
    ]
    
    print("创建 RAG 系统...")
    rag = SimpleRAG()
    
    print("添加文档...")
    rag.add_documents(documents)
    
    print("\n查询...")
    result = rag.query_with_source("Python 是什么？")
    print(f"结果:\n{result}")
