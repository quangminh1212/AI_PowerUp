<!-- source: https://github.com/subinium/awesome-agent-frameworks.git sha: e4a80292813c74114613fdb7fed5fa0bcbf32558 readme: main/README.md -->
# subinium/awesome-agent-frameworks

Architecture-focused guide to open-source personal AI agent frameworks (the Claw ecosystem)

---

# Awesome Agent Frameworks

**English** | [中文](README_CN.md) | [日本語](README_JA.md) | [한국어](README_KO.md)

An architecture-focused guide to the open-source personal AI agent ecosystem (the "Claw" family).

Not a link dump. Each entry explains **what problem it solves, how it solves it, and why that approach matters**.

---

## Table of Contents

- [How to Read This Guide](#how-to-read-this-guide)
- [The Origin Story](#the-origin-story)
- [Architecture Map](#architecture-map)
- [By Category](#by-category)
  - [Full Platform](#full-platform)
  - [Lightweight](#lightweight)
  - [Rust Native](#rust-native)
  - [Embedded / Edge](#embedded--edge)
  - [Unique Paradigm](#unique-paradigm)
  - [Python Ecosystem](#python-ecosystem)
  - [Mobile](#mobile)
  - [Other Languages](#other-languages)
- [Cross-Cutting Comparisons](#cross-cutting-comparisons)
  - [Security Models](#security-models)
  - [Channel Coverage](#channel-coverage)
  - [LLM Provider Strategy](#llm-provider-strategy)
  - [Memory & Learning](#memory--learning)
  - [Deployment Targets](#deployment-targets)
- [By Popularity](#by-popularity)
- [Decision Framework](#decision-framework)
- [Contributing](#contributing)

---

## Disclaimer

This guide describes **architecture and design intent**, not guaranteed working software.

**Verification scope**: We cloned all repos and read source code to verify repo existence, license files, primary language, and structural claims (file counts, module organization, trait definitions). We did **not** build binaries, run tests, or verify runtime behavior. Performance numbers (binary size, RAM, boot time) are taken from project READMEs — not independently measured. Channel and tool counts are based on code definitions, not confirmed integrations.

**LOC and numeric claims**: Many projects market themselves with selective metrics. "~4K LOC" may refer to a core subset while the full codebase is 10-50x larger. "Zero unsafe code" may mean workspace-level deny with per-crate exceptions. We note these nuances where we found them, but we may have missed some.

**Opinions and superlatives**: Phrases like "the most auditable" or "designed for maximum security" reflect design intent and relative positioning within this ecosystem, not absolute benchmarks. We have not conducted formal security audits or performance comparisons.

**License warnings**: Two projects (HermitClaw, DroidClaw) had no LICENSE file at the time of our audit. Without a license file, code is legally "all rights reserved" regardless of verbal claims. Check the repo before depending on it.

**Freshness**: Star counts and version numbers are snapshots. The shields.io badges above each entry are live. The "By Popularity" table is a point-in-time reference.

**Not affiliated**: This guide is not endorsed by or affiliated with any listed project. If you are a maintainer and believe something is inaccurate, please open an issue.

---

## How to Read This Guide

Each framework entry follows this structure:

> **Concept** — The core idea in one sentence.
>
> **Architecture** — How the agent loop, tools, and state management work.
>
> **Key Trade-off** — What this framework optimizes for, and what it sacrifices.
>
> **When to Choose** — The scenario where this is the best option.

---

## The Origin Story

In November 2025, Peter Steinberger released **Clawdbot** — a personal AI assistant that operated across messaging channels. Renamed **OpenClaw** in January 2026, it became one of the fastest-growing open-source projects on GitHub.

The community reaction was split. Some loved it. Others thought hundreds of thousands of lines of TypeScript was too much for a personal assistant. Within 3 months, dozens of alternatives emerged — each making a different trade-off:

- "What if we stripped it down to a small, auditable core?" → NanoClaw
- "What if it ran on a $5 microcontroller?" → MimiClaw
- "What if the agent improved itself?" → Hermes Agent
- "What if the database WAS the agent?" → SupaClaw
- "What if it were a creature, not a tool?" → HermitClaw

This guide maps that design space.

---

## Architecture Map

```
  Footprint          Small ◄──────────────────────► Large
                     │                                │
  ┌──────────────────┼────────────────────────────────┤
  │                  │                                │
  │  Embedded/Edge   │          Server/Cloud          │
  │                  │                                │
  │  NullClaw  678KB │  nanobot ··· NanoClaw          │
  │  MimiClaw  ~2MB  │  BabyClaw · TinyClaw           │
  │  Autobot   2MB   │  Hermes ··· AstrBot            │
  │  PicoClaw  ~8MB  │  TrinityClaw · SupaClaw        │
  │  ZeptoClaw ~6MB  │  HermitClaw                    │
  │                  │                                │
  │  ZeroClaw  ~9MB  │  MicroClaw · OpenCrabs         │
  │  FastClaw (Go)   │  NemoClaw (OpenClaw wrapper)   │
  │                  │  Moltis ···· IronClaw           │
  │                  │  OpenFang ·· OpenClaw           │
  │                  │                                │
  │  ◄── Rust/Zig/C/Go ──►  │  ◄── TS/Python ──►     │
  │  compile to binary       │  need runtime          │
  └──────────────────┴────────────────────────────────┘
                     │
  Learning    Static │ ──────────────────► Self-improving
                     │
              Most   │  Hermes (skill auto-creation)
              agents │  OpenCrabs (self-modification)
                     │  HermitClaw (belief evolution)
                     │  TrinityClaw (dynamic skills)
                     │  BabyClaw (personality cron)
```

**How to read**: Left side = compiled, single-binary agents sorted by size. Right side = runtime-dependent agents. Bottom axis highlights which agents have learning/self-improvement capabilities.

---

## By Category

### Full Platform

#### OpenClaw

> **Concept**: The original. A hub-and-spoke gateway that routes messages from 22+ channels through an execution pipeline with retry/fallback logic.

**Architecture**: Large TypeScript monorepo (our source audit measured ~200K LOC in .ts/.js files; community references cite ~500K but this is unverified). Messages enter via the Gateway WebSocket on port 18789. The execution pipeline handles queue policies, retry/fallback, and skill resolution through a priority system (workspace → bundled → plugins). State management and memory indexing are handled internally.

**Key Trade-off**: Maximum feature completeness at the cost of complexity. The codebase is large enough that no single person can review it all. The `openclaw doctor --fix` command exists specifically because the system has many failure modes.

**When to Choose**: You want a production-ready assistant with native iOS/Android apps, voice wake, live canvas, browser-based onboarding, and the largest community in the ecosystem.

`TypeScript` · `MIT` · [openclaw/openclaw](https://github.com/openclaw/openclaw) · ![Stars](https://img.shields.io/github/stars/openclaw/openclaw?style=flat-square)

---

#### NemoClaw

> **Concept**: Not an agent — a security harness. Runs OpenClaw inside NVIDIA OpenShell with kernel-level sandboxing and managed NVIDIA inference.

**Architecture**: NemoClaw is an OpenClaw plugin + CLI orchestrator, not a standalone agent. It creates a Landlock + seccomp + network namespace sandbox via NVIDIA OpenShell, routes inference through NVIDIA Nemotron models (120B/253B/49B/30B), and enforces per-binary network policies (e.g., Claude Code can only POST to `api.anthropic.com/v1/messages`). SSRF protection validates full IPv4/IPv6 CIDR ranges. Sandbox images are pinned by SHA256 digest. No agent loop — that lives in OpenClaw.

**Key Trade-off**: Enterprise-grade kernel isolation at the cost of requiring OpenClaw + NVIDIA OpenShell as prerequisites. Not standalone.

**When to Choose**: You run OpenClaw in a regulated or security-sensitive environment and need Landlock/seccomp isolation, fine-grained network egress control, and managed NVIDIA inference. Alpha status — not production-ready per their own docs.

`TypeScript` · `Apache-2.0` · [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) · ![Stars](https://img.shields.io/github/stars/NVIDIA/NemoClaw?style=flat-square)

---

### Lightweight

#### NanoClaw

> **Concept**: Container-sandboxed assistant with a small core. No config files — you fork the source and modify it directly via Claude Code.

**Architecture**: ~20 core TypeScript source files in `src/` (70+ files total including tests and skills). Each chat session gets its own Docker container (or Apple Container on macOS for near-instant startup). Credential handling via OneCLI Agent Vault keeps API keys outside containers. State is filesystem-based IPC (JSON files in `data/ipc/{group}/`). Primarily Claude-based via Agent SDK, but also supports local models via Ollama with an API proxy.

**Key Trade-off**: Simplicity and security at the cost of upgradeability. Each fork diverges intentionally — "bespoke, not bloatware."

**When to Choose**: You want a small, auditable codebase with strong container isolation, and you're comfortable modifying source code instead of writing config files.

`TypeScript` · `MIT` · [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) · ![Stars](https://img.shields.io/github/stars/qwibitai/nanoclaw?style=flat-square)

---

#### nanobot

> **Concept**: 99% of OpenClaw's functionality in ~4,000 lines of Python. Academic-backed (HKU Data Intelligence Lab).

**Architecture**: `nanobot/` is a Python package with 18+ subdirectories (agent, channels, providers, skills, security, etc. — 97+ Python files total). The project claims "~4K core LOC" but this counts only the agent loop subset (verified via `core_agent_lines.sh`, which explicitly excludes commands, providers, security, and templates). End-to-end streaming with Anthropic prompt caching. "Dream" two-stage memory separates live conversation from consolidated long-term knowledge.

**Key Trade-off**: Small core agent loop at the cost of a larger surrounding codebase. The "4K LOC" claim refers to the auditable core, not the full project.

**When to Choose**: You want a Python-native agent that's small enough to read in an afternoon, with strong multi-channel support (12+ including Chinese platforms) and academic rigor.

`Python` · `MIT` · [HKUDS/nanobot](https://github.com/HKUDS/nanobot) · ![Stars](https://img.shields.io/github/stars/HKUDS/nanobot?style=flat-square)

---

#### BabyClaw

> **Concept**: A single JavaScript file on Claude Agent SDK. The agent's personality evolves — a cron job analyzes communication patterns every 3 days and rewrites the agent's identity.

**Architecture**: Everything in `index.js`. Three-layer persistence: `state.json` (current state), dated markdown files (history), rolling 50-entry `recent.md`. Four built-in crons handle personality evolution, pattern detection, skill suggestion, and daily digests.

**Key Trade-off**: Maximum simplicity at the cost of everything else. Single channel (Telegram), single provider (Claude), no database.

**When to Choose**: You want the absolute simplest possible agent with an interesting personality evolution mechanic.

`JavaScript` · `MIT` · [yogesharc/babyclaw](https://github.com/yogesharc/babyclaw) · ![Stars](https://img.shields.io/github/stars/yogesharc/babyclaw?style=flat-square)

---

### Rust Native

#### ZeroClaw

> **Concept**: Seven Rust traits define the entire system. Swap any component via config. Deploys from ESP32 firmware to cloud.

**Architecture**: Core systems are defined as Rust traits (providers, channels, tools, memory, tunnels, peripherals). Everything is compile-time polymorphism — zero runtime overhead. Config-driven component swapping means you choose which implementations to use via TOML, not code changes. Secrets are encrypted at rest. 129+ security tests in CI.

**Key Trade-off**: Rust's compile-time guarantees and zero overhead at the cost of contributor accessibility. You need to know Rust to extend it.

**When to Choose**: You want the widest deployment range (ESP32 to cloud) with the smallest footprint (<5MB RAM, <10ms startup, 8.8MB binary) and don't mind Rust.

`Rust` · `MIT/Apache-2.0` · [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) · ![Stars](https://img.shields.io/github/stars/zeroclaw-labs/zeroclaw?style=flat-square)

---

#### IronClaw

> **Concept**: Privacy-first. Credentials never enter guest WASM memory. Every request and response is scanned for leaks.

**Architecture**: WASM sandbox pipeline: WASM → Allowlist → Leak Scan → Credential → Execute → Leak Scan → WASM. A dedicated safety layer handles prompt injection defense. The trait system extends ZeroClaw's model with additional capabilities (database, embedding, network policy). WASM capabilities control resource access.

**Key Trade-off**: Maximum security at the cost of performance overhead from WASM sandboxing and double leak scanning.

**When to Choose**: You handle sensitive data and need WASM-level isolation with credential boundary enforcement. Backed by NEAR AI.

`Rust` · `MIT/Apache-2.0` · [nearai/ironclaw](https://github.com/nearai/ironclaw) · ![Stars](https://img.shields.io/github/stars/nearai/ironclaw?style=flat-square)

---

#### OpenFang

> **Concept**: An "Agent OS" with 7 bundled autonomous "Hands" that run 24/7 without human prompting.

**Architecture**: 14 Rust crates: kernel, runtime, api, channels, memory, types, skills, hands, extensions, wire, cli, desktop, migrate, xtask. The 7 bundled Hands (Clip, Lead, Collector, Predictor, Researcher, Twitter, Browser) are always-on autonomous agents — they don't wait for user messages. Custom OFP P2P protocol with HMAC-SHA256 mutual authentication. WASM dual-metered sandbox with Merkle hash-chain auditing and taint tracking.

**Key Trade-off**: Large scope in the Rust ecosystem (project claims 137K LOC, 40 channel adapters, 26-27 providers — upstream sources vary) at the cost of complexity approaching OpenClaw.

**When to Choose**: You want autonomous agents that work proactively (not just reactively) with serious security (16 discrete security systems) and a Tauri desktop app.

`Rust` · `MIT/Apache-2.0` · [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) · ![Stars](https://img.shields.io/github/stars/RightNow-AI/openfang?style=flat-square)

---

#### Moltis

> **Concept**: ~46 modular crates (per project README). Designed for auditability — the agent loop fits in ~5,000 LOC.

**Architecture**: Gateway pattern: User → Moltis → LLM providers via Axum HTTP/WS. Hybrid memory combines SQLite FTS with vector embeddings for cross-session recall. XChaCha20-Poly1305 encryption with Argon2id key derivation. voice support (multiple TTS and STT providers). Session branching from checkpoints. Signed releases via Sigstore keyless signing. Note: the project sets `#[deny(unsafe_code)]` at workspace level but uses `#[allow(unsafe_code)]` in specific crates for FFI/WASM interop — a common Rust pattern, but worth noting if "zero unsafe" is a deciding factor for you.

**Key Trade-off**: Security and auditability at the cost of a large binary (44MB per the project's own README — includes web UI + voice engine).

**When to Choose**: You want Rust's safety guarantees with voice support and a compact, reviewable agent loop.

`Rust` · `MIT` · [moltis-org/moltis](https://github.com/moltis-org/moltis) · ![Stars](https://img.shields.io/github/stars/moltis-org/moltis?style=flat-square)

---

#### ZeptoClaw

> **Concept**: 9-layer security all active by default, zero configuration needed. ~6MB binary, ~6MB RAM per workspace.

**Architecture**: MessageBus routes from Channels → Agent Loop → Provider Stack. 9 security layers all active by default: (1) Sandbox (6 runtime options), (2) Prompt Injection Detection, (3) Secret Leak Scanner, (4) Policy Engine, (5) Input Validator, (6) Shell Blocklist, (7) SSRF Prevention, (8) Chain Alerting (detects dangerous sequences like write→execute), (9) Tool Approval Gate.

**Key Trade-off**: Security-by-default (9 layers, not 7 as some sources claim) at the cost of flexibility. Multi-tenant capable (hundreds of workspaces at ~6MB each) but opinionated about what's allowed.

**When to Choose**: You're hosting agents for multiple users and need strong default security without per-tenant configuration.

`Rust` · `Apache-2.0` · [qhkm/zeptoclaw](https://github.com/qhkm/zeptoclaw) · ![Stars](https://img.shields.io/github/stars/qhkm/zeptoclaw?style=flat-square)

---

#### OpenCrabs

> **Concept**: Self-modifying agent. Edits its own source code, rebuilds, and hot-restarts via `exec()`.

**Architecture**: Brain system with live-editable files (SOUL, IDENTITY, USER, AGENTS, TOOLS, MEMORY) that can be modified between turns. `/rebuild` clones source to `~/.opencrabs/source/`, builds, and `exec()` replaces the running process. Local embeddings via embeddinggemma-300M (768-dim, no external API). `zeroize` crate clears API keys from RAM. A2A Protocol (Agent-to-Agent) via JSON-RPC 2.0.

**Key Trade-off**: True self-modification at the cost of stability. An agent that rewrites itself can break itself.

**When to Choose**: You want an agent that learns by modifying its own code and tools, with a tmux-style TUI for parallel sessions.

`Rust` · `MIT` · [adolfousier/opencrabs](https://github.com/adolfousier/opencrabs) · ![Stars](https://img.shields.io/github/stars/adolfousier/opencrabs?style=flat-square)

---

#### MicroClaw

> **Concept**: Rust agent with 16 channel adapters (per source audit: Telegram, Discord, Slack, Feishu/Lark, IRC, Web, Matrix, DingTalk, Email, iMessage, Nostr, QQ, Signal, WeChat, WhatsApp, ACP).

**Architecture**: Unified agent loop rewritten in Rust. Built-in document processing (PDF, DOCX, XLSX, PPTX). ACP (Agent Client Protocol) for stdio server mode. MCP support included. `microclaw doctor` for diagnostics and `microclaw upgrade` for self-update.

**Key Trade-off**: Channel breadth at the cost of maturity. Supports Telegram, Discord, Slack, Feishu/Lark, IRC, Web, Matrix, and more — but the project is pre-v1.0 (v0.1.x).

**When to Choose**: You need a Rust agent with Feishu/Lark and Chinese platform support alongside Western channels, and don't mind early-stage software.

`Rust` · `MIT` · [microclaw/microclaw](https://github.com/microclaw/microclaw) · ![Stars](https://img.shields.io/github/stars/microclaw/microclaw?style=flat-square)

---

### Embedded / Edge

#### NullClaw

> **Concept**: 678KB binary. 50+ providers, 19 channels, 35+ tools — all under 1MB of RAM. Boots in <2ms.

**Architecture**: Zig with manual vtable interfaces (function pointer tables — no compiler-generated trait object overhead). `comptime` metaprogramming avoids proc macro / codegen bloat. SQLite hybrid: vector BLOBs + FTS5 + BM25. Cross-compiles to ARM, x86, RISC-V from a single `build.zig`. Tiered sandbox auto-detection: Landlock → Firejail → Bubblewrap → Docker.

**Key Trade-off**: Extreme minimalism at the cost of ecosystem maturity. Zig has a smaller community than Rust or Go.

**When to Choose**: You want an extremely small agent binary that can run from Raspberry Pi GPIO control to VPS deployment.

`Zig` · `MIT` · [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) · ![Stars](https://img.shields.io/github/stars/nullclaw/nullclaw?style=flat-square)

---

#### PicoClaw

> **Concept**: Go single binary that runs on $10 hardware. Cross-compiles to RISC-V, ARM, MIPS, x86.

**Architecture**: `cmd/` + `pkg/` + `config/` + `web/` structure. Provider abstraction across 30+ LLM backends. Native MCP integration. Reference target: LicheeRV-Nano ($9.90, 0.8GHz single-core). 95% of core code was AI-generated (inspired by nanobot's architecture, but rebuilt from scratch in Go).

**Key Trade-off**: Hardware accessibility at the cost of feature depth. Go's simplicity enables $10 deployment but limits advanced patterns available in Rust.

**When to Choose**: You want an agent on cheap hardware (old Android phones via Termux, RISC-V boards, RPi) and Go is your language.

`Go` · `MIT` · [sipeed/picoclaw](https://github.com/sipeed/picoclaw) · ![Stars](https://img.shields.io/github/stars/sipeed/picoclaw?style=flat-square)

---

#### MimiClaw

> **Concept**: C on ESP32-S3 with FreeRTOS. No Linux, no Node.js, no shell. Runs on USB power.

**Architecture**: Dual-core: Core 0 handles I/O (WiFi, Telegram, WebSocket, serial), Core 1 runs the agent loop exclusively (pinned via `xTaskCreatePinnedToCore`). 16MB flash, 8MB PSRAM. ReAct agent loop with up to 10 iterations per turn (4 parallel tool calls per LLM response).

**Key Trade-off**: Lowest possible power and cost ($5-10 board, ~0.5W) at the cost of limited compute and channels.

**When to Choose**: You want a physical, always-on AI device that sits on your desk and runs on USB power — not a software agent on a computer.

`C` · `MIT` · [memovai/mimiclaw](https://github.com/memovai/mimiclaw) · ![Stars](https://img.shields.io/github/stars/memovai/mimiclaw?style=flat-square)

---

### Unique Paradigm

#### Hermes Agent

> **Concept**: The only agent with a closed learning loop. Complex tasks automatically become reusable skills that improve during subsequent use.

**Architecture**: Synchronous `AIAgent` class runs: build prompt → call LLM → dispatch tools → append results → loop (max 90 iterations). The learning loop: complex tasks trigger auto skill creation → skills stored as agentskills.io documents → skills self-modify on subsequent use → Honcho dialectic user modeling builds understanding of the user across sessions. 6 terminal backends: local, Docker, SSH, Modal (serverless), Daytona (cloud workspace), Singularity (HPC). MCP first-class with OAuth and sampling support.

**Key Trade-off**: Learning and flexibility at the cost of polish. No native apps, no GUI — CLI/TUI + messaging platforms only. Multiple LLM providers (Anthropic, OpenAI, Google, xAI, DeepSeek, Kimi, MiniMax, plus OpenRouter for 200+ models) with live `/model` swap (no restart).

**When to Choose**: You want an agent that gets better over time, runs anywhere (laptop to $5 VPS to HPC cluster), and you value model freedom over GUI polish. Also: if you're training your own models (Atropos RL pipeline).

`Python` · `MIT` · [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) · ![Stars](https://img.shields.io/github/stars/NousResearch/hermes-agent?style=flat-square)

---

#### HermitClaw

> **Concept**: Not a tool — an autonomous digital creature. It picks its own research topics, writes reports, and develops emergent beliefs over days and weeks.

**Architecture**: Continuous 5-second loop: context → LLM → tool → store → reflect. SHA-512 personality genome from keyboard entropy deterministically selects 3 curiosity domains (50 options), 2 thinking styles (16 options), 1 temperament (8 options). Memory inspired by Park et al. 2023 Generative Agents paper: recency (exponential decay) + importance (LLM-rated 1-10) + relevance (cosine similarity). Hierarchical reflection: depth-0 (thoughts) → depth-1 (patterns) → depth-2+ (beliefs).

**Key Trade-off**: Philosophical novelty at the cost of practical utility. This is closer to art than engineering.

**When to Choose**: You want to explore what an autonomous AI creature looks like, not build a productivity tool. "A tamagotchi that does research."

`Python` · `No LICENSE file` · [brendanhogan/hermitclaw](https://github.com/brendanhogan/hermitclaw) · ![Stars](https://img.shields.io/github/stars/brendanhogan/hermitclaw?style=flat-square)

---

#### SupaClaw

> **Concept**: Zero daemon. PostgreSQL IS the application — message broker, state store, scheduler, audit log. Edge Functions for compute.

**Architecture**: Supabase Edge Functions (Deno) for stateless compute. pg_cron for durable scheduling (not a custom scheduler — SQL guarantees). Row Level Security prevents credential exposure to agents. Vercel AI SDK for multi-provider support. Database backup equals complete system snapshot. All execution state is queryable SQL.

**Key Trade-off**: Zero infrastructure management at the cost of Supabase lock-in and limited compute (Edge Function constraints).

**When to Choose**: You already use Supabase and want an agent with zero server management. `SELECT * FROM jobs WHERE status = 'failed'` is your debugging tool.

`TypeScript` · `MIT` · [vincenzodomina/supaclaw](https://github.com/vincenzodomina/supaclaw) · ![Stars](https://img.shields.io/github/stars/vincenzodomina/supaclaw?style=flat-square)

---

#### TinyClaw (TinyAGI)

> **Concept**: Process-per-channel isolation. Each messaging channel (Discord, Telegram, WhatsApp) runs as a forked child process. SQLite WAL is the message broker — no Redis, no RabbitMQ.

**Architecture**: Dual-runtime: TypeScript (queue management), Node.js `fork()` (channel processes). Agents communicate via shared SQLite queue with WAL mode for atomic transactions. Chain execution (Agent A output → Agent B input) and fan-out parallelism. Dead-letter queue with 5 retries.

**Key Trade-off**: Strong channel isolation at the cost of overhead (spawning a forked process per channel).

**When to Choose**: You want a multi-agent team orchestrator for a "one person company" with SQLite-based durable queuing.

`TypeScript` · `MIT` · [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) · ![Stars](https://img.shields.io/github/stars/TinyAGI/tinyagi?style=flat-square)

---

### Python Ecosystem

#### AstrBot

> **Concept**: 14+ IM platforms, large plugin marketplace, desktop app. Pre-dates the Claw ecosystem (originally QQChannelChatGPT, created Dec 2022) — the most mature codebase listed here.

**Architecture**: Event bus + message pipeline (3 major refactors since 2022). Plugin marketplace (project claims 1,000+ community plugins). Automatic context compression. Desktop edition (AstrBot-desktop) for Linux/macOS. Monaco Editor in WebUI.

**Key Trade-off**: Maximum platform coverage and plugin ecosystem at the cost of AGPL-3.0 licensing (most restrictive in the ecosystem — commercial use requires open-sourcing).

**When to Choose**: You need broad IM platform coverage (especially Chinese platforms: QQ, WeChat Work, Feishu, DingTalk) with a mature plugin ecosystem. Note: some listed platforms like WhatsApp are marked "Coming Soon." Be aware of the AGPL license.

`Python` · `AGPL-3.0` · [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) · ![Stars](https://img.shields.io/github/stars/AstrBotDevs/AstrBot?style=flat-square)

---

#### TrinityClaw

> **Concept**: "Nervous system" architecture with dynamic skill generation — the agent writes its own new tools, validated by AST parsing.

**Architecture**: Central `app.py` coordinates 29 read-only core skills and a dynamic skills directory where the agent generates new tools at runtime with AST validation. Can attach to existing Chrome sessions via CDP — accesses your logged-in accounts directly (no API keys needed). Deep Google ecosystem integration (Calendar, Gmail, Drive, Maps). ChromaDB vector storage + JSONL logs.

**Key Trade-off**: Maximum capability (the agent creates its own tools + uses your browser sessions) at the cost of significant security surface. The README warns: local use only.

**When to Choose**: You want a local-only agent that deeply integrates with Google services and can automate your existing browser sessions.

`Python` · `MIT` · [TrinityClaw/trinity-claw](https://github.com/TrinityClaw/trinity-claw) · ![Stars](https://img.shields.io/github/stars/TrinityClaw/trinity-claw?style=flat-square)

---

### Mobile

#### ClawDroid

> **Concept**: Native Android APK with an embedded Go backend. The entire agent runs on-device — no server needed.

**Architecture**: Kotlin/Jetpack Compose frontend + Go backend compiled as a native library inside the APK. Local WebSocket at `ws://127.0.0.1:18793`. 40+ tools organized by category (alarm, calendar, contacts, communication, media, navigation, device control, settings, web). Accessibility service for device automation.

**Key Trade-off**: True on-device execution at the cost of limited compute. Your phone's CPU is running the agent loop.

**When to Choose**: You want an AI assistant as a native Android app that works without any server, and can be set as your default digital assistant.

`Go/Kotlin` · `MIT` · [KarakuriAgent/clawdroid](https://github.com/KarakuriAgent/clawdroid) · ![Stars](https://img.shields.io/github/stars/KarakuriAgent/clawdroid?style=flat-square)

---

#### DroidClaw

> **Concept**: Turn old phones into AI agents. Give it a goal; it reads the screen via ADB accessibility tree, thinks, taps.

**Architecture**: Perception-reasoning-action loop. Parses ADB accessibility tree (falls back to screenshot vision for WebViews/Flutter/games). Three execution modes: Interactive (LLM reasoning per step), Workflows (JSON templates, AI-powered), Flows (YAML, deterministic, no LLM). Stuck loop detection + drift detection for resilience.

**Key Trade-off**: Works with any app without API integration at the cost of speed and reliability. Screen-reading is inherently fragile.

**When to Choose**: You want to automate Android apps that have no API (messaging, social media, legacy apps) using a $30 old phone.

`TypeScript` · `No LICENSE file` · [unitedbyai/droidclaw](https://github.com/unitedbyai/droidclaw) · ![Stars](https://img.shields.io/github/stars/unitedbyai/droidclaw?style=flat-square)

---

### Other Languages

#### Autobot

> **Concept**: Crystal language — Ruby syntax, C performance. 2MB binary, 5MB RAM, <20ms startup. Kernel-enforced sandboxing.

**Architecture**: 98.9% Crystal. Kernel-enforced sandboxing via Docker/bubblewrap mount namespaces (not application-level path checks). Cron jobs fire by publishing `InboundMessage` to the event bus with `channel: "system"` — a cron job is literally just a message, triggering a full agent turn. JSONL session management with memory consolidation at 50-message threshold.

**Key Trade-off**: Best resource efficiency in the ecosystem at the cost of Crystal's small community. Finding contributors is hard.

**When to Choose**: You want to run dozens of isolated bot instances on a single machine, and you appreciate Ruby-like syntax with C-like performance.

`Crystal` · `MIT` · [crystal-autobot/autobot](https://github.com/crystal-autobot/autobot) · ![Stars](https://img.shields.io/github/stars/crystal-autobot/autobot?style=flat-square)

---

#### FastClaw

> **Concept**: Go single binary with zero dependencies. Built-in Telegram/Discord/Slack, embedded web dashboard, concurrent tool execution via goroutines.

**Architecture**: Full ReAct agent loop in `internal/agent/loop.go` (~836 lines). Gateway orchestrates multi-agent teams with pub/sub message bus. 13 built-in tools (exec, file I/O, web fetch/search, memory search, cron, subagent spawn). Plugin system via JSON-RPC 2.0 subprocesses. MCP support (stdio + HTTP). 2 native LLM providers: OpenAI-compatible (covers OpenAI, DeepSeek, Gemini, Groq, Ollama, OpenRouter) + Anthropic Messages API. Dual-layer memory: MEMORY.md (LLM-updated persistent facts) + FTS5 searchable conversation logs. Skills learner auto-extracts patterns after N tool calls. Loop detection via SHA256 hash of consecutive arguments.

**Key Trade-off**: Go simplicity and zero-dependency deployment at the cost of a smaller community and permissive-by-default security (opt-in Docker sandbox, no kernel-level isolation). OpenClaw plugin bridge available.

**When to Choose**: You want a single-binary agent that deploys anywhere without Node.js/Python, with built-in channels, web dashboard, and Go's concurrency model for parallel tool execution.

`Go` · `MIT` · [fastclaw-ai/fastclaw](https://github.com/fastclaw-ai/fastclaw) · ![Stars](https://img.shields.io/github/stars/fastclaw-ai/fastclaw?style=flat-square)

---

## Cross-Cutting Comparisons

### Security Models

| Approach | Frameworks | How It Works |
|---|---|---|
| **WASM Sandbox** | IronClaw, OpenFang | Tools run in sandboxed WASM — credentials injected at host/guest boundary |
| **Kernel Sandbox (Landlock+seccomp)** | NemoClaw (for OpenClaw) | Landlock LSM + seccomp + network namespaces via NVIDIA OpenShell. Per-binary network policies |
| **Container Isolation** | NanoClaw, Moltis | Per-session Docker/Apple Container. NanoClaw's OneCLI Agent Vault keeps keys outside containers |
| **Multi-layer (default-on)** | ZeptoClaw, NullClaw | ZeptoClaw: 6 sandbox options + 9 security layers. NullClaw: tiered auto-detection (Landlock → Firejail → Bubblewrap → Docker) |
| **Kernel Enforcement** | Autobot | Mount namespaces via bubblewrap (OS-level, not application-level) |
| **Command Approval** | OpenClaw, Hermes, OpenCrabs | Allowlists and user approval gates. Hermes adds SSRF protection + OSV malware scanning |
| **Process Isolation** | TinyClaw | Each messaging channel runs as a forked child process |
| **Hardware Isolation** | MimiClaw | FreeRTOS on dedicated microcontroller — no shared OS |

### Channel Coverage

| Tier | Count | Frameworks |
|---|---|---|
| **40+** | OpenFang |
| **22+** | OpenClaw |
| **14-29** | AstrBot, MicroClaw, NullClaw, Hermes Agent, PicoClaw, ZeroClaw (29 per source audit) |
| **5-13** | nanobot, ZeptoClaw, Moltis, OpenCrabs, NanoClaw, ClawDroid, DroidClaw, FastClaw |
| **1-4** | SupaClaw, Autobot, TinyClaw, BabyClaw, MimiClaw (Telegram + WebSocket) |

### LLM Provider Strategy

| Strategy | Frameworks | How |
|---|---|---|
| **Provider-agnostic (20+)** | Hermes Agent | Native SDKs for 20+ providers, live `/model` swap, no restart |
| **Native multi-provider** | ZeroClaw (17+ real impls), NullClaw (40-50 distinct services), PicoClaw (30+) | Direct provider integrations with config-driven selection |
| **Mixed native + compatible** | ZeptoClaw (repo claims vary: 9-16), OpenFang (26-27), AstrBot (10+) | Core providers native, rest via OpenAI-compatible API |
| **Multi-provider with fallback** | OpenCrabs | Priority order: Anthropic → OpenAI → GitHub → Gemini → OpenRouter → others |
| **Claude-primary + compatible** | NanoClaw | Claude Agent SDK primary, but supports Ollama, Together AI, Fireworks, and any Anthropic-compatible endpoint |
| **LiteLLM abstraction** | TrinityClaw | Python LiteLLM for multi-provider routing |
| **Vercel AI SDK** | SupaClaw | TypeScript multi-provider via Vercel |

### Memory & Learning

| Approach | Frameworks | Description |
|---|---|---|
| **Closed learning loop** | Hermes Agent | Auto skill creation → skill self-improvement → user modeling |
| **Self-modification** | OpenCrabs | Agent edits own source, rebuilds, hot-restarts |
| **Dynamic skill generation** | TrinityClaw | Agent writes new tools, validated by AST |
| **Personality evolution** | BabyClaw, HermitClaw | Cron rewrites identity; hierarchical reflection |
| **Dream/consolidation** | OpenClaw, nanobot | Grounded REM backfill; 2-stage Dream memory |
| **Vector + FTS hybrid** | NullClaw, Moltis, OpenCrabs | SQLite FTS5 + vector embeddings |
| **Static skills** | All others | Skills created by humans, executed by agent |

### Deployment Targets

| Target | Frameworks |
|---|---|
| **Bare metal ($5-10)** | MimiClaw (ESP32-S3 ~$5), PicoClaw ($10), NullClaw |
| **$10 hardware** | PicoClaw (LicheeRV-Nano), ZeroClaw (ESP32) |
| **Android device** | ClawDroid, DroidClaw, PicoClaw (Termux) |
| **$5 VPS** | Hermes (Modal hibernation), NullClaw, Autobot |
| **Docker** | Most (OpenClaw, NanoClaw, Moltis, ZeptoClaw...) |
| **Serverless / Cloud workspace** | Hermes (Modal serverless, Daytona workspace), SupaClaw (Supabase Edge) |
| **Enterprise sandbox** | NemoClaw (wraps OpenClaw in NVIDIA OpenShell) |
| **HPC cluster** | Hermes (Singularity) |
| **Desktop native** | OpenClaw (macOS/iOS/Android), OpenFang (Tauri) |
| **Serverless (Supabase)** | SupaClaw (Edge Functions + pg_cron, dashboard for management) |

---

## By Popularity

Sorted by GitHub stars (live badges above, snapshot below for reference).

| # | Project | Lang | Category | Stars (Apr 2026) |
|---|---------|------|----------|-------------------|
| 1 | [OpenClaw](https://github.com/openclaw/openclaw) | TypeScript | Full Platform | ~354K |
| 2 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Python | Self-improving | ~52K |
| 3 | [nanobot](https://github.com/HKUDS/nanobot) | Python | Lightweight | ~39K |
| 4 | [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | Rust | Rust Native | ~30K |
| 5 | [AstrBot](https://github.com/AstrBotDevs/AstrBot) | Python | IM Chatbot | ~30K |
| 6 | [PicoClaw](https://github.com/sipeed/picoclaw) | Go | Embedded | ~28K |
| 7 | [NanoClaw](https://github.com/qwibitai/nanoclaw) | TypeScript | Lightweight | ~27K |
| 8 | [NemoClaw](https://github.com/NVIDIA/NemoClaw) | TypeScript | Security harness | ~19K |
| 9 | [OpenFang](https://github.com/RightNow-AI/openfang) | Rust | Agent OS | ~17K |
| 9 | [IronClaw](https://github.com/nearai/ironclaw) | Rust | Privacy-first | ~12K |
| 10 | [NullClaw](https://github.com/nullclaw/nullclaw) | Zig | Embedded | ~7K |
| 11 | [MimiClaw](https://github.com/memovai/mimiclaw) | C | Bare-metal | ~5K |
| 12 | [TinyAGI](https://github.com/TinyAGI/tinyagi) | TypeScript | Multi-agent | ~4K |
| 13 | [Moltis](https://github.com/moltis-org/moltis) | Rust | Auditable | ~3K |
| 14 | [DroidClaw](https://github.com/unitedbyai/droidclaw) | TypeScript | Mobile | ~1K |
| 15 | [MicroClaw](https://github.com/microclaw/microclaw) | Rust | Multi-channel | ~641 |
| 16 | [OpenCrabs](https://github.com/adolfousier/opencrabs) | Rust | Self-modifying | ~626 |
| 17 | [ZeptoClaw](https://github.com/qhkm/zeptoclaw) | Rust | Security-first | ~587 |
| 18 | [FastClaw](https://github.com/fastclaw-ai/fastclaw) | Go | Zero-dependency | ~539 |
| 18 | [HermitClaw](https://github.com/brendanhogan/hermitclaw) | Python | Autonomous creature | ~319 |
| 19 | [Autobot](https://github.com/crystal-autobot/autobot) | Crystal | Efficient | ~70 |
| 20 | [SupaClaw](https://github.com/vincenzodomina/supaclaw) | TypeScript | Serverless | ~58 |
| 21 | [BabyClaw](https://github.com/yogesharc/babyclaw) | JavaScript | Minimal | ~15 |
| 22 | [ClawDroid](https://github.com/KarakuriAgent/clawdroid) | Go/Kotlin | Android | ~10 |
| 23 | [TrinityClaw](https://github.com/TrinityClaw/trinity-claw) | Python | Dynamic skills | ~5 |

---

## Decision Framework

### "I want the most popular, most complete agent"
→ **OpenClaw** — native apps, largest community and plugin ecosystem

### "I want it to learn and improve itself"
→ **Hermes Agent** — closed learning loop, 20+ providers, serverless deployment

### "I want maximum security"
→ **IronClaw** (WASM sandbox) or **ZeptoClaw** (9-layer default security)

### "I want the smallest possible binary"
→ **NullClaw** (678KB Zig) or **Autobot** (2MB Crystal)

### "I want to run it on cheap hardware ($5-10)"
→ **MimiClaw** (ESP32-S3, ~$5) or **PicoClaw** ($10 Go binary)

### "I want to understand every line of code"
→ **nanobot** (small Python core) or **NanoClaw** (small TypeScript core)

### "I want autonomous agents that work 24/7"
→ **OpenFang** (7 bundled Hands) or **HermitClaw** (autonomous creature)

### "I want zero infrastructure"
→ **SupaClaw** (Supabase-native) or **BabyClaw** (single file)

### "I want it on my Android phone"
→ **ClawDroid** (native APK) or **DroidClaw** (ADB automation)

### "I need Chinese platform support"
→ **AstrBot** (QQ, WeChat Work, DingTalk, Feishu) or **MicroClaw** (16 adapters including Chinese platforms)

---

## Contributing

This is an opinionated architecture guide, not an exhaustive list. To suggest an addition:

1. The framework must be open-source
2. It must have a meaningfully different architecture from existing entries
3. Open an issue with: concept (1 sentence), architecture (how the agent loop works), key trade-off

PRs that add "yet another link" without architectural analysis will be closed.

---

*Last updated: April 11, 2026*
