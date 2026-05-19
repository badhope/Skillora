"""AutoGen 简单多智能体对话模块

这个模块提供了简化的 AutoGen 多智能体对话接口。

使用示例:
    from autogen_wrapper import SimpleChat
    
    chat = SimpleChat(api_key="...")
    chat.add_agent("助手", system_message="你是一个有帮助的助手")
    chat.add_agent("用户", is_user_proxy=True)
    result = chat.start("你好")
"""

import os
from typing import Optional, List, Dict, Any

try:
    import autogen
    from autogen import ConversableAgent
except ImportError:
    print("需要安装 pyautogen: pip install pyautogen")
    ConversableAgent = None


class SimpleChat:
    """简单的多智能体对话类
    
    这是一个简化版的 AutoGen 对话封装。
    
    Args:
        api_key: OpenAI API Key
        model_name: 模型名称，默认为 "gpt-4"
        
    使用示例:
        chat = SimpleChat(api_key="...")
        chat.add_agent("助手", system_message="你是一个有帮助的助手")
        chat.start("你好")
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gpt-4"
    ):
        if ConversableAgent is None:
            raise ImportError("请先安装 pyautogen: pip install pyautogen")
            
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key 或设置 OPENAI_API_KEY 环境变量")
        
        self.model_name = model_name
        self.api_key = api_key
        self.agents: List[ConversableAgent] = []
        self.config_list = [{
            "model": model_name,
            "api_key": api_key
        }]
    
    def add_assistant_agent(
        self,
        name: str,
        system_message: str,
        human_input_mode: str = "NEVER"
    ) -> ConversableAgent:
        """添加助手智能体
        
        Args:
            name: 智能体名称
            system_message: 系统消息
            human_input_mode: 人工输入模式
            
        Returns:
            创建的智能体
        """
        agent = ConversableAgent(
            name=name,
            system_message=system_message,
            llm_config={
                "config_list": self.config_list,
                "temperature": 0.7
            },
            human_input_mode=human_input_mode,
            max_consecutive_auto_reply=10
        )
        self.agents.append(agent)
        return agent
    
    def add_user_proxy_agent(
        self,
        name: str = "user_proxy",
        human_input_mode: str = "ALWAYS"
    ) -> ConversableAgent:
        """添加用户代理智能体
        
        Args:
            name: 智能体名称
            human_input_mode: 人工输入模式
            
        Returns:
            创建的智能体
        """
        agent = ConversableAgent(
            name=name,
            system_message="你是一个用户代理。",
            llm_config={"config_list": self.config_list},
            human_input_mode=human_input_mode,
            max_consecutive_auto_reply=0
        )
        self.agents.append(agent)
        return agent
    
    def start(
        self,
        message: str,
        recipient_name: Optional[str] = None,
        max_turns: Optional[int] = None
    ) -> str:
        """开始对话
        
        Args:
            message: 初始消息
            recipient_name: 接收者名称
            max_turns: 最大对话轮数
            
        Returns:
            对话结果
        """
        if len(self.agents) < 2:
            return "需要至少两个智能体才能开始对话"
        
        # 默认第一个是发起者，最后一个是接收者
        initiator = self.agents[-1]
        recipient = self.agents[0]
        
        # 如果指定了接收者
        if recipient_name:
            for agent in self.agents:
                if agent.name == recipient_name:
                    recipient = agent
                    break
        
        # 开始对话
        chat_result = initiator.initiate_chat(
            recipient,
            message=message,
            max_turns=max_turns,
            summary_method="last_msg"
        )
        
        return str(chat_result)
    
    def get_agent(self, name: str) -> Optional[ConversableAgent]:
        """获取智能体
        
        Args:
            name: 智能体名称
            
        Returns:
            智能体或 None
        """
        for agent in self.agents:
            if agent.name == name:
                return agent
        return None


# 使用示例
if __name__ == "__main__":
    print("=== AutoGen 简单多智能体对话示例 ===\n")
    
    # 注意：需要设置 OPENAI_API_KEY 才能运行
    # import os
    # os.environ["OPENAI_API_KEY"] = "your-key"
    
    print("创建对话系统...")
    chat = SimpleChat()
    
    print("添加助手...")
    chat.add_assistant_agent(
        name="assistant",
        system_message="你是一个知识渊博的助手。"
    )
    
    print("添加用户代理...")
    chat.add_user_proxy_agent(name="user")
    
    print("\n开始对话...")
    # result = chat.start("你好，请介绍一下人工智能")
    # print(f"结果: {result}")
    print("（请设置 OPENAI_API_KEY 环境变量后运行）")
