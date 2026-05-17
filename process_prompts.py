#!/usr/bin/env python3
import re
import json
import os
from pathlib import Path
from typing import List, Dict

CATEGORIES = {
    "development": "开发",
    "writing": "写作",
    "business": "商业",
    "life": "生活",
    "creative": "创意"
}

def extract_markdown_prompts(file_path: str) -> List[Dict]:
    """Extract prompts from markdown files with <details> format"""
    prompts = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'<details>\s*<summary><strong>([^<]+)</strong></summary>\s*##\s*([^\n]+)\s*[^\n]*\s*(?:Contributed by[^\n]*\s*)?```md\s*([\s\S]*?)```\s*</details>'
    matches = re.findall(pattern, content)

    for match in matches:
        title_en, title_clean, prompt = match
        prompts.append({
            "title_en": title_en.strip(),
            "title_zh": title_clean.strip(),
            "prompt": prompt.strip()
        })

    return prompts

def extract_json_prompts(file_path: str) -> List[Dict]:
    """Extract prompts from JSON files"""
    prompts = []
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        if isinstance(item, dict) and 'act' in item and 'prompt' in item:
            prompts.append({
                "title_en": item['act'],
                "title_zh": item['act'],
                "prompt": item['prompt'].strip()
            })

    return prompts

def extract_txt_prompts(file_path: str) -> List[Dict]:
    """Extract prompts from text files"""
    prompts = []
    filename = Path(file_path).stem
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    if content:
        prompts.append({
            "title_en": filename.replace('_', ' '),
            "title_zh": filename.replace('_', ' '),
            "prompt": content
        })

    return prompts

def categorize_prompt(prompt: str, title: str) -> str:
    """Categorize prompt based on content"""
    prompt_lower = (prompt + " " + title).lower()

    dev_keywords = ['code', 'programming', 'developer', 'software', 'script', 'function',
                    'database', 'sql', 'api', 'frontend', 'backend', 'algorithm', 'debug',
                    'html', 'css', 'javascript', 'python', 'java', 'react', 'node', 'git',
                    'terminal', 'linux', 'excel', 'spreadsheet', 'data analysis', 'ml ', 'machine learning']
    writing_keywords = ['write', 'essay', 'article', 'blog', 'story', 'book', 'novel', 'poem',
                       'translator', 'translate', 'grammar', 'spell', 'improve', 'edit', 'proofread',
                       'resume', 'cover letter', 'email', 'copywrite']
    business_keywords = ['business', 'marketing', 'sales', 'strategy', 'customer', 'product',
                        'management', 'consultant', 'advisor', 'investment', 'financial', 'hr',
                        'recruit', 'interview', 'career', 'startup', 'entrepreneur']
    life_keywords = ['life', 'coach', 'motivation', 'health', 'fitness', 'diet', 'travel',
                    'recipe', 'cook', 'relationship', 'psychology', 'advice', 'habit']
    creative_keywords = ['creative', 'art', 'design', 'music', 'game', 'movie', 'film',
                       'advertisement', 'brand', 'logo', 'illustration', 'photo']

    for keyword in dev_keywords:
        if keyword in prompt_lower:
            return "development"

    for keyword in writing_keywords:
        if keyword in prompt_lower:
            return "writing"

    for keyword in business_keywords:
        if keyword in prompt_lower:
            return "business"

    for keyword in life_keywords:
        if keyword in prompt_lower:
            return "life"

    for keyword in creative_keywords:
        if keyword in prompt_lower:
            return "creative"

    return "creative"

def transform_to_cross_platform(prompt: str, title: str) -> str:
    """Transform prompt to be cross-platform compatible"""
    prompt = re.sub(r'I want you to act as', '请扮演', prompt)
    prompt = re.sub(r'I want you to be a', '请担任', prompt)
    prompt = re.sub(r'I want you to', '请', prompt)
    prompt = re.sub(r'Please act as', '请扮演', prompt)
    prompt = re.sub(r'as a', '作为', prompt)
    prompt = re.sub(r'ChatGPT|chatgpt', 'AI助手', prompt)
    prompt = re.sub(r'Claude|claude', 'AI助手', prompt)
    prompt = re.sub(r'you are an?\s*', '', prompt, flags=re.IGNORECASE)

    prompt = re.sub(r'\{([^{}]+)\}', r'[\1]', prompt)

    return prompt.strip()

def create_prompt_document(prompts: List[Dict], category: str, lang: str = "zh") -> str:
    """Create a markdown document for a category"""
    category_zh = CATEGORIES.get(category, category)

    doc = f"# {category_zh}提示词集合\n\n"
    doc += f"> 跨平台AI助手通用提示词 - 适用于OpenAI、Claude、Gemini、文心一言、通义千问等\n\n"
    doc += f"---\n\n"

    for i, p in enumerate(prompts, 1):
        title = p.get('title_zh', p.get('title_en', f'提示词{i}'))
        prompt_text = p.get('prompt', '')

        doc += f"## {i}. {title}\n\n"
        doc += f"**提示词：**\n\n"
        doc += f"```\n{prompt_text}\n```\n\n"
        doc += f"---\n\n"

    return doc

def main():
    all_prompts = []

    print("开始处理提示词仓库...")

    english_md = "/workspace/external/awesome-chatgpt-prompts/PROMPTS.md"
    if os.path.exists(english_md):
        print(f"处理: {english_md}")
        prompts = extract_markdown_prompts(english_md)
        all_prompts.extend(prompts)
        print(f"  - 提取了 {len(prompts)} 个英文提示词")

    chinese_json = "/workspace/external/awesome-chatgpt-prompts-zh/prompts-zh.json"
    if os.path.exists(chinese_json):
        print(f"处理: {chinese_json}")
        prompts = extract_json_prompts(chinese_json)
        all_prompts.extend(prompts)
        print(f"  - 提取了 {len(prompts)} 个中文提示词")

    awesome_prompts_dir = "/workspace/external/awesome-prompts/prompts"
    if os.path.exists(awesome_prompts_dir):
        print(f"处理目录: {awesome_prompts_dir}")
        count = 0
        for file in os.listdir(awesome_prompts_dir):
            file_path = os.path.join(awesome_prompts_dir, file)
            if file.endswith(('.txt', '.md')):
                prompts = extract_txt_prompts(file_path)
                all_prompts.extend(prompts)
                count += len(prompts)
        print(f"  - 提取了 {count} 个 awesome-prompts 提示词")

    claude_readme = "/workspace/external/awesome-claude-prompts/README.md"
    if os.path.exists(claude_readme):
        print(f"处理: {claude_readme}")
        prompts = extract_markdown_prompts(claude_readme)
        all_prompts.extend(prompts)
        print(f"  - 提取了 {len(prompts)} 个 Claude 提示词")

    print(f"\n总计提取: {len(all_prompts)} 个提示词")

    categorized = {cat: [] for cat in CATEGORIES.keys()}

    for prompt in all_prompts:
        title = prompt.get('title_zh') or prompt.get('title_en', '')
        prompt_text = prompt.get('prompt', '')
        category = categorize_prompt(prompt_text, title)

        transformed_prompt = transform_to_cross_platform(prompt_text, title)

        categorized[category].append({
            "title_en": prompt.get('title_en', title),
            "title_zh": title,
            "prompt": transformed_prompt,
            "original_prompt": prompt_text
        })

    print("\n分类统计:")
    for cat, prompts_list in categorized.items():
        print(f"  - {CATEGORIES[cat]}: {len(prompts_list)} 个")

    output_base = "/workspace/prompts/library"
    os.makedirs(output_base, exist_ok=True)

    for category, prompts_list in categorized.items():
        if prompts_list:
            doc = create_prompt_document(prompts_list, category)
            output_file = os.path.join(output_base, f"{category}.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(doc)
            print(f"\n生成: {output_file}")

    json_output = os.path.join(output_base, "all_prompts.json")
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(categorized, f, ensure_ascii=False, indent=2)
    print(f"\n生成: {json_output}")

    print("\n处理完成!")

if __name__ == "__main__":
    main()
