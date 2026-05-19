"""百度翻译模块"""

import os
import hashlib
import random
from typing import Optional

try:
    import requests
except ImportError:
    requests = None


class BaiduTranslator:
    """百度翻译包装类"""
    
    def __init__(self, app_id: Optional[str] = None, app_key: Optional[str] = None):
        if requests is None:
            raise ImportError("请先安装 requests: pip install requests")
        
        self.app_id = app_id or os.getenv("BAIDU_TRANSLATE_APP_ID")
        self.app_key = app_key or os.getenv("BAIDU_TRANSLATE_APP_KEY")
        
        if not self.app_id or not self.app_key:
            raise ValueError("需要提供 app_id 和 app_key")
        
        self.url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
    
    def _generate_sign(self, query: str, salt: str) -> str:
        """生成签名"""
        sign_str = self.app_id + query + salt + self.app_key
        return hashlib.md5(sign_str.encode()).hexdigest()
    
    def translate(self, text: str, target_language: str = "zh") -> str:
        """翻译文本
        
        Args:
            text: 要翻译的文本
            target_language: 目标语言代码
            
        Returns:
            翻译结果
        """
        try:
            salt = str(random.randint(32768, 65536))
            sign = self._generate_sign(text, salt)
            
            params = {
                "q": text,
                "from": "auto",
                "to": target_language,
                "appid": self.app_id,
                "salt": salt,
                "sign": sign
            }
            
            response = requests.get(self.url, params=params)
            result = response.json()
            
            if "trans_result" in result:
                return result["trans_result"][0]["dst"]
            else:
                return f"翻译失败: {result.get('error_msg', '未知错误')}"
                
        except Exception as e:
            return f"翻译失败: {e}"


# 使用示例
if __name__ == "__main__":
    # 需要设置环境变量
    # os.environ["BAIDU_TRANSLATE_APP_ID"] = "your-app-id"
    # os.environ["BAIDU_TRANSLATE_APP_KEY"] = "your-app-key"
    
    translator = BaiduTranslator()
    result = translator.translate("Hello, world!", "zh")
    print(f"翻译结果: {result}")
