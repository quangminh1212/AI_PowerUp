<div align="center">

<h2 id="claude-code-community-guide">Claude Code Guide</h2>

_For reference and contributions, visit the [official Claude Code documentation](https://code.claude.com/docs/en/overview)_

![Claude Code](https://img.shields.io/npm/v/@anthropic-ai/claude-code?label=Claude%20Code&logo=anthropic)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://anthropics/claude-code)
[![License](https://img.shields.io/badge/License-Anthropic-orange)](https://claude.ai/code)

</div>

<div align="center">

<kbd>

| Section                               | Status | Other Resources                                                                                         |
| ------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------- |
| Getting Started                       | ✅   | **Claude-Code** [Docs](https://code.claude.com/docs/en/overview)                                    |
| Configuration & Environment Variables | ✅   | **Claude-Code via** [**Discord**](https://zebbern/claude-code-discord)                       |
| Commands & Usage                      | ✅   | Security Agents [SKILL.md](https://zebbern/claude-code-guide/tree/main/skills)               |
| Interface & Input                     | ✅   | Let Agent Create [SKILL.md](https://zebbern/agent-skills-authoring)                          |
| Advanced Features                     | ✅   | 954+ Agent [Skills](https://zebbern/antigravity-awesome-skills)                              |
| Automation & Integration              | ✅   | No cost ai [resources](https://zebbern/no-cost-ai)                                           |
| Help & Troubleshooting                | ✅   | 250+ Mermaid [templates](https://zebbern/mermaid-templates)                                  |
| Third-Party Integrations              | ✅   | Discord Communication [MCP](https://zebbern/discord-mcp-agent)                               |


</kbd>

</div>

---

<h3 id="content">Contents</h3>

**Fast paths:** [Install](#quick-start) · [Commands](#claude-commands) · [Config](#configuration--environment) · [MCP](#mcp-integration) · [Agents](#sub-agents) · [Troubleshoot](#help--troubleshooting)

| Area | Start here | Also useful |
| --- | --- | --- |
| [Getting Started](#getting-started) | [Quick Start](#quick-start) | [Initial Setup](#initial-setup), [System Requirements](#system-requirements) |
| [Configuration](#configuration--environment) | [Environment Variables](#environment-variables) | [Configuration Files](#configuration-files) |
| [Commands](#commands--usage) | [Slash Commands](#claude-commands) | [CLI Quick Reference](#cheat-sheet) |
| [Interface](#interface--input) | [Keyboard Shortcuts](#keyboard-shortcuts) | [Vim Mode](#vim-mode) |
| [Advanced Features](#advanced-features) | [Plan Mode](#plan-mode), [Auto Mode](#auto-mode), [MCP](#mcp-integration) | [Sub Agents](#sub-agents), [Skills](#skills), [Hooks](#hooks-system) |
| [Security](#security--permissions) | [Security & Permissions](#security--permissions) | [Dangerous Mode](#dangerous-mode), [Best Practices](#security-best-practices-main) |
| [Automation](#automation--integration) | [Automation & Scripting](#automation--scripting-with-claude-code) | [PR Review](#auto-pr-review-inline-comments), [Issue Triage](#issue-triage-suggest-labels--severity) |
| [Help](#help--troubleshooting) | [Troubleshooting](#help--troubleshooting) | [Best Practices](#best-practices), [Monitoring](#monitoring--alerting) |
| [Third-Party Integrations](#third-party-integrations) | [DeepSeek Integration](#deepseek-integration) | [Provider Setup Examples](#provider-setup-examples) |

<details>
<summary>Full content map</summary>

- **[Getting Started](#getting-started)**
  - [Quick Start](#quick-start)
  - [System Requirements](#system-requirements)
  - [Initial Setup](#initial-setup)

- **[Configuration & Environment](#configuration--environment)**
  - [Environment Variables](#environment-variables)
  - [Configuration Files](#configuration-files)

- **[Commands & Usage](#commands--usage)**
  - [Slash Command Reference](#claude-commands)
  - [CLI Quick Reference](#cheat-sheet)

- **[Interface & Input](#interface--input)**
  - [Keyboard Shortcuts](#keyboard-shortcuts)
  - [Vim Mode](#vim-mode)

- **[Advanced Features](#advanced-features)**
  - [Thinking Mode](#thinking-keywords)
  - [Effort Levels](#effort-levels)
  - [Fast Mode](#fast-mode)
  - [Auto Mode](#auto-mode)
  - [Plan Mode](#plan-mode)
  - [Background Tasks](#background-tasks)
  - [Workflows & Scheduling](#workflows--scheduling)
  - [Remote Sessions](#remote-sessions)
  - [Claude in Chrome](#claude-in-chrome)
  - [Sandbox Mode](#sandbox-mode)
  - [LSP Tool](#lsp-tool)
  - [Sub Agents](#sub-agents)
  - [Agent Teams](#agent-teams)
  - [Skills](#skills)
  - [Plugin System](#plugin-system)
  - [Worktree Isolation](#worktree-isolation)
  - [Native Installer](#native-installer)
  - [Authentication CLI](#claude-auth)
  - [Agent Management CLI](#claude-agents-cli)
  - [Remote Control](#remote-control)
  - [Managed Settings](#managed-settings)
  - [Model Updates](#model-updates)
  - [Theming & Customization](#theming--customization)
  - [Code Review](#code-review)
  - [Insights](#insights)
  - [MCP Integration](#mcp-integration)
  - [Hooks System](#hooks-system)

- **[Security & Permissions](#security--permissions)**
  - [Dangerous Mode](#dangerous-mode)
  - [Security Best Practices](#security-best-practices-main)

- **[Automation & Integration](#automation--integration)**
  - [Automation & Scripting](#automation--scripting-with-claude-code)
  - [Auto PR Review](#auto-pr-review-inline-comments)
  - [Issue Triage](#issue-triage-suggest-labels--severity)

- **[Help & Troubleshooting](#help--troubleshooting)**
  - [Installation Issues](#installation--nodejs-issues)
  - [MCP Issues](#mcp-model-context-protocol-issues)
  - [Best Practices](#best-practices)
  - [Monitoring & Alerting](#monitoring--alerting)

- **[Third-Party Integrations](#third-party-integrations)**
  - [Provider Setup Examples](#provider-setup-examples)
  - [DeepSeek Integration](#deepseek-integration)

</details>

---

<h1 id="getting-started">Getting Started</h1>

**Enable sound alerts when claude completes the task:**

> <kbd>claude config set --global preferredNotifChannel terminal_bell</kbd>

<h2 id="quick-start">Quick Start</h2>

> [!TIP]
> **Send <mark>claude</mark> or <mark>npx claude</mark> in terminal to start the interface**
>
> **Go to [Help & Troubleshooting](#help--troubleshooting) to fix issues...**

```C
# Native Installer (preferred — no Node.js required) ⭐️
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Windows
/* Via CMD (native)      */ curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
/* Via Powershell        */ irm https://claude.ai/install.ps1 | iex
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# macOS / Linux / WSL
/* Via Terminal          */ curl -fsSL https://claude.ai/install.sh | bash
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Arch
/* Via Terminal          */ yay -S claude-code*/
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Alternative (npm) — useful when your environment already standardizes on Node.js
# Requires Node.js 18+
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Windows
/* Via CMD (npm)         */ npm install -g @anthropic-ai/claude-code
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# macOS
/* Via Terminal          */ brew install node && npm install -g @anthropic-ai/claude-code
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Linux
/* Via Terminal          */ sudo apt update && sudo apt install -y nodejs npm
/* Via Terminal          */ npm install -g @anthropic-ai/claude-code
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# WSL/GIT
/* Via Terminal          */ npm install -g @anthropic-ai/claude-code
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Docker
/* Windows (CMD)         */ docker run -it --rm -v "%cd%:/workspace" -e ANTHROPIC_API_KEY="sk-your-key" node:20-slim bash -lc "npm i -g @anthropic-ai/claude-code && cd /workspace && claude"
/* macOS/Linux (bash/zsh)*/ docker run -it --rm -v "$PWD:/workspace" -e ANTHROPIC_API_KEY="sk-your-key" node:20-slim bash -lc 'npm i -g @anthropic-ai/claude-code && cd /workspace && claude'
/* No bash Fallback      */ docker run -it --rm -v "$PWD:/workspace" -e ANTHROPIC_API_KEY="sk-your-key" node:20-slim sh -lc 'npm i -g @anthropic-ai/claude-code && cd /workspace && claude'
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Check if claude is installed correctly
/* Linux                 */ which claude
/* Windows               */ where claude
/* Universal             */ claude --version
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Common Management
/*claude config          */ Configure settings
/*claude mcp list        */ Setup MCP servers, you can also replace "list" with add/remove
/*claude agents          */ Open the agent/session dashboard
/*claude update          */ Run a manual update check
```

---

> [!Tip]
> <ins>**Open Project Via Terminal Into VS Code / Cursor**</ins>
>
> ### $ - <kbd>cd /path/to/project</kbd>
>
> ### $ - <kbd>code .</kbd>
>
> **Make sure you have the <mark>(Claude Code extension)</mark> installed in your VS Code / Cursor**

---

<h2 id="system-requirements">System Requirements</h2>

> - OS: macOS 10.15+, Ubuntu 20.04+/Debian 10+, or Windows 10/11 or WSL

> - Hardware: 4GB RAM minimum 8GB+ recommended

> - Software: Git 2.23+ is optional for PR/worktree workflows. Node.js 18+ is only required for npm-based installation; the native installer bundles its own runtime.

> - Internet: Connection for API calls

---

<h2 id="initial-setup">Initial Setup</h2>

> [!Tip]
> **Find API key from [Anthropic Console](https://console.anthropic.com)**
>
> **Do NOT commit real keys use git-ignored files, OS key stores, or secret managers**

```C
# Universal
/* Authenticate via Anthropic account     */ claude auth login
/* Authenticate via Console/API billing   */ claude auth login --console
/* Switch accounts inside Claude          */ /login
----------------------------------------------------------------------------------------------------------------------------------
# Windows
/* Set-api-key        */ set ANTHROPIC_API_KEY=sk-your-key-here-here
/* cmd-masked-check   */ echo OK: %ANTHROPIC_API_KEY:~0,8%***
/* Set-persistent-key */ setx ANTHROPIC_API_KEY "sk-your-key-here-here"
/* cmd-unset-key      */ set ANTHROPIC_API_KEY=
----------------------------------------------------------------------------------------------------------------------------------
# Linux
/* Set-api-key        */ export ANTHROPIC_API_KEY="sk-your-key-here-here"
/* masked-check       */ echo "OK: ${ANTHROPIC_API_KEY:0:8}***"
/* remove-session     */ unset ANTHROPIC_API_KEY
----------------------------------------------------------------------------------------------------------------------------------
# Powershell
/* ps-session         */ $env:ANTHROPIC_API_KEY = "sk-your-key-here-here"
/* ps-masked-check    */ "OK: $($env:ANTHROPIC_API_KEY.Substring(0,8))***"
/* ps-persist         */ [Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY","sk-your-key-here-here","User")
/* ps-rotate          */ $env:ANTHROPIC_API_KEY = "sk-new-key"
/* ps-remove          */ Remove-Item Env:\ANTHROPIC_API_KEY
----------------------------------------------------------------------------------------------------------------------------------
# Other...
# persist-bash/*      */ echo 'export ANTHROPIC_API_KEY="sk-your-key-here-here"' >> ~/.bashrc && source ~/.bashrc
# persist-zsh /*      */ echo 'export ANTHROPIC_API_KEY="sk-your-key-here-here"' >> ~/.zshrc  && source ~/.zshrc
# persist-fish/*      */ fish -lc 'set -Ux ANTHROPIC_API_KEY sk-your-key-here-here'
----------------------------------------------------------------------------------------------------------------------------------
```

---

<h1 id="configuration--environment">Configuration & Environment</h1>

<h2 id="environment-variables">Environment Variables</h2>

> **You can also set any of these in settings.json under the "env" key for automatic application.**

> [!Important]
> **Windows Users replace <kbd>export</kbd> with <kbd>set</kbd> or <kbd>setx</kbd> for perm**

```bash
# Environment toggles (put in ~/.bashrc or ~/.zshrc)
export ANTHROPIC_API_KEY="sk-your-key-here-here"      # API key sent as X-Api-Key header (interactive usage: /login)
export ANTHROPIC_AUTH_TOKEN="my-auth-token"           # Custom Authorization header; Claude adds "Bearer " prefix automatically
export ANTHROPIC_CUSTOM_HEADERS="X-Trace-Id: 12345"   # Extra request headers (format: "Name: Value")

export ANTHROPIC_MODEL="sonnet"                                  # Custom model name or alias to use
export ANTHROPIC_DEFAULT_SONNET_MODEL="sonnet"                   # Default Sonnet alias or pinned Sonnet model ID
export ANTHROPIC_DEFAULT_OPUS_MODEL="opus"                       # Default Opus alias or pinned Opus model ID
export ANTHROPIC_SMALL_FAST_MODEL="haiku-model"                  # Haiku-class model for background tasks (placeholder)
export ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION="REGION"            # Override AWS region for the small/fast model on Bedrock (placeholder)

export AWS_BEARER_TOKEN_BEDROCK="bedrock_..."         # Amazon Bedrock API key/token for authentication

export BASH_DEFAULT_TIMEOUT_MS=60000                  # Default timeout (ms) for long-running bash commands
export BASH_MAX_TIMEOUT_MS=300000                     # Maximum timeout (ms) allowed for long-running bash commands
export BASH_MAX_OUTPUT_LENGTH=20000                   # Max characters in bash outputs before middle-truncation

export CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1     # (0 or 1) return to original project dir after each Bash command
export CLAUDE_BASH_NO_LOGIN=1                         # Force BashTool to skip login shell startup files
export CLAUDE_CODE_API_KEY_HELPER_TTL_MS=600000       # Interval (ms) to refresh creds when using apiKeyHelper
export CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL=1            # (0 or 1) skip auto-installation of IDE extensions
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096             # Max number of output tokens for most requests

export CLAUDE_CODE_USE_BEDROCK=1                      # (0 or 1) use Amazon Bedrock
export CLAUDE_CODE_USE_VERTEX=0                       # (0 or 1) use Google Vertex AI
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=0                # (0 or 1) skip AWS auth for Bedrock (e.g., via LLM gateway)
export CLAUDE_CODE_SKIP_VERTEX_AUTH=0                 # (0 or 1) skip Google auth for Vertex (e.g., via LLM gateway)

export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=0     # (0 or 1) disable nonessential traffic (equivalent to DISABLE_* below)
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=0           # (0 or 1) disable automatic terminal title updates

export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1         # (0 or 1) enable agent teams research preview
export CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 # (0 or 1) load CLAUDE.md from --add-dir paths
export CLAUDE_CODE_ENABLE_TASKS=false                 # Set to "false" to disable the task system

export DISABLE_AUTOUPDATER=0                          # (0 or 1) disable automatic updates (overrides autoUpdates setting)
export DISABLE_BUG_COMMAND=0                          # (0 or 1) disable the /bug command
export DISABLE_COST_WARNINGS=0                        # (0 or 1) disable cost warning messages
export DISABLE_ERROR_REPORTING=0                      # (0 or 1) opt out of Sentry error reporting
export DISABLE_NON_ESSENTIAL_MODEL_CALLS=0            # (0 or 1) disable model calls for non-critical paths
export DISABLE_TELEMETRY=0                            # (0 or 1) opt out of Statsig telemetry

export HTTP_PROXY="http://proxy:8080"                 # HTTP proxy server URL
export HTTPS_PROXY="https://proxy:8443"               # HTTPS proxy server URL

export MAX_THINKING_TOKENS=0                          # (0 or 1 to turn off/on) force a thinking budget for the model
export MCP_TIMEOUT=120000                             # MCP server startup timeout (ms)
export MCP_TOOL_TIMEOUT=60000                         # MCP tool execution timeout (ms)
export MAX_MCP_OUTPUT_TOKENS=25000                    # Max tokens allowed in MCP tool responses (default 25000)

export USE_BUILTIN_RIPGREP=0                          # (0 or 1) set 0 to use system-installed rg instead of bundled one

# Vertex AI region overrides follow VERTEX_REGION_CLAUDE_<MODEL_FAMILY>.
export VERTEX_REGION_CLAUDE_3_5_HAIKU="REGION"        # 3.x family example
export VERTEX_REGION_CLAUDE_4_6_SONNET="REGION"       # Sonnet family example
export VERTEX_REGION_CLAUDE_4_8_OPUS="REGION"         # Opus family example

# -- Session and runtime controls ---------------------------------------------
export CLAUDE_CODE_SIMPLE=1                            # Minimal mode: disables MCP tools, attachments, hooks, CLAUDE.md, and skills
export CLAUDE_CODE_DISABLE_1M_CONTEXT=1                # Disable 1 M-token context window (use default shorter context)
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1          # Disable background tasks entirely
export CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1        # Opt out of experimental beta features
export CLAUDE_CODE_AUTO_CONNECT_IDE=false              # Disable automatic IDE connection on startup
export CLAUDE_CODE_TMPDIR="/custom/tmp"                # Override the temp directory Claude Code uses
export CLAUDE_CODE_SHELL="/bin/zsh"                    # Override shell detection (force a specific shell)
export CLAUDE_CODE_SHELL_PREFIX="command-wrapper"      # Prefix/wrap every shell command Claude runs
export CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS=50000   # Override max output tokens for the Read tool
export CLAUDE_CODE_PROXY_RESOLVES_HOSTS=true           # Let the HTTP/HTTPS proxy handle DNS resolution
export CLAUDE_CODE_EXIT_AFTER_STOP_DELAY=30000         # Auto-exit SDK mode after idle for N ms
export CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS=30000         # Timeout (ms) for plugin git operations
export CLAUDE_CODE_ACCOUNT_UUID="uuid"                 # Override account UUID (SDK / automation flows)
export CLAUDE_CODE_USER_EMAIL="user@example.com"       # Override user email (SDK / automation flows)
export CLAUDE_CODE_ORGANIZATION_UUID="uuid"            # Override organization UUID (SDK / automation flows)
export ENABLE_CLAUDEAI_MCP_SERVERS=false               # Opt out from claude.ai-synced MCP servers
export FORCE_AUTOUPDATE_PLUGINS=1                      # Allow plugin auto-update even when main updater is disabled
export IS_DEMO=1                                       # Demo mode — hides email/org from the UI
export NO_PROXY="localhost,127.0.0.1"                  # Bypass proxy for specified hosts (comma-separated)

# -- Provider, terminal, and telemetry controls --------------------------------
export CLAUDE_CODE_ENABLE_AUTO_MODE=1                  # Enable auto mode on Bedrock, Vertex, and Foundry for Opus 4.7/4.8
export CLAUDE_CODE_USE_POWERSHELL_TOOL=1               # Enable PowerShell tool where available; Windows provider sessions may default to it
export CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1 # Opt out of PowerShell -ExecutionPolicy Bypass behavior
export CLAUDE_CODE_NO_FLICKER=1                        # Prefer flicker-free alternate-screen rendering where supported
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1    # Let compatible gateways populate the model picker from /v1/models
export CLAUDE_CODE_FORCE_SYNC_OUTPUT=1                 # Force synchronized terminal output when auto-detection misses support
export CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1       # Let package-manager installs run background upgrades where supported
export ENABLE_PROMPT_CACHING_1H=true                   # Opt in to 1-hour prompt cache TTL when your provider supports it
export OTEL_LOG_TOOL_DETAILS=1                         # Include tool parameters in tool_decision telemetry events
export OTEL_METRICS_INCLUDE_ENTRYPOINT=true            # Include session entrypoint on OpenTelemetry metrics
```

<h2 id="global-config-options">Global Config Options</h2>

```bash
claude config set -g theme dark                               # Theme: dark | light | light-daltonized | dark-daltonized
claude config set -g preferredNotifChannel iterm2_with_bell   # Notification channel: iterm2 | iterm2_with_bell | terminal_bell | notifications_disabled
claude config set -g autoUpdates true                         # Auto-download & install updates (applied on restart)
claude config set -g verbose true                             # Show full bash/command outputs

claude config set -g attribution false                        # Omit "co-authored-by Claude" in git commits/PRs
claude config set -g forceLoginMethod claudeai                 # Restrict login flow: claudeai | console
claude config set -g model "sonnet"                          # Default model override; use a full model ID only when pinning
claude config set -g statusLine '{"type":"command","command":"~/.claude/statusline.sh"}'  # Custom status line

claude config set -g enableAllProjectMcpServers true              # Auto-approve all MCP servers from .mcp.json
claude config set -g enabledMcpjsonServers '["memory","github"]'  # Approve specific MCP servers
claude config set -g disabledMcpjsonServers '["filesystem"]'      # Reject specific MCP servers
```

<h2 id="configuration-files">Configuration Files</h2>

**(Memory type) Claude Code offers four memory locations in a hierarchical structure, each serving a different purpose:**

| Memory Type                | Location                                                                                                                                                | Purpose                                             | Use Case Examples                                                    | Shared With                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------- |
| **Enterprise policy**      | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br />Linux: `/etc/claude-code/CLAUDE.md`<br />Windows: `C:\ProgramData\ClaudeCode\CLAUDE.md` | Organization-wide instructions managed by IT/DevOps | Company coding standards, security policies, compliance requirements | All users in organization       |
| **Project memory**         | `./CLAUDE.md`                                                                                                                                           | Team-shared instructions for the project            | Project architecture, coding standards, common workflows             | Team members via source control |
| **User memory**            | `~/.claude/CLAUDE.md`                                                                                                                                   | Personal preferences for all projects               | Code styling preferences, personal tooling shortcuts                 | Just you (all projects)         |
| **Project memory (local)** | `./CLAUDE.local.md`                                                                                                                                     | Personal project-specific preferences (git-ignored) | Your sandbox URLs, preferred test data, personal overrides           | Just you (current project)      |
| **Project rules**          | `.claude/rules/*.md`                                                                                                                                    | Modular project rules (loaded alongside CLAUDE.md)  | Linting rules, API conventions, per-directory standards              | Team members via source control |

> All memory files are automatically loaded into Claude Code's context when launched. Files higher in the hierarchy take precedence and are loaded first, providing a foundation that more specific memories build upon.

#### `.claude/rules/` Directory

The `.claude/rules/` directory lets you break project instructions into separate Markdown files instead of one large `CLAUDE.md`. Every `*.md` file inside is automatically loaded into context alongside `CLAUDE.md`. This is useful for:

- **Modular organization**: Separate concerns (e.g., `api-conventions.md`, `testing-rules.md`)
- **Per-directory overrides**: Nested `rules/` directories can apply scoped rules
- **Team collaboration**: Different team members can own different rule files via PR review

#### Auto-Memory

Claude can save useful working context during your sessions, such as project conventions, tooling preferences, and architectural decisions it observes while helping you. Use `/memory` to inspect, edit, or remove saved memories.

Auto-memory is most useful for context you would otherwise repeat across sessions:

- Preferred build, test, and lint commands
- Local conventions that are not obvious from code alone
- Architecture decisions that influence future edits
- Team preferences that should shape how Claude proposes changes

Keep durable team rules in `CLAUDE.md` or `.claude/rules/`. Treat auto-memory as helpful working context, not as the only source of truth.

---

<h1 id="commands--usage">Commands & Usage</h1>

<h2 id="claude-commands">Slash Command Reference</h2>

| Command                   | Purpose                                                                                                  |
| :------------------------ | :------------------------------------------------------------------------------------------------------- |
| `/add-dir`                | Add additional working directories                                                                       |
| `/agents`                 | Manage custom AI subagents for specialized tasks                                                         |
| `/branch`                 | Branch or fork the current conversation into a separate session                                          |
| `/bug`                    | Report bugs (sends conversation to Anthropic)                                                            |
| `/clear`                  | Clear conversation history                                                                               |
| `/compact [instructions]` | Compact conversation with optional focus instructions                                                    |
| `/config`                 | Open the Settings interface (Config tab)                                                                 |
| `/context`                | Visualize current context usage as a colored grid                                                        |
| `/copy`                   | Copy conversation content to clipboard                                                                   |
| `/code-review [effort]`   | Run correctness-focused code review; use `--fix` to apply findings or `--comment` for PR comments        |
| `/color`                  | Set or randomize the current session accent color                                                        |
| `/debug`                  | Troubleshoot current session and diagnose issues                                                         |
| `/doctor`                 | Checks the health of your Claude Code installation                                                       |
| `/effort`                 | Pick reasoning effort for the current model/session                                                      |
| `/exit`                   | Exit the REPL                                                                                            |
| `/export [filename]`      | Export the current conversation to a file or clipboard                                                   |
| `/fast`                   | Toggle fast mode for accelerated Opus responses where available                                          |
| `/goal`                   | Set a completion condition so Claude keeps working across turns until it is met                          |
| `/help`                   | Get usage help                                                                                           |
| `/init`                   | Initialize project with CLAUDE.md guide                                                                  |
| `/insights`               | Generate an interactive HTML report analyzing your coding habits                                         |
| `/keybindings`            | Configure custom keyboard shortcuts                                                                      |
| `/login`                  | Switch Anthropic accounts                                                                                |
| `/loop`                   | Schedule a recurring prompt or slash command                                                             |
| `/logout`                 | Sign out from your Anthropic account                                                                     |
| `/mcp`                    | Manage MCP server connections and OAuth authentication                                                   |
| `/memory`                 | Edit CLAUDE.md memory files                                                                              |
| `/model`                  | Select or change the AI model                                                                            |
| `/permissions`            | View or update tool permissions                                                                          |
| `/plan`                   | Enter plan mode directly from the prompt                                                                 |
| `/plugins`                | Manage plugins (install, enable, disable, marketplace)                                                   |
| `/pr_comments`            | View pull request comments                                                                               |
| `/release-notes`          | Open the built-in release notes view                                                                     |
| `/rename <name>`          | Rename the current session for easier identification                                                     |
| `/resume [session]`       | Resume a conversation by ID or name, or open session picker                                              |
| `/rules`                  | View and manage `.claude/rules/` directory (modular project rules)                                       |
| `/rewind`                 | Rewind the conversation and/or code to a previous point                                                  |
| `/sandbox`                | View sandbox dependency status with installation instructions                                            |
| `/scroll-speed`           | Tune mouse wheel scroll speed with a live preview                                                        |
| `/settings`               | Open Settings interface (alias for `/config`)                                                            |
| `/simplify`               | Run cleanup-only review for reuse, simplification, efficiency, and altitude                              |
| `/status`                 | Open Settings interface (Status tab) showing version, model, account                                     |
| `/statusline`             | Set up Claude Code's status line UI                                                                      |
| `/tasks`                  | List and manage background tasks                                                                         |
| `/teleport`               | Resume a remote session from claude.ai (subscribers only)                                                |
| `/terminal-setup`         | Install Shift+Enter key binding for newlines (iTerm2, VS Code, Kitty, Alacritty, Zed, Warp, and WezTerm) |
| `/remote-env`             | Configure remote environment settings                                                                    |
| `/theme`                  | Change the color theme                                                                                   |
| `/todos`                  | List current TODO items                                                                                  |
| `/ultrareview [target]`   | Run comprehensive cloud code review with parallel multi-agent analysis                                   |
| `/usage`                  | Show plan usage limits and rate limit status (subscription plans)                                        |
| `/usage-credits`          | Enable or inspect usage credits for higher-throughput modes                                              |
| `/workflows`              | View dynamic workflow runs and background orchestration status                                           |
| `/batch`                  | Run batch operations on multiple files (bundled skill)                                                   |

<h2 id="command-line-flags">Command Line Flags</h2>

| Flag / Command                                       | Description                                                                                                                                                  | Example                                                                                |
| :--------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- |
| `-d, --debug`                                        | Enable debug mode (shows detailed debug output).                                                                                                             | `claude -d -p "query"`                                                                 |
| `--include-partial-messages`                         | partial message streaming support via CLI flag                                                                                                               | `claude -p "query" --include-partial-messages`                                         |
| `--verbose`                                          | Override verbose mode setting from config (shows expanded logging / turn-by-turn output).                                                                    | `claude --verbose`                                                                     |
| `-p, --print`                                        | Print response and exit (useful for piping output).                                                                                                          | `claude -p "query"`                                                                    |
| `--output-format <format>`                           | Output format (only works with `--print`): `text` (default), `json` (single result), or `stream-json` (realtime streaming).                                  | `claude -p "query" --output-format json`                                               |
| `--input-format <format>`                            | Input format (only works with `--print`): `text` (default) or `stream-json` (realtime streaming input).                                                      | `claude -p --output-format stream-json --input-format stream-json`                     |
| `--replay-user-messages`                             | Re-emit user messages from stdin back to stdout for acknowledgment — **only works with** `--input-format=stream-json` **and** `--output-format=stream-json`. | `claude --input-format stream-json --output-format stream-json --replay-user-messages` |
| `--allowedTools`, `--allowed-tools <tools...>`       | Comma/space-separated list of tool names to allow (e.g. `"Bash(git:*) Edit"`).                                                                               | `--allowed-tools "Bash(git:*)" Edit"`                                                  |
| `--disallowedTools`, `--disallowed-tools <tools...>` | Comma/space-separated list of tool names to deny (e.g. `"Bash(git:*) Edit"`).                                                                                | `--disallowed-tools "Edit"`                                                            |
| `--mcp-config <configs...>`                          | Load MCP servers from JSON files or strings (space-separated).                                                                                               | `claude --mcp-config ./mcp-servers.json`                                               |
| `--strict-mcp-config`                                | Only use MCP servers from `--mcp-config`, ignoring other MCP configurations.                                                                                 | `claude --mcp-config ./a.json --strict-mcp-config`                                     |
| `--append-system-prompt <prompt>`                    | Append a system prompt to the default system prompt (useful in print mode).                                                                                  | `claude -p --append-system-prompt "Do X then Y"`                                       |
| `--permission-mode <mode>`                           | Permission mode for the session (choices include `acceptEdits`, `auto`, `bypassPermissions`, `default`, `plan`).                                             | `claude --permission-mode plan`                                                        |
| `--permission-prompt-tool <tool>`                    | Specify an MCP tool to handle permission prompts in non-interactive mode.                                                                                    | `claude -p --permission-prompt-tool mcp_auth_tool "query"`                             |
| `--fallback-model <model>`                           | Enable automatic fallback to a specified model when the default is overloaded (note: only works with `--print` per help).                                    | `claude -p --fallback-model claude-haiku-20240307 "query"`                             |
| `--model <model>`                                    | Model for the current session. Accepts aliases like `sonnet`/`opus` or a full model ID when pinning.                                                         | `claude --model sonnet`                                                                |
| `--settings <file-or-json>`                          | Load additional settings from a JSON file or a JSON string.                                                                                                  | `claude --settings ./settings.json`                                                    |
| `--add-dir <directories...>`                         | Additional directories to allow tool access to.                                                                                                              | `claude --add-dir ../apps ../lib`                                                      |
| `--ide`                                              | Automatically connect to an IDE on startup if exactly one valid IDE is available.                                                                            | `claude --ide`                                                                         |
| `-c, --continue`                                     | Continue the most recent conversation in the current directory.                                                                                              | `claude --continue`                                                                    |
| `-r, --resume [sessionId]`                           | Resume a conversation; provide a session ID or interactively select one.                                                                                     | `claude -r "abc123"`                                                                   |
| `--session-id <uuid>`                                | Use a specific session ID for the conversation (must be a valid UUID).                                                                                       | `claude --session-id 123e4567-e89b-12d3-a456-426614174000`                             |
| `--agents <json>`                                    | Define custom subagents dynamically via JSON (see subagent docs for format).                                                                                 | `claude --agents '{"reviewer":{"description":"Reviews code","prompt":"..."}}'`         |
| `--agent <name>`                                     | Specify a specific agent for the current session.                                                                                                            | `claude --agent my-custom-agent`                                                       |
| `--bg`                                               | Start or continue work as a background session that can be viewed from `claude agents`.                                                                      | `claude --bg "fix failing tests"`                                                      |
| `--bg --exec <command>`                              | Run a shell command as an attachable background session.                                                                                                     | `claude --bg --exec "npm test"`                                                        |
| `--name <label>`                                     | Name a background or remote session for easier identification.                                                                                               | `claude --bg --name nightly-check "run checks"`                                       |
| `--chrome`                                           | Enable Chrome browser integration for web automation and testing.                                                                                            | `claude --chrome`                                                                      |
| `--no-chrome`                                        | Disable Chrome browser integration for this session.                                                                                                         | `claude --no-chrome`                                                                   |
| `--remote`                                           | Create a new web session on claude.ai with the provided task description.                                                                                    | `claude --remote "Fix the login bug"`                                                  |
| `--teleport`                                         | Resume a web session in your local terminal.                                                                                                                 | `claude --teleport`                                                                    |
| `--fork-session`                                     | When resuming, create a new session ID instead of reusing the original.                                                                                      | `claude --resume abc123 --fork-session`                                                |
| `--json-schema <schema>`                             | Get validated JSON output matching a JSON Schema after agent completes (print mode only).                                                                    | `claude -p --json-schema '{"type":"object",...}' "query"`                              |
| `--max-budget-usd <amount>`                          | Maximum dollar amount to spend on API calls before stopping (print mode only).                                                                               | `claude -p --max-budget-usd 5.00 "query"`                                              |
| `--max-turns <n>`                                    | Limit the number of agentic turns (print mode only). Exits with error when limit reached.                                                                    | `claude -p --max-turns 3 "query"`                                                      |
| `--betas <headers>`                                  | Beta headers to include in API requests (API key users only).                                                                                                | `claude --betas interleaved-thinking`                                                  |
| `--tools <tools>`                                    | Restrict which built-in tools Claude can use. Use "" to disable all, "default" for all, or specific tool names.                                              | `claude --tools "Bash,Edit,Read"`                                                      |
| `--system-prompt <prompt>`                           | Replace the entire system prompt with custom text (works in interactive and print modes).                                                                    | `claude --system-prompt "You are a Python expert"`                                     |
| `--system-prompt-file <file>`                        | Load system prompt from a file, replacing the default prompt (print mode only).                                                                              | `claude -p --system-prompt-file ./custom-prompt.txt "query"`                           |
| `--append-system-prompt-file <file>`                 | Load additional system prompt text from a file and append to default (print mode only).                                                                      | `claude -p --append-system-prompt-file ./extra-rules.txt "query"`                      |
| `--plugin-dir <dir>`                                 | Load plugins from directories for this session only (repeatable).                                                                                            | `claude --plugin-dir ./my-plugins`                                                     |
| `--setting-sources <sources>`                        | Comma-separated list of setting sources to load (user, project, local).                                                                                      | `claude --setting-sources user,project`                                                |
| `--no-session-persistence`                           | Disable session persistence so sessions are not saved to disk (print mode only).                                                                             | `claude -p --no-session-persistence "query"`                                           |
| `--disable-slash-commands`                           | Disable all skills and slash commands for this session.                                                                                                      | `claude --disable-slash-commands`                                                      |
| `--dangerously-skip-permissions`                     | Bypass all permission checks (only for trusted sandboxes).                                                                                                   | `claude --dangerously-skip-permissions`                                                |
| `--worktree`, `-w`                                   | Start in an isolated git worktree; `worktree.baseRef` controls whether it branches from fresh remote state or local HEAD.                                    | `claude -w "implement feature"`                                                        |
| `--from-pr <url>`                                    | Start a session from a pull request URL.                                                                                                                     | `claude --from-pr https://org/repo/pull/123`                                |
| `--init`                                             | Trigger the Setup hook event.                                                                                                                                | `claude --init`                                                                        |
| `--init-only`                                        | Run Setup hooks and exit.                                                                                                                                    | `claude --init-only`                                                                   |
| `--maintenance`                                      | Run Setup hooks in maintenance mode.                                                                                                                         | `claude --maintenance`                                                                 |
| `-v, --version`                                      | Show the installed `claude` CLI version.                                                                                                                     | `claude --version`                                                                     |
| `-h, --help`                                         | Display help / usage.                                                                                                                                        | `claude --help`                                                                        |

> The `--output-format json` flag is particularly useful for scripting and automation, allowing you to parse Claude's responses programmatically.

<h2 id="cheat-sheet">CLI Quick Reference & Configuration Examples</h2>

```md
## Claude Cheat Sheet

# Start and resume

claude # Start interactive REPL
claude "explain this project" # Start REPL seeded with a prompt
claude -p "summarize README.md" # Non-interactive print mode (SDK-backed)
cat logs.txt | claude -p "explain" # Pipe input to Claude and exit
claude -c # Continue most recent conversation
claude -r "<session-id>" "finish this" # Resume by ID or name
claude --model sonnet # Pick the Sonnet alias for this run
claude --model opus # Pick the Opus alias for harder tasks

# Install, update, and auth

claude update # Manually update Claude Code
claude doctor # Diagnose install/version & setup
claude install # Start the native binary installer
claude migrate-installer # Switch from global npm to the native installer
claude auth login # Log in to your Anthropic account
claude auth status # Check authentication status
claude auth logout # Log out

# Background and remote sessions

claude agents # Open the live session dashboard: running, blocked, completed
claude agents --json # Scriptable JSON list of live/background sessions
claude --bg "run the integration suite and summarize failures" # Start a background session
claude --bg --exec "npm test" # Run a shell command as an attachable background session
claude remote-control # Start remote-control mode for external tooling
claude --remote "Fix the bug" # Create web session on claude.ai
claude --teleport # Resume web session locally

# Config essentials

claude config # Interactive config wizard
claude config set model "sonnet" # Override default model for this project
claude config set attribution false # Disable "co-authored-by Claude" byline in git/PRs
claude config set enableAllProjectMcpServers true # Auto-approve all MCP servers from .mcp.json
claude config set defaultMode "acceptEdits" # Set default permission mode
claude config set worktree.baseRef "head" # Use local HEAD instead of origin/default for new worktrees
claude config set -g autoUpdates false # Turn off automatic updates globally
claude config set -g theme dark # Theme: dark | light | light-daltonized | dark-daltonized

# MCP essentials

claude mcp # Launch MCP wizard / configure MCP servers
claude mcp list # List configured MCP servers
claude mcp get <name> # Show details for a server
claude mcp add <name> <command> [args...] # Add local stdio server
claude mcp add --transport http <name> <url> # Add remote HTTP server
claude mcp reset-project-choices # Reset approvals for project .mcp.json servers
claude mcp serve # Run Claude Code itself as an MCP stdio server

# High-value flags

claude --add-dir ../apps ../lib # Add additional working directories
claude --allowedTools "Bash(git log:\*)" "Read" # Allow listed tools without permission prompts
claude --disallowedTools "Edit" # Disallow listed tools without permission prompts
claude -p "query" --output-format json --input-format stream-json # Control IO formats for scripting
claude --verbose # Verbose logging (turn-by-turn)
claude --dangerously-skip-permissions # Skip permission prompts (use with caution)
claude --permission-mode plan # Start in plan mode (read-only analysis)
claude --max-turns 3 -p "query" # Limit agentic turns (print mode only)
claude --json-schema '{"type":"object"}' -p "query" # Get validated JSON output
claude --chrome # Enable Chrome browser integration
claude --agent code-reviewer # Run this session with a named agent
claude ultrareview 123 --json # Non-interactive comprehensive review for PR/target 123

# Slash shortcuts

claude --fork-session -r abc123 # Fork instead of reusing original
claude -w "implement feature" # Start in an isolated git worktree
/rename auth-refactor # Name current session
/resume # Open session picker
/export output.md # Export conversation to file
/branch experiment-name # Branch the current conversation
/goal "all tests pass and README is updated" # Keep working until the completion condition is met
/loop 30m "check deploy health and summarize anomalies" # Schedule recurring work
/workflows # View dynamic workflows and background orchestration

# Notes: project scope is default for 'claude config'; use -g/--global for user-global settings.
# Settings precedence: Enterprise > CLI args > local project > shared project > user (~/.claude).
```

---

<h1 id="interface--input">Interface & Input</h1>

<h2 id="keyboard-shortcuts">Keyboard Shortcuts</h2>

| Shortcut                     | Description                        | Context                                  |
| :--------------------------- | :--------------------------------- | :--------------------------------------- |
| `Ctrl+C`                     | Cancel current input or generation | Standard interrupt                       |
| `Ctrl+D`                     | Exit Claude Code session           | EOF signal                               |
| `Ctrl+G`                     | Open in default text editor        | Edit your prompt or custom response      |
| `Ctrl+L`                     | Clear terminal screen              | Keeps conversation history               |
| `Ctrl+O`                     | Toggle verbose output              | Shows detailed tool usage and execution  |
| `Ctrl+R`                     | Reverse search command history     | Search through previous commands         |
| `Ctrl+V` or `Cmd+V` (iTerm2) | Paste image from clipboard         | Pastes an image or path to an image file |
| `Ctrl+B`                     | Background running tasks           | Backgrounds bash commands and agents     |
| `Ctrl+F` (press twice)       | Kill all background agents         | Two-press confirmation to stop agents    |
| `Up/Down arrows`             | Navigate command history           | Recall previous inputs                   |
| `Left/Right arrows`          | Cycle through dialog tabs          | Navigate between tabs in dialogs         |
| `Esc` + `Esc`                | Rewind the code/conversation       | Restore to a previous point              |
| `Shift+Tab` or `Alt+M`       | Toggle permission modes            | Switch between Auto-Accept, Plan, Normal |
| `Option+P` (macOS) / `Alt+P` | Switch model                       | Switch models without clearing prompt    |
| `Option+T` (macOS) / `Alt+T` | Toggle extended thinking           | Enable/disable extended thinking mode    |

<h3 id="text-editing">Text Editing</h3>

| Shortcut               | Description                  | Context                               |
| :--------------------- | :--------------------------- | :------------------------------------ |
| `Ctrl+K`               | Delete to end of line        | Stores deleted text for pasting       |
| `Ctrl+U`               | Delete entire line           | Stores deleted text for pasting       |
| `Ctrl+Y`               | Paste deleted text           | Paste text deleted with Ctrl+K/U      |
| `Alt+Y` (after Ctrl+Y) | Cycle paste history          | Cycle through previously deleted text |
| `Alt+B`                | Move cursor back one word    | Requires Option as Meta on macOS      |
| `Alt+F`                | Move cursor forward one word | Requires Option as Meta on macOS      |

<h3 id="multiline-input">Multiline Input</h3>

| Method           | Shortcut       | Context                           |
| :--------------- | :------------- | :-------------------------------- |
| Quick escape     | `\` + `Enter`  | Works in all terminals            |
| macOS default    | `Option+Enter` | Default on macOS                  |
| Terminal setup   | `Shift+Enter`  | After `/terminal-setup`           |
| Control sequence | `Ctrl+J`       | Line feed character for multiline |
| Paste mode       | Paste directly | For code blocks, logs             |

<h3 id="quick-commands">Quick Commands</h3>

| Shortcut     | Description       | Notes                                 |
| :----------- | :---------------- | :------------------------------------ |
| `/` at start | Command or skill  | See built-in commands and skills      |
| `!` at start | Bash mode         | Run commands directly, add to context |
| `@`          | File path mention | Trigger file path autocomplete        |

> [!Tip]
> **PDF Page Ranges:** Use the `pages` parameter with the Read tool for PDFs (e.g., `pages: "1-5"`). Large PDFs (>10 pages) return a lightweight reference when @-mentioned instead of being inlined.

<h2 id="vim-mode">Vim Mode</h2>

> [!Note]
> Enable vim-style editing from `/config` -> Editor mode.

<h3 id="vim-mode-switching">Vim Mode Switching</h3>

| Command | Action                      | From mode |
| :------ | :-------------------------- | :-------- |
| `Esc`   | Enter NORMAL mode           | INSERT    |
| `i`     | Insert before cursor        | NORMAL    |
| `I`     | Insert at beginning of line | NORMAL    |
| `a`     | Insert after cursor         | NORMAL    |
| `A`     | Insert at end of line       | NORMAL    |
| `o`     | Open line below             | NORMAL    |
| `O`     | Open line above             | NORMAL    |

<h3 id="vim-navigation">Vim Navigation</h3>

| Command         | Action                    |
| :-------------- | :------------------------ |
| `h`/`j`/`k`/`l` | Move left/down/up/right   |
| `w`             | Next word                 |
| `e`             | End of word               |
| `b`             | Previous word             |
| `0`             | Beginning of line         |
| `$`             | End of line               |
| `^`             | First non-blank character |
| `gg`            | Beginning of input        |
| `G`             | End of input              |

<h3 id="vim-editing">Vim Editing</h3>

| Command        | Action                  |
| :------------- | :---------------------- |
| `x`            | Delete character        |
| `dd`           | Delete line             |
| `D`            | Delete to end of line   |
| `dw`/`de`/`db` | Delete word/to end/back |
| `cc`           | Change line             |
| `C`            | Change to end of line   |
| `cw`/`ce`/`cb` | Change word/to end/back |
| `.`            | Repeat last change      |

> [!Tip]
> Configure your preferred line break behavior in terminal settings. Run `/terminal-setup` to install Shift+Enter binding for iTerm2, VS Code, Kitty, Alacritty, Zed, Warp, and WezTerm.

<h2 id="command-history">Command History</h2>

> Claude Code maintains command history for the current session:

```
* History is stored per working directory
* Cleared with `/clear` command
* Use Up/Down arrows to navigate (see keyboard shortcuts above)
* **Ctrl+R**: Reverse search through history (if supported by terminal)
* **Note**: History expansion (`!`) is disabled by default
```

---

<h1 id="advanced-features">Advanced Features</h1>

<h2 id="thinking-keywords">Thinking Keywords</h2>

> [!Note]
> **Gives Claude extra pre-answer planning time by adding ONE of these keywords to your prompt.**
> **Order (lowest → highest) token consumption**
>
> <table><tr><td>
>
> > **<kbd>think</kbd> -------------> Lowest**
>
> > **<kbd>think hard</kbd>**
>
> > **<kbd>think harder</kbd>**
>
> > **<kbd>ultrathink</kbd> --------> Highest**
>
> </td></tr></table>

<h3 id="this-makes-claude-spend-more-time">This makes Claude spend more time:</h3>

1. **Planning the solution**
2. #### breaking down steps
3. #### weighing alternatives/trade-offs
4. #### checking constraints & edge cases
   > > #### Higher levels usually increase **latency** and **token usage** pick the smallest that works.

<h5 id="thinking-examples">Examples</h5>

```md
# Small boost

claude -p "Think. Outline a plan to refactor the auth module."

# Medium boost

claude -p "Think harder. Draft a migration plan from REST to gRPC."

# Max boost

claude -p "Ultrathink. Propose a step-by-step strategy to fix flaky payment tests and add guardrails."
```

<h2 id="effort-levels">Effort Levels</h2>

Use `/effort` to tune how much reasoning the selected model applies before answering. Higher effort levels are best for planning-heavy work, deep reviews, and long-context tasks.

```bash
/effort            # Open the effort picker
/effort low        # Faster, lighter reasoning
/effort medium     # Balanced default for many tasks
/effort high       # Deeper planning and review
/effort xhigh      # Highest effort for Opus 4.8-scale hard tasks
```

Prefer the lowest effort that still solves the task: higher effort can improve planning, code review, and long-context reasoning, but it usually increases latency and token usage.

<h2 id="fast-mode">Fast Mode</h2>

> [!Note]
> **Fast Mode provides accelerated Opus responses for rapid iteration when speed matters more than maximum depth.**

**How to enable Fast Mode:**

```bash
# Enable usage credits if your plan requires it, then toggle fast mode
/usage-credits
/fast

# Or toggle during conversation
# The status bar will show when Fast Mode is active
```

**Key features:**

- **Faster responses** - Reduced latency for quick tasks
- **Opus support** - Use with Opus models where fast mode is available
- **Usage credits** - Some plans require `/usage-credits` before `/fast`
- **Visible state** - The status bar and IDE indicators show when Fast Mode is active

**When to use Fast Mode:**

- Quick code reviews and edits
- Rapid prototyping
- Simple questions and commands
- Iterative debugging

> Fast Mode trades some depth for speed. Use normal mode for complex analysis and planning tasks.

<h2 id="auto-mode">Auto Mode</h2>

Auto mode lets Claude evaluate and approve lower-risk actions automatically while still blocking or asking on higher-risk operations. It is useful for trusted development loops where repeated permission prompts slow down work.

```bash
# Enable auto mode for Bedrock, Vertex, and Foundry Opus 4.7/4.8 sessions
export CLAUDE_CODE_ENABLE_AUTO_MODE=1
```

```json
{
  "autoMode": {
    "allow": ["$defaults"],
    "soft_deny": ["$defaults"],
    "hard_deny": []
  }
}
```

Key points:

- Enable auto mode through environment and settings so the policy is visible and repeatable.
- Use `"$defaults"` in `autoMode.allow`, `autoMode.soft_deny`, or `autoMode.environment` to add rules without replacing built-ins.
- `settings.autoMode.hard_deny` blocks actions unconditionally regardless of user intent.
- Denied actions can appear in `/permissions` recent activity, where supported, so you can retry or adjust policy.

<h2 id="plan-mode">Plan Mode</h2>

> [!Note]
> **Plan Mode instructs Claude to analyze the codebase with read-only operations, perfect for exploring codebases, planning complex changes, or reviewing code safely.**

**When to use Plan Mode:**

- **Multi-step implementation**: When your feature requires making edits to many files
- **Code exploration**: When you want to research the codebase thoroughly before changing anything
- **Interactive development**: When you want to iterate on the direction with Claude

**How to enable Plan Mode:**

```bash
# Start a new session in Plan Mode
claude --permission-mode plan

# Or toggle during session with Shift+Tab
# (cycles through: Normal → Auto-Accept → Plan Mode)

# Enter plan mode from the prompt
/plan

# Run headless queries in Plan Mode
claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"
```

**Configure Plan Mode as default:**

```json
// .claude/settings.json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

---

<h2 id="background-tasks">Background Tasks</h2>

> [!Note]
> **Claude Code supports background commands and full background sessions, allowing you to continue working while long-running processes or agents execute.**

**How to use background tasks:**

| Method        | Description                                                                |
| :------------ | :------------------------------------------------------------------------- |
| Prompt Claude | Ask Claude to "run this in the background"                                 |
| `Ctrl+B`      | Move a running Bash tool invocation to background (tmux users press twice) |
| `! <command>` | In `claude agents`, start an attachable background shell session            |
| `claude --bg` | Launch a task as a background Claude session                                |

**Key features:**

- Output is buffered and can be read from the persisted background output file path
- Background tasks have unique IDs for tracking and output retrieval
- Background sessions appear in `/resume` and the `claude agents` dashboard, marked with `bg`
- Use `/tasks` to list and manage background tasks
- Use `claude agents --json` for scripts, status bars, session pickers, and tmux integrations

**Common backgrounded commands:**

- Build tools (webpack, vite, make)
- Package managers (npm, yarn, pnpm)
- Test runners (jest, pytest)
- Development servers
- Long-running processes (docker, terraform)

**Bash mode with `!` prefix:**

```bash
# Run bash commands directly without Claude interpretation
! npm test
! git status
! ls -la

# Run a command as an attachable background session
claude --bg --exec "npm test"

# Name a background session
claude --bg --name nightly-check "run the full verification suite"
```

**Disable background tasks:**

```bash
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1
```

---

<h2 id="workflows--scheduling">Workflows & Scheduling</h2>

Dynamic workflows coordinate many background agents for larger work than a single foreground turn can comfortably handle. Ask Claude to create a workflow, then use `/workflows` to inspect runs and status.

```bash
/workflows
/goal "the migration is implemented, tested, and documented"
/loop 15m "check the deployment dashboard and summarize any incidents"
```

| Feature      | Purpose                                                                                 |
| :----------- | :-------------------------------------------------------------------------------------- |
| `/workflows` | View workflow runs that orchestrate many agents in the background                       |
| `/goal`      | Give Claude a completion condition and let it continue across turns until it is reached |
| `/loop`      | Run a prompt or slash command on a recurring interval                                   |

Use workflows for broad, decomposable efforts. Use `/goal` for a single outcome that may require several turns. Use `/loop` for monitoring and scheduled checks.

---

<h2 id="remote-sessions">Remote Sessions</h2>

> [!Note]
> **For subscribers: Use `--remote` to start tasks on claude.ai and `--teleport` to resume them locally.**

**Start a remote session:**

```bash
# Create a new web session on claude.ai with task description
claude --remote "Fix the login bug"
```

**Resume a remote session:**

```bash
# Resume a web session in your local terminal
claude --teleport

# Or use the slash command
/teleport
```

---

<h2 id="claude-in-chrome">Claude in Chrome</h2>

Claude Code can control Google Chrome for browser-based tasks like testing, web scraping, and UI verification.

**Setup:**

```bash
claude --chrome                    # Launch with Chrome integration
```

**Capabilities:**

- Navigate to URLs, click elements, fill forms
- Take screenshots and analyze page content
- Execute JavaScript in the browser context
- Interact with web applications for testing

> [!NOTE]
> Requires Google Chrome installed. Claude uses the Chrome DevTools Protocol for browser control.

---

<h2 id="sandbox-mode">Sandbox Mode</h2>

Sandbox mode restricts the BashTool to run commands in an isolated environment, preventing modifications to your actual filesystem.

```bash
/sandbox              # Toggle sandbox mode on/off
```

**When sandboxed:**

- File system writes are contained
- Network access may be restricted
- Useful for testing destructive commands safely

Available on Linux and macOS. Use `claude --sandbox` to start in sandbox mode.

---

<h2 id="lsp-tool">LSP Tool (Language Server Protocol)</h2>

Claude Code integrates with language servers to provide IDE-level code intelligence:

- **Go to Definition** — Jump to where a symbol is defined
- **Find References** — Find all usages of a symbol across the codebase
- **Hover Information** — Get type information and documentation

The LSP tool activates automatically when a compatible language server is available for the current project. This enables Claude to navigate codebases more precisely than text search alone.

> Tool results exceeding 50,000 characters are automatically persisted to disk to manage context efficiently.

---

<h2 id="sub-agents">Sub Agents</h2>

> Sub‑Agents are purpose‑built helpers with their **own prompts, tools, and isolated context windows**. Treat this like a "mixture‑of‑experts" you **compose** per repo.

<h3 id="built-in-subagents">Built-in Subagents</h3>

Claude Code includes built-in subagents that Claude automatically uses when appropriate:

| Subagent            | Model        | Tools     | Purpose                                           |
| :------------------ | :----------- | :-------- | :------------------------------------------------ |
| **Explore**         | Haiku (fast) | Read-only | File discovery, code search, codebase exploration |
| **Plan**            | Configurable | Read-only | Planning complex changes without making edits     |
| **General-purpose** | Default      | Inherited | General task delegation                           |

> Claude delegates to **Explore** when it needs to search or understand a codebase without making changes, keeping exploration results out of your main conversation context.

**When to use subagents:**

> - You need high signal responses (plans, reviews, diffs) without side quests.
> - You want version‑controlled prompts and tool policies alongside the codebase.
> - You work in PR‑driven teams and want scoped edits by role.
> - The task produces verbose output you don't need in your main context.

<h3 id="each-sub-agent-has-its-own-context">Each Sub‑Agent Has Its Own Context</h3>

**Design rules for your lineup**

> - Define **one clear responsibility** per agent.
> - Keep the **minimum** tool set needed for that role.
> - Prefer **read‑only** agents for analysis/review tasks.
> - Give edit powers to as few agents as possible.

<img width="700" height="160" alt="image" src="https://user-attachments/assets/42767417-20aa-4bd4-aaf2-cfa0e515b54b" />

_Caption: Agents selection UI in the terminal._

<h3 id="configure-agents">Configure Agents</h3>

> Keep agents **in the project** so they're versioned with the repo and evolve via PRs.

<h3 id="agents-quick-start">Quick start</h3>

> Update CLI and open the agents panel/dashboard

```bash
claude update
/agents
claude agents
claude agents --json
```

`claude agents` shows running, blocked, completed, and background sessions in one place. It can launch new sessions, attach to background work, and script session lists with `--json`.

<h3 id="agent-scopes">Subagent Scopes</h3>

| Location                     | Scope                   | Priority    |
| :--------------------------- | :---------------------- | :---------- |
| `--agents` CLI flag          | Current session only    | 1 (highest) |
| `.claude/agents/`            | Current project         | 2           |
| `~/.claude/agents/`          | All your projects       | 3           |
| Plugin's `agents/` directory | Where plugin is enabled | 4 (lowest)  |

Dispatched sessions honor the `agent` field in `settings.json`. Pass `--agent <name>` to override the configured default for a specific run.

<h3 id="define-agents-via-cli">Define Agents via CLI</h3>

```bash
# Define custom subagents dynamically via JSON
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  },
  "debugger": {
    "description": "Debugging specialist for errors and test failures.",
    "prompt": "You are an expert debugger. Analyze errors, identify root causes, and provide fixes."
  },
  "background-impl": {
    "description": "Implements features in an isolated worktree in the background.",
    "prompt": "Implement the requested feature. Commit when done.",
    "isolation": "worktree",
    "background": true
  }
}'
```

<h3 id="create-your-core-agents">Create your core agents</h3>

> - **planner** (read‑only): turns features/issues into small, testable tasks; outputs a task list or plan.md.
> - **codegen** (edit‑capable): implements tasks; limited to `src/` + `tests/`.
> - **tester** (read‑only or patch‑only): writes _one_ failing test or a minimal repro.
> - **reviewer** (read‑only): leaves structured review comments; never edits.
> - **docs** (edit‑capable): updates `README.md`/`docs/` only.

**\*Policy** tip: Prefer **patch output** for edit‑capable agents so changes land through your normal Git workflow.\*

<img width="700" height="173" alt="image" src="https://user-attachments/assets/84bc80de-35b8-4ef7-9b27-f74f7d4a51f9" />

_Caption: Choose only the tools an agent truly needs (e.g., advisory vs editing access)._

<h3 id="example-prompts">Example prompts</h3>

> Keep prompts short, testable, and repo‑specific. Check them into `agents/`:

<img width="700" height="217" alt="image" src="https://user-attachments/assets/b4f92591-ff5c-4775-aec2-051f145b9616" />

_Caption: Example prompt for a **test‑coverage‑analyzer** agent._

**tester.prompt.md (sample)**

```
Role: Write a single, focused failing test for the specific scenario I describe.
Scope: Only create/modify tests under tests/. Do not change src/.
Output: A brief rationale + a unified diff or patch.
If the scenario is unclear, ask exactly one clarifying question.
```

<h3 id="expected-output">Expected output</h3>

> Your tester agent should produce a small diff or patch plus a short rationale:

<img width="700" height="273" alt="image" src="https://user-attachments/assets/839151ce-02c9-4283-a53b-9dd105802ada" />

_Caption: Example response from the **test‑coverage‑analyzer** agent._

<h3 id="subagent-frontmatter">Subagent Frontmatter Fields</h3>

Subagent files use YAML frontmatter for configuration:

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
disallowedTools: Write, Edit
model: sonnet
permissionMode: default
skills:
  - api-conventions
---

You are a code reviewer. Analyze the code and provide feedback.
```

| Field             | Required | Description                                                         |
| :---------------- | :------- | :------------------------------------------------------------------ |
| `name`            | Yes      | Unique identifier (lowercase, hyphens)                              |
| `description`     | Yes      | When Claude should delegate to this subagent                        |
| `tools`           | No       | Tools the subagent can use (inherits all if omitted)                |
| `disallowedTools` | No       | Tools to deny, removed from inherited or specified list             |
| `model`           | No       | Model: `sonnet`, `opus`, `haiku`, or `inherit` (default: sonnet)    |
| `permissionMode`  | No       | `default`, `acceptEdits`, `auto`, `bypassPermissions`, or `plan`    |
| `skills`          | No       | Skills to preload into the subagent's context                       |
| `hooks`           | No       | Lifecycle hooks scoped to this subagent                             |
| `memory`          | No       | Persistent memory scope: `user`, `project`, or `local`              |
| `isolation`       | No       | Set to `worktree` to run the agent in an isolated git worktree      |
| `background`      | No       | Set to `true` to run the agent as a background task                 |

Background and isolated agents can switch between Claude-managed worktrees with `EnterWorktree` when the session needs to move between related isolated checkouts.

<h3 id="why-this-shift-matters">Why This Shift Matters</h3>

**Operational benefits**

> - **Less context switching:** you stay in one mental mode; agents do the rest.
> - **Cleaner PRs:** narrow prompts + limited tools → smaller, reviewable diffs.
> - **Fewer regressions:** tester/reviewer agents catch gaps before merge.
> - **Repeatability:** prompts + policies live in the repo and travel with branches.

**Security & governance**

> - Limit write access by path (e.g., `src/`, `tests/`, `docs/`).
> - Favor read‑only analysis for high‑risk areas.
> - Log/commit assistant outputs as patches for auditability.

<h3 id="a-mindset-shift">A Mindset Shift</h3>

**Do**

> - Treat agents as teammates with job descriptions.
> - Start read‑only; grant write access _last_.
> - Keep prompts in version control and iterate via PR.

**Don't**

> - Ask one agent to plan, code, and test in a single turn.
> - Give blanket write permissions.
> - Accept multi‑file diffs when you asked for one test.

---

<h2 id="agent-teams">Agent Teams (Research Preview)</h2>

> [!Note]
> **Agent Teams is an experimental feature enabling multiple Claude instances to work in parallel on a shared codebase autonomously.**

**Enable Agent Teams:**

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

**Key Concepts:**

- Multiple Claude instances run in parallel on the same codebase
- Each agent can specialize in different tasks (debugging, documentation, testing, etc.)
- Agents communicate through git-based synchronization
- Enables autonomous, long-running development workflows

**Case Study: C Compiler Built by Agent Teams**

Anthropic's research team demonstrated agent teams by tasking 16 parallel Claude instances to build a C compiler from scratch. Key results:

| Metric              | Value                                  |
| :------------------ | :------------------------------------- |
| **Claude Sessions** | ~2,000                                 |
| **API Cost**        | ~$20,000                               |
| **Lines of Code**   | 100,000                                |
| **Capability**      | Compiled Linux 6.9 on x86, ARM, RISC-V |
| **Test Pass Rate**  | 99% on GCC torture test suite          |

**Lessons for Agent Teams:**

1. **Write high-quality tests** - The task verifier must be nearly perfect
2. **Design for parallelism** - Agents should be able to work independently without blocking each other
3. **Specialize agents** - Dedicate agents to specific roles (code quality, documentation, performance)
4. **Maintain context files** - Keep READMEs and progress files updated for agent orientation

> Read the full case study: [Building a C Compiler with Parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler)

---

<h2 id="skills">Skills (Custom Slash Commands)</h2>

> [!Note]
> **Skills extend what Claude can do. Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with `/skill-name`.**

<h3 id="skill-locations">Skill Locations</h3>

| Location                                 | Scope    | Description                                   |
| :--------------------------------------- | :------- | :-------------------------------------------- |
| `~/.claude/skills/<skill-name>/SKILL.md` | Personal | All your projects                             |
| `.claude/skills/<skill-name>/SKILL.md`   | Project  | This project only (commit to version control) |
| `<plugin>/skills/<skill-name>/SKILL.md`  | Plugin   | Where plugin is enabled                       |

> Project skills override personal skills with the same name. Files in `.claude/commands/` still work and support the same frontmatter.
> Plugins in `.claude/skills` directories are automatically loaded; use `/reload-skills` to re-scan skill directories without restarting the session.

<h3 id="create-skill">Create a Skill</h3>

```bash
# Create skill directory
mkdir -p ~/.claude/skills/explain-code

# Scaffold a plugin-backed skill in the current project
claude plugin init explain-code
```

Create `~/.claude/skills/explain-code/SKILL.md`:

```markdown
---
name: explain-code
description: Explains code with visual diagrams and analogies. Use when explaining how code works.
---

When explaining code, always include:

1. **Start with an analogy**: Compare the code to something from everyday life
2. **Draw a diagram**: Use ASCII art to show the flow, structure, or relationships
3. **Walk through the code**: Explain step-by-step what happens
4. **Highlight a gotcha**: What's a common mistake or misconception?
```

**Use the skill:**

```bash
# Let Claude invoke automatically
How does this code work?

# Or invoke directly
/explain-code src/auth/login.ts
```

<h3 id="skill-frontmatter">Skill Frontmatter Fields</h3>

| Field                      | Required    | Description                                                 |
| :------------------------- | :---------- | :---------------------------------------------------------- |
| `name`                     | No          | Display name for the skill (uses directory name if omitted) |
| `description`              | Recommended | What the skill does and when to use it                      |
| `argument-hint`            | No          | Hint shown during autocomplete (e.g., `[filename]`)         |
| `disable-model-invocation` | No          | Set `true` to prevent Claude from auto-invoking             |
| `user-invocable`           | No          | Set `false` to hide from / menu                             |
| `allowed-tools`            | No          | Tools Claude can use without asking permission              |
| `disallowed-tools`         | No          | Tools removed from the model while the skill is active      |
| `model`                    | No          | Model to use when this skill is active                      |
| `context`                  | No          | Set to `fork` to run in a forked subagent context           |
| `agent`                    | No          | Which subagent to use when `context: fork` is set           |
| `hooks`                    | No          | Hooks scoped to this skill's lifecycle                      |

<h3 id="skill-arguments">Pass Arguments to Skills</h3>

Use `$ARGUMENTS` placeholder to receive arguments:

```markdown
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---

Fix GitHub issue $ARGUMENTS following our coding standards.

1. Read the issue description
2. Implement the fix
3. Write tests
4. Create a commit
```

**Usage:** `/fix-issue 123`

<h3 id="skill-dynamic-context">Inject Dynamic Context</h3>

Use `` !`command` `` syntax to run shell commands before the skill content is sent to Claude:

```markdown
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
---

## Pull request context

- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`

## Your task

Summarize this pull request...
```

<h3 id="skill-subagent">Run Skills in a Subagent</h3>

Add `context: fork` to run a skill in isolation:

```markdown
---
name: deep-research
description: Research a topic thoroughly
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly:

1. Find relevant files using Glob and Grep
2. Read and analyze the code
3. Summarize findings with specific file references
```

> The `agent` field can be `Explore`, `Plan`, `general-purpose`, or any custom subagent from `.claude/agents/`.

---

<h2 id="plugin-system">Plugin System</h2>

> [!Note]
> **Plugins extend Claude Code with custom commands, skills, agents, hooks, and MCP servers. Plugins can be loaded from local directories, Git repos, or the npm registry.**

**Key commands:**

```bash
claude plugin init my-plugin
/plugins install @org/claude-code-plugin
/plugins list
/plugins enable <plugin-name>
/plugins disable <plugin-name>
/plugins validate ./my-plugin
/plugins marketplace

# CLI aliases exist for scripting, for example:
claude plugin install https://org/claude-plugin-example
```

**Plugin structure:**

```
my-plugin/
├── plugin.json          # Plugin manifest (name, version, description)
├── agents/              # Custom agents (*.md frontmatter files)
├── skills/              # Custom skills (SKILL.md files)
├── hooks/               # Hook scripts
├── commands/            # Custom slash commands
└── mcp-servers/         # MCP server configurations
```

**Plugin scopes:**

| Location              | Scope        | Notes                     |
| :-------------------- | :----------- | :------------------------ |
| `--plugin-dir ./path` | Session only | CLI flag, not persisted   |
| `.claude/plugins/`    | Project      | Committed with the repo   |
| `~/.claude/plugins/`  | User-global  | Available in all projects |

**Plugin manifest (`plugin.json`):**

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "A Claude Code plugin",
  "defaultEnabled": false,
  "agents": ["agents/"],
  "skills": ["skills/"],
  "hooks": "hooks/hooks.json",
  "mcpServers": "mcp-servers/servers.json",
  "dependencies": ["required-plugin"]
}
```

> Plugins auto-update by default. Set `FORCE_AUTOUPDATE_PLUGINS=1` to force updates even when the main updater is disabled, or override with `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` for slow repos. Git/GitHub marketplace sources can use `skipLfs` to skip Git LFS downloads during clone and update.

Dependency behavior:

- `claude plugin enable` enables transitive dependencies automatically.
- `claude plugin disable` refuses when another enabled plugin depends on the target and reports the disable chain.
- `defaultEnabled: false` lets a plugin ship installed but disabled until the user explicitly enables it.

---

<h2 id="worktree-isolation">Worktree Isolation</h2>

> [!Note]
> **The `--worktree` (`-w`) flag starts Claude in an isolated git worktree, allowing it to make changes in a separate branch without affecting your working directory.**

**Usage:**

```bash
# Start Claude in an isolated worktree
claude -w "implement the new feature"

# Choose whether new worktrees branch from origin/default or local HEAD
claude config set worktree.baseRef "fresh" # default, uses origin/<default>
claude config set worktree.baseRef "head"  # use current local HEAD

# Claude will:
# 1. Create a temporary git worktree from the configured base ref
# 2. Run in that isolated worktree
# 3. Commit changes and optionally create a PR
# 4. Clean up the worktree when done
```

For repositories where worktrees are impractical, `worktree.bgIsolation: "none"` lets background sessions edit the working copy directly without `EnterWorktree`.

**Agent-level worktree isolation:**

```markdown
---
name: background-coder
description: Implements features in isolation
isolation: worktree
background: true
---

Implement the requested feature in this isolated worktree.
```

> Worktree isolation is especially powerful combined with `background: true` for agents, enabling parallel development workflows where multiple agents work on separate features simultaneously.

---

<h2 id="native-installer">Native Installer</h2>

> [!Note]
> **Use the native binary installer when you want faster startup, auto-updates, and no dependency on Node.js being available on your PATH.**

```bash
# Start the native installer (interactive)
claude install

# Switch from npm global install to native installer
claude migrate-installer
```

> The npm installation method (`npm install -g @anthropic-ai/claude-code`) continues to work. Choose the installer that best fits your environment and automation model.

---

<h2 id="claude-auth">Authentication CLI</h2>

> [!Note]
> **Manage authentication directly from the CLI without entering the REPL.**

```bash
# Log in to your Anthropic account
claude auth login

# Check current authentication status
claude auth status

# Log out
claude auth logout
```

---

<h2 id="claude-agents-cli">Agent Management CLI</h2>

> [!Note]
> **List configured agents and live Claude sessions from the command line.**

```bash
# List all agents (project, user, plugin, CLI-defined)
claude agents

# Script live sessions for status bars, session pickers, or tmux integrations
claude agents --json

# Dispatch with a specific agent, overriding settings.json for this run
claude --agent code-reviewer "review the current branch"
```

---

<h2 id="remote-control">Remote Control</h2>

> [!Note]
> **The `claude remote-control` subcommand allows external tools and build systems to drive Claude Code programmatically.**

```bash
# Start Claude in remote-control mode
claude remote-control
```

This is useful for IDE extensions, CI/CD pipelines, or custom orchestration tools that want to interact with Claude Code via its SDK interface.

---

<h2 id="managed-settings">Managed Settings</h2>

> [!Note]
> **Enterprise administrators can push managed settings via macOS plist or Windows Registry, providing organization-wide configuration control.**

**macOS (plist):**

Settings can be deployed via MDM profiles to `/Library/Managed Preferences/com.anthropic.claude-code.plist`.

**Windows (Registry):**

Settings can be deployed via Group Policy to `HKLM\SOFTWARE\Policies\Anthropic\ClaudeCode`.

> Managed settings take precedence over user/project settings and cannot be overridden by individual users.

---

<h2 id="model-updates">Model Updates</h2>

### Model Guidance

> [!Note]
> **Use model family aliases (`sonnet`, `opus`, `haiku`) for most workflows. Pin a full model ID only when reproducibility matters more than automatic upgrades.**

**Key highlights:**

- **Opus 4.8**: highest-effort Opus path, with `xhigh` effort and fast mode support.
- **Opus 4.7/4.8 on providers**: Bedrock, Vertex, and Foundry support auto mode opt-in with `CLAUDE_CODE_ENABLE_AUTO_MODE=1`.
- **Sonnet**: use the `sonnet` alias for balanced coding, planning, and refactoring.
- **Haiku/small-fast models**: use `ANTHROPIC_SMALL_FAST_MODEL` overrides for background naming and side-query paths when needed.
- **Gateway discovery**: set `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` to populate compatible gateway model pickers from `/v1/models`.

**Use in Claude Code:**

```bash
# Set by family alias
claude --model sonnet
claude --model opus

# Configure in settings with aliases
claude config set model "sonnet"

# Pin only when you need exact reproducibility
claude --model <full-model-id>
```

Model selection tips:

- Use family aliases in general examples so shared docs age well.
- Pin full model IDs only in workflows that need reproducible model behavior.
- Teach `/model` and `/fast` for day-to-day model switching instead of provider-specific overrides.

---

<h2 id="theming--customization">Theming & Customization</h2>

Claude Code supports built-in themes, custom named themes, and session accent colors.

```bash
/theme          # Pick a theme or create a custom one
/color          # Pick a session accent color
/color random   # Randomize session accent color
```

Custom themes can be edited as JSON under `~/.claude/themes/`, and plugins can ship themes for teams. The `Auto (match terminal)` theme follows terminal light/dark mode where supported.

---

<h2 id="code-review">Code Review</h2>

Claude Code has separate review paths for correctness, cleanup, and broader branch-level review.

| Command | Behavior |
| :------ | :--------------- |
| `/code-review [effort]` | Correctness-focused review at the chosen effort level |
| `/code-review --fix` | Applies review findings to the working tree, including reuse/simplification/efficiency suggestions |
| `/code-review --comment` | Posts inline GitHub PR comments where supported |
| `/simplify` | Cleanup-only review for reuse, simplification, efficiency, and altitude |
| `/ultrareview [target]` | Cloud review using parallel multi-agent analysis and critique |
| `claude ultrareview [target]` | Non-interactive CI/script entrypoint; supports JSON output |

Use `/code-review` for local correctness review, `/simplify` for cleanup, and `/ultrareview` when you want a broader cloud review of a branch or PR.

---

<h2 id="insights">Claude Code Insights</h2>

> [!Note]
> **The `/insights` command generates an interactive HTML report analyzing your coding habits from the past 30 days.**

**Run Insights:**

```bash
# In Claude Code terminal
/insights

# Open the generated report
start ~/.claude/usage-data/report.html     # Windows
open ~/.claude/usage-data/report.html      # Mac
xdg-open ~/.claude/usage-data/report.html  # Linux
```

**How It Works:**

1. **Session Collection** - Pulls session logs from `~/.claude/projects/`, filters agent sub-sessions and short sessions
2. **Metadata Extraction** - Extracts duration, token usage, tools used, languages detected, git activity
3. **Facet Extraction** - Uses Haiku model to analyze transcripts and identify goals, satisfaction signals, friction points
4. **Report Generation** - Creates interactive HTML report with personalized suggestions

**Report Sections:**

| Section               | Description                                                 |
| :-------------------- | :---------------------------------------------------------- |
| **What's Working**    | Your strengths and successful patterns                      |
| **What's Hindering**  | Where Claude struggled or where you caused friction         |
| **Friction Analysis** | Breakdown of problem areas with specific examples           |
| **Stats Dashboard**   | Tool usage, language breakdown, coding time distribution    |
| **Quick Wins**        | Copy-paste suggestions for CLAUDE.md improvements           |
| **Features to Try**   | Personalized recommendations (skills, hooks, headless mode) |

> Everything runs locally using the Anthropic API. Session data stays on your machine.

---

<h2 id="mcp-integration">MCP Integration</h2>

<h3 id="understanding-mcp-model-context-protocol">Understanding MCP (Model Context Protocol)</h3>

#### What is MCP?

> MCP extends Claude's capabilities by connecting to external services, databases, APIs, and tools (filesystem, Puppeteer, GitHub, Context7 etc...)

MCP behavior to know:

- MCP servers are available in more headless `claude -p` workflows, so automation can use configured tools without opening the full REPL.
- Remote OAuth and claude.ai connector flows have improved reconnect and refresh handling; use `/mcp` to reconnect after changing `.mcp.json`.
- Large MCP tool results can be persisted or capped by server annotations, reducing context blowups for large outputs.
- Tool names still follow the `mcp__server__tool` pattern for permissions and hooks.

###### **MCP Architecture:**

```
Claude Code ←→ MCP Protocol ←→ MCP Servers ←→ External Services
```

<h3 id="claudeai-mcp-connectors">claude.ai MCP Connectors</h3>

Claude Code can use MCP servers configured in your claude.ai account, bringing cloud-hosted tools to your CLI workflow.

```bash
# Enabled by default — to opt out:
export ENABLE_CLAUDEAI_MCP_SERVERS=false
```

This allows you to access the same MCP tool integrations available in claude.ai directly from the command line, without local MCP server configuration.

<h3 id="mcp-setup--configuration">MCP Setup & Configuration</h3>

###### Basic MCP Commands

```bash
claude mcp                   # Interactive MCP configuration
claude mcp list              # List configured servers
claude mcp add <name> <cmd>  # Add new server
claude mcp remove <name>     # Remove server
```

###### MCP Configuration File Location

```bash
~/.claude.json      # Global File
`.mcp.json`         # Project-scoped servers are stored in a File at your project's root directory
```

## Quick Start

> **If you're in a hurry, here's the fastest way to add:**

```bash
# Add file system access (most commonly used)
claude mcp add filesystem -s user -- npx -y @modelcontextprotocol/server-filesystem ~/Documents ~/Desktop

# Verify if successful
claude mcp list
```

> **Responce if it 