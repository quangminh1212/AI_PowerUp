<!-- source: https://github.com/mahekaggarwal17/Azure-Open-AI.git sha: 425408427a2a8d62a48fc1dba0b537fd00358460 readme: main/README.md -->
# mahekaggarwal17/Azure-Open-AI

Azure AI Foundry project (Advanced prompt engineering, chain-of-thought reasoning, scoped FAQ chatbot deployment)

---

# Company FAQ Bot - Azure OpenAI Playground & Deployment Dashboard

A modern, high-fidelity single-page React web application designed for prompt engineering and scoped FAQ chatbot deployment. This workspace connects directly to your Azure OpenAI resource, allowing you to edit system prompt templates, manage the FAQ knowledge base dynamically, simulate builds, and test your chatbot in an interactive playground.

---

## 🎨 Key Features

### 🔐 Enforced Deployment Lifecycle
- **Deployment-Locked Playgrounds**: Interactive chat is strictly disabled and greyed out until the chatbot is successfully deployed to simulate production security.
- **Enterprise Build Simulation**: Running a deployment initiates a simulated enterprise build pipeline, printing status logs to a monospaced terminal window.
- **Verification Gates**: Prevents deployment if Azure OpenAI credentials (API Key, Endpoint, or Deployment Name) are missing, displaying alert banners.

### 🌐 Dynamic Configurations & Environment Selection
- **Multi-Environment Support**: Choose between **Development**, **Testing**, and **Production** environments before triggering deployments.
- **Deployment Details**: Displays comprehensive post-deployment data:
  - **Deployment Time**: A formatted timestamp captured at completion (e.g. `08 Jul 2026 02:18 AM`).
  - **Authentic Subdomain-Based Endpoint**: Automatically parses the subdomain of your Azure URL to display the authentic API endpoint (e.g., `https://faqbot.azure-api.net/chat`).
  - **Model Hyperparameters**: Shows model deployment names alongside deterministic prompt engineering settings (Temperature: `0.0`, Max Tokens: `1000`).

### 📊 Dynamic FAQ Knowledge Base & System Prompts
- **Interactive FAQ Editor Table**: Add, modify, or delete FAQ rows (categories, questions, answers) dynamically to update the context injected into your LLM prompt.
- **System Prompt Settings**: Edit the prompt template in real-time. The application dynamically compiles the prompt by replacing `{faq_context}` with formatted FAQ rows before making API calls.

### 🚥 Live Status indicators
- **Dual Sidebar Badges**: Monitor both API Connection status (`API Connected` / `Credentials Missing`) and Deployment status (`Deployment Active` / `Deployment Pending`) at a glance.
- **Header Badges**: Active deployments illuminate green status pills: `Connected`, `Deployment Active`, and `[Model Name] Ready`.
- **Live Latency Ping**: Simulates real-time Azure endpoint roundtrip latency.

---

## ⚙️ Running Locally

### 1. Prerequisites
- **Node.js 18.0+**
- **npm** (comes with Node.js)

### 2. Environment Variables
Add your Azure OpenAI credentials in a `.env` file at the root of the project:
```env
VITE_AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
VITE_AZURE_OPENAI_KEY=your-api-key
VITE_AZURE_OPENAI_DEPLOYMENT=your-deployment-name
VITE_AZURE_OPENAI_API_VERSION=2024-12-01-preview
```

### 3. Setup & Start
Install dependencies and launch the local development server:
```bash
# Install dependencies
npm install

# Start the Vite local server
npm run dev
```
Open your browser and navigate to `http://localhost:5173`.

---

## 🛠️ Project Structure
```text
├── index.html                   # HTML template wrapper
├── package.json                 # Node package definitions & build scripts
├── vite.config.js               # Vite configurations
├── .env                         # Local environment credentials (git-ignored)
├── src/
│   ├── main.jsx                 # React entry point
│   ├── index.css                # Base theme variables, resets, and typography
│   ├── App.jsx                  # Main dashboard component, state, and API routing
│   └── App.css                  # UI design layouts, terminal styles, and animations
└── system_prompts/              # Raw prompt templates for Azure AI Foundry reference
```
