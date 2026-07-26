<!-- source: https://github.com/ToolJet/ActionRail.git sha: b86a78b4b3b58edfd322f4a2c04dba8f55403706 readme: master/README.md -->
# ToolJet/ActionRail

Open-source runtime action grounding framework for AI agents. Verify proposed actions against live systems of record before execution.

---

<p align="center">
  <img src="docs/static/img/actionrail-logo-horizontal.svg" alt="ActionRail Beta by ToolJet" width="320">
</p>

# Verify what an AI agent is about to _do_ — before it does it.

ActionRail is an open-source project by [ToolJet](https://www.tooljet.com).

> **Release status:** ActionRail is currently in public beta. Interfaces may
> evolve before ActionRail v1, which is planned for August 2026.

> **Integration support:** Any Python application can use the framework-neutral
> `ActionRuntime`. LangGraph also has automatic tool discovery and wrapping;
> additional automatic framework adapters are planned.

An agent's tool call can be perfectly *permitted* and perfectly *well-formed* and
still be *wrong*: a refund on an order that was already refunded, a transfer to a
real account that belongs to the wrong customer, a withdrawal larger than the
balance. Allowlists and schema checks pass all of these, because the *shape* is
fine — it's the *value* that's wrong.

ActionRail intercepts an agent's consequential tool calls and, before execution,
grounds each argument **against your live system of record** — then returns
**allow / hold-for-human / block**. It's the last-mile correctness gate: not "is
the agent allowed to do this?" but "is this specific value actually right, right
now, against your real data?"

![ActionRail verifies an agent tool call against live systems of record before allowing execution](docs/static/img/actionrail-runtime-gate.svg)

*ActionRail runs at the execution boundary. Source lookups and credentials stay
in the customer environment, and the tool runs only after an `allow` decision.*

## Choose an integration path

The ActionRail runtime is framework-neutral. LangGraph is the first adapter
that adds automatic tool discovery and wrapping.

| Your application | Integration | Start here |
| --- | --- | --- |
| Any Python agent, worker, API, or application | Explicit `ActionRuntime` boundary | [Direct Python guide](https://actionrail.ai/docs/sdk/framework-neutral/) |
| LangGraph | Automatic discovery and tool wrapping | [LangGraph quickstart](https://actionrail.ai/docs/getting-started/quickstart/) |

### Any Python application

Install the base SDK, create an agent and its actions in the Console, then put
`ActionRuntime` around the real operation:

```bash
python -m pip install actionrail actionrail-console
```

```python
from actionrail import ActionRuntime

runtime = ActionRuntime(
    agent_id="…",
    api_key="ark_…",
)

result = runtime.execute(
    "issue_refund",
    {"order_id": order_id, "amount": amount},
    issue_refund,
    context={"customer_id": authenticated_customer_id},
)
```

`execute()` invokes `issue_refund(**arguments)` only after authorization. Use
the same API in custom agent loops, workers, API handlers, or frameworks without
a dedicated adapter. See the [direct Python integration](https://actionrail.ai/docs/sdk/framework-neutral/).

### LangGraph automatic adapter

Use `enforce()` when you want ActionRail to discover and wrap a compiled
LangGraph agent's tools:

```python
from actionrail import enforce, trusted_context
from actionrail.sdk.grounding import SQLiteSource

agent = enforce(
    agent,
    agent_id="…",
    api_key="ark_…",
    sources={"billing": SQLiteSource("billing.db")},
)
with trusted_context(customer_id="C-1007"):
    agent.invoke(inputs)
# wire_money(account="1234567") -> blocked before the underlying tool runs
```

Detailed reasons remain available to local application code through the
`on_decision` callback. The model-facing tool result, outbound Activity, and
review records use separate value-free representations.

### Run the packaged LangGraph demo

The complete deterministic demo needs no model API key:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "actionrail[agents]" actionrail-console
actionrail-console --no-open
```

In a second terminal:

```bash
source .venv/bin/activate
actionrail-quickstart
```

The demo creates a local SQLite Source, installs a grounding rule, attempts a
cross-customer refund, proves the real tool did not execute, and verifies the
redacted block in Activity. Open `http://127.0.0.1:8020/activity` to inspect it.

To run the same poisoned support note through a real model-driven LangGraph
loop, provide an Anthropic API key and a model ID available to your account:

```bash
export ANTHROPIC_API_KEY="…"
actionrail-quickstart --model claude-sonnet-4-6
```

The demo tool is local and harmless. If the model proposes the cross-customer
refund, ActionRail verifies the order against authenticated caller context and
blocks it before the function runs. If the model resists the injected note, the
command reports that outcome and submits the same poisoned proposal as a clearly
labelled deterministic runtime challenge. This tests the ActionRail boundary
without pretending the proposal came from the model. The deterministic mode
remains the stable path for CI and first-time evaluation.

## Why it's different

Policy engines and authz (OPA, Cedar, ReBAC) decide whether an action is
*permitted* given facts you've pre-loaded. By design they don't reach out to a
live system and check a value at call time — Cedar, for instance, is a
side-effect-free language with no I/O. ActionRail fills exactly that gap: it
queries your real data at the moment of the call and verifies the argument.

| Check | Answers | ActionRail |
|---|---|---|
| Allowlist / schema | is the call *well-formed*? | — |
| Policy / authz | is the agent *permitted*? | — |
| **Grounding** | is the *value* correct vs. live data? | ✅ |

### The evidence

We red-teamed eight models across four providers with value-poisoning attacks:
inputs that steer an agent toward a well-formed but *wrong* argument value. Every
model executed at least one poisoned value when unprotected, with attack success
ranging from **1.7% to 63.3%** — a stronger model did not make the risk go away.
With ActionRail in front, **0 of 480** manipulated actions executed and **0 of
480** legitimate look-alike requests were wrongly blocked.

**[Read the value-poisoning benchmark →](https://actionrail.ai/research/value-poisoning-benchmark)** · [PDF](https://actionrail.ai/research/value-poisoning-benchmark.pdf)

## The decision pipeline

`decide()` runs cheapest-check-first and returns `allow` / `hold` / `block`
(block outranks hold outranks allow):

| Tier | Check | Example |
|---|---|---|
| **Policy** | deterministic expression | `amount <= 200` → over limit *holds* for a human |
| **Grounding** | value vs. system of record | account must exist, belong to the caller, and be in a refundable state → mismatch *blocks* |

Grounding is expressive: multiple checks ANDed across different Sources, each
comparing a returned field with an operator (`= ≠ > ≥ < ≤ contains, is one of, is
set, is empty`) against a caller-context value, a literal, **another argument**
(`balance ≥ amount`), or the **current time** (`delivered_at ≥ now-30d`). Checks
can require a row (`expect: row`) or its *absence* (`expect: absent`, for
blocklists / idempotency), bind query params by name (`:customer_id` in SQLite,
`%(customer_id)s` in PostgreSQL/MySQL), and carry a retry + fail-open/closed policy.

## Action Tests: rules as executable contracts

Commit expected action behavior alongside your rules and run it through the
same decision pipeline used in production:

```yaml
# actionrail.cases.yaml
schema_version: 1
cases:
  - name: cross-customer refund is blocked
    tool: issue_refund
    args: {order_id: order-100, amount: 75}
    context: {customer_id: customer-2}
    expect: block
    fixtures:
      billing-production:
        by_value:
          order-100: {customer_id: customer-1, status: delivered}
```

```bash
actionrail test
# PASS  cross-customer refund is blocked
# 1 passed · 0 failed
```

**Action Tests** make `allow`, `hold`, and `block` a reviewable CI contract.
Deterministic Source fixtures exercise the real policy evaluator and grounding
matcher without a model, Console, credentials, or network access. Production
Sources remain off unless a separate integration stage explicitly passes
`--live-sources`. See the [Action Tests guide](docs/docs/testing/action-tests.mdx)
or run the complete contract in [`examples/action_tests/`](examples/action_tests/).

## Sources

Grounding runs against sources that stay in your environment (the data plane
never leaves your VPC). Today: **SQLite**, **PostgreSQL**, **MySQL/MariaDB**,
**HTTP/REST**, and **MCP gateway** adapters. MCP Sources call a configured verification tool over
Streamable HTTP, require its `readOnlyHint`, and prefer structured tool output. Secrets are
written as `${env:VAR}` references and resolve locally, so credentials never
reach the control plane. Use a gateway identity that can invoke only read tools;
MCP annotations are hints, not an authorization boundary.

```yaml
sources:
  stripe-production:
    adapter: mcp
    endpoint: https://gateway.internal/mcp
    headers:
      Authorization: Bearer ${env:MCP_GATEWAY_TOKEN}
    tool: stripe.get_charge
    arguments:
      charge_id: "{value}"
    select: data.charge
    timeout: 10
    require_read_only: true
```

This keeps MCP connection details on the Source. Rules reference the Source and
only describe how to evaluate the returned record; they do not duplicate the
gateway endpoint, tool name, or argument mapping.

PostgreSQL Sources keep connection details on the Source and queries on rules.
Use a dedicated role with `SELECT`-only permissions. ActionRail also forces each
verification transaction into PostgreSQL read-only mode and applies connection
and statement timeouts. Queries use Psycopg named parameters such as
`%(value)s`, `%(amount)s`, and `%(customer_id)s`:

```yaml
sources:
  billing-production:
    adapter: postgres
    host: postgres.internal
    port: 5432
    dbname: billing
    user: actionrail_reader
    password: ${env:POSTGRES_PASSWORD}
    sslmode: verify-full
    sslrootcert: /etc/ssl/certs/postgres-ca.pem
    connect_timeout: 5
    statement_timeout_ms: 5000
    require_read_only: true
```

The SDK depends on the Psycopg interface, leaving the libpq implementation to
the host application. For a self-contained local install, add
`psycopg[binary]>=3.2,<4`; production environments can use the system-linked
`psycopg[c]` build instead.

MySQL and MariaDB Sources use the same named query parameters and enforce
`START TRANSACTION READ ONLY` for every check. PyMySQL is included with the SDK:

```yaml
sources:
  billing-mysql:
    adapter: mysql
    host: mysql.internal
    port: 3306
    database: billing
    user: actionrail_reader
    password: ${env:MYSQL_PASSWORD}
    ssl_mode: verify-identity
    ssl_ca: /etc/ssl/certs/mysql-ca.pem
    connect_timeout: 5
    query_timeout: 5
    require_read_only: true
```

## Control plane + Console

An optional Django + DRF control plane and React Console let you register
sources, author grounding rules per argument, and watch a live **Activity
feed** of every allow / hold / block the runtime made. The SDK reports metadata
only — tool names, outcomes, value-free reasons, and redacted previews. Detailed
grounding results and rendered previews are exposed only on the local `Decision`;
model-facing tool results receive their own fully redacted representation. Preview
placeholders in control-plane reports become `[redacted]` unless a rule explicitly
allowlists a field with `write.report_args`; source-record values are never exported. Runtime reports use
a bounded, local SQLite outbox with batching, retry backoff, saturation
backpressure, and a normal-shutdown flush. Events are committed before the SDK
accepts them, stable IDs make retries idempotent, and delivery resumes after a
process restart. The outbox contains metadata but never the agent key and is
stored under `~/.actionrail/sdk/` by default; set `ACTIONRAIL_SDK_STATE_DIR` or
pass `state_dir=` to choose another location. Call `close_reporting(agent)` from
your application shutdown hook. A `False` result means rows remain durably
pending for the next process rather than being discarded.

Argument reporting is explicit and field-level; everything else remains
redacted:

```yaml
write:
  preview: "Refund order {order_id} for {amount}"
  report_args: [amount]  # explicit opt-in; order_id remains [redacted]
```

Expose `get_runtime_health(agent)` from your application health endpoint to see
whether the SDK is using cached configuration, how stale its last validated
snapshot is, and whether audit rows are pending after a delivery failure.

Human-review actions always fail closed when the Console cannot be reached. The
model-facing result uses `ACTIONRAIL_REVIEW_UNAVAILABLE`, distinct from a normal
pending review or human rejection, and the underlying tool is never executed.

Remote enforcement accepts cached configuration for up to 24 hours by default.
After `max_config_staleness` is exceeded, enforcing-mode tool calls fail closed with
`ACTIONRAIL_CONFIG_STALE` until a refresh succeeds. Set the limit in seconds on
`enforce(...)`; pass `None` only when your deployment explicitly accepts
unbounded configuration staleness.

## Anonymous usage telemetry

The OSS Console and SDK send three allowlisted events to
`https://hub.actionrail.ai/v1/events`: `console_started`, `sdk_initialized`, and
one `usage_summary` snapshot per UTC day. The summary contains exact totals
for configured and active agents, observed and evaluated actions, and actions
monitored, allowed, blocked, or held. Events also contain a locally generated
anonymous installation UUID, package version, Python major/minor version, and
operating-system family. They never contain agent or tool identities, rules,
arguments, individual decisions, Source configuration, endpoints, credentials,
audit records, paths, or errors.

Disable telemetry before starting the Console or agent process:

```bash
export ACTIONRAIL_TELEMETRY_DISABLED=1
```

`DO_NOT_TRACK=1` and `CI=1` are also honored. Delivery has a one-second timeout
and cannot affect enforcement or startup. Lifecycle events are best-effort. The
Console persists at most one aggregate-only usage summary for an hourly retry;
it never queues individual activity. See [Anonymous telemetry](docs/docs/security/telemetry.mdx)
for the complete event schema, counter definitions, and identifier lifecycle.

See [Runtime availability and failure behavior](docs/docs/operations/runtime-availability.mdx)
for the complete startup, outage, recovery, review, and shutdown contract.

## Development

Contributors using an editable repository checkout can run the packaged
quickstart implementation through `python examples/langgraph_quickstart.py`.

For development and the full test suite:

```bash
uv pip install -e ".[dev,control-plane]"   # SDK + tests + control plane
pytest                                     # run the suite
```

To run the development Console:

```bash
python control-plane/manage.py migrate && python control-plane/manage.py runserver 8020
cd frontend && npm install && npm run dev   # http://localhost:5173
```

To build the two beta wheels for manual distribution:

```bash
python scripts/build_beta_wheels.py
# dist/actionrail-0.1.0b9-py3-none-any.whl
# dist/actionrail_console-0.1.0b9-py3-none-any.whl
# dist/SHA256SUMS
```

Install both wheels, then start the self-contained local Console:

```bash
python -m pip install dist/actionrail-*.whl dist/actionrail_console-*.whl
actionrail-console
```

### Documentation site

The Docusaurus site lives in `docs/`:

```bash
cd docs
npm ci
npm start
```

Run the production build and broken-link checks with:

```bash
npm run build
```

See [`docs/README.md`](docs/README.md) for deployment variables, optional Algolia
search, site structure, and contribution conventions.

## Repository layout

```
actionrail/sdk/
  runtime.py            # framework-neutral evaluate / execute boundary
  actions.py            # explicit, privacy-safe action definitions
  action_tests.py        # versioned allow / hold / block regression contracts
  scanner.py            # zero-config action-surface discovery on a LangGraph agent
  instrument.py         # report the surface + observed calls to the control plane
  enforce.py            # the runtime gate: wrap consequential tools, decide before they run
  pipeline.py           # policy -> grounding -> allow / hold / block
  policy.py             # tier-1 deterministic policy
  config.py             # rule config + Source adapter build (with ${env:VAR} resolution)
  report.py             # metadata-only client to the control plane
  safewrite.py          # dry-run preview + transactional rollback (reversible sinks)
  grounding/
    base.py             # Source protocol + GroundVerdict
    match.py            # shared condition matcher (operators, ctx/arg/now targets)
    sqlite.py           # SQLite source adapter
    http.py             # HTTP/REST source adapter
    mcp.py              # MCP gateway source adapter (read-only tools)
    postgres.py         # PostgreSQL source adapter (read-only transactions)
    mysql.py            # MySQL/MariaDB source adapter (read-only transactions)
actionrail/cli.py        # `actionrail test` framework CLI
control-plane/          # Django + DRF: agents, rules, sources, decision feed
frontend/               # React console
tests/                  # pytest suite (grounding, pipeline, domains, SDK, control plane)
examples/               # runnable deterministic integrations
```

## Project status

**Public beta:** the framework-neutral `ActionRuntime`, LangGraph discovery and
`enforce()` adapter, policy + grounding pipeline, deterministic Action Tests,
SQLite + PostgreSQL + MySQL + HTTP + MCP Sources, control plane, and Console are
implemented and covered by the test suite.

**Roadmap:** provenance and taint tracking for values from untrusted memory,
additional agent-framework integrations, and more vendor-specific Source
adapters. ActionRail v1 is planned for August 2026.

## Contributing and support

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, safety-critical
change requirements, and pull-request guidance. Usage questions and bug-report
routing are documented in [SUPPORT.md](SUPPORT.md). Security reports must follow
[SECURITY.md](SECURITY.md).

Release changes are tracked in [CHANGELOG.md](CHANGELOG.md). Participation in
the project is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

ActionRail is licensed under the [Apache License 2.0](LICENSE).

Copyright 2026 ToolJet Solutions, Inc.
