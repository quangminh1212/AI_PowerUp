#!/usr/bin/env python3
"""Fetch awesome-list markdown files from GitHub and extract GitHub repo URLs."""
import json
import re
import time
from pathlib import Path
from urllib.parse import urlparse
import requests

REPO_ROOT = Path(__file__).resolve().parents[2]
GITMODULES = REPO_ROOT / ".gitmodules"


def parse_gitmodules(path: Path):
    existing = set()
    if not path.exists():
        return existing
    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        m = re.match(r'^\s*url\s*=\s*(.+?)\s*$', line)
        if m:
            url = m.group(1).strip()
            if url.endswith(".git"):
                url = url[:-4]
            existing.add(url)
    return existing


def normalize_url(url: str):
    url = url.strip().rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]
    parsed = urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        return None
    owner, repo = parts[0], parts[1]
    repo = re.sub(r"[.,;:!?)\]+]+$", "", repo)
    if repo.endswith(".git"):
        repo = repo[:-4]
    if "." in repo:
        repo = repo.split(".")[0]
    return f"https://github.com/{owner}/{repo}"


def extract_github_urls(text: str):
    pattern = re.compile(r"https?://github\.com/([^/\s\)\"]+)/([^/\s\)\"]+)")
    found = set()
    for m in pattern.finditer(text):
        owner, repo = m.group(1), m.group(2)
        repo = re.sub(r"[.,;:!?)\]+]+$", "", repo)
        if repo.endswith(".git"):
            repo = repo[:-4]
        if "." in repo:
            repo = repo.split(".")[0]
        if not owner or not repo or owner in {"features", "docs", "platform"}:
            continue
        found.add(f"https://github.com/{owner}/{repo}")
    return found


def fetch_raw(url: str):
    raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    # If URL is github.com/OWNER/REPO, assume README.md on main branch
    if "/" in raw_url and raw_url.count("/") == 4:
        raw_url = f"{raw_url}/main/README.md"
    try:
        r = requests.get(raw_url, timeout=20)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(f"Failed to fetch {raw_url}: {e}")
        return None


def main():
    lists = [
        "https://github.com/Supersynergy/awesome-ai-agents-2025",
        "https://github.com/kelvins/awesome-mlops",
        "https://github.com/ashishpatel26/500-AI-Agents-Projects",
        "https://github.com/awesomelistsio/awesome-generative-ai",
        "https://github.com/dair-ai/Prompt-Engineering-Guide",
    ]

    existing = parse_gitmodules(GITMODULES)
    print(f"Existing unique URLs in .gitmodules: {len(existing)}")

    all_urls = set()
    for lst in lists:
        print(f"\nFetching {lst} ...")
        text = fetch_raw(lst)
        if not text:
            continue
        urls = extract_github_urls(text)
        print(f"  found {len(urls)} GitHub URLs")
        all_urls.update(urls)
        time.sleep(0.5)

    print(f"\nTotal unique URLs from lists: {len(all_urls)}")

    new_urls = sorted(all_urls - existing)
    print(f"New URLs not in .gitmodules: {len(new_urls)}")

    # Save candidates
    out = REPO_ROOT / "_submodules" / "scripts" / "awesome_candidates.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(new_urls, f, indent=2)
    print(f"Saved candidates to {out}")


if __name__ == "__main__":
    main()
