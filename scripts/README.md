# PromptHub Scripts

Useful scripts for managing your prompt library.

## 📋 Contents

- [sync-repos.sh](./sync-repos.sh) - Download and sync open-source prompt collections
- [prompthub.py](./prompthub.py) - PromptHub library management tool (WIP)

## 🚀 Quick Start

### Sync Repositories

```bash
chmod +x scripts/sync-repos.sh
./scripts/sync-repos.sh
```

This will download popular open-source prompt engineering repos to the `external/` directory.

## 📦 External Repos

The sync script will download:

- Prompt Engineering Guide (dair-ai)
- Awesome ChatGPT Prompts (English & Chinese)
- Awesome Prompt Engineering
- Claude-specific prompts
- And more...

## 🔄 Updating

Re-run the sync script anytime to pull the latest changes from all repositories.
