<!-- source: https://github.com/Zisky-ai/Luper.git sha: ad498cf20a520afcce84c639da2e209367b6ebea readme: main/README.md -->
# Zisky-ai/Luper

Text-defined workflow harness for autonomous AI delivery via local CLIs

---

<img width="1000" height="333" alt="Luper" src="docs/assets/luper_hero.png" />

# Luper

**A thin harness around a text-defined workflow — agents drive your local `claude` and `codex` CLIs to deliver a verified result from an approved contract.**

▶ **[Watch the demo on YouTube](https://www.youtube.com/watch?v=PSIwy57rCuY)**

You don't chat with Luper. You hand it a brief, approve the contract it writes back, walk away, and it produces the artifact your contract asked for — with every LLM call, every verdict, and every routing decision on disk so you can audit the trail months later.

Luper is a small Python harness — about 8,000 lines you can read in an afternoon. The orchestrator is a `while` loop with explicit phases. The workflow itself (phase sequence, agent prompts, JSON schemas) is plain text you can edit without touching code. The cockpit is FastAPI + HTMX, no SPA, no JS framework. The whole project exists because the same job built on LangGraph + Postgres + a React frontend would be 50,000 lines that nobody can audit, debug, or fork in a weekend.


---

## Why Luper exists

The market has two answers for "I need an autonomous agent to deliver a structured deliverable."

**Hosted SaaS** (Devin, Cognition, the long tail of GPT wrappers) — you upload your data, you don't see the prompts, you can't change the routing, you pay per call, and the audit trail is whatever the vendor decided to expose. Fine if your work isn't sensitive and you don't care how the sausage is made. Not fine for analytical and managerial work where you need to defend the output to a board, a client, or yourself in six months.

**Frameworks** (LangGraph, AutoGPT, CrewAI, the rest) — you get a graph DSL, a state-machine engine, a plugin system, a hooks API, a stream API, and a thousand abstractions for problems you don't have. The autonomy is real, but so is the surface area; debugging a stuck run means reading framework internals you didn't write.

Luper is the third answer. It is **a single file you can read end-to-end** (`luper/orchestrator.py`) sitting on top of CLIs you already have installed (`claude`, `codex`) under subscriptions you already pay for (Claude Max, ChatGPT Plus / Pro). No new accounts. No metered API spending (except optional Deep Research). No state-machine framework — the loop is a `while` loop with five branches. The workflow is **text**: `workflow/workflow.md` (phase sequence), `workflow/prompts/*.md` (agent system prompts), `workflow/schemas/*.json` (output structure). Edit a prompt, the next run uses it. No code change needed.


---

## What it does in 30 seconds

```bash
# 1. Write a brief — a markdown file describing what you want
cat > my_brief.md <<'EOF'
# Brief: 5-page market overview of MCP for a non-technical audience

Goal: explain Model Context Protocol to a CEO who knows AI exists but
nothing about agent infrastructure. 1500–2500 words, plain language,
no jargon walls.

Deliverables:
  - artifacts/mcp_overview.md — the explainer document.

Acceptance criteria:
  - Word count between 1500 and 2500.
  - Contains at least 3 concrete real-world examples.
  - No paragraph longer than 5 sentences.
EOF

# 2. Hand it to Luper
luper run my_brief.md
# → Task 0042-a3f1c2 created, contract written, status:
#   awaiting_contract_approval

# 3. Review the contract (in the cockpit at http://localhost:8000 or
#    by cat-ing tasks/0042-a3f1c2/contract.json) — edit if needed
luper approve 0042-a3f1c2

# 4. Walk away. The agents plan, execute, verify, criticise, ship.
luper watch 0042-a3f1c2
# → live snapshot in the terminal; on DONE, find the result at
#   tasks/0042-a3f1c2/artifacts/mcp_overview.md
```

The artifact is in `tasks/<id>/artifacts/`. The full trail — every prompt, every response, every verdict, every routing decision — is in `tasks/<id>/llm_calls.jsonl` and `tasks/<id>/events.jsonl`. Nothing is hidden.

---

## Install

Prerequisites:

- **Python 3.12+** and **git**.
- **[claude CLI](https://claude.com/docs/claude-code) 2.1+** authenticated via `claude login` (Claude Max subscription).
- **[codex CLI](https://github.com/openai/codex) 0.125+** authenticated via your ChatGPT account (Plus / Pro).
- **(optional) `OPENAI_API_KEY`** in `.env` — only needed if your briefs use Deep Research steps.

```bash
git clone https://github.com/Zisky-ai/Luper.git luper && cd luper
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

cp .env.example .env       # fill in OPENAI_API_KEY only if you need Deep Research
```

> **New here and driving Luper from Claude Code?** Just say *"onboard me"* / *"jak začít"* and the [`onboarding`](.claude/skills/onboarding/SKILL.md) skill walks you from this clone to your first finished artifact — install check, `luper doctor`, a ready-made starter brief, the contract gate, and where the result lands.

Verify the CLIs:

```bash
claude --version           # e.g. 2.1.119
codex --version            # 0.125.0+
luper --version            # 0.1.0.dev0
```

Run the test suite (fast subset — integration tests hit real CLIs and take ~15 min):

```bash
.venv/bin/python -m pytest tests/ -q --ignore=tests/test_integration_runner.py
```

---

## Running a task

### From the CLI

```bash
luper run my_brief.md                       # create task, run to contract approval
luper run my_brief.md -i input1.md -i input2.md   # with input files copied to inputs/
luper run my_brief.md --executor codex --critic claude   # per-task role swap

luper list                                  # show all tasks + status
luper status <task-id>                      # status snapshot (use --json for machine output)
luper watch <task-id>                       # live snapshot in the terminal

luper approve <task-id>                     # approve the contract, start the autonomous run
luper stop <task-id>                        # cooperative stop after the current phase
luper resume <task-id>                      # restart paused / stopped task
luper resume <task-id> --recover            # resume an error / partial task after manual fix
luper log <task-id> --tail 20               # last LLM calls (use --full for full prompts + responses)
luper events <task-id>                      # tail of events.jsonl
luper finalize <task-id>                    # regenerate artifacts/README.md + sanitise wikilinks
luper accept-draft <task-id> <step>         # accept the current artifact as the step result
luper skip-step <task-id> <step>            # skip a step that won't converge
luper discard <task-id>                     # discard the task before approval
```

Full reference: `luper --help`, `luper <command> --help`, and the stable contract for supervisor recipes in [`docs/api_reference.md`](docs/api_reference.md).

### From the cockpit (web UI)

```bash
uvicorn cockpit.app:app --reload --port 8000
# open http://localhost:8000
```

The cockpit handles the same operations as the CLI: new task via form, contract review / edit / approve, live status + events + LLM-call stream, stop / resume / discard buttons, recovery from error / partial states. It owns no state — it only writes `contract_approval.json`, `contract_edited.md`, and `stop.signal`; everything else is read-only display from the task workspace.

---

## Mental model

```
                              brief (markdown)
                                     │
                                     ▼
                  ┌───────── CONTRACT ─────────┐
                  │  claude reads brief, emits  │
                  │  goal + deliverables +      │
                  │  acceptance_criteria        │
                  └─────────────┬───────────────┘
                                ▼
                       ✋ APPROVAL GATE
                  (cockpit / luper approve)
                                │
                                ▼
                  ┌─────────── PLAN ───────────┐
                  │ claude drafts plan (1–20    │
                  │ steps), codex critiques,    │
                  │ claude finalises            │
                  └─────────────┬───────────────┘
                                ▼
        ┌─────────────── EXECUTE LOOP ─────────────────┐
        │   for each incomplete step:                  │
        │     executor (claude or codex) → artifact    │
        │     deterministic checks (regex, word_count) │
        │     verifier (claude) → pass / fail / inc.   │
        │       on pass: critic loop (codex) reviews   │
        │       on fail: retry up to max_retry         │
        │       retries out: replan once               │
        │       replan out: PARTIAL                    │
        └────────────────┬─────────────────────────────┘
                         ▼
                 ┌─── terminal ───┐
                 │ DONE | PARTIAL │
                 │ ERROR | STOPPED│
                 │ DISCARDED      │
                 └────────────────┘
                         │
                         ▼ (on DONE)
                  auto-finalize:
              artifacts/README.md generated,
            [[wikilinks]] sanitised for Obsidian
```

**The runner is deterministic in routing — no LLM decides "what next".** Agents have maximum freedom *inside* a phase; the runner alone decides which phase runs next. Hard limits (`max_retry_per_step`, `max_replan_per_task`, `max_research_per_task`) are integers checked by the loop, not policies an LLM has to be persuaded to respect.

**State lives on disk.** `tasks/<id>/state.json` is the single source of truth (atomic save, `tempfile + os.replace`). `events.jsonl` is the append-only audit log. `llm_calls.jsonl` records every prompt and response. The runner can be killed and resumed from disk alone — no replay log to reconstruct.

**Workflow is text.** Edit `workflow/prompts/<role>.md` or `workflow/workflow.md`, the next task picks it up. Existing tasks read from their snapshot in `tasks/<id>/workflow_snapshot/` and stay reproducible. This is the load-bearing "workflow as product" principle from the binding spec.

For the deep version: [`AGENTS.md`](AGENTS.md) (deep technical reference for AI models joining the codebase) and [`docs/design_notes.md`](docs/design_notes.md) (the *why* behind every load-bearing design choice).

---

## What Luper is NOT

- **Not a chat.** No dialogue interface. No agent debate. You write a brief, you get an artifact.
- **Not a multi-step agent** like AutoGPT. The workflow is **fixed text**, not LLM-decided.
- **Not a state-machine engine.** It's a `while` loop with explicit phases. No graph DSL, no nodes-and-edges abstraction.
- **Not a paid-by-call service.** Uses subscription CLIs and never reports cost. Deep Research is the one metered exception (and is hard-capped at 3 calls per task).
- **Not a SaaS.** Your machine, your data, your subscriptions. Nothing leaves your box except the API calls your `claude` / `codex` CLIs already make.
- **Not multi-tenant.** Single user, single task at a time, single process. No queue, no scheduler — that's what the external supervisor does.
- **Not a framework.** No plugin API, no hooks, no extension points. Forking the source is the extension model.

If you need any of the above, Luper is not your tool. If the absence of all of them sounds refreshing, read on.

---

## Documentation map

### Start here

| Document | Contents |
|---|---|
| [README.md](README.md) | This file. |
| [`.claude/skills/onboarding/`](.claude/skills/onboarding/SKILL.md) | First-run onboarding skill — say *"onboard me"* in Claude Code to be walked from clone to first artifact. |
| [AGENTS.md](AGENTS.md) | Deep technical reference for AI models joining the codebase. Read this if you want to extend or debug. |
| [docs/design_notes.md](docs/design_notes.md) | Permanent design rationale — the *why* behind load-bearing choices that survived 19+ real-life briefs. |
| [docs/design_spec.md](docs/design_spec.md) | The binding spec (translated from the original Czech `zadání v3 final`). Source of truth for what the system must do. |
| [LICENSE](LICENSE) | MIT. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to open an issue, the dev loop, test/lint commands, project values. |

### Writing briefs

| Document | Contents |
|---|---|
| [docs/brief_quickstart.md](docs/brief_quickstart.md) | 5-minute guide for your first brief. |
| [docs/brief_template.md](docs/brief_template.md) | Copy-pasta skeleton for `luper run`. |
| [docs/brief_author_guide.md](docs/brief_author_guide.md) | Full guide — how Luper reads briefs, how to write acceptance criteria that pass first-try, patterns and anti-patterns. |
| [docs/examples/briefs/](docs/examples/briefs/) | Real example briefs Luper processed successfully — copy and adapt. |

### Running, supervising, integrating

| Document | Contents |
|---|---|
| [docs/api_reference.md](docs/api_reference.md) | **Stable contract** — CLI commands, exit codes, event kinds, state.json schema. What supervisor skills pin to. |
| [docs/automation_integration.md](docs/automation_integration.md) | How to drive Luper from an external agent (Saturnin, Claude Code skills, custom orchestrators). |
| [docs/operations/recipes.md](docs/operations/recipes.md) | Reusable how-to patterns for supervisors: stale-session recovery, monitor filters, AFK heartbeat, contract-approval gating, plateau intervention. |
| [docs/operations/incidents.md](docs/operations/incidents.md) | Append-only log of past incidents with fixes and prevention notes. |
| [docs/cli_findings.md](docs/cli_findings.md) | Operational notes on the `claude` and `codex` CLIs (flags, quirks, gotchas). |

### Implementation-level

| Document | Contents |
|---|---|
| [docs/audit_2026-05_synthesis.md](docs/audit_2026-05_synthesis.md) | Dual-model code audit (Claude Opus 4.7 + GPT-5) synthesis — the basis for the 2026-05 cleanup. |
| [docs/_archive_index.md](docs/_archive_index.md) | Index of files removed in the public-release cleanup, with recovery recipe via git. |
| [TODO.md](TODO.md) | Active sprint plan. |
| [workflow/workflow.md](workflow/workflow.md) | Human prose description of the phase sequence. |
| [workflow/prompts/](workflow/prompts/) | Agent system prompts (contract, planner, executor, verifier, critic). |
| [workflow/schemas/](workflow/schemas/) | JSON Schemas for contract / plan / verdict. |

---

## Directory structure

```
luper/
├── README.md                # this file
├── AGENTS.md                # deep reference for AI models
├── CONTRIBUTING.md          # how to contribute
├── LICENSE                  # MIT
├── TODO.md                  # live sprint plan
├── config.yaml              # limits, timeouts, CLI binary paths
├── pyproject.toml           # Python package + `luper` entry point
├── .env.example             # ENV template
│
├── workflow/                # text definition of the workflow + prompts + schemas
│   ├── workflow.md
│   ├── prompts/
│   └── schemas/
│
├── luper/                   # thin orchestrator (Python, async) — the harness
│   ├── orchestrator.py      # main while-loop
│   ├── phases.py            # per-phase logic
│   ├── cli.py               # claude/codex subprocess wrapper
│   ├── sessions.py          # persistent claude sessions
│   ├── state.py             # TaskState (pydantic, atomic save)
│   ├── deterministic.py     # word_count / regex_present / …
│   ├── validation.py        # JSON Schema + minimal repair
│   ├── deep_research.py     # OpenAI Responses API wrapper
│   ├── events.py            # append-only events.jsonl
│   ├── config.py            # config.yaml loader
│   ├── finalize.py          # artifacts/README.md + wikilink sanitiser
│   ├── recovery.py          # accept-draft / skip-step / resume --recover
│   └── cli_app.py           # `luper` CLI (typer)
│
├── cockpit/                 # FastAPI single-file app + HTML templates
│   ├── app.py
│   ├── static/style.css
│   └── templates/
│
├── tasks/                   # per-task state (gitignored)
│   └── <NNNN-uuidprefix>/
│       ├── state.json
│       ├── events.jsonl
│       ├── llm_calls.jsonl
│       ├── brief.md
│       ├── contract.json
│       ├── plan.json
│       ├── artifacts/
│       │   └── README.md         # auto on DONE: deliverable map + sanitised wikilinks
│       ├── verdicts/
│       ├── caveats.jsonl
│       ├── sessions/
│       └── workflow_snapshot/
│
├── tests/                   # pytest, incl. integration with real CLIs
└── docs/                    # spec, findings, design notes, operations
```

---

## Status & maturity

**Used in production by the maintainer since 2026-04 — 19+ real-life briefs processed end-to-end, two months of daily use.** Brief types range from analytical writing (market overviews, research-paper intros, GTM strategy) to managerial deliverables (audit synthesis, pricing models, source-discipline reviews). The brief journals (preserved in the maintainer’s private archive; index at [`docs/_archive_index.md`](docs/_archive_index.md)) are the empirical evidence base for the design rationale in [`docs/design_notes.md`](docs/design_notes.md).

**Operating model: supervised.** The default persona is "supervisor agent drives Luper" — typically a Claude Code skill (the `brief-launch` skill that ships in the maintainer's workspace). Solo unsupervised use works for sanity-level briefs and dev work but isn't the design target for v1. The runner exposes everything a supervisor needs to observe (`events.jsonl`, `state.json --json`) and intervene (`luper stop`, `luper resume --recover`, `luper accept-draft`, `luper skip-step`); see [`docs/automation_integration.md`](docs/automation_integration.md) for the full integration contract.

**Stability.** The CLI / event / state contract in [`docs/api_reference.md`](docs/api_reference.md) is the stable surface — breaking changes will bump the semver minor with a migration note. Internals may still move. Platform: Linux (developed and used on Ubuntu). macOS likely works for the Python core; Windows untested.

**Honest take.** Luper asks more of you than a one-click app. You install a CLI, write a brief, supervise the run. In return you get a harness you can read in an afternoon, an audit trail of every LLM call, and a workflow defined in editable text. If you want a button that magically produces a deliverable, this isn't it. If you want to *own* the agent harness driving your work, it might be.

---

## License & contributing

MIT — see [LICENSE](LICENSE).

How to contribute: [CONTRIBUTING.md](CONTRIBUTING.md). Open an issue first; small PRs preferred; the anti-overkill principle is load-bearing. Every code change follows the procedure in [`.claude/skills/dev-workflow/SKILL.md`](.claude/skills/dev-workflow/SKILL.md).

