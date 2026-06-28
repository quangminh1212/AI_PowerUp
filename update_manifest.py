#!/usr/bin/env python3
"""Regenerate repos.json from current .gitmodules (run after adding temp submodules)."""
import subprocess, json, re
from pathlib import Path

ROOT = Path(__file__).parent
out = subprocess.check_output(
    ['git', 'config', '--file', '.gitmodules', '--get-regexp', r'submodule\..*\.(path|url)'],
    text=True
)
entries = {}
for line in out.strip().split('\n'):
    m = re.match(r'submodule\.([^.]+)\.(path|url)\s+(.+)', line)
    if m:
        name, key, val = m.groups()
        entries.setdefault(name, {})[key] = val.strip()

manifest = [{'path': e['path'], 'url': e['url']} for e in entries.values()]
manifest.sort(key=lambda x: x['path'])

with open(ROOT / 'repos.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Updated repos.json with {len(manifest)} repos")