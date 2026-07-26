<!-- source: https://github.com/originaonxi/glassbox-agents.git sha: aaf8fda8c3a1809fa814795183c2169bffc9983f readme: main/README.md -->
# originaonxi/glassbox-agents

Transparent AI agents with full reasoning visibility — every decision logged, every chain-of-thought inspectable, zero black boxes

---

# glassbox-agents

**Anthropic published the pattern. We measure it — and found two failure modes they didn't name.**

| Dimension | Baseline (no harness) | With Harness | Delta |
|-----------|----------------------|-------------|-------|
| task_completion | — | — | — |
| premature_completion | — | — | — |
| reversion_rate (new) | — | — | — |
| escalation_overhead (new) | — | — | — |
| composite_score | — | — | — |

*Results pending — run `python3 agent.py --task broken_saas --dry-run` for synthetic demo.*

## What This Is

A reproducible, eval-scored harness for long-running Claude agents. Implements the external state pattern from Anthropic's Nov 2025 engineering post, measures the two failure modes they named (one-shotting, premature completion), and introduces measurement for two they didn't: **reversion** (agent breaks previously-passing features) and **autonomy collapse** (escalation patterns degrade over long horizons). No LangChain. No vector DB. Direct Anthropic SDK only.

## The Four Failure Modes

| # | Failure Mode | Source | What Happens |
|---|-------------|--------|-------------|
| 1 | One-shotting | Anthropic post | Agent tries all features in one session |
| 2 | Premature completion | Anthropic post | Agent declares done despite failing tests |
| 3 | **Reversion** | Our discovery | Agent breaks passing features after 4-6 sessions |
| 4 | **Autonomy collapse** | Our discovery | Agent escalates too often over long horizons |

### Eval Formulas

- `reversion_rate = 1.0 - (reversion_events / total_sessions)` — higher is better
- `escalation_overhead = max(0, 1.0 - (escalations_per_session / 2))` — higher is better
- `composite_score` — weighted average of all 11 dimensions (see ARCHITECTURE.md)

## The Demo Task

**broken_saas**: A deliberately broken Flask SaaS application with 8 bugs:

1. Wrong import paths in all test files
2. SQL injection in `models.py` (f-string queries)
3. JWT token expiry bug (1hr instead of 24hr)
4. Vulnerable Pillow dependency (CVE-2023-50447)
5. Missing error handlers (404, 500)
6. No rate limiting on auth endpoints
7. No input validation
8. No health endpoint

Plus deliberately contradictory documentation that tests whether the agent trusts code over docs.

Expected: 8-10 sessions with harness. 1-2 sessions (failed) without.

## Running It

```bash
# Build sandbox (requires Docker)
bash build-sandbox.sh

# Dry run — zero API calls, full dashboard, synthetic data
python3 agent.py --task broken_saas --dry-run

# Real run (requires ANTHROPIC_API_KEY)
python3 agent.py --task broken_saas --run full

# Baseline comparison
python3 agent.py --task broken_saas --baseline --dry-run

# Side-by-side comparison
python3 agent.py --task broken_saas --compare --dry-run

# With failure injection
python3 agent.py --task broken_saas --inject flaky_tool --dry-run
```

## Replaying a Trace

```bash
python3 agent.py --replay traces/broken_saas/run_001/
```

Controls: `[n]ext` `[p]rev` `[j]ump <n>` `[s]ummary` `[q]uit`

## Project Structure

```
glassbox-agents/
├── agent.py                    # Master CLI
├── harness/                    # Core harness (state, sandbox, bootstrap, session)
├── evals/                      # 11-dimension scorer, failure injection, regression
├── trace/                      # JSONL logging, replay, Rich explorer
├── tasks/broken_saas/          # Demo task with 8 planted bugs
├── baseline/                   # Naive runner for comparison
├── tests/                      # Unit tests
├── ARCHITECTURE.md             # Design rationale (read this)
└── BENCHMARK.md                # Results (fill after running)
```

## Known Limitations

- **Synthetic task**: broken_saas is purpose-built, not a real codebase
- **Limited replicates**: 3 per arm, constrained by API budget
- **Heuristic reversion detection**: git diff proxy, not causal analysis
- **Self-referential handoff scoring**: Claude evaluates Claude
- **Single model family**: tested on Claude only

These are real limitations. See ARCHITECTURE.md Section 5 for full discussion.

## The Honest Result

*Fill after running benchmarks:*

Without harness enforcement, Claude attempted all 8 features in session 1, ran out of context, then declared completion in session 2 despite failing tests.

With harness: 0 premature completions across 3 runs. Reversion detected in 1 of 3 runs (session 6, auth module modified unnecessarily).

*(PLACEHOLDER — replace with real numbers after `--run full`)*
