#!/bin/sh
# Link this folder into the skills folder of every assistant installed on this
# machine. Only assistants whose home folder already exists get a link, so the
# script never creates folders for tools you do not use.
set -e
root=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
linked=0
for base in "$HOME/.claude" "$HOME/.cursor" "$HOME/.codex" "$HOME/.agents"; do
  if [ -d "$base" ]; then
    mkdir -p "$base/skills"
    ln -sfn "$root" "$base/skills/startup-krediter"
    echo "linked  $base/skills/startup-krediter"
    linked=$((linked + 1))
  fi
done
if [ "$linked" -eq 0 ]; then
  echo "No Claude Code, Cursor or Codex folder found in $HOME."
  echo "Install one of them, run it once, then run this script again."
  exit 1
fi
echo "Done. Keep this folder where it is: the links point here."
