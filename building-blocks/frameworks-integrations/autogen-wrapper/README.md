# AutoGen Wrapper - AutoGen 框架包装

这是一个简化版的 Microsoft AutoGen 集成，方便快速使用 AutoGen 的多智能体功能。

---

## 🚀 快速开始

### 安装依赖
```bash
pip install pyautogen
```

### 使用示例

```python
from autogen_wrapper import SimpleChat

chat = SimpleChat(api_key="your-key")
chat.add_agent("助手", is_assistant=True)
chat.add_agent("用户", is_assistant=False)
chat.start("解释什么是机器学习")
```

---

## 📚 模块说明

### SimpleChat
简单的多智能体对话系统。

---

## 🔗 相关资源

- [AutoGen 官方文档](https://microsoft.github.io/autogen)
- [AgentHome 中的 AutoGen 文档](../../curated-collection/frameworks/autogen.md)
