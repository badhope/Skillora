"""LlamaIndex 简单查询模块"""

import os
from typing import Optional, List

try:
    from llama_index.llms.openai import OpenAI
except ImportError:
    print("需要安装: pip install llama-index llama-index-llms-openai")
    OpenAI = None


class SimpleQuery:
    """简单的直接查询类
    
    不使用 RAG，直接调用 LLM 进行问答。
    
    Args:
        api_key: OpenAI API Key
        model_name: 模型名称，默认为 "gpt-4"
        system_prompt: 系统提示词
        
    使用示例:
        query = SimpleQuery(api_key="...")
        result = query.ask("解释量子计算")
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gpt-4",
        system_prompt: Optional[str] = None
    ):
        if OpenAI is None:
            raise ImportError("请先安装: pip install llama-index llama-index-llms-openai")
            
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key 或设置 OPENAI_API_KEY 环境变量")
        
        self.llm = OpenAI(
            model=model_name,
            api_key=api_key
        )
        
        self.system_prompt = system_prompt or "你是一个有帮助的助手。"
    
    def ask(self, question: str) -> str:
        """提问
        
        Args:
            question: 问题
            
        Returns:
            回答
        """
        from llama_index.core.prompts import ChatPromptTemplate
        
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": question}
        ]
        
        prompt = ChatPromptTemplate.from_messages(messages)
        response = self.llm.complete(prompt.format())
        return str(response)
    
    def chat(self, messages: List[dict]) -> str:
        """对话
        
        Args:
            messages: 消息列表
            
        Returns:
            回复
        """
        from llama_index.core.prompts import ChatPromptTemplate
        
        prompt = ChatPromptTemplate.from_messages(messages)
        response = self.llm.complete(prompt.format())
        return str(response)


# 使用示例
if __name__ == "__main__":
    print("=== LlamaIndex 简单查询示例 ===\n")
    
    query = SimpleQuery(system_prompt="你是一个友好的助手")
    result = query.ask("你好！")
    print(f"回答: {result}")
