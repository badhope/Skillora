"""知识库模块"""

from typing import List, Dict


class KnowledgeBase:
    """知识库类"""
    
    def __init__(self):
        self.documents: List[Dict] = []
        self._load_default_knowledge()
    
    def _load_default_knowledge(self):
        """加载默认知识库"""
        self.documents = [
            # 产品信息
            {
                "category": "产品",
                "content": "我们的产品定价分为三个档次：基础版免费，专业版每月99元，企业版每月299元。",
                "tags": ["价格", "收费", "费用"]
            },
            {
                "category": "产品",
                "content": "产品支持 Windows、Mac 和 Linux 系统，也提供 iOS 和 Android 移动应用。",
                "tags": ["系统", "平台", "支持"]
            },
            {
                "category": "产品",
                "content": "注册账号后点击'开始使用'即可免费试用基础功能，无需信用卡。",
                "tags": ["注册", "试用", "免费"]
            },
            
            # 支付相关
            {
                "category": "支付",
                "content": "我们支持支付宝、微信支付、信用卡和 PayPal 等多种支付方式。",
                "tags": ["支付", "付款", "支付宝", "微信"]
            },
            {
                "category": "支付",
                "content": "退款政策：付费后7天内可申请全额退款，超过7天按剩余时间比例退款。",
                "tags": ["退款", "退钱"]
            },
            
            # 技术支持
            {
                "category": "技术",
                "content": "遇到技术问题可以发送邮件到 support@example.com 或拨打客服热线 400-123-4567。",
                "tags": ["技术", "支持", "联系"]
            },
            {
                "category": "技术",
                "content": "常见问题解决方案：1) 刷新页面 2) 清除浏览器缓存 3) 重新登录 4) 更新到最新版本。",
                "tags": ["问题", "解决", "帮助"]
            },
            
            # 账户相关
            {
                "category": "账户",
                "content": "忘记密码可以点击登录页的'忘记密码'，输入注册邮箱后会收到重置链接。",
                "tags": ["密码", "登录", "账户"]
            },
            {
                "category": "账户",
                "content": "账户注销可以通过'设置'->'账户'->'注销账户'操作，注销后数据无法恢复。",
                "tags": ["注销", "删除", "账户"]
            },
            
            # 服务
            {
                "category": "服务",
                "content": "工作时间：周一至周五 9:00-18:00，节假日除外。紧急问题可以提交工单。",
                "tags": ["时间", "服务时间", "工作时间"]
            },
            {
                "category": "服务",
                "content": "VIP 客户可以享受专属客服、优先响应和定制化服务。",
                "tags": ["VIP", "专属", "服务"]
            }
        ]
    
    def add_document(self, content: str, category: str = "通用", tags: List[str] = None):
        """添加文档"""
        self.documents.append({
            "category": category,
            "content": content,
            "tags": tags or []
        })
    
    def get_all_documents(self) -> List[Dict]:
        """获取所有文档"""
        return self.documents
    
    def get_by_category(self, category: str) -> List[Dict]:
        """按类别获取"""
        return [doc for doc in self.documents if doc["category"] == category]
    
    def show_summary(self) -> str:
        """显示知识库摘要"""
        categories = {}
        for doc in self.documents:
            cat = doc["category"]
            if cat not in categories:
                categories[cat] = 0
            categories[cat] += 1
        
        summary = "\n📚 知识库内容:\n\n"
        for cat, count in categories.items():
            summary += f"  📁 {cat}: {count} 条\n"
        
        summary += f"\n总计: {len(self.documents)} 条知识"
        
        return summary


# 使用示例
if __name__ == "__main__":
    kb = KnowledgeBase()
    print(kb.show_summary())
