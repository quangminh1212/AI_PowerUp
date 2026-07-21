#!/usr/bin/env python3
"""Normalize .gitmodules to match actual tracked file paths and remove duplicates."""
import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GITMODULES = REPO_ROOT / ".gitmodules"


def parse_gitmodules(path: Path):
    text = path.read_text(encoding="utf-8-sig", errors="ignore")
    entries = []
    current = {}
    for line in text.splitlines():
        m = re.match(r'^\[submodule\s+"([^"]+)"\]', line)
        if m:
            if current:
                entries.append(current)
            current = {"name": m.group(1)}
        m = re.match(r'^\s*path\s*=\s*(.+?)\s*$', line)
        if m:
            current["path"] = m.group(1)
        m = re.match(r'^\s*url\s*=\s*(.+?)\s*$', line)
        if m:
            current["url"] = m.group(1)
    if current:
        entries.append(current)
    return entries


def get_tracked_dirs():
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "HEAD"],
        capture_output=True, text=True, encoding="utf-8", errors="ignore", cwd=REPO_ROOT
    )
    dirs = {}
    for line in result.stdout.splitlines():
        if not line:
            continue
        p = Path(line)
        if p.name.lower().startswith("readme"):
            parent_posix = p.parent.as_posix()
            dirs[parent_posix.lower()] = parent_posix
    return dirs


def main():
    entries = parse_gitmodules(GITMODULES)
    tracked = get_tracked_dirs()
    seen = set()
    keep = []
    removed = []
    for e in entries:
        path = e.get("path") or e["name"]
        path_lower = path.lower()
        if path_lower not in tracked:
            removed.append(f"{path} (no tracked README)")
            continue
        actual = tracked[path_lower]
        if actual in seen:
            removed.append(f"{path} -> duplicate of {actual}")
            continue
        seen.add(actual)
        e["path"] = actual
        e["name"] = actual
        keep.append(e)

    blocks = []
    for e in keep:
        blocks.append(f'[submodule "{e["name"]}"]\n\tpath = {e["path"]}\n\turl = {e["url"]}\n')

    with open(GITMODULES, "w", encoding="utf-8") as f:
        f.writelines(blocks)

    print(f"Kept {len(keep)} entries, removed {len(removed)}:")
    for r in removed[:20]:
        print(f"  - {r}")
    if len(removed) > 20:
        print(f"  ... and {len(removed)-20} more")


if __name__ == "__main__":
    main()
