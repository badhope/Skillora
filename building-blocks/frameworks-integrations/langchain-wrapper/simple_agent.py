"""简单智能体模块

这个模块提供了带工具调用能力的简单智能体。

使用示例:
    from langchain_wrapper import SimpleAgent
    
    agent = SimpleAgent(api_key="...")
    agent.add_tool(search_function, "search", "搜索互联网信息")
    result = agent.invoke("查询今天的天气")
"""

import os
from typing import Optional, Dict, Any, Callable, List

try:
    from langchain_openai import ChatOpenAI
    from langchain.agents import AgentExecutor, create_react_agent
    from langchain.prompts import PromptTemplate
    from langchain.tools import Tool
except ImportError:
    print("需要安装 langchain: pip install langchain langchain-openai")
    ChatOpenAI = None
    AgentExecutor = None


class SimpleTool:
    """简单工具类"""
    
    def __init__(self, func: Callable, name: str, description: str):
        self.func = func
        self.name = name
        self.description = description
    
    def to_langchain_tool(self):
        """转换为 LangChain Tool"""
        return Tool(
            name=self.name,
            func=self.func,
            description=self.description
        )


class SimpleAgent:
    """简单的工具调用智能体
    
    这是一个简化版的 LangChain Agent 封装。
    
    Args:
        api_key: OpenAI API Key
        model_name: 模型名称，默认为 "gpt-4"
        system_prompt: 系统提示词
        
    使用示例:
        agent = SimpleAgent(api_key="...")
        
        def search(query):
            return f"搜索结果: {query}"
        
        agent.add_tool(search, "search", "搜索互联网")
        result = agent.invoke("搜索 AI 的最新进展")
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gpt-4",
        system_prompt: Optional[str] = None
    ):
        if ChatOpenAI is None or AgentExecutor is None:
            raise ImportError("请先安装 langchain: pip install langchain langchain-openai")
            
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("需要提供 api_key 或设置 OPENAI_API_KEY 环境变量")
        
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=0,
            api_key=api_key
        )
        
        self.system_prompt = system_prompt or (
            "你是一个有帮助的助手，可以使用工具来完成任务。"
            "当你需要使用工具时，请在响应中明确说明。"
        )
        
        self.tools: List[Tool] = []
        self.agent = None
        self.executor = None
        
        # 默认提示词模板
        self.prompt_template = PromptTemplate.from_template("""你是一个有用的助手。

你可以使用以下工具:

{tools}

使用以下格式:

问题: {input}
思考: 你应该总是考虑如何回答
行动: 工具名称
行动输入: 工具输入
观察: 工具结果
... (这个思考/行动/行动输入/观察 可以重复多次)
思考: 我现在知道最终答案了
最终答案: 对原始问题的最终回答

问题: {input}
思考:""")
    
    def add_tool(self, func: Callable, name: str, description: str) -> None:
        """添加工具
        
        Args:
            func: 工具函数
            name: 工具名称
            description: 工具描述
        """
        tool = SimpleTool(func, name, description).to_langchain_tool()
        self.tools.append(tool)
        
        # 重新创建 Agent
        self._rebuild_agent()
    
    def _rebuild_agent(self) -> None:
        """重建 Agent"""
        if self.tools:
            self.agent = create_react_agent(
                self.llm,
                self.tools,
                self.prompt_template
            )
            self.executor = AgentExecutor(
                agent=self.agent,
                tools=self.tools,
                verbose=True,
                max_iterations=10
            )
    
    def invoke(self, input_text: str, **kwargs) -> str:
        """执行智能体
        
        Args:
            input_text: 输入文本
            **kwargs: 其他参数
            
        Returns:
            生成的文本
        """
        if not self.executor:
            # 如果没有工具，直接使用 LLM
            from langchain.schema import HumanMessage, SystemMessage
            response = self.llm.invoke([
                SystemMessage(content=self.system_prompt),
                HumanMessage(content=input_text)
            ])
            return response.content
        
        return self.executor.invoke({"input": input_text}, **kwargs)["output"]
    
    def __call__(self, input_text: str) -> str:
        """简化调用"""
        return self.invoke(input_text)


# 示例工具函数
def calculator(expression: str) -> str:
    """计算器工具"""
    try:
        result = eval(expression)
        return f"计算结果: {result}"
    except Exception as e:
        return f"计算错误: {e}"


def search_web(query: str) -> str:
    """搜索工具（示例）"""
    return f"搜索 '{query}' 的结果：这是一个示例结果。"


# 使用示例
if __name__ == "__main__":
    print("=== LangChain 简单智能体示例 ===\n")
    
    # 注意：需要设置 OPENAI_API_KEY 才能运行
    # import os
    # os.environ["OPENAI_API_KEY"] = "your-key"
    
    print("创建智能体...")
    agent = SimpleAgent(system_prompt="你是一个有帮助的助手")
    
    # 添加工具
    print("添加计算器工具...")
    agent.add_tool(calculator, "calculator", "执行数学计算")
    
    print("添加搜索工具...")
    agent.add_tool(search_web, "search", "搜索互联网")
    
    # 执行
    print("\n执行智能体...")
    result = agent.invoke("请计算 15 * 23 + 100 等于多少？")
    print(f"结果: {result}")
