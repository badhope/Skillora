"""客服机器人主程序

一个基于知识库的智能客服机器人。

运行:
    python main.py
"""

import os
import sys

# 添加 building-blocks 到路径
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper
from building_blocks.tools.memory.buffer_memory import BufferMemory
from building_blocks.capabilities.rag.simple_rag import SimpleRAG
from knowledge import KnowledgeBase
from responses import ResponseTemplates


class CustomerSupportBot:
    """客服机器人"""
    
    def __init__(self):
        # 初始化 LLM
        self.llm = OpenAIWrapper(
            model="gpt-4",
            temperature=0.7,
            system_prompt="你是一个专业、友好的客服助手。"
        )
        
        # 初始化记忆
        self.memory = BufferMemory(
            max_window=20,
            system_prompt="你是一个专业、友好的客服助手。"
        )
        
        # 初始化知识库
        self.knowledge = KnowledgeBase()
        
        # 初始化 RAG
        self.rag = SimpleRAG(
            llm=self.llm,
            memory=self.memory,
            system_prompt="你是一个客服助手。请根据知识库回答问题。"
        )
        
        # 加载知识库
        self._load_knowledge()
        
        # 初始化回复模板
        self.templates = ResponseTemplates()
        
        print("💬 你好！我是智能客服，有什么可以帮你的？")
        print("   (输入 /knowledge 查看知识库, /clear 清空, /quit 退出)")
        print("-" * 60)
    
    def _load_knowledge(self):
        """加载知识库"""
        docs = self.knowledge.get_all_documents()
        for doc in docs:
            self.rag.add_document(doc["content"], source=doc.get("category", "通用"))
    
    def chat(self, user_input: str) -> str:
        """处理对话"""
        # 检查是否是命令
        if user_input.startswith("/"):
            return self._handle_command(user_input)
        
        # 检查是否匹配常见问题
        template_response = self.templates.match(user_input)
        if template_response:
            return template_response
        
        # 使用 RAG 回答
        response = self.rag.query(user_input)
        
        # 添加转人工提示
        if self._needs_human(user_input):
            response += "\n\n🤝 如果需要人工服务，请输入 /human"
        
        return response
    
    def _needs_human(self, question: str) -> bool:
        """判断是否需要转人工"""
        human_keywords = ["投诉", "紧急", "退款", "退钱", "严重问题"]
        return any(keyword in question for keyword in human_keywords)
    
    def _handle_command(self, command: str) -> str:
        """处理命令"""
        if command == "/knowledge":
            return self.knowledge.show_summary()
        elif command == "/clear":
            self.rag.memory.clear()
            return "✅ 对话已清空"
        elif command == "/help":
            return self.templates.show_help()
        elif command == "/human":
            return "🤝 正在转接人工客服，请稍候..."
        else:
            return "❓ 未知命令"
    
    def show_history(self):
        """显示历史"""
        print("\n📋 对话历史:")
        for msg in self.rag.memory.get_history():
            prefix = "🗣️" if msg["role"] == "user" else "🤖"
            print(f"  {prefix}: {msg['content'][:100]}...")
        print()
    
    def run(self):
        """运行聊天循环"""
        while True:
            try:
                user_input = input("\n🗣️ 你: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ["/quit", "/exit"]:
                    print("👋 再见！祝您愉快！")
                    break
                
                if user_input == "/history":
                    self.show_history()
                    continue
                
                print("🤖 正在回复...", end="", flush=True)
                response = self.chat(user_input)
                print("\r" + " " * 30 + "\r", end="", flush=True)
                print(f"🤖 客服: {response}")
                
            except KeyboardInterrupt:
                print("\n\n👋 再见！祝您愉快！")
                break
            except Exception as e:
                print(f"\n❌ 出错了: {e}")


def main():
    """主函数"""
    # 检查 API Key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️ 请先设置 OPENAI_API_KEY 环境变量:")
        print("   export OPENAI_API_KEY=your-key-here")
        return
    
    # 运行客服
    bot = CustomerSupportBot()
    bot.run()


if __name__ == "__main__":
    main()
