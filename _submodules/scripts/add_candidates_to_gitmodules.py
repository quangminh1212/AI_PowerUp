#!/usr/bin/env python3
"""Add candidate GitHub URLs from JSON to .gitmodules with category heuristics."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[2]
GITMODULES = REPO_ROOT / ".gitmodules"
DEFAULT_CANDIDATES = REPO_ROOT / "_submodules" / "scripts" / "awesome_candidates.json"


def parse_gitmodules(path: Path):
    existing_urls = set()
    existing_paths = {}
    if not path.exists():
        return existing_urls, existing_paths
    current_path = current_url = None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r'^\[submodule\s+"([^"]+)"\]', line)
        if m:
            if current_url:
                existing_urls.add(current_url)
            if current_path and current_url:
                existing_paths[current_path] = current_url
            current_path = current_url = None
        m = re.match(r'^\s*path\s*=\s*(.+?)\s*$', line)
        if m:
            current_path = m.group(1)
        m = re.match(r'^\s*url\s*=\s*(.+?)\s*$', line)
        if m:
            current_url = m.group(1)
    if current_url:
        existing_urls.add(current_url)
    if current_path and current_url:
        existing_paths[current_path] = current_url
    return existing_urls, existing_paths


def suggest_category(owner: str, repo: str):
    lower = (owner + " " + repo).lower()
    checks = [
        (["voice", "speech", "audio", "tts", "stt", "ultravox", "pipecat", "bosca", "livekit", "whisper", "wav2lip"], "audio"),
        (["vision", "image", "diffusion", "yolo", "segment", "depth", "stable-diffusion", "dalle", "clip"], "vision"),
        (["video", "step-video", "sora"], "video"),
        (["multimodal", "cog", "florence", "glm-4v", "paligemma", "qwen-vl"], "multimodal"),
        (["memory", "mem0", "zep", "letta"], "memory"),
        (["mcp", "context-protocol"], "mcp-servers"),
        (["rag", "llamaindex", "unstructured", "chroma", "qdrant", "weaviate", "ragflow", "milvus", "pinecone"], "data-rag"),
        (["model", "llm", "gpt", "claude", "gemini", "qwen", "deepseek", "phi", "llama", "mixtral", "jamba", "dbrx", "solar", "glm", "orca", "command-r", "yi", "falcon"], "models"),
        (["train", "finetun", "rlhf", "unsloth", "axolotl", "llama-factory", "trl", "transformers", "pytorch", "lightning", "deepspeed", "megatron"], "training"),
        (["eval", "benchmark", "observ", "phoenix", "langfuse", "opik", "garak", "wandb", "mlflow"], "evaluation"),
        (["security", "guard", "firewall", "armor", "lakera", "vigil", "rebuff"], "security"),
        (["robot", "lerobot", "manipulation", "embodied"], "robotics"),
        (["deploy", "platform", "modal", "bentoml", "skypilot", "dify", "flowise", "lovable", "bolt"], "platforms"),
        (["reason", "cot", "chain-of-thought", "reflection", "debate", "swe-agent", "swe"], "reasoning"),
        (["agent", "swarm", "crew", "autogpt", "langchain", "langgraph", "autogen", "agno", "pydantic", "smol", "goose", "openinterpreter", "composio"], "agents"),
        (["skill", "prompt", "cookbook", "guide"], "skills"),
        (["infra", "orchestr", "k8s", "kube", "docker", "server", "gpu", "vllm", "ollama", "sglang"], "infrastructure"),
        (["mlops", "monitor", "pipeline", "experiment", "zenml", "metaflow", "clearml", "dagster"], "mlops"),
        (["course", "book", "paper", "knowledge", "roadmap", "awesome"], "knowledge"),
    ]
    for keys, cat in checks:
        if any(k in lower for k in keys):
            return cat
    return "agents"


def slug(repo: str):
    return re.sub(r"[^a-zA-Z0-9_.-]", "-", repo).strip("-").lower() or repo


def main():
    candidates_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CANDIDATES
    if not candidates_path.is_absolute():
        candidates_path = REPO_ROOT / "_submodules" / "scripts" / candidates_path
    if not candidates_path.exists():
        print(f"Candidates file not found: {candidates_path}")
        return

    candidates = json.loads(candidates_path.read_text(encoding="utf-8"))
    existing_urls, existing_paths = parse_gitmodules(GITMODULES)

    added = 0
    skipped = 0
    new_blocks = []

    for url in candidates:
        if url.endswith(".git"):
            url = url[:-4]
        canon = f"{url}.git"
        if canon in existing_urls:
            skipped += 1
            continue

        parsed = urlparse(url)
        parts = [p for p in parsed.path.split("/") if p]
        if len(parts) < 2:
            continue
        owner, repo = parts[0], parts[1]
        category = suggest_category(owner, repo)
        path = f"{category}/{slug(repo)}"

        base = path
        counter = 1
        while path in existing_paths:
            path = f"{base}-{counter}"
            counter += 1

        existing_urls.add(canon)
        existing_paths[path] = canon
        new_blocks.append(f'[submodule "{path}"]\n\tpath = {path}\n\turl = {canon}\n')
        added += 1
        print(f"+ {path} -> {canon}")

    if new_blocks:
        with open(GITMODULES, "a", encoding="utf-8") as f:
            f.writelines(new_blocks)
        print(f"\nAdded {added} submodules. Skipped {skipped} duplicates.")
    else:
        print("No new submodules to add.")


if __name__ == "__main__":
    main()
