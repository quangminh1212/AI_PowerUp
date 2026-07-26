<!-- source: https://github.com/Kabeer-Sachdev/BrownField-IDE-with-Code-Migration-Agent-.git sha: b6d2dcc85156d7bbf76debb2f821d63377507b1d readme: main/README.md -->
# Kabeer-Sachdev/BrownField-IDE-with-Code-Migration-Agent-

An AI-powered Brownfield IDE that helps developers understand, refactor, and modernize legacy applications with an intelligent AI assistant and automated Code Migration Agent for faster, safer, and smarter application modernization.

---

# Agentic Brownfield Development Environment & AI Code Migration Agent

An intelligent, decoupled developer environment built for existing ("Brownfield") codebases. It provides deep architectural analysis, AST-based semantic searches, interactive dependency impact graphs, an AI development agent, and an automated multi-pass **AI Code Migration Agent** to migrate systems safely across languages and frameworks with transactional rollback guarantees.

---

## 🚀 Key Features & Capabilities

### 1. Brownfield IDE Subsystem
* **Instant Project Ingestion**: Scan any local project directory or imported zip archive to automatically build a structural codebase representation within seconds.
* **Three-Tier Architectural Recognition**: Automatically maps files and directories to their structural layer: **Presentation** (Controllers/UI), **Business Logic** (Services/Use Cases), and **Data Access** (Repositories/Entities/DB).
* **Granular Component Classification**: Classifies codebase components across 10 architectural categories including Controllers, Services, Repositories, Models, DTOs, Entities, Interfaces, Utilities, Exceptions, and Test Files.
* **Semantic & AST Symbol Search**: Search codebase contents natively using structural AST properties (class definitions, function signatures, REST routes, variables) rather than slow, flat-file string matches.
* **Architecture Impact Analysis**: Construct and traverse dynamic node-edge dependency graphs to evaluate change risks and cascade paths before writing code.
* **Intelligent Development Agent**: Interact with a dedicated AI coding assistant that takes natural language requests and converts them into safe, multi-file code diff bundles.
* **Transactional Code Updates**: Proposed changes are held in-memory or staged in isolated paths. Applying changes creates automated backups, with full undo functionality.

### 2. AI Code Migration Agent Subsystem
* **Language & Framework Agnostic**: Translate legacy code across modern language combinations (e.g., Python to Java, Java to Python, C# to Java, JavaScript to TypeScript, Go, Rust, Kotlin).
* **6 Migration Scopes**: Narrow down or scale out migrations across:
  1. `Current File` - Single file conversion.
  2. `Selected Folder` - Full sub-directory package migration.
  3. `Frontend Layer` - Target UI/Presentation components.
  4. `Backend Layer` - Target Business Logic and Service components.
  5. `Database Layer` - Target entities, schema tables, and repository layers.
  6. `Entire Project` - Fully integrated end-to-end repository translation.
* **Staged Generation**: Code is generated and validated inside an isolated directory (`~/.brownfield-ide/migrations/<session_id>/`) before ever touching active workspace source code.
* **6-Pass Security & Validation**: Prior to merging, generated code is evaluated for:
  1. *Syntax Correctness* - Compiles/parses cleanly.
  2. *Architecture Alignment* - Checks structure against layer conventions.
  3. *Dependency Resolution* - Audits package imports and third-party libraries.
  4. *Database & Model Audit* - Verifies schema and data structures.
  5. *Configuration Integrity* - Inspects build scripts and configuration profiles.
  6. *Risk Level Evaluation* - Calculates a 0-100 safety score (Low, Medium, High risk).
* **Byte-for-Byte Rollback**: If issues are detected, restore pre-migration source states instantly using byte-for-byte snapshot comparisons.

---

## 📐 System Architecture

The application is split into three core layers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      FRONTEND LAYER (Vanilla JS + HTML5 + CSS3)            │
│  ┌─────────────────────────┐  ┌──────────────────┐  ┌───────────────────┐  │
│  │ Brownfield IDE UI       │  │ Monaco Editor    │  │ Integrated        │  │
│  │ (Tree, Tabs, Panels)    │  │ (Syntax, Diff)   │  │ Terminal (xterm)  │  │
│  └────────────┬────────────┘  └────────┬─────────┘  └─────────┬─────────┘  │
│               │                        │                      │            │
│  ┌────────────┴────────────┐  ┌────────┴─────────┐  ┌─────────┴─────────┐  │
│  │ Migration Workspace UI  │  │ Impact Graph UI  │  │ AI Chat & Agent   │  │
│  │ (Config, Progress, Diff)│  │ (Interactive)    │  │ (Console/Panel)   │  │
│  └────────────┬────────────┘  └────────┬─────────┘  └─────────┬─────────┘  │
└───────────────┼────────────────────────┼──────────────────────┼────────────┘
                │                        │                      │
                ▼                        ▼                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       BACKEND API LAYER (FastAPI / Uvicorn)                 │
│  ┌───────────────────┐  ┌────────────────────┐  ┌────────────────────────┐ │
│  │ Workspace & FS    │  │ Terminal (PyWinPTY)│  │ Search & Impact        │ │
│  │ (/api/workspace)  │  │ (/ws/terminal)     │  │ (/api/search,/impact)  │ │
│  └─────────┬─────────┘  └─────────┬──────────┘  └───────────┬────────────┘ │
│            │                      │                         │              │
│  ┌─────────┴─────────┐  ┌─────────┴──────────┐  ┌───────────┴────────────┐ │
│  │ Analysis Engine   │  │ Development Agent  │  │ Validation & Source    │ │
│  │ (/api/analysis)   │  │ (/api/agent)       │  │ (/api/validation,source)│ │
│  └─────────┬─────────┘  └─────────┬──────────┘  └───────────┬────────────┘ │
│            │                      │                         │              │
│  ┌─────────┴──────────────────────┴─────────────────────────┴────────────┐ │
│  │ Migration Pipeline Engine (/api/migration/*)                          │ │
│  │ (Analysis -> Generation -> Validation -> Apply -> Rollback)            │ │
│  └────────────────────────────────┬──────────────────────────────────────┘ │
└───────────────────────────────────┼────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      AI PROVIDER AGNOSTIC LAYER                             │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌────────────────────┐   │
│  │ Ollama       │ │ Gemini       │ │ Groq         │ │ OpenAI / OpenRouter│   │
│  │ (Local LLM)  │ │ (Google Cloud│ │ (Fast LPU)   │ │ / Azure / Local    │   │
│  └──────────────┘ └──────────────┘ └──────────────┘ └────────────────────┘   │
│  └─ BaseLLMProvider Interface (Dynamic Config & Failover to AST scrapper)─┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

* **Backend**: FastAPI, Uvicorn, Python AST, PyWinPTY (Windows Pseudo-Terminal wrappers).
* **Frontend**: Vanilla HTML5, CSS3 (Modern Glassmorphism Design System), Vanilla JS, Monaco Editor API, Xterm.js.
* **AI Providers**: OpenRouter, OpenAI GPT-4o, Google Gemini Pro, Anthropic Claude, Groq Llama-3, Local Ollama.

---

## 💻 Installation & Setup

### Prerequisites
* **Windows OS** (PyWinPTY dependency requires a Windows environment).
* **Python 3.10+** (Make sure Python is added to your environment `PATH`).

### Step-by-Step Launch
1. Clone this repository locally.
2. Run the `start.bat` script at the root directory:
   ```cmd
   start.bat
   ```
   This script will:
   * Verify your Python version.
   * Auto-detect or clean-recreate the Python virtual environment (`venv`).
   * Install all required libraries from `requirements.txt`.
   * Boot up the FastAPI backend on `http://localhost:8000`.
3. Open `frontend/index.html` in your web browser (or serve it locally using any static web server).

### Environment Configuration (`.env`)
To enable AI services, create a `.env` file in the root or set environment variables for your active AI Provider:
```env
# Example configuration keys
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
OLLAMA_BASE_URL=http://localhost:11434
```

---

## 📡 API Directory

The FastAPI backend exposes endpoints structured for tooling and IDE operations:

| Area | Protocol/Method | Path | Description |
|---|---|---|---|
| **System** | `GET` | `/api/health` | Health Check and Server Version |
| **Workspace** | `POST` | `/api/workspace/open` | Initialize a workspace folder path |
| | `GET` | `/api/workspace/current` | Retrieve metadata of current workspace |
| **Filesystem** | `GET` | `/api/fs/tree` | Read filesystem directory hierarchy |
| | `GET` | `/api/fs/file` | Retrieve file contents |
| | `PUT` | `/api/fs/file` | Update/overwrite file contents |
| **Terminal** | `WebSocket` | `/ws/terminal` | Stream shell execution session in real-time |
| **Analysis** | `POST` | `/api/analysis/scan` | Analyze structural layer layout |
| **Search** | `POST` | `/api/search/symbols` | Search classes, methods, and REST paths |
| **Impact Graph** | `POST` | `/api/impact/graph` | Build dynamic node-edge dependencies |
| **Dev Agent** | `POST` | `/api/agent/chat` | Issue prompts and request diff changes |
| **Validation** | `POST` | `/api/validation/validate` | Execute the 6-pass code safety pipeline |
| **Migration** | `POST` | `/api/migration/analyze` | Assess migration scope & component list |
| | `POST` | `/api/migration/generate` | Stage translations in staging workspace |
| | `POST` | `/api/migration/apply` | Merge staged files and create backup |
| | `POST` | `/api/migration/rollback` | Perform byte-for-byte backup restoration |

---

## 📘 Workflows in Action

### A. Developing Features Safely
1. Start `start.bat` and open the Frontend client.
2. In the workspace explorer, choose your project directory.
3. Use the **Impact Graph** panel to inspect component dependencies.
4. Input a prompt into the **Development Agent** panel (e.g., *"Add a health check route"*).
5. Review the proposed side-by-side Monaco code diff.
6. The system executes the **6-pass validation engine**.
7. Click **Apply Changes** to transactionally write files to disk (or click **Undo** to revert).

### B. Migrating a Legacy Service
1. Navigate to the **Migration** tab in the client interface.
2. Configure your migration parameters (e.g., Target: `Java`, Scope: `Selected Folder`, Strategy: `rewrite`).
3. Click **Analyze** to check component details and complexity.
4. Click **Generate** to stage translated code in the isolated path.
5. Review generated files, check their validation score, and resolve dependencies.
6. Apply the migration; if issues are found post-apply, trigger **Rollback** to revert instantly.
