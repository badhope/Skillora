"""缓冲记忆模块

这个模块提供了简单的对话记忆功能，保留最近的对话历史。

使用示例:
    from building_blocks.tools.memory.buffer_memory import BufferMemory
    
    memory = BufferMemory(max_window=10)
    memory.add_message("user", "你好")
    memory.add_message("assistant", "你好！")
    history = memory.get_history()
"""

from typing import List, Dict, Optional


class BufferMemory:
    """缓冲记忆类
    
    保留最近的对话历史，用于多轮对话。
    
    Args:
        max_window: 保留的最大消息数，默认为 20
        system_prompt: 可选的系统提示词
        
    使用示例:
        memory = BufferMemory()
        memory.add_message("user", "你好")
        memory.add_message("assistant", "你好！")
        print(memory.get_history())
    """
    
    def __init__(self, max_window: int = 20, system_prompt: Optional[str] = None):
        self.max_window = max_window
        self.messages: List[Dict[str, str]] = []
        if system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})
    
    def add_message(self, role: str, content: str) -> None:
        """添加消息
        
        Args:
            role: 角色，"user" 或 "assistant"
            content: 消息内容
        """
        self.messages.append({"role": role, "content": content})
        
        # 超过最大窗口时，删除最早的消息（保留系统提示词）
        has_system = self.messages and self.messages[0]["role"] == "system"
        while len(self.messages) > self.max_window:
            if has_system and len(self.messages) > 1:
                self.messages.pop(1)  # 删除第一条用户消息
            else:
                self.messages.pop(0)
    
    def get_history(self, include_system: bool = True) -> List[Dict[str, str]]:
        """获取历史记录
        
        Args:
            include_system: 是否包含系统提示词
            
        Returns:
            历史消息列表
        """
        if include_system:
            return self.messages.copy()
        else:
            return [msg for msg in self.messages if msg["role"] != "system"]
    
    def clear(self) -> None:
        """清空记忆"""
        # 如果有系统提示词，保留
        has_system = self.messages and self.messages[0]["role"] == "system"
        if has_system:
            self.messages = [self.messages[0]]
        else:
            self.messages = []
    
    def to_string(self) -> str:
        """将记忆转为字符串格式
        
        Returns:
            字符串表示的历史记录
        """
        lines = []
        for msg in self.messages:
            lines.append(f"{msg['role']}: {msg['content']}")
        return "\n".join(lines)


# 使用示例
if __name__ == "__main__":
    print("=== 缓冲记忆使用示例 ===")
    
    # 创建记忆
    memory = BufferMemory(max_window=10, system_prompt="你是一个友好的助手")
    
    # 添加对话
    memory.add_message("user", "你好")
    memory.add_message("assistant", "你好！有什么可以帮助你的？")
    memory.add_message("user", "今天天气怎么样？")
    
    # 获取历史
    history = memory.get_history()
    print("\n历史记录:")
    for msg in history:
        print(f"  {msg['role']}: {msg['content']}")
    
    # 转为字符串
    print("\n字符串格式:")
    print(memory.to_string())
