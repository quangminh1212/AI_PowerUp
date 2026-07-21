#!/usr/bin/env python3
"""Parse GitHub URLs from markdown awesome-lists and append [submodule] entries to .gitmodules."""
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[2]
GITMODULES = REPO_ROOT / ".gitmodules"


def parse_gitmodules(path: Path):
    """Return set of existing URLs and dict of path->url from .gitmodules."""
    existing_urls = set()
    existing_paths = {}
    if not path.exists():
        return existing_urls, existing_paths
    current_name = current_path = current_url = None
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.rstrip()
        m = re.match(r'^\[submodule\s+"([^"]+)"\]', line)
        if m:
            if current_url:
                existing_urls.add(current_url)
            if current_path and current_url:
                existing_paths[current_path] = current_url
            current_name = m.group(1)
            current_path = current_url = None
            continue
        m = re.match(r'^\s*path\s*=\s*(.+?)\s*$', line)
        if m:
            current_path = m.group(1)
            continue
        m = re.match(r'^\s*url\s*=\s*(.+?)\s*$', line)
        if m:
            current_url = m.group(1)
    if current_url:
        existing_urls.add(current_url)
    if current_path and current_url:
        existing_paths[current_path] = current_url
    return existing_urls, existing_paths


def normalize_github_url(url: str):
    url = url.strip().rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]
    if "github.com" not in url:
        return None
    parsed = urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        return None
    owner, repo = parts[0], parts[1]
    # Strip trailing punctuation/markdown artifacts
    repo = re.sub(r"[.,;:!?)\]+]+$", "", repo)
    if repo.endswith(".git"):
        repo = repo[:-4]
    if "." in repo:
        repo = repo.split(".")[0]
    if not owner or not repo:
        return None
    return f"https://github.com/{owner}/{repo}.git"


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
        if not owner or not repo or owner in {"platform", "docs"}:
            continue
        url = f"https://github.com/{owner}/{repo}.git"
        found.add(url)
    return found


def suggest_category(owner: str, repo: str, markdown: str):
    lower = (owner + " " + repo).lower()
    if any(k in lower for k in ["voice", "speech", "audio", "tts", "stt", "ultravox", "pipecat", "bosca", "livekit"]):
        return "audio"
    if any(k in lower for k in ["vision", "image", "diffusion", "yolo", "segment", "depth"]):
        return "vision"
    if any(k in lower for k in ["video"]):
        return "video"
    if any(k in lower for k in ["multimodal", "cog", "florence", "glm-4v", "clip"]):
        return "multimodal"
    if any(k in lower for k in ["memory", "mem0", "zep", "letta"]):
        return "memory"
    if any(k in lower for k in ["mcp", "context-protocol"]):
        return "mcp-servers"
    if any(k in lower for k in ["rag", "llamaindex", "unstructured", "chroma", "qdrant", "weaviate", "ragflow"]):
        return "data-rag"
    if any(k in lower for k in ["model", "llm", "gpt", "claude", "gemini", "qwen", "deepseek", "phi", "llama", "mixtral", "jamba", "dbrx", "solar", "glm", "orca", "command-r"]):
        return "models"
    if any(k in lower for k in ["train", "finetun", "rlhf", "unsloth", "axolotl", "llama-factory", "trl", "transformers", "pytorch", "lightning", "deepspeed", "megatron"]):
        return "training"
    if any(k in lower for k in ["eval", "benchmark", "observ", "phoenix", "langfuse", "opik", "garak"]):
        return "evaluation"
    if any(k in lower for k in ["security", "guard", "firewall", "armor", "lakera", "vigil", "rebuff"]):
        return "security"
    if any(k in lower for k in ["robot", "lerobot", "manipulation", "embodied"]):
        return "robotics"
    if any(k in lower for k in ["deploy", "platform", "modal", "bentoml", "skypilot", "dify", "flowise", "lovable", "bolt"]):
        return "platforms"
    if any(k in lower for k in ["reason", "cot", "chain-of-thought", "reflection", "debate", "swe-agent", "swe"]):
        return "reasoning"
    if any(k in lower for k in ["agent", "swarm", "crew", "autogpt", "langchain", "langgraph", "autogen", "agno", "pydantic", "smol", "goose", "openinterpreter", "composio", "awesome"]):
        return "agents"
    if any(k in lower for k in ["skill", "prompt", "cookbook", "guide"]):
        return "skills"
    if any(k in lower for k in ["infra", "orchestr", "k8s", "kube", "docker", "server", "gpu"]):
        return "infrastructure"
    if any(k in lower for k in ["mlops", "monitor", "pipeline", "experiment"]):
        return "mlops"
    if any(k in lower for k in ["course", "book", "paper", "knowledge", "roadmap"]):
        return "knowledge"
    return "agents"


def slug_for_repo(repo: str):
    return re.sub(r"[^a-zA-Z0-9_.-]", "-", repo).strip("-").lower() or repo


def main():
    if len(sys.argv) < 2:
        print("Usage: python add_submodules_from_awesome.py <awesome-markdown-file> [category-override]")
        sys.exit(1)

    md_path = Path(sys.argv[1])
    override_cat = sys.argv[2] if len(sys.argv) > 2 else None
    if not md_path.exists():
        print(f"File not found: {md_path}")
        sys.exit(1)

    markdown = md_path.read_text(encoding="utf-8")
    urls = extract_github_urls(markdown)
    print(f"Found {len(urls)} GitHub URLs in {md_path}")

    existing_urls, existing_paths = parse_gitmodules(GITMODULES)
    print(f"Existing .gitmodules entries: {len(existing_paths)}")

    added = 0
    skipped_existing = 0
    skipped_invalid = 0
    new_entries = []

    for url in sorted(urls):
        canon = normalize_github_url(url)
        if not canon:
            skipped_invalid += 1
            continue
        if canon in existing_urls:
            skipped_existing += 1
            continue

        m = re.match(r"https://github\.com/([^/]+)/([^/]+)\.git", canon)
        owner, repo = m.group(1), m.group(2)

        category = override_cat or suggest_category(owner, repo, markdown)
        slug = slug_for_repo(repo)
        path = f"{category}/{slug}"

        base_path = path
        counter = 1
        while path in existing_paths:
            path = f"{base_path}-{counter}"
            counter += 1

        existing_urls.add(canon)
        existing_paths[path] = canon
        new_entries.append((path, canon))
        added += 1
        print(f"+ {path} -> {canon}")

    if added:
        with open(GITMODULES, "a", encoding="utf-8") as f:
            for path, url in new_entries:
                f.write(f'[submodule "{path}"]\n')
                f.write(f"\tpath = {path}\n")
                f.write(f"\turl = {url}\n")
        print(f"\nAdded {added} submodules to .gitmodules, skipped {skipped_existing} existing, {skipped_invalid} invalid.")
    else:
        print("\nNo new submodules to add.")


if __name__ == "__main__":
    main()
