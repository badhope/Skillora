# 💬 Customer Support - 客服机器人

一个基于知识库的智能客服机器人，可以处理常见客户问题。

---

## 🚀 快速开始

### 安装
```bash
pip install -r requirements.txt
```

### 运行
```bash
python main.py
```

---

## 📁 目录结构

```
customer-support/
├── main.py           # 主程序
├── knowledge.py      # 知识库管理
├── responses.py      # 回复模板
├── requirements.txt  # 依赖
└── README.md         # 说明
```

---

## 💡 功能特点

- ✅ 知识库问答
- ✅ 多轮对话支持
- ✅ 常见问题自动回复
- ✅ 转人工选项
- ✅ 满意度调查

---

## 🛠️ 使用说明

运行 `main.py` 后，你可以：
- 直接提问：`这个产品怎么购买？`
- 查看知识库：`/knowledge`
- 清空对话：`/clear`
- 退出：`/quit`

---

## 📋 依赖

- openai

---

## 🎯 下一步

- 修改 `knowledge.py` 添加你的知识库
- 修改 `responses.py` 自定义回复模板
- 集成到你的客服系统
