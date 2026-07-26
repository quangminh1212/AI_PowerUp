<!-- source: https://github.com/doozie-akshay/clippys_revenge.git sha: 8cd39b1b8777233c1954cd92854fe3dd300e4139 readme: main/README.md -->
# doozie-akshay/clippys_revenge

A desktop-native AI agent that resurrects the iconic Microsoft Office Assistant as a proactive, agentic coding companion. Unlike its passive predecessor, this Clippy possesses genuine agency through the Model Context Protocol (MCP), enabling it to connect directly to your filesystem, terminal, and IDE.

---

# Clippy's Revenge 📎

A desktop-native AI agent that resurrects the iconic Microsoft Office Assistant as a proactive, agentic coding companion. Unlike its passive predecessor, this Clippy possesses genuine agency through the Model Context Protocol (MCP), enabling it to connect directly to your filesystem, terminal, and IDE.

## Features

- **Always-on-top overlay** - Transparent, frameless Clippy that floats on your desktop
- **Proactive interventions** - Automatically detects build failures and linter errors
- **MCP integration** - Read/write files and execute commands through secure MCP servers
- **Personality modes** - Choose from Intern Mode, Passive-Aggressive Mode, or Doomsday Mode
- **VS Code extension** - Monitors terminal output and diagnostics
- **Safety controls** - Requires approval before executing commands or modifying files

## Prerequisites

- **Node.js** >= 18.x
- **npm** >= 9.x
- **VS Code** (for the extension)

## Project Structure

```
clippys-revenge/
├── src/
│   ├── main/           # Electron main process
│   │   ├── animation/  # Animation state management
│   │   ├── chat/       # Chat service and message store
│   │   ├── intervention/ # Proactive intervention logic
│   │   ├── ipc/        # IPC handlers
│   │   ├── kiro/       # Kiro hook system (WebSocket server)
│   │   ├── llm/        # LLM client (Anthropic)
│   │   ├── mcp/        # MCP client manager
│   │   ├── persistence/ # SQLite database layer
│   │   ├── personality/ # Personality engine
│   │   ├── safety/     # Safety controls
│   │   └── window/     # Window manager
│   ├── renderer/       # React frontend
│   └── shared/         # Shared types
├── vscode-extension/   # VS Code extension for event detection
└── tests/              # Test suites
```

## Quick Start

### 1. Install Dependencies

```bash
# Install main app dependencies
npm install

# Install VS Code extension dependencies
cd vscode-extension
npm install
cd ..
```

### 2. Run in Development Mode

**Start the Electron app:**

```bash
npm run dev
```

This launches the Electron app with hot-reload enabled. The app will:
- Open a transparent overlay window with Clippy
- Start a WebSocket server on port 9876 for VS Code extension communication
- Initialize the MCP client manager

**Build and run the VS Code extension:**

```bash
cd vscode-extension
npm run compile
```

Then in VS Code:
1. Open the `vscode-extension` folder
2. Press `F5` to launch the Extension Development Host
3. The extension will auto-connect to the Clippy Desktop Client

### 3. Run Tests

```bash
# Run all tests once
npm test

# Run tests in watch mode
npm run test:watch
```

## Configuration

### LLM Provider Options

Clippy supports multiple LLM providers. It auto-detects which one to use:

#### Option 1: Ollama (Free, Local) - Default
No API key needed! Runs completely locally on your machine.

1. Install Ollama: https://ollama.ai
2. Start the server: `ollama serve`
3. Pull a model: `ollama pull llama3.2`
4. Run Clippy: `npm run dev`

Supported models: `llama3.2`, `mistral`, `codellama`, `phi3`, etc.

#### Option 2: Anthropic Claude (Paid API)
For the best quality responses, use Claude:

```bash
export ANTHROPIC_API_KEY=your-api-key-here
npm run dev
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Anthropic API key (enables Claude) | - |
| `ANTHROPIC_MODEL` | Claude model to use | `claude-sonnet-4-20250514` |
| `OLLAMA_MODEL` | Ollama model to use | `llama3.2` |
| `OLLAMA_ENDPOINT` | Ollama server URL | `http://localhost:11434` |
| `KIRO_WS_PORT` | WebSocket port for VS Code extension | `9876` |

### VS Code Extension Settings

The extension exposes these settings:

| Setting | Default | Description |
|---------|---------|-------------|
| `clippy-kiro.websocketPort` | 9876 | WebSocket port for Desktop Client |
| `clippy-kiro.autoConnect` | true | Auto-connect on startup |
| `clippy-kiro.terminalOutputLines` | 50 | Lines to capture on failure |

## Development Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start Electron app in dev mode with hot-reload |
| `npm run build` | Build the Electron app for production |
| `npm run preview` | Preview the production build |
| `npm test` | Run test suite once |
| `npm run test:watch` | Run tests in watch mode |

### VS Code Extension Commands

```bash
cd vscode-extension
npm run compile    # Compile TypeScript
npm run watch      # Watch mode compilation
npm run lint       # Run ESLint
npm test           # Run extension tests
```

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code Extension                         │
│  ┌─────────────────┐  ┌──────────────────────────────────┐  │
│  │ Terminal Detector│  │ Diagnostic Detector              │  │
│  └────────┬────────┘  └───────────────┬──────────────────┘  │
│           │                           │                      │
│           └───────────┬───────────────┘                      │
│                       ▼                                      │
│              WebSocket Client                                │
└───────────────────────┬─────────────────────────────────────┘
                        │ ws://localhost:9876
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                 Clippy Desktop Client (Electron)             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                    Kiro Hook Server                      ││
│  │                   (WebSocket Server)                     ││
│  └────────────────────────┬────────────────────────────────┘│
│                           ▼                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │ Intervention │  │  Personality │  │   Safety         │   │
│  │   Manager    │  │    Engine    │  │  Controller      │   │
│  └──────┬───────┘  └──────┬───────┘  └────────┬─────────┘   │
│         │                 │                    │             │
│         └─────────────────┼────────────────────┘             │
│                           ▼                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │  LLM Client  │  │  MCP Client  │  │   Persistence    │   │
│  │  (Anthropic) │  │   Manager    │  │     Layer        │   │
│  └──────────────┘  └──────────────┘  └──────────────────┘   │
│                           │                                  │
│                           ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐│
│  │              Renderer (React + Lottie)                   ││
│  │  ┌─────────┐  ┌──────────────┐  ┌────────────────────┐  ││
│  │  │ Clippy  │  │ Speech Bubble│  │ Action Approval    │  ││
│  │  │ Overlay │  │              │  │                    │  ││
│  │  └─────────┘  └──────────────┘  └────────────────────┘  ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## Troubleshooting

### Electron app won't start

```bash
# Rebuild native dependencies
npm run postinstall
```

### VS Code extension not connecting

1. Ensure the Electron app is running first
2. Check the WebSocket port matches (default: 9876)
3. Run `Clippy: Show Connection Status` from VS Code command palette

### Tests failing

```bash
# Clear any cached builds
rm -rf dist
npm run build
npm test
```

## License

MIT © [Kiro Systems](https://kiro.systems)