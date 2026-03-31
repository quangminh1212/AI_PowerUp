# 🏭 LLM Infrastructure

Local runners, high-performance inference engines, web UIs, proxies, serving platforms, and tokenization tools.

## Overview

This directory contains **39 submodules** providing the complete infrastructure stack for running, serving, and managing LLMs — from local desktop runners (Ollama, GPT4All) and high-performance GPU inference (vLLM, SGLang) to ChatGPT-style web UIs and cloud orchestration. Deploy AI anywhere, from a laptop to a GPU cluster.

## Submodules (39)

### Local LLM Runners
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`ollama`](https://github.com/ollama/ollama) | Ollama | Run LLMs locally with one command |
| [`llamacpp`](https://github.com/ggml-org/llama.cpp) | GGML | Lightweight LLM inference in C/C++ |
| [`gpt4all`](https://github.com/nomic-ai/gpt4all) | Nomic AI | Run LLMs locally on consumer hardware |
| [`llamafile`](https://github.com/Mozilla-Ocho/llamafile) | Mozilla | Single-file executable LLM distribution |
| [`localai`](https://github.com/mudler/LocalAI) | mudler | OpenAI-compatible local AI server |
| [`localGPT`](https://github.com/PromtEngineer/localGPT) | PromptEngineer | Chat with documents using local LLMs |
| [`privateGPT`](https://github.com/zylon-ai/private-gpt) | Zylon AI | Private, enterprise-grade local AI |
| [`h2ogpt`](https://github.com/h2oai/h2ogpt) | H2O.ai | LLM gateway with RAG and fine-tuning |

### High-Performance Inference
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`vllm`](https://github.com/vllm-project/vllm) | vLLM | Fastest LLM inference engine with PagedAttention |
| [`sglang`](https://github.com/sgl-project/sglang) | SGLang | Structured generation language for fast serving |
| [`mlc-llm`](https://github.com/mlc-ai/mlc-llm) | MLC AI | Universal LLM deployment on any device |
| [`infinity`](https://github.com/michaelfeil/infinity) | michaelfeil | High-throughput embedding inference server |
| [`candle`](https://github.com/huggingface/candle) | Hugging Face | Minimalist ML framework in Rust |
| [`gemma-cpp`](https://github.com/google/gemma.cpp) | Google | Lightweight Gemma inference in C++ |
| [`whisper-cpp`](https://github.com/ggerganov/whisper.cpp) | ggerganov | Whisper speech recognition in C/C++ |
| [`exo`](https://github.com/exo-explore/exo) | Exo | Run AI clusters at home using everyday devices |
| [`openllm`](https://github.com/bentoml/OpenLLM) | BentoML | Operating LLMs in production |

### Web UIs & Chat Interfaces
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`open-webui`](https://github.com/open-webui/open-webui) | Open WebUI | Self-hosted ChatGPT-like interface |
| [`lobe-chat`](https://github.com/lobehub/lobe-chat) | LobeHub | Modern AI chat framework |
| [`text-generation-webui`](https://github.com/oobabooga/text-generation-webui) | oobabooga | Gradio web UI for LLM text generation |
| [`anything-llm`](https://github.com/Mintplex-Labs/anything-llm) | Mintplex | Full-stack AI application platform |
| [`librechat`](https://github.com/danny-avila/LibreChat) | danny-avila | Multi-model chat interface with plugin support |
| [`chatbox`](https://github.com/Bin-Huang/chatbox) | Bin Huang | Desktop AI chat app |
| [`jan`](https://github.com/janhq/jan) | Jan HQ | Open-source ChatGPT alternative for desktop |
| [`chatbot-ui`](https://github.com/mckaywrigley/chatbot-ui) | McKay Wrigley | Open-source AI chat interface |
| [`hf-chat-ui`](https://github.com/huggingface/chat-ui) | Hugging Face | Official HuggingChat web interface |
| [`lmstudio`](https://github.com/lmstudio-ai/lms) | LM Studio | Desktop app for local LLM management |
| [`astrbot`](https://github.com/AstrBotDevs/AstrBot) | AstrBot | IM chatbot infrastructure for messaging platforms |

### LLM Proxy & Gateway
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`litellm`](https://github.com/BerriAI/litellm) | BerriAI | Unified proxy for 100+ LLM providers |
| [`llm-cli`](https://github.com/simonw/llm) | Simon Willison | CLI tool for interacting with any LLM |
| [`ai-gateway`](https://github.com/Portkey-AI/gateway) | Portkey | Production AI gateway with routing and fallbacks |

### Model Serving & MLOps
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`bentoml`](https://github.com/bentoml/BentoML) | BentoML | Build and deploy ML services |
| [`ray`](https://github.com/ray-project/ray) | Ray | Distributed computing framework for AI |
| [`mlflow`](https://github.com/mlflow/mlflow) | MLflow | ML lifecycle management platform |

### Cloud Orchestration
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`skypilot`](https://github.com/skypilot-org/skypilot) | SkyPilot | Run AI on any cloud with auto cost optimization |
| [`dstack`](https://github.com/dstackai/dstack) | dstack | Open-source GPU orchestration for AI workloads |

### Tokenization & Translation
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`tiktoken`](https://github.com/openai/tiktoken) | OpenAI | Fast BPE tokenizer for OpenAI models |
| [`tokenizers`](https://github.com/huggingface/tokenizers) | Hugging Face | Ultra-fast tokenizer implementations in Rust |
| [`LibreTranslate`](https://github.com/LibreTranslate/LibreTranslate) | LibreTranslate | Self-hosted machine translation API |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Local Desktop** | ollama, gpt4all, jan, llamafile |
| **GPU Inference** | vllm, sglang, llamacpp |
| **Web Chat UI** | open-webui, lobe-chat, librechat |
| **LLM Proxy** | litellm, ai-gateway |
| **Cloud GPU** | skypilot, dstack, ray |
| **Model Serving** | bentoml, openllm, mlflow |
| **Edge/Mobile** | mlc-llm, candle, exo |

## Usage

```bash
# Run LLM locally with Ollama
git submodule update --init --depth 1 infrastructure/ollama
cd infrastructure/ollama && ollama run llama3

# Start vLLM for high-throughput serving
git submodule update --init --depth 1 infrastructure/vllm
pip install vllm && vllm serve meta-llama/Llama-3-8B

# Deploy web UI
git submodule update --init --depth 1 infrastructure/open-webui
cd infrastructure/open-webui && docker compose up
```
