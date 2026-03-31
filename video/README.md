# 🎬 Video Generation

AI-powered video generation, editing, and synthesis — from text-to-video diffusion models to video extension tools.

## Overview

This directory contains **6+ submodules** of leading AI video generation models — covering text-to-video generation (CogVideo, Open-Sora), image-to-video animation (AnimateDiff, Stable Video Diffusion), and next-generation video models from top labs.

## Submodules (6+)

| Submodule | Source | Description |
|-----------|--------|-------------|
| [`CogVideo`](https://github.com/THUDM/CogVideo) | Tsinghua | Text-to-video diffusion model — CogVideoX for high-quality generation |
| [`Open-Sora`](https://github.com/hpcaitech/Open-Sora) | HPC-AI Tech | Open reproduction of Sora-like video generation |
| [`hunyuan-video`](https://github.com/Tencent/HunyuanVideo) | Tencent | Open video generation foundation model |
| [`AnimateDiff`](https://github.com/guoyww/AnimateDiff) | guoyww | Animate personalized text-to-image models into videos |
| [`stable-video`](https://github.com/Stability-AI/generative-models) | Stability AI | Stable Video Diffusion for video synthesis |
| [`moneyprinter`](https://github.com/FujiwaraChoki/MoneyPrinter) | FujiwaraChoki | Automated short video generation pipeline |

> **New additions being added**: wan-video (Alibaba video model), ltx-video (Lightricks real-time video), mochi (Genmo high-fidelity video)

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Text-to-Video** | CogVideo, Open-Sora, hunyuan-video |
| **Image Animation** | AnimateDiff, stable-video |
| **Automated Production** | moneyprinter |

## Usage

```bash
# Run CogVideoX
git submodule update --init --depth 1 video/CogVideo
cd video/CogVideo && pip install -r requirements.txt

# Open-Sora video generation
git submodule update --init --depth 1 video/Open-Sora
cd video/Open-Sora && pip install -e .
```
