#!/usr/bin/env python3
"""Build a fine-grained taxonomy map for all submodules from .gitmodules."""
import json
import re
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parents[2]
GITMODULES = REPO_ROOT / ".gitmodules"
OUT_JSON = REPO_ROOT / "_submodules" / "taxonomy.json"
OUT_MD = REPO_ROOT / "_submodules" / "taxonomy_breakdown.md"


def parse_gitmodules(path: Path):
    entries = []
    text = path.read_text(encoding="utf-8-sig", errors="ignore")
    current = {}
    for line in text.splitlines():
        m = re.match(r'^\[submodule\s+"([^"]+)"\]', line)
        if m:
            if current:
                entries.append(current)
            current = {"path": m.group(1)}
        m = re.match(r'^\s*url\s*=\s*(.+?)\s*$', line)
        if m:
            current["url"] = m.group(1)
    if current:
        entries.append(current)
    return entries


def full_text(owner: str, repo: str):
    return f"{owner} {repo}".lower()


def classify(category: str, owner: str, repo: str):
    t = full_text(owner, repo)

    if category == "agents":
        checks = [
            ("coding", ["code", "coder", "claude", "codex", "copilot", "programming", "devin", "ide", "editor", "lint", "refactor", "commit", "terminal", "shell", "repl", "build", "compile", "autocode", "codegen", "code-review", "codegraph", "coding", "developer", "sw"]),
            ("chat", ["chat", "chatbot", "convers", "dialog", "talk", "tavern", "friend", "companion", "nextchat", "chatbox", "chatall", "wechat"]),
            ("browser", ["browser", "web", "page", "surf", "stagehand", "puppeteer", "playwright", "selenium", "scraping", "crawlee", "crawl"]),
            ("voice", ["voice", "speech", "whisper", "tts", "stt", "audio", "asr", "microphone", "realtime", "stt", "speaker"]),
            ("finance", ["stock", "trade", "trading", "finance", "crypto", "bitcoin", "hedge", "fund", "market", "quant", "forex", "invest", "portfolio"]),
            ("research", ["research", "scientist", "paper", "arxiv", "academic", "study", "survey", "literature", "review", "deep-research", "autoresearch"]),
            ("productivity", ["todo", "task", "calendar", "email", "note", "schedule", "productivity", "organize", "workflow", "planner", "reminder", "inbox"]),
            ("framework", ["framework", "sdk", "platform", "agent-sdk", "agentos", "swarm", "crew", "langchain", "autogen", "smol", "agno", "pydantic", "goose", "openinterpreter", "ollama", "vllm", "textgen"]),
            ("image", ["image", "photo", "diffusion", "stable-diffusion", "dalle", "midjourney", "upscayl", "inpaint", "super-resolution", "avatar", "portrait"]),
            ("video", ["video", "clip", "movie", "subtitle", "matting", "vid2vid", "frame"]),
            ("rag", ["rag", "search", "retrieval", "index", "embedding", "chroma", "qdrant", "weaviate", "pinecone", "milvus", "vector"]),
            ("data", ["data", "dataset", "etl", "pipeline", "scrape", "clean", "parse", "extract", "formulator", "pandas"]),
            ("devops", ["deploy", "infra", "kube", "k8s", "docker", "server", "cloud", "sre", "observ", "monitor", "logging"]),
        ]
    elif category == "models":
        checks = [
            ("llm", ["llm", "gpt", "claude", "qwen", "llama", "gemini", "mistral", "mixtral", "phi", "falcon", "yi", "baichuan", "chatglm", "yi-"]),
            ("vision", ["vision", "image", "clip", "dalle", "diffusion", "stable-diffusion", "segment", "yolo", "detr", "vit", "sam", "var", "dreambooth"]),
            ("audio", ["audio", "voice", "speech", "whisper", "tts", "asr", "music", "sound", "wav"]),
            ("code", ["code", "coder", "coding", "program", "dev", "commit", "decompile"]),
            ("multimodal", ["multimodal", "vlm", "mm", "omni", "imagebind", "llava", "qwen-vl", "gemini"]),
            ("chinese", ["chinese", "chinese-llm", "chinese-"]),
            ("small", ["tiny", "nano", "small", "mini", "mobile", "edge", "quantized", "gguf", "onnx"]),
            ("training", ["train", "finetune", "factory", "unsloth", "axolotl", "trl"]),
            ("inference", ["inference", "vllm", "llama.cpp", "ollama", "serving", "deploy"]),
        ]
    elif category == "training":
        checks = [
            ("nlp", ["nlp", "bert", "transformer", "seq2seq", "text", "llm", "language", "gpt", "rwkv"]),
            ("cv", ["vision", "image", "yolo", "cnn", "resnet", "segmentation", "diffusion", "stable-diffusion", "unet", "detr"]),
            ("reinforcement", ["reinforcement", "rl", "ppo", "a3c", "q-learning", "stable-baselines", "dqn"]),
            ("gan", ["gan", "cgan", "stylegan", "cyclegan", "pix2pix", "vae"]),
            ("optimization", ["optimization", "pruning", "quantization", "distillation", "efficient", "opcounter", "grad-cam"]),
            ("framework", ["pytorch", "tensorflow", "keras", "lightning", "catalyst", "fastai"]),
            ("tutorials", ["tutorial", "course", "book", "example", "note", "learn", "practice", "handbook"]),
        ]
    elif category == "vision":
        checks = [
            ("detection", ["yolo", "detr", "rcnn", "detection", "ssd", "efficientdet", "bytetrack"]),
            ("segmentation", ["segment", "unet", "mmsegmentation", "mask"]),
            ("diffusion", ["diffusion", "stable-diffusion", "dalle", "dreambooth", "latent"]),
            ("generation", ["gan", "stylegan", "image-synthesis", "super-resolution", "inpaint", "texture"]),
            ("recognition", ["ocr", "face", "facenet", "clip", "recognition", "classification"]),
            ("3d", ["3d", "pointcloud", "neural-radiance", "nerf", "pytorch3d", "depth", "pose"]),
            ("medical", ["medical", "xray", "ct", "monai"]),
        ]
    elif category == "audio":
        checks = [
            ("tts", ["tts", "speech", "voice-cloning", "styletts", "vits", "bark", "tortoise", "emotivoice"]),
            ("stt", ["stt", "asr", "whisper", "deepspeech", "speech-recognition", "vosk"]),
            ("music", ["music", "audio-generation", "jukebox", "sound"]),
            ("enhancement", ["noise", "suppression", "enhance", "voice-changer", "voice-pro"]),
        ]
    elif category == "knowledge":
        checks = [
            ("courses", ["course", "tutorial", "learn", "mooc", "bootcamp", "lecture", "camp", "book"]),
            ("papers", ["paper", "arxiv", "cvpr", "neurips", "icml", "survey", "roadmap", "reading"]),
            ("awesome-lists", ["awesome", "list", "curated"]),
            ("roadmaps", ["roadmap", "guide", "path", "interview"]),
        ]
    elif category == "skills":
        checks = [
            ("prompts", ["prompt", "system-prompt", "prompts"]),
            ("coding", ["code", "coding", "programming", "developer"]),
            ("career", ["career", "interview", "skill-assessment", "resume", "job"]),
        ]
    elif category == "mcp-servers":
        checks = [
            ("browser", ["browser", "playwright", "selenium", "web"]),
            ("dev-tools", ["git", "github", "vscode", "xcode", "ide", "mcp-ui"]),
            ("productivity", ["atlassian", "notion", "whatsapp", "figma", "windows"]),
            ("databases", ["db", "postgres", "sql", "vector"]),
        ]
    elif category == "data-rag":
        checks = [
            ("vector-db", ["chroma", "qdrant", "weaviate", "milvus", "pinecone", "vector", "rag"]),
            ("frameworks", ["llamaindex", "ragflow", "haystack"]),
        ]
    else:
        checks = []

    tags = []
    for subcat, keys in checks:
        if any(k in t for k in keys):
            tags.append(subcat)
    if not tags:
        tags.append("general")
    return tags


def main():
    entries = parse_gitmodules(GITMODULES)
    taxonomy = {}
    counter = Counter()
    for e in entries:
        path = e["path"]
        url = e.get("url", "")
        parts = [p for p in url.replace("https://github.com/", "").replace(".git", "").split("/") if p]
        if len(parts) < 2:
            continue
        owner, repo = parts[0], parts[1]
        category = path.split("/")[0]
        tags = classify(category, owner, repo)
        taxonomy[path] = {"owner": owner, "repo": repo, "category": category, "tags": tags, "url": url}
        for tag in tags:
            counter[f"{category}/{tag}"] += 1

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(taxonomy, f, indent=2, ensure_ascii=False)

    lines = ["# Taxonomy Breakdown\n", f"Total submodules: {len(taxonomy)}\n\n"]
    for cat_tag, count in counter.most_common():
        lines.append(f"- `{cat_tag}`: {count}\n")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"Wrote {OUT_JSON} with {len(taxonomy)} entries")
    print(f"Wrote {OUT_MD} with {len(counter)} subcategories")
    print("\nTop 20 subcategories:")
    for cat_tag, count in counter.most_common(20):
        print(f"  {count:4d}  {cat_tag}")


if __name__ == "__main__":
    main()
