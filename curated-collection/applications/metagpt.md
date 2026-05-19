# MetaGPT

## 基本信息
- **GitHub**: https://github.com/geekan/MetaGPT
- **官网**: https://docs.deepwisdom.ai/main/en/
- **⭐ Stars**: 47k+
- **语言**: Python
- **维护者**: DeepWisdom

## 简介

MetaGPT 是一个创新的多智能体框架，将软件公司的工作流程引入 AI 智能体世界。每个智能体扮演不同的角色（产品经理、架构师、工程师等），通过 SOP（标准操作程序）协调工作。

## 核心特点

### 创新架构
- **角色扮演系统**: 产品经理、架构师、工程师、QA
- **SOP 驱动**: "Code = SOP(Team)"
- **端到端流程**: 从需求到完整产品

### 高级功能
- **Data Interpreter**: 强大的数据分析能力
- **多 LLM 支持**: 可为不同角色分配不同模型
- **序列化支持**: 状态保存和恢复

### 研究价值
- **ICLR 2024 Oral**: 被顶会接收

## 适用场景

- 软件开发生命周期自动化
- Web 应用开发
- 数据分析工具
- 研究和原型验证

## 快速开始

```bash
pip install metagpt
```

```python
from metagpt.roles.product_manager import ProductManager
from metagpt.teams import Team

async def main():
    team = Team()
    team.hire([ProductManager()])
    team.run_project("Build a todo app")

asyncio.run(main())
```

## 学习资源

- [官方文档](https://docs.deepwisdom.ai/main/en/)
- [GitHub Examples](https://github.com/geekan/MetaGPT/tree/main/examples)
- [研究论文](https://arxiv.org/abs/2308.00352)

## 推荐理由

MetaGPT 是目前最有创意的多智能体框架之一。它的"软件公司"概念让智能体协作变得非常直观。
