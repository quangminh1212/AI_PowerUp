<!-- source: https://github.com/neosun100/higgs-audio-web.git sha: b20679f38c23f672218f93eb85ebaccd0f96a3b7 readme: main/README.md -->
# neosun100/higgs-audio-web

🎵 All-in-One Docker deployment for Higgs Audio v2 with Web UI, REST API & MCP support. Features: Expressive TTS, Zero-Shot Voice Cloning, Multi-Speaker Dialog, Text Profile Voice.

---

<h1 align="center">🎵 Higgs Audio v2 Web</h1>

<p align="center">
  <strong>All-in-One Docker deployment for Higgs Audio v2 with Web UI, REST API & MCP support</strong>
</p>

<p align="center">
  <a href="README.md">English</a> | 
  <a href="README_CN.md">简体中文</a> | 
  <a href="README_TW.md">繁體中文</a> | 
  <a href="README_JP.md">日本語</a>
</p>

<p align="center">
  <a href="https://github.com/neosun100/higgs-audio-web/stargazers"><img src="https://img.shields.io/github/stars/neosun100/higgs-audio-web?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/neosun100/higgs-audio-web/blob/main/LICENSE"><img src="https://img.shields.io/github/license/neosun100/higgs-audio-web?style=flat-square" alt="License"></a>
  <a href="https://hub.docker.com/r/neosun/higgs-audio-web"><img src="https://img.shields.io/docker/pulls/neosun/higgs-audio-web?style=flat-square" alt="Docker Pulls"></a>
  <img src="https://img.shields.io/badge/python-3.10+-blue?style=flat-square" alt="Python">
  <img src="https://img.shields.io/badge/CUDA-12.x-green?style=flat-square" alt="CUDA">
</p>

<p align="center">
  <img src="figures/webui-screenshot.png" alt="Web UI Screenshot" width="800">
</p>

---

## ✨ Features

- 🎤 **Expressive TTS** - State-of-the-art text-to-speech with emotional expression
- 🎭 **Zero-Shot Voice Cloning** - Clone any voice with just 5-10 seconds of audio
- 👥 **Multi-Speaker Dialog** - Generate natural conversations with multiple speakers
- 📝 **Text Profile Voice** - Describe voice characteristics in text, no audio needed
- 📚 **Long-form Generation** - Auto-chunking for long text with consistent voice
- 🌐 **Modern Web UI** - Beautiful dark-themed interface with multi-language support
- 🔌 **REST API** - Full-featured API with Swagger documentation
- 🤖 **MCP Support** - Model Context Protocol for AI agent integration
- 🐳 **One-Click Docker** - All-in-one container, no external dependencies
- 🎮 **GPU Optimized** - Auto-selects the GPU with most free memory

---

## 🚀 Quick Start

### Docker (Recommended)

```bash
docker run -d --gpus all \
  -p 8095:8095 \
  -v ~/.cache/huggingface:/app/models \
  --name higgs-audio \
  neosun/higgs-audio-web:latest
```

Then visit: http://localhost:8095

---

## 📦 Installation

### Prerequisites

- NVIDIA GPU with **24GB+ VRAM** (e.g., RTX 4090, L40S, A100)
- Docker with NVIDIA Container Toolkit
- Or: Python 3.10+, CUDA 12.x

### Option 1: Docker (Recommended)

```bash
# Pull the image
docker pull neosun/higgs-audio-web:latest

# Run with GPU support
docker run -d --gpus all \
  -p 8095:8095 \
  -v ~/.cache/huggingface:/app/models \
  -v ./outputs:/app/outputs \
  --name higgs-audio \
  neosun/higgs-audio-web:latest

# Check logs
docker logs -f higgs-audio

# Verify
curl http://localhost:8095/health
```

### Option 2: Docker Compose

```yaml
# docker-compose.yml
services:
  higgs-audio:
    image: neosun/higgs-audio-web:latest
    ports:
      - "8095:8095"
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
      - MODEL_PATH=bosonai/higgs-audio-v2-generation-3B-base
      - AUDIO_TOKENIZER_PATH=bosonai/higgs-audio-v2-tokenizer
    volumes:
      - ~/.cache/huggingface:/app/models
      - ./outputs:/app/outputs
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

```bash
docker compose up -d
```

### Option 3: From Source

```bash
# Clone repository
git clone https://github.com/neosun100/higgs-audio-web.git
cd higgs-audio-web

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
pip install -e .
pip install fastapi uvicorn python-multipart aiofiles fastmcp soundfile

# Run
python app/main.py
```

### Option 4: One-Click Script

```bash
git clone https://github.com/neosun100/higgs-audio-web.git
cd higgs-audio-web
chmod +x start.sh
./start.sh
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8095` | Service port |
| `NVIDIA_VISIBLE_DEVICES` | `all` | GPU device ID(s) |
| `MODEL_PATH` | `bosonai/higgs-audio-v2-generation-3B-base` | Model path |
| `AUDIO_TOKENIZER_PATH` | `bosonai/higgs-audio-v2-tokenizer` | Tokenizer path |
| `HF_HOME` | `~/.cache/huggingface` | HuggingFace cache |

### .env Example

```bash
PORT=8095
NVIDIA_VISIBLE_DEVICES=0
MODEL_PATH=bosonai/higgs-audio-v2-generation-3B-base
AUDIO_TOKENIZER_PATH=bosonai/higgs-audio-v2-tokenizer
```

---

## 📖 Usage

### Web UI

Visit `http://localhost:8095` for the web interface with 6 modes:

| Mode | Description |
|------|-------------|
| **Smart Voice** | Model auto-selects appropriate voice |
| **Preset Voice** | Choose from 16 built-in voices |
| **Voice Clone** | Upload reference audio for cloning |
| **Text Profile** | Describe voice in text (e.g., "Male, British accent") |
| **Multi-Speaker** | Generate dialog with `[SPEAKER0]`, `[SPEAKER1]` tags |
| **Long-form** | Auto-chunk long text for consistent generation |

### REST API

#### Health Check
```bash
curl http://localhost:8095/health
```

#### Basic TTS
```bash
curl -X POST http://localhost:8095/api/tts \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world!", "temperature": 0.3}'
```

#### Voice Cloning with Preset
```bash
curl -X POST http://localhost:8095/api/tts/preset \
  -F "text=Hello world!" \
  -F "voice=belinda" \
  -F "temperature=0.3"
```

#### Text Profile TTS
```bash
curl -X POST http://localhost:8095/api/tts/profile \
  -H "Content-Type: application/json" \
  -d '{"text": "Good morning!", "profile": "male_en_british"}'
```

#### Multi-Speaker Dialog
```bash
curl -X POST http://localhost:8095/api/tts/multispeaker \
  -H "Content-Type: application/json" \
  -d '{
    "text": "[SPEAKER0] Hello!\n[SPEAKER1] Hi there!",
    "voices": "belinda,broom_salesman"
  }'
```

#### Long-form Generation
```bash
curl -X POST http://localhost:8095/api/tts/longform \
  -H "Content-Type: application/json" \
  -d '{"text": "Long text here...", "voice": "belinda", "chunk_size": 100}'
```

Full API documentation: `http://localhost:8095/docs`

### MCP Integration

Add to your MCP client config:

```json
{
  "mcpServers": {
    "higgs-audio": {
      "command": "python",
      "args": ["app/mcp_server.py"],
      "env": {
        "MODEL_PATH": "bosonai/higgs-audio-v2-generation-3B-base"
      }
    }
  }
}
```

Available MCP tools:
- `text_to_speech` - Basic TTS
- `text_to_speech_with_voice` - TTS with preset voice
- `text_to_speech_with_profile` - TTS with text profile
- `text_to_speech_multispeaker` - Multi-speaker dialog
- `list_voices` / `list_profiles` - List available options
- `get_gpu_status` / `load_model` / `unload_model` - GPU management

---

## 📁 Project Structure

```
higgs-audio-web/
├── app/
│   ├── main.py           # FastAPI server
│   ├── mcp_server.py     # MCP server
│   └── static/
│       └── index.html    # Web UI
├── boson_multimodal/     # Core model code
├── examples/
│   └── voice_prompts/    # 16 preset voices
├── Dockerfile
├── docker-compose.yml
├── start.sh              # One-click launcher
└── requirements.txt
```

---

## 🛠️ Tech Stack

- **Model**: Higgs Audio v2 (3.6B LLM + 2.2B audio adapter)
- **Backend**: FastAPI, Uvicorn
- **Frontend**: Vanilla JS, CSS3
- **Container**: Docker, NVIDIA Container Toolkit
- **ML Framework**: PyTorch, Transformers, TorchAudio

---

## 🎯 Performance

| Benchmark | Score |
|-----------|-------|
| EmergentTTS Emotions | **75.7%** win rate vs gpt-4o-mini-tts |
| EmergentTTS Questions | **55.7%** win rate vs gpt-4o-mini-tts |
| Seed-TTS Eval SIM | **67.70** |
| ESD Emotion SIM | **86.13** |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

---

## 📝 Changelog

### v2.1.0 (2024-12-19)
- ✨ Multi-speaker dialog generation
- ✨ Text profile voice (no audio needed)
- ✨ Long-form generation with auto-chunking
- 🎨 Enhanced Web UI with 6 generation modes

### v2.0.0 (2024-12-18)
- 🎉 Initial release
- ✨ Web UI with multi-language support
- ✨ REST API with Swagger docs
- ✨ MCP server integration
- ✨ All-in-one Docker image
- ✨ Auto GPU selection

---

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

Based on [Higgs Audio v2](https://github.com/boson-ai/higgs-audio) by Boson AI.

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=neosun100/higgs-audio-web&type=Date)](https://star-history.com/#neosun100/higgs-audio-web)

---

## 📱 Follow Us

<p align="center">
  <img src="https://img.aws.xin/uPic/扫码_搜索联合传播样式-标准色版.png" alt="WeChat" width="300">
</p>

---

<p align="center">Made with ❤️ by <a href="https://github.com/neosun100">neosun100</a></p>
