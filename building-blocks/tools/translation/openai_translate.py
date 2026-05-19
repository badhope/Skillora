"""OpenAI 翻译模块"""

import os
from typing import Optional

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class OpenAITranslator:
    """OpenAI 翻译包装类"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        if OpenAI is None:
            raise ImportError("请先安装 openai: pip install openai")
        
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key")
        
        self.client = OpenAI(api_key=api_key)
        self.model = model
    
    def translate(self, text: str, target_language: str = "Chinese") -> str:
        """翻译文本
        
        Args:
            text: 要翻译的文本
            target_language: 目标语言（中文、English 等）
            
        Returns:
            翻译结果
        """
        try:
            prompt = f"""请将以下文本翻译成 {target_language}：

{text}

只返回翻译结果，不要其他内容。"""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return f"翻译失败: {e}"
    
    def translate_with_context(self, text: str, context: str, target_language: str = "Chinese") -> str:
        """带上下文翻译
        
        Args:
            text: 要翻译的文本
            context: 上下文说明
            target_language: 目标语言
            
        Returns:
            翻译结果
        """
        try:
            prompt = f"""请将以下文本翻译成 {target_language}，并参考上下文：

上下文：{context}

文本：{text}

只返回翻译结果，不要其他内容。"""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return f"翻译失败: {e}"


# 使用示例
if __name__ == "__main__":
    translator = OpenAITranslator()
    result = translator.translate("Hello, world!", "Chinese")
    print(f"翻译结果: {result}")
