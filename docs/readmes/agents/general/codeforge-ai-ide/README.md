<!-- source: https://github.com/siddharth9238/CodeForge-AI-IDE.git sha: bf3d9da03c61ef959737be7f084b28afa29cbf95 readme: main/README.md -->
# siddharth9238/CodeForge-AI-IDE

A modern AI-powered full-stack IDE built with React, TypeScript, Monaco Editor, Node.js, and TurboRepo, featuring an integrated code editor, terminal, compiler, AI assistant, debugger, extensions, and workspace management.

---

# CodeForge AI IDE

An extensible AI-powered IDE built with React, Monaco Editor, and TypeScript.

## Features

- **AI Assistant** - Integrated AI coding assistant with streaming responses
- **Extension System** - VS Code-like extension architecture
- **Marketplace** - Browse and install extensions
- **Modern UI** - Clean, customizable interface with multiple themes
- **Terminal** - Integrated terminal with shell support
- **Debugger** - Full debugging capabilities
- **Git Integration** - Built-in Git support
- **Monaco Editor** - VS Code-like editing experience

## Development

```bash
# Install dependencies
pnpm install

# Start development server
pnpm --filter @codeforge/web dev

# Build all packages
pnpm build

# Run typecheck
pnpm typecheck
```

## Project Structure

```
CodeForge-AI-IDE/
├── apps/
│   ├── web/           # Main web application
│   ├── api/           # API server
│   ├── compiler/      # Compiler service
│   └── desktop/       # Electron desktop app
├── packages/
│   ├── core/          # Core utilities
│   ├── ui/            # UI components
│   ├── editor/        # Monaco editor integration
│   ├── extensions/    # Extension system
│   ├── ai/            # AI integration
│   ├── terminal/      # Terminal component
│   ├── debugger/      # Debugger component
│   └── shared/        # Shared types and utilities
└── .github/
    └── workflows/    # CI/CD pipelines
```

## Extension Development

Extensions are defined in `package.json`:

```json
{
  "id": "my-extension",
  "name": "My Extension",
  "publisher": "my-name",
  "version": "1.0.0",
  "engines": {
    "kiloIde": "^1.0.0"
  },
  "activationEvents": ["onCommand:my-extension.helloWorld"],
  "contributes": {
    "commands": [{
      "command": "my-extension.helloWorld",
      "title": "Hello World"
    }]
  }
}
```

## License

MIT