<p align="center">
  <a href="https://ollama.com">
    <img src="https://ollama/ollama/assets/3325447/0d0b44e2-8f4a-4e99-9b52-a5c1c741c8f7" alt="ollama" width="200"/>
  </a>
</p>

# Ollama

Start building with open models.

## Download

### macOS

```shell
curl -fsSL https://ollama.com/install.sh | sh
```

or [download manually](https://ollama.com/download/Ollama.dmg)

### Windows

```shell
irm https://ollama.com/install.ps1 | iex
```

or [download manually](https://ollama.com/download/OllamaSetup.exe)

### Linux

```shell
curl -fsSL https://ollama.com/install.sh | sh
```

[Manual install instructions](https://docs.ollama.com/linux#manual-install)

### Docker

The official [Ollama Docker image](https://hub.docker.com/r/ollama/ollama) `ollama/ollama` is available on Docker Hub.

### Libraries

- [ollama-python](https://ollama/ollama-python)
- [ollama-js](https://ollama/ollama-js)

### Community

- [Discord](https://discord.gg/ollama)
- [𝕏 (Twitter)](https://x.com/ollama)
- [Reddit](https://reddit.com/r/ollama)

## Get started

```
ollama
```

You'll be prompted to run a model or connect Ollama to your existing agents or applications such as `Claude Code`, `OpenClaw`, `OpenCode` , `Codex`, `Copilot`,  and more.

### Coding

To launch a specific integration:

```
ollama launch claude
```

Supported integrations include [Claude Code](https://docs.ollama.com/integrations/claude-code), [Codex](https://docs.ollama.com/integrations/codex), [Copilot CLI](https://docs.ollama.com/integrations/copilot-cli), [Droid](https://docs.ollama.com/integrations/droid), and [OpenCode](https://docs.ollama.com/integrations/opencode).

### AI assistant

Use [OpenClaw](https://docs.ollama.com/integrations/openclaw) to turn Ollama into a personal AI assistant across WhatsApp, Telegram, Slack, Discord, and more:

```
ollama launch openclaw
```

### Chat with a model

Run and chat with [Gemma 4](https://ollama.com/library/gemma4):

```
ollama run gemma4
```

See [ollama.com/library](https://ollama.com/library) for the full list.

See the [quickstart guide](https://docs.ollama.com/quickstart) for more details.

## REST API

Ollama has a REST API for running and managing models.

```
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4",
  "messages": [{
    "role": "user",
    "content": "Why is the sky blue?"
  }],
  "stream": false
}'
```

See the [API documentation](https://docs.ollama.com/api) for all endpoints.

### Python

```
pip install ollama
```

```python
from ollama import chat

response = chat(model='gemma4', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response.message.content)
```

### JavaScript

```
npm i ollama
```

```javascript
import ollama from "ollama";

const response = await ollama.chat({
  model: "gemma4",
  messages: [{ role: "user", content: "Why is the sky blue?" }],
});
console.log(response.message.content);
```

## Supported backends

- [llama.cpp](https://ggml-org/llama.cpp) project founded by Georgi Gerganov.

## Documentation

- [CLI reference](https://docs.ollama.com/cli)
- [REST API reference](https://docs.ollama.com/api)
- [Importing models](https://docs.ollama.com/import)
- [Modelfile reference](https://docs.ollama.com/modelfile)
- [Building from source](https://ollama/ollama/blob/main/docs/development.md)

## Community Integrations

> Want to add your project? Open a pull request.

### Chat Interfaces

#### Web

- [Open WebUI](https://open-webui/open-webui) - Extensible, self-hosted AI interface
- [Onyx](https://onyx-dot-app/onyx) - Connected AI workspace
- [LibreChat](https://danny-avila/LibreChat) - Enhanced ChatGPT clone with multi-provider support
- [Lobe Chat](https://lobehub/lobe-chat) - Modern chat framework with plugin ecosystem ([docs](https://lobehub.com/docs/self-hosting/examples/ollama))
- [NextChat](https://ChatGPTNextWeb/ChatGPT-Next-Web) - Cross-platform ChatGPT UI ([docs](https://docs.nextchat.dev/models/ollama))
- [Perplexica](https://ItzCrazyKns/Perplexica) - AI-powered search engine, open-source Perplexity alternative
- [big-AGI](https://enricoros/big-AGI) - AI suite for professionals
- [Lollms WebUI](https://ParisNeo/lollms-webui) - Multi-model web interface
- [ChatOllama](https://sugarforever/chat-ollama) - Chatbot with knowledge bases
- [Bionic GPT](https://bionic-gpt/bionic-gpt) - On-premise AI platform
- [Chatbot UI](https://ivanfioravanti/chatbot-ollama) - ChatGPT-style web interface
- [Hollama](https://fmaclen/hollama) - Minimal web interface
- [Chatbox](https://Bin-Huang/Chatbox) - Desktop and web AI client
- [chat](https://swuecho/chat) - Chat web app for teams
- [Ollama RAG Chatbot](https://datvodinh/rag-chatbot.git) - Chat with multiple PDFs using RAG
- [Tkinter-based client](https://chyok/ollama-gui) - Python desktop client

#### Desktop

- [Dify.AI](https://langgenius/dify) - LLM app development platform
- [AnythingLLM](https://Mintplex-Labs/anything-llm) - All-in-one AI app for Mac, Windows, and Linux
- [Maid](https://Mobile-Artificial-Intelligence/maid) - Cross-platform mobile and desktop client
- [Witsy](https://nbonamy/witsy) - AI desktop app for Mac, Windows, and Linux
- [Cherry Studio](https://kangfenmao/cherry-studio) - Multi-provider desktop client
- [Ollama App](https://JHubi1/ollama-app) - Multi-platform client for desktop and mobile
- [PyGPT](https://szczyglis-dev/py-gpt) - AI desktop assistant for Linux, Windows, and Mac
- [Alpaca](https://Jeffser/Alpaca) - GTK4 client for Linux and macOS
- [SwiftChat](https://aws-samples/swift-chat) - Cross-platform including iOS, Android, and Apple Vision Pro
- [Enchanted](https://AugustDev/enchanted) - Native macOS and iOS client
- [RWKV-Runner](https://josStorer/RWKV-Runner) - Multi-model desktop runner
- [Ollama Grid Search](https://dezoito/ollama-grid-search) - Evaluate and compare models
- [macai](https://Renset/macai) - macOS client for Ollama and ChatGPT
- [AI Studio](https://MindWorkAI/AI-Studio) - Multi-provider desktop IDE
- [Reins](https://ibrahimcetin/reins) - Parameter tuning and reasoning model support
- [ConfiChat](https://1runeberg/confichat) - Privacy-focused with optional encryption
- [LLocal.in](https://kartikm7/llocal) - Electron desktop client
- [MindMac](https://mindmac.app) - AI chat client for Mac
- [Msty](https://msty.app) - Multi-model desktop client
- [BoltAI for Mac](https://boltai.com) - AI chat client for Mac
- [IntelliBar](https://intellibar.app/) - AI-powered assistant for macOS
- [Kerlig AI](https://www.kerlig.com/) - AI writing assistant for macOS
- [Hillnote](https://hillnote.com) - Markdown-first AI workspace
- [Perfect Memory AI](https://www.perfectmemory.ai/) - Productivity AI personalized by screen and meeting history

#### Mobile

- [Ollama Android Chat](https://sunshine0523/OllamaServer) - One-click Ollama on Android

> SwiftChat, Enchanted, Maid, Ollama App, Reins, and ConfiChat listed above also support mobile platforms.

### Code Editors & Development

- [Cline](https://cline/cline) - VS Code extension for multi-file/whole-repo coding
- [Continue](https://continuedev/continue) - Open-source AI code assistant for any IDE
- [Void](https://voideditor/void) - Open source AI code editor, Cursor alternative
- [Copilot for Obsidian](https://logancyang/obsidian-copilot) - AI assistant for Obsidian
- [twinny](https://rjmacarthy/twinny) - Copilot and Copilot chat alternative
- [gptel Emacs client](https://karthink/gptel) - LLM client for Emacs
- [Ollama Copilot](https://bernardo-bruning/ollama-copilot) - Use Ollama as GitHub Copilot
- [Obsidian Local GPT](https://pfrankov/obsidian-local-gpt) - Local AI for Obsidian
- [Ellama Emacs client](https://s-kostyaev/ellama) - LLM tool for Emacs
- [orbiton](https://xyproto/orbiton) - Config-free text editor with Ollama tab completion
- [AI ST Completion](https://yaroslavyaroslav/OpenAI-sublime-text) - Sublime Text 4 AI assistant
- [VT Code](https://vinhnx/vtcode) - Rust-based terminal coding agent with Tree-sitter
- [QodeAssist](https://Palm1r/QodeAssist) - AI coding assistant for Qt Creator
- [AI Toolkit for VS Code](https://aka.ms/ai-tooklit/ollama-docs) - Microsoft-official VS Code extension
- [Open Interpreter](https://docs.openinterpreter.com/language-model-setup/local-models/ollama) - Natural language interface for computers

### Libraries & SDKs

- [LiteLLM](https://BerriAI/litellm) - Unified API for 100+ LLM providers
- [Semantic Kernel](https://microsoft/semantic-kernel/tree/main/python/semantic_kernel/connectors/ai/ollama) - Microsoft AI orchestration SDK
- [LangChain4j](https://langchain4j/langchain4j) - Java LangChain ([example](https://langchain4j/langchain4j-examples/tree/main/ollama-examples/src/main/java))
- [LangChainGo](https://tmc/langchaingo/) - Go LangChain ([example](https://tmc/langchaingo/tree/main/examples/ollama-completion-example))
- [Spring AI](https://spring-projects/spring-ai) - Spring framework AI support ([docs](https://docs.spring.io/spring-ai/reference/api/chat/ollama-chat.html))
- [LangChain](https://python.langchain.com/docs/integrations/chat/ollama/) and [LangChain.js](https://js.langchain.com/docs/integrations/chat/ollama/) with [example](https://js.langchain.com/docs/tutorials/local_rag/)
- [Ollama for Ruby](https://crmne/ruby_llm) - Ruby LLM library
- [any-llm](https://mozilla-ai/any-llm) - Unified LLM interface by Mozilla
- [OllamaSharp for .NET](https://awaescher/OllamaSharp) - .NET SDK
- [LangChainRust](https://Abraxas-365/langchain-rust) - Rust LangChain ([example](https://Abraxas-365/langchain-rust/blob/main/examples/llm_ollama.rs))
- [Agents-Flex for Java](https://agents-flex/agents-flex) - Java agent framework ([example](https://agents-flex/agents-flex/tree/main/agents-flex-llm/agents-flex-llm-ollama/src/test/java/com/agentsflex/llm/ollama))
- [Elixir LangChain](https://brainlid/langchain) - Elixir LangChain
- [Ollama-rs for Rust](https://pepperoni21/ollama-rs) - Rust SDK
- [LangChain for .NET](https://tryAGI/LangChain) - .NET LangChain ([example](https://tryAGI/LangChain/blob/main/examples/LangChain.Samples.OpenAI/Program.cs))
- [chromem-go](https://philippgille/chromem-go) - Go vector database with Ollama embeddings ([example](https://philippgille/chromem-go/tree/v0.5.0/examples/rag-wikipedia-ollama))
- [LangChainDart](https://davidmigloz/langchain_dart) - Dart LangChain
- [LlmTornado](https://lofcz/llmtornado) - Unified C# interface for multiple inference APIs
- [Ollama4j for Java](https://ollama4j/ollama4j) - Java SDK
- [Ollama for Laravel](https://cloudstudio/ollama-laravel) - Laravel integration
- [Ollama for Swift](https://mattt/ollama-swift) - Swift SDK
- [LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/ollama/) and [LlamaIndexTS](https://ts.llamaindex.ai/modules/llms/available_llms/ollama) - Data framework for LLM apps
- [Haystack](https://deepset-ai/haystack-integrations/blob/main/integrations/ollama.md) - AI pipeline framework
- [Firebase Genkit](https://firebase.google.com/docs/genkit/plugins/ollama) - Google AI framework
- [Ollama-hpp for C++](https://jmont-dev/ollama-hpp) - C++ SDK
- [PromptingTools.jl](https://svilupp/PromptingTools.jl) - Julia LLM toolkit ([example](https://svilupp.github.io/PromptingTools.jl/dev/examples/working_with_ollama))
- [Ollama for R - rollama](https://JBGruber/rollama) - R SDK
- [Portkey](https://portkey.ai/docs/welcome/integration-guides/ollama) - AI gateway
- [Testcontainers](https://testcontainers.com/modules/ollama/) - Container-based testing
- [LLPhant](https://theodo-group/LLPhant?tab=readme-ov-file#ollama) - PHP AI framework

### Frameworks & Agents

- [AutoGPT](https://Significant-Gravitas/AutoGPT/blob/master/docs/content/platform/ollama.md) - Autonomous AI agent platform
- [crewAI](https://crewAIInc/crewAI) - Multi-agent orchestration framework
- [Strands Agents](https://strands-agents/sdk-python) - Model-driven agent building by AWS
- [Cheshire Cat](https://cheshire-cat-ai/core) - AI assistant framework
- [any-agent](https://mozilla-ai/any-agent) - Unified agent framework interface by Mozilla
- [Stakpak](https://stakpak/agent) - Open source DevOps agent
- [Hexabot](https://hexastack/hexabot) - Conversational AI builder
- [Neuro SAN](https://cognizant-ai-lab/neuro-san-studio) - Multi-agent orchestration ([docs](https://cognizant-ai-lab/neuro-san-studio/blob/main/docs/user_guide.md#ollama))

### RAG & Knowledge Bases

- [RAGFlow](https://infiniflow/ragflow) - RAG engine based on deep document understanding
- [R2R](https://SciPhi-AI/R2R) - Open-source RAG engine
- [MaxKB](https://1Panel-dev/MaxKB/) - Ready-to-use RAG chatbot
- [Minima](https://dmayboroda/minima) - On-premises or fully local RAG
- [Chipper](https://TilmanGriesel/chipper) - AI interface with Haystack RAG
- [ARGO](https://xark-argo/argo) - RAG and deep research on Mac/Windows/Linux
- [Archyve](https://nickthecook/archyve) - RAG-enabling document library
- [Casibase](https://casibase.org) - AI knowledge base with RAG and SSO
- [BrainSoup](https://www.nurgo-software.com/products/brainsoup) - Native client with RAG and multi-agent automation

### Bots & Messaging

- [LangBot](https://RockChinQ/LangBot) - Multi-platform messaging bots with agents and RAG
- [AstrBot](https://Soulter/AstrBot/) - Multi-platform chatbot with RAG and plugins
- [Discord-Ollama Chat Bot](https://kevinthedang/discord-ollama) - TypeScript Discord bot
- [Ollama Telegram Bot](https://ruecat/ollama-telegram) - Telegram bot
- [LLM Telegram Bot](https://innightwolfsleep/llm_telegram_bot) - Telegram bot for roleplay

### Terminal & CLI

- [aichat](https://sigoden/aichat) - All-in-one LLM CLI with Shell Assistant, RAG, and AI tools
- [oterm](https://ggozad/oterm) - Terminal client for Ollama
- [gollama](https://sammcj/gollama) - Go-based model manager for Ollama
- [tlm](https://yusufcanb/tlm) - Local shell copilot
- [tenere](https://pythops/tenere) - TUI for LLMs
- [ParLlama](https://paulrobello/parllama) - TUI for Ollama
- [llm-ollama](https://taketwo/llm-ollama) - Plugin for [Datasette's LLM CLI](https://llm.datasette.io/en/stable/)
- [ShellOracle](https://djcopley/ShellOracle) - Shell command suggestions
- [LLM-X](https://mrdjohnson/llm-x) - Progressive web app for LLMs
- [cmdh](https://pgibler/cmdh) - Natural language to shell commands
- [VT](https://vinhnx/vt.ai) - Minimal multimodal AI chat app

### Productivity & Apps

- [AppFlowy](https://AppFlowy-IO/AppFlowy) - AI collaborative workspace, self-hostable Notion alternative
- [Screenpipe](https://mediar-ai/screenpipe) - 24/7 screen and mic recording with AI-powered search
- [Vibe](https://thewh1teagle/vibe) - Transcribe and analyze meetings
- [Page Assist](https://n4ze3m/page-assist) - Chrome extension for AI-powered browsing
- [NativeMind](https://NativeMindBrowser/NativeMindExtension) - Private, on-device browser AI assistant
- [Ollama Fortress](https://ParisNeo/ollama_proxy_server) - Security proxy for Ollama
- [1Panel](https://1Panel-dev/1Panel/) - Web-based Linux server management
- [Writeopia](https://Writeopia/Writeopia) - Text editor with Ollama integration
- [QA-Pilot](https://reid41/QA-Pilot) - GitHub code repository understanding
- [Raycast extension](https://MassimilianoPasquini97/raycast_ollama) - Ollama in Raycast
- [Painting Droid](https://mateuszmigas/painting-droid) - Painting app with AI integrations
- [Serene Pub](https://doolijb/serene-pub) - AI roleplaying app
- [Mayan EDMS](https://gitlab.com/mayan-edms/mayan-edms) - Document management with Ollama workflows
- [TagSpaces](https://www.tagspaces.org) - File management with [AI tagging](https://docs.tagspaces.org/ai/)

### Observability & Monitoring

- [Opik](https://www.comet.com/docs/opik/cookbook/ollama) - Debug, evaluate, and monitor LLM applications
- [OpenLIT](https://openlit/openlit) - OpenTelemetry-native monitoring for Ollama and GPUs
- [Lunary](https://lunary.ai/docs/integrations/ollama) - LLM observability with analytics and PII masking
- [Langfuse](https://langfuse.com/docs/integrations/ollama) - Open source LLM observability
- [HoneyHive](https://docs.honeyhive.ai/integrations/ollama) - AI observability and evaluation for agents
- [MLflow Tracing](https://mlflow.org/docs/latest/llms/tracing/index.html#automatic-tracing) - Open source LLM observability

### Database & Embeddings

- [pgai](https://timescale/pgai) - PostgreSQL as a vector database ([guide](https://timescale/pgai/blob/main/docs/vectorizer-quick-start.md))
- [MindsDB](https://mindsdb/mindsdb/blob/staging/mindsdb/integrations/handlers/ollama_handler/README.md) - Connect Ollama with 200+ data platforms
- [chromem-go](https://philippgille/chromem-go/blob/v0.5.0/embed_ollama.go) - Embeddable vector database for Go ([example](https://philippgille/chromem-go/tree/v0.5.0/examples/rag-wikipedia-ollama))
- [Kangaroo](https://dbkangaroo/kangaroo) - AI-powered SQL client

### Infrastructure & Deployment

#### Cloud

- [Google Cloud](https://cloud.google.com/run/docs/tutorials/gpu-gemma2-with-ollama)
- [Fly.io](https://fly.io/docs/python/do-more/add-ollama/)
- [Koyeb](https://www.koyeb.com/deploy/ollama)
- [Harbor](https://av/harbor) - Containerized LLM toolkit with Ollama as default backend

#### Package Managers

- [Pacman](https://archlinux.org/packages/extra/x86_64/ollama/)
- [Homebrew](https://formulae.brew.sh/formula/ollama)
- [Nix package](https://search.nixos.org/packages?show=ollama&from=0&size=50&sort=relevance&type=packages&query=ollama)
- [Helm Chart](https://artifacthub.io/packages/helm/ollama-helm/ollama)
- [Gentoo](https://gentoo/guru/tree/master/app-misc/ollama)
- [Flox](https://flox.dev/blog/ollama-part-one)
- [Guix channel](https://codeberg.org/tusharhero/ollama-guix)
