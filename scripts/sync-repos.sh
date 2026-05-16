#!/bin/bash
# PromptHub - Sync & Download Script
# Download and manage open-source prompt collections

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "======================================"
echo "   PromptHub - Sync & Download Tool"
echo "======================================"
echo ""

# Create external directory
mkdir -p external
cd external

# Function to clone or update a repo
clone_or_update() {
    local repo_url=$1
    local dir_name=$2

    if [ -d "$dir_name" ]; then
        echo -e "${GREEN}Updating $dir_name...${NC}"
        cd "$dir_name"
        git pull
        cd ..
    else
        echo -e "${GREEN}Cloning $dir_name...${NC}"
        git clone "$repo_url" "$dir_name"
    fi
}

echo "Downloading key prompt engineering repositories..."
echo ""

# Core prompt engineering resources
clone_or_update "https://github.com/dair-ai/Prompt-Engineering-Guide.git" "prompt-engineering-guide"
clone_or_update "https://github.com/f/awesome-chatgpt-prompts.git" "awesome-prompts"
clone_or_update "https://github.com/PlexPt/awesome-chatgpt-prompts-zh.git" "awesome-prompts-zh"
clone_or_update "https://github.com/promptslab/Awesome-Prompt-Engineering.git" "awesome-prompt-engineering"
clone_or_update "https://github.com/langgptai/awesome-claude-prompts.git" "awesome-claude-prompts"
clone_or_update "https://github.com/ai-boost/awesome-prompts.git" "ai-boost-awesome-prompts"

echo ""
echo -e "${GREEN}======================================${NC}"
echo -e "${GREEN}Download complete!${NC}"
echo ""
echo "Repos downloaded to external/ directory:"
ls -1
echo ""
echo "To update all repos, re-run this script."
