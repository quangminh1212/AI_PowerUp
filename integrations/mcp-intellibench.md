# 🧠 MCP IntelliBench

<div align="center">

![MCP IntelliBench](https://img.shields.io/badge/MCP-IntelliBench-blue?style=for-the-badge&logo=artificial-intelligence)
![Version](https://img.shields.io/badge/version-1.0.0-green?style=for-the-badge)
![TypeScript](https://img.shields.io/badge/TypeScript-5.7-blue?style=for-the-badge&logo=typescript)
![Node.js](https://img.shields.io/badge/Node.js-20+-green?style=for-the-badge&logo=node.js)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A comprehensive MCP (Model Context Protocol) Server for evaluating AI Coding Intelligence**

[📖 Documentation](#documentation) • [🚀 Quick Start](#quick-start) • [📊 Benchmarks](#benchmarks) • [🔧 API Reference](#api-reference)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Benchmarks](#benchmarks)
- [API Reference](#api-reference)
- [Dashboard](#dashboard)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

**MCP IntelliBench** is a state-of-the-art evaluation framework designed to assess the intelligence capabilities of AI coding assistants through the Model Context Protocol (MCP). It provides a standardized, reproducible, and comprehensive benchmark suite for measuring AI coding performance across multiple dimensions.

### Why MCP IntelliBench?

- 🔬 **Scientific Rigor**: Follows peer-reviewed evaluation methodologies
- 📊 **Multi-dimensional Assessment**: Evaluates code quality, reasoning, creativity, and efficiency
- 🔄 **Real-time Feedback**: Instant scoring and detailed analysis
- 🌐 **MCP Compliant**: Built on Anthropic's Model Context Protocol standard
- 📈 **Historical Tracking**: Monitor AI performance over time
- 🎨 **Beautiful Dashboard**: Modern web interface for results visualization

## ✨ Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| 🧪 **30+ Benchmark Tests** | Comprehensive test suite covering all coding domains |
| 📊 **Multi-category Scoring** | Code quality, logic, creativity, efficiency metrics |
| 🔄 **Real-time Evaluation** | Instant feedback with detailed explanations |
| 📈 **Performance Analytics** | Historical tracking and trend analysis |
| 🌐 **REST API** | Easy integration with external systems |
| 🎨 **Web Dashboard** | Modern, responsive UI for results visualization |

### Evaluation Categories

1. **🔧 Code Generation** - Ability to generate correct, efficient code
2. **🐛 Bug Detection** - Identifying and explaining code issues
3. **🔄 Code Refactoring** - Improving code quality and maintainability
4. **📚 Algorithm Design** - Problem-solving and algorithmic thinking
5. **🧪 Test Generation** - Creating comprehensive test cases
6. **📖 Documentation** - Writing clear, helpful documentation
7. **🏗️ Architecture Design** - System design and patterns
8. **🔒 Security Analysis** - Identifying security vulnerabilities

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         MCP IntelliBench                                │
├─────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│  │   MCP Core  │  │  Benchmark  │  │   Scoring   │  │  Analytics  │   │
│  │   Server    │  │   Engine    │  │   Engine    │  │   Engine    │   │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘   │
│         │                │                │                │          │
│         └────────────────┴────────────────┴────────────────┘          │
│                                    │                                   │
│  ┌─────────────────────────────────┴──────────────────────────────┐   │
│  │                      Challenge Repository                       │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐  │   │
│  │  │CodeGen  │ │BugFix   │ │Refactor │ │Algorithm│ │Security │  │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘  │   │
│  └────────────────────────────────────────────────────────────────┘   │
│                                                                        │
│  ┌────────────────────────────────────────────────────────────────┐   │
│  │                         Data Layer                              │   │
│  │  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐      │   │
│  │  │   Results   │  │  Leaderboard │  │  Session History │      │   │
│  │  │   Store     │  │    Cache     │  │      Store       │      │   │
│  │  └─────────────┘  └──────────────┘  └──────────────────┘      │   │
│  └────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** >= 20.0.0
- **pnpm** >= 9.0.0 (recommended) or npm >= 10.0.0
- **TypeScript** >= 5.7.0

### One-Command Setup

```bash
# Clone and setup
git clone https://quangminh1212/MCP_IntelliBench.git
cd MCP_IntelliBench
pnpm install
pnpm build

# Start MCP Server
pnpm start:server

# Start Dashboard (optional)
pnpm start:dashboard
```

### Quick Test

```bash
# Run a quick benchmark test
pnpm test:quick

# Run full benchmark suite
pnpm benchmark
```

## 📦 Installation

### Using pnpm (Recommended)

```bash
pnpm install
```

### Using npm

```bash
npm install
```

### Global Installation

```bash
npm install -g @mcp/intellibench
```

### ☁️ Vercel Deployment (Cloud Hosting)

Deploy MCP IntelliBench to Vercel for cloud access:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://quangminh1212/MCP_IntelliBench)

**Manual Deployment:**

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy to Vercel
vercel

# Deploy to production
vercel --prod
```

**Endpoints after deployment:**
- Health Check: `https://your-app.vercel.app/api/health`
- MCP Server: `https://your-app.vercel.app/api/mcp`
- SSE Transport: `https://your-app.vercel.app/api/mcp/sse`

**Configure MCP Client for Vercel:**

```json
{
  "mcpServers": {
    "intellibench-cloud": {
      "transport": {
        "type": "sse",
        "url": "https://your-app.vercel.app/api/mcp/sse"
      }
    }
  }
}
```


## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Server Configuration
MCP_SERVER_PORT=3000
MCP_SERVER_HOST=localhost

# Benchmark Configuration
BENCHMARK_TIMEOUT=30000
BENCHMARK_MAX_RETRIES=3
BENCHMARK_PARALLEL=true

# Scoring Configuration
SCORING_STRICT_MODE=false
SCORING_PARTIAL_CREDIT=true

# Dashboard Configuration
DASHBOARD_PORT=8080
DASHBOARD_HOST=localhost

# Database Configuration
DATABASE_PATH=./data/intellibench.db

# Logging
LOG_LEVEL=info
LOG_FORMAT=json
```

### MCP Client Configuration

Add to your MCP client's configuration (e.g., Claude Desktop):

```json
{
  "mcpServers": {
    "intellibench": {
      "command": "node",
      "args": ["path/to/MCP_IntelliBench/dist/server/index.js"],
      "env": {
        "MCP_SERVER_PORT": "3000"
      }
    }
  }
}
```

## 📊 Benchmarks

### Challenge Categories

#### 1. Code Generation (10 challenges)
- Basic function implementation
- Data structure operations
- API client creation
- File processing
- Async/await patterns

#### 2. Bug Detection & Fixing (8 challenges)
- Logic errors
- Memory leaks
- Race conditions
- Type mismatches
- Security vulnerabilities

#### 3. Code Refactoring (6 challenges)
- DRY principle application
- SOLID principles
- Design pattern implementation
- Performance optimization
- Readability improvement

#### 4. Algorithm Design (8 challenges)
- Sorting algorithms
- Graph algorithms
- Dynamic programming
- Tree traversal
- Search algorithms

#### 5. Security Analysis (4 challenges)
- SQL injection detection
- XSS vulnerability identification
- Authentication bypass
- Secure coding practices

### Scoring Methodology

| Metric | Weight | Description |
|--------|--------|-------------|
| **Correctness** | 40% | Does the code produce correct output? |
| **Efficiency** | 20% | Time and space complexity |
| **Code Quality** | 20% | Readability, maintainability, best practices |
| **Completeness** | 10% | Handles edge cases and errors |
| **Creativity** | 10% | Novel approaches and solutions |

### Difficulty Levels

- 🟢 **Easy** (1-3): Basic concepts, straightforward solutions
- 🟡 **Medium** (4-6): Moderate complexity, multiple approaches
- 🔴 **Hard** (7-9): Advanced concepts, optimization required
- ⚫ **Expert** (10): Research-level complexity

## 🔧 API Reference

### MCP Tools

#### `intellibench_start_session`
Start a new benchmark session.

```typescript
// Input
{
  sessionName?: string;
  categories?: string[];
  difficulty?: "easy" | "medium" | "hard" | "expert" | "all";
}

// Output
{
  sessionId: string;
  totalChallenges: number;
  estimatedTime: string;
}
```

#### `intellibench_get_challenge`
Retrieve the next challenge in the session.

```typescript
// Input
{
  sessionId: string;
}

// Output
{
  challengeId: string;
  category: string;
  difficulty: number;
  title: string;
  description: string;
  requirements: string[];
  hints?: string[];
  timeLimit: number;
}
```

#### `intellibench_submit_solution`
Submit a solution for evaluation.

```typescript
// Input
{
  sessionId: string;
  challengeId: string;
  solution: string;
  language?: string;
}

// Output
{
  score: number;
  maxScore: number;
  breakdown: {
    correctness: number;
    efficiency: number;
    codeQuality: number;
    completeness: number;
    creativity: number;
  };
  feedback: string;
  suggestions: string[];
  passed: boolean;
}
```

#### `intellibench_get_results`
Get comprehensive session results.

```typescript
// Input
{
  sessionId: string;
}

// Output
{
  overallScore: number;
  percentile: number;
  categoryScores: Record<string, number>;
  strengths: string[];
  weaknesses: string[];
  recommendations: string[];
  completedChallenges: number;
  totalTime: string;
}
```

#### `intellibench_leaderboard`
Get the current leaderboard.

```typescript
// Input
{
  category?: string;
  limit?: number;
  timeframe?: "daily" | "weekly" | "monthly" | "all";
}

// Output
{
  entries: Array<{
    rank: number;
    aiModel: string;
    score: number;
    completedAt: string;
  }>;
}
```

### MCP Resources

#### `intellibench://challenges`
List all available challenges.

#### `intellibench://sessions/{sessionId}`
Get session details.

#### `intellibench://results/{sessionId}`
Get session results.

#### `intellibench://leaderboard`
Get current leaderboard.

### MCP Prompts

#### `benchmark_introduction`
Comprehensive introduction to the benchmark system.

#### `challenge_tips`
Tips for approaching challenges effectively.

#### `score_interpretation`
Guide to understanding scores and feedback.

## 🎨 Dashboard

The dashboard provides a modern web interface for visualizing benchmark results.

### Features

- 📊 Real-time score visualization
- 📈 Performance trend charts
- 🏆 Interactive leaderboard
- 📋 Detailed session history
- 🔍 Challenge browser
- 📱 Responsive design

### Starting the Dashboard

```bash
pnpm start:dashboard
```

Open http://localhost:8080 in your browser.

## 🧪 Testing

```bash
# Run all tests
pnpm test

# Run with coverage
pnpm test:coverage

# Run specific test suite
pnpm test:unit
pnpm test:integration
pnpm test:e2e
```

## 📁 Project Structure

```
MCP_IntelliBench/
├── src/
│   ├── server/              # MCP Server implementation
│   │   ├── index.ts         # Server entry point
│   │   ├── tools/           # MCP Tools
│   │   ├── resources/       # MCP Resources
│   │   ├── prompts/         # MCP Prompts
│   │   └── handlers/        # Request handlers
│   ├── core/                # Core business logic
│   │   ├── benchmark/       # Benchmark engine
│   │   ├── scoring/         # Scoring engine
│   │   ├── challenges/      # Challenge management
│   │   └── analytics/       # Analytics engine
│   ├── data/                # Data layer
│   │   ├── challenges/      # Challenge definitions
│   │   ├── solutions/       # Reference solutions
│   │   └── testcases/       # Test cases
│   ├── dashboard/           # Web dashboard
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   └── styles/          # CSS styles
│   └── shared/              # Shared utilities
│       ├── types/           # TypeScript types
│       ├── utils/           # Utility functions
│       └── constants/       # Constants
├── tests/                   # Test files
├── docs/                    # Documentation
├── .github/                 # GitHub workflows
├── package.json
├── tsconfig.json
├── vitest.config.ts
└── README.md
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone the repository
git clone https://quangminh1212/MCP_IntelliBench.git
cd MCP_IntelliBench

# Install dependencies
pnpm install

# Start development
pnpm dev
```

### Code Standards

- TypeScript strict mode
- ESLint + Prettier for formatting
- Vitest for testing
- Conventional commits

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [Anthropic](https://anthropic.com) for the Model Context Protocol
- [MCP-Bench](https://MCP-bench) for inspiration
- All contributors and testers

---

<div align="center">

**Made with ❤️ for the AI community**

[⬆ Back to Top](#-mcp-intellibench)

</div>