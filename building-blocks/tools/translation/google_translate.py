"""Google 翻译模块"""

import os
from typing import Optional

try:
    from googletrans import Translator
except ImportError:
    Translator = None


class GoogleTranslator:
    """Google 翻译包装类"""
    
    def __init__(self, api_key: Optional[str] = None):
        if Translator is None:
            raise ImportError("请先安装 googletrans: pip install googletrans==4.0.0-rc1")
        
        self.translator = Translator()
    
    def translate(self, text: str, target_language: str = "zh") -> str:
        """翻译文本
        
        Args:
            text: 要翻译的文本
            target_language: 目标语言代码
            
        Returns:
            翻译结果
        """
        try:
            result = self.translator.translate(text, dest=target_language)
            return result.text
        except Exception as e:
            return f"翻译失败: {e}"
    
    def detect_language(self, text: str) -> str:
        """检测语言
        
        Args:
            text: 文本
            
        Returns:
            语言代码
        """
        try:
            result = self.translator.detect(text)
            return result.lang
        except Exception as e:
            return f"检测失败: {e}"


# 使用示例
if __name__ == "__main__":
    translator = GoogleTranslator()
    result = translator.translate("Hello, world!", "zh")
    print(f"翻译结果: {result}")
