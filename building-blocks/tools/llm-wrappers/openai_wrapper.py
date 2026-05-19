"""OpenAI LLM 简单包装模块

这个模块提供了简单的 OpenAI API 调用包装，方便快速集成使用。

使用示例:
    from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper
    
    llm = OpenAIWrapper(api_key="your-api-key")
    response = llm.generate("你好，世界！")
"""

import os
from typing import Optional, List, Dict

try:
    from openai import OpenAI
except ImportError:
    print("需要安装 openai 包: pip install openai")
    OpenAI = None


class OpenAIWrapper:
    """OpenAI API 简单包装
    
    这是一个简化版的 OpenAI API 调用类，方便快速使用。
    
    Args:
        api_key: OpenAI API Key，如果不提供则从环境变量 OPENAI_API_KEY 读取
        model: 使用的模型，默认为 "gpt-4"
        temperature: 温度参数，默认为 0.7
        max_tokens: 最大生成 token 数，默认为 1000
        
    使用示例:
        llm = OpenAIWrapper(api_key="...")
        response = llm.generate("你好！")
        print(response)
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-4",
        temperature: float = 0.7,
        max_tokens: int = 1000
    ):
        if OpenAI is None:
            raise ImportError("请先安装 openai 包: pip install openai")
            
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key 或设置 OPENAI_API_KEY 环境变量")
            
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """生成文本
        
        Args:
            prompt: 用户输入的提示词
            system_prompt: 系统提示词，可选
            
        Returns:
            生成的文本
        """
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        
        return response.choices[0].message.content
    
    def generate_with_history(
        self,
        messages: List[Dict[str, str]]
    ) -> str:
        """带历史记录的生成
        
        Args:
            messages: 历史消息列表，每个消息为 {"role": "...", "content": "..."}
            
        Returns:
            生成的文本
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        
        return response.choices[0].message.content


# 使用示例
if __name__ == "__main__":
    # 示例 1: 简单生成
    llm = OpenAIWrapper()
    response = llm.generate("你好，请介绍自己")
    print("示例 1:", response)
    
    # 示例 2: 带系统提示词
    response = llm.generate(
        "推荐一本好书",
        system_prompt="你是一个文学评论家"
    )
    print("\n示例 2:", response)
    
    # 示例 3: 带历史记录
    messages = [
        {"role": "system", "content": "你是一个友好的助手"},
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好！有什么可以帮助你的？"},
        {"role": "user", "content": "今天天气怎么样？"}
    ]
    response = llm.generate_with_history(messages)
    print("\n示例 3:", response)
