#!/usr/bin/env python3
"""Clone all repos from repos.json as shallow submodules (reference only)."""
import json, subprocess, sys, os
from pathlib import Path

ROOT = Path(__file__).parent
manifest = json.loads((ROOT / "repos.json").read_text(encoding="utf-8"))

for item in manifest:
    path = Path(item["path"])
    url = item["url"]
    if path.exists():
        print(f"SKIP {path} (exists)")
        continue
    path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["git", "clone", "--depth", "1", "--single-branch", url, str(path)]
    print(f"CLONE {url} -> {path}")
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"FAIL {url}: {e.stderr[-200:]}", file=sys.stderr)

print("Done.")