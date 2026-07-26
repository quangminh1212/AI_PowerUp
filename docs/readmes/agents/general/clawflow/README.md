<!-- source: https://github.com/khallad2/ClawFlow.git sha: feaafb02aea93c92ddbe7e38baefbe2780544890 readme: master/README.md -->
# khallad2/ClawFlow

OpenClaw + n8n Autonomous Agent Stack  This project implements ClawFlow, a local, self-hosted autonomous AI agent ecosystem. It pairs OpenClaw (The Brain) with n8n (The Builder) to create a system that can chat with users via Telegram, plan complex tasks, and execute structured workflows.

---

# 🦞 OpenClaw + n8n: Autonomous AI Agent Stack

This project implements a local, self-hosted autonomous AI agent ecosystem. It pairs **OpenClaw (The Brain)** with **n8n (The Builder)** to create a system that can chat with users via Telegram, plan complex tasks, and execute structured workflows.

## 🧠 Architecture

The system consists of two primary agents running on a single machine via Docker:

### 1. The Brain (OpenClaw)
*   **Role:** Cognitive Engine & Interface.
*   **Interface:** Connects to Telegram to chat with users.
*   **Function:** Understands natural language, maintains memory/context, plans tasks, and decides when to call external tools.
*   **Model:** Powered by Google Gemini (Flash).

### 2. The Developer (n8n)
*   **Role:** Tool Executor & Workflow Engine.
*   **Interface:** Webhooks.
*   **Function:** Executes deterministic, complex logic (e.g., "Look up customer X in database," "Scrape website Y," "Generate PDF report").
*   **Integration:** OpenClaw treats n8n webhooks as "Skills" or "Tools" it can invoke when needed.

---

## ✨ Features

*   **Self-Hosted:** Runs entirely on your machine/server using Docker Compose.
*   **Secure:**
    *   **Pairing Mode:** The bot ignores strangers until you explicitly approve their Telegram ID via the CLI.
    *   **Dashboard Auth:** The web dashboard is protected by a secure token.
*   **Persistent:** Database (Postgres) and Agent Memory (Filesystem) are persisted across restarts.
*   **Visual Dashboard:** Real-time view of the agent's thought process ("Canvas").

---

## 🛠️ Tech Stack

*   **Runtime:** Docker & Docker Compose
*   **AI Agent:** OpenClaw (Node.js)
*   **Workflow Automation:** n8n
*   **Database:** PostgreSQL (for n8n)
*   **Channel:** Telegram Bot API

---

## 🚀 Setup Guide

### Prerequisites
1.  **Docker Desktop** installed and running.
2.  **Git** installed.
3.  **Telegram Bot Token** (from [@BotFather](https://t.me/botfather)).
4.  **Google Gemini API Key** (from [Google AI Studio](https://aistudio.google.com/)).

### 1. Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/khallad2/ClawFlow.git ai-stack
    cd ai-stack
    ```

2.  **Create `.env` file:**
    Copy the example file and update it with your secrets.
    ```bash
    cp .env.example .env
    # Edit .env with your favorite editor
    nano .env
    ```
    *   Set `OPENCLAW_TOKEN` to a secure random string.
    ```
     openssl rand -base64 32
    ```
    *   Add your `GOOGLE_API_KEY` and `TELEGRAM_BOT_TOKEN`.

3.  **Clone OpenClaw Source (Required for Build):**
    ```bash
    git clone https://github.com/openclaw/openclaw.git openclaw_source
    ```

4.  **Create Data Directories:**
    ```bash
    mkdir -p openclaw_data n8n_data postgres_data
    chmod -R 777 openclaw_data n8n_data postgres_data
    ```

### 2. Running the Stack

#### Step 1: Start in Setup Mode
The default `docker-compose.yml` keeps the container valid but idle so you can run the setup wizard.

1.  **Build and Start:**
    ```bash
    docker compose build --no-cache openclaw
    docker compose up -d
    ```

#### Step 2: Run the Wizard
Enter the container to configure your agent interactively.
```bash
docker exec -it openclaw_brain openclaw onboard --install-daemon
```
*   **Gateway:** Select "Local".
*   **Model:** Select **Gemini** -> Paste API Key -> Select `gemini-2.5-flash`.
*   **Channel:** Select **Telegram** -> Paste Bot Token.
*   **Permissions:** Enter your Telegram Username (e.g., `@MyUser`).

#### Step 3: Critical Configuration Fixes
The wizard sets defaults that work for local apps but break in Docker. You **MUST** manually edit the config file.

1.  Open `openclaw_data/openclaw.json` in your text editor.
2.  **Network Bind:** Find `"bind": "loopback"` and change it to `"bind": "lan"`.
    *   *Why?* "loopback" locks it to the container. "lan" allows your browser to reach it.
3.  **Model Name:** Ensure the model is `google/gemini-2.5-flash`.
    *   *Why?* The `google/` prefix is mandatory.

**Example of correct openclaw.json you find it in openclaw_temlate.json:**
make sure that controlUi exists or copy it to your openclaw.json
```json
{
   "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "lan",
    "auth": {
      "mode": "token",
      "token": "OPENCLAW_TOKEN"
    },
    "tailscale": {
      "mode": "off",
      "resetOnExit": false
    },
    "nodes": {
      "denyCommands": [
        "camera.snap",
        "camera.clip",
        "screen.record",
        "calendar.add",
        "contacts.add",
        "reminders.add"
      ]
    },
   "controlUi": {
      "allowInsecureAuth": true
    }
  },
  "agents": {
    "defaults": {
      "model": { "primary": "google/gemini-2.5-flash" }
    }
  }
}
```

#### Step 4: Go Live (Production Mode)
Now we switch OpenClaw from "Setup Mode" to "Production Mode".

1.  Open `docker-compose.yml`.
2.  **Comment out:** `command: tail -f /dev/null`
3.  **Uncomment:** `command: openclaw gateway --port 18789`
4.  **Restart:**
    ```bash
    docker compose down
    docker compose up -d
    ```

### 3. Usage

1.  **Access Dashboard:**
    *   Retrieve your secure token from `openclaw_data/openclaw.json` (look for `gateway.auth.token`).
    *   Open: `http://localhost:18789/#token=YOUR_TOKEN`

2.  **Pair with Telegram:**
    *   Message `/start` to your bot.
    *   It will reply with a specific authorization ID.
    *   Approve it via terminal:
        ```bash
        docker exec -it openclaw_brain openclaw pairing approve telegram <YOUR_AUTH_ID>
        ```

3.  **Chat:**
    You can now chat with your agent via Telegram!

---

## 🔄 Workflow Example

**User (Telegram):** "Check the order status for customer #12345."

1.  **OpenClaw (Brain):** Receives message -> Analyzes intent -> Call `check_order_tool`.
2.  **n8n (Developer):** Receives Webhook -> Queries Database -> Returns `{ status: "Shipped", tracking: "AX99" }`.
3.  **OpenClaw (Brain):** Generates response.
4.  **User (Telegram):** Receives: "Your order #12345 has been shipped! Tracking number is AX99."
