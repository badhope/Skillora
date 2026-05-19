# MetaGPT

## 基本信息
- **GitHub**: https://github.com/geekan/MetaGPT
- **官网**: https://docs.deepwisdom.ai/main/en/
- **⭐ Stars**: 47k+
- **语言**: Python
- **维护者**: DeepWisdom

## 简介

MetaGPT 是一个创新的多智能体框架，它将软件公司的工作流程引入 AI 智能体世界。与其他框架不同，MetaGPT 为每个智能体分配不同的角色（如产品经理、架构师、工程师等），并通过 SOP（标准操作程序）协调它们的工作，实现端到端的软件开发。

## 核心特点

### 创新架构
- **角色扮演系统** - 每个智能体都有明确的角色和职责
- **SOP 驱动** - "Code = SOP(Team)" 核心哲学
- **端到端流程** - 从需求到完整软件产品的全过程
- **ICLR 2024 Oral** - 被顶会接收并评为 LLM Agent 类别第一

### 智能体类型
- **产品经理 (PM)** - 需求分析和产品规划
- **架构师 (Architect)** - 系统设计
- **项目经理 (PM)** - 项目协调
- **工程师 (Engineer)** - 代码实现
- **质量保证 (QA)** - 测试用例

### 高级功能
- **Data Interpreter** - 强大的数据分析智能体
- **多 LLM 支持** - 可为不同角色分配不同模型
- **序列化支持** - 状态保存和恢复
- **多语言支持** - 中文、英文等

## 适用场景

- 完整软件开发生命周期自动化
- Web 应用开发
- 数据分析工具
- 游戏开发
- 研究和原型验证
- 需要多角色协作的复杂任务

## 快速开始

```bash
# 安装
pip install --upgrade metagpt

# 初始化配置
metagpt --init-config
# 编辑 ~/.metagpt/config2.yaml
```

```python
from metagpt.roles.product_manager import ProductManager
from metagpt.roles.engineer import Engineer
from metagpt.roles.architect import Architect
from metagpt.teams import Team

async def main():
    team = Team()
    team.hire([
        ProductManager(),
        Architect(),
        Engineer()
    ])
    
    team.run_project("Build a todo app with React")
    await team.run(n_round=3)

asyncio.run(main())
```

### Docker 运行
```bash
docker pull metagpt/metagpt:latest
docker run --rm -e METAGPT_API_KEY=your-key metagpt/metagpt:latest
```

## 学习资源

- [官方文档](https://docs.deepwisdom.ai/main/en/)
- [GitHub Examples](https://github.com/geekan/MetaGPT/tree/main/examples)
- [研究论文](https://arxiv.org/abs/2308.00352)
- [Discord 社区](https://discord.gg/metagpt)

## 推荐理由

MetaGPT 是目前最有创意的多智能体框架之一。它的"软件公司"概念让智能体协作变得非常直观。ICLR 2024 Oral 的荣誉证明了它的学术价值。对于想要构建复杂多智能体系统的开发者，MetaGPT 提供了独特的视角和强大的功能。
