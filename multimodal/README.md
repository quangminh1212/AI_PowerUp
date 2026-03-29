# 🌐 Multimodal AI

Vision-language and multimodal foundation models.

## Overview

This directory contains 8 submodules of cutting-edge multimodal AI models that can understand and reason across text, images, and video simultaneously.

## Submodules (8)

| Submodule | Source | Description |
|-----------|--------|-------------|
| [`llava-next`](https://github.com/LLaVA-VL/LLaVA-NeXT) | LLaVA-VL | Next-gen visual instruction tuning |
| [`internvl`](https://github.com/OpenGVLab/InternVL) | OpenGVLab | Open-source GPT-4V alternative |
| [`qwen-vl`](https://github.com/QwenLM/Qwen-VL) | Alibaba | Qwen vision-language model |
| [`minigpt4`](https://github.com/Vision-CAIR/MiniGPT-4) | Vision-CAIR | Visual understanding with GPT-4 quality |
| [`moondream`](https://github.com/vikhyat/moondream) | vikhyat | Tiny but powerful vision-language model |
| [`cambrian`](https://github.com/cambrian-mllm/cambrian) | Cambrian | Vision-centric multimodal LLM |
| [`ferret`](https://github.com/apple/ml-ferret) | Apple | Grounded multimodal model |
| [`florence2`](https://github.com/microsoft/Florence-2-base) | Microsoft | Unified vision foundation model |

## Key Capabilities

- **Visual Question Answering**: Ask questions about images (LLaVA-NeXT, InternVL)
- **Grounded Understanding**: Locate objects and regions (Ferret, Florence2)
- **Lightweight Deployment**: Run on edge devices (Moondream)
- **Multi-turn Conversation**: Chat about images naturally (Qwen-VL, MiniGPT-4)

## Usage

```bash
git submodule update --init --depth 1 multimodal/internvl
git submodule update --init --depth 1 multimodal/qwen-vl
```
