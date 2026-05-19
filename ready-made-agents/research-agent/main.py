"""研究助手主程序

一个带知识库的问答系统，可以基于文档回答问题。

运行:
    python main.py
"""

import os
import sys

# 添加 building-blocks 到路径
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from building_blocks.capabilities.rag.simple_rag import SimpleRAG
from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper
from building_blocks.tools.memory.buffer_memory import BufferMemory


class ResearchAssistant:
    """研究助手类"""
    
    def __init__(self):
        # 初始化 LLM
        self.llm = OpenAIWrapper(
            model="gpt-4",
            temperature=0.5
        )
        
        # 初始化记忆
        self.memory = BufferMemory(
            max_window=15,
            system_prompt="你是一个研究助手。请根据提供的文档回答问题。"
        )
        
        # 初始化 RAG
        self.rag = SimpleRAG(
            llm=self.llm,
            memory=self.memory,
            system_prompt="你是一个研究助手。请根据提供的文档回答问题。"
        )
        
        print("🔍 你好！我是研究助手。我可以基于文档回答问题。")
        print("   (输入 /add 添加文档, /docs 查看文档, /help 查看帮助)")
        print("-" * 60)
        
        # 添加一些默认文档作为示例
        self._add_default_docs()
    
    def _add_default_docs(self):
        """添加默认示例文档"""
        docs = [
            "人工智能（AI）是计算机科学的一个分支，"
            "致力于创建能够执行通常需要人类智能的任务的系统。",
            
            "大语言模型（LLM）是一种基于深度学习的人工智能模型，"
            "通过训练大量文本数据来学习语言模式。",
            
            "RAG（检索增强生成）是一种结合信息检索和文本生成的技术，"
            "可以使模型基于外部知识库回答问题。"
        ]
        
        for i, doc in enumerate(docs, 1):
            self.rag.add_document(doc, source=f"示例文档{i}")
        
        print(f"✅ 已加载 {len(docs)} 个示例文档\n")
    
    def ask(self, question: str) -> str:
        """提问"""
        print("🔍 正在思考...", end="", flush=True)
        response = self.rag.query(question)
        print("\r" + " " * 30 + "\r", end="", flush=True)
        return response
    
    def add_document(self, content: str, source: str = "用户添加"):
        """添加文档"""
        self.rag.add_document(content, source)
        return f"✅ 文档已添加（共 {self.rag.get_document_count()} 个文档）"
    
    def list_documents(self):
        """列出文档"""
        docs = self.rag.documents
        print(f"\n📚 文档列表（共 {len(docs)} 个）:")
        for i, doc in enumerate(docs[:10], 1):  # 最多显示10个
            preview = doc[:100] if len(doc) > 100 else doc
            print(f"  {i}. {preview}...")
        if len(docs) > 10:
            print(f"  ... 还有 {len(docs) - 10} 个文档")
        print()
    
    def show_help(self):
        """显示帮助"""
        print("\n📖 可用命令:")
        print("  /add <文本>     - 添加文档")
        print("  /docs          - 查看文档列表")
        print("  /clear         - 清空所有文档")
        print("  /clear-chat    - 清空对话历史")
        print("  /history       - 查看对话历史")
        print("  /help          - 显示此帮助")
        print("  /quit          - 退出\n")
    
    def show_history(self):
        """显示历史"""
        print("\n📋 对话历史:")
        for msg in self.rag.memory.get_history():
            prefix = "🗣️" if msg["role"] == "user" else "🤖"
            print(f"  {prefix}: {msg['content']}")
        print()
    
    def run(self):
        """运行主循环"""
        while True:
            try:
                user_input = input("\n🗣️ 你: ").strip()
                
                if not user_input:
                    continue
                    
                # 处理命令
                if user_input == "/quit" or user_input == "/exit":
                    print("👋 再见！")
                    break
                elif user_input == "/help":
                    self.show_help()
                    continue
                elif user_input == "/docs":
                    self.list_documents()
                    continue
                elif user_input.startswith("/add "):
                    content = user_input[5:].strip()
                    if content:
                        print(f"  {self.add_document(content)}")
                    else:
                        print("  ❌ 请输入文档内容")
                    continue
                elif user_input == "/clear":
                    self.rag.clear_documents()
                    print("  ✅ 文档已清空")
                    continue
                elif user_input == "/clear-chat":
                    self.rag.memory.clear()
                    print("  ✅ 对话已清空")
                    continue
                elif user_input == "/history":
                    self.show_history()
                    continue
                
                # 正常提问
                response = self.ask(user_input)
                print(f"🤖 助手: {response}")
                
            except KeyboardInterrupt:
                print("\n\n👋 再见！")
                break
            except Exception as e:
                print(f"\n❌ 出错了: {e}")


def main():
    """主函数"""
    # 检查 API Key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️ 请先设置 OPENAI_API_KEY 环境变量:")
        print("   export OPENAI_API_KEY=your-key-here")
        api_key = input("\n或者直接输入你的 API Key: ").strip()
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
        else:
            print("❌ 没有 API Key，无法继续。")
            return
    
    # 运行助手
    assistant = ResearchAssistant()
    assistant.run()


if __name__ == "__main__":
    main()
