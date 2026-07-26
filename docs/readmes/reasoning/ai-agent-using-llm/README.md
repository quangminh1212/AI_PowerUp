<!-- source: https://github.com/Huzaifa-Ahmed010/AI-Agent-using-LLM.git sha: 2e21d83ec8b8eb11d47617a8a6344cf707249d13 readme: main/README.md -->
# Huzaifa-Ahmed010/AI-Agent-using-LLM

🤖 AI Agent powered by Gemini 2.5 Flash that uses chain-of-thought reasoning to solve queries step by step — with built-in tools for live weather lookup and Linux command execution.

---

# 🤖 AI Agent with Chain-of-Thought Reasoning

A Python-based AI agent powered by **Gemini 2.5 Flash** (via OpenAI-compatible API) that uses structured **chain-of-thought reasoning** to solve user queries step by step — with support for real-time tool execution.

---

## 🧠 How It Works

The agent follows a structured reasoning loop with four steps:

| Step | Emoji | Description |
|------|-------|-------------|
| `START` | 🔥 | User provides a query |
| `PLAN` | 🧠 | Agent breaks the problem into logical steps |
| `TOOL` | 🔧 | Agent calls an external tool if needed |
| `OUTPUT` | 🤖 | Final response delivered to the user |

The agent keeps reasoning in a loop (PLAN → TOOL → PLAN → ...) until it's confident enough to produce a final `OUTPUT`.

---

## 🛠️ Available Tools

### `get_weather(city: str)`
Fetches live weather data for any city using [wttr.in](https://wttr.in).

**Example:**
```
User: What's the weather in Mumbai?
→ get_weather("mumbai")
→ "The weather in Mumbai is Partly cloudy +31°C"
```

### `run_command(cmd: str)`
Executes any Linux shell command on the host system and returns the output.

**Example:**
```
User: How much disk space is available?
→ run_command("df -h")
→ Shows disk usage output
```

> ⚠️ **Security Warning:** `run_command` executes real system commands. Use with caution and never expose this agent to untrusted inputs in production.

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies
```bash
pip install openai python-dotenv pydantic requests
```

### 3. Set up environment variables
Create a `.env` file in the root directory:
```env
# Add any environment variables here if needed
```

> The API key is currently hardcoded in the script. For production use, move it to `.env` and load it with `os.getenv("API_KEY")`.

---

## 🚀 Usage

Run the agent:
```bash
python agent.py
```

Then type your query at the `👉` prompt:

```
👉 What is the weather in Delhi?
🧠 User is asking for weather information about Delhi
🧠 I have the get_weather tool available for this query
tool: get_weather (delhi) = The weather in Delhi is Haze +38°C
🧠 I received the weather info. Now I'll provide the output
🤖 The current weather in Delhi is hazy with a temperature of 38°C.
```

---

## 🗂️ Project Structure

```
├── agent.py          # Main agent script
├── .env              # Environment variables (not committed)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## ⚙️ Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| Model | `gemini-2.5-flash` | LLM used for reasoning |
| Base URL | Google Generative Language API | OpenAI-compatible endpoint |
| Output Format | Pydantic `MyoutputFormat` | Structured JSON responses |
| Max History | Unlimited (full conversation) | All turns sent each request |

---

## 🧩 Adding New Tools

1. Define a Python function:
```python
def my_tool(input: str) -> str:
    # your logic here
    return result
```

2. Register it in `available_tools`:
```python
available_tools = {
    "get_weather": get_weather,
    "run_command": run_command,
    "my_tool": my_tool,     # ← add here
}
```

3. Document it in the `SYSTEM_PROMPT` under `Available Tools`.

---

## 📋 Requirements

- Python 3.8+
- Internet access (for weather tool and Gemini API)
- Linux/macOS (for `run_command` tool)

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [Google Gemini](https://deepmind.google/technologies/gemini/) for the LLM
- [wttr.in](https://wttr.in) for the weather API
- [Pydantic](https://docs.pydantic.dev/) for structured output parsing
