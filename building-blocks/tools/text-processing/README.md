# Text Processing Tools

Common text processing utilities for AI agent development.

---

## 📁 Directory Structure

```
text-processing/
├── README.md
├── __init__.py
├── summarizer.py         # Text Summarization
├── keyword_extractor.py  # Keyword Extraction
└── sentiment_analyzer.py # Sentiment Analysis
```

---

## 🚀 Quick Start

```python
from tools.text_processing.summarizer import Summarizer
from tools.text_processing.sentiment_analyzer import SentimentAnalyzer

# Text Summarization
summarizer = Summarizer()
summary = summarizer.summarize("Long text content...")
print(summary)

# Sentiment Analysis
analyzer = SentimentAnalyzer()
result = analyzer.analyze("I love this product!")
print(result)
```

---

## 💡 Features

| Tool | Description | Status |
|------|-------------|--------|
| Summarizer | Text summarization | ✅ |
| KeywordExtractor | Keyword extraction | ✅ |
| SentimentAnalyzer | Sentiment analysis | ✅ |

---

## 🔧 Installation

```bash
pip install transformers torch
```

---

# Text Processing - 文本处理工具

常用的文本处理功能模块。

---

## 📁 目录结构

```
text-processing/
├── README.md
├── __init__.py
├── summarizer.py         # 文本摘要
├── keyword_extractor.py  # 关键词提取
└── sentiment_analyzer.py # 情感分析
```

---

## 🚀 快速开始

```python
from tools.text_processing.summarizer import Summarizer
from tools.text_processing.sentiment_analyzer import SentimentAnalyzer

# 文本摘要
summarizer = Summarizer()
summary = summarizer.summarize("长文本内容...")
print(summary)

# 情感分析
analyzer = SentimentAnalyzer()
result = analyzer.analyze("我喜欢这个产品！")
print(result)
```

---

## 💡 功能

| 工具 | 说明 | 状态 |
|------|------|------|
| Summarizer | 文本摘要生成 | ✅ |
| KeywordExtractor | 关键词提取 | ✅ |
| SentimentAnalyzer | 情感分析 | ✅ |

---

## 🔧 安装

```bash
pip install transformers torch
```