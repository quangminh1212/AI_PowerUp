<!-- source: https://github.com/krishnakanthb13/everything-antigravity.git sha: bcf399361124fbf16a6ef8f71b56fee116334d14 readme: main/README.md -->
# krishnakanthb13/everything-antigravity

Welcome to the central repository for the **Antigravity** ecosystem. This project houses a collection of AI Agents, Task Skills, and Coding Rules designed to enhance autonomous coding workflows.

---

# Everything Antigravity

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Welcome to the central repository for the **Antigravity** ecosystem. This project houses a collection of AI Agents, Task Skills, and Coding Rules designed to enhance autonomous coding workflows.

Inspired by [everything-claude-code](https://github.com/krishnakanthb13/everything-claude-code)

## 🚀 Overview

Everything Antigravity provides a standardized framework for building and maintaining software using AI agents. It bridges the gap between high-level architectural decisions and low-level coding implementation.

## 📂 Project Structure

- **`agents/`**: Specialist AI persona definitions (Architect, Planner, Reviewer, etc.) with dedicated focus areas.
- **`docs/rules/`**: Hierarchical coding standards organized into "Common" principles and "Language-specific" extensions (Python, TypeScript, Go).
- **`skills/`**: Actionable, deep-dive reference materials for specific tasks (e.g., TDD workflows, performance optimization, security audits).

## 🛠️ Components

### 1. Agents
Specialized personas designed to handle specific stages of the software development lifecycle.
- **Architect**: System design and scalability.
- **Code Reviewer**: Quality assurance and security.
- **Planner**: Task decomposition and roadmapping.

### 2. Rules
Formalized standards that agents must follow.
- **Common**: Universal principles like immutability and error handling.
- **Language-Specific**: PEP 8 for Python, standard `go test` for Go, Zod validation for TypeScript.

### 3. Skills
Executable knowledge modules that provide agents with the "How-To" for complex operations.

## 📦 Installation

There are two ways to install the components from this repository:

### 1. Global Installation (Sync Everything)

This is the recommended way to keep your global AI environment (Claude and Antigravity) perfectly in sync with the latest rules, skills, and workflows.

- **Universal (Any OS)**: `python install.py`
- **Linux / macOS**: `./install.sh`
- **Windows (PowerShell)**: `.\install.ps1`

### 2. Selective Rule Installation

If you only want to install specific language rules without syncing skills or workflows:

```bash
cd docs/rules
# Use the installers inside this directory
python install.py python typescript
```

## 📜 Documentation

- [Code Documentation](./CODE_DOCUMENTATION.md) - Technical architecture of this repository.
- [Design Philosophy](./DESIGN_PHILOSOPHY.md) - The "Why" behind the Antigravity framework.
- [Rules Guide](./docs/rules/README.md) - Details on the rules hierarchy.
- [Contributing](./CONTRIBUTING.md) - How to help improve the project.

---
*Built with ❤️ for the future of agentic coding.*

© 2026 Krishna Kanth B. Licensed under the [GPL v3 License](./LICENSE).
