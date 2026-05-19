"""任务自动化主程序

一个能够自动分解和执行复杂任务的 AI 助手。

运行:
    python main.py
"""

import os
import sys
from typing import Optional, List

# 添加 building-blocks 到路径
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper
from planner import TaskPlanner
from executor import TaskExecutor


class TaskAutomationBot:
    """任务自动化机器人"""
    
    def __init__(self):
        # 初始化 LLM
        self.llm = OpenAIWrapper(
            model="gpt-4",
            temperature=0.7
        )
        
        # 初始化规划器
        self.planner = TaskPlanner(self.llm)
        
        # 初始化执行器
        self.executor = TaskExecutor(self.llm)
        
        # 当前任务计划
        self.current_plan = None
        
        print("⚡ 你好！我是任务自动化助手。")
        print("   告诉我你想要完成的任务，我会帮你规划和执行！")
        print("   (输入 /help 查看帮助, /quit 退出)")
        print("-" * 60)
    
    def process(self, user_input: str) -> str:
        """处理输入"""
        if user_input.startswith("/"):
            return self._handle_command(user_input)
        
        # 规划任务
        print("\n🤔 正在规划任务...")
        self.current_plan = self.planner.create_plan(user_input)
        
        # 显示计划
        response = self._show_plan()
        response += "\n\n输入 /execute 开始执行，或描述新任务"
        
        return response
    
    def _show_plan(self) -> str:
        """显示当前计划"""
        if not self.current_plan:
            return "暂无计划"
        
        steps = self.current_plan["steps"]
        
        response = f"\n📋 任务计划（{len(steps)} 个步骤）:\n\n"
        
        for i, step in enumerate(steps, 1):
            status = "⬜" if step["status"] == "pending" else "✅" if step["status"] == "completed" else "🔄"
            response += f"{i}. {status} {step['description']}\n"
        
        response += f"\n💡 估计时间: {self.current_plan.get('estimated_time', '未知')}"
        
        return response
    
    def execute_plan(self) -> str:
        """执行计划"""
        if not self.current_plan:
            return "❌ 没有可执行的计划，请先描述任务"
        
        steps = self.current_plan["steps"]
        pending_steps = [s for s in steps if s["status"] == "pending"]
        
        if not pending_steps:
            return "✅ 所有步骤已完成！"
        
        response = "\n🚀 开始执行计划...\n"
        
        for step in pending_steps:
            step["status"] = "in_progress"
            response += f"\n🔄 正在执行: {step['description']}...\n"
            
            # 执行步骤
            result = self.executor.execute_step(step)
            step["status"] = "completed"
            step["result"] = result
            
            response += f"✅ 完成: {result[:100]}...\n"
        
        response += "\n🎉 计划执行完成！"
        
        return response
    
    def _handle_command(self, command: str) -> str:
        """处理命令"""
        if command == "/help":
            return """
📖 可用命令:
  /help       - 显示帮助
  /plan       - 查看当前计划
  /execute    - 执行当前计划
  /progress   - 查看执行进度
  /reset      - 重置计划
  /quit       - 退出
"""
        elif command == "/plan":
            return self._show_plan()
        elif command == "/execute":
            return self.execute_plan()
        elif command == "/progress":
            if not self.current_plan:
                return "暂无计划"
            
            steps = self.current_plan["steps"]
            completed = len([s for s in steps if s["status"] == "completed"])
            total = len(steps)
            progress = completed / total * 100 if total > 0 else 0
            
            return f"📊 进度: {completed}/{total} ({progress:.1f}%)"
        elif command == "/reset":
            self.current_plan = None
            return "✅ 计划已重置"
        else:
            return "❓ 未知命令"
    
    def run(self):
        """运行主循环"""
        while True:
            try:
                user_input = input("\n🗣️ 你: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ["/quit", "/exit"]:
                    print("👋 再见！")
                    break
                
                response = self.process(user_input)
                print(f"\n🤖 助手: {response}")
                
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
        return
    
    # 运行任务自动化
    bot = TaskAutomationBot()
    bot.run()


if __name__ == "__main__":
    main()
