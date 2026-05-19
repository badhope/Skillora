# Connectors - 外部服务连接器

这里提供了常用外部服务的连接器，方便智能体与外部系统交互。

---

## 📁 目录

```
connectors/
├── README.md
├── __init__.py
├── search_connector.py     # 搜索连接器
├── file_connector.py      # 文件连接器
└── web_connector.py       # 网页连接器
```

---

## 🚀 快速开始

### 搜索
```python
from connectors.search_connector import SearchConnector

search = SearchConnector(api_key="...")
results = search.search("AI 最新进展")
```

### 文件
```python
from connectors.file_connector import FileConnector

file_conn = FileConnector()
content = file_conn.read_file("document.txt")
```

---

## 📦 可用连接器

| 连接器 | 功能 | 状态 |
|--------|------|------|
| SearchConnector | 网络搜索 | ✅ |
| FileConnector | 文件读写 | ✅ |
| WebConnector | 网页抓取 | ✅ |
