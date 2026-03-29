# AI Advanced Cognitive Skills & Intelligence Hub

The definitive, production-grade ecosystem for AI Agents. Integrates the world's leading open-source frameworks, memory layers, coding agents, infrastructure tools, training pipelines, evaluation harnesses, security guardrails, vision/audio AI, and Model Context Protocol (MCP) servers — all organized as Git submodules (reference-only) for maximum modularity.

## Ecosystem Architecture (144 Submodules / 14 Categories)

### 1. Core Cognitive Skills (`skills/`)
Explicit reasoning techniques and curated knowledge resources:
- **Internal Skills**: `first-principles-thinking`, `self-correction-loop`, `system-impact-analyzer`, `devil-advocate`, `ooda-loop`, `design-thinking`, `tdd-advanced`.
- **Prompt Engineering**: `prompt-engineering-guide` (~72k★ DAIR.AI), `prompt-engineering` (NirDiamant tutorials), `instructor` (~10k★ structured LLM output).
- **External Knowledge**: `anthropic-cookbook`, `openai-cookbook`, `chatgpt-autoexpert`, `awesome-cursorrules`, `fabric` (~50k★).
- **Curated Lists**: `awesome-claude-code`, `awesome-mcp-servers`.
- **CI/CD**: `claude-code-action`, `browser-use` (~58k★).

### 2. Orchestration Frameworks (`frameworks/`)
The world's best AI agent orchestration platforms:
- **Foundational**: `langchain` (~131k★), `llama_index` (~48k★), `semantic-kernel` (~25k★ Microsoft).
- **Agent Workflows**: `langgraph` (~28k★), `pydantic-ai` (~16k★), `openai-agents-python` (~20k★).
- **Multimodal Agents**: `agno` (~21k★ ex-Phidata), `composio` (~16k★ tool integrations).
- **Multi-Agent Systems**: `autogen`, `crewAI`, `MetaGPT`, `smolagents`, `swarms`, `chatdev`.
- **Autonomous Agents**: `babyagi`, `devika`, `open-interpreter`.
- **LLM Routing & Structured**: `dspy`, `guidance`, `outlines`, `chainlit` (~12k★ UI).
- **Workflow & Pipeline**: `embedchain`, `taskweaver`, `promptflow` (~12k★ Microsoft).
- **UI Builders**: `gradio` (~40k★), `streamlit` (~40k★).
- **Project Management**: `superpowers`, `ccpm`.

### 3. AI Coding Agents (`agents/`)
Terminal-native AI coding assistants:
- `AutoGPT` (~175k★) — Autonomous AI agent pioneer.
- `claude-code` — Anthropic's agentic terminal coder.
- `codex` (~66k★) — OpenAI's terminal coding agent.
- `aider` (~42k★) — Git-native AI pair programmer.
- `openhands` (~54k★) — Multi-tool open-source coding platform.
- `swe-agent` (~20k★) — Autonomous software engineering agent.
- `gpt-pilot` (~35k★) — AI dev tool for full app generation.
- `tabby` (~30k★) — Self-hosted AI code assistant.
- `continue` (~25k★) — Open-source AI code assistant IDE extension.

### 4. AI Platforms (`platforms/`)
Production-ready low-code/visual AI app builders:
- `dify` (~135k★) — All-in-one LLM app platform with visual workflow & RAG.
- `langflow` (~146k★) — Drag-and-drop AI agent builder on LangChain.
- `n8n` (~182k★) — Visual workflow automation with native AI integrations.
- `flowise` (~35k★) — Drag-and-drop LLM flow builder.
- `fastgpt` (~25k★) — Knowledge-based QA platform with visual workflow.

### 5. Persistent Memory (`memory/`)
Long-term memory and context management:
- `mem0` — Universal memory layer for personalized AI.
- `cipher` — Persistent memory optimized for coding agents.
- `memgpt` — OS-inspired virtual memory for unbounded context.

### 6. Training & Fine-tuning (`training/`) ⭐ NEW
Model training, adaptation, and optimization:
- `transformers` (~145k★ Hugging Face) — Core ML/NLP library.
- `LLaMA-Factory` (~50k★) — One-stop LLM fine-tuning with WebUI.
- `DeepSpeed` (~40k★ Microsoft) — Distributed training optimization.
- `unsloth` (~30k★) — 2-5x faster LLM fine-tuning.
- `peft` (~18k★ Hugging Face) — Parameter-efficient fine-tuning (LoRA/QLoRA).
- `trl` (~12k★ Hugging Face) — Transformer Reinforcement Learning.
- `TensorRT-LLM` (~12k★ NVIDIA) — GPU-optimized LLM inference.
- `text-generation-inference` (~10k★ Hugging Face) — Production inference server.
- `axolotl` (~10k★) — YAML-driven fine-tuning framework.
- `torchtune` (~5k★ PyTorch) — Native PyTorch LLM fine-tuning.

### 7. LLM Infrastructure (`infrastructure/`)
Core tools for running, serving, and managing AI models:
- `ollama` (~130k★) — Run open-source LLMs locally.
- `open-webui` (~129k★) — Self-hosted AI platform with web UI.
- `llama.cpp` (~80k★) — C/C++ LLM inference engine.
- `vllm` (~75k★) — High-throughput LLM inference engine.
- `lobe-chat` (~60k★) — Modern ChatGPT-style UI for multiple providers.
- `text-generation-webui` (~42k★) — All-in-one local LLM web interface.
- `anything-llm` (~38k★) — Desktop RAG + AI agent platform.
- `gpt4all` (~30k★) — Run LLMs locally on any hardware.
- `litellm` (~30k★) — LLM proxy/router for 100+ providers.
- `jan` (~28k★) — Offline-first AI desktop app.
- `librechat` (~25k★) — Multi-provider ChatGPT alternative.
- `chatbox` (~25k★) — Desktop AI chat client.
- `sglang` (~15k★) — High-performance LLM serving framework.

### 8. Data & RAG Pipelines (`data-rag/`)
Data collection, processing, and Retrieval-Augmented Generation:
- `firecrawl` (~100k★) — Web crawling/scraping for LLMs.
- `ragflow` (~76k★) — Enterprise-grade RAG engine.
- `crawl4ai` (~61k★) — Fast async web crawler for AI.
- `docling` (~57k★ IBM) — Document conversion to structured data.
- `graphrag` (~32k★ Microsoft) — Graph-based RAG system.
- `khoj` (~34k★) — Personal AI assistant with RAG.
- `kotaemon` (~25k★) — RAG UI for document chat.
- `marker` (~20k★) — PDF/document to markdown converter.
- `surya` (~15k★) — OCR and text detection engine.
- `unstructured` (~12k★) — Document preprocessing for LLMs.
- `embeddings` (~10k★ FlagEmbedding) — State-of-the-art embedding models.

### 9. AI Evaluation & Testing (`evaluation/`)
Standardized benchmarking, testing, and observability:
- `lm-evaluation-harness` (~10k★ EleutherAI) — Gold-standard LLM benchmarking framework.
- `langfuse` (~10k★) — LLM observability and tracing platform.
- `ragas` (~10k★) — RAG pipeline evaluation framework.
- `deepeval` (~8k★) — LLM unit testing with hallucination detection.
- `promptfoo` (~8k★) — Prompt testing in CI/CD pipelines.
- `OpenCompass` (~5k★) — Comprehensive LLM evaluation platform.

### 10. AI Security & Safety (`security/`) ⭐ NEW
Guardrails, red-teaming, and content safety:
- `guardrails` (~5k★) — Structural validation and safety for LLM outputs.
- `NeMo-Guardrails` (~5k★ NVIDIA) — Programmable conversational guardrails.
- `garak` (~3k★ NVIDIA) — LLM vulnerability scanner and red-teaming.
- `llm-guard` (~3k★) — LLM interaction security toolkit.

### 11. Vision & Image AI (`vision/`) ⭐ NEW
Image generation, segmentation, and computer vision:
- `stable-diffusion-webui` (~148k★) — The standard for AI image generation.
- `ComfyUI` (~80k★) — Node-based image generation workflow.
- `segment-anything` (~50k★ Meta) — Foundation model for image segmentation.
- `ultralytics` (~40k★) — YOLO object detection and vision AI.

### 12. Voice & Audio AI (`audio/`) ⭐ NEW
Speech synthesis, recognition, and audio generation:
- `whisper` (~80k★ OpenAI) — Industry-standard speech-to-text.
- `bark` (~40k★) — Text-to-audio generation model.
- `ChatTTS` (~35k★) — Conversational text-to-speech.
- `TTS` (~40k★ Coqui) — Deep learning text-to-speech toolkit.
- `OpenVoice` (~35k★) — Instant voice cloning.
- `fish-speech` (~20k★) — Multilingual text-to-speech.

### 13. Knowledge & Learning (`knowledge/`) ⭐ NEW
Courses, SDKs, and curated AI knowledge:
- `generative-ai-for-beginners` (~70k★ Microsoft) — Generative AI course.
- `llm-course` (~50k★) — Comprehensive LLM course with notebooks.
- `Awesome-LLM` (~25k★) — Curated LLM resources and papers.
- `openai-python` (~25k★) — Official OpenAI Python SDK.
- `ai-agents-masterclass` (~10k★) — GenAI agents tutorial collection.
- `anthropic-sdk-python` (~5k★) — Official Anthropic Python SDK.
- `Awesome-LLMOps` (~5k★) — Curated LLMOps tools and resources.

### 14. MCP Servers (`mcp-servers/`)
Extensive Model Context Protocol integrations (25 servers):
- **Official**: `official-servers` (Time, Filesystem, Git, SQLite, etc.).
- **Vector/Graph DB**: `pinecone-mcp`, `chroma-mcp`, `mcp-qdrant`, `milvus-mcp`, `neo4j-mcp`.
- **Databases**: `redis-mcp`, `mongodb-mcp`, `elasticsearch-mcp`.
- **Search/Scraping**: `brave-search`, `exa-mcp`, `apify-mcp`.
- **DevOps/Tracking**: `agentops-mcp`, `langfuse-mcp`, `cloudflare-mcp`.
- **Workspaces/Auth**: `notion-mcp`, `auth0-mcp`.
- **Browser**: `mcp-chrome`, `playwright-mcp`, `chrome-devtools-mcp`.
- **CI/CD & Tools**: `github-mcp-server`, `cli-mcp-server`, `MCPRules`, `context7`, `mcp-feedback-enhanced`.

## Quick Start

```bash
# 1. Clone (submodules are reference-only, no data downloaded)
git clone https://github.com/quangminh1212/AI.git

# 2. Init only the submodules you need
git submodule update --init --depth 1 frameworks/langchain
git submodule update --init --depth 1 infrastructure/ollama

# 3. Copy skills for Auto Skill Discovery
cp -r skills/ ~/.agent/skills/

# 4. Run local models (optional)
cd infrastructure/ollama && ollama serve
```

## Project Statistics
- **Total Submodules**: 144
- **Categories**: 14
- **Combined GitHub Stars**: ~4M+ ★
- **Storage Mode**: Reference-only (no data cloned by default)
