#!/usr/bin/env python3
"""Move agents/ repos into agents/{subcategory}/ subdirectories."""
import json
import subprocess
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parents[2]
TAXONOMY = REPO_ROOT / "_submodules" / "taxonomy.json"


def run(cmd, **kwargs):
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore", **kwargs)
    if result.returncode != 0:
        print(f"ERR {' '.join(map(str, cmd))}: {result.stderr.strip()}")
        return False
    return True


def batch_move(srcs, dest_dir, batch_size=25):
    dest_dir.mkdir(parents=True, exist_ok=True)
    for i in range(0, len(srcs), batch_size):
        batch = srcs[i:i + batch_size]
        run(["git", "mv", *batch, str(dest_dir)], cwd=REPO_ROOT)


def move_one_with_temp(src: Path, dest: Path):
    """Move src into dest, handling collisions where src basename equals a subcategory dir name."""
    if not src.exists():
        print(f"  skip missing {src}")
        return False
    dest_dir = dest.parent
    dest_dir.mkdir(parents=True, exist_ok=True)
    # If source basename equals an existing destination directory and source is inside it,
    # we are trying to move a directory into itself. Use a temp rename.
    temp = src.parent / (src.name + "-tmp-rename")
    if not run(["git", "mv", str(src), str(temp)], cwd=REPO_ROOT):
        return False
    # ensure dest parent (which was same as src) exists again after rename
    dest_dir.mkdir(parents=True, exist_ok=True)
    return run(["git", "mv", str(temp), str(dest)], cwd=REPO_ROOT)


def main():
    taxonomy = json.loads(TAXONOMY.read_text(encoding="utf-8"))
    agent_entries = {p: d for p, d in taxonomy.items() if d["category"] == "agents"}

    groups = defaultdict(list)
    moves = {}

    for path, data in agent_entries.items():
        tags = data["tags"]
        subcat = tags[0] if tags else "general"
        slug = path.split("/")[-1]
        new_path = f"agents/{subcat}/{slug}"

        base = new_path
        counter = 1
        while new_path in moves.values():
            new_path = f"{base}-{counter}"
            counter += 1
        groups[subcat].append((path, new_path, slug))
        moves[path] = new_path

    print(f"Reorganizing {len(agent_entries)} agents into {len(groups)} subcategories")

    for subcat, items in sorted(groups.items()):
        dest_dir = REPO_ROOT / "agents" / subcat
        print(f"  {subcat}: {len(items)} repos")

        # First, handle any repo whose slug exactly matches the subcategory name (would move into itself)
        normal = []
        for old, new, slug in items:
            old_path = REPO_ROOT / old
            new_path = REPO_ROOT / new
            if slug == subcat:
                # e.g. agents/browser -> agents/browser/browser
                if not move_one_with_temp(old_path, new_path):
                    continue
            else:
                normal.append((str(old_path), str(new_path), slug))

        # Batch move the rest
        srcs = [o for o, n, s in normal]
        if srcs:
            batch_move(srcs, dest_dir, batch_size=25)

    # Rewrite .gitmodules using git-config-like entries
    # Parse current .gitmodules and apply path/name changes for moved agents.
    import re
    gitmodules = REPO_ROOT / ".gitmodules"
    text = gitmodules.read_text(encoding="utf-8-sig", errors="ignore")
    lines = text.splitlines()
    out = []
    current = None
    for line in lines:
        m = re.match(r'^\[submodule\s+"([^"]+)"\]', line)
        if m:
            current = m.group(1)
        m = re.match(r'^(\s*path\s*=\s*)(.+?)\s*$', line)
        if m and current and current in moves:
            line = f"{m.group(1)}{moves[current]}"
            current = moves[current]
        m = re.match(r'^\[submodule\s+"([^"]+)"\]', line)
        if m and m.group(1) in moves:
            line = f'[submodule "{moves[m.group(1)]}"]'
        out.append(line)
    with open(gitmodules, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    # remove empty leftover dirs under agents (old direct subdirs)
    for child in (REPO_ROOT / "agents").iterdir():
        if child.is_dir() and child.name not in set(groups.keys()):
            try:
                child.rmdir()
                print(f"  removed empty {child}")
            except OSError:
                pass

    print(f"\nDone. Updated {len(moves)} paths.")


if __name__ == "__main__":
    main()
