# 👁️ Computer Vision

Image generation, editing, detection, segmentation, and visual understanding — from diffusion models to real-time detection.

## Overview

This directory contains **32 submodules** covering the full computer vision AI stack — from frontier image generation (Stable Diffusion, FLUX, Kolors) and editing (ControlNet, IP-Adapter, InstantID) to object detection (YOLO, Detectron2), segmentation (SAM2), 3D generation (Point-E, Shap-E), and production tooling (ComfyUI, InvokeAI).

## Submodules (32)

### Image Generation
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`diffusers`](https://github.com/huggingface/diffusers) | Hugging Face | The standard diffusion model library — Stable Diffusion, FLUX, Kolors, SDXL |
| [`stable-diffusion-original`](https://github.com/CompVis/stable-diffusion) | CompVis | Original Stable Diffusion research code |
| [`stable-diffusion-webui`](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | AUTOMATIC1111 | Most popular SD web UI |
| [`ComfyUI`](https://github.com/comfyanonymous/ComfyUI) | comfyanonymous | Node-based diffusion workflow engine |
| [`invokeai`](https://github.com/invoke-ai/InvokeAI) | InvokeAI | Creative engine for Stable Diffusion |
| [`fooocus`](https://github.com/lllyasviel/Fooocus) | lllyasviel | One-click Stable Diffusion with optimized UI |
| [`kohya-ss`](https://github.com/kohya-ss/sd-scripts) | kohya-ss | Training scripts for Stable Diffusion models |
| [`flux`](https://github.com/black-forest-labs/flux) | Black Forest Labs | Next-gen image generation model |
| [`kolors`](https://github.com/Kwai-Kolors/Kolors) | Kwai | High-quality Chinese-English bilingual image generator |
| [`stability-generative`](https://github.com/Stability-AI/generative-models) | Stability AI | SDXL, SVD, and generative model research |
| [`ml-stable-diffusion`](https://github.com/apple/ml-stable-diffusion) | Apple | Stable Diffusion on Apple Silicon with Core ML |
| [`dalle2-pytorch`](https://github.com/lucidrains/DALLE2-pytorch) | lucidrains | DALL-E 2 implementation in PyTorch |
| [`imagen-pytorch`](https://github.com/lucidrains/imagen-pytorch) | lucidrains | Imagen implementation in PyTorch |

### Image Editing & Control
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`controlnet`](https://github.com/lllyasviel/ControlNet) | lllyasviel | Adding conditional control to diffusion models |
| [`ip-adapter`](https://github.com/tencent-ailab/IP-Adapter) | Tencent | Image prompt adapter for style/content transfer |
| [`instantid`](https://github.com/InstantID/InstantID) | InstantID | Zero-shot identity-preserving generation |
| [`photomaker`](https://github.com/TencentARC/PhotoMaker) | TencentARC | Customizable realistic photo generation |
| [`instruct-pix2pix`](https://github.com/timothybrooks/instruct-pix2pix) | timothybrooks | Image editing via text instructions |
| [`realesrgan`](https://github.com/xinntao/Real-ESRGAN) | xinntao | Practical image/video restoration and super-resolution |
| [`deep-live-cam`](https://github.com/hacksider/Deep-Live-Cam) | hacksider | Real-time face swap and deepfake |

### Object Detection & Segmentation
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`segment-anything`](https://github.com/facebookresearch/segment-anything) | Meta | Foundation model for image segmentation |
| [`sam2`](https://github.com/facebookresearch/sam2) | Meta | Segment Anything Model 2 — video + image segmentation |
| [`grounding-dino`](https://github.com/IDEA-Research/GroundingDINO) | IDEA Research | Open-set object detection with language grounding |
| [`ultralytics`](https://github.com/ultralytics/ultralytics) | Ultralytics | YOLOv8 — real-time object detection |
| [`yolov9`](https://github.com/WongKinYiu/yolov9) | WongKinYiu | Next-generation YOLO architecture |
| [`detectron2`](https://github.com/facebookresearch/detectron2) | Meta | Detection and segmentation platform |
| [`mmdetection`](https://github.com/open-mmlab/mmdetection) | OpenMMLab | Object detection toolbox |
| [`supervision`](https://github.com/roboflow/supervision) | Roboflow | Computer vision visualization and tools |
| [`omniparser`](https://github.com/microsoft/OmniParser) | Microsoft | Screen parsing for GUI agents |

### Depth & 3D
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`depth-anything`](https://github.com/LiheYoung/Depth-Anything) | LiheYoung | Foundation model for monocular depth estimation |
| [`point-e`](https://github.com/openai/point-e) | OpenAI | 3D point cloud generation from text |
| [`shap-e`](https://github.com/openai/shap-e) | OpenAI | 3D object generation from text/images |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Image Generation** | diffusers, ComfyUI, flux, stable-diffusion-webui |
| **Image Editing** | controlnet, ip-adapter, instruct-pix2pix |
| **Detection** | ultralytics (YOLOv8), grounding-dino, detectron2 |
| **Segmentation** | sam2, segment-anything |
| **Super Resolution** | realesrgan |
| **3D Generation** | point-e, shap-e |
| **Training SD** | kohya-ss, diffusers |

## Usage

```bash
# Run ComfyUI workflow engine
git submodule update --init --depth 1 vision/ComfyUI
cd vision/ComfyUI && pip install -r requirements.txt && python main.py

# YOLOv8 object detection
git submodule update --init --depth 1 vision/ultralytics
pip install ultralytics && yolo detect predict model=yolov8n.pt source=image.jpg

# Segment Anything
git submodule update --init --depth 1 vision/sam2
pip install sam2
```
