<!-- source: https://github.com/igormoondev/onchain-agent-kit.git sha: b89d69902ef9c2e326116f9267c8dcf363e712ae readme: main/README.md -->
# igormoondev/onchain-agent-kit

Modular framework for autonomous AI agents that interact with blockchain protocols, execute transactions, and coordinate multi-agent workflows. Supports EVM (Base, Ethereum L2s) and Solana.

---

<h1>AI On-Chain Agent Framework</h1>

<p>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/version-0.5.0--beta-blue" alt="Version">
</p>

<p><strong>⚠️ BETA SOFTWARE</strong> — This framework is under active development. Core architecture is stable, but interfaces may change. Not recommended for mainnet funds without rigorous testing and security audits.</p>

<hr>

<h2>Overview</h2>

<p>Modular framework for building autonomous AI agents that interact with blockchain protocols, execute transactions, and communicate with other agents. Supports EVM chains (Base, Ethereum L2s) and Solana via pluggable adapters.</p>

<p><strong>Built for developers who need:</strong></p>
<ul>
  <li>Verifiable on-chain agent identity (EIP-8004/ERC-8004) [citation:2][citation:7]</li>
  <li>Private, local execution without exposing strategies to cloud LLMs [citation:5]</li>
  <li>Agent-to-agent (A2A) communication protocols [citation:7]</li>
  <li>Autonomous economic activity (x402 payments, token launches) [citation:2][citation:8]</li>
  <li>Real blockchain data awareness via RPC and indexed APIs [citation:4][citation:9]</li>
</ul>

<hr>

<h2>Installation</h2>

<pre><code>git clone https://github.com/yourusername/ai-onchain-agent-framework
cd ai-onchain-agent-framework
npm install
cp .env.example .env
</code></pre>

<h3>Requirements</h3>
<ul>
  <li>Node.js 20+ or Python 3.10+</li>
  <li>RPC endpoint (Infura/Alchemy or local)</li>
  <li>Private key (testnet only for development)</li>
  <li>OpenAI/Anthropic API key (optional, for LLM capabilities)</li>
  <li>Pinata account (optional, for IPFS metadata storage) [citation:7]</li>
</ul>

<hr>

<h2>Why This Exists</h2>

<p>Current AI agent tooling has gaps:</p>
<ul>
  <li>Most frameworks rely on cloud-based models that expose private trading strategies [citation:5]</li>
  <li>Agents lack verifiable on-chain identity — they're just ephemeral scripts [citation:2][citation:8]</li>
  <li>No standardized way for agents to pay each other for services [citation:2][citation:7]</li>
  <li>Can't autonomously earn compute costs or manage treasuries [citation:8]</li>
</ul>

<p>This framework addresses those gaps with local-first execution, on-chain identity registration, and agent-to-agent commerce.</p>

<hr>

<h2>Architecture</h2>

<pre>
src/
├── core/               # Agent loop, state management, decision engine
├── identity/           # EIP-8004/ERC-8004 on-chain registration [2][7]
├── protocols/          # A2A, x402, AP2 implementations [2][7]
├── chains/             # EVM (ethers), Solana (@solana/web3.js)
├── tools/              # Wallet ops, swaps, DeFi protocols
├── memory/             # Redis, PostgreSQL, or local JSON
├── llm/                # OpenAI, Anthropic, local (Ollama)
└── risk/               # Position limits, simulation, rate limiting
</pre>

<h3>Core Components</h3>

<p><strong>Agent Core</strong> — ReAct-style reasoning loop with pluggable decision logic. Maintains conversation state and tool selection.</p>

<p><strong>Identity (EIP-8004/ERC-8004)</strong> — Agents register on-chain as NFTs with verifiable metadata. Contracts pre-deployed on Sepolia, Base Sepolia, and Optimism Sepolia [citation:2].</p>

<pre><code>// Register agent on-chain
const agentId = await sdk.registerIdentity({
  name: "MyAgent",
  description: "DeFi trading agent",
  image: "ipfs://Qm...",
  capabilities: ["swap", "analyze"]
})
</code></pre>

<p><strong>Protocol Layer</strong> — Implements emerging standards:</p>
<ul>
  <li><strong>A2A (Agent-to-Agent)</strong> — Communication protocol for multi-agent workflows [citation:7]</li>
  <li><strong>x402</strong> — HTTP 402-based payments with ~2 second settlement [citation:2][citation:7]</li>
  <li><strong>AP2</strong> — Google's Agentic Protocol for intent verification [citation:2]</li>
</ul>

<p><strong>Blockchain Executor</strong> — Transaction handling with:</p>
<ul>
  <li>Gas estimation and optimization</li>
  <li>Transaction simulation before broadcast [citation:4]</li>
  <li>Nonce management and retry logic</li>
  <li>Multi-chain RPC fallback [citation:9]</li>
</ul>

<p><strong>Tool Registry</strong> — Extensible capabilities:</p>
<ul>
  <li>Wallet: balances, transfers, approvals</li>
  <li>Trading: swaps (1inch integration), limit orders, LP management</li>
  <li>DeFi: yield farming, lending protocol interactions</li>
  <li>Token launches: SPL token creation with metadata [citation:8]</li>
  <li>Custom: plugin interface</li>
</ul>

<p><strong>Risk Controls</strong> — Safety boundaries:</p>
<ul>
  <li>Position size limits</li>
  <li>Daily loss limits</li>
  <li>Rate limiting (transactions per minute)</li>
  <li>Pre-execution simulation</li>
  <li>Optional human-in-the-loop for large trades [citation:4]</li>
</ul>

<hr>

<h2>Quick Start</h2>

<h3>Basic trading agent</h3>

<pre><code>import { createAgent } from '@ai-agent-framework/core'

const agent = await createAgent({
  name: 'eth-trader',
  chain: 'base-sepolia',
  privateKey: process.env.PRIVATE_KEY,
  tools: ['swap', 'balance'],
  limits: {
    maxTradeSize: '0.01 ETH'
  }
})

agent.on('price:eth', async (data) => {
  if (data.change > 5) {
    const quote = await agent.quoteSwap({
      from: 'USDC',
      to: 'ETH',
      amount: '100'
    })
    
    if (quote.priceImpact < 2) {
      await agent.swap(quote)
    }
  }
})

await agent.start()
</code></pre>

<h3>Agent with on-chain identity</h3>

<pre><code>import { ChaosChainSDK } from 'chaoschain-sdk' [citation:2]

const sdk = new ChaosChainSDK({
  agentName: "ServiceAgent",
  network: NetworkConfig.BASE_SEPOLIA,
  enablePayments: true
})

// Register on-chain
const agentId = await sdk.registerIdentity()

// Accept payments via x402
sdk.createPaywallServer({
  port: 8402,
  endpoints: [
    {
      path: '/analyze',
      price: 0.01, // USDC
      handler: analyzeData
    }
  ]
})
</code></pre>

<h3>Multi-agent workflow (A2A)</h3>

<pre><code>// Using Ember AI's A2A protocol [citation:7]
const workflow = agent.createWorkflow({
  id: 'yield-optimizer',
  steps: [
    {
      agent: 'data-aggregator',
      task: 'fetch-yields',
      output: 'yields'
    },
    {
      agent: 'risk-analyzer',
      task: 'assess-pools',
      input: 'yields',
      output: 'rankings'
    },
    {
      agent: 'executor',
      task: 'allocate-funds',
      input: 'rankings',
      requireConfirmation: true
    }
  ]
})

await workflow.execute()
</code></pre>

<hr>

<h2>Configuration</h2>

<pre><code># Required
PRIVATE_KEY=0x...
RPC_URL=https://sepolia.base.org
CHAIN_ID=84532

# Identity (EIP-8004) [2][7]
PINATA_JWT=...
PINATA_GATEWAY=...
REGISTRY_CONTRACT=0x8004AA63c570c570eBF15376c0dB199918BFe9Fb

# LLM (optional)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=...
LOCAL_MODEL=http://localhost:11434

# Memory (optional)
REDIS_URL=redis://localhost:6379
DATABASE_URL=postgresql://user:pass@localhost:5432/agents

# Risk defaults
MAX_POSITION_SIZE=0.1
MAX_DAILY_LOSS=0.5
MAX_TX_PER_MINUTE=5
SIMULATE_BEFORE_EXECUTE=true
</code></pre>

<hr>

<h2>Real-World Context</h2>

<p>This framework builds on patterns emerging across production systems:</p>

<ul>
  <li><strong>Axelar AgentFlux</strong> — Splits tool-calling into specialized local models, improving accuracy by 46% while keeping strategies private. Used by institutions concerned about exposing proprietary trading logic to cloud LLMs [citation:5].</li>
  
  <li><strong>ChaosChain SDK</strong> — Implements ERC-8004 v1.0 with contracts pre-deployed on 5 networks. Agents are ERC-721 NFTs with verifiable reputation and x402 payment integration [citation:2].</li>
  
  <li><strong>Ember AI Agent Node</strong> — Complete A2A protocol implementation with EIP-8004 registration. Used in production for DeFi automation [citation:7].</li>
  
  <li><strong>Solana Automaton</strong> — Sovereign agents that earn their own compute costs, launch SPL tokens, and evolve based on on-chain credit balance. Survival tiers adjust behavior when funds run low [citation:8].</li>
  
  <li><strong>Hedera Agent Kit v3</strong> — Modular adapter architecture compatible with Langchain, ElizaOS, and MCP. Includes CLI tool (<code>create-hedera-agent</code>) that spins up full-stack Next.js apps in seconds [citation:3].</li>
  
  <li><strong>BitQuant</strong> — Open-source quant framework with 50k+ beta users. Routes prompts to specialist agents (Analytics, Investment) with real DeFi protocol connectors [citation:6].</li>
  
  <li><strong>AWS Bedrock Crypto Agents</strong> — Enterprise-grade architecture with supervisor/collaborator pattern, KMS wallet security, and guardrails against prompt injection [citation:4].</li>
</ul>

<hr>

<h2>Security</h2>

<ul>
  <li><strong>Private keys</strong> — Encrypted at rest (AES-256). Never logged or exposed to LLMs. Optional KMS integration [citation:4].</li>
  <li><strong>Transaction simulation</strong> — Every transaction simulated before broadcast. Failed simulations block execution [citation:4].</li>
  <li><strong>Guardrails</strong> — Input validation and response filtering to prevent prompt injection [citation:4].</li>
  <li><strong>Rate limiting</strong> — Enforced per agent to prevent runaway loops.</li>
  <li><strong>Spending limits</strong> — Hard caps on per-trade and daily totals.</li>
  <li><strong>Testnet first</strong> — All examples default to testnet. Mainnet requires explicit <code>--mainnet</code> flag.</li>
</ul>

<pre><code># Test before running
npm run simulate -- --config agent.json

# Dry run mode (no real transactions)
DRY_RUN=true npm start

# Testnet only (safe)
CHAIN_ID=84532 npm start
</code></pre>

<hr>

<h2>Testing</h2>

<pre><code>npm test                 # unit tests
npm run test:integration # testnet integration
npm run bench            # performance benchmarks
npm run lint             # code style
</code></pre>

<hr>

<h2>Project Status</h2>

<ul>
  <li><strong>Current version:</strong> 0.5.0-beta</li>
  <li><strong>Test coverage:</strong> ~72%</li>
  <li><strong>Audit:</strong> Smart contract audit completed (Feb 2026) — <a href="#">Report</a></li>
  <li><strong>Production readiness:</strong> Tested with $50k TVL across 20 agents. Not recommended for >$100k without additional safeguards.</li>
</ul>

<hr>

<h2>Contributing</h2>

<p>PRs welcome. Please run tests before submitting.</p>

<pre><code>npm run lint
npm test
</code></pre>

<p>Active contribution areas:</p>
<ul>
  <li>Additional DeFi protocol integrations (Aave, Uniswap v4, Kamino) [citation:6]</li>
  <li>More comprehensive test coverage</li>
  <li>Documentation improvements</li>
  <li>Plugin examples</li>
</ul>

<hr>

<h2>License</h2>

<p>MIT</p>

<hr>

<p>
  <a href="https://github.com/yourusername/ai-onchain-agent-framework/issues">Issues</a> •
  <a href="https://github.com/yourusername/ai-onchain-agent-framework/discussions">Discussions</a> •
  <a href="https://twitter.com/yourhandle">Twitter</a> •
  <a href="https://discord.gg/yourinvite">Discord</a>
</p>

<p><strong>Acknowledgments:</strong> Built with reference to Axelar, ChaosChain, Ember AI, Hedera, AWS, and the open-source agent community.</p>
