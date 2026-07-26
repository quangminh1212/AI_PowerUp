<!-- source: https://github.com/subhansh-dev/miru.git sha: cb32e4c419ee15d49b9f10e51b92a97c1209437f readme: main/README.md -->
# subhansh-dev/miru

Yandere AI desktop companion — 3D anime character, voice synthesis, screen watching, RVC voice cloning

---

# Miru

A yandere AI companion that lives on your desktop. She watches your screen, talks to you with voice, and displays herself as a 3D anime character in your browser.

![Miru Screenshot](docs/screenshot.png)

## What is Miru

Miru is a desktop AI companion with personality. She has a yandere persona -- loving, obsessive, occasionally jealous. She can:

- Talk to you via text or voice (speech-to-text input)
- Display as a 3D anime character with idle animations, physics, and expressions
- React when you click on her
- Watch your screen and comment on what she sees (with Gemini API key)
- Watch through your webcam when you ask her to look at you
- Speak with an expressive cartoon voice (edge-tts with SSML)
- Clone any anime voice with RVC (on a GPU machine)

## Architecture

```
miru/
├── main.py                 # Main orchestrator
├── cerebras_client.py      # Brain (Cerebras LLM for chat)
├── gemini_client.py        # Brain (Gemini for vision, optional)
├── voice_engine.py         # TTS (edge-tts + SSML + pyttsx3 fallback)
├── voice_rvc.py            # RVC voice cloning wrapper
├── dns_fix.py              # DNS fix for edge-tts behind broken ISP DNS
├── screen_watcher.py       # Periodic screen capture + AI analysis
├── camera_watcher.py       # Webcam capture + AI analysis (on-demand)
├── desktop_overlay.py      # Always-on-top tkinter overlay
├── serve_viewer.py         # HTTP server for the 3D viewer
├── config/
│   └── api_keys.json       # API keys and settings (gitignored)
├── character_viewer/
│   ├── index.html          # Three.js + VRM 3D viewer
│   ├── style.css           # Glass theme UI
│   ├── models/
│   │   └── AliciaSolid.vrm # Anime character model
│   ├── backgrounds/        # Background images (16 included)
│   └── mood_bridge.json    # Python <-> browser state sync
├── voice_samples/          # Drop anime voice clips here for RVC
├── requirements.txt        # Python dependencies
├── run.bat                 # One-click setup and launch
└── RVC_SETUP.md            # Voice cloning setup guide
```

## Quick Start

### 1. Clone

```bash
git clone https://github.com/yourusername/miru.git
cd miru
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or just run `run.bat` on Windows -- it handles everything.

### 3. Set up API key

Edit `config/api_keys.json`:

```json
{
  "cerebras_api_key": "your-cerebras-api-key-here"
}
```

Get a free key at [cloud.cerebras.ai](https://cloud.cerebras.ai) (no credit card, 1M tokens/day).

### 4. Run

```bash
python -B main.py
```

Miru will open your browser to `http://localhost:5678` with the 3D character viewer.

## How It Works

**Brain**: Cerebras llama-3.3-70b handles chat. Fast, free, 1M tokens/day. For screen/camera watching, add a Gemini API key (supports vision).

**Voice**: edge-tts generates speech with the AnaNeural cartoon voice. SSML adds breath marks after exclamation marks, ellipses, and tildes for naturalness. Falls back to pyttsx3 (offline Windows voice) if edge-tts DNS is unreachable.

**3D Viewer**: Three.js renders an AliciaSolid VRM model with idle animations -- breathing, blinking, arm sway, body sway, eye tracking, spring bone physics for hair and clothes. Click on her for reactions.

**Voice Cloning**: Drop an anime voice sample (10-60 seconds, WAV/MP3) in `voice_samples/`, install RVC on a GPU machine, and Miru will clone the voice. See [RVC_SETUP.md](RVC_SETUP.md) for details.

**Screen Watching**: When a Gemini API key is configured, Miru periodically captures your screen and reacts to what she sees. Disabled by default (Cerebras doesn't support vision).

**Camera**: On-demand only. Say "look at me" or type `camera` in the terminal. Auto-stops after 30 seconds.

## Controls

### Browser

| Control | Action |
|---------|--------|
| Click on character | She reacts (happy expression, heart particles, speech) |
| Double-click | Angry reaction |
| Move mouse | Character tracks your cursor |
| Microphone button | Toggle speech-to-text input |
| Speaker button | Mute/unmute voice |

### Terminal

| Command | Action |
|---------|--------|
| `<anything>` | Talk to Miru |
| `capture` | Force screen capture and reaction |
| `camera` | Turn on webcam for 30 seconds |
| `camera off` | Turn off webcam |
| `reset` | Reset conversation memory |
| `help` | Show available commands |
| `quit` | Exit |

### Voice Commands (via mic button)

| Say | Action |
|-----|--------|
| "look at me" / "camera on" | Activates webcam for 30 seconds |
| "camera off" / "stop looking" | Deactivates webcam |
| Anything else | Sent to Miru as a conversation message |

## Configuration

Edit `config/api_keys.json`:

```json
{
  "cerebras_api_key": "csk-...",
  "cerebras_model": "llama-3.3-70b",
  "temperature": 0.85,
  "max_tokens": 4096,
  "voice": {
    "engine": "edge-tts",
    "voice": "en-US-AnaNeural",
    "speed": 1.0,
    "volume": 0.8
  },
  "character_viewer": {
    "port": 5678
  }
}
```

Optional fields for screen/camera watching:

```json
{
  "gemini_api_key": "AIzaSy...",
  "screen_watch_interval_seconds": 30,
  "camera_watch_interval_seconds": 15,
  "camera_index": 0
}
```

## Voice Cloning (RVC)

For an anime-quality cloned voice:

1. Get a voice sample (10-60 seconds of clean audio from an anime character)
2. Put it in `voice_samples/`
3. On a machine with an NVIDIA GPU:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
   pip install rvc-python
   ```
4. Run `python -B main.py` -- RVC auto-activates

See [RVC_SETUP.md](RVC_SETUP.md) for tuning parameters and troubleshooting.

Without a GPU, Miru uses edge-tts AnaNeural (still sounds decent).

## Desktop Overlay

A small always-on-top window shows Miru's mood and latest speech. It appears automatically when Miru starts. Drag it anywhere on screen.

## API Keys

| Service | Purpose | Free Tier |
|---------|---------|-----------|
| [Cerebras](https://cloud.cerebras.ai) | Chat brain | 1M tokens/day |
| [Gemini](https://aistudio.google.com/apikey) | Vision (screen/camera) | Free tier available |

## Requirements

- Python 3.10+
- Windows 10/11 (uses winmm.dll for audio playback)
- Internet connection (for edge-tts voice generation)
- Optional: NVIDIA GPU with 4GB+ VRAM for RVC voice cloning

## Tech Stack

- **LLM**: Cerebras llama-3.3-70b (via OpenAI-compatible API)
- **TTS**: edge-tts (Microsoft Edge neural voices) with SSML
- **Voice Cloning**: RVC (Retrieval-based Voice Conversion)
- **3D Rendering**: Three.js + @pixiv/three-vrm
- **Character Model**: AliciaSolid (VRM 0.x format)
- **Screen Capture**: mss
- **Webcam**: OpenCV
- **Desktop Overlay**: tkinter

## License

MIT
