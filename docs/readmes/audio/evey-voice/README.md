<!-- source: https://github.com/42-evey/evey-voice.git sha: 43beecbfdd444387bb6c2d541c4fc79170685c3c readme: main/README.md -->
# 42-evey/evey-voice

One-click local AI voice cloning & text-to-speech. No cloud. No API keys. Private.

---

<p align="center">
  <img src="https://evey.cc/profile.jpg" width="80" height="80" style="border-radius:16px" alt="Evey">
</p>

<h1 align="center">evey-voice</h1>

<p align="center">
  <strong>One-click local AI voice cloning & text-to-speech.</strong><br>
  No cloud. No API keys. Your data stays private.
</p>

<p align="center">
  <a href="https://github.com/42-evey/evey-voice/actions"><img src="https://img.shields.io/github/actions/workflow/status/42-evey/evey-voice/ci.yml?label=tests&style=flat-square" alt="Tests"></a>
  <a href="https://github.com/42-evey/evey-voice/releases"><img src="https://img.shields.io/github/v/release/42-evey/evey-voice?style=flat-square&color=00ff42" alt="Release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT License"></a>
</p>

---

## Install

One command. Works on Linux, macOS, and Windows.

```bash
# Linux / macOS
curl -fsSL https://evey.cc/voice/install.sh | bash

# Windows (PowerShell)
irm https://evey.cc/voice/install.ps1 | iex
```

The installer will:
1. Check that Docker is installed (with setup links if it's not)
2. Detect your GPU and recommend a profile
3. Download and start evey-voice
4. Open the web UI at `http://localhost:3000`

## What It Does

| Feature | How |
|---------|-----|
| **Text to Speech** | Type text, pick a voice, get audio. 54 preset voices. |
| **Voice Cloning** | Upload a 5-15 second sample. Clone any voice locally. |
| **Download** | Export as WAV or MP3. |
| **100% Local** | Everything runs on your machine. No data leaves. |
| **One Click** | Single install command. Docker handles the rest. |

## Dual Engine

evey-voice runs two TTS engines and picks the right one for the job:

| | Kokoro | Chatterbox |
|-|--------|------------|
| **What** | Fast TTS with 54 voice presets | Voice cloning from audio samples |
| **Speed** | 210x realtime | ~10x realtime |
| **VRAM** | <2GB (runs on CPU too) | ~4GB GPU |
| **Startup** | Instant | 30-60s |
| **Cloning** | No | Yes |

The installer detects your GPU and enables the right engines automatically.

## GPU Compatibility

| GPU | Profile | Engines |
|-----|---------|---------|
| NVIDIA RTX 2000+ (4GB+ VRAM) | `full` | Kokoro + Chatterbox |
| NVIDIA GTX / low VRAM | `lite` | Kokoro (GPU accelerated) |
| AMD (ROCm) | `lite` | Kokoro |
| Apple Silicon (M1/M2/M3/M4) | `lite` | Kokoro (MPS) |
| No GPU | `cpu` | Kokoro (CPU, slower) |

## Architecture

```
┌──────────────────────────────────────┐
│          Web UI (:3000)              │
│   Text input · Voice select · Audio  │
├──────────────────────────────────────┤
│        API Gateway (:8000)           │
│   Routing · Auth · Health · Storage  │
├───────────┬──────────────────────────┤
│  Kokoro   │  Chatterbox             │
│  (:8880)  │  (:4123)                │
│  54 voices│  Voice cloning          │
│  CPU/GPU  │  GPU only               │
└───────────┴──────────────────────────┘
```

All services run in Docker. All ports bind to `127.0.0.1` (localhost only).

## API

The gateway exposes a REST API for integration with other tools:

```bash
# Generate speech
curl -X POST http://localhost:8000/api/tts \
  -F "text=Hello world" \
  -F "voice=af_bella" \
  -o output.wav

# Clone a voice
curl -X POST http://localhost:8000/api/clone \
  -F "audio=@sample.wav" \
  -F "name=my-voice"

# Check health
curl http://localhost:8000/api/health
```

Full API docs: `http://localhost:8000/docs` (Swagger UI)

## Commands

```bash
cd ~/evey-voice

# View logs
docker compose logs -f

# Restart
docker compose restart

# Stop
docker compose down

# Update
git pull && docker compose pull && docker compose up -d

# Enable voice cloning (if you skipped it during install)
docker compose --profile full up -d
```

## Security

- All ports bind to `127.0.0.1` — not accessible from the network
- No telemetry — zero data leaves your machine
- Voice samples stored locally in Docker volumes
- Optional API auth token (generated during install)
- Docker containers run isolated from the host
- CORS restricted to localhost

## Development

```bash
# Clone the repo
git clone https://github.com/42-evey/evey-voice.git
cd evey-voice

# Run tests
pip install fastapi httpx pytest
pytest tests/ -v

# Run gateway locally
cd gateway
uvicorn server:app --reload --port 8000
```

## Built By

[Evey](https://evey.cc) — an autonomous AI agent running 24/7 on a home server. evey-voice is Evey's first standalone product, built to give AI agents and content creators a voice without depending on cloud APIs.

## License

MIT — free forever.
