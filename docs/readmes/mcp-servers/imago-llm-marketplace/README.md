<!-- source: https://github.com/maxrihter/imago-LLM-marketplace.git sha: b837f21819ea2b1aeb0527c24773d3db4bfe1cbd readme: main/README.md -->
# maxrihter/imago-LLM-marketplace

AI Inference Gateway native to TON/Telegram: OpenAI-compatible API, TON micropayments, MCP server, Telegram Mini App

---

<p align="center">
  <img src="assets/banner_imago.png" alt="IMAGO: First LLM Marketplace on Cocoon and TON" width="100%"/>
</p>

<h3 align="center">First LLM Marketplace on Cocoon and TON</h3>

<p align="center">
  Cocoon TEE privacy by default &bull; pay with TON &bull; MCP-native for AI agents
</p>

<p align="center">
  <a href="https://platform.openai.com/docs/api-reference"><img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI Compatible"/></a>
  <a href="https://ton.org"><img src="https://img.shields.io/badge/TON-Native-0088CC?style=for-the-badge&logo=ton&logoColor=white" alt="TON Native"/></a>
  <a href="https://cocoon.build"><img src="https://img.shields.io/badge/Cocoon-TEE%20Privacy-7C3AED?style=for-the-badge" alt="Cocoon TEE"/></a>
  <a href="https://modelcontextprotocol.io"><img src="https://img.shields.io/badge/MCP-Server-FF6B35?style=for-the-badge" alt="MCP Server"/></a>
  <a href="https://core.telegram.org/bots/webapps"><img src="https://img.shields.io/badge/Telegram-Mini%20App-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Mini App"/></a>
  <a href="https://tact-lang.org"><img src="https://img.shields.io/badge/Tact-Smart%20Contracts-1E40AF?style=for-the-badge" alt="Tact"/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="MIT License"/>
  <img src="https://img.shields.io/badge/TypeScript-5.x-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>
  <img src="https://img.shields.io/badge/Node.js-22+-339933?style=flat-square&logo=node.js&logoColor=white" alt="Node.js"/>
  <img src="https://img.shields.io/badge/TON-Mainnet-0088CC?style=flat-square" alt="TON Mainnet"/>
</p>

---

## The Problem

TON has 1 billion+ Telegram users and the fastest-growing L1 blockchain. Yet developers building AI-powered bots and agents on TON face critical gaps:

- **No agent infrastructure**: AI agents cannot autonomously discover, call, and pay for LLM inference on TON
- **Payment friction**: every AI provider requires credit cards and KYC, incompatible with on-chain payments
- **Zero privacy**: every prompt is visible to the provider, with no hardware-level protection

## The Solution

**IMAGO** is an AI inference gateway built on Cocoon and TON. One OpenAI-compatible endpoint, TON payments with zero KYC, and an MCP server so AI agents can autonomously call models and pay with TON credits. Private inference via Cocoon TEE where even IMAGO cannot see your prompts.

## Key Features

| Feature | Description |
|---------|-------------|
| **OpenAI-Compatible API** | Drop-in replacement: change one line of code (`base_url`) and it works |
| **Multi-provider Models** | GPT-4o, Claude, Llama, Qwen, Gemini and more via OpenRouter |
| **TON Micropayments** | Deposit TON → get credits → pay per token. No credit cards needed |
| **MCP Server** | AI agents (Claude, GPT) can autonomously call inference and pay in TON |
| **Cocoon TEE Privacy** | Hardware-isolated inference: prompts are encrypted, even IMAGO can't see them |
| **Telegram Mini App** | Full dashboard: models, balance, API keys, chat, right inside Telegram |
| **Smart Contract** | Tact contract on TON mainnet for trustless deposits |
| **Streaming** | Full SSE streaming support, identical to OpenAI API format |

## Architecture

<p align="center">
  <img src="assets/architecture.svg" alt="IMAGO Architecture" width="100%"/>
</p>

## Agent Infrastructure

IMAGO is an [MCP](https://modelcontextprotocol.io)-native inference gateway. AI agents (Claude Desktop, Claude Code, or any MCP client) can autonomously discover models, run inference, check balance, and manage payments on TON.

### MCP Tools

| Tool | What the agent does |
|------|---------------------|
| `imago_list_models` | Discover available models with context length and per-token pricing |
| `imago_chat` | Send inference requests to any model (GPT-4o, Claude, Llama, Cocoon TEE) |
| `imago_get_balance` | Check remaining credits before making calls |
| `imago_get_deposit_info` | Get the TON deposit address and current exchange rate |

### How an Agent Uses IMAGO

```
1. Agent receives a task requiring specialized AI
2. Calls imago_list_models → discovers models and pricing
3. Calls imago_get_balance → verifies sufficient credits
4. Calls imago_chat(model, messages) → gets inference result
5. Credits are deducted automatically per token (atomic, Postgres-backed)
6. Agent continues its workflow with the result
```

### Why This Matters

Today, AI agents have no way to pay for inference on TON. Credit cards and KYC make autonomous agent-to-service payments impossible. IMAGO solves this:

- **Agent autonomy**: the agent decides which model to use, calls it, and pays -- all without human intervention
- **On-chain payments**: TON credits are deposited via smart contract, no KYC, no credit cards
- **Model selection**: agents pick the right model for each sub-task (cheap for simple queries, powerful for reasoning, private for sensitive data via Cocoon TEE)
- **Standard protocol**: built on MCP, works with Claude Desktop, Claude Code, and any MCP-compatible client

## Quick Start

### Use the API (2 lines of code)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://imago.market/v1",
    api_key="sk-imago-YOUR_KEY"  # Get from Telegram Mini App
)

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello from TON!"}]
)
print(response.choices[0].message.content)
```

### Use with TypeScript / Node.js

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://imago.market/v1",
  apiKey: "sk-imago-YOUR_KEY",
});

const response = await client.chat.completions.create({
  model: "openai/gpt-4o-mini",
  messages: [{ role: "user", content: "Hello from TON!" }],
});
console.log(response.choices[0].message.content);
```

### Use with cURL

```bash
curl https://imago.market/v1/chat/completions \
  -H "Authorization: Bearer sk-imago-YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-4o-mini",
    "messages": [{"role": "user", "content": "Hello!"}],
    "stream": true
  }'
```

### Use with MCP (Claude Desktop / Claude Code)

IMAGO ships an MCP server so AI agents can discover models, call inference, and pay with TON autonomously.

```bash
# Clone and build the MCP server
git clone https://github.com/maxrihter/imago-LLM-marketplace.git
cd imago/packages/mcp-server && npm install && npm run build
```

Add to your MCP config (`claude_desktop_config.json` or `.claude/settings.json`):

```json
{
  "mcpServers": {
    "imago": {
      "command": "node",
      "args": ["/path/to/imago/packages/mcp-server/build/index.js"],
      "env": {
        "IMAGO_API_KEY": "sk-imago-YOUR_KEY"
      }
    }
  }
}
```

Now Claude can call AI models and pay with your TON credits autonomously. The agent has 4 tools: `imago_chat`, `imago_list_models`, `imago_get_balance`, `imago_get_deposit_info`.

### Get Your API Key

1. Open [@imago_tonbot](https://t.me/imago_tonbot) in Telegram
2. Connect your TON wallet (2 taps)
3. Deposit TON for credits
4. Generate an API key. Done!

## How It Works

```
1. Developer gets API key via Telegram Mini App
2. Deposits TON → credits are added instantly (on-chain polling)
3. Makes API calls (OpenAI-compatible) → credits deducted per token
4. AI agents use MCP to call inference autonomously
5. Cocoon TEE models available for privacy-sensitive workloads
```

### Payment Flow

```
User sends TON → Smart Contract → TonCenter polling (15s) →
  → Credits added (Postgres atomic) → Redis cache invalidated →
    → API calls deduct credits per token → Settlement
```

## Comparison

| Feature | IMAGO | OpenRouter | LiteLLM | Together.ai |
|---------|-------|-----------|---------|-------------|
| OpenAI-compatible API | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| First on Cocoon TEE | :white_check_mark: | :x: | :x: | :x: |
| TON/Telegram native | :white_check_mark: | :x: | :x: | :x: |
| Decentralized payments | :white_check_mark: | :x: | :x: | :x: |
| MCP server for agents | :white_check_mark: | :x: | :x: | :x: |
| Hardware-level privacy (TEE) | :white_check_mark: | :x: | :x: | :x: |
| Telegram Mini App | :white_check_mark: | :x: | :x: | :x: |
| Self-hostable | :white_check_mark: | :x: | :white_check_mark: | :x: |

## Project Structure

```
imago/
├── packages/
│   ├── api/              # Fastify API gateway (Node.js 22+)
│   │   ├── src/
│   │   │   ├── routes/   # /v1/chat, /v1/models, /auth
│   │   │   ├── services/ # OpenRouter, Cocoon, credits, TON poller
│   │   │   ├── middleware/# Auth, Telegram initData validation
│   │   │   └── utils/    # TON address normalization
│   │   └── prisma/       # Database schema
│   ├── tma/              # React Telegram Mini App
│   │   └── src/
│   │       ├── pages/    # 8 pages: Home, Models, Chat, Deposit...
│   │       ├── components/# 20+ UI components
│   │       └── lib/      # Hooks, utilities
│   ├── contracts/        # Tact smart contracts (TON mainnet)
│   │   ├── contracts/    # imago_market.tact
│   │   ├── scripts/      # Deploy scripts
│   │   └── tests/        # Blueprint tests
│   └── mcp-server/       # MCP server for AI agents
│       └── src/          # 4 tools: chat, list_models, get_balance, deposit_info
├── assets/               # Banner, architecture diagram
├── .env.example          # Environment template
└── package.json          # Monorepo workspace root
```

## API Reference

### Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/v1/chat/completions` | Bearer | Chat completion (streaming + non-streaming) |
| `GET` | `/v1/models` | none | List available models with pricing |
| `GET` | `/v1/usage` | Bearer | Usage logs by model |
| `POST` | `/auth/keys` | Telegram | Create API key |
| `GET` | `/auth/keys` | Telegram | List keys + balance |
| `DELETE` | `/auth/keys/:id` | Telegram | Deactivate API key |
| `GET` | `/auth/deposit` | none | Deposit instructions + live TON price |
| `GET` | `/health` | none | Health check (Postgres + Redis status) |

### MCP Tools

See [Agent Infrastructure](#agent-infrastructure) for detailed MCP tools documentation and agent workflow.

## Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| **API Gateway** | Node.js 22 + Fastify | High performance, OpenAI SDK compatible |
| **Database** | PostgreSQL + Prisma | ACID guarantees for credit balance |
| **Cache** | Redis | Rate limiting, credit cache, session data |
| **AI Backend** | OpenRouter + Cocoon TEE | Multi-provider routing + hardware privacy |
| **Frontend** | React 18 + Vite + Tailwind | TMA standard, fast builds |
| **Blockchain** | Tact + Blueprint | TON smart contracts |
| **MCP** | `@modelcontextprotocol/sdk` | Official MCP standard |
| **Wallet** | TON Connect 2.0 | Native Telegram wallet integration |

## Local Development

### Prerequisites

- Node.js 22+
- PostgreSQL 15+
- Redis 7+ (optional, works without it)

### Setup

```bash
# Clone the repository
git clone https://github.com/maxrihter/imago-LLM-marketplace.git
cd imago

# Install dependencies
npm install

# Copy environment config
cp .env.example packages/api/.env

# Set up the database
cd packages/api
npx prisma db push

# Start development servers
cd ../..
npm run dev:api   # API on :3000
npm run dev:tma   # TMA on :5173
```

## Security

- **No plaintext keys stored**: API keys are SHA-256 hashed before storage
- **Atomic credit operations**: PostgreSQL `UPDATE ... WHERE credits >= amount` prevents races
- **Telegram initData HMAC**: validates every TMA request via bot token
- **Redis resilience**: all Redis operations wrapped in try/catch, DB fallback
- **Rate limiting**: per-key + per-user + global limits
- **Streaming timeouts**: 120s abort with client disconnect detection
- **TON address normalization**: prevents duplicate accounts from address format variants

## Cocoon TEE: Private AI, First on Market

IMAGO is the **first LLM marketplace integrated with Cocoon TEE** on TON mainnet. No other marketplace offers hardware-isolated inference in the TON ecosystem.

Cocoon runs models inside Intel TDX (Trust Domain Extensions) enclaves. This is not software encryption: it is hardware-level isolation verified by cryptographic attestation (RA-TLS).

**What this means for you:**
- Prompts are encrypted in transit and at rest
- Neither IMAGO nor Cocoon operators can read your data
- Attestation proof verifies the enclave is genuine before every session

Available model: `cocoon/Qwen/Qwen3-32B`. Use it like any other model in the API: same endpoint, same SDK, same credits.

## TON Integration

- **Smart Contract**: `imago_market.tact` (Tact), handles deposits and owner withdrawals
- **TON Connect 2.0**: Native wallet connection in Telegram
- **TonCenter Polling**: Real-time deposit detection (15s intervals)
- **TON Price Feed**: Live TON/USD from Binance + CoinGecko with sanity bounds

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

[MIT](LICENSE). Free to use, fork, and build on.

---

<p align="center">
  <b>First LLM Marketplace on <a href="https://cocoon.build">Cocoon</a> and <a href="https://ton.org">TON</a></b>
  <br/>
  <a href="https://imago.market">imago.market</a> &bull; <a href="https://t.me/imago_tonbot">@imago_tonbot</a>
</p>
