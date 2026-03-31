# 🏋️ Model Training

Everything needed to train, fine-tune, and optimize LLMs — from distributed training frameworks to quantization, RLHF, and efficient fine-tuning.

## Overview

This directory contains **37 submodules** spanning the full model training spectrum — from massive distributed training (DeepSpeed, Megatron-LM) and efficient fine-tuning (LoRA, PEFT, Unsloth) to quantization (GPTQ, bitsandbytes), RLHF (TRL, OpenRLHF), custom kernels (Flash Attention, CUTLASS), and Apple Silicon training (MLX).

## Submodules (37)

### Distributed Training
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`DeepSpeed`](https://github.com/microsoft/DeepSpeed) | Microsoft | Ultra-efficient distributed training |
| [`deepspeed-examples`](https://github.com/microsoft/DeepSpeedExamples) | Microsoft | DeepSpeed usage examples and recipes |
| [`deepspeed-mii`](https://github.com/microsoft/DeepSpeed-MII) | Microsoft | Model Implementations for Inference |
| [`megatron-lm`](https://github.com/NVIDIA/Megatron-LM) | NVIDIA | Large-scale distributed LLM training |
| [`colossalai`](https://github.com/hpcaitech/ColossalAI) | HPC-AI Tech | Efficient large model training (also in frameworks/) |
| [`accelerate`](https://github.com/huggingface/accelerate) | Hugging Face | Simple distributed training abstraction |
| [`pytorch-lightning`](https://github.com/Lightning-AI/pytorch-lightning) | Lightning AI | Lightweight PyTorch training framework |
| [`nemo`](https://github.com/NVIDIA/NeMo) | NVIDIA | Scalable GenAI training framework |

### Fine-Tuning
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`LLaMA-Factory`](https://github.com/hiyouga/LLaMA-Factory) | hiyouga | One-stop LLM fine-tuning platform |
| [`unsloth`](https://github.com/unslothai/unsloth) | Unsloth | 2x faster fine-tuning with 80% less memory |
| [`peft`](https://github.com/huggingface/peft) | Hugging Face | Parameter-efficient fine-tuning (LoRA, QLoRA, etc.) |
| [`lora`](https://github.com/microsoft/LoRA) | Microsoft | Original Low-Rank Adaptation implementation |
| [`axolotl`](https://github.com/axolotl-ai-cloud/axolotl) | Axolotl | Streamlined LLM fine-tuning toolkit |
| [`torchtune`](https://github.com/pytorch/torchtune) | PyTorch | Official PyTorch LLM fine-tuning library |
| [`trl`](https://github.com/huggingface/trl) | Hugging Face | Transformers reinforcement learning (RLHF/DPO) |
| [`ms-swift`](https://github.com/modelscope/ms-swift) | ModelScope | Efficient LLM training and inference framework |
| [`mistral-finetune`](https://github.com/mistralai/mistral-finetune) | Mistral AI | Official Mistral fine-tuning toolkit |
| [`nanotron`](https://github.com/huggingface/nanotron) | Hugging Face | Minimalist large model training |
| [`alignment-handbook`](https://github.com/huggingface/alignment-handbook) | Hugging Face | Robust alignment recipes for LLMs |
| [`openrlhf`](https://github.com/OpenRLHF/OpenRLHF) | OpenRLHF | High-performance RLHF framework |
| [`verl`](https://github.com/volcengine/verl) | Volcengine | Volcano Engine RL for LLM training |
| [`olive`](https://github.com/microsoft/Olive) | Microsoft | Hardware-aware model optimization toolkit |
| [`petals`](https://github.com/bigscience-workshop/petals) | BigScience | Run LLMs collaboratively over the internet |

### Quantization
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`bitsandbytes`](https://github.com/bitsandbytes-foundation/bitsandbytes) | bitsandbytes | 8-bit/4-bit quantization primitives |
| [`autogptq`](https://github.com/AutoGPTQ/AutoGPTQ) | AutoGPTQ | Automated GPTQ quantization |
| [`exllamav2`](https://github.com/turboderp/exllamav2) | turboderp | Fast quantized inference for Llama models |
| [`ggml`](https://github.com/ggml-org/ggml) | GGML | Tensor library for ML — powers GGUF format |

### Inference Optimization
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`TensorRT-LLM`](https://github.com/NVIDIA/TensorRT-LLM) | NVIDIA | TensorRT for LLM inference acceleration |
| [`text-generation-inference`](https://github.com/huggingface/text-generation-inference) | Hugging Face | Production text generation server |

### Custom Kernels & Hardware
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`flash-attention`](https://github.com/Dao-AILab/flash-attention) | Dao-AILab | IO-aware exact attention — 2-4x faster training |
| [`cutlass`](https://github.com/NVIDIA/cutlass) | NVIDIA | CUDA templates for GEMM and beyond |
| [`llama-cpp-python`](https://github.com/abetlen/llama-cpp-python) | abetlen | Python bindings for llama.cpp |

### Core Frameworks
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`transformers`](https://github.com/huggingface/transformers) | Hugging Face | The standard library for pretrained models |
| [`jax`](https://github.com/google/jax) | Google | High-performance numerical computing with autograd |
| [`keras`](https://github.com/keras-team/keras) | Keras | Multi-backend deep learning API |

### Apple Silicon
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`mlx`](https://github.com/ml-explore/mlx) | Apple | ML framework optimized for Apple Silicon |
| [`mlx-examples`](https://github.com/ml-explore/mlx-examples) | Apple | MLX example models and fine-tuning scripts |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **One-Click Fine-Tune** | LLaMA-Factory, unsloth, axolotl |
| **Distributed Training** | DeepSpeed, megatron-lm, accelerate |
| **RLHF/DPO** | trl, openrlhf, verl |
| **LoRA/PEFT** | peft, lora, torchtune |
| **Quantization** | bitsandbytes, autogptq, exllamav2 |
| **Kernel Optimization** | flash-attention, cutlass, TensorRT-LLM |
| **Apple Silicon** | mlx, mlx-examples |

## Usage

```bash
# Quick fine-tune with LLaMA-Factory
git submodule update --init --depth 1 training/LLaMA-Factory
cd training/LLaMA-Factory && pip install -e . && llamafactory-cli train examples/lora_single_gpu/llama3_lora_sft.yaml

# Fine-tune with Unsloth (2x faster)
git submodule update --init --depth 1 training/unsloth
pip install unsloth
```
