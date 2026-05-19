"""回复模板模块"""

from typing import Optional, List, Dict


class ResponseTemplates:
    """回复模板类"""
    
    def __init__(self):
        self.templates: List[Dict] = [
            {
                "keywords": ["你好", "您好", "hi", "hello"],
                "response": "你好！有什么我可以帮助你的吗？😊"
            },
            {
                "keywords": ["谢谢", "感谢"],
                "response": "不客气！很高兴能帮到你。还有其他问题吗？😊"
            },
            {
                "keywords": ["再见", "拜拜", "bye"],
                "response": "再见！祝您愉快！有需要随时回来找我。👋"
            },
            {
                "keywords": ["价格", "多少钱", "收费"],
                "response": "我们的产品有三个版本：\n"
                           "• 基础版：免费\n"
                           "• 专业版：99元/月\n"
                           "• 企业版：299元/月\n"
                           "需要了解更多信息请告诉我！"
            },
            {
                "keywords": ["联系", "人工", "客服"],
                "response": "你可以这样联系我们：\n"
                           "📧 邮箱：support@example.com\n"
                           "📞 电话：400-123-4567\n"
                           "⏰ 时间：周一至周五 9:00-18:00"
            },
            {
                "keywords": ["退款", "退钱"],
                "response": "关于退款政策：\n"
                           "• 付费后7天内可申请全额退款\n"
                           "• 超过7天按剩余时间比例退款\n"
                           "如需申请，请联系客服。"
            }
        ]
    
    def match(self, question: str) -> Optional[str]:
        """匹配回复模板"""
        question_lower = question.lower()
        
        for template in self.templates:
            for keyword in template["keywords"]:
                if keyword.lower() in question_lower:
                    return template["response"]
        
        return None
    
    def add_template(self, keywords: List[str], response: str):
        """添加模板"""
        self.templates.append({
            "keywords": keywords,
            "response": response
        })
    
    def show_help(self) -> str:
        """显示帮助"""
        return """
📖 可用命令:
  /help       - 显示帮助
  /knowledge  - 查看知识库
  /human      - 转接人工
  /clear      - 清空对话
  /quit       - 退出

💡 你也可以直接提问，我会尽力回答！
"""


if __name__ == "__main__":
    templates = ResponseTemplates()
    print(templates.show_help())
