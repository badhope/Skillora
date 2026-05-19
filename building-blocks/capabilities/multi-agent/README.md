# Multi-Agent - 多智能体能力

这里提供了多智能体协作的能力模块。

---

## 📁 目录

```
multi-agent/
├── README.md
├── __init__.py
└── simple_crew.py      # 简单多智能体团队
```

---

## 🚀 快速开始

```python
from capabilities.multi_agent.simple_crew import SimpleCrew

crew = SimpleCrew()
crew.add_agent("研究员", "研究最新进展")
crew.add_agent("作家", "写文章")
crew.add_task("写研究报告", "一份完整报告")
result = crew.run("AI 的最新进展")
```

---

## 💡 能力特点

- 角色化智能体设计
- 任务分配和协调
- 顺序和分层流程
