# ⚙️ Orchestration Frameworks

The world's most comprehensive collection of AI agent orchestration, LLM application, and ML development frameworks.

## Overview

This directory houses **71 submodules** covering the full spectrum of AI development — from foundational LLM frameworks (LangChain, LlamaIndex) and multi-agent systems (AutoGen, CrewAI) to structured output engines, autonomous agents, UI builders, and core ML/NLP libraries. Everything you need to build production AI applications.

## Submodules (71)

### Foundational LLM Frameworks
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`langchain`](https://github.com/langchain-ai/langchain) | LangChain | The most popular LLM application framework |
| [`llama_index`](https://github.com/run-llama/llama_index) | LlamaIndex | Data framework for LLM applications |
| [`semantic-kernel`](https://github.com/microsoft/semantic-kernel) | Microsoft | AI orchestration SDK for .NET/Python/Java |
| [`haystack`](https://github.com/deepset-ai/haystack) | deepset | End-to-end NLP/RAG framework |
| [`llama-stack`](https://github.com/meta-llama/llama-stack) | Meta | Official Llama application stack |
| [`lightrag`](https://github.com/HKUDS/LightRAG) | HKUDS | Ultra-fast RAG with knowledge graphs |

### Agent Workflows & Structured Output
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`langgraph`](https://github.com/langchain-ai/langgraph) | LangChain | Stateful multi-agent workflow graphs |
| [`pydantic-ai`](https://github.com/pydantic/pydantic-ai) | Pydantic | Type-safe AI agents with Pydantic validation |
| [`openai-agents-python`](https://github.com/openai/openai-agents-python) | OpenAI | Official OpenAI agent SDK |
| [`dspy`](https://github.com/stanfordnlp/dspy) | Stanford NLP | Programming (not prompting) LLMs with automatic optimization |
| [`guidance`](https://github.com/guidance-ai/guidance) | guidance-ai | Structured and constrained generation engine |
| [`outlines`](https://github.com/outlines-dev/outlines) | outlines-dev | JSON/regex-constrained text generation |
| [`typechat`](https://github.com/microsoft/TypeChat) | Microsoft | Type-safe LLM response schemas |
| [`marvin`](https://github.com/prefecthq/marvin) | Prefect | AI engineering toolkit for structured extraction |
| [`controlflow`](https://github.com/PrefectHQ/ControlFlow) | Prefect | Agentic workflow orchestration by Prefect |
| [`mirascope`](https://github.com/Mirascope/mirascope) | Mirascope | Pythonic LLM library with multi-provider support |

### Multimodal & Tool Agents
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`agno`](https://github.com/agno-agi/agno) | Agno | Multimodal agent framework (formerly Phidata) |
| [`composio`](https://github.com/composio-dev/composio) | Composio | 250+ tool integrations for AI agents |
| [`openai-swarm`](https://github.com/openai/swarm) | OpenAI | Lightweight agent handoff orchestration |
| [`code-interpreter`](https://github.com/e2b-dev/code-interpreter) | E2B | Sandboxed code execution environment for AI |
| [`bmtools`](https://github.com/OpenBMB/BMTools) | OpenBMB | Tool learning for big models |
| [`owl`](https://github.com/camel-ai/owl) | CAMEL AI | Optimized Workforce Learning for multi-agent tasks |
| [`google-adk`](https://github.com/google/adk-python) | Google | Agent Development Kit for Gemini ecosystem |
| [`a2a-python`](https://github.com/google/a2a-python) | Google | Agent-to-Agent protocol implementation |
| [`mcp-agent`](https://github.com/lastmile-ai/mcp-agent) | LastMile AI | MCP-native agent framework |

### Multi-Agent Systems
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`autogen`](https://github.com/microsoft/autogen) | Microsoft | Multi-agent conversation framework |
| [`autogen-core`](https://github.com/microsoft/autogen) | Microsoft | AutoGen core library |
| [`ag2`](https://github.com/ag2ai/ag2) | AG2 | Next-gen multi-agent framework (AutoGen fork) |
| [`crewAI`](https://github.com/crewAIInc/crewAI) | CrewAI | Role-based AI agent crews |
| [`crew-ai-tools`](https://github.com/crewAIInc/crewAI-tools) | CrewAI | Tool extensions for CrewAI |
| [`MetaGPT`](https://github.com/geekan/MetaGPT) | geekan | Multi-agent meta programming framework |
| [`smolagents`](https://github.com/huggingface/smolagents) | Hugging Face | Lightweight agent framework from HF |
| [`swarms`](https://github.com/kyegomez/swarms) | kyegomez | Scalable multi-agent swarm intelligence |
| [`chatdev`](https://github.com/OpenBMB/ChatDev) | OpenBMB | AI-powered virtual software company |
| [`camel-ai`](https://github.com/camel-ai/camel) | CAMEL AI | Communicative agents for multi-agent exploration |
| [`atomic-agents`](https://github.com/BrainBlend-AI/atomic-agents) | BrainBlend | Modular composable agent framework |
| [`agentgpt`](https://github.com/reworkd/AgentGPT) | Reworkd | Browser-based autonomous agent platform |

### Autonomous Agents
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`babyagi`](https://github.com/yoheinakajima/babyagi) | yoheinakajima | Task-driven autonomous agent pioneer |
| [`devika`](https://github.com/stitionai/devika) | stitionai | Agentic AI software engineer |
| [`open-interpreter`](https://github.com/OpenInterpreter/open-interpreter) | OpenInterpreter | Natural language computer interface |

### Workflow & Pipeline Engines
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`embedchain`](https://github.com/embedchain/embedchain) | embedchain | Simple RAG framework |
| [`taskweaver`](https://github.com/microsoft/TaskWeaver) | Microsoft | Code-first agent framework |
| [`promptflow`](https://github.com/microsoft/promptflow) | Microsoft | LLM workflow automation and evaluation |
| [`chainlit`](https://github.com/Chainlit/chainlit) | Chainlit | Conversational AI app builder |
| [`semantic-router`](https://github.com/aurelio-labs/semantic-router) | Aurelio Labs | Semantic intent routing for LLMs |
| [`canals`](https://github.com/deepset-ai/canals) | deepset | DAG pipeline architecture |
| [`celery`](https://github.com/celery/celery) | Celery | Distributed task queue for async workflows |
| [`llmware`](https://github.com/llmware-ai/llmware) | LLMWare | Enterprise RAG pipeline |
| [`cohere-toolkit`](https://github.com/cohere-ai/cohere-toolkit) | Cohere | Enterprise AI application toolkit |
| [`langmem`](https://github.com/langchain-ai/langmem) | LangChain | Long-term memory for LangChain agents |

### Memory & Context
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`mem0ai`](https://github.com/mem0ai/mem0) | Mem0 | Memory layer for personalized AI applications |

### Sandboxing & Security
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`opensandbox`](https://github.com/alibaba/OpenSandbox) | Alibaba | Secure sandbox environment for agent code execution |
| [`openviking`](https://github.com/volcengine/OpenViking) | Volcengine | Context database for AI agent workflows |

### UI Builders
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`gradio`](https://github.com/gradio-app/gradio) | Gradio | ML demo UI builder — 3 lines of code |
| [`streamlit`](https://github.com/streamlit/streamlit) | Streamlit | Data app framework for rapid prototyping |

### Core ML & NLP Libraries
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`pytorch`](https://github.com/pytorch/pytorch) | PyTorch | Industry-standard deep learning framework |
| [`spacy`](https://github.com/explosion/spaCy) | Explosion | Industrial-strength NLP pipeline |
| [`fastapi`](https://github.com/fastapi/fastapi) | FastAPI | High-performance async API framework |
| [`tinygrad`](https://github.com/tinygrad/tinygrad) | tinygrad | Minimal neural network framework |
| [`transformers-js`](https://github.com/xenova/transformers.js) | Xenova | Run Transformers models in JavaScript |
| [`jina`](https://github.com/jina-ai/jina) | Jina AI | Cloud-native neural search framework |
| [`vercel-ai-sdk`](https://github.com/vercel/ai) | Vercel | AI SDK for building web AI apps |
| [`mastra`](https://github.com/mastra-ai/mastra) | Mastra | TypeScript-first AI agent framework |
| [`onnxruntime`](https://github.com/microsoft/onnxruntime) | Microsoft | Cross-platform ML inference engine |
| [`colossalai`](https://github.com/hpcaitech/ColossalAI) | HPC-AI Tech | Efficient large model training and inference |
| [`spring-ai`](https://github.com/spring-projects/spring-ai) | Spring | AI integration for Java/Spring ecosystem |
| [`litserve`](https://github.com/Lightning-AI/litserve) | Lightning AI | Lightning-fast model serving |
| [`qwen-agent`](https://github.com/QwenLM/Qwen-Agent) | Qwen | Agent framework for Qwen models |

### Robotics
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`lerobot`](https://github.com/huggingface/lerobot) | Hugging Face | Real-world robotics with AI |

### Project Management
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`superpowers`](https://github.com/obra/superpowers) | obra | AI project management |
| [`ccpm`](https://github.com/automazeio/ccpm) | automazeio | Critical chain project management |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **LLM App Framework** | langchain, llama_index, haystack, semantic-kernel |
| **Agent Orchestration** | langgraph, crewAI, autogen, pydantic-ai |
| **Structured Output** | outlines, guidance, dspy, typechat |
| **Multi-Agent Systems** | autogen, crewAI, MetaGPT, swarms, camel-ai |
| **Tool Integration** | composio, agno, mcp-agent |
| **RAG Pipelines** | lightrag, embedchain, llmware |
| **UI / Demo** | gradio, streamlit, chainlit |

## Usage

```bash
# Init LangChain
git submodule update --init --depth 1 frameworks/langchain

# Init multiple frameworks
git submodule update --init --depth 1 frameworks/langgraph frameworks/pydantic-ai frameworks/crewAI
```
