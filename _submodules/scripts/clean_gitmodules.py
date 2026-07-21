#!/usr/bin/env python3
"""Remove invalid and duplicate-URL entries from .gitmodules."""
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[2]
GITMODULES = REPO_ROOT / ".gitmodules"


def parse(path: Path):
    text = path.read_text(encoding="utf-8")
    # Split on submodule headers while keeping them
    pattern = re.compile(r'^(\[submodule\s+"([^"]+)"\])', re.MULTILINE)
    parts = pattern.split(text)
    header = parts[0]
    entries = []
    i = 1
    while i < len(parts):
        name = parts[i+1]
        body = parts[i+2] if i+2 < len(parts) else ""
        # Extract path and url from body
        pth = None
        url = None
        m = re.search(r'^\s*path\s*=\s*(.+?)\s*$', body, re.MULTILINE)
        if m:
            pth = m.group(1)
        m = re.search(r'^\s*url\s*=\s*(.+?)\s*$', body, re.MULTILINE)
        if m:
            url = m.group(1)
        entries.append({
            "name": name,
            "path": pth,
            "url": url,
            "block": f"[submodule \"{name}\"]" + body
        })
        i += 3
    return header, entries


def is_github_repo_url(url: str):
    if not url:
        return False
    if "github.com" not in url:
        return False
    if "?" in url or "#" in url:
        return False
    parsed = urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    return len(parts) >= 2 and parts[0] not in {"features", "docs", "marketplace", "stars", "sponsors"}


def normalize(url: str):
    url = url.rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]
    parsed = urlparse(url)
    parts = [p for p in parsed.path.split("/") if p][:2]
    return f"https://github.com/{'/'.join(parts)}" if len(parts) == 2 else None


def main():
    dry_run = "--dry-run" in sys.argv
    header, entries = parse(GITMODULES)
    seen_urls = set()
    keep = []
    removed = []

    for e in entries:
        if not e.get("url"):
            removed.append((e["name"], "missing url"))
            continue
        if not is_github_repo_url(e["url"]):
            removed.append((e["name"], f"invalid url: {e['url']}"))
            continue
        norm = normalize(e["url"])
        if norm in seen_urls:
            removed.append((e["name"], f"duplicate url: {e['url']}"))
            continue
        seen_urls.add(norm)
        keep.append(e)

    if not dry_run:
        with open(GITMODULES, "w", encoding="utf-8") as f:
            f.write(header)
            for e in keep:
                f.write(e["block"])

    print(f"Kept {len(keep)} submodules, removed {len(removed)}:")
    for name, reason in removed[:30]:
        print(f"  - {name}: {reason}")
    if len(removed) > 30:
        print(f"  ... and {len(removed)-30} more")


if __name__ == "__main__":
    main()
