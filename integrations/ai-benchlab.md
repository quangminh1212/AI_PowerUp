# AI_BenchLab

Benchmark & identity probe for multi-provider LLM APIs.

**Providers:** OpenAI · Anthropic · Gemini · OpenRouter · any OpenAI-compatible endpoint

**Metrics:** latency · token usage · instruction adherence · safety · identity match · logprobs fingerprint

## Quickstart

```powershell
cd C:\Dev\AI_BenchLab
$env:OPENAI_API_KEY = "sk-..."
python aibench.py --config bench.json --out results/openai.json
python analyze.py results/openai.json --out report.html --json
start report.html
```

## Configs

| File | Provider |
|------|----------|
| `bench.json` | OpenAI (default) |
| `bench.anthropic.json` | Anthropic |
| `bench.gemini.json` | Google Gemini |
| `bench.openrouter.json` | OpenRouter |

Env vars override:

| Provider | Env |
|----------|-----|
| OpenAI / OpenRouter | `OPENAI_API_KEY` |
| Anthropic | `ANTHROPIC_API_KEY` |
| Gemini | `GEMINI_API_KEY` |

## CLI

```
python aibench.py [--config bench.json] [--cases cases.json]
                  [--out results/results.json] [--timeout 120]
                  [--temperature 0] [--logprobs] [--dry] [-q]
```

```
python analyze.py results.json [--out report.html] [--json]
```

`--logprobs` captures token-level log-probabilities (slower, higher cost). Use for fingerprinting.

## Identity probe

`identity_match` compares **requested** vs **reported** model name from the provider response.
`system_fingerprint` (OpenAI) is extracted when present.

**Hard limit:** a provider can return any model name it likes. This is **not** cryptographic proof.
For stronger signal, use:

1. Multiple runs of the same prompt → `logprobs` Jensen-Shannon divergence (0 = identical)
2. Compare against a known baseline of the true model (control endpoint)
3. Check TLS cert / response headers / x-request-id patterns

## Remote git

```powershell
# Create empty repo on GitHub first, then:
git remote add origin https://<you>/AI_BenchLab.git
git push -u origin master
```

## Structure

```
aibench.py          # runner
adapters.py         # OpenAI / Anthropic / Gemini / OpenRouter
analyze.py          # HTML + JS-divergence report
cases.json          # test cases
bench*.json         # provider configs
results/            # output (gitignored)
```

## Extending cases

Edit `cases.json`:

```json
{ "id": "my-case", "prompt": "..." }
```

Add scoring later if needed — keep it simple first.
