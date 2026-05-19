"""关键词提取模块"""

import os
from typing import Optional, List

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class KeywordExtractor:
    """关键词提取类"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        if OpenAI is None:
            raise ImportError("请先安装 openai: pip install openai")
        
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key")
        
        self.client = OpenAI(api_key=api_key)
        self.model = model
    
    def extract(self, text: str, num_keywords: int = 5) -> List[str]:
        """提取关键词
        
        Args:
            text: 文本
            num_keywords: 关键词数量
            
        Returns:
            关键词列表
        """
        try:
            prompt = f"""请从以下文本中提取 {num_keywords} 个关键词：

{text}

请以逗号分隔返回关键词，不要其他内容。"""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            
            result = response.choices[0].message.content
            return [k.strip() for k in result.split(",") if k.strip()]
        
        except Exception as e:
            return []


# 使用示例
if __name__ == "__main__":
    extractor = KeywordExtractor()
    text = "人工智能和机器学习正在改变我们的生活方式，从自动驾驶到智能助手。"
    keywords = extractor.extract(text)
    print(f"关键词: {keywords}")
