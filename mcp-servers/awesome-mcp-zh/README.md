# Awesome-MCP-ZH

![](https://files.mdnice.com/user/43439/48b72eef-4bca-4d2b-86e3-0055a1036ea7.jpg)

欢迎来到 `Awesome-MCP-ZH`，一个专为中文用户打造的 MCP（模型上下文协议）资源合集！
这里有 MCP 的基础介绍、玩法、客户端、服务器和社区资源，帮你快速上手这个 AI 界的“万能插头”。

[![简体中文](https://img.shields.io/badge/中文文档-点击查看-orange)](README.md) 


- 作者：云中江树 （微信公众号：云中江树，微信：1796060717）

- 如果国内的朋友想免费快速的体验MCP能力，推荐 Cherry Studio（客户端） + 阿里 Qwen (大模型）的组合，优势是免费、操作简单、LLM无需魔法、无需充值。

- LLM 选型我的使用体感是： Claude4.5 > GPT-5 > Gemini-2.5 > Qwen3-Max > DeepSeek

分析文章：
- [ 10分钟搞定高德地图MCP！我用AI解决了约会地点选择难题 ](https://mp.weixin.qq.com/s/SUifLfJIBX_JNIZesTm8CA)
- [ 因为Manus爆火的 Claude MCP，90%人的认知可能都是错的](https://mp.weixin.qq.com/s/mT43PSiyO9ZsXKCbiVsWzQ)
- [ 刚官宣支持MCP，就发布自家Agent协议（A2A），扒一扒Google暗藏的小心思](https://mp.weixin.qq.com/s/Zoq2bgPfJIERAzPiN1l0QA)
- [阿里云拥抱 MCP 这步棋，太多人都没有真正看懂](https://mp.weixin.qq.com/s/GrEWFqpmvp1LfURAT1XzZw)
- [ 详解 MCP 传输机制 ](https://mp.weixin.qq.com/s/gmgo_glOzbvdFwePP1yQ9g)
---

## 目录

- [MCP 是什么？](#mcp-是什么)
- [MCP 能干什么？](#mcp-能干什么)
- [MCP 客户端](#mcp-客户端)
- [MCP 服务器精选列表](#mcp-服务器精选列表)
  - [🌐 浏览器自动化与网页交互](#浏览器自动化与网页交互)
  - [💻 开发与代码执行](#开发与代码执行)
  - [🖥️ 命令行与 Shell 交互](#命令行与-shell-交互)
  - [🔄 版本控制 (Git / GitHub / GitLab)](#版本控制-git--github--gitlab)
  - [🗄️ 数据库交互](#数据库交互)
  - [☁️ 云平台与服务集成 (AWS, Cloudflare, Azure, K8s, etc.)](#云平台与服务集成-aws-cloudflare-azure-k8s-etc)
  - [🔍 搜索](#搜索)
  - [💬 通讯与协作 (Slack, Email, Calendar, Social, etc.)](#通讯与协作-slack-email-calendar-social-etc)
  - [💰 金融与加密货币](#金融与加密货币)
  - [📁 文件系统与存储](#文件系统与存储)
  - [📊 数据分析、处理与可视化](#数据分析处理与可视化)
  - [🛠️ 效率工具与集成 (Office, Project Management, Notes, etc.)](#效率工具与集成-office-project-management-notes-etc)
  - [multimedia 多媒体与内容创作](#multimedia-多媒体与内容创作)
  - [📕 社交媒体与内容创作 (小红书/RedNote)](#社交媒体与内容创作-小红书rednote)
  - [🛒 电商商家经营 (E-Commerce)](#电商商家经营-e-commerce)
  - [🧠 知识、记忆与 RAG](#知识记忆与-rag)
  - [🔒 安全与分析](#安全与分析)
  - [🌍 地理位置与出行](#地理位置与出行)
  - [🏃 体育与游戏](#体育与游戏)
  - [🏛️ 艺术与文化](#艺术与文化)
  - [🛠️ 其他实用工具与集成](#其他实用工具与集成)
  - [更多 MCP Server 资源](#更多-mcp-server-资源)
- [MCP 更多玩法](#mcp-更多玩法)
- [MCP 资源](#mcp-资源)
- [MCP Server 开发](#mcp-server-开发)
- [Star History](#star-history)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

---

## MCP 是什么？

MCP 全称 **模型上下文协议（Model Context Protocol）**，由 Anthropic 在 2024 年 11 月推出，是个开源通信标准。简单说，它给 AI 装了个“超级网线”，让 AI 能跟外部工具、数据、系统无缝对接。

- **比喻**：AI 是个聪明但宅家的书呆子，MCP 就是它的“外卖员”，能帮它拿数据、干活儿。
- **目标**：让 AI 不只聊天，还能真动手，比如查数据库、发邮件、写代码。

![MCP 架构图](https://files.mdnice.com/user/43439/e43d85e3-53c4-440d-ad88-bd5218028b20.png)

想深入了解？看 [官方介绍](https://www.anthropic.com/news/model-context-protocol)。

微软出的面向初学者的 Model Context Protocol (MCP) 课程也不错，推荐一下：
- [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)

---

## MCP 能干什么？

MCP 能让 AI 从“嘴炮王”变成“实干家”，以下是几个例子：

1. **连工具**：用 Slack 发消息、用 GitHub 管代码、用 Blender 建 3D 模型。
2. **查数据**：直接看你电脑文件、数据库记录，甚至网上实时信息。
3. **干复杂活儿**：写网页时，AI 能查代码、生成图片、调试页面，一条龙搞定。
4. **人机协作**：AI 干一半问你意见，你点头它再继续。

**例子**：在 Cursor 里装个 Slack MCP 服务器，AI 能一边写代码一边发消息通知团队，超省事！

---

## MCP 客户端

MCP 客户端是 AI 的“操作台”，以下是几个热门选择：

- **Claude Desktop**  
  - **简介**：Claude 桌面版，普通人也能用。  
  - **功能**：官方客户端，连接各种MCP服务器，例如连 Blender MCP，用自然语言建 3D 模型。  
  - **链接**：[Anthropic 官网](https://docs.anthropic.com)  
  - **截图**：
    ![Claude Desktop](https://files.mdnice.com/user/43439/8e500f0e-e4c3-453e-9439-ddc6735a6cbc.png)
  - **Tips**：不写代码也能玩，新手友好。

- **Cherry Studio**  
  - **简介**：新兴客户端，支持可视化配置。  
  - **功能**：点选即可配置MCP服务器，简单上手。  
  - **链接**：[Cherry Studio](https://github.com/CherryHQ/cherry-studio)  
  - **截图**：  
    ![Cherry Studio 配置 MCP](https://files.mdnice.com/user/43439/d3a71dcd-5ac6-4548-8200-30a793d46255.png)  
  - **Tips**：开发中，关注社区动态。

- **5ire**  
  - **简介**：一款现代化的 AI 助手和 MCP 客户端，支持多种主流服务提供商。  
  - **功能**：通过 MCP 协议连接工具与数据源，提供文件系统访问、数据库交互、远程数据获取等功能；支持本地知识库、使用分析、提示库、书签、快速搜索等特性。  
  - **链接**：[5ire 官网](https://5ire.app/) | [GitHub 仓库](https://github.com/nanbingxyz/5ire)  
  - **截图**：  
    ![5ire](https://files.mdnice.com/user/43439/0c1c47ad-689d-4302-824e-9dd5e2706e2c.png)
  - **Tips**：适合开发者与非开发者使用，支持多平台（Windows、macOS、Linux）。

- **Cursor**  
  - **简介**：代码编辑器，装上 MCP 变“全能选手”。  
  - **功能**：写代码、发 Slack、生成图片。  
  - **链接**：[官网](https://cursor.sh/)  
  - **截图**：
    ![Cursor](https://files.mdnice.com/user/43439/3971db3e-2a0d-4128-b6e5-bcc487034d47.png)
  - **Tips**：程序员必备，试试连 GitHub MCP。

- **Claude Code**  
  - **简介**：Anthropic 官方命令行 AI 编程工具，原生支持 MCP 协议。  
  - **功能**：在终端中读写代码、运行命令、调用 MCP 服务器扩展工具与数据源，可配置本地或远程 MCP Server。  
  - **链接**：[GitHub 仓库](https://github.com/anthropics/claude-code)  
  - **Tips**：适合在终端工作流中深度集成 MCP 的开发者。

- **DeepChat**  
  - **简介**：连接强大 AI 与个人世界的智能助手。  
  - **功能**：支持多模型云服务（如 DeepSeek、OpenAI 等）和本地模型部署（如 Ollama），具备多通道聊天并发支持、完整的 Markdown 渲染、本地文件处理、MCP 支持等特性。  
  - **链接**：[DeepChat 官网](https://deepchat.thinkinai.xyz/) | [GitHub 仓库](https://github.com/ThinkInAIXYZ/deepchat)  
  - **截图**：  
    ![DeepChat](https://files.mdnice.com/user/43439/802fc73d-6fd6-46ca-9e7c-9aff38715a88.png)
  - **Tips**：适合开发者与非开发者使用，支持多种平台（Windows、macOS、Linux），可通过 MCP 快速集成到现有工作流中。  

- **ChatWise**  
  - **简介**：功能强大且注重隐私保护。  
  - **功能**：支持任意 LLM 模型（如 GPT-4、Claude、Gemini 等），具备多模态聊天（音频、PDF、图片、文本等）、网页搜索（Tavily API 或本地浏览器）、MCP 工具集成（如 Notion、Google Sheets 等）以及实时渲染 HTML/React/图表等功能。  
  - **链接**：[ChatWise 官网](https://chatwise.app/) | [文档](https://docs.chatwise.app/)  
  - **截图**：  
    ![ChatWise](https://files.mdnice.com/user/43439/306e535a-7b7b-43c5-b6ba-02c83d167485.jpg)
  - **Tips**：数据完全本地存储，适合需要高效工具的用户；通过 MCP 扩展其功能！

- **eechat**  
  - **简介**：简单易用的本地部署 LLM 工具，注重隐私、安全和性能。  
  - **功能**：一键集成、管理、运行多种 MCP 工具，可视化配置 + 自动读取 Readme MCP 配置信息，内置 Node, Python 运行环境，兼容 Claude, Cursor 配置，同时支持本地化部署模型。
  - **链接**：[eechat 官网](https://ee.chat/) | [GitHub 仓库](https://github.com/Lucassssss/eechat)  
  - **截图**：  
    ![eechat](https://www.ee.chat/img/mcp_chat.png)
  - **Tips**：低门槛适合小白。

- **MCP Dock**  
  - **简介**：桌面端 MCP 配置管理工具，支持 14 个 AI 客户端的 MCP Server 统一管理。  
  - **功能**：9200+ MCP Server 商店、3100+ AI Skills 商店、一键安装到多客户端、内置 MCP Inspector 调试、配置历史记录与回滚。  
  - **链接**：[官网](https://mcp.folay.top) | [GitHub 仓库](https://github.com/OldJii/mcp-dock)  
  - **Tips**：本地优先，不需要账号；支持 Cursor、Claude Code、VS Code、Gemini CLI 等 14 个客户端。

- **Cline**
  - **简介**：VS Code 中的自主编程 Agent，也提供 SDK/CLI 形态。
  - **功能**：原生 MCP 客户端，可读写文件、运行命令，并可安装 MCP 服务器扩展能力。
  - **链接**：[GitHub 仓库](https://github.com/cline/cline)
  - **Tips**：VS Code 用户的 MCP 首选之一。

- **Continue**
  - **简介**：开源编程 Agent，支持 VS Code 与 JetBrains。
  - **功能**：可配置本地/远程 MCP 服务器，接入自定义模型与工具。
  - **链接**：[GitHub 仓库](https://github.com/continuedev/continue)

- **Goose**
  - **简介**：Block 开源的可扩展本地 AI Agent。
  - **功能**：原生 MCP 宿主，可安装/执行/编辑/测试代码，支持任意 LLM，提供桌面版 + CLI 双形态。
  - **链接**：[GitHub 仓库](https://github.com/block/goose)
  - **Tips**：MCP 生态最活跃的开源 Agent 之一。

- **AnythingLLM**
  - **简介**：本地优先的全栈 AI 应用，一体化文档/知识库/Agent。
  - **功能**：内置 MCP 兼容，接入工具与数据源，支持桌面与自托管。
  - **链接**：[GitHub 仓库](https://github.com/Mintplex-Labs/anything-llm)

- **LibreChat**
  - **简介**：增强版开源多模型聊天平台，支持自托管多用户。
  - **功能**：内置 MCP、Agents、Code Interpreter，可切换 Claude/GPT/Gemini 等模型。
  - **链接**：[GitHub 仓库](https://github.com/danny-avila/LibreChat)

- **Dive**
  - **简介**：开源 MCP Host 桌面应用。
  - **功能**：对接任意支持 function calling 的 LLM，可视化管理 MCP 服务器。
  - **链接**：[GitHub 仓库](https://github.com/OpenAgentPlatform/Dive)

- **其他MCP客户端资源**  
  - [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)

---
## MCP 服务器精选列表

模型上下文协议 (MCP) 服务器是赋予 AI 模型与外部工具、数据和系统交互能力的“工具箱”。以下是按不同应用场景精选的 MCP 服务器列表，按场景和质量（官方/参考 > 常用/成熟 > 社区/特定）排序，方便中文用户查找和使用。

**说明:**

*   **名称:** 点击可跳转到对应的 GitHub 仓库。
*   **中文介绍:** 简述该服务器的主要功能和用途。
*   **备注:** 包含开发者信息（如官方、社区）、主要技术、适用平台或关键特性。

---


### 🌐 浏览器自动化与网页交互

*(让 AI 能够像人一样浏览网页、提取信息、填写表单等)*

| 名称                                                                 | 中文介绍                                                                          | 备注                                                                               |
| :------------------------------------------------------------------- | :-------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 微软官方出品，使用 Playwright 让 AI 精确控制网页，自动化抓取数据。                   | 官方实现，浏览器自动化强推，适合需要精细网页交互的场景。                               |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 谷歌 Chrome 官方出品，让 AI 编程代理直接驱动 Chrome DevTools：导航页面、检查 DOM、抓取网络请求、跑性能与 Lighthouse 审计、执行脚本。 | 官方实现 (Google Chrome) 🎖️, TypeScript 开发 📇, 本地运行 🏠, 浏览器调试与自动化, 42K+ Stars。 |
| [webclaw](https://github.com/0xMassi/webclaw) | 快速本地优先的网页内容提取工具，专为 LLM 设计。支持将网页转换为 Markdown/JSON/纯文本，内置 TLS 指纹伪装绕过反爬，无需浏览器。提供 MCP 服务器（10 个工具）和 CLI。 | 社区实现, Rust 开发 🦀, 本地运行 🏠, MIT 开源, 高性能网页提取。 |
| [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | 云端浏览器自动化服务，能导航网页、提取数据、填表单等，无需本地安装。                  | 官方实现 (Browserbase) 🎖️, TypeScript 开发 📇, 云端浏览器操作。                      |
| [modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer) | 官方参考实现，使用 Puppeteer 进行浏览器自动化和网页抓取。                           | 官方参考, TypeScript 开发 📇, 本地运行 🏠, 网页抓取和交互基础工具。                 |
| [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) | 集成 Apify 平台 3000+ 云工具，用于网站、电商、社交媒体等数据提取。                  | 官方实现 (Apify), TypeScript 开发 📇, 云端数据抓取工具库 ☁️。                      |
| [AgentQL](https://github.com/tinyfish-io/agentql-mcp)                | 让 AI 代理从非结构化网页中获取结构化数据。                                         | 官方实现 (TinyFish IO) 🎖️, TypeScript 开发 📇, 网页数据结构化提取 ☁️。           |
| [Firecrawl](https://github.com/mendableai/firecrawl-mcp-server)      | 使用 Firecrawl 提取网页数据，支持 JavaScript 渲染。                              | 官方实现 (Mendable AI), TypeScript 开发, 高级网页抓取。                           |
| [crw](https://github.com/us/crw)                                    | 开源网页抓取工具，专为 AI 代理设计。单一 Rust 二进制文件，内置 MCP 服务器，兼容 Firecrawl API。 | 社区实现, Rust 开发 🦀, 本地运行 🏠, 高性能网页抓取。                             |
| [Free Web Search Ultimate](https://github.com/wd041216-bit/free-web-search-ultimate) | Zero-cost, privacy-first universal web search MCP server. Enforces a Search-First paradigm — instructs LLMs to retrieve real-time web information before answering factual questions, eliminating hallucinations. Supports text, news, images, books, and videos via DuckDuckGo. No API key required. Install: `pip install free-web-search-ultimate` | 社区实现, Python 开发 🐍, 本地运行 🏠, 零成本通用网页搜索。                      |
| [Oxylabs](https://github.com/oxylabs/oxylabs-mcp)                    | 使用 Oxylabs Web API 抓取网站，支持动态渲染和结构化数据提取。                       | 官方实现 (Oxylabs), Python 开发, 专业级网页抓取。                                |
| [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | Bright Data 官方出品，为 AI 代理提供一体化公网访问能力：实时网页搜索、抓取、绕过反爬与地理限制，获取干净结构化的网页数据。 | 官方实现 (Bright Data) 🎖️, JavaScript 开发 📇, 云服务 ☁️, 公网数据访问与抓取, 2.4K+ Stars。 |
| [IPLoop/ProxyClaw](https://github.com/Iploop/proxyclaw)              | 通过 2M+ 真实住宅 IP (195+ 国家) 访问网页，内置反检测 (TLS/JA3 指纹 + Chrome 头)。66 个站点预设。Python SDK: `pip install iploop-sdk`                    | 社区实现, Python/Node.js 开发, 住宅代理 🌐。                                      |
| [Hyperbrowser](https://github.com/hyperbrowserai/mcp)                | 新一代 AI 代理浏览器自动化平台，支持大规模、无缝操作。                              | 官方实现 (Hyperbrowser AI), TypeScript 开发, 大规模浏览器自动化。                  |
| [ScreenshotOne](https://github.com/screenshotone/mcp/)               | 使用 ScreenshotOne 服务渲染网站截图。                                            | 官方实现 (ScreenshotOne), TypeScript 开发, 网页截图工具。                          |
| [modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | 官方参考实现，灵活获取网页内容（HTML/JSON/MD），并为 AI 处理优化。                | 官方参考, Python 开发 🐍, 本地/云端 🏠☁️, 基础网页内容获取。                         |
| [automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) | 使用 Playwright 进行浏览器自动化的 MCP 服务器。                              | 社区实现, Python 开发 🐍.                                                          |
| [blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) | 使用 Playwright 的 Python MCP 服务器，更适合 LLM。                         | 社区实现, Python 开发 🐍.                                                          |
| [browsermcp/mcp](https://github.com/browsermcp/mcp)                  | 自动化本地 Chrome 浏览器。                                                 | 社区实现, TypeScript 开发 📇, 本地运行 🏠.                                        |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | Chrome 浏览器扩展形式的 MCP 服务器，复用用户现有浏览器（含登录态与配置），让 AI 接管真实 Chrome 进行网页自动化、内容分析与语义检索。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 基于 Chrome 扩展, 11K+ Stars。 |
| [co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) | 将 browser-use 打包为带 SSE 传输的 MCP 服务器，含 Dockerfile。           | 社区实现, Python 开发 🐍.                                                          |
| [executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) | 使用 Playwright 进行浏览器自动化和网页抓取的 MCP 服务器。                    | 社区实现, TypeScript 开发 📇.                                                     |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | 面向移动端自动化与抓取的 MCP 服务器，统一驱动 iOS、Android、模拟器与真机，让 AI 代理通过无障碍树或坐标操作 App、抓取屏幕内容并执行 E2E 测试。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 移动端 (iOS/Android) 自动化与抓取, 5.3K+ Stars。 |
| [flutter-skill](https://github.com/ai-dashboad/flutter-skill) | AI驱动的E2E测试MCP服务器，支持Flutter、iOS、Android、Web、Electron、Tauri、KMP、React Native、.NET MAUI等8个平台。 | 社区实现, Dart 开发, E2E跨平台测试。                                                |
| [eyalzh/browser-control-mcp](https://github.com/eyalzh/browser-control-mcp) | 与浏览器扩展配对，使 LLM 客户端能控制用户的 Firefox 浏览器。              | 社区实现, TypeScript 开发 📇, 本地运行 🏠.                                        |
| [getrupt/ashra-mcp](https://github.com/getrupt/ashra-mcp)            | 从任何网站提取结构化数据，只需提示即可获得 JSON。                             | 社区实现, Python 开发 🐍, 本地运行 🏠.                                             |
| [kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) | 使用 Azure OpenAI 和 Playwright 的最小化 MCP 服务器/客户端实现。           | 社区实现, Python 开发 🐍, 本地运行 🏠.                                             |
| [ndthanhdev/mcp-browser-kit](https://github.com/ndthanhdev/mcp-browser-kit) | 用于与 manifest v2 兼容浏览器交互的 MCP 服务器。                         | 社区实现, TypeScript 开发 📇, 本地运行 🏠.                                        |
| [RAG Web Browser](https://github.com/apify/mcp-server-rag-web-browser) | Apify 开源工具，执行网页搜索、抓取 URL 并以 Markdown 格式返回内容。                | 社区实现 (Apify), TypeScript 开发 📇, 结合 RAG 的网页浏览 ☁️。                    |
| [scrapling-fetch](https://github.com/cyberchitta/scrapling-fetch-mcp) | 从有反爬虫措施的网站获取文本内容。                                                | 社区实现, Python 开发, 突破反爬。                                               |
| [jae-jae/fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)        | 使用 Playwright 无头浏览器获取网页内容，支持 JS 渲染和智能提取 (Markdown/HTML)。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, Playwright 网页内容提取。              |
| [ryoppippi/sitemcp](https://github.com/ryoppippi/sitemcp)           | 抓取整个网站并将其作为 MCP 服务器使用。                                          | 支持 TypeScript，提供工具命名策略、页面匹配、内容选择器等功能。可通过 NPM、Bun 等安装和运行。 |
| [34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) | 支持搜索 Bilibili 内容的 MCP 服务器。                                      | 社区实现, TypeScript 开发 📇, 本地运行 🏠.                                        |
| [OpenTabs](https://github.com/opentabs-dev/opentabs) | 基于插件的 MCP 服务器，通过用户已认证的浏览器会话让 AI 代理访问 Web 应用。Chrome 扩展 + 100 多个插件，支持 Slack、Discord、GitHub、Reddit 等。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 插件化浏览器集成。 |
| [Zlatanwic/wechat-article-read-mcp](https://github.com/Zlatanwic/Wechat-Read-MCP-in-Rust) |支持微信公众号内容提取，绕过微信反爬机制|  社区实现，rust开发 🦀，本地运行 🏠，高性能，易分发|
| [achiya-automation/safari-mcp](https://github.com/achiya-automation/safari-mcp) | 原生 Safari 浏览器自动化，专为 macOS 设计。通过 AppleScript + JavaScript 提供 80 个工具，零 Chrome 开销，保留登录状态，后台静默运行。 | 社区实现, JavaScript 开发 📇, 本地运行 🏠, macOS 原生 🍎 |
| [vostride/agent-qa](https://github.com/vostride/agent-qa) | 自我改进的 Agentic QA 测试工具，通过自然语言编写 Web 和移动端测试，并用执行记忆和自修复动作排查回归。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, E2E 测试与浏览器自动化。 |
| [Unagi-cq/cdp-bridge-mcp](https://github.com/Unagi-cq/cdp-bridge-mcp) | 通过 Chrome DevTools Protocol (CDP) 与配套浏览器扩展，将 MCP 客户端桥接到用户的真实浏览器，复用已有会话与登录态进行网页操作。 | 社区实现, Python 开发 🐍, 本地运行 🏠, CDP + 扩展桥接真实浏览器。 |
| [AI-XiaoDao/ai-browser-mcp](https://github.com/AI-XiaoDao/ai-browser-mcp) | Windows 本地浏览器自动化 MCP，基于 FBrowser CEF 内核暴露 200+ `browser_*` 工具：导航、原生 DOM、填表 RPA、CDP 断点、POST 抓包、JS 逆向与爬虫。原生 API 优先，支持 stdio / HTTP / WebSocket 接入 Cursor、Claude、Cline。 | 社区实现, C++ 开发, 本地运行 🏠, Windows 🪟, 浏览器自动化 + JS 逆向, MIT。 |
---

### 💻 开发与代码执行

*(让 AI 能够运行代码、分析代码库、与开发工具集成等)*

| 名称                                                                 | 中文介绍                                                                              | 备注                                                                                 |
| :------------------------------------------------------------------- | :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------- |
| [Muvon/octocode](https://github.com/Muvon/octocode) | Rust 编写的语义代码索引器，构建代码库 GraphRAG 知识图谱并通过 MCP 暴露给 AI 代理。支持 13+ 语言，提供 tree-sitter 解析、ast-grep 结构化搜索和代码签名视图。 | 社区实现, Rust 开发 🦀, 本地运行 🏠, 跨平台 🍎🪟🐧, 语义搜索 + GraphRAG 知识图谱, Apache 2.0。 |
| [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) | 多智能体编排器，协调 37 个 CLI 编码代理（Claude Code、Codex、Gemini CLI、Cursor、Aider 等）在并行 Git worktree 中运行。内置 MCP 服务器模式（stdio + HTTP/SSE）。 | 社区实现, Python 开发 🐍, 本地/云端 🏠☁️, Apache 2.0, 确定性调度器, 多代理编排。 |
| [aresyn/codex-control-plane-mcp](https://github.com/aresyn/codex-control-plane-mcp) | 面向 Codex Desktop 长任务的持久化 MCP 控制平面，统一调度、跟踪与恢复长时运行的智能体任务，让 AI 可靠地驱动长周期编码工作流。 | 社区实现, Python 开发 🐍, 本地运行 🏠, 长任务编排与持久化控制平面, Apache 2.0。 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 高性能代码智能 MCP 服务器，将整个代码库索引为持久化知识图谱，为 AI 代理提供调用关系、依赖与代码结构记忆，按需精准检索相关上下文。 | 社区实现, 本地运行 🏠, 代码智能 + 持久化知识图谱, 17K+ Stars。 |
| [win4r/codebase-memory-mcp-pro](https://github.com/win4r/codebase-memory-mcp-pro) | 纯 C 实现的代码知识图谱 MCP 服务器，构建并增量重索引代码库的调用关系图，为 AI 提供代码结构记忆。整合 9 个上游 PR，修复增量重索引的 CALLS 边。 | 社区实现, C 开发, 本地运行 🏠, 代码知识图谱 + 增量重索引, MIT。 |
| [iohub/codexray](https://github.com/iohub/codexray) | 仓库感知的本地 MCP，用混合语义 + 全文检索引擎实时理解代码库，按需为 AI 提供相关代码上下文。兼容 Claude Code 与 Codex。 | 社区实现, Rust 开发 🦀, 本地运行 🏠, 混合语义 + 全文代码检索, MIT。 |
| [21st.dev Magic](https://github.com/21st-dev/magic-mcp)             | 21st.dev 官方集成，创建受顶级设计工程师启发的精美 UI 组件。                          | 官方实现 (21st.dev) 🎖️, UI 组件创建。                                               |
| [upstash/context7](https://github.com/upstash/context7) | Upstash 出品，为 LLM 和 AI 编辑器实时注入最新的库文档与代码示例，消除模型对过时 API 的幻觉。Cursor / Claude 等一键接入。 | 官方实现 (Upstash) 🎖️, TypeScript 开发 📇, 云服务 ☁️, 实时文档检索, 56K+ Stars。 |
| [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) | Sentry 官方集成，让 AI 通过自然语言查询错误、性能问题与发布信息，快速定位线上故障根因。 | 官方实现 (Sentry) 🎖️, TypeScript 开发 📇, 云服务 ☁️, 错误监控与可观测性。 |
| [getsentry/XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP) | 面向 iOS/macOS 开发的 MCP 服务器与 CLI，为 AI 代理提供 Xcode 项目构建、运行、模拟器管理与日志捕获等工具，打通 Apple 平台开发工作流。 | 官方实现 (Sentry) 🎖️, TypeScript 开发 📇, 本地运行 🏠, macOS 🍎, Xcode 构建工具, 5.9K+ Stars。 |
| [pydantic/mcp-run-python](https://github.com/pydantic/mcp-run-python) | Pydantic 出品，在安全的沙盒环境中运行 Python 代码，适合开发编程代理。                   | 官方实现 (Pydantic) 🎖️, Python 开发 🐍, 本地运行 🏠, 安全代码执行。                   |
| [E2B](https://github.com/e2b-dev/mcp-server)                         | 在 E2B 提供的安全云沙盒中运行代码。                                                 | 官方实现 (E2B), TypeScript 开发, 云端安全代码沙盒。                                  |
| [JetBrains IDE Proxy](https://github.com/JetBrains/mcpProxy)           | JetBrains 官方代理，连接到 JetBrains IDE。                                       | 官方实现 (JetBrains) 🎖️, TypeScript 开发 📇, 本地运行 🏠, IDE 连接。             |
| [JetBrains](https://github.com/JetBrains/mcp-jetbrains)              | JetBrains 官方集成，让 AI 在 JetBrains IDE 中处理代码。                               | 官方实现 (JetBrains), Kotlin 开发, IDE 代码操作。                                  |
| [yepcode/mcp-server-js](https://github.com/yepcode/mcp-server-js)    | 在安全可扩展的沙盒环境中执行 LLM 生成的代码，并用 JS/Python 创建自定义 MCP 工具。 | 官方实现 (YepCode) 🎖️, TypeScript 开发 📇, 云服务 ☁️, 安全代码执行，自定义工具。       |
| [yzfly/mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter) | 安全、标准化的 Python 环境，支持代码执行、环境和包管理。                              | 社区标杆, 轻量级 Python 执行环境, 适合开发和数据分析。                                |
| [admica/FileScopeMCP](https://github.com/admica/FileScopeMCP)        | 分析代码库依赖关系，生成图表，帮助 AI 理解项目结构。                                  | 社区实现, 多语言 (Py 🐍/TS 📇/Rust 🦀), 代码结构分析。                               |
| [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp)                | 管理代码偏好和模式，支持语义搜索，方便在 IDE 中存取技术文档。 (Mem0 官方)             | 官方实现 (Mem0 AI) 🎖️, Python 开发 🐍, 本地运行 🏠, 程序员的记忆助手和偏好管理。       |
| [code-executor](https://github.com/bazinga012/mcp_code_executor)     | 允许 AI 在指定的 Conda 环境中执行 Python 代码。                                      | 社区实现, Python 开发, Conda 环境代码执行。                                         |
| [code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp) | 创建安全的 Docker 容器环境来执行代码。                                              | 社区实现, Python 开发, Docker 沙盒代码执行。                                         |
| [knowlyr-sandbox](https://github.com/liuxiaotong/knowlyr-agent/tree/main/packages/sandbox) | Code Agent 执行沙箱 — Docker 隔离、文件捕获、超时控制，为 LLM 代码代理提供安全的运行环境。 | 社区实现, Python 开发 🐍, 本地运行 🏠, Docker 沙箱执行。 |
| [ForeverVM](https://github.com/jamsocket/forevervm/tree/main/javascript/mcp-server) | 在代码沙盒中运行 Python 代码。                                                     | 官方实现 (Jamsocket), JavaScript 开发, 代码沙盒。                                   |
| [Riza](https://github.com/riza-io/riza-mcp)                          | Riza 提供的任意代码执行和工具使用平台。                                              | 官方实现 (Riza), Go 开发, 通用代码执行平台。                                       |
| [Roundtable](https://github.com/askbudi/roundtable) | 统一AI编程助手的零配置MCP服务器，专为自主代理开发设计，简化多AI工具集成工作流程。 | 社区实现 🌟, Python 开发 🐍, 本地/云端部署 🏠☁️, pip install roundtable-ai |
| [Semgrep](https://github.com/semgrep/mcp)                            | 让 AI 代理使用 Semgrep 进行代码安全扫描。 (Semgrep 官方)                           | 官方实现 (Semgrep) 🎖️, TypeScript 开发 📇, 代码安全扫描 ☁️. |
| [ZenML](https://github.com/zenml-io/mcp-zenml)                       | 与 ZenML MLOps/LLMOps 平台交互，管理机器学习流程。 (ZenML 官方)                   | 官方实现 (ZenML) 🎖️, Python 开发 🐍, 本地/云端 🏠☁️, MLOps 流程管理。               |
| [vivekVells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)    | 使用 Pandoc 进行无缝文档格式转换（Markdown, HTML, PDF, DOCX, CSV 等）。            | 社区实现, Python 开发 🐍, 本地运行 🏠, 文档格式转换。                                |
| [oraios/serena](https://github.com/oraios/serena)                    | 功能齐全的编码代理，依赖于使用语言服务器的符号化代码操作。                        | 社区实现, Python 开发 🐍, 本地运行 🏠, 编码代理。                                    |
| [ezyang/codemcp](https://github.com/ezyang/codemcp)                  | 具有基本读、写和命令行工具的编码代理。                                         | 社区实现, Python 开发 🐍, 本地运行 🏠, 编码代理。                                    |
| [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | 增强的文件系统和搜索工具，以及特定于编码的命令和提示。(也含命令行功能)              | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 跨平台 🍎🪟🐧, 编码/文件/命令行工具。     |
| [maxim-saplin/mcp_safe_local_python_executor](https://github.com/maxim-saplin/mcp_safe_local_python_executor) | 基于 HF Smolagents `LocalPythonExecutor` 的安全 Python 解释器。            | 社区实现, Python 开发, 本地安全 Python 执行。                                        |
| [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor)      | 面向行的文本文件编辑器。针对 LLM 工具优化，通过高效的部分文件访问最小化 Token 使用。 | 社区实现, Python 开发 🐍, 本地运行 🏠, 文本编辑。                                     |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx)                | 面向 AI 编程代理的上下文运行时。通过会话缓存、AST 感知压缩和 90+ Shell 输出模式，将 LLM Token 成本降低 60-99%。单一 Rust 二进制文件，46 个 MCP 工具。Apache-2.0 开源。 | 社区实现, Rust 开发 🦀, 本地运行 🏠, [leanctx.com](https://leanctx.com), 900+ Stars, 32k+ 安装。 |
| [VSCode Devtools](https://github.com/biegehydra/BifrostMCP)            | 连接到 VSCode IDE 并使用语义工具，如 `find_usages`。                         | 社区实现, TypeScript 开发 📇, VSCode 集成。                                        |
| [xzq.xu/jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)      | 基于 JVM 的 MCP 服务器实现项目。                                            | 社区实现, TypeScript 开发 📇, 本地运行 🏠, JVM 集成。                              |
| [yWorks/mcp-typescribe](https://github.com/yWorks/mcp-typescribe)    | 高效地向代理提供 TypeScript API 信息，使其能够处理未经训练的 API。             | 官方实现 (yWorks), TypeScript 开发 📇, 本地运行 🏠, TypeScript API 信息。           |
| [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp)            | 灵活获取 JSON、文本和 HTML 数据的 MCP 服务器。                               | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 数据获取。                                 |
| [idosal/git-mcp](https://github.com/idosal/git-mcp)                  | 通用远程 MCP 服务器，用于连接任何 GitHub 仓库或项目以获取文档。                  | 社区实现, TypeScript 开发 📇, 云服务 ☁️, 远程 GitHub 文档访问 ([gitmcp.io](https://gitmcp.io/))。 |
| [tgeselle/bugsnag-mcp](https://github.com/tgeselle/bugsnag-mcp)        | 用于与 Bugsnag 交互的 MCP 服务器。                                         | 社区实现, TypeScript 开发 📇, 云服务 ☁️, Bugsnag 集成。                              |
| [jordandalton/restcsv-mcp-server](https://github.com/JordanDalton/RestCsvMcpServer) | 用于 CSV 文件的 MCP 服务器。                                               | 社区实现, TypeScript 开发 📇, 云服务 ☁️, CSV 处理。                                 |
| [jjsantos01/jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp) | 将 Jupyter Notebook 连接到 Claude AI，允许 Claude 直接交互和控制 Jupyter。 | 社区实现, Python 开发 🐍, 本地运行 🏠, Jupyter 集成。                               |
| [tersePrompts/jarp-mcp](https://github.com/tersePrompts/jarp-mcp) | Java Archive Reader Protocol - 为 AI 代理提供对 Maven 依赖中反编译 Java 代码的即时访问，如同为 AI 装上"X 光透视眼"。 | 社区实现 🌟, Node.js/Java 开发 ☕🟢, 本地运行 🏠, Java 类分析与反编译, CFR 内置, 智能缓存 |
| [tersePrompts/fastMCP4J](https://github.com/tersePrompts/fastMCP4J) | Java 语言构建 MCP 服务器的轻量级注解驱动框架，JSON Schema 2020-12 兼容，安全、快速、零配置。 | 社区实现 🌟, Java 开发 ☕, 本地运行 🏠, 注解驱动, 12 个依赖, 支持异步、内存、任务、文件操作 |
| [wopee-mcp](https://www.npmjs.com/package/wopee-mcp) | Web应用AI测试代理，支持调度测试运行、分析爬虫和AI代理测试，获取工件和项目状态。 | 社区实现, TypeScript 开发 📇, 云服务 ☁️, AI 测试代理。 |
| [memtrace](https://github.com/syncable-dev/memtrace-public) | 面向编码代理的结构化内存层，通过 AST 构建双时态知识图谱，为 Claude、Cursor 等 MCP 客户端提供低延迟代码理解与检索能力。 | 社区实现，Rust 核心 🦀，MCP 服务 ☁️，代码智能与代理记忆。 | 
| [ozgurcd/gograph](https://github.com/ozgurcd/gograph) | 纯本地的 Go 静态分析引擎，内置 MCP 服务器，为 AI 编程代理提供确定性的结构感知：调用图、影响分析、符号搜索等。 | 社区实现, Go 开发 🏎️, 本地运行 🏠, Go 调用图与影响分析。 |
| [lightbearco/tupper](https://github.com/lightbearco/tupper) | 面向 AI 代理的开源沙箱，在本机安全运行不受信任的 AI 生成代码、Shell 命令与文件读写。基于 Apple Containers，提供 E2B 风格的 TypeScript SDK，内置 MCP 服务器、CLI 与 HTTP API（macOS 用 Apple Containers，Linux/Windows 经 Firecracker/WSL）。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, macOS 🍎, 自托管代码执行沙箱, MIT。 |
| [mybolide/mcp-probe-kit](https://github.com/mybolide/mcp-probe-kit) | 规格驱动的通用开发工作流 MCP（30 工具）：`start_feature` / `start_bugfix` / `start_ui` 编排全流程，自动 Skill + AGENTS.md bootstrap，跨项目向量记忆（Qdrant），GitNexus 代码图谱，规格校验与质量闸门。任意 MCP 客户端可用。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 跨平台 🍎🪟🐧, 工作流编排 + 记忆, MIT, `npx -y mcp-probe-kit@latest`。 |
| [Necmttn/ax](https://github.com/Necmttn/ax) | 本地优先的 AI 编程代理遥测与召回图谱，可通过 MCP 查询 Claude Code、Codex、Cursor、OpenCode、Pi 的会话、工具调用、技能和成本数据。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, SurrealDB 存储, 编码代理可观测性与工作流复盘, AGPL-3.0。 |
| [kerlenton/mcpsnoop](https://github.com/kerlenton/mcpsnoop) | 「MCP 界的 Wireshark」——透明代理，在终端实时显示 AI 客户端（Claude Desktop / Cursor / Claude Code）与 MCP server 之间的每一次真实工具调用。零配置包裹 server 命令即可逐帧查看 JSON-RPC，支持调用重放、能力握手检查、挂起调用检测与过滤查询。 | 社区实现, Go 开发 🏎️, 本地运行 🏠, MCP 流量调试 (TUI), 单一二进制无运行时依赖, MIT。 |
| [msradam/ocarina](https://github.com/msradam/ocarina) | 面向 MCP server 的自动化测试框架。用 YAML 剧本（rondo）驱动一个或多个真实 server 的工具调用，支持步骤间传值、分支、循环、重试与 `expect` 断言，链路中无需 LLM，每次运行确定可复现且零 token 成本，开箱即可作 CI 健康检查。 | 社区实现, Go 开发 🏎️, 本地运行 🏠, MCP 确定性测试/自动化 (YAML), MIT。 |
| [docker/mcp-gateway](https://github.com/docker/mcp-gateway) | Docker 官方 MCP 网关与 `docker mcp` CLI 插件，安全聚合、编排并容器化运行多个 MCP 服务器。 | 官方实现 (Docker) 🎖️, Go 开发 🏎️, 本地/云端 🏠☁️, MCP 网关/聚合。 |
| [ref-tools/ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp) | 为编程代理提供公共/私有库的文档检索，减少调用陌生 API 时的幻觉并节省上下文窗口。 | 社区实现, TypeScript 开发 📇, 云服务 ☁️, 文档检索。 |
| [apollographql/apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server) | Apollo 官方 MCP 服务器，把 GraphQL 操作暴露为 AI 可调用的工具。 | 官方实现 (Apollo GraphQL) 🎖️, Rust 开发 🦀, 本地/云端 🏠☁️, GraphQL 工具化。 |
| [huggingface/hf-mcp-server](https://github.com/huggingface/hf-mcp-server) | Hugging Face 官方 MCP 服务器，检索 Hub 上的模型、数据集、论文与 Spaces 并调用相关工具。 | 官方实现 (Hugging Face) 🎖️, TypeScript 开发 📇, 云服务 ☁️, HF Hub 集成。 |


---

### 🖥️ 命令行与 Shell 交互

*(让 AI 能够执行命令行指令、与 Shell 交互)*

| 名称                                                                 | 中文介绍                                                                                        | 备注                                                                                      |
| :------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| [iTerm MCP](https://github.com/ferrislucas/iterm-mcp)                | 集成 macOS 的 iTerm2 终端，让 AI 执行和监控终端命令。                                           | 社区实现, Python 开发 🐍, 本地运行 🏠, macOS 终端控制 🍎。                              |
| [Windows CLI](https://github.com/SimonB97/win-cli-mcp-server)        | 在 Windows 系统上安全执行命令行（PowerShell, CMD, Git Bash）。                                  | 社区实现, Python 开发 🐍, 本地运行 🏠, Windows 命令行控制 🪟。                          |
| [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) | 使用 `run_command` 和 `run_script` 工具运行任何命令。                                  | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 通用命令执行。                             |
| [MladenSU/cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) | 具有安全执行和可自定义安全策略的命令行接口。                                             | 社区实现, Python 开发 🐍, 本地运行 🏠, 安全命令行执行。                                  |
| [OthmaneBlial/term_mcp_deepseek](https://github.com/OthmaneBlial/term_mcp_deepseek) | 用于终端的 DeepSeek 类 MCP 服务器。                                                | 社区实现, Python 开发 🐍, 本地运行 🏠, 终端交互。                                         |
| [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server)    | 实现模型上下文协议 (MCP) 的安全 Shell 命令执行服务器。                                   | 社区实现, Python 开发, 安全 Shell 执行。                                                  |
| [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | 多功能工具，可管理/执行程序，读/写/搜索/编辑代码和文本文件。(也含代码/文件功能)             | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 跨平台 🍎🪟🐧, 命令行/文件/程序管理。          |
| [olo-dot-io/Uni-CLI](https://github.com/olo-dot-io/Uni-CLI) | 自修复 CLI 目录，将网页、桌面应用、Electron 应用、外部 CLI 作为确定性命令通过一个 MCP 服务器暴露给 AI 代理；声明式 YAML 适配器加结构化错误信封，调用失败时代理可直接编辑 YAML 并重试。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 跨平台 🍎🪟🐧, Apache-2.0；目录规模与每次调用 token 预算见仓库 [README](https://github.com/olo-dot-io/Uni-CLI#readme) 与 [`docs/BENCHMARK.md`](https://github.com/olo-dot-io/Uni-CLI/blob/main/docs/BENCHMARK.md)。 |

---

### 🔄 版本控制 (Git / GitHub / GitLab)

*(让 AI 能够操作代码仓库、管理 Pull Request、处理 Issues 等)*

| 名称                                                                 | 中文介绍                                                                                        | 备注                                                                                          |
| :------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | GitHub 官方出品，让 AI 通过 API 深度集成 GitHub，实现自动化工作流等。                         | 官方实现 (GitHub), Go 开发 🏎️。功能全面，推荐 Docker 部署。                                  |
| [Gitee](https://github.com/oschina/mcp-gitee)                        | Gitee 官方集成，管理 Gitee 仓库、Issues 和 Pull Requests。                                    | 官方实现 (Gitee/oschina) 🎖️, Go 开发 🏎️, 云端/本地 ☁️🏠, Gitee 用户必备。                  |
| [gitea/gitea-mcp](https://gitea.com/gitea/gitea-mcp)                 | Gitea 官方集成，通过 MCP 与 Gitea 实例交互。                                           | 官方实现 (Gitea) 🎖️, Go 开发 🏎️, 云端/本地 ☁️🏠, 跨平台 🍎🪟🐧, Gitea 集成。          |
| [modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github) | 官方参考实现，集成 GitHub API，管理仓库、文件、PR 和 Issues。                                 | 官方参考, TypeScript 开发 📇, 云服务 ☁️, GitHub 重度用户必备。                             |
| [modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | 官方参考实现，直接操作本地 Git 仓库，进行读取、搜索和分析。                                   | 官方参考, Python 开发 🐍, 本地运行 🏠, 本地 Git 仓库操作。                                 |
| [modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gitlab) | 官方参考实现，集成 GitLab API，进行项目管理和 CI/CD 操作。                                    | 官方参考, TypeScript 开发 📇, 云端/本地 ☁️🏠, GitLab 用户适用。                         |
| [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) | 使用 LLM 读取和分析 GitHub 仓库。                                                    | 社区实现, Python 开发 🐍, 本地运行 🏠, GitHub 仓库分析。                                  |
| [ddukbg/github-enterprise-mcp](https://github.com/ddukbg/github-enterprise-mcp) | 用于 GitHub Enterprise API 集成的 MCP 服务器。                                       | 社区实现, TypeScript 开发 📇, 云端/本地 ☁️🏠, GitHub Enterprise 集成。                  |
| [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) | 无缝地与 GitLab 项目的 Issues 和 Merge Requests 交互。                                | 社区实现, TypeScript 开发 📇, 云服务 ☁️, GitLab Issues/MR 操作。                       |
| [Github Actions](https://github.com/ko1ynnky/github-actions-mcp-server) | 与 Github Actions 交互，管理工作流。                                                          | 社区实现, TypeScript 开发, GitHub Actions 管理。                                          |
| [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) | 用于仓库管理、工作项和流水线的 Azure DevOps 集成。                                  | 社区实现, TypeScript 开发 📇, 云服务 ☁️, Azure DevOps 集成。                          |
| [Forward-Future/DeployBot](https://github.com/Forward-Future/DeployBot) | 面向 Codex、Claude Code、Cursor 及任意 MCP 客户端的 agent 托管式 GitHub 合并队列。代理可准备并评审 PR，最终合并决定权仍归用户；权限存于 GitHub 标签与认证评论，支持突发冻结、串行合并、累积集成 PR 与失败后暂停。 | 社区实现, Python 开发 🐍, 云服务 ☁️, GitHub 合并队列 (MCP), MIT。 |

---

### 🗄️ 数据库交互

*(让 AI 能够查询数据库、检查表结构、甚至修改数据)*

| 名称                                                                 | 中文介绍                                                                                              | 备注                                                                                                       |
| :------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| [Alibaba Cloud AnalyticDB for MySQL](https://github.com/aliyun/alibabacloud-adb-mysql-mcp-server) | 阿里云 AnalyticDB for MySQL 官方集成，连接 AnalyticDB for MySQL 集群进行数据库元数据查询和数据分析。 | 官方实现 (Alibaba Cloud) 🎖️, 阿里云数据库服务。                                                          |
| [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) | MongoDB 官方 MCP 服务器，连接 MongoDB 数据库与 Atlas 集群，支持查询、聚合、索引管理与集群运维。 | 官方实现 (MongoDB) 🎖️, TypeScript 开发 📇, 本地/云端 🏠☁️, MongoDB 数据库管理。 |
| [redis/mcp-redis](https://github.com/redis/mcp-redis) | Redis 官方 MCP 服务器，为智能体应用提供自然语言接口，高效管理和搜索 Redis 中的数据。 | 官方实现 (Redis) 🎖️, Python 开发 🐍, 本地/云端 🏠☁️, Redis 数据管理与检索。 |
| [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) | Elastic 官方 MCP 服务器，用自然语言查询 Elasticsearch 索引数据，进行全文搜索与数据探索。 | 官方实现 (Elastic) 🎖️, TypeScript 开发 📇, 本地/云端 🏠☁️, Elasticsearch 搜索分析。 |
| [Alibaba Cloud AnalyticDB for PostgreSQL](https://github.com/aliyun/alibabacloud-adbpg-mcp-server) | 阿里云 AnalyticDB for PostgreSQL 官方集成，连接 AnalyticDB for PostgreSQL 实例，查询和分析数据。     | 官方实现 (Alibaba Cloud) 🎖️, 阿里云 PostgreSQL 服务。                                                   |
| [Aiven](https://github.com/Aiven-Open/mcp-aiven)                     | Aiven 官方集成，导航 Aiven 项目，与 PostgreSQL®, Kafka®, ClickHouse®, OpenSearch® 服务交互。          | 官方实现 (Aiven) 🎖️, Python 开发 🐍, 云服务 ☁️, Aiven 云数据库管理。                                       |
| [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) | ClickHouse 官方集成，连接 ClickHouse 数据库进行查询和模式检查。                                       | 官方实现 (ClickHouse) 🎖️, Python 开发 🐍, 云服务 ☁️, ClickHouse 数据分析利器。                             |
| [Chroma](https://github.com/chroma-core/chroma-mcp)                  | Chroma 官方集成，用于嵌入、向量搜索、文档存储和全文搜索。                                                 | 官方实现 (Chroma) 🎖️, Python 开发 🐍, 本地/云端 🏠☁️, AI 应用数据库，向量搜索。                           |
| [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) | Confluent 集成，与 Confluent Kafka 和 Confluent Cloud REST API 交互。                          | 官方实现 (Confluent) 🎖️, Python 开发 🐍, 云服务 ☁️, Kafka 集成。                                      |
| [fireproof-storage/mcp-database-server](https://github.com/fireproof-storage/mcp-database-server) | Fireproof 官方集成，不可变账本数据库，支持实时同步。                                                    | 官方实现 (Fireproof) 🎖️, TypeScript 开发 📇, 云服务 ☁️, 分布式数据库同步。                            |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | Google 官方开源 MCP 服务器，专注于为数据库提供简单、快速、安全的工具。                            | 官方实现 (Google) 🎖️, Go 开发 🏎️, 云服务 ☁️, Google Cloud 数据库工具。                           |
| [GreptimeDB](https://github.com/GreptimeTeam/greptimedb-mcp-server)  | GreptimeDB 官方集成，让 AI 安全地探索和分析 GreptimeDB 中的时序数据。                                   | 官方实现 (Greptime) 🎖️, Python 开发 🐍, 本地运行 🏠, GreptimeDB 时序数据分析。                           |
| [Milvus](https://github.com/zilliztech/mcp-server-milvus)            | Zilliz/Milvus 官方集成，搜索、查询和交互 Milvus 向量数据库中的数据。                                    | 官方实现 (Zilliz/Milvus) 🎖️, Python 开发 🐍, 本地/云端 🏠☁️, Milvus 向量数据库操作。                    |
| [MotherDuck](https://github.com/motherduckdb/mcp-server-motherduck)  | MotherDuck 官方集成，使用 MotherDuck 和本地 DuckDB 查询和分析数据。                                     | 官方实现 (MotherDuck), Python 开发, DuckDB 云服务交互。                                                    |
| [Neo4j](https://github.com/neo4j-contrib/mcp-neo4j/)                 | Neo4j 官方贡献，操作 Neo4j 图数据库（模式+读写 Cypher），并提供图数据库支持的记忆功能。                     | 官方贡献 (Neo4j) 🎖️, Python 开发 🐍, 本地运行 🏠, 图数据库操作和记忆。                                  |
| [Neon](https://github.com/neondatabase/mcp-server-neon)              | Neon 官方集成，与 Neon 无服务器 Postgres 平台交互，创建和管理数据库。                                   | 官方实现 (Neon) 🎖️, TypeScript 开发 📇, 云服务 ☁️, Neon Serverless PG 管理。                          |
| [niledatabase/nile-mcp-server](https://github.com/niledatabase/nile-mcp-server) | Nile 的 Postgres 平台 MCP 服务器 - 使用 LLM 管理和查询 Postgres 数据库、租户、用户、认证。     | 官方实现 (Nile) 🎖️, Python 开发, Nile PG 平台管理。                                                  |
| [Qdrant](https://github.com/qdrant/mcp-server-qdrant/)               | Qdrant 官方集成，基于 Qdrant 向量搜索引擎实现语义记忆层。                                                 | 官方实现 (Qdrant) 🎖️, Python 开发 🐍, 本地运行 🏠, Qdrant 向量搜索与记忆。                            |
| [SingleStore](https://github.com/singlestore-labs/mcp-server-singlestore) | SingleStore 官方集成，与 SingleStore 数据库平台交互。                                                 | 官方实现 (SingleStore), Python 开发, SingleStore 数据库操作。                                           |
| [StarRocks](https://github.com/StarRocks/mcp-server-starrocks)       | StarRocks 官方集成，与 StarRocks 数据库交互。                                                          | 官方实现 (StarRocks), Python 开发, StarRocks 数据仓库交互。                                            |
| [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) | Supabase 官方 MCP 服务器，将 AI 助手直接连接到你的 Supabase 项目，允许执行任务如管理表、获取配置和查询数据。 | 官方实现 (Supabase Community) 🎖️, TypeScript 开发 📇, 云服务 ☁️, Supabase 项目管理与查询。         |
| [Tinybird](https://github.com/tinybirdco/mcp-tinybird)               | Tinybird 官方集成，与 Tinybird 无服务器 ClickHouse 平台交互 (查询和 API 能力)。                       | 官方实现 (Tinybird) 🎖️, Python 开发 🐍, 云服务 ☁️, Tinybird 平台交互。                               |
| [weaviate/mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate) | 连接到 Weaviate 集合作为知识库，并将 Weaviate 用作聊天记忆存储的 MCP 服务器。                 | 官方实现 (Weaviate) 🎖️, Python/TypeScript 开发 🐍📇, 云服务 ☁️, Weaviate 知识库/记忆。            |
| [modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres) | 官方参考实现，集成 PostgreSQL，支持查询和模式分析。                                                    | 官方参考, TypeScript 开发 📇, 本地运行 🏠, PostgreSQL 数据库操作。                                  |
| [modelcontextprotocol/server-redis](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/redis) | 官方参考实现，与 Redis 键值存储进行交互。                                                              | 官方参考, TypeScript 开发, Redis 缓存/存储操作。                                                      |
| [modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sqlite) | 官方参考实现，操作 SQLite 数据库，并内置商业智能能力。                                                  | 官方参考, Python 开发 🐍, 本地运行 🏠, 本地 SQLite 数据库操作。                                        |
| [DBHub](https://github.com/bytebase/dbhub/)                          | 通用数据库 MCP 服务器，可连接 MySQL, PostgreSQL, SQLite, DuckDB 等。                                  | 社区实现 (Bytebase) 🎖️, TypeScript 开发 📇, 本地运行 🏠, 多种数据库支持。                           |
| [alexanderzuev/supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) | Supabase MCP 服务器，支持 SQL 查询执行和数据库探索工具。                                       | 社区实现, Supabase 集成。                                                                         |
| [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) | 阿里云 Tablestore MCP 服务，功能包括添加文档、基于向量和标量的文档语义搜索、RAG 友好、Serverless。 | 官方实现 (Alibaba Cloud) 🎖️, Java/Python 开发 ☕🐍, 云服务 ☁️, 阿里云 Tablestore。              |
| [benborla29/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) | NodeJS 中的 MySQL 数据库集成，具有可配置的访问控制和模式检查。                               | 社区实现, Node.js 开发, 云端/本地 ☁️🏠, MySQL 集成 (Node.js)。                                   |
| [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb)     | TiDB 数据库集成，具有模式检查和查询能力。                                                        | 社区实现, Python 开发 🐍, 云服务 ☁️, TiDB 集成。                                               |
| [Canner/wren-engine](https://github.com/Canner/wren-engine)          | 面向 MCP 客户端和 AI Agents 的语义引擎。                                                        | 社区实现, Python/Rust 开发 🐍🦀, 本地运行 🏠, 语义引擎。                                        |
| [centralmind/gateway](https://github.com/centralmind/gateway)        | MCP 和 MCP SSE 服务器，根据数据库模式和数据自动生成 API。支持 PG, Clickhouse, MySQL, Snowflake, BigQuery, Supabase。 | 社区实现, Go 开发 🏎️, 本地运行 🏠, 跨平台 🍎🪟, 数据库 API 自动生成。                        |
| [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) | 提供 Elasticsearch 交互的 MCP 服务器实现。                                                 | 社区实现, Python 开发 🐍, 本地运行 🏠, Elasticsearch 集成。                                     |
| [Dataring-engineering/mcp-server-trino](https://github.com/Dataring-engineering/mcp-server-trino) | Trino MCP 服务器，用于从 Trino 集群查询和访问数据。                                        | 社区实现, Python 开发 🐍, 云服务 ☁️, Trino 集成。                                               |
| [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) | Python 实现的 MySQL 集成，带访问控制和模式检查。                                                        | 社区实现, Python 开发 🐍, 本地运行 🏠, MySQL 数据库操作。                                        |
| [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) | 读写 Airtable 数据库，带模式检查。                                                                | 社区实现, TypeScript 开发 📇, 本地运行 🏠, Airtable 读写。                                      |
| [edwinbernadus/nocodb-mcp-server](https://github.com/edwinbernadus/nocodb-mcp-server) | Nocodb 数据库集成，读写能力。                                                            | 社区实现, TypeScript 开发 📇, 云服务 ☁️, Nocodb 集成。                                       |
| [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) | Google BigQuery 集成的服务器实现，支持直接访问和查询。                                       | 社区实现, TypeScript 开发 📇, 云服务 ☁️, BigQuery 集成 (TS)。                                   |
| [f4ww4z/mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)    | 基于 Node.js 的 MySQL 数据库集成，提供安全的数据库操作。                                    | 社区实现, Node.js 开发, 本地运行 🏠, MySQL 集成 (Node.js)。                                     |
| [FreePeak/db-mcp-server](https://github.com/FreePeak/db-mcp-server)    | 高性能多数据库 MCP 服务器 (Go)，支持 MySQL & PG (NoSQL 即将推出)。含查询、事务、模式探索等工具。 | 社区实现, Go 开发 🏎️, 本地运行 🏠, 多数据库支持 (Go)。                                        |
| [furey/mongodb-lens](https://github.com/furey/mongodb-lens)            | 功能齐全的 MongoDB 数据库 MCP 服务器。                                                            | 社区实现, TypeScript 开发 📇, 本地运行 🏠, MongoDB 高级操作。                                    |
| [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp)        | Firebase 服务，包括 Auth、Firestore 和 Storage。                                            | 社区实现, Firebase 集成 🔥, 云服务 ☁️.                                                        |
| [get-convex/convex-backend](https://stack.convex.dev/convex-mcp-server) | Convex 数据库集成，用于内省表、函数和运行一次性查询。                                         | 官方实现 (Convex) 🎖️, TypeScript 开发 📇, 云服务 ☁️, Convex 集成。 ([Source](https://github.com/get-convex/convex-backend/blob/main/npm-packages/convex/src/cli/mcp.ts)) |
| [hannesrudolph/sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) | 提供对 SQLite 数据库安全只读访问的 MCP 服务器 (FastMCP)。LLM 可探索查询，带安全特性和查询验证。 | 社区实现, Python 开发 🐍, 本地运行 🏠, SQLite 安全只读访问 (FastMCP)。                         |
| [idoru/influxdb-mcp-server](https://github.com/idoru/influxdb-mcp-server) | 对 InfluxDB OSS API v2 执行查询。                                                        | 社区实现, TypeScript 开发 📇, 云端/本地 ☁️🏠, InfluxDB 查询。                                  |
| [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) | Snowflake 集成，实现读和（可选）写操作以及洞察跟踪。                                        | 社区实现, Python 开发 🐍, 云服务 ☁️, Snowflake 集成。                                        |
| [joshuarileydev/supabase-mcp-server](https://github.com/joshuarileydev/supabase) | 用于在 Supabase 中管理和创建项目及组织的 Supabase MCP 服务器。                                | 社区实现, Supabase 管理。                                                                       |
| [jovezhong/mcp-timeplus](https://github.com/jovezhong/mcp-timeplus)    | Apache Kafka 和 Timeplus 的 MCP 服务器。能列出 Kafka 主题、轮询消息、本地保存数据并通过 Timeplus 用 SQL 查询流数据。 | 社区实现, Python 开发 🐍, 云服务 ☁️, Kafka/Timeplus 集成。                                   |
| [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) | VikingDB 集成，具有集合和索引介绍、向量存储和搜索能力。                                     | 社区实现, Python 开发 🐍, 云服务 ☁️, VikingDB 集成。                                          |
| [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) | 用于 MongoDB 的模型上下文协议服务器。                                                       | 社区实现, TypeScript 开发 📇, 本地运行 🏠, MongoDB 集成 (TS)。                                |
| [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) | DuckDB 数据库集成，具有模式检查和查询能力。                                                 | 社区实现, Python 开发 🐍, 本地运行 🏠, DuckDB 集成。                                          |
| [BigQuery (by LucasHild)](https://github.com/LucasHild/mcp-server-bigquery) | 让 AI 检查 BigQuery 数据库模式并执行查询。                                                         | 社区实现, Python 开发 🐍, 云服务 ☁️, Google BigQuery 查询。                                    |
| [mcp-server-jdbc](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jdbc) | 连接到任何兼容 JDBC 的数据库，并执行查询、插入、更新、删除等操作。                           | 社区实现 (Quarkiverse), Java 开发 ☕, 本地运行 🏠, 通用 JDBC 连接。                            |
| [memgraph/mcp-memgraph](https://github.com/memgraph/ai-toolkit)    | Memgraph MCP 服务器 - 包括对 Memgraph 执行查询和模式资源的工具。                               | 官方实现 (Memgraph) 🎖️, Python 开发 🐍, 本地运行 🏠, Memgraph 集成。                            |
| [openlink/mcp-server-odbc](https://github.com/OpenLinkSoftware/mcp-odbc-server) | 通过开放数据库连接 (ODBC) 协议实现通用数据库管理系统 (DBMS) 连接的 MCP 服务器。              | 社区实现 (OpenLink), Python 开发 🐍, 本地运行 🏠, 通用 ODBC 连接。                             |
| [openlink/mcp-server-sqlalchemy](https://github.com/OpenLinkSoftware/mcp-sqlalchemy-server) | 通过 SQLAlchemy 使用 Python ODBC (pyodbc) 实现通用 DBMS 连接的 MCP 服务器。             | 社区实现 (OpenLink), Python 开发 🐍, 本地运行 🏠, 通用 SQLAlchemy 连接 (ODBC)。                 |
| [pab1it0/adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)      | 查询和分析 Azure Data Explorer 数据库。                                                  | 社区实现, Python 开发 🐍, 云服务 ☁️, Azure Data Explorer 查询。                               |
| [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) | 查询和分析 Prometheus 开源监控系统。                                                    | 社区实现, Python 开发 🐍, 云服务 ☁️, Prometheus 查询。                                      |
| [PerfectXM/mcp-db-server](https://github.com/PerfectXM/mcp-db-server) | 无状态数据库 MCP 服务，连接参数即传即用、零持久化零配置，让 AI 直接操作 MySQL / PostgreSQL / SQLite / SQL Server / Oracle / H2。 | 社区实现, Java 开发 ☕, 本地运行 🏠, 多数据库无状态连接, MIT。 |
| [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)    | MongoDB 集成，使 LLM 能够直接与数据库交互。                                                 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, MongoDB 集成 (TS)。                                |
| [rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp) | 将 AI 工具直接连接到 Airtable。使用自然语言查询、创建、更新和删除记录。功能包括库管理、表操作等。 | 社区实现, Python 开发 🐍, 云服务 ☁️, Airtable 全功能操作 (Python)。                          |
| [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) | 通用 SQLAlchemy 数据库集成，支持 PG, MySQL, MariaDB, SQLite, Oracle, MS SQL Server 等。含模式/关系检查和大数据集分析能力。 | 社区实现, Python 开发 🐍, 本地运行 🏠, 通用 SQLAlchemy 集成。                                  |
| [sirmews/mcp-pinecone](https://github.com/sirmews/mcp-pinecone)        | Pinecone 集成，具有向量搜索能力。                                                        | 社区实现, Python 开发 🐍, 云服务 ☁️, Pinecone 向量搜索。                                     |
| [TheRaLabs/legion-mcp](https://github.com/TheRaLabs/legion-mcp)        | 通用数据库 MCP 服务器，支持 PG, Redshift, CockroachDB, MySQL, RDS MySQL, MS SQL Server, BigQuery, Oracle DB, SQLite。 | 社区实现, Python 开发 🐍, 本地运行 🏠, 多种数据库支持 (Python)。                               |
| [tradercjz/dolphindb-mcp-server](https://github.com/tradercjz/dolphindb-mcp-server) | DolphinDB 数据库集成，具有模式检查和查询能力。                                             | 社区实现, Python 开发 🐍, 云服务 ☁️, DolphinDB 集成。                                        |
| [XGenerationLab/xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server) | 支持使用自然语言查询从数据库获取数据的 MCP 服务器，由 XiyanSQL 作为 text-to-SQL LLM 驱动。   | 社区实现, TypeScript 开发 📇, 云服务 ☁️, 自然语言转 SQL 查询 (XiyanSQL)。                    |
| [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)    | 用于与 Google Sheets 交互的模型上下文协议服务器。提供创建、读取、更新和管理电子表格的工具。        | 社区实现, Python 开发 🐍, 云服务 ☁️, Google Sheets 操作。                                    |
| [Zhwt/go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)              | 易于使用、零依赖的 MySQL MCP 服务器 (Go)，具有可配置的只读模式和模式检查。                  | 社区实现, Go 开发 🏎️, 本地运行 🏠, MySQL 集成 (Go)。                                         |

---

### ☁️ 云平台与服务集成 (AWS, Cloudflare, Azure, K8s, etc.)

*(让 AI 能够管理云资源、调用云服务 API 等)*

| 名称                                                                 | 中文介绍                                                                                             | 备注                                                                                                          |
| :------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| [Alibaba Cloud DataWorks](https://github.com/aliyun/alibabacloud-dataworks-mcp-server) | 阿里云 DataWorks 官方集成，通过标准化接口与 DataWorks Open API 进行 AI 交互，用于云资源操作。      | 官方实现 (Alibaba Cloud) 🎖️, 阿里云数据平台。                                                               |
| [AWS MCP Servers](https://github.com/awslabs/mcp) | AWS 官方维护的一组 MCP 服务器合集，通过 Model Context Protocol（MCP）为 AI 助手提供对 AWS 文档、API、基础设施等资源的访问，帮助在任意支持 MCP 的环境中高效使用 AWS。  | 官方实现（AWS）🎖️，覆盖 AWS API、文档/最佳实践、基础设施与部署等多类场景，可配合各类 MCP 客户端（IDE、聊天应用等）使用。 |
| [Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)    | Cloudflare 官方集成，部署、配置和查询 Cloudflare 开发者平台资源 (Workers/KV/R2/D1)。                   | 官方实现 (Cloudflare) 🎖️, TypeScript 开发 📇, 云服务 ☁️, Cloudflare 平台管理。                           |
| [microsoft/mcp](https://github.com/microsoft/mcp) | 微软官方维护的 MCP 服务器合集目录，汇总 Azure、Microsoft 365、Dev Box、Files 等官方实现，为 AI 提供数据访问与工具集成。 | 官方实现 (Microsoft) 🎖️, 多语言, 官方 MCP 服务器目录。 |
| [Azure/azure-mcp](https://github.com/Azure/azure-mcp) | 微软 Azure 官方 MCP 服务器，让 AI 代理管理和查询 Azure 资源（存储、Cosmos DB、Monitor、AKS 等）。 | 官方实现 (Microsoft Azure) 🎖️, C#/.NET 开发, 云服务 ☁️, Azure 资源管理。 |
| [AWS KB Retrieval](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/aws-kb-retrieval-server) | 官方参考实现，使用 Bedrock Agent Runtime 从 AWS 知识库检索信息。                                     | 官方参考, TypeScript 开发, AWS Bedrock 知识库。                                                             |
| [AWS S3](https://github.com/aws-samples/sample-mcp-server-s3)        | AWS 官方示例，灵活地从 S3 获取对象（如 PDF 文档）。                                                  | 官方示例 (AWS), TypeScript 开发, S3 文件获取。                                                               |
| [VolcEngine TOS](https://github.com/dinghuazhou/sample-mcp-server-tos) | 火山引擎官方示例，灵活地从火山引擎对象存储 (TOS) 获取对象。                                           | 官方示例 (VolcEngine), TypeScript 开发, 火山引擎 TOS 文件获取。                                             |
| [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs)        | 上传和操作 IPFS 存储。                                                                        | 社区实现, TypeScript 开发 📇, 云服务 ☁️, IPFS 存储操作。                                                 |
| [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) | 轻量级服务器，让 AI 执行 AWS CLI 命令 (带 Unix 管道和模板)，支持 Docker 安全运行 (多架构)。              | 社区实现, Python 开发 🐍, 云服务 ☁️, 通过 CLI 管理 AWS (安全 Docker)。                                      |
| [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) | 轻量级服务器，让 AI 安全地执行 Kubernetes CLI 命令 (`kubectl`, `helm`, `istioctl`, `argocd`) (带 Unix 管道)，支持 Docker 安全运行 (多架构)。 | 社区实现, Python 开发 🐍, Kubernetes CLI 操作 (安全 Docker)。                                             |
| [AWS Resources Operations](https://github.com/baryhuang/mcp-server-aws-resources-python) | 运行生成的 Python 代码以安全地查询或修改任何 boto3 支持的 AWS 资源。                                | 社区实现, Python 开发, 通过 Boto3 管理 AWS 资源。                                                          |
| [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) | 基于 MCP 的 VMware ESXi/vCenter 管理服务器，提供虚拟机管理的简单 REST API 接口。                 | 社区实现, Python 开发 🐍, 云服务 ☁️, VMware ESXi/vCenter 管理。                                          |
| [flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) | Kubernetes 集群操作的 TypeScript 实现 (pods, deployments, services)。                     | 社区实现, TypeScript 开发 📇, 云端/本地 ☁️🏠, Kubernetes 操作 (TS)。                                     |
| [hardik-id/azure-resource-graph-mcp-server](https://github.com/hardik-id/azure-resource-graph-mcp-server) | 使用 Azure Resource Graph 大规模查询和分析 Azure 资源的 MCP 服务器，使 AI 助手能探索监控 Azure 基础设施。 | 社区实现, TypeScript 开发 📇, 云端/本地 ☁️🏠, Azure Resource Graph 查询。                               |
| [jdubois/azure-cli-mcp](https://github.com/chanezon/azure-cli-mcp)      | Azure CLI 命令行包装器，允许直接与 Azure 对话。                                                | 社区实现, Azure CLI 封装。                                                                                  |
| [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) | 提供对 Netskope Private Access 环境中所有组件的访问，包括详细设置信息和 LLM 使用示例。           | 社区实现, 云服务 ☁️, Netskope Private Access 集成。                                                       |
| [Kubernetes (Go)](https://github.com/strowk/mcp-k8s-go)               | Go 语言实现的 Kubernetes 服务器，用于浏览 Pods、日志、事件、命名空间等。                               | 社区实现, Go 开发 🏎️, 云端/本地 ☁️🏠, Kubernetes 集群管理 (Go)。                                          |
| [Kubernetes and OpenShift](https://github.com/manusa/kubernetes-mcp-server) | 功能强大的 Kubernetes MCP 服务器，额外支持 OpenShift。提供 CRUD 操作及专用工具。                       | 社区实现, Go 开发 🏎️, 本地运行 🏠, Kubernetes/OpenShift 高级管理。                                       |
| [KubeStellar Console](https://github.com/kubestellar/console) | AI 驱动的多集群 Kubernetes 管理仪表板，内置 MCP 服务器 (kc-agent)，支持 AI 辅助运维、合规审计和跨集群资源管理。 | 社区实现, Go/TypeScript 开发 🏎️📇, 本地 🏠, 多集群 K8s 管理仪表板 (AI + MCP)。 |
| [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)                      | Terraform MCP 服务器，允许 AI 助手管理和操作 Terraform 环境 (读配置/分析计划/应用配置/管理状态)。   | 社区实现, Rust 开发 🦀, 本地运行 🏠, Terraform 管理。                                                    |
| [Pulumi](https://github.com/dogukanakkaya/pulumi-mcp-server)         | 与 Pulumi API 交互，创建和列出 Stacks（基础设施即代码）。                                           | 社区实现, Go 开发, Pulumi IaC 管理。                                                                        |
| [rohitg00/kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) | 用于 Kubernetes 的 MCP 服务器，使 AI 助手能通过自然语言与 K8s 集群交互。                       | 社区实现, Python 开发 🐍, 云端/本地 ☁️🏠, Kubernetes 自然语言交互。                                      |
| [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s)          | AI 驱动的 Kubernetes 资源管理工具，允许通过自然语言操作 K8s 集群中的任何资源 (原生/CRD)。         | 社区实现, Go 开发 🏎️, 云端/本地 ☁️🏠, AI 驱动 K8s 管理。                                                |
| [thunderboltsid/mcp-nutanix](https://github.com/thunderboltsid/mcp-nutanix) | 基于 Go 的 MCP 服务器，用于与 Nutanix Prism Central 资源交互。                              | 社区实现, Go 开发 🏎️, 本地/云端 🏠☁️, Nutanix Prism Central 交互。                                  |
| [weibaohui/k8m](https://github.com/weibaohui/k8m)                    | 提供 MCP 多集群 Kubernetes 管理和操作，带管理界面、日志记录和近 50 个内置工具 (支持标准/CRD)。   | 社区实现, Go 开发 🏎️, 云端/本地 ☁️🏠, 多集群 K8s 管理 (带 UI)。                                       |
| [weibaohui/kom](https://github.com/weibaohui/kom)                    | 提供 MCP 多集群 Kubernetes 管理和操作。可作为 SDK 集成到项目中，含近 50 个内置工具 (支持标准/CRD)。 | 社区实现, Go 开发 🏎️, 云端/本地 ☁️🏠, 多集群 K8s 管理 (SDK)。                                        |
| [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye)      | 用于 Kubernetes 管理的 MCP 服务器，分析集群和应用健康状况。                                   | 社区实现, Go 开发 🏎️, 云端/本地 ☁️🏠, K8s 管理与健康分析。                                         |
| [erikhoward/adls-mcp-server](https://github.com/erikhoward/adls-mcp-server) | 用于 Azure Data Lake Storage 的 MCP 服务器。可管理容器、读/写/上传/下载文件及管理元数据。   | 社区实现, Python 开发 🐍, 云端/本地 ☁️🏠, Azure Data Lake Storage 管理。                              |
| [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) | HashiCorp 官方出品，让 AI 与 Terraform 生态（Registry、Provider/模块文档等）深度集成，辅助 IaC 开发。 | 官方实现 (HashiCorp) 🎖️, Go 开发 🏎️, 本地/云端 🏠☁️, Terraform IaC。 |

---

### 🔍 搜索

*(让 AI 能够调用各种搜索引擎或专业搜索服务)*

| 名称                                                                 | 中文介绍                                                                                           | 备注                                                                                        |
| :------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| [Alibaba Cloud OpenSearch](https://github.com/aliyun/alibabacloud-opensearch-mcp-server) | 阿里云 OpenSearch 官方集成，AI 代理通过标准化接口与 OpenSearch 交互的工具。                      | 官方实现 (Alibaba Cloud) 🎖️, 阿里云搜索服务。                                              |
| [Exa](https://github.com/exa-labs/exa-mcp-server)                    | Exa 官方集成，使用专为 AI 设计的 Exa 搜索引擎进行搜索。                                             | 官方实现 (Exa) 🎖️, TypeScript 开发 📇, 云服务 ☁️, AI 专用搜索引擎。                         |
| [Kagi Search](https://github.com/kagisearch/kagimcp)                 | Kagi 官方集成，使用 Kagi 的搜索 API 进行网页搜索。                                                 | 官方实现 (Kagi) 🎖️, TypeScript 开发 📇, 云服务 ☁️, Kagi 搜索引擎。 (用户列表为Py, awesome为TS) |
| [Perplexity](https://github.com/ppl-ai/modelcontextprotocol)         | Perplexity 官方集成，连接 Perplexity Sonar API，实现实时全网研究。                                    | 官方实现 (Perplexity), Python 开发, Perplexity 实时搜索。                                   |
| [Search1API](https://github.com/fatwang2/search1api-mcp)             | Search1API 官方集成，一个 API 实现搜索、抓取和站点地图功能 (需付费 API Key)。                      | 官方实现 (Search1API), TypeScript 开发 📇, 云服务 ☁️, 多功能搜索 API。                     |
| [Tavily](https://github.com/tavily-ai/tavily-mcp)                    | Tavily 官方集成，专为 AI 代理设计的搜索引擎（搜索+提取）。                                           | 官方实现 (Tavily), Python 开发, AI 代理专用搜索引擎。                                       |
| [tinyfish-io/agentql-mcp](https://github.com/tinyfish-io/agentql-mcp) | AgentQL MCP 服务器，提供 AgentQL 的数据提取能力。                                           | 官方实现 (TinyFish IO) 🎖️, TypeScript 开发 📇, 云服务 ☁️, AgentQL 数据提取。             |
| [vectorize-io/vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server) | Vectorize MCP 服务器，用于高级检索、私有深度研究、任意文件转 Markdown 提取和文本分块。        | 官方实现 (Vectorize) 🎖️, TypeScript 开发 📇, 云服务 ☁️, 高级检索/RAG。                   |
| [zoomeye-ai/mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)  | 通过 ZoomEye MCP 服务器查询网络资产信息。                                                   | 官方实现 (ZoomEye), TypeScript 开发 📇, 云服务 ☁️, 网络空间测绘搜索。                     |
| [Brave Search](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/brave-search) | 官方参考实现，使用 Brave 的搜索 API 进行网页和本地搜索。                                           | 官方参考, TypeScript 开发 📇, 云服务 ☁️, Brave 搜索引擎。                                    |
| [0xdaef0f/job-searchoor](https://github.com/0xDAEF0F/job-searchoor)    | 用于搜索职位列表的 MCP 服务器，支持日期、关键词、远程工作选项等筛选。                            | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 职位搜索。                                      |
| [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)  | Kagi 搜索 API 集成 (社区实现版本)。                                                       | 社区实现, TypeScript 开发 📇, 云服务 ☁️, Kagi 搜索 (社区 TS 版)。                         |
| [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) | 让 LLM 从 arXiv 搜索和阅读论文的 MCP。                                                 | 社区实现, Python 开发 🐍, 云服务 ☁️, arXiv 论文搜索。                                       |
| [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) | 让 LLM 从 PubMed 搜索和阅读医学/生命科学论文的 MCP。                                  | 社区实现, Python 开发 🐍, 云服务 ☁️, PubMed 论文搜索。                                    |
| [angheljf/nyt](https://github.com/angheljf/nyt)                      | 使用 NYTimes API 搜索文章。                                                            | 社区实现, TypeScript 开发 📇, 云服务 ☁️, 纽约时报文章搜索。                                 |
| [Bigsy/Clojars-MCP-Server](https://github.com/Bigsy/Clojars-MCP-Server) | Clojars MCP 服务器，提供 Clojure 库的最新依赖信息。                                        | 社区实现, TypeScript 开发 📇, 云服务 ☁️, Clojure 依赖搜索。                                |
| [ClawSearch](https://clawsearch.cc) | 安全优先的 AI Agent 技能搜索引擎，提供 Trust Score 评分、10语言语义搜索和供应链安全检查。 | 社区实现, 云服务 ☁️, AI Agent 技能安全搜索。 |
| [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | 搜索 ArXiv 研究论文。                                                                 | 社区实现, Python 开发 🐍, 云服务 ☁️, ArXiv 搜索 (另一版本)。                                |
| [connerlambden/bgpt-mcp](https://github.com/connerlambden/bgpt-mcp) | 搜索科学论文，获取从全文研究中提取的结构化实验数据，每篇论文返回25+字段，包括方法、结果、样本量、局限性和质量评分。 | 社区实现, Python 开发 🐍, 云服务 ☁️, 科学论文结构化数据搜索。                                |
| [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) | Google News 集成，自动主题分类，多语言支持，全面搜索能力 (SerpAPI)。                    | 社区实现, TypeScript 开发 📇, 云服务 ☁️, Google News 搜索 (SerpAPI)。                   |
| [ConechoAI/openai-websearch-mcp](https://github.com/ConechoAI/openai-websearch-mcp) | 提供 OpenAI `web_search` 内置工具的 Python MCP 服务器。                                  | 社区实现, Python 开发 🐍, 本地/云端 🏠☁️, OpenAI 网页搜索模拟。                           |
| [devflowinc/trieve](https://github.com/devflowinc/trieve/tree/main/clients/mcp-server) | 通过 Trieve 爬取、嵌入、分块、搜索和检索数据集信息。                                      | 官方实现 (Trieve) 🎖️, TypeScript 开发 📇, 云端/本地 🏠☁️, Trieve RAG 平台。              |
| [Dumpling-AI/mcp-server-dumplingai](https://github.com/Dumpling-AI/mcp-server-dumplingai) | 访问 Dumpling AI 提供的数据、网页抓取和文档转换 API。                                    | 官方实现 (Dumpling AI) 🎖️, TypeScript 开发 📇, 云服务 ☁️, Dumpling AI API 集成。           |
| [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn)                | 用于搜索 Hacker News、获取头条等的 MCP 服务器。                                            | 社区实现, Python 开发 🐍, 云服务 ☁️, Hacker News 搜索。                                   |
| [genomoncology/biomcp](https://github.com/genomoncology/biomcp)        | 生物医学研究服务器，提供对 PubMed、ClinicalTrials.gov 和 MyVariant.info 的访问。         | 社区实现, Python 开发 🐍, 云服务 ☁️, 生物医学信息搜索。                                     |
| [Google Custom Search](https://github.com/adenot/mcp-google-search)  | 通过 Google 自定义搜索 API 提供 Google 搜索结果。                                                | 社区实现, TypeScript 开发, Google 自定义搜索。                                            |
| [hellokaton/unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server) | 用于 Unsplash 图片搜索的 MCP 服务器。                                                  | 社区实现, Python 开发 🐍, 云服务 ☁️, Unsplash 图片搜索。                                  |
| [Ihor-Sokoliuk/MCP-SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) | 连接到 SearXNG 元搜索引擎实例。                                                             | 社区实现, TypeScript 开发 📇, 本地/云端 🏠☁️, SearXNG 元搜索。                             |
| [isnow890/naver-search-mcp](https://github.com/isnow890/naver-search-mcp) | Naver 搜索 API 集成 MCP 服务器，支持博客、新闻、购物搜索和 DataLab 分析功能。               | 社区实现, TypeScript 开发 📇, 云服务 ☁️, Naver 搜索 (韩国)。                              |
| [Bing Web Search API](https://github.com/leehanchung/bing-search-mcp) | 微软必应网页搜索 API 的服务器实现。                                                             | 社区实现, Python 开发 🐍, Bing 搜索。 (Awesome列表为TS, 用户列表为Py, 可能有多个实现)           |
| [kshern/mcp-tavily](https://github.com/kshern/mcp-tavily.git)        | Tavily AI 搜索 API (社区实现版本)。                                                    | 社区实现, TypeScript 开发 📇, 云服务 ☁️, Tavily 搜索 (社区 TS 版)。                        |
| [mzxrai/mcp-webresearch](https://github.com/mzxrai/mcp-webresearch)    | 搜索 Google 并在任何主题上进行深度网络研究。                                                | 社区实现, 搜索与研究。                                                                        |
| [nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server) | 使用 DuckDuckGo 进行网页搜索。                                                         | 社区实现, Python 开发 🐍, 云服务 ☁️, DuckDuckGo 搜索 (Python)。                            |
| [pskill9/web-search](https://github.com/pskill9/web-search)            | 无需 API Key，使用 Google 搜索结果进行免费网页搜索的 MCP 服务器。                           | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 免费 Google 搜索。                             |
| [reading-plus-ai/mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research) | 提供类 OpenAI/Perplexity 自主深度研究、结构化查询细化和简洁报告的 MCP 服务器。              | 社区实现, TypeScript 开发 📇, 云服务 ☁️, 自主深度研究。                                    |
| [SecretiveShell/MCP-searxng](https://github.com/SecretiveShell/MCP-searxng) | 连接到 searXNG 实例的 MCP 服务器 (社区实现版本)。                                         | 社区实现, Python 开发 🐍, 本地运行 🏠, SearXNG 元搜索 (Python)。                          |
| [takashiishida/arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp) | 获取 arXiv 论文的 LaTeX 源码，以处理数学内容和公式。                                   | 社区实现, Python 开发 🐍, 云服务 ☁️, arXiv LaTeX 源码获取。                                |
| [the0807/GeekNews-MCP-Server](https://github.com/the0807/GeekNews-MCP-Server) | 检索和处理来自 GeekNews 网站新闻数据的 MCP 服务器。                                      | 社区实现, Python 开发 🐍, 云服务 ☁️, GeekNews 新闻获取。                                  |
| [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) | Tavily AI 搜索 API (社区实现版本)。                                                    | 社区实现, Python 开发 🐍, 云服务 ☁️, Tavily 搜索 (社区 Py 版)。                            |
| [zhsama/duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mpc-server) | 提供 DuckDuckGo 搜索功能的基于 TypeScript 的 MCP 服务器。                               | 社区实现, TypeScript 开发 📇, 本地/云端 🏠☁️, DuckDuckGo 搜索 (TypeScript)。             |
| [mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)           | 本地运行的 RAG 式网页搜索，使用 MediaPipe Embedder 和 DuckDuckGo。                               | 社区实现, Python 开发, 本地 RAG 搜索 (无需 API Key)。                                        |
| [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)           | 提取抖音无水印视频链接，视频文案，douyin-mcp-server  | 社区实现, Python 开发, API 默认使用 [SiliconFlow API](https://cloud.siliconflow.cn/i/TxUlXG3u)                              |
| [Aas-ee/open-webSearch](https://github.com/Aas-ee/open-webSearch)           | 一个基于多引擎搜索结果的模型上下文协议(MCP)服务器，支持免费网络搜索，无需API密钥。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 云服务 ☁️ , 支持 Bing, Baidu, DuckDuckGo, Brave, Exa, Github, and CSDN.                            |
| [Multi-Source Media MCP Server (M3S)](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server) | 多源媒体聚合与生成，统一访问 Unsplash/Pexels、Web 爬取媒体，支持多后端 AI 图像生成以及全网图片爬虫。 | 原生 Go ✨，本地运行 🏠，支持多平台媒体 API 和 AI 图像生成、爬虫扩展。 |
| [MLT-OSS/FirstData](https://github.com/MLT-OSS/FirstData) | 全球最全面的权威数据源知识库，132+ 经验证数据源（政府、国际组织、学术机构），帮助 AI 减少幻觉。提供结构化元数据、100% URL 验证、中英双语支持。目标：1000+ 数据源。 | 本地/云端 🏠☁️，中国数据源深度覆盖 🇨🇳，AI 事实防线，抗幻觉数据底座。 |
| [GEOScore](https://github.com/henu-wang/geoscore-mcp) | AI 搜索优化（GEO）MCP 服务器。扫描网站的 AI 搜索就绪度，生成 llms.txt、Schema.org 修复、meta 标签优化。 | 社区实现, TypeScript 开发 📇, 本地运行 🏠, 支持 Claude/Cursor/Windsurf。 |
| [Episkey-G/GrokSearch-rs](https://github.com/Episkey-G/GrokSearch-rs) | Rust 编写的 MCP 服务器，提供 Grok 联网搜索与 Tavily 支持的来源检索，为 AI 代理补充实时网络信息。 | 社区实现, Rust 开发 🦀, 云服务 ☁️, Grok 联网搜索 + Tavily 检�