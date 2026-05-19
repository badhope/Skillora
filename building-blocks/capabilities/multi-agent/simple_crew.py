"""简单多智能体团队模块

这是一个简化版的多智能体协作实现。

使用示例:
    from simple_crew import SimpleCrew
    
    crew = SimpleCrew()
    crew.add_agent("研究员", "研究最新进展")
    crew.add_agent("作家", "写文章")
    crew.add_task("写研究报告", "一份完整报告")
    result = crew.run("AI 的最新进展")
"""

from typing import List, Dict, Optional, Callable, Any
import sys
import os

# 添加 building-blocks 到路径
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper


class Agent:
    """智能体类"""
    
    def __init__(
        self,
        name: str,
        role: str,
        goal: str,
        backstory: str,
        llm: OpenAIWrapper
    ):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.llm = llm
        
        self.system_prompt = f"""你是 {role}。

目标: {goal}

背景: {backstory}

以你的角色身份完成这个任务。"""
    
    def execute(self, task: str) -> str:
        """执行任务"""
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": task}
        ]
        
        return self.llm.generate_with_history(messages)
    
    def __repr__(self):
        return f"Agent({self.name}, role={self.role})"


class Task:
    """任务类"""
    
    def __init__(
        self,
        description: str,
        expected_output: str,
        agent: Optional[Agent] = None
    ):
        self.description = description
        self.expected_output = expected_output
        self.agent = agent
        self.output = None
    
    def __repr__(self):
        return f"Task({self.description[:30]}...)"


class SimpleCrew:
    """简单多智能体团队类
    
    这是一个简化版的多智能体协作实现。
    
    Args:
        api_key: OpenAI API Key
        model: 模型名称
        
    使用示例:
        crew = SimpleCrew()
        crew.add_agent("研究员", "研究最新进展")
        crew.add_agent("作家", "写文章")
        crew.add_task("写研究报告", "一份完整报告")
        result = crew.run("AI 的最新进展")
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-4"
    ):
        self.llm = OpenAIWrapper(api_key=api_key, model=model)
        self.agents: List[Agent] = []
        self.tasks: List[Task] = []
        self.process = "sequential"  # sequential or hierarchical
    
    def add_agent(
        self,
        name: str,
        role: str,
        goal: str,
        backstory: Optional[str] = None
    ) -> Agent:
        """添加智能体
        
        Args:
            name: 智能体名称
            role: 角色
            goal: 目标
            backstory: 背景故事
            
        Returns:
            创建的智能体
        """
        if backstory is None:
            backstory = f"你是一个专业的 {role}。"
        
        agent = Agent(
            name=name,
            role=role,
            goal=goal,
            backstory=backstory,
            llm=self.llm
        )
        self.agents.append(agent)
        return agent
    
    def add_task(
        self,
        description: str,
        expected_output: str,
        agent_name: Optional[str] = None
    ) -> Task:
        """添加任务
        
        Args:
            description: 任务描述
            expected_output: 期望输出
            agent_name: 负责的智能体名称
            
        Returns:
            创建的任务
        """
        agent = None
        if agent_name:
            for a in self.agents:
                if a.name == agent_name:
                    agent = a
                    break
        
        task = Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )
        self.tasks.append(task)
        return task
    
    def run(self, goal: str, verbose: bool = True) -> str:
        """运行团队
        
        Args:
            goal: 团队目标
            verbose: 是否输出详细信息
            
        Returns:
            执行结果
        """
        if verbose:
            print(f"🎯 目标: {goal}")
            print(f"📊 团队成员: {len(self.agents)} 个智能体")
            print(f"📋 任务数: {len(self.tasks)} 个任务\n")
        
        results = []
        
        # 如果没有任务，创建一个默认任务
        if not self.tasks:
            if self.agents:
                task = Task(
                    description=goal,
                    expected_output="完成目标的结果",
                    agent=self.agents[0]
                )
                self.tasks.append(task)
            else:
                return "请先添加智能体"
        
        # 顺序执行任务
        for i, task in enumerate(self.tasks, 1):
            agent = task.agent or self.agents[i % len(self.agents)] if self.agents else None
            
            if not agent:
                return f"任务 '{task.description}' 没有负责的智能体"
            
            if verbose:
                print(f"--- 任务 {i}/{len(self.tasks)} ---")
                print(f"🤖 执行者: {agent.name} ({agent.role})")
                print(f"📝 任务: {task.description}")
            
            # 构建任务提示
            task_prompt = f"""任务: {task.description}

期望输出: {task.expected_output}

请完成这个任务。"""
            
            # 执行
            output = agent.execute(task_prompt)
            task.output = output
            results.append(output)
            
            if verbose:
                print(f"✅ 完成\n")
        
        # 汇总结果
        final_result = "\n\n".join(results)
        
        if verbose:
            print("=" * 60)
            print("🎉 所有任务完成！")
        
        return final_result
    
    def get_results(self) -> Dict[str, Any]:
        """获取所有结果"""
        return {
            "agents": [
                {"name": a.name, "role": a.role}
                for a in self.agents
            ],
            "tasks": [
                {
                    "description": t.description,
                    "output": t.output
                }
                for t in self.tasks
            ]
        }


# 使用示例
if __name__ == "__main__":
    print("=== 多智能体团队示例 ===\n")
    
    # 创建团队
    crew = SimpleCrew()
    
    # 添加研究员
    crew.add_agent(
        name="研究员",
        role="研究员",
        goal="研究并总结信息",
        backstory="你是一个专业的研究员，擅长收集和分析信息。"
    )
    
    # 添加作家
    crew.add_agent(
        name="作家",
        role="作家",
        goal="将研究内容转化为优质文章",
        backstory="你是一个优秀的作家，擅长用优美的语言表达复杂概念。"
    )
    
    # 添加任务
    crew.add_task(
        description="研究人工智能在医疗领域的应用",
        expected_output="一份详细的研究报告",
        agent_name="研究员"
    )
    
    crew.add_task(
        description="将研究报告转化为一篇科普文章",
        expected_output="一篇通俗易懂的科普文章",
        agent_name="作家"
    )
    
    # 运行
    print("开始执行团队任务...\n")
    result = crew.run("写一篇关于 AI 医疗的文章", verbose=True)
    
    print("\n最终结果:")
    print(result)
