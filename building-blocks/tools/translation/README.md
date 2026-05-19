# Translation Tools

Connectors for popular translation services.

---

## 📁 Directory Structure

```
translation/
├── README.md
├── __init__.py
├── google_translate.py    # Google Translate
├── baidu_translate.py     # Baidu Translate
└── openai_translate.py    # OpenAI Translation
```

---

## 🚀 Quick Start

```python
from tools.translation.google_translate import GoogleTranslator

translator = GoogleTranslator(api_key="...")
result = translator.translate("Hello", target_language="zh")
print(result)
```

---

## 💡 Supported Services

| Service | Description | Status |
|---------|-------------|--------|
| Google Translate | Google Translation API | ✅ |
| Baidu Translate | Baidu Translation API | ✅ |
| OpenAI Translate | Translation using OpenAI models | ✅ |

---

# Translation Tools - 翻译工具

常用翻译服务的连接器模块。

---

## 📁 目录结构

```
translation/
├── README.md
├── __init__.py
├── google_translate.py    # Google 翻译
├── baidu_translate.py     # 百度翻译
└── openai_translate.py    # OpenAI 翻译
```

---

## 🚀 快速开始

```python
from tools.translation.google_translate import GoogleTranslator

translator = GoogleTranslator(api_key="...")
result = translator.translate("Hello", target_language="zh")
print(result)
```

---

## 💡 支持的翻译服务

| 服务 | 说明 | 状态 |
|------|------|------|
| Google Translate | Google 翻译 API | ✅ |
| Baidu Translate | 百度翻译 API | ✅ |
| OpenAI Translate | 使用 OpenAI 模型翻译 | ✅ |