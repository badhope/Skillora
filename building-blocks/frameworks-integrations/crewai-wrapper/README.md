# CrewAI Wrapper - CrewAI 框架包装

这是一个简化版的 CrewAI 集成，方便快速使用 CrewAI 的多智能体功能。

---

## 🚀 快速开始

### 安装依赖
```bash
pip install crewai crewai-tools
```

### 使用示例

```python
from crewai_wrapper import SimpleCrew

crew = SimpleCrew(api_key="your-key")
crew.add_agent("研究员", "研究最新的 AI 进展")
crew.add_agent("作家", "写科技文章")
crew.run("写一篇关于 AI 的文章")
```

---

## 📚 模块说明

### SimpleCrew
简单的多智能体团队。

---

## 🔗 相关资源

- [CrewAI 官方文档](https://docs.crewai.com)
- [AgentHome 中的 CrewAI 文档](../../curated-collection/frameworks/crewai.md)
