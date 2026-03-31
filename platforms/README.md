# 🖥️ AI Platforms

Full-stack AI application platforms with visual builders, workflow engines, and chat interfaces.

## Overview

This directory contains **14 submodules** of production-ready AI platforms — from visual workflow builders (Dify, Flowise, n8n) and chatbot frameworks (Rasa, Botpress) to academic-oriented tools and API management. These are the "no-code / low-code" tools that let teams deploy AI applications without heavy engineering.

## Submodules (14)

### Visual AI Workflow Builders
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`dify`](https://github.com/langgenius/dify) | Dify | Open-source LLMOps platform with visual builder |
| [`flowise`](https://github.com/FlowiseAI/Flowise) | Flowise | Drag & drop LLM flow builder |
| [`flowise-embed`](https://github.com/FlowiseAI/FlowiseChatEmbed) | Flowise | Embeddable chat widget for Flowise |
| [`langflow`](https://github.com/langflow-ai/langflow) | Langflow | Visual framework for multi-agent AI |
| [`n8n`](https://github.com/n8n-io/n8n) | n8n | Fair-code workflow automation platform |
| [`fastgpt`](https://github.com/labring/FastGPT) | Sealos | Knowledge-base QA platform with visual orchestration |
| [`maxkb`](https://github.com/1Panel-dev/MaxKB) | 1Panel | Knowledge-base QA system with RAG pipeline |

### Chat Applications
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`chatgpt-next`](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) | CNXW | Cross-platform ChatGPT interface |
| [`gpt-academic`](https://github.com/binary-husky/gpt_academic) | binary-husky | Academic writing & research assistant |

### Chatbot Frameworks
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`rasa`](https://github.com/RasaHQ/rasa) | Rasa | Enterprise conversational AI framework |
| [`botpress`](https://github.com/botpress/botpress) | Botpress | Conversational AI development platform |

### API & Agent Management
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`oneapi`](https://github.com/songquanpeng/one-api) | songquanpeng | Multi-LLM API proxy — unified management |
| [`opengpts`](https://github.com/langchain-ai/opengpts) | LangChain | Open-source GPTs alternative by LangChain |
| [`vane`](https://github.com/nicobailon/vane) | nicobailon | AI agent orchestration platform |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Visual Builder** | dify, flowise, langflow, n8n |
| **Knowledge QA** | fastgpt, maxkb |
| **Chat Interface** | chatgpt-next, gpt-academic |
| **Conversational AI** | rasa, botpress |
| **API Gateway** | oneapi |

## Usage

```bash
# Deploy Dify platform
git submodule update --init --depth 1 platforms/dify
cd platforms/dify && docker compose up -d

# Start Flowise visual builder
git submodule update --init --depth 1 platforms/flowise
npx flowise start
```
