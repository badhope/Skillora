# 🔍 Research Assistant - 研究助手

一个带知识库的问答系统，可以基于文档回答问题。

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
research-agent/
├── main.py           # 主程序
├── requirements.txt  # 依赖
├── README.md         # 说明
└── docs/           # 文档目录（可以放你的文档）
```

---

## 💡 功能特点

- ✅ 文档问答（RAG）
- ✅ 支持添加文档
- ✅ 带记忆功能
- ✅ 文档列表管理
- ✅ 友好的交互界面

---

## 🛠️ 使用说明

运行 `main.py` 后，你可以：
- 直接提问：`什么是 AI？`
- 添加文档：`/add 这是一些知识...`
- 查看文档：`/docs`
- 清空文档：`/clear`
- 清空对话：`/clear-chat`
- 查看历史：`/history`
- 退出：`/quit`

---

## 📋 依赖

- openai

---

## 🎯 下一步

- 在 `docs/` 目录放入你的文档
- 修改 `main.py` 自定义行为
