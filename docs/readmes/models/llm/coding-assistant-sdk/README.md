<!-- source: https://github.com/canfieldjuan/coding-assistant-sdk.git sha: 385dfcd14ebb0d18f63089a1d1cb147e141ac383 readme: master/README.md -->
# canfieldjuan/coding-assistant-sdk

🚀 Complete Coding Assistant SDK - Fully Integrated AI Development Platform with Backend-CLI Integration, 17-Model LLM System, Web IDE, and Vibe-to-Production Pipeline

---

# 🚀 Unified Coding Assistant SDK

**The Copilot Killer** - Go from idea to deployed product in minutes!

A revolutionary development platform that combines:
- 🧠 **17 Specialized AI Models** via OpenRouter
- ⚡ **Lightning-fast Go Backend** for code analysis  
- 🎯 **Intelligent Generators** that create production-ready code
- 🌐 **Web IDE** with real-time collaboration
- 🔥 **Vibe-to-Product Pipeline** - Describe it, ship it!

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [System Architecture](#-system-architecture)
- [Directory Structure](#-directory-structure)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [API Reference](#-api-reference)
- [Testing](#-testing)
- [External Integration](#-external-integration)
- [Troubleshooting](#-troubleshooting)

## 🚀 Quick Start

```bash
# 1. Set your API key
export OPENROUTER_API_KEY=your_key_here

# 2. Start the unified system
python start_unified_system.py

# 3. Create your first product
python claude_code/main.py vibe "I want a SaaS for invoice management"
```

That's it! Your product is being generated with all components.

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   UNIFIED SYSTEM                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────┐     ┌──────────┐    ┌─────────┐         │
│  │   CLI   │     │  Web IDE │    │   API   │         │
│  └────┬────┘     └────┬─────┘    └────┬────┘         │
│       │               │                │               │
│       └───────────────┴────────────────┘               │
│                       │                                │
│              ┌────────▼────────┐                       │
│              │ Unified Gateway │                       │
│              └────────┬────────┘                       │
│                       │                                │
│    ┌─────────────────┼─────────────────┐              │
│    │                 │                 │              │
│ ┌──▼───┐     ┌──────▼──────┐   ┌─────▼────┐         │
│ │ Go   │     │     LLM     │   │  Claude  │         │
│ │Backend│     │   Service   │   │   Code   │         │
│ │:8080 │     │    :8081    │   │Generators│         │
│ └──────┘     └─────────────┘   └──────────┘         │
└─────────────────────────────────────────────────────────┘
```

## 📁 Directory Structure

```
coding-assistant-sdk/
│
├── 🧠 claude_code/                 # Core SDK & CLI
│   ├── cli/                       # Command line interfaces
│   │   ├── claude_cli.py         # Main CLI interface
│   │   ├── natural_cli.py        # Natural language CLI
│   │   └── unified_commands.py   # Vibe & unified commands
│   │
│   ├── generators/                # Code generators
│   │   ├── server.py             # Server generator (MCP, FastAPI, Express)
│   │   ├── agent.py              # Agent generator
│   │   ├── tool.py               # Tool generator
│   │   ├── sdk.py                # SDK generator
│   │   └── ai_integration.py     # AI integration generator
│   │
│   ├── integrations/              # System integrations
│   │   └── unified_system.py     # Core unified system logic
│   │
│   ├── memory/                    # Persistent memory system
│   ├── templates/                 # Code templates
│   ├── tools/                     # Built-in tools
│   └── utils/                     # Utilities (logger, file_ops, etc.)
│
├── ⚡ coding-assistant-backend/    # Go backend service
│   ├── scanner/                   # Main application
│   │   ├── main.go               # Entry point
│   │   ├── api/                  # REST API routes
│   │   ├── analyzer/             # Code analysis
│   │   └── parser/               # Language parsers
│   │
│   ├── frontend/                  # Python client library
│   │   ├── client.py             # Backend client
│   │   └── integration_example.py # Usage examples
│   │
│   └── storage/                   # Database layer
│
├── 🤖 llm_provider_api_calls/     # 17-model LLM system
│   ├── llm_provider.py           # Core LLM provider
│   ├── llm_server.py             # FastAPI service
│   ├── capability_router.py      # Route to best model
│   └── agent_with_capabilities.py # Multi-agent system
│
├── 🌐 coding-assistant-webui/     # Web IDE (Next.js)
│   ├── src/
│   │   ├── app/                  # Next.js app router
│   │   ├── components/           # React components
│   │   │   └── IDE/             # IDE components
│   │   ├── lib/                  # Libraries
│   │   │   └── unifiedClient.ts # Unified system client
│   │   └── hooks/                # React hooks
│   │       └── useUnifiedSystem.ts
│   │
│   └── public/                   # Static assets
│
├── 📊 generated/                  # Generated projects go here
├── 🧪 tests/                      # Comprehensive test suites
│   ├── brutal_unified_tests.py   # Stress & edge case tests
│   ├── validation_suite.py       # Correctness validation
│   └── service_stress_test.py    # Service load testing
│
├── 📝 docs/                       # Documentation
│   ├── api-references/           # API documentation
│   ├── guides/                   # How-to guides
│   └── patterns/                 # Design patterns
│
└── 🚀 Root Files
    ├── start_unified_system.py    # Start everything
    ├── run_all_tests.py          # Run all tests
    ├── example_client.py         # Example API client
    └── setup_external_access.py  # Enable external access
```

## 💻 Installation

### Prerequisites

- Python 3.8+
- Go 1.21+
- Node.js 18+ (for Web IDE)
- Git

### Setup

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd coding-assistant-sdk

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install Go dependencies
cd coding-assistant-backend
go mod download
cd ..

# 4. Install Node dependencies (optional, for Web IDE)
cd coding-assistant-webui
npm install
cd ..

# 5. Set environment variable
export OPENROUTER_API_KEY=your_openrouter_api_key_here
```

## 📖 Usage Guide

### Starting the System

```bash
# Start all services (Backend + LLM Service + CLI)
python start_unified_system.py

# Include Web IDE
python start_unified_system.py --with-web
```

Services will run on:
- Backend: http://localhost:8080
- LLM Service: http://localhost:8081
- Web IDE: http://localhost:3000

### CLI Commands

#### Vibe-to-Product (The Magic Command)
```bash
# Create a complete product from description
python claude_code/main.py vibe "I want a SaaS for managing gym memberships"

# With deployment
python claude_code/main.py ship "A tool for tracking crypto portfolios"
```

#### Unified Commands
```bash
# Check system status
python claude_code/main.py unified_status

# Generate with full context
python claude_code/main.py unified_generate server my_api
```

#### Classic Generators (Enhanced with context)
```bash
# Generate a server
python claude_code/main.py generate server my_server

# Generate an agent
python claude_code/main.py generate agent my_assistant --type claude

# Generate a tool
python claude_code/main.py generate tool data_processor

# Generate an SDK
python claude_code/main.py generate sdk my_api --language typescript
```

#### Memory & Context
```bash
# Remember information
python claude_code/main.py remember "api_endpoint" "https://api.example.com"

# Recall information
python claude_code/main.py recall "api_endpoint"

# Inject context
python claude_code/main.py inject --context "Building a fintech app"
```

### Web IDE Usage

1. Start with `--with-web` flag
2. Open http://localhost:3000
3. Features:
   - Real-time code editing with Monaco Editor
   - AI-powered suggestions
   - File explorer with project structure
   - Live preview for web projects
   - Integrated terminal

## 🔌 API Reference

### LLM Service API (Port 8081)

#### Complete Text
```bash
POST /api/v1/llm/complete
{
  "purpose": "code_generation|analysis|debugging|...",
  "prompt": "Your prompt here",
  "context": {"optional": "context"}
}
```

#### Vibe to Spec
```bash
POST /api/v1/llm/vibe-to-spec
{
  "vibe": "I want an app that...",
  "tech_preferences": {"backend": "fastapi"},
  "constraints": ["must be GDPR compliant"]
}
```

#### Generate Code
```bash
POST /api/v1/llm/generate-code
{
  "type": "server|agent|tool",
  "name": "component_name",
  "context": {"language": "python"}
}
```

#### List Models
```bash
GET /api/v1/llm/models
```

Full API docs: http://localhost:8081/docs

### Backend API (Port 8080)

#### Scan Project
```bash
POST /api/v1/scan
{
  "project_path": "/path/to/project",
  "analyze_dependencies": true
}
```

#### Get Files
```bash
GET /api/v1/files?project_path=/path/to/project
```

#### Get Dependencies
```bash
GET /api/v1/dependencies/:fileId
```

#### Get Metrics
```bash
GET /api/v1/metrics/file/:fileId
```

### Python Client Example

```python
from coding_assistant_backend.frontend.client import CodingAssistantClient

# Initialize client
client = CodingAssistantClient()

# Scan project
result = client.scan_project("/path/to/project")
print(f"Found {result.total_files} files")

# Get Python files
python_files = client.get_files_by_type("/path/to/project", "python")
```

## 🧪 Testing

### Run All Tests
```bash
# Run complete test suite
python run_all_tests.py

# With automatic service startup
python run_all_tests.py --with-services
```

### Individual Test Suites
```bash
# Brutal stress tests
python tests/brutal_unified_tests.py

# Validation tests
python tests/validation_suite.py

# Service stress tests
python tests/service_stress_test.py
```

### What Gets Tested
- ✅ Input validation (empty, huge, malicious inputs)
- ✅ Edge cases and boundaries
- ✅ Concurrent operations
- ✅ Memory and performance limits
- ✅ Error handling and recovery
- ✅ Security vulnerabilities
- ✅ Integration between components

## 🌐 External Integration

### For Claude Desktop

1. Run setup script:
```bash
python setup_external_access.py
```

2. Add to Claude Desktop config:
```json
{
  "external_services": [{
    "name": "Unified Coding Assistant",
    "endpoints": {
      "llm": "http://YOUR_IP:8081",
      "backend": "http://YOUR_IP:8080"
    }
  }]
}
```

### API Client Example

```python
from example_client import UnifiedSystemClient

# Create client
client = UnifiedSystemClient()

# Generate code
result = client.call_llm(
    purpose="code_generation",
    prompt="Create a REST API for user management"
)

# Convert vibe to spec
spec = client.vibe_to_spec("I want an app like Airbnb but for boats")
```

### Docker Deployment

```bash
# Use generated docker-compose
docker-compose -f docker-compose.unified.yml up
```

## 🛠️ Configuration

### Environment Variables

```bash
# Required
OPENROUTER_API_KEY=your_key_here

# Optional
CLAUDE_BACKEND_URL=http://localhost:8080
LLM_SERVICE_PORT=8081
CLAUDE_USE_BACKEND=true
UNIFIED_SYSTEM_ENABLED=true
```

### Feature Flags

- `ENABLE_AI_INTEGRATION_GENERATOR` - Enable AI integration generator
- `ENABLE_SMART_TEST_GENERATOR` - Enable intelligent test generation
- `CLAUDE_USE_BACKEND` - Use backend for context awareness

## 🚨 Troubleshooting

### Common Issues

#### Services not starting
```bash
# Check if ports are in use
netstat -an | grep 8080
netstat -an | grep 8081

# Kill processes if needed
# Windows: netstat -ano | findstr :8080
# Then: taskkill /PID <PID> /F
```

#### API key issues
```bash
# Verify key is set
echo $OPENROUTER_API_KEY

# Set it if missing
export OPENROUTER_API_KEY=sk-or-v1-xxxxx
```

#### Backend compilation errors
```bash
cd coding-assistant-backend
go mod tidy
go mod download
```

### Logs

- Backend logs: Console output
- LLM service logs: Console output
- Generated code: `./generated/` directory
- Test results: `*_test_results.json` files

## 🎯 Advanced Features

### Multi-Model Intelligence

The system automatically selects the best model for each task:
- **Claude 3.5 Sonnet** - Complex code generation
- **GPT-4 Turbo** - Code review and optimization
- **Claude 3 Opus** - Deep debugging
- **GLM 4.5** - Multilingual support
- **GPT-4 Vision** - Image analysis
- And 12 more specialized models!

### Context-Aware Generation

Every generation uses:
- Current project structure
- Language conventions
- Existing patterns
- Dependency analysis

### Self-Improving Generators

The system learns from:
- Successful generations
- Failed attempts
- User modifications
- Best practices

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Run tests: `python run_all_tests.py`
4. Submit a pull request

## 📄 License

MIT License - See LICENSE file for details

## 🚀 What's Next?

Ready for your next mission? The system is built to evolve and integrate with anything. Sky's the limit!

---

**Built with ❤️ by developers who believe coding should be as easy as describing what you want.**