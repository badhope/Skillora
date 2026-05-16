"""
PromptHub - Prompts Manager
Manage and organize your prompt library
"""

import json
import os
from pathlib import Path

class PromptHub:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.index_file = self.base_dir / "index.json"
        self.prompts = self._load_index()

    def _load_index(self):
        if self.index_file.exists():
            with open(self.index_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "version": "1.0.0",
            "platforms": {
                "international": [],
                "chinese": []
            },
            "collections": {}
        }

    def save_index(self):
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(self.prompts, f, indent=2, ensure_ascii=False)

    def list_platforms(self):
        print("International Platforms:")
        for p in self.prompts["platforms"]["international"]:
            print(f"  - {p['name']}")
        
        print("\nChinese Platforms:")
        for p in self.prompts["platforms"]["chinese"]:
            print(f"  - {p['name']}")

    def search_prompts(self, keyword):
        results = []
        # Search logic here
        return results

    def get_prompt(self, platform, category):
        pass

def main():
    hub = PromptHub()
    print("=== PromptHub Manager ===")
    hub.list_platforms()

if __name__ == "__main__":
    main()
