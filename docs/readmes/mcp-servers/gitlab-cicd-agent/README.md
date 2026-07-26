<!-- source: https://github.com/shalwin04/GitLab-CICD-Agent.git sha: 808c5bcf800a8e07eb1c8e91d3e628e9f7dccfd8 readme: main/README.md -->
# shalwin04/GitLab-CICD-Agent

agentic-cicd is an AI-powered multi-agent system that automates GitLab CI/CD workflows using natural language. Built with LangGraphJS, it connects to GitLab via OAuth, interprets user intent, generates pipelines, and executes deployments — all orchestrated by autonomous AI agents and backed by a GitLab MCP server.

---

# 🚀 agentic-cicd: Automate GitLab CI/CD with Natural Language + AI

> “Automate your GitLab CI/CD workflows using natural language — powered by AI and Google Cloud.”

---

## ✨ Overview

**`agentic-cicd`** is an intelligent DevOps agent that allows users to automate complex GitLab CI/CD workflows simply by describing what they want in natural language.

It bridges **natural language commands** and **real infrastructure changes** by using an AI-driven **multi-agent system** that understands, generates, pushes, and monitors CI/CD pipelines on **GitLab**.

Whether you're a developer looking to set up a CI/CD pipeline or an ops engineer handling deployments — this tool simplifies GitLab automation through **LLMs + agents + MCP tool servers.**

---

## 📟️ Demo

[Live Application](https://git-lab-cicd-agent.vercel.app/)
[youtube demo](https://www.youtube.com/watch?v=lCwZ1eVZkLg)

---

## 🧠 Key Features

* 🔐 **GitLab OAuth Integration** – Connect your GitLab account securely.

* 💬 **Natural Language Input** – Describe what you want, like:

  ```
  Set up CI to run tests on push and deploy to GKE when main branch is updated.
  ```

* 🤖 **Multi-Agent AI Engine** – Understands the request and plans accordingly.

* ⚙️ **Pipeline & Infra Generation** – Generates `.gitlab-ci.yml`, Dockerfile, Terraform, Helm config, etc.

* ↻ **Push + Merge Request** – Pushes the generated files to your GitLab repo and opens an MR.

* 🔍 **Pipeline Monitoring** – Optionally track status of the build, test, and deployment stages.

* 🧹 **MCP Server/Client Architecture** – Modular tool abstraction to interface with GitLab API via agents.

---

## 🧹 Architecture

### ↻ System Flow
![image](https://github.com/user-attachments/assets/a237bd7d-019a-47f9-bf80-2d3720853cf4)

---
## 🧠 Multi-Agent Architecture – LangGraphJS Supervisor Pattern

This project follows the [LangGraphJS Multi-Agent Supervisor Pattern](https://js.langgraph.dev/guides/multi-agent/) to automate GitLab CI/CD workflows using natural language commands.

---

### 🧑‍⚖️ 1. **Supervisor Agent**

- The central decision-maker.
- Receives **natural language input** from the user.
- Maintains **shared memory** and execution state across agents.
- Dynamically delegates to sub-agents using a **graph-based control flow**.

---

### 🔄 Agent Workflow Graph

The Supervisor uses LangGraph to define a **directed graph of agents**, where edges represent conditional flows based on task results.

---

### 🤖 Sub-Agents

Each agent handles a distinct responsibility within the pipeline.

---

### 🧭 `PlanAgent`

> _“Understand what needs to be done.”_

- Parses user intent and decomposes it into logical subtasks.
- Understands GitLab CI/CD terminology and translates user commands accordingly.
- Outputs a plan with goals such as:
  - Generate `.gitlab-ci.yml`
  - Create `Dockerfile`
  - Define cloud deployment strategy (e.g., GKE)

---

### 🧑‍💻 `CodeAgent`

> _“Write the code/configuration needed.”_

- Converts the structured plan into CI/CD artifacts such as:
  - `.gitlab-ci.yml`
  - `Dockerfile`
  - `Terraform` / `Helm` configurations
- Adapts generation based on selected cloud providers (GCP, AWS, etc.)
- Can scaffold standard GitLab CI templates dynamically.

---

### 🧪 `TestAgent`

> _“Validate the configuration before use.”_

- Runs tests on generated configuration to ensure correctness.
- Performs:
  - YAML linting / CI syntax validation
  - Dry-run of GitLab CI if applicable
  - Optional LLM-assisted analysis of pipeline logic

---

### 💬 `ChatAgent`

> _“Explain what’s happening or answer user queries.”_

- Maintains conversation with the user.
- Can answer questions like:
  - "What is this pipeline doing?"
  - "Why did my build fail?"
- Pushes updates about:
  - MR creation
  - Pipeline execution
  - Deployment status
- Can re-prompt for missing details if required

---

## 🔧 GitLab MCP Tool Server (Tool Use via API)

Agents like `CodeAgent` and `ChatAgent` interact with GitLab via a **dedicated Tool Server** (GitLab MCP Server).

### 🛠 MCP GitLab Tool Server

- A REST API wrapper around GitLab’s official APIs.
- Allows fine-grained agent control over GitLab actions like:
  - Getting project info
  - Creating branches/commits
  - Listing and triggering pipelines
  - Monitoring job statuses
  - Opening Merge Requests

---

### 🤝 MCP Client

- Each agent uses an **MCP Client** to communicate with the Tool Server.
- Benefits:
  - Keeps logic clean and separated from direct API calls.
  - Enables observability, tracing, and debugging of agent decisions.
  - Makes actions reversible and replicable.

---

## 🔄 Feedback Loop

1. **User Input**  
   > “Set up CI to run tests on push and deploy to GKE when main is updated.”

2. **Supervisor Flow**
   - `PlanAgent` → Understands the request and breaks into subgoals.
   - `CodeAgent` → Generates `.gitlab-ci.yml`, `Dockerfile`, etc.
   - `TestAgent` → Validates the generated files.
   - `GitLab MCP Server` → Applies the changes via GitLab API (opens MR).
   - `ChatAgent` → Informs the user and monitors progress.

3. **Pipeline Execution**
   - GitLab CI is triggered.
   - Status is periodically updated to the user.

---

## ✅ Why LangGraphJS?

- **Structured Reasoning**  
  Flow is modeled as a directed graph for better traceability and control.

- **Shared Memory Across Agents**  
  All agents work with a centralized state context.

- **Retries and Fallbacks**  
  Automatically retry failed tasks or re-ask user when needed.

- **Plug-and-Play Agents**  
  Each agent is modular, testable, and can be extended independently.

---

> ✨ The result is a natural-language-driven GitLab CI/CD automation system powered by intelligent agents, tailored infrastructure, and real-time feedback – all orchestrated via LangGraph.


### 🔐 Authorization:

* Uses the user’s OAuth token to act on their behalf.
* Each API call is scoped by the GitLab OAuth access token.

---

## 💽 Tech Stack

| Layer       | Tech                                 |
| ----------- | ------------------------------------ |
| Frontend    | React, React Router, Vite, Tailwind  |
| Backend     | Node.js, Express, Supabase           |
| AI Agents   | LangGraphJS, LangChainJS, Gemini/GPT |
| Auth        | GitLab OAuth 2.0                     |
| Infra Tools | Docker, Terraform, Helm (generated)  |
| Hosting     | Vercel (frontend), Render (backend)  |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/agentic-cicd.git
cd agentic-cicd
```

---

### 2. Frontend Setup

```bash
cd frontend
npm install
```

Create a `.env` file:

```env
VITE_BACKEND_URL=https://your-backend-url.onrender.com
VITE_GITLAB_CLIENT_ID=your_gitlab_client_id
VITE_REDIRECT_URI=https://your-frontend-url.vercel.app/oauth/callback
```

```bash
npm run dev
```

---

### 3. Backend Setup

```bash
cd backend
npm install
```

`.env` file:

```env
GITLAB_CLIENT_ID=your_gitlab_client_id
GITLAB_CLIENT_SECRET=your_gitlab_client_secret
GITLAB_REDIRECT_URI=https://your-frontend-url.vercel.app/oauth/callback

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

GOOGLE_API_KEY=your_gemini_api_key
TAVUS_API_KEY=your_tavus_key
```

Build and Run:

```bash
npm run build
npm run start
```

---

## 🧪 Usage

1. Go to the app homepage.

2. Click "Connect GitLab" and authorize access.

3. Enter your command like:

   ```
   Set up CI to run tests on push and deploy to GKE when main branch is updated.
   ```

4. Agent will:

   * Understand your intent
   * Generate `.gitlab-ci.yml` and Dockerfile
   * Push to a new branch
   * Open a merge request
   * Trigger a pipeline

5. Watch pipeline logs via GitLab or frontend.

---

## ☁️ Deployment Guide

### Frontend (Vercel)

1. Link GitHub Repo → Vercel Dashboard
2. Set environment variables in Settings
3. Deploy

### Backend (Render)

1. Create new Web Service → Connect to GitHub
2. Build Command: `npm run build`
3. Start Command: `node dist/index.js`
4. Add your environment variables

---

## ❗ Troubleshooting

| Issue                | Fix                                                       |
| -------------------- | --------------------------------------------------------- |
| `CORS error`         | Ensure backend sets correct `Access-Control-Allow-Origin` |
| `OAuth redirect 404` | Check GitLab app redirect URI matches deployed frontend   |
| `Failed to fetch`    | Backend must be live + CORS enabled                       |
| `503 MCP Init`       | GitLab token expired or MCP endpoint down                 |
| `CI config invalid`  | Re-run or correct command syntax                          |

---

## 🤝 Contributing

We welcome PRs and ideas!

```bash
# Fork -> Clone -> Create Branch -> Code -> Commit -> PR
```

Please open issues for:

* Bugs
* New agent tasks
* GitLab features you'd like automated

---

## 📄 License

MIT License © 2025 MemeVerse CICD Dev Team

---

## 💡 Inspired By

* [LangGraph](https://www.langgraph.dev/)
* [LangChainJS](https://js.langchain.com/)
* [GitLab API](https://docs.gitlab.com/ee/api/)
* [MCP](https://modelcontextprotocol.io/introduction)
* [Google Gemini](https://ai.google.dev/)

---

## 🗂️ Folder Structure (Simplified)

```
agentic-cicd/
│
├── frontend/
│   ├── App.jsx
│   ├── pages/
│   └── components/
│
├── backend/
│   ├── agents/
│   ├── routes/
│   |── services/
|-─ mcp-server/
│
├── .env.example
└── README.md
```

---

## 📬 Contact

For inquiries or collaborations:
📧 **[shalwinsanju.25cs@licet.ac.in](mailto:shalwinsanju.25cs@licet.ac.in)**
🐦 Twitter: [@samshalwin](https://twitter.com/samshalwin)

---
