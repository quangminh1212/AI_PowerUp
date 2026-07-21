#!/usr/bin/env python3
"""Search GitHub for AI repos with > min_stars and collect missing URLs."""
import json
import re
import subprocess
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GITMODULES = REPO_ROOT / ".gitmodules"
MIN_STARS = 5000
QUERIES = [
    "AI",
    "LLM",
    "large-language-model",
    "machine-learning",
    "deep-learning",
    "generative-ai",
    "agent",
    "RAG",
    "stable-diffusion",
    "MCP",
    "voice",
    "vision",
    "prompt-engineering",
    "fine-tuning",
    "transformer",
    "PyTorch",
    "TensorFlow",
]


def existing_urls(path: Path):
    urls = set()
    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        m = re.match(r'^\s*url\s*=\s*(.+?)\s*$', line)
        if m:
            u = m.group(1).strip()
            if u.endswith(".git"):
                u = u[:-4]
            urls.add(u)
    return urls


def search(query: str, min_stars: int, limit: int = 1000):
    cmd = [
        "gh", "search", "repos",
        "--stars", f">{min_stars}",
        "--sort", "stars",
        "--order", "desc",
        "--limit", str(limit),
        "--json", "fullName,stargazersCount,description",
        query,
    ]
    print(f"[search] {query} ...")
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    if result.returncode != 0:
        print(f"  error: {result.stderr.strip()}")
        return []
    try:
        data = json.loads(result.stdout)
    except Exception as e:
        print(f"  json error: {e}")
        return []
    print(f"  got {len(data)} results")
    return data


def main():
    existing = existing_urls(GITMODULES)
    found = {}
    for q in QUERIES:
        for item in search(q, MIN_STARS):
            full = item["fullName"]
            stars = item.get("stargazersCount", 0)
            url = f"https://github.com/{full}"
            if url in existing or url in found:
                continue
            # Skip non-AI junk like general programming interview guides
            desc = (item.get("description") or "").lower()
            name = full.split("/")[-1].lower()
            ai_signals = [
                "ai", "llm", "agent", "model", "gpt", "claude", "llama", "stable-diffusion",
                "rag", "prompt", "embedding", "transformer", "diffusion", "multimodal",
                "nlp", "cv", "computer-vision", "speech", "voice", "mcp", "fine-tune",
                "llama.cpp", "ollama", "langchain", "langgraph", "autogpt", "openai",
                "pytorch", "tensorflow", "huggingface", "eval", "benchmark", "dataset",
                "deep-learning", "machine-learning", "generative", "synthetic",
            ]
            if not any(s in desc or s in name for s in ai_signals):
                continue
            found[url] = stars
        time.sleep(7)  # ~10 searches/min for auth gh

    out = sorted(found.items(), key=lambda x: -x[1])
    out_path = REPO_ROOT / "_submodules" / "scripts" / "github_stars_candidates.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump([u for u, s in out], f, indent=2)
    print(f"\nCollected {len(out)} new AI repos with >{MIN_STARS} stars. Saved to {out_path}")
    for u, s in out[:20]:
        print(f"  {s:>7} {u}")


if __name__ == "__main__":
    main()
