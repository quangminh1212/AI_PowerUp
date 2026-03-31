# 🛡️ AI Safety & Security

Guardrails, red-teaming, and security tools to make AI systems safe, reliable, and resistant to adversarial attacks.

## Overview

This directory contains **5+ submodules** focused on AI safety — from prompt injection defense and output guardrails to LLM red-teaming and vulnerability scanning. Critical infrastructure for deploying LLMs in production without exposing your systems to misuse.

## Submodules (5+)

| Submodule | Source | Description |
|-----------|--------|-------------|
| [`NeMo-Guardrails`](https://github.com/NVIDIA/NeMo-Guardrails) | NVIDIA | Programmable guardrails for LLM apps — Colang rules for topic control, factuality, and jailbreak prevention |
| [`guardrails`](https://github.com/guardrails-ai/guardrails) | Guardrails AI | Output validation framework for LLMs — structured output enforcement and hallucination detection |
| [`garak`](https://github.com/leondz/garak) | leondz | LLM vulnerability scanner — automated red-teaming |
| [`llm-guard`](https://github.com/protectai/llm-guard) | Protect AI | Input/output guardrails for LLM interactions |
| [`rebuff`](https://github.com/protectai/rebuff) | Protect AI | Prompt injection detection service |

> **New additions being added**: heretic (adversarial testing), llm-attacks (jailbreak research), vigil (runtime monitoring)

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Guardrails** | NeMo-Guardrails, guardrails, llm-guard |
| **Red Teaming** | garak |
| **Prompt Injection** | rebuff, llm-guard |
| **Output Validation** | guardrails |

## Usage

```bash
# Init NeMo Guardrails
git submodule update --init --depth 1 security/NeMo-Guardrails
pip install nemoguardrails

# Scan LLM for vulnerabilities
git submodule update --init --depth 1 security/garak
pip install garak && python -m garak --model_type openai --model_name gpt-3.5-turbo
```
