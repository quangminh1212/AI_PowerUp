# 🤖 AI Coding Agents

Terminal-native, IDE-integrated, and autonomous AI coding assistants for every development workflow.

## Overview

This directory contains **39 submodules** of the world's leading AI-powered coding agents — from fully autonomous software engineers to IDE extensions, browser automation, and specialized code review tools. These agents can write, debug, refactor, and deploy code with minimal human intervention.

## Submodules (39)

### Autonomous Coding Agents
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`AutoGPT`](https://github.com/Significant-Gravitas/AutoGPT) | Significant Gravitas | Pioneer autonomous AI agent with memory and tool use (~175k★) |
| [`openhands`](https://github.com/All-Hands-AI/OpenHands) | All-Hands-AI | Multi-tool open-source coding platform (~54k★) |
| [`codex`](https://github.com/openai/codex) | OpenAI | Terminal-native agentic coding from OpenAI (~66k★) |
| [`gpt-pilot`](https://github.com/Pythagora-io/gpt-pilot) | Pythagora | Full-app generation from natural language specifications (~35k★) |
| [`swe-agent`](https://github.com/SWE-agent/SWE-agent) | Princeton NLP | State-of-the-art autonomous software engineering (~20k★) |
| [`open-swe`](https://github.com/langchain-ai/open-swe) | LangChain | Async open-source SWE agent built on LangGraph |
| [`deepagents`](https://github.com/langchain-ai/deepagents) | LangChain | Deep-learning-powered agent harness for complex tasks |
| [`deer-flow`](https://github.com/bytedance/deer-flow) | ByteDance | Long-horizon SuperAgent for complex multi-step workflows |
| [`xagent`](https://github.com/OpenBMB/XAgent) | OpenBMB | Autonomous LLM agent with tool use and planning |
| [`jarvis`](https://github.com/microsoft/JARVIS) | Microsoft | Task-driven autonomous agent connecting multiple AI models |
| [`metagpt-agent`](https://github.com/geekan/MetaGPT) | geekan | Multi-role AI software company simulation |
| [`agentless`](https://github.com/OpenAutoCoder/Agentless) | OpenAutoCoder | Solves SWE-bench without complex agent loops — simple & effective |
| [`devon`](https://github.com/entropy-research/Devon) | Entropy Research | Open-source alternative to Devin AI software engineer |
| [`plandex`](https://github.com/plandex-ai/plandex) | Plandex | Terminal-based AI coding engine for complex multi-file tasks |

### Terminal & CLI Agents
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`claude-code`](https://github.com/anthropics/claude-code) | Anthropic | Agentic terminal-native coder with full codebase understanding |
| [`aider`](https://github.com/paul-gauthier/aider) | Paul Gauthier | Git-native AI pair programmer with multi-model support (~42k★) |
| [`gemini-cli`](https://github.com/google-gemini/gemini-cli) | Google | Gemini-powered command-line coding agent |
| [`goose`](https://github.com/block-open-source/goose) | Block | Open-source AI developer agent from Square/Cash App |
| [`mentat`](https://github.com/AbanteAI/mentat) | AbanteAI | Terminal-native AI coding assistant with undo/redo |
| [`gpt-runner`](https://github.com/nicepkg/gpt-runner) | nicepkg | File-based AI runner for any project |

### IDE Extensions & AI Editors
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`continue`](https://github.com/continuedev/continue) | Continue | Open-source AI code assistant for VS Code & JetBrains (~25k★) |
| [`cline`](https://github.com/cline/cline) | Cline | Autonomous coding agent inside VS Code |
| [`cursor`](https://github.com/getcursor/cursor) | Cursor | AI-first code editor with multi-file context |
| [`roo-code`](https://github.com/rooVetGit/Roo-Code) | Roo Code | Smart AI code assistant for VS Code |
| [`void`](https://github.com/voideditor/void) | Void | Open-source AI-powered code editor |
| [`tabby`](https://github.com/TabbyML/tabby) | TabbyML | Self-hosted AI code completion and chat (~30k★) |
| [`aide`](https://github.com/codestoryai/aide) | CodeStory | AI-native IDE with deep codebase understanding |

### Code Generation & Review
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`bolt-new`](https://github.com/stackblitz/bolt.new) | StackBlitz | Full-stack web app generator in browser sandbox |
| [`screenshot-to-code`](https://github.com/abi/screenshot-to-code) | abi | Convert UI screenshots to working code |
| [`pr-agent`](https://github.com/Codium-ai/pr-agent) | CodiumAI | AI-powered PR reviewer with auto-descriptions & suggestions |
| [`sweep`](https://github.com/sweepai/sweep) | Sweep AI | AI-powered GitHub issue-to-PR automation |

### Browser Automation & Web Agents
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`skyvern`](https://github.com/Skyvern-AI/skyvern) | Skyvern AI | Browser automation with visual page understanding (~10k★) |
| [`lavague`](https://github.com/lavague-ai/LaVague) | LaVague | AI web agent for browser task automation |

### Research & Code Search
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`gpt-researcher`](https://github.com/assafelovic/gpt-researcher) | assafelovic | Autonomous deep research agent |
| [`sourcegraph`](https://github.com/sourcegraph/sourcegraph-public-snapshot) | Sourcegraph | Code intelligence and search platform at scale |

### Multi-Provider SDKs & Foundations
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`anthropic-quickstarts`](https://github.com/anthropics/anthropic-quickstarts) | Anthropic | Official quick-start templates for Claude API |
| [`agent-zero`](https://github.com/frdel/agent-zero) | frdel | General-purpose AI agent framework |
| [`hermes-agent`](https://github.com/NousResearch/hermes-agent) | Nous Research | Self-improving agent built on Hermes models |
| [`astra`](https://github.com/awslabs/multi-agent-orchestrator) | AWS Labs | Multi-agent orchestrator for routing and coordination |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Autonomous Coding** | AutoGPT, openhands, codex, swe-agent, agentless, deer-flow |
| **Pair Programming** | aider, claude-code, continue, cline, goose |
| **PR Review** | pr-agent, sweep |
| **Full-App Generation** | bolt-new, gpt-pilot, screenshot-to-code |
| **Browser Automation** | skyvern, lavague |
| **Self-Hosted** | tabby, void, aide |

## Usage

```bash
# Init a specific agent
git submodule update --init --depth 1 agents/aider

# Run aider for AI pair programming
cd agents/aider && pip install -e . && aider

# Init OpenHands for autonomous coding
git submodule update --init --depth 1 agents/openhands
cd agents/openhands && docker compose up
```
