"""简单链式调用模块

这个模块提供了简化的 LangChain 链式调用接口。

使用示例:
    from langchain_wrapper import SimpleChain
    
    chain = SimpleChain(model_name="gpt-4", api_key="...")
    result = chain.invoke("你好")
"""

import os
from typing import Optional, List, Dict, Any

try:
    from langchain_openai import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate
    from langchain.schema.output_parser import StrOutputParser
    from langchain_core.runnables import RunnablePassthrough
except ImportError:
    print("需要安装 langchain: pip install langchain langchain-openai")
    ChatOpenAI = None


class SimpleChain:
    """简单的链式调用类
    
    这是一个简化版的 LangChain 链式调用封装。
    
    Args:
        api_key: OpenAI API Key
        model_name: 模型名称，默认为 "gpt-4"
        temperature: 温度参数，默认为 0.7
        system_prompt: 系统提示词
        
    使用示例:
        chain = SimpleChain(api_key="...")
        result = chain.invoke("解释量子计算")
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gpt-4",
        temperature: float = 0.7,
        system_prompt: Optional[str] = None
    ):
        if ChatOpenAI is None:
            raise ImportError("请先安装 langchain: pip install langchain langchain-openai")
            
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key 或设置 OPENAI_API_KEY 环境变量")
        
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            api_key=api_key
        )
        
        self.system_prompt = system_prompt or "你是一个有帮助的助手。"
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("user", "{input}")
        ])
        
        self.chain = self.prompt | self.llm | StrOutputParser()
    
    def invoke(self, input_text: str, **kwargs) -> str:
        """执行链式调用
        
        Args:
            input_text: 输入文本
            **kwargs: 其他参数
            
        Returns:
            生成的文本
        """
        return self.chain.invoke({"input": input_text}, **kwargs)
    
    def __call__(self, input_text: str) -> str:
        """简化调用"""
        return self.invoke(input_text)


class ConversationChain:
    """对话链类
    
    支持多轮对话的链式调用。
    
    Args:
        api_key: OpenAI API Key
        model_name: 模型名称
        system_prompt: 系统提示词
        
    使用示例:
        chain = ConversationChain(api_key="...")
        chain.add_user_message("你好")
        response = chain.get_response()
        chain.add_user_message("你是谁")
        response = chain.get_response()
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gpt-4",
        temperature: float = 0.7,
        system_prompt: Optional[str] = None
    ):
        if ChatOpenAI is None:
            raise ImportError("请先安装 langchain: pip install langchain langchain-openai")
            
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key 或设置 OPENAI_API_KEY 环境变量")
        
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            api_key=api_key
        )
        
        self.system_prompt = system_prompt or "你是一个有帮助的助手。"
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": self.system_prompt}
        ]
    
    def add_user_message(self, message: str) -> None:
        """添加用户消息"""
        self.messages.append({"role": "user", "content": message})
    
    def add_ai_message(self, message: str) -> None:
        """添加 AI 消息"""
        self.messages.append({"role": "assistant", "content": message})
    
    def get_response(self) -> str:
        """获取响应"""
        from langchain.schema import HumanMessage, AIMessage, SystemMessage
        
        # 转换消息格式
        langchain_messages = []
        for msg in self.messages:
            if msg["role"] == "system":
                langchain_messages.append(SystemMessage(content=msg["content"]))
            elif msg["role"] == "user":
                langchain_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                langchain_messages.append(AIMessage(content=msg["content"]))
        
        response = self.llm.invoke(langchain_messages)
        response_text = response.content
        
        # 保存到历史
        self.messages.append({"role": "assistant", "content": response_text})
        
        return response_text
    
    def clear_history(self) -> None:
        """清空历史（保留系统提示词）"""
        self.messages = [{"role": "system", "content": self.system_prompt}]


# 使用示例
if __name__ == "__main__":
    print("=== LangChain 简单链式调用示例 ===\n")
    
    # 示例 1: 简单链式调用
    print("示例 1: SimpleChain")
    chain = SimpleChain(system_prompt="你是一个友好的助手")
    result = chain.invoke("你好！")
    print(f"回复: {result}\n")
    
    # 示例 2: 对话链
    print("示例 2: ConversationChain")
    conv = ConversationChain(system_prompt="你是一个历史老师")
    conv.add_user_message("请介绍一下唐朝")
    response = conv.get_response()
    print(f"唐朝介绍: {response[:200]}...\n")
    
    conv.add_user_message("那么宋朝呢？")
    response = conv.get_response()
    print(f"宋朝介绍: {response[:200]}...")
