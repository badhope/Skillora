"""简单 RAG 模块

这个模块提供了简单的检索增强生成（RAG）功能，可以从文档中检索信息并回答问题。

使用示例:
    from building_blocks.capabilities.rag.simple_rag import SimpleRAG
    from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper
    
    llm = OpenAIWrapper()
    rag = SimpleRAG(llm=llm)
    rag.add_document("文件路径或文本")
    response = rag.query("问题")
"""

from typing import Optional, List
from ..tools.llm_wrappers.openai_wrapper import OpenAIWrapper
from ..tools.memory.buffer_memory import BufferMemory


class SimpleRAG:
    """简单 RAG 类
    
    提供基本的检索增强生成功能。
    
    Args:
        llm: LLM 包装实例
        memory: 可选的记忆模块
        system_prompt: 系统提示词
        
    使用示例:
        llm = OpenAIWrapper()
        rag = SimpleRAG(llm=llm)
        rag.add_document("文档1")
        rag.add_document("文档2")
        response = rag.query("问题")
    """
    
    def __init__(
        self,
        llm: Optional[OpenAIWrapper] = None,
        memory: Optional[BufferMemory] = None,
        system_prompt: Optional[str] = None
    ):
        self.llm = llm or OpenAIWrapper()
        self.memory = memory or BufferMemory()
        self.documents: List[str] = []
        self.system_prompt = system_prompt or (
            "你是一个问答助手。请根据以下文档回答问题。"
            "如果答案在文档中找不到，请诚实说明。"
        )
    
    def add_document(self, content: str, source: Optional[str] = None) -> None:
        """添加文档
        
        Args:
            content: 文档内容
            source: 可选的文档来源
        """
        if source:
            self.documents.append(f"来源: {source}\n{content}")
        else:
            self.documents.append(content)
    
    def add_documents_from_list(self, documents: List[str]) -> None:
        """从列表批量添加文档
        
        Args:
            documents: 文档列表
        """
        self.documents.extend(documents)
    
    def query(self, question: str, max_documents: int = 3) -> str:
        """查询回答
        
        Args:
            question: 用户的问题
            max_documents: 检索的文档数（这里简化为使用所有文档）
            
        Returns:
            回答
        """
        # 构建提示词
        context = "\n\n".join(self.documents[-max_documents:])  # 简单地使用最近的文档
        
        prompt = f"""请根据以下文档回答问题：
        
文档:
{context}

问题: {question}

请根据文档内容回答问题。"""
        
        # 调用 LLM
        response = self.llm.generate(prompt, system_prompt=self.system_prompt)
        
        # 保存到记忆
        self.memory.add_message("user", question)
        self.memory.add_message("assistant", response)
        
        return response
    
    def clear_documents(self) -> None:
        """清空文档"""
        self.documents = []
    
    def get_document_count(self) -> int:
        """获取文档数量"""
        return len(self.documents)


# 使用示例
if __name__ == "__main__":
    print("=== 简单 RAG 使用示例 ===")
    
    # 1. 创建 LLM 和 RAG
    llm = OpenAIWrapper()
    rag = SimpleRAG(llm=llm)
    
    # 2. 添加文档
    rag.add_document(
        "北京是中华人民共和国的首都，是全国的政治、文化中心。"
        "北京历史悠久，是著名的古都。",
        source="百科"
    )
    
    rag.add_document(
        "上海是中国最大的城市，是经济、金融和贸易中心。"
        "上海位于长江入海口，是重要的港口城市。",
        source="百科"
    )
    
    # 3. 查询
    question = "北京和上海分别是什么中心？"
    response = rag.query(question)
    print(f"\n问题: {question}")
    print(f"回答: {response}")
    
    # 4. 再问一个问题
    question2 = "哪个城市是古都？"
    response2 = rag.query(question2)
    print(f"\n问题: {question2}")
    print(f"回答: {response2}")
