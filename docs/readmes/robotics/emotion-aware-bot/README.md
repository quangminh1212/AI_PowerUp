<!-- source: https://github.com/ShivamGami/Emotion-Aware-bot.git sha: 8bcff877b6c20d1dc22d69a70d7f80ba46dfc311 readme: main/README.md -->
# ShivamGami/Emotion-Aware-bot

AI/RL-powered conversational robotic twin system utilizing computer vision for facial emotion detection, ROS2 communication, and real-time animation control in Unreal Engine.

---

# 🤖 EmoBot — Emotion-Aware Conversational Robot System

<div align="center">

![EmoBot Banner](https://img.shields.io/badge/EmoBot-Emotion--Aware%20Digital%20Twin-blueviolet?style=for-the-badge&logo=unrealengine)

**A real-time, multi-agent system that bridges human facial emotions with an empathetic Unreal Engine 5 MetaHuman.**

[![React](https://img.shields.io/badge/React-TypeScript-61DAFB?style=flat-square&logo=react)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Python%203.13-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![ROS2](https://img.shields.io/badge/ROS2-Humble-22314E?style=flat-square&logo=ros)](https://docs.ros.org/en/humble/)
[![Unreal Engine](https://img.shields.io/badge/Unreal%20Engine-5-0E1128?style=flat-square&logo=unrealengine)](https://www.unrealengine.com/)
[![WSL2](https://img.shields.io/badge/WSL2-Ubuntu%2022.04-E95420?style=flat-square&logo=ubuntu)](https://ubuntu.com/wsl)

</div>

---

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [System Architecture](#-system-architecture--flow)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Port Configuration](#-port-configurations)
- [Installation](#️-step-by-step-installation)
- [Running the System](#-how-to-run--operate-the-system)
- [Team](#-team)

---

## 💡 About the Project

Modern conversational AI often lacks situational context and emotional empathy. **EmoBot** builds a real-time reactive bridge between a user's physical emotional expressions (captured via webcam) and a digital twin's responses.

When a user looks **angry**, **sad**, or **happy** — the digital twin detects this transition, adapts its internal state, and responds with context-appropriate speech, creating a highly realistic human-to-digital-twin conversational loop.

### ✨ What We Built

| Layer | What It Does |
|---|---|
| 🎥 **Facial Expression Detector** | Camera-based real-time emotion classification on a React web client |
| 🧠 **Orchestration Backend** | Manages state, filters idle inputs, and coordinates message dispatches |
| 🔗 **WSL2-to-Windows Bridge** | Cross-environment communication using ROS2 message passing |
| 🎮 **Unreal Engine Integration** | Dynamic file polling that drives voice lip-sync and animations on a MetaHuman |

---

## ⚙️ System Architecture & Flow

```
+--------------------+       +----------------------+       +-------------------------+
|                    |       |                      |       |                         |
|   React Frontend   |       |   FastAPI Backend    |       |   ROS2 Bridge Node      |
|   (Webcam / FER)   | ----> |   (AI/RL Logic)      | ----> |   (ROS2 Topic /speech)  |
|   Port: 5173       |       |   Port: 8001         |       |   Port: 8000 (WSL)      |
|                    |       |                      |       |                         |
+--------------------+       +----------------------+       +-------------------------+
                                                                         |
                                                                         v
                                                            +-------------------------+
                                                            |                         |
                                                            |   Unreal Engine 5       |
                                                            |   (MetaHuman/ConvAI)    |
                                                            |   input.json polling    |
                                                            |                         |
                                                            +-------------------------+
```

### 🔄 End-to-End Flow

1. **Frontend (React + Vite)** — Captures webcam video and classifies emotions in real time using the `fer` deep learning library.
2. **Backend (FastAPI)** — Filters out `neutral` states, enforces a **20-second cooldown** to prevent spamming, and dispatches background tasks to ROS2 publishers inside WSL.
3. **ROS2 Bridge Node (`bridge.py`)** — Runs in WSL2 (ROS2 Humble). Subscribes to `/speech`, extracts conversational commands, and writes them to a shared `input.json` on the Windows filesystem.
4. **Unreal Engine 5** — Polls `input.json` via a timer, triggers MetaHuman voice responses using **ConvAI**, and animates lips and gestures dynamically.

---

## 🛠 Tech Stack

| Category | Technology |
|---|---|
| **Frontend** | React, TypeScript, Vite, FER (Facial Emotion Recognition) |
| **Backend** | FastAPI, Python 3.13, OpenAI, Google Gemini, LangChain, ChromaDB |
| **Robotics Middleware** | ROS2 Humble (WSL2 / Ubuntu 22.04) |
| **3D Engine** | Unreal Engine 5, MetaHuman, ConvAI, VaRest |
| **ML / AI** | TF-Keras, sentence-transformers, MediaPipe, Librosa |
| **Platform** | Windows 11, WSL2 |

---

## 📂 Project Structure

```
.
├── backend/                    # FastAPI backend server
│   ├── api/                    # API endpoints & ROS2 commands dispatcher
│   │   ├── ros_publisher.py    # Spawns interactive WSL shells to publish ROS2 messages
│   │   └── routes_emotion.py   # Cooldown filter & dispatch router
│   ├── emotion_detection/      # Face detection and emotion classification
│   │   └── face_emotion.py     # Webcam FER image processor
│   ├── main.py                 # FastAPI backend entrypoint (port 8001)
│   └── README.md               # Backend installation details
│
├── frontend/                   # React (TypeScript) + Vite user interface
│   ├── src/                    # App, components, and API client configs
│   │   └── config.ts           # Endpoint configs (points to port 8001)
│   └── README.md               # Frontend installation details
│
├── unreal/                     # Unreal Engine 5 digital twin documentation
│   ├── blueprints/             # Copy-pasteable blueprint graphs
│   │   └── json_watcher_nodes.txt  # Event Graph text for BP_Natalia
│   └── README.md               # Required plugins and blueprint details
│
├── bridge.py                   # WSL ROS2 subscriber -> Windows input.json bridge (port 8000)
├── .gitattributes              # Git LFS rules for large binary tracking
├── .gitignore                  # Build cache and virtual environment ignore files
└── README.md                   # Main project setup and runner guide (this file)
```

---

## 🔌 Port Configurations

| Service | Technology | Port | Runs On |
|---|---|---|---|
| **Frontend UI** | React / Vite | `5173` | Windows |
| **Backend API** | FastAPI / Python 3.13 | `8001` | Windows |
| **WSL ROS2 Bridge** | FastAPI / ROS2 Humble | `8000` | WSL2 (Ubuntu 22.04) |

---

## 🛠️ Step-by-Step Installation

### Prerequisites

Ensure the following are installed on your host system before proceeding:

- ✅ **Windows 11 / 10**
- ✅ **Node.js** (v18 or higher)
- ✅ **Python 3.13** (Windows environment)
- ✅ **WSL 2** with **Ubuntu-22.04**
- ✅ **ROS2 Humble** (installed inside the WSL Ubuntu distro)
- ✅ **Unreal Engine 5** (with **VaRest** and **ConvAI** plugins)

---

### 1. Backend Setup (Windows)

```cmd
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install uvicorn fastapi tf-keras sentence-transformers chromadb fer mediapipe openai google-genai langchain langchain-community librosa
```

Create a `.env` file inside `backend/`:

```env
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

---

### 2. Frontend Setup (Windows)

```cmd
cd frontend
npm install
```

---

### 3. ROS2 Bridge Setup (WSL Ubuntu)

```cmd
wsl -d Ubuntu-22.04
```

```bash
pip3 install fastapi uvicorn
```

---

## 🚀 How to Run & Operate the System

Start all services **in order** for a successful end-to-end run.

### Step 1 — Start the ROS2 Bridge (WSL Terminal)

```bash
wsl -d Ubuntu-22.04
source /opt/ros/humble/setup.bash
python3 bridge.py
```

> The bridge starts an HTTP server on port `8000` and subscribes to the `/speech` ROS2 topic.

---

### Step 2 — Start the Backend (Windows)

```cmd
cd backend
.venv\Scripts\activate
python -m uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

---

### Step 3 — Start the Frontend (Windows)

```cmd
cd frontend
npm run dev
```

Open `http://localhost:5173` in your browser and **grant webcam permissions**.

---

### Step 4 — Play the Unreal Engine Scene

1. Open your Unreal Engine project (configured with **BP_Natalia**).
2. Ensure the Natalia Character Blueprint includes the Event Graph logic parsing the JSON file from:
   `D:/Unreal_Projects/Final_V2/input.json`
   *(Refer to [unreal/README.md](unreal/README.md) to copy-paste the blueprint graph nodes).*
3. Press **Play** in the Unreal Editor.

---

### Step 5 — Verify End-to-End Operation

1. **Smile or look sad** at your webcam in the React frontend.
2. The frontend detects the emotion and sends it to the Windows backend.
3. The backend executes a WSL background command:
   ```bash
   wsl -d Ubuntu-22.04 -- bash -i -c "source /opt/ros/humble/setup.bash && ros2 topic pub -1 /speech std_msgs/msg/String \"{data: 'speaking:I am angry, very angry, absolutely furious'}\""
   ```
4. The bridge picks up the `/speech` message and writes to `D:/Unreal_Projects/Final_V2/input.json`.
5. The Unreal Engine character detects the file change, plays **lip-sync voice dialogue** via ConvAI, and animates! 🎉

---

## 💾 Versioning the Unreal Engine Project

This repository versions **blueprints and config settings** without the heavy 1.5 GB binary assets.

- See [unreal/README.md](unreal/README.md) for Git LFS setup and level configurations.
- See [unreal/blueprints/json_watcher_nodes.txt](unreal/blueprints/json_watcher_nodes.txt) for copy-pasteable blueprint graphs.

---

