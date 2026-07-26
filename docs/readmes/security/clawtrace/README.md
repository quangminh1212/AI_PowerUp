<!-- source: https://github.com/alexgutscher26/ClawTrace.git sha: ac9805ea1a788182123e540c4d5c6c9b01c5a0fd readme: main/README.md -->
# alexgutscher26/ClawTrace

Stop polling. Start listening. ClawTrace delivers 0.1ms telemetry across your agent swarms. Zero-knowledge security, remote execution, and policy guardrails as standard.

---

# ⚡ ClawTrace Orchestrator

> **Orchestrate your silicon fleet with sub-millisecond precision.**

ClawTrace is a high-performance, secure, and scalable command center designed for managing autonomous AI agent swarms with sub-millisecond precision. It bridges the gap between human operators and distributed agent collectives, providing real-time telemetry, remote execution, and deep policy enforcement in a single, beautiful interface.

---

## ✨ Key Features

- **🚀 Real-time Telemetry**: Sub-millisecond latency heartbeat system via WebSockets. Monitor CPU, Memory, and Latency across thousands of nodes concurrently.
- **🔐 Zero-Knowledge Security**: End-to-End Encryption (E2EE) powered by AES-256-GCM. Agent configurations and secrets are encrypted in the browser and never leave the edge in plain text.
- **📡 Remote Execution**: Instantly dispatch shell commands or scripts to any individual agent or entire fleets. Stream `stdout`/`stderr` back to the console in real-time.
- **🔌 Plugin Architecture**: Seamlessly extend agent capabilities with custom Python/JS scripts for specialized metric collection.
- **🔍 Auto-Discovery**: Zero-config pairing via local network scanning to find ClawTrace gateways instantly.
- **🛡️ Policy Engine**: Define granular "Guardrails" and profiles (Dev, Ops, Exec) to control agent capabilities, resource usage, and network access.
- **📦 Single Binary / Edge First**: Agents are lightweight daemons that run on Linux, macOS, and Windows. No complex dependencies, just pure performance.
- **🎨 Premium UX**: A brutalist, grid-based interface with glassmorphism aesthetics, designed for focus and operational clarity.

---

## 🛠️ Technology Stack

- **Framework**: [Next.js](https://nextjs.org/) (App Router)
- **Database / Auth**: [Supabase](https://supabase.com/)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Components**: [Shadcn/UI](https://ui.shadcn.com/)
- **Icons**: [Lucide React](https://lucide.dev/)
- **Notifications**: [Sonner](https://sonner.steveney.com/)

---

## 🚦 Getting Started

### 1. Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- [Bun](https://bun.sh/) (Recommended) or NPM
- A [Supabase](https://supabase.com/) Project

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/alexgutscher26/fleet
cd fleet

# Install dependencies
bun install

# Configure environment variables
cp .env.example .env
# Edit .env with your Supabase credentials
```

### 3. Development

```bash
bun dev
```

Open [http://localhost:3000](http://localhost:3000) to enter the console.

---

## 📖 Architecture

```text
[CONTROL PLANE] <---> [GATEWAY] <---> [AGENTS]
      |                   |
  [DASHBOARD]        [DATABASE]
```

- **Control Plane**: Manages API requests, authentication, and global state.
- **Gateway**: High-performance WebSocket server handling agent connections.
- **Agents**: Lightweight daemons running on edge compute (EC2, Droplets, Bare Metal).

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

Built with ⚡ by the **ClawTrace** team.
