# AI Advanced Cognitive Skills & Intelligence Hub

The definitive, production-grade ecosystem for AI Agents. Integrates the world's leading open-source frameworks, reasoning engines, open-weight models, memory layers, coding agents, infrastructure tools, training pipelines, evaluation harnesses, security guardrails, vision/audio/video AI, MLOps, robotics, multimodal models, and Model Context Protocol (MCP) servers — all organized as Git submodules (reference-only) for maximum modularity.

## Ecosystem Architecture (457 Submodules / 20 Categories)

### 1. Core Cognitive Skills (`skills/`) — 26 submodules
Explicit reasoning techniques, prompt engineering, and curated knowledge resources.
- **Internal Skills**: `first-principles-thinking`, `self-correction-loop`, `system-impact-analyzer`, `devil-advocate`, `ooda-loop`, `design-thinking`, `tdd-advanced`.
- **Prompt Engineering**: `prompt-engineering-guide` (~72k★), `prompt-engineering`, `instructor` (~10k★), `ai-prompts`.
- **External Knowledge**: `anthropic-cookbook`, `openai-cookbook`, `gemini-cookbook`, `google-ai-docs`, `chatgpt-autoexpert`, `fabric` (~50k★).
- **Curated Lists**: `awesome-claude-code`, `awesome-mcp-servers`, `awesome-cursorrules`, `lobe-chat-agents`.
- **CI/CD**: `claude-code-action`, `browser-use` (~58k★), `search-with-lepton`, `rags`.

### 2. Orchestration Frameworks (`frameworks/`) — 66 submodules
The world's best AI agent orchestration platforms:
- **Foundational**: `langchain` (~131k★), `llama_index` (~48k★), `semantic-kernel` (~25k★), `haystack`.
- **Agent Workflows**: `langgraph` (~28k★), `pydantic-ai` (~16k★), `openai-agents-python` (~20k★), `phidata` (~15k★).
- **Multi-Agent**: `autogen`, `ag2` (AutoGen successor), `crewAI`, `eliza` (~15k★), `MetaGPT`, `smolagents`, `swarms`, `chatdev`, `owl` (CAMEL-AI).
- **Google**: `google-adk` (Agent Dev Kit), `a2a-python` (Agent-to-Agent).
- **Autonomous**: `babyagi`, `devika`, `open-interpreter`, `agentgpt`.
- **MCP & Memory**: `mcp-agent`, `langmem`, `controlflow`.
- **LLM Routing**: `dspy`, `guidance`, `outlines`, `mirascope`, `typechat`.
- **Serving**: `colossalai`, `litserve`, `llama-stack`, `onnxruntime`.
- **UI**: `gradio` (~40k★), `streamlit` (~40k★), `chainlit`.
- **Core ML**: `pytorch`, `spacy`, `fastapi`, `tinygrad`, `transformers-js`, `jina`, `vercel-ai-sdk`, `mastra`.

### 3. AI Coding Agents (`agents/`) — 34 submodules
Terminal-native and IDE-integrated coding assistants:
- `AutoGPT` (~175k★), `openhands` (~54k★), `codex` (~66k★), `claude-code`, `aider` (~42k★).
- `gpt-pilot` (~35k★), `swe-agent` (~20k★), `tabby` (~30k★), `continue` (~25k★).
- `cline`, `cursor`, `roo-code`, `void`, `gemini-cli`, `goose`, `bolt-new`.
- **Generalist / OS UI**: `OS-Copilot`, `UFO`.
- **Browser / Web**: `Skyvern`.
- **Agentic Reasoning**: `XAgent`.
- **New**: `agent-zero`, `anthropic-quickstarts`, `sweep`, `mentat`, `plandex`, `gpt-runner`.

### 4. AI Platforms (`platforms/`) — 11 submodules
Production-ready low-code/visual AI app builders:
- `dify` (~135k★), `langflow` (~146k★), `n8n` (~182k★), `flowise` (~35k★), `fastgpt` (~25k★).
- `botpress`, `rasa`, `opengpts`, `oneapi` (multi-provider API proxy).

### 5. Persistent Memory (`memory/`) — 4 submodules
- `mem0`, `cipher`, `memgpt` (OS-inspired virtual memory), `zep`.

### 6. Training & Fine-tuning (`training/`) — 36 submodules
- **Core**: `transformers` (~145k★), `keras`, `jax`, `accelerate`, `pytorch-lightning`.
- **RLHF / Post-Training**: `OpenRLHF` (Scaling), `verl` (Volcengine), `alignment-handbook`.
- **Fine-tuning**: `LLaMA-Factory` (~50k★), `unsloth` (~30k★), `axolotl`, `torchtune`, `ms-swift`.
- **PEFT**: `peft` (~18k★), `lora`, `trl` (~12k★).
- **Distributed**: `DeepSpeed` (~40k★), `megatron-lm`, `nemo`, `colossalai`, `gpt-neox`, `petals`.
- **Quantization**: `autogptq`, `bitsandbytes`, `exllamav2`.
- **Inference**: `TensorRT-LLM`, `text-generation-inference`, `llama-cpp-python`, `deepspeed-mii`.
- **GPU**: `flash-attention`, `cutlass`, `ggml`.
- **Apple**: `mlx`, `mlx-examples`.

### 7. LLM Infrastructure (`infrastructure/`) — 33 submodules
- **Local**: `ollama` (~130k★), `llamacpp` (~80k★), `gpt4all`, `llamafile`, `localai`.
- **Inference**: `vllm` (~75k★), `sglang`, `mlc-llm`, `candle`.
- **Web UIs**: `open-webui` (~129k★), `lobe-chat` (~60k★), `text-generation-webui`, `anything-llm`, `librechat`, `chatbox`, `jan`.
- **Proxy**: `litellm` (~30k★), `llm-cli`.
- **MLOps**: `mlflow`, `ray`, `bentoml`.

### 8. Data & RAG Pipelines (`data-rag/`) — 37 submodules
- **Crawling**: `firecrawl` (~100k★), `crawl4ai` (~61k★), `scrapegraph-ai`.
- **RAG**: `ragflow` (~76k★), `graphrag` (~32k★), `khoj`, `kotaemon`, `quivr`, `txtai`, `r2r`, `storm`.
- **Document**: `docling` (~57k★), `marker`, `markitdown`, `unstructured`, `llama-parse`, `MegaParse`.
- **OCR**: `surya`, `tesseract`, `EasyOCR`, `doctr`.
- **Vector DB**: `chroma`, `faiss`, `weaviate`, `lancedb`, `milvus`, `qdrant`, `pgvector`.
- **Embeddings**: `embeddings` (~10k★), `sentence-transformers`.
- **Knowledge Graph**: `kg-gen` (LLM-powered KG extraction).
- **Datasets**: `hf-datasets`, `nemo-curator`, `fiftyone`.

### 9. AI Evaluation & Testing (`evaluation/`) — 17 submodules
- **Benchmarking**: `lm-evaluation-harness`, `OpenCompass`, `swe-bench`, `mteb`, `vlm-eval`, `lmms-eval`, `evals`.
- **Testing**: `deepeval`, `promptfoo`, `ragas`, `inspect-ai`.
- **Observability**: `langfuse`, `langsmith-sdk`, `phoenix`, `helicone`, `agentops`, `wandb`.

### 10. AI Security & Safety (`security/`) — 5 submodules
- `guardrails`, `NeMo-Guardrails`, `garak`, `llm-guard`, `rebuff`.

### 11. Vision & Image AI (`vision/`) — 30 submodules
- **Generation**: `stable-diffusion-webui` (~148k★), `ComfyUI` (~80k★), `fooocus`, `invokeai`, `flux`, `diffusers`.
- **Image Edit**: `instruct-pix2pix`, `photomaker`, `instantid`, `realesrgan`.
- **Models**: `imagen-pytorch`, `dalle2-pytorch`.
- **Segmentation**: `segment-anything` (~50k★), `sam2`, `grounding-dino`.
- **Detection**: `ultralytics` (~40k★), `detectron2`, `mmdetection`, `supervision`, `yolov9`.
- **3D**: `shap-e`, `point-e`, `depth-anything`.
- **Parsing/UI Understanding**: `OmniParser` (~6k★).

### 12. Voice & Audio AI (`audio/`) — 16 submodules
- **ASR**: `whisper` (~80k★), `WhisperX`, `speechbrain`, `coqui-stt`.
- **TTS**: `TTS` (~40k★), `ChatTTS`, `bark`, `fish-speech`, `parler-tts`, `f5-tts`, `mars5-tts`, `voicecraft`.
- **Voice Clone**: `OpenVoice` (~35k★).
- **Audio Gen**: `audiocraft`, `stable-audio`.
- **Speaker**: `pyannote-audio`.

### 13. Video AI (`video/`) — 5 submodules
- `Open-Sora`, `CogVideo`, `AnimateDiff`, `hunyuan-video`, `stable-video`.

### 14. Knowledge & Learning (`knowledge/`) — 29 submodules
- **Courses**: `generative-ai-for-beginners` (~70k★), `llm-course` (~50k★), `ai-agents-masterclass`, `llm-zoomcamp`, `hands-on-llm`, `made-with-ml`, `ml-systems-design`.
- **SDKs**: `openai-python` (~25k★), `anthropic-sdk-python`.
- **Educational**: `nanogpt`, `mingpt`, `llm-c` (Karpathy), `nvidia-ai-examples`, `tuning-playbook`.
- **Curated**: `Awesome-LLM`, `Awesome-LLMOps`, `awesome-ai-agents`, `awesome-chatgpt-prompts`, `awesome-genai`, `papers-with-code`.
- **Roadmaps**: `developer-roadmap`, `ai-expert-roadmap`, `system-design-primer`, `coding-interview`, `build-your-own-x`, `free-programming-books`.

### 15. MCP Servers (`mcp-servers/`) — 30 submodules
- **Official**: `official-servers`, `mcp-python-sdk`, `mcp-typescript-sdk`.
- **Vector/Graph**: `pinecone-mcp`, `chroma-mcp`, `mcp-qdrant`, `milvus-mcp`, `neo4j-mcp`.
- **Databases**: `redis-mcp`, `mongodb-mcp`, `elasticsearch-mcp`, `supabase-mcp`.
- **Search**: `brave-search`, `exa-mcp`, `apify-mcp`.
- **DevOps**: `agentops-mcp`, `langfuse-mcp`, `cloudflare-mcp`, `github-mcp-server`, `docker-mcp`.
- **Workspace**: `notion-mcp`, `auth0-mcp`, `stripe-mcp`.
- **Browser**: `mcp-chrome`, `playwright-mcp`, `chrome-devtools-mcp`.
- **Tools**: `cli-mcp-server`, `MCPRules`, `context7`, `mcp-feedback-enhanced`.

### 16. Reasoning & Cognitive Architecture (`reasoning/`) — 26 submodules
- **Core**: `tree-of-thoughts`, `chain-of-thought-hub`, `chain-of-verification`.
- **Logic & Symbolic**: `lean4` (Prover).
- **Simulations**: `ai-town`.
- **Self-Improvement**: `self-refine`, `reflexion`, `self-rag`.
- **Agent Reasoning**: `camel` (~10k★), `agentscope`, `voyager`, `letta`.
- **Optimization**: `adalflow`, `tensorzero`, `textgrad`.
- **Tool Use**: `gorilla`, `toolformer`, `minichain`, `ell`.
- **Knowledge Graphs**: `graphiti`.

### 17. Open-Weight Models (`models/`) — 42 submodules
- **Reasoning Replications**: `open-r1` (HuggingFace), `Marco-o1` (AIDC).
- **DeepSeek**: `deepseek-r1`, `deepseek-v3`, `deepseek-v2`, `deepseek-coder`, `deepseek-coder-v2`.
- **Qwen**: `qwen`, `qwen2.5`, `qwen3`.
- **Meta Llama**: `llama`, `llama3`, `llama-models`, `codellama`, `purple-llama`.
- **Mistral**: `mistral-inference`, `mistral-common`.
- **Microsoft**: `phi-cookbook`, `grin-moe`, `bitnet` (1-bit LLMs).
- **Google**: `gemma`, `deepmind-gemma`.
- **Apple**: `corenet` (OpenELM).
- **Vision-Language**: `clip`, `llava`, `cogvlm2`, `minicpm-v`.
- **AllenAI**: `olmo`, `olmoe` (open-weight MoE).
- **Others**: `yi`, `internlm`, `chatglm`, `glm4`, `grok`, `StableLM`, `starcoder2`, `openchat`, `wizardlm`, `minicpm`, `moshi`, `jamba`, `dbrx`.

### 18. MLOps & Workflow Orchestration (`mlops/`) ⭐ NEW — 15 submodules
Production ML lifecycle and infrastructure:
- **Orchestration**: `kubeflow` (~14k★), `dagster` (~12k★), `prefect` (~17k★), `flyte`, `argo-workflows` (~15k★).
- **Experiment Tracking**: `clearml`, `dvc` (~14k★), `evidently`.
- **Feature Store**: `feast` (~6k★).
- **Data Quality**: `great-expectations` (~10k★).
- **Serving**: `triton-server` (NVIDIA), `seldon-core`.
- **ML Lifecycle**: `zenml`, `metaflow` (Netflix).
- **Learning**: `mlops-zoomcamp`.

### 19. Robotics & Embodied AI (`robotics/`) ⭐ NEW — 10 submodules
Simulation, navigation, and physical AI:
- **Simulation**: `habitat-sim` (Meta), `habitat-lab`, `isaaclab` (NVIDIA), `mujoco` (DeepMind).
- **RL**: `gymnasium` (Farama), `robosuite`, `pybullet`.
- **ROS**: `ros2`, `nav2` (Navigation2).
- **Data**: `openx` (Open X-Embodiment).

### 20. Multimodal AI (`multimodal/`) ⭐ NEW — 8 submodules
Vision-language and multimodal foundation models:
- `llava-next`, `internvl` (OpenGVLab), `qwen-vl` (Alibaba).
- `minigpt4`, `moondream`, `cambrian`, `ferret` (Apple), `florence2` (Microsoft).

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
- **Total Submodules**: 473
- **Categories**: 20
- **Combined GitHub Stars**: ~10M+ ★
- **Storage Mode**: Reference-only (no data cloned by default)
- **New in v2**: MLOps, Robotics, Multimodal categories + 104 new repos
