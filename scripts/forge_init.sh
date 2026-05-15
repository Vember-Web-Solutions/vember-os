#!/bin/bash
# 🔱 VEMBER-OS: FORGE INITIALIZATION

# 1. Load standard user bash settings (so you don't lose your 'ls' colors, etc)
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

# 2. Force Vember Virtual Environment Activation
if [ -d "./.venv" ]; then
    source ./.venv/bin/activate
    export VIRTUAL_ENV_PROMPT="[🔱 FORGE] "
fi

# 3. Rebrand the Terminal Title
echo -ne "\033]0;🔱 VEMBER OS // FORGE\007"

# 4. Auto-Engage the Developer Console
uv run python scripts/vember_cli.py