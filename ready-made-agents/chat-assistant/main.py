"""聊天助手主程序

一个简单的多轮对话聊天助手，带记忆功能。

运行:
    python main.py
"""

import os
import sys

# 添加 building-blocks 到路径
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper
from building_blocks.tools.memory.buffer_memory import BufferMemory


class ChatAssistant:
    """聊天助手类"""
    
    def __init__(self):
        # 初始化 LLM
        self.llm = OpenAIWrapper(
            model="gpt-4",
            temperature=0.7,
            system_prompt="你是一个友好、有帮助的助手。"
        )
        
        # 初始化记忆
        self.memory = BufferMemory(
            max_window=20,
            system_prompt="你是一个友好、有帮助的助手。"
        )
        
        print("🤖 你好！我是聊天助手。有什么可以帮助你的吗？")
        print("   (输入 /history 查看历史, /clear 清空, /quit 退出)")
        print("-" * 60)
    
    def chat(self, user_input: str) -> str:
        """进行对话"""
        # 添加用户消息
        self.memory.add_message("user", user_input)
        
        # 获取历史并生成回复
        history = self.memory.get_history()
        response = self.llm.generate_with_history(history)
        
        # 添加助手消息
        self.memory.add_message("assistant", response)
        
        return response
    
    def show_history(self):
        """显示历史"""
        print("\n📋 对话历史:")
        for msg in self.memory.get_history():
            prefix = "🗣️" if msg["role"] == "user" else "🤖"
            print(f"  {prefix}: {msg['content']}")
        print()
    
    def clear(self):
        """清空记忆"""
        self.memory.clear()
        print("✅ 对话已清空\n")
    
    def run(self):
        """运行聊天循环"""
        while True:
            try:
                user_input = input("\n🗣️ 你: ").strip()
                
                if not user_input:
                    continue
                    
                # 处理命令
                if user_input == "/quit" or user_input == "/exit":
                    print("👋 再见！")
                    break
                elif user_input == "/history":
                    self.show_history()
                    continue
                elif user_input == "/clear":
                    self.clear()
                    continue
                
                # 正常对话
                print("🤖 正在思考...", end="", flush=True)
                response = self.chat(user_input)
                print("\r" + " " * 30 + "\r", end="", flush=True)
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
    assistant = ChatAssistant()
    assistant.run()


if __name__ == "__main__":
    main()
