#!/usr/bin/env python3
"""Remove .gitmodules entries for folders that have no README file on disk."""
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GITMODULES = REPO_ROOT / ".gitmodules"


def parse(path: Path):
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r'^(\[submodule\s+"([^"]+)"\])', re.MULTILINE)
    parts = pattern.split(text)
    header = parts[0]
    entries = []
    i = 1
    while i < len(parts):
        name = parts[i+1]
        body = parts[i+2] if i+2 < len(parts) else ""
        pth = None
        m = re.search(r'^\s*path\s*=\s*(.+?)\s*$', body, re.MULTILINE)
        if m:
            pth = m.group(1)
        entries.append({"name": name, "path": pth, "block": f"[submodule \"{name}\"]" + body})
        i += 3
    return header, entries


def has_readme(path: Path):
    if not path.exists():
        return False
    return any(f.name.lower().startswith("readme") for f in path.iterdir() if f.is_file())


def main():
    header, entries = parse(GITMODULES)
    keep = []
    remove = []
    for e in entries:
        p = REPO_ROOT / e["path"] if e["path"] else None
        if p and has_readme(p):
            keep.append(e)
        else:
            remove.append(e["name"])

    with open(GITMODULES, "w", encoding="utf-8") as f:
        f.write(header)
        for e in keep:
            f.write(e["block"])

    print(f"Kept {len(keep)} entries, removed {len(remove)} empty/folderless:")
    for name in remove[:30]:
        print(f"  - {name}")
    if len(remove) > 30:
        print(f"  ... and {len(remove)-30} more")


if __name__ == "__main__":
    main()
