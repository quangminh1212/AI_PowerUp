<!-- source: https://github.com/aroldos91/antigravity-mem.git sha: 75dd630c35796fa16c65acde593a9eb5067f54c7 readme: main/README.md -->
# aroldos91/antigravity-mem

🧠 Persistent memory compression and retrieval for the Antigravity IDE — give your AI coding assistant long-term memory across sessions

---

<div align="center">

# 🧠 Antigravity Mem

**Persistent memory compression and retrieval for the [Antigravity IDE](https://developers.google.com/gemini)**

[![License](https://img.shields.io/badge/License-Apache_2.0-00d4aa.svg)](LICENSE)
[![Node.js](https://img.shields.io/badge/Node.js-20%2B-339933.svg)](https://nodejs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6.svg)](https://www.typescriptlang.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

*Give your AI coding assistant a long-term memory across sessions.*

[Quick Start](#-quick-start) · [Features](#-features) · [Architecture](#-architecture) · [Web Viewer](#-web-viewer) · [MCP Integration](#-mcp-integration) · [Contributing](#-contributing)

</div>

---

## 🤔 The Problem

Every time you start a new conversation in Antigravity (Google's AI coding IDE), the AI has **zero context** about your previous sessions. It doesn't remember:

- What bugs you fixed yesterday
- Which architecture decisions you made
- What files you modified last week
- How you solved similar problems before

**Antigravity Mem solves this.** It scans your local conversation artifacts, extracts structured observations, and makes your entire coding history searchable — both through a web UI and directly inside Antigravity via MCP tools.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Smart Extraction** | Parses walkthroughs, tasks, plans, and analyses into typed observations |
| 💾 **Local SQLite** | Zero-dependency WASM SQLite (sql.js) — no native compilation needed |
| 🌐 **Web Viewer** | Premium dark-mode SPA with stream, search, and session views |
| 🔌 **MCP Integration** | 4 tools exposed to Antigravity for in-conversation memory access |
| ⌨️ **CLI** | Scan, search, serve, and manage your memory from the terminal |
| 🏷️ **Auto-Tagging** | Keyword-based tagging (react, typescript, cors, auth, etc.) |
| 📁 **File Tracking** | Tracks which files were touched in each observation |
| 🔒 **100% Local** | All data stays on your machine — nothing leaves localhost |

## 📦 Quick Start

### Prerequisites

- **Node.js 20+** (uses ESM modules and modern APIs)
- **Antigravity IDE** installed (data lives in `~/.gemini/antigravity/`)

### Installation

```bash
# Clone the repository
git clone https://github.com/aroldos91/antigravity-mem.git
cd antigravity-mem

# Install dependencies
npm install

# Scan your Antigravity conversations
npx tsx src/cli/index.ts scan

# Start the web viewer
npx tsx src/cli/index.ts serve
```

Open **http://localhost:37888** to browse your memory.

### Register MCP in Antigravity

```bash
npx tsx src/cli/index.ts install
```

This adds `antigravity-mem` as an MCP server in `~/.gemini/antigravity/mcp_config.json`. Restart Antigravity to activate — you'll have access to `memory_search`, `memory_timeline`, `memory_get`, and `memory_stats` tools in every conversation.

## 🏗️ Architecture

<div align="center">

<img src="docs/images/architecture.png" alt="Antigravity Mem Architecture" width="800">

</div>

### Data Flow

```
Antigravity Brain → Scanner → Extractor → SQLite DB → { Web UI, MCP Server, CLI }
```

1. **Scanner** discovers markdown artifacts across all conversation directories in `~/.gemini/antigravity/brain/`
2. **Extractor** parses each artifact by type (walkthrough, task, plan) and produces structured observations with titles, summaries, file paths, and tags
3. **Database** stores observations in a WASM SQLite database with deduplication (upsert by source file)
4. **Consumers** query the database via REST API (web viewer), MCP tools (Antigravity), or CLI (terminal)

### Directory Structure

```
~/.gemini/antigravity/brain/          ← Antigravity's conversation storage
  ├── {conversation-id}/
  │   ├── walkthrough.md              ← Session summaries
  │   ├── task.md                     ← TODO tracking
  │   ├── implementation_plan.md      ← Technical plans
  │   └── *.md                        ← Other artifacts
  └── ...

~/.antigravity-mem/                   ← Antigravity Mem's storage
  └── memory.db                       ← SQLite database (WASM)
```

## 🌐 Web Viewer

The web viewer runs at `http://localhost:37888` with a premium dark-mode interface:

<div align="center">

<img src="docs/images/web-viewer-stream.png" alt="Stream View" width="800">

<em>Stream View — chronological feed with color-coded type badges, tags, and file counts</em>

</div>

<br>

<div align="center">

<img src="docs/images/web-viewer-search.png" alt="Search View" width="800">

<em>Search View — full-text search with type filtering and relevance scoring</em>

</div>

### Views

| View | Description |
|------|-------------|
| ⚡ **Stream** | Chronological feed of all observations |
| 🔍 **Search** | Full-text search with type filters (Walkthrough, Bug Fix, Plan, Decision) |
| 💬 **Sessions** | Browse by Antigravity conversation session |

Click any observation card to open a **detail modal** with full content, files touched, and tags.

## 🔌 MCP Integration

Once installed, Antigravity can use these tools in any conversation:

### `memory_search`
```
Search your coding memory for past observations.
Supports multi-term queries with relevance scoring.

Parameters:
  query    (required)  Search query string
  type     (optional)  Filter: walkthrough, task, plan, bug_fix, code_change, decision, analysis
  project  (optional)  Filter by project name
  limit    (optional)  Max results (default: 20)
```

### `memory_timeline`
```
Get chronological context around a specific event.

Parameters:
  around_id    (optional)  Observation ID to center around
  around_date  (optional)  ISO date to center around
  window       (optional)  Number of entries (default: 10)
```

### `memory_get`
```
Fetch full observation details by IDs.

Parameters:
  ids  (required)  Array of observation IDs
```

### `memory_stats`
```
Get statistics about stored memory.
Returns: total observations, sessions, projects, top tags, date range.
```

## ⌨️ CLI Reference

```bash
# Scan all Antigravity conversations into the database
antigravity-mem scan

# Start web viewer + API server
antigravity-mem serve [--port 37888]

# Search from the terminal
antigravity-mem search "CORS bug fix"

# Show database statistics
antigravity-mem status

# Register MCP server in Antigravity config
antigravity-mem install

# Start MCP server on stdio (called by Antigravity)
antigravity-mem mcp
```

## 📁 Project Structure

```
antigravity-mem/
├── src/
│   ├── types.ts            # Core TypeScript interfaces
│   ├── config.ts           # Configuration management
│   ├── database.ts         # SQLite layer (sql.js WASM)
│   ├── extractor.ts        # Artifact → Observation parser
│   ├── compressor.ts       # Heuristic text compression
│   ├── scanner.ts          # Brain directory scanner
│   ├── cli/
│   │   └── index.ts        # CLI entry point (6 commands)
│   ├── mcp/
│   │   └── server.ts       # MCP server (4 tools)
│   └── web/
│       ├── server.ts       # Express API server
│       └── public/         # SPA frontend
│           ├── index.html
│           ├── style.css
│           └── app.js
├── docs/
│   └── images/             # Architecture & UI screenshots
├── package.json
├── tsconfig.json
├── LICENSE                  # Apache 2.0
├── CONTRIBUTING.md
└── README.md
```

## 🔧 Configuration

Default paths (can be overridden via environment variables or config):

| Setting | Default | Description |
|---------|---------|-------------|
| `antigravityDataDir` | `~/.gemini/antigravity` | Antigravity's data directory |
| `dbPath` | `~/.antigravity-mem/memory.db` | SQLite database location |
| `port` | `37888` | Web viewer port |

## 🧪 Observation Types

The extractor recognizes these observation types:

| Type | Source | What it captures |
|------|--------|------------------|
| `walkthrough` | `walkthrough.md` | Session summaries, changes made, what was tested |
| `task` | `task.md` | TODO items (completed, in-progress, pending) |
| `plan` | `implementation_plan.md` | Technical plans, proposed changes |
| `decision` | Extracted from plans | Architecture decisions, design choices |
| `code_change` | Extracted from walkthroughs | Diff blocks, file modifications |
| `bug_fix` | Extracted from walkthroughs | Bug descriptions, root causes, fixes |
| `analysis` | Other `.md` files | PR reviews, research, investigations |
| `configuration` | Config-related files | Deployment settings, infrastructure |

## 🗺️ Roadmap

- [ ] **Real-time file watcher** — Auto-scan new artifacts via `chokidar` (`--watch` flag)
- [ ] **Improved project detection** — Better regex for extracting project names from paths
- [ ] **npm scripts** — `npm run dev`, `npm run scan`, `npm run build`
- [ ] **FTS5 search** — Upgrade to FTS5 when sql.js adds compile-time support
- [ ] **AI-powered compression** — Optional LLM summarization of observations
- [ ] **Export/import** — JSON export for backup and sharing
- [ ] **Multi-IDE support** — Extend to other AI coding assistants
- [ ] **Diagram generation** — Auto-generate architecture diagrams from observations

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick contribution guide

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the scanner to test (`npx tsx src/cli/index.ts scan`)
5. Commit with a descriptive message
6. Push and open a Pull Request

### Areas where help is needed

- 🔍 Improving the text extraction heuristics
- 🌐 Adding more observation types
- 📊 Web viewer UI enhancements
- 🧪 Adding test coverage
- 📖 Documentation improvements
- 🌍 Internationalization

## 📄 License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

### Why Apache 2.0?

- ✅ **Patent protection** — Contributors automatically grant patent rights
- ✅ **Contributor license** — Contributions are automatically licensed under the same terms
- ✅ **Commercial friendly** — Can be used in proprietary projects
- ✅ **Attribution required** — Must give credit when redistributing
- ✅ **Modification notice** — Must note changes in modified files
- ✅ **Compatible** — All dependencies (sql.js, express, MCP SDK) are MIT-licensed

## 🙏 Acknowledgments

- Inspired by [claude-mem](https://github.com/thedotmack/claude-mem) by @thedotmack
- Built for the [Antigravity IDE](https://developers.google.com/gemini) ecosystem
- Uses [sql.js](https://github.com/sql-js/sql.js) for portable SQLite
- Uses [Model Context Protocol](https://modelcontextprotocol.io) for IDE integration

---

<div align="center">

**Built with 🧠 by the community, for the community.**

If this project helps you, consider giving it a ⭐

</div>
