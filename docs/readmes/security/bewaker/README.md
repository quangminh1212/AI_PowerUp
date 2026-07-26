<!-- source: https://github.com/bewakerai/bewaker.git sha: 4078af028d1d031352651768cc1723903e45871b readme: main/README.md -->
# bewakerai/bewaker

Guardrails for agentic coding

---

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)]()
[![License](https://img.shields.io/badge/license-Apache_2.0-green.svg)]()
![VS Code](https://img.shields.io/badge/Built_for-VS_Code-orange?logo=visualstudiocode)

Bewaker.AI – AI-aware Repo Guardrails
=====================================

> AI pair programmers ship code faster than review and change-control processes can keep up. Without guardrails, regulated configs are overwritten, secrets leak, and compliance evidence disappears.

Bewaker keeps AI-assisted and human commits honest. It combines policy-driven file protection, cryptographic Merkle locking, unlock approvals, Git hook enforcement, and a tamper-evident audit trail – all enforced locally inside VS Code and your Git repo.

Features at a glance
--------------------
- Policy-driven protections defined in `.guardpolicy.yml` (glob patterns with optional approvals and owners)
- One-click policy discovery via `Bewaker: Recommend Policy` (now includes vulnerability scanning)
- File Explorer decorations and a warning banner on protected files, plus quick unlock/approve actions
- Protected Files view, Command Center dashboard, and Risk Inspector with heuristic signal explanations
- Line-level locks via `.bewaker-ranges.json`; edits within locked ranges auto-revert and are logged
- Cryptographic lockfile `.guardlock` with SHA-256 + Merkle root + Ed25519 signatures (keys remain local)
- Tamper-evident audit trail `.bewaker-audit.jsonl` (hash-chained JSON lines with in-product verifier)
- Git pre-commit and pre-push hooks that verify staged content, enforce unlock approvals, and log outcomes
- Local AI session tracking (`Bewaker.AI: Start/Stop`) that can raise approval requirements during active AI work

Requirements
------------
- **VS Code** 1.85.0 or newer (Desktop)
- **Node.js** 18.x or 20.x (for building, running scripts, and Git hooks)
- **Git** 2.39 or newer (hooks call `git` commands and inspect the index)
- Ability to run local Node scripts (hooks are Node-based)

Installation
------------
### Option A – Visual Studio Marketplace (recommended)
1. Open VS Code and navigate to the Extensions marketplace (`⇧⌘X` / `Ctrl+Shift+X`).
2. Search for **"Bewaker.AI – AI-aware Repo Guardrails"** and install the extension published by `bewaker`.
3. Reload VS Code and open the repository you want to guard.

### Option B – Install the packaged VSIX
1. Download or build `bewaker-1.0.0.vsix` (run `vsce package` in this repo if you need a fresh artifact).
2. Install with VS Code: `code --install-extension bewaker-1.0.0.vsix`.
3. Reload VS Code and open the repository you want to guard.

### Option C – Run from source (development)
1. Clone the repository and open it in VS Code.
2. Install dependencies: `npm ci`.
3. Build TypeScript: `npm run build`.
4. Launch the extension in a dev window: run the "Run Extension" debug configuration or press `F5`.

After installation, open the **Bewaker** activity bar icon to access the Command Center, Protected Files tree, and Audit Trail.

Quick start
-----------
1. **Create a policy** – add a `.guardpolicy.yml` or run `Bewaker: Recommend Policy` to bootstrap one. Example:
   ```yaml
   - id: core-configs
     match:
       - package.json
       - tsconfig.json
     approvals_required: 1
   ```
2. **Lock the repository** – run `Bewaker: Lock Repository`. This writes `.guardlock` and generates `.bewaker/keys.json` (keep it untracked).
3. **Install hooks** – run `Bewaker: Install Git Hooks`. Commits and pushes now verify the staged content matches the lock and approvals.
4. **View protections** – open the Protected Files view or the Command Center for metrics, alerts, and active unlocks.
5. **Try an edit** – modify a protected file without unlocking. The edit is reverted, an audit entry is recorded, and the tree highlights the protected state.
6. **Request and approve unlocks** – use the banner or command palette (`Bewaker: Request Unlock…`, `Bewaker: Approve Unlock`) to record temporary access with expiry and approvals. Unlocks are per file, so repeat this step for each protected path you plan to modify.
7. **Verify integrity** – run `Bewaker: Verify Repository` anytime or let the Git hooks run verification on every commit/push.

Example workflow
----------------
```bash
# Install dependencies and build the extension
npm ci
npm run build

# Start VS Code with the current repo
code .

# In VS Code command palette (⇧⌘P / Ctrl+Shift+P):
#   1. Bewaker: Recommend Policy
#   2. Bewaker: Lock Repository
#   3. Bewaker: Install Git Hooks
#   4. Bewaker: Verify Repository
```

When you attempt `git commit` with a protected file staged and no unlock, the pre-commit hook blocks the commit, prints the offending paths, and records a `commit_blocked` audit entry.

Command Center
--------------
![Command Center overview](media/command-center.png)

- Review unlock approvals, filesystem guardian incidents, risk signals, and pending actions from a single dashboard.
- Launch remediation flows (`Relock Repository`, `Resolve Merkle Mismatch`, `View Audit Log`) without leaving the view.
- Filter by policy, risk tier, or incident type to focus on the unlocks that need attention.

Protected Files Tree
--------------------
![Protected Files Tree 2.0](media/protected-files.png)

- Inline badges call out risk tier, approval counts, and external edit incidents next to every guardlocked asset.
- Quick actions let you request or approve unlocks, filter to high risk only, and deep link into the Command Center.
- Context-aware filters surface only the files your policy protects, avoiding noise from the rest of the repo.

Configuration reference
-----------------------
### `.guardpolicy.yml`
Array of policies that describe which files are protected and how many approvals they need.
- `id` *(string, required)* – logical name for the policy
- `match` *(string or string[])* – glob(s) matched relative to repo root
- `owners` *(string[])* – optional code owners or approvers
- `approvals_required` *(number)* – minimum approvals before commit

Example with multiple policies:
```yaml
- id: release-assets
  match:
    - scripts/release/**
    - .github/workflows/release.yml
  approvals_required: 2
  owners:
    - release-team@example.com

- id: infrastructure
  match:
    - terraform/**
    - helm/**
    - k8s/**
  approvals_required: 1
```

### `.bewaker/config.json`
Created automatically; tweak via commands or manual edits.
- `risk.enableApprovalBump` – if `true`, high/medium risk files add extra approvals (defaults to `false`).
- `risk.high` / `risk.medium` – approvals added when bumps are enabled.
- `aiSession.active` – toggled by `Bewaker.AI` commands.
- `aiSession.provider` – descriptive label for the active AI session (display only).
- `aiSession.fileThreshold` – staged file count that triggers AI bulk warnings.
- `aiSession.extraApprovals` – approvals automatically required during an AI session.

Example:
```json
{
  "risk": { "enableApprovalBump": true, "high": 2, "medium": 1 },
  "aiSession": { "active": false, "fileThreshold": 20, "extraApprovals": 1 }
}
```

### `.bewaker/heuristics.json` (optional)
Overrides default risk scoring weights. See `docs/risk-signals.md` for the full schema. A minimal example:
```json
{
  "thresholds": { "high": 6, "medium": 3 },
  "weights": { "docPenalty": -4 },
  "overrides": [
    { "pattern": "docs/**", "level": "low", "reason": "Documentation" }
  ],
  "allowPatterns": ["README.md"],
  "denyPatterns": ["prod/**"]
}
```

### `.bewaker-ranges.json` (optional)
Defines line-level locks. Each range is 1-based inclusive:
```json
[
  { "path": "src/api.ts", "start": 10, "end": 42, "policy": "core-configs" }
]
```

Git hooks
---------
- **Pre-commit (`scripts/hooks/pre-commit.js`)** – Verifies the staged copy of every protected file against the locked Merkle tree, checks unlock expirations, and enforces approval counts. Blocks the commit when mismatches are detected.
- **Pre-push (`scripts/hooks/pre-push.js`)** – Re-runs staged verification before pushing and records audit entries.

Hooks are installed via `Bewaker: Install Git Hooks` and call Node directly (`node scripts/hooks/...`). They respect:
- `GIT_AUTHOR_NAME` / `GIT_AUTHOR_EMAIL` – used for audit attribution when available
- `USER` / `USERNAME` – used when recording quick unlock actors

To uninstall, delete `.git/hooks/pre-commit` and `.git/hooks/pre-push` or reinstall your own hooks, then remove `.bewaker` artifacts if desired.

Commands & views
----------------
- `Bewaker: Lock Repository` / `Relock Repository` – regenerate `.guardlock` and sign it
- `Bewaker: Verify Repository` – recompute hashes and verify signature
- `Bewaker: Recommend Policy` – scans for high-risk files, includes detected vulnerabilities, and writes `.guardpolicy.yml`
- `Bewaker: Request Unlock…`, `Bewaker: Approve Unlock`, `Quick Unlock`, `Quick Approve` – manage local unlock windows
- `Bewaker: Open Risk Inspector` – rich table of protected files, risk levels, approvals, and signals
- `Bewaker: View Audit Log` – opens a live-updating webview with the audit chain verifier
- `Bewaker.AI: Start/Stop/Toggle AI Session` – mark AI-assisted edits and add temporary approval bumps

Every protected file displays CodeLens actions, a banner, and explorer decorations showing its risk tier (`H`, `M`, `L`).

Documentation
-------------
- [Policy syntax reference](docs/POLICY_REFERENCE.md) – exhaustive `.guardpolicy.yml` schema, approvals, owners, and inheritance rules.
- [Troubleshooting guide](docs/TROUBLESHOOTING.md) – workflows for verification failures, unlock issues, watcher alerts, and incident response.
- [Architecture overview](docs/ARCHITECTURE.md) – how the extension, Git hooks, audit ledger, and filesystem guardian coordinate enforcement tiers.
- [External edit incidents](docs/EXTERNAL_EDIT_GUIDE.md) – investigative checklist when guardlocked files change outside unlock windows.
- [Merkle mismatch playbook](docs/MERKLE_MISMATCH_GUIDE.md) – recovery steps when `.guardlock` diverges from workspace content.
- [Risk signals](docs/risk-signals.md) – heuristic weights and overrides powering the risk inspector.
- [Sequential unlock workflow](docs/MULTI_FILE_UNLOCK_WORKFLOW.md) – guidance for editing multiple protected files safely.

Practical examples
------------------
Lock a single file from the editor title bar:
1. Open the file.
2. Run `Bewaker: Lock Current File`.
3. Attempt to edit; Bewaker cancels the change, prompts for an unlock, and writes an `edit_blocked` entry.

Review risk signals for a file:
1. Select the file in the editor or Protected Files tree.
2. Run `Bewaker: Show File Risk Details`.
3. View the heuristics that triggered the protection (path matches, secret keywords, etc.).

Troubleshooting
---------------
| Symptom | Suggested resolution |
| --- | --- |
| `missing_guardlock` during commit/push | Run `Bewaker: Lock Repository` to regenerate `.guardlock`, commit it, and retry. |
| `missing_file:…` reason | The locked file has been removed or renamed. Restore it or relock the repo once the change is intentional. |
| `merkle_mismatch` | The staged content differs from the locked hash. Run `Bewaker: Verify Repository`, review or revert the diff, then relock once approved. Use `Bewaker: Resolve Merkle Mismatch` for a step-by-step guide. |
| `signature_invalid` / `signature_error` | `.guardlock` or `.bewaker/keys.json` may be corrupted. Delete `.guardlock`, run `Bewaker: Lock Repository`, and re-install hooks. |
| Unlock not honoured | Check `.bewaker/unlocks.json` expiry and that system clock is accurate. Unlocks are local-only (not shared) and must be requested per file. |
| VS Code decoration missing | Ensure the workspace folder is recognised as the Bewaker root (contains `.guardpolicy.yml`). Use `Bewaker: Refresh View` to reload state. |
| Hook blocked but file already approved | Confirm the unlock includes enough approvals and hasn’t expired. `Bewaker: Protected Files` view shows current approval counts. |

Known limitations
-----------------
- Unlock workflows are per file. Batch or multi-select unlock operations are not yet supported; request and approve each path individually.
- Guardlock verification relies on local filesystem access and may report false positives on network drives with eventual consistency.

Roadmap highlights
------------------
- Batch unlock operations – under consideration for v1.1 based on launch feedback. Track the GitHub issue tracker for updates.

Testing & CI
------------
- Run the typecheck/build: `npm run build`
- Run automated tests: `npm test`
  - Includes risk heuristic unit tests and guardlock verification tests (tampering, missing files)
- CI (`.github/workflows/ci.yml`) runs both commands on Node 18.x and 20.x

Before publishing a new build, run both commands locally and re-lock your target repository to ensure `.guardlock` is up to date.

Environment variables
---------------------
- `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL` – preferred values for audit actor identity in hooks
- `USER` / `USERNAME` – fallback identity for unlock requests and quick approvals

Support & contact
-----------------
- Security disclosures: `security@bewaker.ai`
- Code of conduct and community issues: `conduct@bewaker.ai`
- Product questions, feature requests, and bug reports: [GitHub Issues](https://github.com/bewakerai/bewaker/issues)

Security notes
--------------
- Keys are stored locally under `.bewaker/keys.json` (mode `0600`). Do **not** commit this file.
- The audit log (`.bewaker-audit.jsonl`) is a hash-chained ledger. Use `Bewaker: Verify Audit Chain` to validate integrity.
- No telemetry or remote services are used; everything runs locally.
- Consider adding a CI step that executes `npm run build` and `npm test`, and verifies `.guardlock` before merge.

Contributing
------------
See `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` for contribution guidelines, conduct expectations, and responsible disclosure instructions.

License
-------
Apache-2.0. See `LICENSE` and `NOTICE`.
