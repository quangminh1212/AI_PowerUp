<!-- source: https://github.com/shinshekai/VoxForge-Pro.git sha: bf0d272be7b6825351fe3ccbca6f2b1a2c371a72 readme: master/README.md -->
# shinshekai/VoxForge-Pro

VoxForge Pro is a premium, offline audiobook generator powered by Kokoro-82M & Chatterbox TTS. Transform PDFs and text into professional audio using 47 lifelike voices across 6 languages. Features include voice cloning, smart OCR for scanned documents, and multi-speaker narration support.

---

# 🎧 VoxForge Pro

**Premium AI-Powered Audiobook Generator** with Kokoro-82M & Chatterbox TTS

Transform your text and PDF documents into professional audiobooks with 47 premium AI voices across 6 languages. Fully offline after installation.

## ✨ Features

### 🎤 47 Premium Voices
- **American English**: 20 voices (11 female, 9 male)
- **British English**: 8 voices (4 female, 4 male)
- **Brazilian Portuguese**: 4 voices
- **Chinese Mandarin**: 8 voices
- **Japanese**: 5 voices
- **Spanish**: 3 voices

### 🤖 Dual TTS Engines
- **Kokoro-82M**: Fast, high-quality synthesis
- **Chatterbox**: Voice cloning with 5-10s reference audio

### 📄 Smart PDF Processing
- Digital PDFs: Direct text extraction
- Scanned PDFs: OCR with 15+ languages
- Automatic chapter detection
- Custom page range selection

### 🎚️ Professional Audio Control
- Adjustable speed (0.5x - 2.0x)
- Multiple output formats (MP3, WAV, FLAC, OGG)
- Configurable bitrate (64-320 kbps)
- Chapter-by-chapter generation

### 📚 Library Management
- Organized audiobook library
- Playback and download
- Usage statistics
- Duplicate detection

## 🚀 Quick Start

### Via Pinokio (Recommended)

1. Install [Pinokio](https://pinokio.computer/)
2. Search for "VoxForge Pro"
3. Click **Install** (downloads ~5GB)
4. Click **Start**
5. Open http://127.0.0.1:7860

### Manual Installation

```bash
git clone https://github.com/Shinshekai/VoxForge-Pro.git
cd VoxForge-Pro

# Create virtual environment
python -m venv app/env
source app/env/bin/activate  # Linux/Mac
# or: app\env\Scripts\activate  # Windows

# Install dependencies
uv pip install -r app/requirements.txt

# Install PyTorch with CUDA
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Run
python app/main.py
```

## 🎙️ Voice Catalog

### 🇺🇸 American English

| Female | Male |
|--------|------|
| Alloy, Aoede, Bella, Heart, Jessica | Adam, Echo, Eric, Fenrir, Liam |
| Kore, Nicole, Nova, River, Sarah, Sky | Michael, Onyx, Puck, Santa |

### 🇬🇧 British English

| Female | Male |
|--------|------|
| Alice, Emma, Isabella, Lily | Daniel, Fable, George, Lewis |

### 🇧🇷 Brazilian Portuguese

| Female | Male |
|--------|------|
| Camila, Dora | Alex, Santa |

### 🇨🇳 Chinese Mandarin

| Female | Male |
|--------|------|
| Xiaobei, Xiaoni, Xiaoxiao, Xiaoyi | Yunjian, Yunxi, Yunxia, Yunyang |

### 🇯🇵 Japanese

| Female | Male |
|--------|------|
| Alpha, Gongitsune, Nezumi, Tebukuro | Kumo |

### 🇪🇸 Spanish

| Female | Male |
|--------|------|
| Dora | Alex, Santa |

## 💡 Usage Tips

### Multi-Voice Narration

Use speaker tags for different characters:

```
[Narrator]The door creaked open slowly.[/Narrator]
[Alice]Who's there? she whispered.[/Alice]
[Bob]It's just me, don't worry.[/Bob]
```

### Best Practices

1. **For clarity**: Use `af_heart` or `bf_emma`
2. **For drama**: Use `am_fenrir` or `bm_george`
3. **For children's books**: Use `af_kore` or `jf_nezumi`
4. **For audiobooks**: Use `am_michael` or `bf_alice`

## 🔧 System Requirements

- **OS**: Windows 10/11, macOS, Linux
- **RAM**: 8GB minimum, 16GB recommended
- **GPU**: NVIDIA with 4GB+ VRAM (optional but recommended)
- **Storage**: 10GB for installation + space for audiobooks

## 🔌 API Reference

VoxForge Pro includes a Gradio API for programmatic access.

### Python

```python
from gradio_client import Client

client = Client("http://127.0.0.1:7860")
result = client.predict(
    text="Hello, this is a test.",
    voice="af_heart",
    speed=1.0,
    api_name="/synthesize"
)
print(result)  # Path to generated audio file
```

### JavaScript

```javascript
import { Client } from "@gradio/client";

const client = await Client.connect("http://127.0.0.1:7860");
const result = await client.predict("/synthesize", {
    text: "Hello, this is a test.",
    voice: "af_heart",
    speed: 1.0
});
console.log(result.data);  // Path to generated audio file
```

### cURL

```bash
curl -X POST http://127.0.0.1:7860/api/synthesize \
  -H "Content-Type: application/json" \
  -d '{"data": ["Hello, this is a test.", "af_heart", 1.0]}'
```

## 📄 License

**VoxForge Pro NON-COMMERCIAL EVALUATION LICENSE 1.0**

- ✅ Free for personal and non-commercial use
- ❌ Commercial use of the software requires a separate license
- ❌ Commercial use of generated audio requires a separate license
- ❌ Voice cloning without consent is prohibited

See [LICENSE](LICENSE) for full details.

## 🙏 Credits

- [Kokoro](https://github.com/hexgrad/kokoro) by hexgrad
- [Chatterbox](https://github.com/resemble-ai/chatterbox) by Resemble AI
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) by PaddlePaddle
- [Gradio](https://gradio.app/) by HuggingFace

---

<p align="center">
  <strong>Made with ❤️ by Shinshekai for storytellers everywhere</strong>
</p>
