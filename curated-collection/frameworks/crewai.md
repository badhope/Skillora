# CrewAI

## 基本信息
- **GitHub**: https://github.com/joaomdmoura/crewAI
- **官网**: https://crewai.com
- **⭐ Stars**: 20k+
- **语言**: Python
- **维护者**: CrewAI Inc.

## 简介

CrewAI 是一个多智能体框架，强调用户友好性。它将多智能体协作建模为团队（crew）的角色扮演。你定义每个代理的角色、背景故事和目标，然后将它们组装成 crew 并分配任务。代理自然地进行交流并可以相互委托工作。

## 核心特点

- **角色化设计** - 直观的基于角色的智能体设计，映射到真实团队结构
- **自主团队** - Crew 模式，代理有真正的自主权
- **事件驱动流程** - Flow 模式，用于需要更多可预测性的生产工作负载
- **分层流程** - 自动生成管理代理来监督任务委派和审查输出
- **轻量级依赖** - 精简快速，没有繁重的外部库
- **A2A 协议支持** - 不断增长的智能体互操作性支持
- **大型开发者社区** - 100K+ 认证开发者

## 适用场景

- 研究团队协作
- 内容生产流水线
- 客户服务工作流
- 复杂业务流程自动化
- 多步骤任务分解与执行
- 需要专业分工的工作场景

## 快速开始

```bash
pip install crewai langchain-openai
```

```python
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

# 配置 LLM
llm = ChatOpenAI(model="gpt-4")

# 创建代理
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI',
    backstory='You are an expert in AI research.',
    llm=llm
)

writer = Agent(
    role='Content Writer',
    goal='Create compelling content about AI',
    backstory='You are a skilled writer.',
    llm=llm
)

# 创建任务
task1 = Task(
    description='Research AI trends',
    expected_output='A report on AI trends',
    agent=researcher
)

task2 = Task(
    description='Write a blog post',
    expected_output='A 500-word blog post',
    agent=writer,
    dependencies=[task1]
)

# 创建 Crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True
)

# 运行
result = crew.kickoff()
print(result)
```

## 学习资源

- [官方文档](https://docs.crewai.com)
- [CrewAI Academy](https://academy.crewai.com)
- [GitHub Examples](https://github.com/joaomdmoura/crewAI-examples)
- [YouTube 教程](https://www.youtube.com/@CrewAI)
- [Discord 社区](https://discord.gg/crewai)

## 推荐理由

CrewAI 的角色化设计非常直观，特别适合模拟真实团队协作。它的分层流程模式可以自动生成管理代理，适合复杂任务分解。学习曲线相对平缓，适合快速上手。如果你需要构建角色清晰的团队协作 AI，CrewAI 是绝佳选择。
