"""CrewAI 简单多智能体模块

这个模块提供了简化的 CrewAI 多智能体接口。

使用示例:
    from crewai_wrapper import SimpleCrew
    
    crew = SimpleCrew(api_key="...")
    crew.add_agent("研究员", "研究最新的 AI 进展")
    crew.add_agent("作家", "写科技文章")
    result = crew.run("写一篇关于 AI 的文章")
"""

import os
from typing import Optional, List, Dict, Any

try:
    from crewai import Agent, Task, Crew
    from crewai.llm import LLM
except ImportError:
    print("需要安装 crewai: pip install crewai crewai-tools")
    Agent = None


class SimpleAgent:
    """简单智能体类"""
    
    def __init__(self, role: str, goal: str, backstory: str, llm: Any):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.llm = llm
        self._agent = None
    
    def create(self) -> Agent:
        """创建 CrewAI Agent"""
        self._agent = Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            llm=self.llm,
            verbose=True
        )
        return self._agent
    
    @property
    def agent(self) -> Agent:
        if self._agent is None:
            self.create()
        return self._agent


class SimpleCrew:
    """简单的多智能体团队类
    
    这是一个简化版的 CrewAI Crew 封装。
    
    Args:
        api_key: OpenAI API Key
        model_name: 模型名称，默认为 "gpt-4"
        process_type: 流程类型，"sequential" 或 "hierarchical"
        
    使用示例:
        crew = SimpleCrew(api_key="...")
        crew.add_agent("研究员", "研究最新的 AI 进展")
        crew.add_agent("作家", "写科技文章")
        result = crew.run("写一篇关于 AI 的文章")
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gpt-4",
        process_type: str = "sequential"
    ):
        if Agent is None:
            raise ImportError("请先安装 crewai: pip install crewai crewai-tools")
            
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key 或设置 OPENAI_API_KEY 环境变量")
        
        # 初始化 LLM
        self.llm = LLM(model=f"openai/{model_name}", api_key=api_key)
        
        self.process_type = process_type
        self.agents: List[SimpleAgent] = []
        self.tasks: List[Task] = []
    
    def add_agent(
        self,
        role: str,
        goal: str,
        backstory: Optional[str] = None
    ) -> None:
        """添加智能体
        
        Args:
            role: 角色名称
            goal: 目标
            backstory: 背景故事
        """
        if backstory is None:
            backstory = f"你是一个专业的 {role}。"
        
        agent = SimpleAgent(
            role=role,
            goal=goal,
            backstory=backstory,
            llm=self.llm
        )
        self.agents.append(agent)
    
    def add_task(
        self,
        description: str,
        expected_output: str,
        agent_index: Optional[int] = None
    ) -> None:
        """添加任务
        
        Args:
            description: 任务描述
            expected_output: 期望输出
            agent_index: 负责的智能体索引
        """
        agent = None
        if agent_index is not None and agent_index < len(self.agents):
            agent = self.agents[agent_index].agent
        
        task = Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )
        self.tasks.append(task)
    
    def run(self, goal: str, verbose: bool = True) -> str:
        """运行团队
        
        Args:
            goal: 团队目标
            verbose: 是否输出详细信息
            
        Returns:
            执行结果
        """
        if not self.agents:
            return "请先添加智能体"
        
        # 如果没有任务，创建一个默认任务
        if not self.tasks:
            task = Task(
                description=goal,
                expected_output="完成目标的结果",
                agent=self.agents[0].agent if self.agents else None
            )
            self.tasks.append(task)
        
        # 创建 Crew
        crew = Crew(
            agents=[agent.agent for agent in self.agents],
            tasks=self.tasks,
            process=self.process_type,
            verbose=verbose
        )
        
        # 执行
        result = crew.kickoff()
        return str(result)
    
    def clear(self) -> None:
        """清空团队"""
        self.agents = []
        self.tasks = []


# 使用示例
if __name__ == "__main__":
    print("=== CrewAI 简单多智能体示例 ===\n")
    
    # 注意：需要设置 OPENAI_API_KEY 才能运行
    # import os
    # os.environ["OPENAI_API_KEY"] = "your-key"
    
    print("创建团队...")
    crew = SimpleCrew()
    
    print("添加研究员...")
    crew.add_agent(
        role="研究员",
        goal="研究并总结最新的人工智能进展",
        backstory="你是一个专业的研究员，擅长分析科技趋势。"
    )
    
    print("添加作家...")
    crew.add_agent(
        role="作家",
        goal="将研究内容转化为通俗易懂的文章",
        backstory="你是一个科技作家，擅长用简单的语言解释复杂概念。"
    )
    
    print("\n添加任务...")
    crew.add_task(
        description="调研 2024 年 AI 领域的最新进展",
        expected_output="一份 AI 进展报告",
        agent_index=0
    )
    
    crew.add_task(
        description="将报告转化为一篇 500 字的文章",
        expected_output="一篇通俗易懂的文章",
        agent_index=1
    )
    
    print("\n执行团队任务...")
    # result = crew.run("写一篇关于 2024 年 AI 进展的文章")
    # print(f"结果: {result}")
    print("（请设置 OPENAI_API_KEY 环境变量后运行）")
