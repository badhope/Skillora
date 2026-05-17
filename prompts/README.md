# PromptHub 提示词库

最全的跨平台提示词库，覆盖所有领域和场景。

## 📋 目录

- [平台覆盖](#平台覆盖)
- [分类体系](#分类体系)
- [快速开始](#快速开始)
- [使用指南](#使用指南)
- [贡献指南](#贡献指南)

## 🌐 平台覆盖

### 国际平台（7个）
- [OpenAI (GPT系列)](/workspace/international/openai/README.md)
- [Google (Gemini)](/workspace/international/google/README.md)
- [Microsoft (Copilot)](/workspace/international/microsoft/README.md)
- [Anthropic (Claude)](/workspace/international/anthropic/README.md)
- [Meta (Llama)](/workspace/international/meta/README.md)
- [Cohere](/workspace/international/cohere/README.md)
- [Mistral & Groq](/workspace/international/mistral-groq/README.md)

### 国内平台（8个）
- [百度 (文心/ERNIE)](/workspace/chinese/baidu/README.md)
- [阿里 (通义/千问)](/workspace/chinese/alibaba/README.md)
- [腾讯 (混元)](/workspace/chinese/tencent/README.md)
- [字节 (豆包)](/workspace/chinese/bytedance/README.md)
- [360 智脑](/workspace/chinese/360/README.md)
- [智谱 (GLM)](/workspace/chinese/zhipu/README.md)
- [讯飞 (星火)](/workspace/chinese/xunfei/README.md)
- [小冰](/workspace/chinese/xiaoice/README.md)

## 📚 分类体系

### 按领域分类
- [技术与开发](/workspace/prompts/development/README.md)
- [创意写作](/workspace/prompts/creative-writing/README.md)
- [商业与管理](/workspace/prompts/business/README.md)
- [各领域综合](/workspace/prompts/domains/README.md)

### 其他资源
- [开源提示词收集](/workspace/opensource/README.md)
- [框架集成](/workspace/frameworks/README.md)
- [工具脚本](/workspace/scripts/README.md)
- [快速模板](/workspace/examples/README.md)

## 🚀 快速开始

### 寻找合适的提示词

1. 根据使用的平台进入对应文件夹
2. 选择任务领域
3. 复制提示词模板
4. 按需求修改使用

### 平台适配

大部分提示词都可以跨平台使用，只需要：
1. 调整模型名称
2. 保持核心内容不变
3. 根据平台特点微调

### 示例使用

```python
# 复制提示词后使用
prompt = """
你是一位 Python 专家...

[任务描述]
"""
```

## 💡 使用指南

### 通用提示词技巧

1. **明确角色** - 指定 AI 扮演的角色
2. **清晰任务** - 详细描述要完成的任务
3. **设定要求** - 明确输出格式和质量要求
4. **提供示例** - 展示期望的输出格式
5. **设定约束** - 说明不能做什么

### 不同平台适配

#### 国际平台
主要是格式差异，核心内容通用

#### 国内平台
中文平台对中文理解更好，可适当调整表达

### 提示词迭代

1. 先用基础提示词
2. 根据结果调整
3. 逐步优化完善
4. 保存最佳版本

## 🔄 同步开源提示词

使用提供的脚本同步优质开源提示词：

```bash
cd /workspace/scripts
chmod +x sync-repos.sh
./sync-repos.sh
```

## 🤝 贡献指南

欢迎贡献提示词！请参考：
- [CONTRIBUTING.md](/workspace/CONTRIBUTING.md)

贡献方式：
1. Fork 项目
2. 添加提示词
3. 提交 PR
4. 审核合并

## 📦 项目结构

```
PromptHub/
├── international/          # 国际平台提示词
├── chinese/               # 国内平台提示词
├── prompts/               # 分类提示词库
│   ├── domains/          # 各领域提示词
│   ├── development/      # 开发提示词
│   ├── creative-writing/ # 写作提示词
│   └── business/         # 商业提示词
├── frameworks/           # 框架集成
├── opensource/           # 开源收集
├── examples/             # 示例模板
├── scripts/              # 工具脚本
└── ...
```

## 📖 更多资源

- [主 README](/workspace/README.md)
- [开源项目收集](/workspace/opensource/expanded-collection.md)
- [框架集成指南](/workspace/frameworks/integrations.md)

---

**PromptHub** - 让每个平台都能用上优质提示词！✨
