# 🧠 Memory Systems

Persistent memory layers enabling AI agents to remember, learn, and personalize over time.

## Overview

This directory contains **3 submodules** focused on long-term memory for AI systems — from personal AI memory layers to cognitive architectures with memory management. These tools solve the critical challenge of making AI agents stateful across conversations and sessions.

## Submodules (3)

| Submodule | Source | Description |
|-----------|--------|-------------|
| [`mem0`](https://github.com/mem0ai/mem0) | Mem0 | Memory layer for personalized AI applications (~25k★) — stores user preferences, context, and history across sessions |
| [`memgpt`](https://github.com/cpacker/MemGPT) | cpacker | OS-inspired LLM memory management (~13k★, now Letta) — virtual context window with tiered memory for unlimited conversations |
| [`cipher`](https://github.com/nicobailon/cipher) | nicobailon | Encrypted memory storage for sensitive AI contexts |

## Key Capabilities

| Capability | Best Option |
|-----------|------------|
| **User Personalization** | mem0 — stores preferences and learns over time |
| **Unlimited Context** | memgpt — virtual memory paging for long conversations |
| **Secure Storage** | cipher — encrypted memory for sensitive data |

## Usage

```bash
# Init Mem0 memory layer
git submodule update --init --depth 1 memory/mem0
pip install mem0ai

# Init MemGPT (Letta)
git submodule update --init --depth 1 memory/memgpt
pip install letta
```
