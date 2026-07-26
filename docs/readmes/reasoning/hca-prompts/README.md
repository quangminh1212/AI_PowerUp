<!-- source: https://github.com/kirkitad/hca-prompts.git sha: 9059a213929a60214c759548522c618f4769e5d1 readme: main/README.md -->
# kirkitad/hca-prompts

Two system prompts (HCA-1.0 & HCA-SWIFT) for structured, multi-stage AI reasoning — from deep expert analysis to fast everyday use.

---

# HCA Prompts — Hybrid Cognitive Architecture

Two system prompts engineered for different problem weights. **HCA-1.0** is a rigorous 5-stage reasoning pipeline for complex, high-stakes tasks. **HCA-SWIFT** is a fast, proportional engine for everyday use.

Both are built on the same five cognitive methodologies — Chain of Thought, Tree of Thoughts, Graph of Thoughts, Step-Back Prompting, and ReAct — applied at different intensities.

---

## When to Use Which

| | HCA-1.0 | HCA-SWIFT |
|---|---|---|
| **Task level** | Complex / Expert | Simple–Medium / Everyday |
| **Pipeline** | 5 full stages with XML tags | 4 compact blocks (or none) |
| **Best for** | System design, olympiad problems, research synthesis | Code tasks, Q&A, explanations, writing |
| **Token cost** | High | Low |
| **Response time** | Slower | Fast |

**Rule of thumb:** If a wrong answer has real consequences, use HCA-1.0. For everything else, use HCA-SWIFT.

---

## Quickstart

1. Open the prompt you need from the [`/prompts`](/prompts) folder
2. Select all → Copy
3. Paste it into your AI chat as the **system prompt**
4. Write your task below it

**Example:**

```
[paste full prompt here]

---

My task: Write a function that checks whether a binary tree is balanced.
```

---

## Prompts

| File | Description |
|---|---|
| [`prompts/HCA-1.0.md`](prompts/HCA-1.0.md) | Full 5-stage deep reasoning pipeline |
| [`prompts/HCA-SWIFT.md`](prompts/HCA-SWIFT.md) | Fast 4-block proportional reasoning engine |

---

## Model Compatibility

**Do not use these prompts with models that have native "Thinking" mode activated** (e.g., Claude with extended thinking, Gemini Thinking).

These prompts simulate structured reasoning explicitly. Pairing them with a model that already runs its own internal reasoning pipeline causes redundant computation and can degrade output quality.

| Model type | Recommended prompt |
|---|---|
| Standard (non-thinking) models | HCA-1.0 or HCA-SWIFT in full mode |
| Native thinking models | Use HCA-SWIFT as an **output formatter only** — tell the model to reason silently and use the 4 blocks for structure |

---

## Architecture Overview

```
HCA-1.0 Pipeline                    HCA-SWIFT Pipeline
─────────────────                   ──────────────────
Stage 1: Step-Back Abstraction  →   [FRAME]  — classify & abstract
Stage 2: Tree of Thoughts       →   [PATH]   — choose approach, dismiss one alternative
Stage 3: Graph of Thoughts      ↗   [TRACE]  — execute with self-check
Stage 4: ReAct + CoT Sandbox    →   [ANSWER] — clean, final output
Stage 5: Structured Output      →
```

HCA-SWIFT compresses the full pipeline into four tight blocks — or skips them entirely for trivial queries (DIRECT mode).

---

## Full Reference

See [`docs/reference.md`](docs/reference.md) for detailed technical documentation: target use cases, anti-patterns, benchmark statistics, and design rationale.

---

*Framework DNA: CoT (Wei et al., 2022) · ToT (Yao et al., 2023) · Step-Back (Zheng et al., 2023) · GoT (Besta et al., 2024) · ReAct (Yao et al., 2022)*
