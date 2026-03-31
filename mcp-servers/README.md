# 🔌 MCP Servers

Model Context Protocol servers — standardized tool connectors that give LLMs access to the real world.

## Overview

This directory contains **30 submodules** of MCP server implementations that connect AI agents to external tools and data sources via the standardized Model Context Protocol. From search engines and databases to code execution environments and cloud services — these servers enable AI to take action beyond text generation.

## Submodules (30)

### Official SDKs & Collections
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`mcp-typescript-sdk`](https://github.com/modelcontextprotocol/typescript-sdk) | MCP | Official TypeScript MCP SDK |
| [`mcp-python-sdk`](https://github.com/modelcontextprotocol/python-sdk) | MCP | Official Python MCP SDK |
| [`official-servers`](https://github.com/modelcontextprotocol/servers) | MCP | Reference MCP server implementations |
| [`MCPRules`](https://github.com/nicobailon/MCPRules) | nicobailon | Rules and patterns for MCP development |

### Search & Web
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`brave-search`](https://github.com/nicobailon/brave-search-mcp) | MCP | Web search via Brave Search API |
| [`exa-mcp`](https://github.com/exa-labs/exa-mcp-server) | Exa | AI-native semantic search |
| [`apify-mcp`](https://github.com/apify/actors-mcp-server) | Apify | Web scraping and automation actors |

### Developer Tools
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`github-mcp-server`](https://github.com/github/github-mcp-server) | GitHub | Official GitHub MCP server |
| [`docker-mcp`](https://github.com/docker/docker-mcp) | Docker | Container management via MCP |
| [`playwright-mcp`](https://github.com/nicobailon/playwright-mcp) | Microsoft | Browser automation via Playwright |
| [`chrome-devtools-mcp`](https://github.com/nicobailon/chrome-devtools-mcp) | nicobailon | Chrome DevTools Protocol access |
| [`mcp-chrome`](https://github.com/nicobailon/mcp-chrome) | nicobailon | Chrome browser control |
| [`cli-mcp-server`](https://github.com/nicobailon/cli-mcp-server) | nicobailon | Terminal/CLI tool execution |
| [`cloudflare-mcp`](https://github.com/cloudflare/mcp-server-cloudflare) | Cloudflare | Cloudflare services management |
| [`context7`](https://github.com/nicobailon/context7) | nicobailon | Up-to-date documentation for LLMs |

### Vector Databases
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`chroma-mcp`](https://github.com/nicobailon/chroma-mcp) | nicobailon | Chroma vector DB operations |
| [`mcp-qdrant`](https://github.com/qdrant/mcp-server-qdrant) | Qdrant | Qdrant vector search |
| [`pinecone-mcp`](https://github.com/pinecone-io/pinecone-mcp) | Pinecone | Pinecone vector operations |
| [`milvus-mcp`](https://github.com/milvus-io/mcp-server-milvus) | Milvus | Milvus vector DB access |
| [`elasticsearch-mcp`](https://github.com/elastic/elasticsearch-mcp-server) | Elastic | Elasticsearch search and analytics |

### Databases & Storage
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`mongodb-mcp`](https://github.com/mongodb-labs/mongodb-mcp-server) | MongoDB | MongoDB database operations |
| [`redis-mcp`](https://github.com/redis/redis-mcp) | Redis | Redis cache and data operations |
| [`neo4j-mcp`](https://github.com/neo4j-labs/mcp-neo4j) | Neo4j | Graph database queries |
| [`supabase-mcp`](https://github.com/supabase-community/supabase-mcp) | Supabase | Supabase backend operations |
| [`notion-mcp`](https://github.com/nicobailon/notion-mcp) | nicobailon | Notion workspace access |

### Payments & SaaS
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`stripe-mcp`](https://github.com/stripe/agent-toolkit) | Stripe | Payment processing via Stripe API |
| [`auth0-mcp`](https://github.com/auth0/auth0-mcp-server) | Auth0 | Identity and access management |

### Observability
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`agentops-mcp`](https://github.com/AgentOps-AI/agentops-mcp) | AgentOps | Agent observability and monitoring |
| [`langfuse-mcp`](https://github.com/langfuse/mcp-server-langfuse) | Langfuse | LLM observability server |

### Agent Enhancement
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`mcp-feedback-enhanced`](https://github.com/nicobailon/mcp-feedback-enhanced) | nicobailon | Human-in-the-loop feedback for agents |

## Key Capabilities

| Category | Servers |
|----------|---------|
| **Search** | brave-search, exa-mcp |
| **Code/Dev** | github-mcp-server, docker-mcp, playwright-mcp |
| **Vector DB** | chroma-mcp, mcp-qdrant, pinecone-mcp, milvus-mcp |
| **Databases** | mongodb-mcp, redis-mcp, neo4j-mcp, supabase-mcp |
| **Cloud** | cloudflare-mcp, auth0-mcp |
| **Payments** | stripe-mcp |

## Usage

```bash
# Init the official MCP servers
git submodule update --init --depth 1 mcp-servers/official-servers

# Init the GitHub MCP server
git submodule update --init --depth 1 mcp-servers/github-mcp-server

# Configure in Claude Desktop
# Add to claude_desktop_config.json:
# { "mcpServers": { "github": { "command": "npx", "args": ["@modelcontextprotocol/server-github"] } } }
```
