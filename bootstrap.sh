#!/bin/sh
set -e
root=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
ln -sfn "$root" "$HOME/.cursor/skills/startup-krediter"
ln -sfn "$root" "$HOME/.claude/skills/startup-krediter"
ln -sfn "$root" "$HOME/.codex/skills/startup-krediter"
ln -sfn "$root" "$HOME/.agents/skills/startup-krediter"
echo "$root"
