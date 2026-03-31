# 🧩 Reasoning & Prompting

Advanced reasoning, prompt engineering, tool-use, and cognitive-architecture frameworks for LLMs.

## Overview

This directory contains **24 submodules** exploring the frontiers of LLM reasoning — from chain-of-thought and tree-of-thought techniques to self-reflection, tool-learning, and memory-augmented agents. These repos push AI beyond simple Q&A into genuine problem-solving.

## Submodules (24)

### Reasoning Techniques
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`chain-of-thought-hub`](https://github.com/FranxYao/chain-of-thought-hub) | FranxYao | Chain-of-thought prompting benchmarks |
| [`chain-of-verification`](https://github.com/ritun16/chain-of-verification) | ritun16 | Self-verification to reduce hallucinations |
| [`tree-of-thoughts`](https://github.com/princeton-nlp/tree-of-thought-llm) | Princeton NLP | Deliberate problem solving via search trees |
| [`self-refine`](https://github.com/madaan/self-refine) | madaan | Iterative self-refinement without supervision |
| [`self-rag`](https://github.com/AkariAsai/self-rag) | AkariAsai | Self-reflective retrieval-augmented generation |
| [`reflexion`](https://github.com/noahshinn/reflexion) | noahshinn | Agents that learn from trial and error |
| [`llm-reasoners`](https://github.com/maitrix-org/llm-reasoners) | maitrix | Unified library for LLM reasoning algorithms |
| [`Awesome-LLM-Reasoning`](https://github.com/atfortes/Awesome-LLM-Reasoning) | atfortes | Curated reasoning papers and resources |

### Tool Use & Function Calling
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`gorilla`](https://github.com/ShishirPatil/gorilla) | UC Berkeley | API call generation for LLMs |
| [`toolformer`](https://github.com/lucidrains/toolformer-pytorch) | lucidrains | PyTorch implementation of tool-learning |
| [`prompttools`](https://github.com/hegelai/prompttools) | hegelai | Testing and experimentation for prompts and LLMs |
| [`ell`](https://github.com/MadcowD/ell) | MadcowD | Prompt engineering as a language — tracking and versioning |

### Agent Architectures
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`letta`](https://github.com/cpacker/MemGPT) | cpacker | Stateful agents with long-term memory (MemGPT) |
| [`opendevin`](https://github.com/All-Hands-AI/OpenHands) | All-Hands AI | AI software development agent |
| [`agentscope`](https://github.com/modelscope/agentscope) | ModelScope | Multi-agent platform with fault tolerance |
| [`voyager`](https://github.com/MineDojo/Voyager) | MineDojo | LLM-powered lifelong learning agent in Minecraft |
| [`phidata`](https://github.com/phidatahq/phidata) | Phidata | Build agents with memory, knowledge, and tools |
| [`adalflow`](https://github.com/SylphAI-Inc/AdalFlow) | SylphAI | Building and auto-optimizing LLM task pipelines |
| [`camel`](https://github.com/camel-ai/camel) | CAMEL AI | Communicative agents for multi-agent exploration |
| [`graphiti`](https://github.com/getzep/graphiti) | Zep | Temporal knowledge graph for agent memory |
| [`tensorzero`](https://github.com/tensorzero/tensorzero) | TensorZero | Data and learning platform for LLM applications |

### Gradient-Based Prompt Optimization
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`textgrad`](https://github.com/zou-group/textgrad) | Stanford | Automatic differentiation through text |
| [`minichain`](https://github.com/srush/MiniChain) | Sasha Rush | Minimal LLM chain library |
| [`litgpt`](https://github.com/Lightning-AI/litgpt) | Lightning AI | Pretrain, finetune, deploy LLMs efficiently |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Reasoning** | tree-of-thoughts, chain-of-thought-hub, self-refine |
| **Self-Correction** | reflexion, self-rag, chain-of-verification |
| **Tool Learning** | gorilla, toolformer |
| **Agent Memory** | letta, graphiti, phidata |
| **Prompt Optimization** | textgrad, ell, dspy (in frameworks/) |

## Usage

```bash
# Explore tree-of-thought prompting
git submodule update --init --depth 1 reasoning/tree-of-thoughts

# Run OpenHands coding agent
git submodule update --init --depth 1 reasoning/opendevin
cd reasoning/opendevin && docker compose up
```
