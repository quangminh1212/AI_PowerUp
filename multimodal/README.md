# 🌐 Multimodal Models

Vision-language models that understand both images and text — from general VLMs to specialized OCR and dialog systems.

## Overview

This directory contains **8 submodules** of leading multimodal (vision-language) models that process images and text together. These models power visual question answering, image captioning, document understanding, and multimodal reasoning tasks.

## Submodules (8)

| Submodule | Source | Description |
|-----------|--------|-------------|
| [`llava-next`](https://github.com/LLaVA-VL/LLaVA-NeXT) | LLaVA-VL | Latest LLaVA visual instruction tuning |
| [`qwen-vl`](https://github.com/QwenLM/Qwen-VL) | Qwen | Vision-language model powering Qwen visual chat |
| [`internvl`](https://github.com/OpenGVLab/InternVL) | OpenGVLab | Scaling vision foundation model to 6B params |
| [`florence2`](https://github.com/microsoft/Florence-2) | Microsoft | Unified vision foundation model — captioning, grounding, OCR |
| [`minigpt4`](https://github.com/Vision-CAIR/MiniGPT-4) | Vision-CAIR | Enhancing vision-language understanding with GPT-4 |
| [`moondream`](https://github.com/vikhyat/moondream) | vikhyat | Tiny powerful vision-language model (1.8B) |
| [`cambrian`](https://github.com/cambrian-mllm/cambrian) | Cambrian | Vision-centric multimodal benchmark/model |
| [`ferret`](https://github.com/apple/ml-ferret) | Apple | Refer and ground anything in images |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Visual Q&A** | llava-next, internvl, qwen-vl |
| **Document/OCR** | florence2, internvl |
| **Edge Deployment** | moondream (1.8B), minigpt4 |
| **Grounding/Detection** | ferret, florence2 |
| **Research/Benchmark** | cambrian |

## Usage

```bash
# Init InternVL for multimodal tasks
git submodule update --init --depth 1 multimodal/internvl

# Run tiny Moondream
git submodule update --init --depth 1 multimodal/moondream
pip install transformers && python -c "
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained('vikhyatk/moondream2', trust_remote_code=True)
"
```
