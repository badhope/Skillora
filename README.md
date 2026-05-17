# PromptHub - Universal Prompt Collection Platform

> The ultimate cross-platform prompt engineering resource hub. Collect, organize, and utilize prompts from global tech giants, open-source communities, and AI pioneers.

## 🌟 Features

- **Universal Coverage**: Prompts from all major platforms - 7+ international (OpenAI, Google, Microsoft, Anthropic, Meta, Cohere, Mistral/Groq) and 8+ Chinese platforms (Baidu, Alibaba, Tencent, ByteDance, 360, Zhipu, Xunfei, Xiaoice)
- **Cross-Platform**: Every prompt is adapted for multiple AI platforms
- **Open Source Curated**: Hand-picked from the best open-source prompt repositories
- **Category System**: Organized by use case, industry, and complexity
- **Community Driven**: Regular updates from trending prompts and new releases

## 📂 Structure

```
PromptHub/
├── international/          # International Tech Companies (7 platforms)
│   ├── openai/             # OpenAI (ChatGPT, GPT-4)
│   ├── google/             # Google (Gemini)
│   ├── microsoft/          # Microsoft (Copilot, Azure AI)
│   ├── anthropic/          # Anthropic (Claude)
│   ├── meta/               # Meta (Llama)
│   ├── cohere/             # Cohere (Command)
│   └── mistral-groq/       # Mistral & Groq
├── chinese/                # Chinese Tech Companies (8 platforms)
│   ├── baidu/              # Baidu (ERNIE Bot, Wenxin)
│   ├── alibaba/            # Alibaba (Tongyi, Qwen)
│   ├── tencent/            # Tencent (Hunyuan)
│   ├── bytedance/          # ByteDance (Doubao)
│   ├── 360/                # 360 (360GPT)
│   ├── zhipu/              # Zhipu (GLM)
│   ├── xunfei/             # Xunfei (Spark)
│   └── xiaoice/            # Xiaoice
├── prompts/                # Prompt Library by Domain
│   ├── development/        # Development & Coding
│   ├── creative-writing/   # Creative Writing & Content
│   ├── business/           # Business & Management
│   ├── domains/            # All Domains Comprehensive
│   └── universal-templates.md
├── opensource/             # Open Source Collections
│   ├── README.md
│   └── expanded-collection.md
├── frameworks/             # Framework Integrations
│   ├── README.md
│   └── integrations.md
├── examples/               # Quick Templates
│   ├── README.md
│   └── quick-templates.md
├── scripts/                # Utility Scripts
│   ├── README.md
│   ├── sync-repos.sh
│   └── prompthub.py
└── tools/                  # Prompt Engineering Tools
    └── README.md
```

## 🎯 Quick Start

Browse prompts by category or platform:

### International Platforms (7)

```markdown
# OpenAI / GPT Series
- [ChatGPT Best Practices](./international/openai/best-practices.md)
- [GPT-4 System Prompts](./international/openai/system-prompts.md)

# Google / Gemini Series
- [Gemini Prompting Guide](./international/google/best-practices.md)
- [Gemini Prompts](./international/google/gemini-prompts.md)

# Microsoft / Copilot Series
- [Copilot Prompt Framework](./international/microsoft/copilot-framework.md)
- [365 Copilot Templates](./international/microsoft/m365-prompts.md)

# Anthropic / Claude Series
- [Claude Prompt Engineering](./international/anthropic/best-practices.md)
- [System Prompt Examples](./international/anthropic/system-prompts.md)

# Meta / Llama Series
- [Llama Prompt Guide](./international/meta/README.md)

# More International Platforms
- [Cohere](./international/cohere/README.md)
- [Mistral & Groq](./international/mistral-groq/README.md)
```

### Chinese Platforms (8)

```markdown
# Baidu / Wenxin Series
- [ERNIE Bot Prompts](./chinese/baidu/ernie-prompts.md)
- [Wenxin Best Practices](./chinese/baidu/wenxin-guide.md)

# Alibaba / Tongyi Series
- [Qwen Prompt Templates](./chinese/alibaba/qwen-prompts.md)
- [Tongyi Best Practices](./chinese/alibaba/tongyi-guide.md)

# Tencent / Hunyuan Series
- [Hunyuan Prompt Guide](./chinese/tencent/hunyuan-guide.md)
- [API Prompt Templates](./chinese/tencent/api-templates.md)

# ByteDance / Doubao
- [Doubao Prompts](./chinese/bytedance/doubao-prompts.md)

# More Chinese Platforms
- [360 智脑](./chinese/360/README.md)
- [智谱 GLM](./chinese/zhipu/README.md)
- [讯飞星火](./chinese/xunfei/README.md)
- [小冰](./chinese/xiaoice/README.md)
```

## 📊 Platform Support Matrix

| Platform | Models | Prompt Format | Special Features |
|----------|--------|---------------|------------------|
| OpenAI | GPT-4, GPT-3.5 | JSON, Markdown | Function calling |
| Google | Gemini, PaLM | XML, Markdown | Multimodal |
| Microsoft | GPT-4, Copilot | Natural language | Office integration |
| Anthropic | Claude 3, 3.5 | XML tags | Constitutional AI |
| Meta | Llama 2, 3, 3.1 | Various | Open source |
| Cohere | Command R/R+ | Structured | Retrieval focused |
| Mistral | Mixtral, Mistral 7B | Various | Fast inference |
| Baidu | ERNIE 4.0, 3.5 | JSON | Chinese optimized |
| Alibaba | Qwen 2, 1.5 | JSON, Markdown | Bilingual |
| Tencent | Hunyuan | JSON | Long context |
| ByteDance | Doubao | JSON | Creative focus |
| 360 | 360GPT 4, Pro | JSON | Enterprise focus |
| Zhipu | GLM-4, 3 Turbo | Various | Open source compatible |
| Xunfei | Spark 4.0, Pro | Various | Voice capabilities |
| Xiaoice | Xiaoice | Conversational | Emotional intelligence |

## 🔥 Popular Prompts Categories

Explore by use case in our comprehensive prompt library:

- **[Development & Code](./prompts/development/README.md)**: Code generation, debugging, architecture
- **[Writing & Content](./prompts/creative-writing/README.md)**: Creative writing, marketing, copywriting
- **[Business & Management](./prompts/business/README.md)**: Strategy, marketing, operations
- **[All Domains](./prompts/domains/README.md)**: Education, health, design, and more
- **[Universal Templates](./prompts/universal-templates.md)**: Generic templates adaptable to any platform

## 📖 Open Source Collections & Frameworks

### Featured Open Source Projects

| Project | Stars | Focus | Link |
|---------|-------|-------|------|
| Prompt Engineering Guide | 50k+ | Learning | [GitHub](https://github.com/dair-ai/Prompt-Engineering-Guide) |
| Awesome ChatGPT Prompts EN | 30k+ | Role prompts | [GitHub](https://github.com/f/awesome-chatgpt-prompts) |
| Awesome ChatGPT Prompts CN | 50k+ | Chinese prompts | [GitHub](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) |
| LangChain | 85k+ | Framework | [GitHub](https://github.com/langchain-ai/langchain) |
| LlamaIndex | 33k+ | Data framework | [GitHub](https://github.com/run-llama/llama_index) |

### Framework Integrations

- [LangChain](./frameworks/integrations.md)
- [LlamaIndex](./frameworks/integrations.md)
- [Semantic Kernel](./frameworks/integrations.md)
- [Hugging Face](./frameworks/integrations.md)

## 🛠️ Utility Scripts

Sync popular open source repositories with:

```bash
cd scripts
chmod +x sync-repos.sh
./sync-repos.sh
```

## 🤝 Contributing

Contributions are welcome! Please read our contribution guidelines in [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

Special thanks to all the open-source prompt repositories, official documentation, and the broader AI community that makes this collection possible.

---

**PromptHub** - Empowering AI interactions across all platforms ✨

v3.0.0 - Last Updated: 2026-05-17
