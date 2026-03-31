# 🎯 Prompt Skills & Cookbooks

Prompt engineering guides, official provider cookbooks, agent recipes, and development patterns.

## Overview

This directory contains **26 submodules** of battle-tested prompt engineering resources — from official cookbooks (OpenAI, Anthropic, Google, Meta) and prompt engineering guides to agent recipes, development patterns, and productivity tools that maximize what you can do with LLMs.

## Submodules (26)

### Official Provider Cookbooks
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`openai-cookbook`](https://github.com/openai/openai-cookbook) | OpenAI | Official OpenAI usage examples and best practices |
| [`anthropic-cookbook`](https://github.com/anthropics/anthropic-cookbook) | Anthropic | Official Claude code recipes and patterns |
| [`gemini-cookbook`](https://github.com/google-gemini/cookbook) | Google | Official Gemini API cookbook |
| [`google-ai-docs`](https://github.com/google/generative-ai-docs) | Google | Google's generative AI documentation |

### Prompt Engineering
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`prompt-engineering-guide`](https://github.com/dair-ai/Prompt-Engineering-Guide) | DAIR.AI | Comprehensive prompt engineering guide |
| [`prompt-engineering`](https://github.com/brexhq/prompt-engineering) | Brex | Enterprise prompt engineering patterns and tips |
| [`ai-prompts`](https://github.com/mustvlad/ChatGPT-System-Prompts) | mustvlad | Collection of system prompt examples |
| [`chatgpt-autoexpert`](https://github.com/spdustin/ChatGPT-AutoExpert) | spdustin | Supercharged ChatGPT system prompts |
| [`instructor`](https://github.com/jxnl/instructor) | jxnl | Structured output extraction from LLMs |
| [`instructor-ai`](https://github.com/instructor-ai/instructor) | Instructor AI | Multi-language structured extraction library |

### Agent Skills & Development
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`awesome-claude-code`](https://github.com/nicobailon/awesome-claude-code) | nicobailon | Curated Claude Code resources |
| [`awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | PatrickJS | Curated Cursor AI rules collection |
| [`awesome-mcp-servers`](https://github.com/punkpeye/awesome-mcp-servers) | punkpeye | Curated MCP server collection |
| [`claude-code-action`](https://github.com/anthropics/claude-code-action) | Anthropic | Claude Code in GitHub Actions |
| [`browser-use`](https://github.com/browser-use/browser-use) | browser-use | AI agent browser automation |
| [`fabric`](https://github.com/danielmiessler/fabric) | danielmiessler | AI augmentation framework with patterns |
| [`rags`](https://github.com/run-llama/rags) | LlamaIndex | RAG recipe collection |
| [`search-with-lepton`](https://github.com/leptonai/search_with_lepton) | Lepton AI | AI-powered search engine reference |
| [`lobe-chat-agents`](https://github.com/lobehub/lobe-chat-agents) | LobeHub | Agent marketplace for LobeChat |

### Thinking Frameworks
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`first-principles-thinking`](https://github.com/nicobailon/first-principles-thinking) | nicobailon | First-principles reasoning for AI agents |
| [`design-thinking`](https://github.com/nicobailon/design-thinking) | nicobailon | Design thinking framework for AI development |
| [`devil-advocate`](https://github.com/nicobailon/devil-advocate) | nicobailon | Adversarial reasoning for better decisions |
| [`ooda-loop`](https://github.com/nicobailon/ooda-loop) | nicobailon | Observe-Orient-Decide-Act decision framework |
| [`self-correction-loop`](https://github.com/nicobailon/self-correction-loop) | nicobailon | Self-correction patterns for AI agents |
| [`system-impact-analyzer`](https://github.com/nicobailon/system-impact-analyzer) | nicobailon | System impact analysis for code changes |
| [`tdd-advanced`](https://github.com/nicobailon/tdd-advanced) | nicobailon | Advanced TDD patterns for AI workflows |

## Key Capabilities

| Category | Best Options |
|----------|--------|
| **Prompt Guides** | prompt-engineering-guide, prompt-engineering |
| **Structured Output** | instructor, instructor-ai |
| **Official Recipes** | openai-cookbook, anthropic-cookbook, gemini-cookbook |
| **Browser Agents** | browser-use |
| **AI Patterns** | fabric, awesome-claude-code |

## Usage

```bash
# Get prompt engineering guide
git submodule update --init --depth 1 skills/prompt-engineering-guide

# Use instructor for structured output
git submodule update --init --depth 1 skills/instructor
pip install instructor
```
