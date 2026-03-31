# 📏 AI Evaluation & Testing

Benchmarking, testing, observability, and experiment tracking for AI/LLM systems.

## Overview

This directory contains **17 submodules** covering the full evaluation lifecycle — from LLM benchmarking and automated testing to production observability and experiment management. Essential for measuring model quality, detecting regressions, and ensuring reliable AI applications.

## Submodules (17)

### LLM Benchmarking
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) | EleutherAI | Industry-standard LLM benchmark framework (200+ tasks) |
| [`OpenCompass`](https://github.com/open-compass/OpenCompass) | COMPASS | Comprehensive LLM evaluation platform |
| [`swe-bench`](https://github.com/princeton-nlp/SWE-bench) | Princeton NLP | Benchmark for AI coding on real GitHub issues |
| [`mteb`](https://github.com/embeddings-benchmark/mteb) | MTEB | Massive text embedding benchmark (58 datasets) |
| [`vlm-eval`](https://github.com/open-compass/VLMEvalKit) | COMPASS | Vision-language model evaluation toolkit |
| [`lmms-eval`](https://github.com/EvolvingLMMs-Lab/lmms-eval) | EvolvingLMMs | Large multimodal model evaluation suite |
| [`evals`](https://github.com/openai/evals) | OpenAI | OpenAI's evaluation framework for LLMs |
| [`simple-evals`](https://github.com/openai/simple-evals) | OpenAI | Lightweight evaluation scripts for common benchmarks |
| [`chatbot-arena`](https://github.com/lm-sys/FastChat) | LMSYS | Chatbot Arena — human preference evaluation platform |

### LLM Testing & Quality
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`deepeval`](https://github.com/confident-ai/deepeval) | Confident AI | Unit testing framework for LLM applications |
| [`promptfoo`](https://github.com/promptfoo/promptfoo) | Promptfoo | Test prompts, models, and RAG pipelines systematically |
| [`ragas`](https://github.com/explodinggradients/ragas) | ExplodingGradients | RAG assessment — faithfulness, relevance, context metrics |
| [`inspect-ai`](https://github.com/UKGovernmentBEIS/inspect_ai) | UK Gov DSIT | Framework for evaluating AI safety and capabilities |

### Observability & Monitoring
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`langfuse`](https://github.com/langfuse/langfuse) | Langfuse | Open-source LLM observability — traces, prompts, evals |
| [`langsmith-sdk`](https://github.com/langchain-ai/langsmith-sdk) | LangChain | Debug, test, and monitor LangChain applications |
| [`phoenix`](https://github.com/Arize-AI/phoenix) | Arize AI | AI observability with trace visualization |
| [`helicone`](https://github.com/Helicone/helicone) | Helicone | LLM proxy with logging, caching, and cost tracking |
| [`agentops`](https://github.com/AgentOps-AI/agentops) | AgentOps | Session replays and metrics for AI agents |

### Experiment Tracking
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`wandb`](https://github.com/wandb/wandb) | Weights & Biases | ML experiment tracking, visualization, hyperparameter sweeps |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **LLM Benchmarks** | lm-evaluation-harness, OpenCompass, chatbot-arena |
| **RAG Testing** | ragas, deepeval, promptfoo |
| **Coding Evals** | swe-bench, evals |
| **Multimodal Evals** | vlm-eval, lmms-eval |
| **Production Tracing** | langfuse, phoenix, helicone |
| **Experiment Mgmt** | wandb, langsmith-sdk |

## Usage

```bash
# Run LLM benchmarks
git submodule update --init --depth 1 evaluation/lm-evaluation-harness
cd evaluation/lm-evaluation-harness && pip install lm-eval
lm_eval --model hf --model_args pretrained=meta-llama/Llama-3-8B --tasks hellaswag

# Test RAG quality
git submodule update --init --depth 1 evaluation/ragas
pip install ragas
```
