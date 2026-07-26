<!-- source: https://github.com/Itachi-1824/goblin-ai.git sha: 01a3f00779f8acd70c041cbab7fe71bccd81f827 readme: main/README.md -->
# Itachi-1824/goblin-ai

🎨 Unlimited free AI image generation. No sign-up required. Supports 30+ models including Flux, SDXL, anime, realistic, and more.

---

<div align="center">

# 🎨 Goblin AI

### ✨ Unlimited Free AI Image Generation ✨

**No sign-up. No API keys. No limits. Just art.**

[![PyPI version](https://img.shields.io/pypi/v/goblin-ai?color=blue&label=PyPI)](https://pypi.org/project/goblin-ai/)
[![Python](https://img.shields.io/pypi/pyversions/goblin-ai?color=green)](https://pypi.org/project/goblin-ai/)
[![Downloads](https://img.shields.io/pypi/dm/goblin-ai?color=orange)](https://pypi.org/project/goblin-ai/)
[![License](https://img.shields.io/badge/license-Proprietary-red)](LICENSE)

<br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=9B59B6&center=true&vCenter=true&width=500&lines=Generate+anything...;Anime+%F0%9F%8C%B8;Portraits+%F0%9F%93%B7;Fantasy+%F0%9F%90%89;Cyberpunk+%F0%9F%8C%83;Pixel+Art+%F0%9F%8E%AE" alt="Typing SVG" />

<br>

[**Get Started**](#-quick-start) • [**Models**](#-30-models) • [**API**](#-simple-api) • [**Server**](#-run-as-server)

</div>

---

## 🚀 Installation

```bash
pip install goblin-ai
```

**With upscaling superpowers:**
```bash
pip install goblin-ai[all]  # Real-ESRGAN + FSRCNN neural upscaling
```

### 💻 System Requirements

| Resolution | CPU | GPU (Optional) |
|------------|-----|----------------|
| Up to 768px | Any modern CPU | Not required |
| Up to 1024px | Any modern CPU | Any GPU with 2GB+ VRAM |
| 1024px - 2048px | i5/Ryzen 5+ | **GTX 1650** or higher recommended |
| 2048px - 4096px | i7/Ryzen 7+ | **GTX 1660** or RTX series recommended |

> **Note:** GPU acceleration (CUDA/DirectML) is optional but highly recommended for high-resolution upscaling. Without GPU, images >1024px may be slow on CPU.

---

## ⚡ Quick Start

```python
import asyncio
from goblin import generate

async def main():
    # 🎯 One-liner - model auto-selected from prompt
    await generate("a cute anime girl", output="anime.png")

    # 📸 Realistic portrait
    await generate("professional headshot, studio lighting", output="portrait.png")

    # 🐉 Fantasy art with specific model
    await generate("epic dragon", model="goblin-fantasy", output="dragon.png")

asyncio.run(main())
```

**That's it.** No API keys. No accounts. No BS.

---

## 🎭 30+ Models

<table>
<tr>
<td width="33%" valign="top">

### 🎨 General
| Model | Style |
|-------|-------|
| `goblin-sd` | All-rounder |
| `goblin-pro` | Professional |
| `goblin-flux` | Best text |
| `goblin-flux-pro` | Enhanced |
| `goblin-sdxl` | High-res |

</td>
<td width="33%" valign="top">

### 🌸 Anime
| Model | Style |
|-------|-------|
| `goblin-anime` | Classic |
| `goblin-anime-xl` | Advanced |
| `goblin-chibi` | Kawaii |
| `goblin-anime-uncensored` | 18+ |

</td>
<td width="33%" valign="top">

### 📷 Photo
| Model | Style |
|-------|-------|
| `goblin-realistic` | Photorealistic |
| `goblin-portrait` | Portraits |
| `goblin-portrait-hd` | HD |
| `goblin-photo` | Camera |

</td>
</tr>
<tr>
<td width="33%" valign="top">

### 🖌️ Art Styles
| Model | Style |
|-------|-------|
| `goblin-digital` | Digital art |
| `goblin-concept` | Concept art |
| `goblin-fantasy` | Fantasy |
| `goblin-cyberpunk` | Cyberpunk |
| `goblin-pixel` | Pixel art |
| `goblin-oil` | Oil painting |

</td>
<td width="33%" valign="top">

### 🏔️ Scenes
| Model | Style |
|-------|-------|
| `goblin-landscape` | Nature |
| `goblin-background` | Wallpapers |

</td>
<td width="33%" valign="top">

### 🎮 Game Assets
| Model | Style |
|-------|-------|
| `goblin-icon` | App icons |
| `goblin-sprite` | 2D sprites |
| `goblin-pokemon` | Creatures |
| `goblin-character` | Characters |
| `goblin-furry` | Furry art |

</td>
</tr>
</table>

---

## 🔧 Simple API

```python
from goblin import generate, detect_model

# 🤖 Auto model selection
model = detect_model("1girl anime")  # Returns "goblin-anime"

# 🎛️ Full control
image = await generate(
    prompt="beautiful sunset over mountains",
    model="goblin-landscape",
    quality="ultra",        # standard | high | ultra | maximum
    width=1024,
    height=768,
    seed=42,                # Reproducible results
    guidance_scale=7.0      # Prompt adherence (1-30)
)
```

---

## 🏗️ Advanced Usage

```python
from goblin import Goblin

async with Goblin() as g:
    # 🎨 Full parameter control
    image = await g.generate(
        prompt="cyberpunk city at night, neon lights, rain",
        model="goblin-cyberpunk",
        style="neon",
        quality="ultra",
        lighting="dramatic",
        guidance_scale=7.5
    )

    # 💾 Save with custom path
    image.save("cyberpunk_city.png")
```

---

## 🌐 Run as Server

```bash
goblin --port 8000
```

Then hit the API:

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "a magical forest", "model": "goblin-fantasy"}'
```

---

## 📊 Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `prompt` | What to generate | *Required* |
| `model` | Model ID (see above) | Auto-detected |
| `quality` | `standard` \| `high` \| `ultra` \| `maximum` | `ultra` |
| `style` | Style preset | `default` |
| `lighting` | Lighting preset | `auto` |
| `width` | Image width (64-4096px) | `768` |
| `height` | Image height (64-4096px) | `768` |
| `seed` | Random seed (-1 = random) | `-1` |
| `guidance_scale` | Prompt adherence (1-30) | Model default |
| `enhance_output` | Smart enhancement pipeline | `True` |
| `upscale_output` | 4x AI upscaling (slower) | `False` |

---

## 🔬 Upscaling & Enhancement

Goblin includes a powerful AI upscaling system with 24+ models:

```python
from goblin import generate

# Auto-enhanced output (default) - resize + restore + PNG
image = await generate("dragon", width=1920, height=1080)

# 4x AI upscaling for maximum quality
image = await generate("dragon", width=4096, height=4096, upscale_output=True)

# Raw output (no enhancement, JPEG from API)
image = await generate("dragon", enhance_output=False)
```

### 🚀 Upscale Performance

| Target Size | GPU (GTX 1650+) | CPU Only |
|-------------|-----------------|----------|
| 768px | ~1s | ~3s |
| 1024px | ~2s | ~8s |
| 2048px | ~5s | ~30s |
| 4096px | ~15s | ~2min |

> **Tip:** For images >1024px, a GPU with 4GB+ VRAM provides 5-10x faster upscaling.

---

## 🔒 Why Compiled Binaries?

<details>
<summary><b>Click to learn why this package uses .pyd/.so files</b></summary>

<br>

This package is distributed as compiled binaries instead of plain Python. Here's why:

### 🛡️ Protecting the Free Service

Goblin wraps a free image generation API with rate limits (1 image at a time per user). If source code were public, bad actors could:
- ❌ Bypass rate limits and overload the service
- ❌ Run concurrent requests that would get everyone blocked
- ❌ Abuse the API and get it shut down

By compiling the code, we ensure **fair usage for everyone** while keeping it **free**.

### ✅ This Is NOT Malware

| What Goblin Does | What Goblin Does NOT Do |
|------------------|------------------------|
| ✅ Generates images via public API | ❌ Access your files |
| ✅ Downloads AI models for upscaling | ❌ Send personal data anywhere |
| ✅ Caches for faster generation | ❌ Install anything outside its folder |
| ✅ Runs offline after setup | ❌ Require accounts or signups |

### 🔓 Open Source Commitment

- The API (`__init__.py`) is readable Python
- All dependencies are standard PyPI packages
- Built with [Nuitka](https://nuitka.net/) (legitimate Python compiler)

*Still concerned? Run it in a sandbox or VM first.*

</details>

---

<div align="center">

## 💜 Made for Artists, by Artists

**Star ⭐ this repo if Goblin helped you create something awesome!**

<br>

[![GitHub stars](https://img.shields.io/github/stars/Itachi-1824/goblin-ai?style=social)](https://github.com/Itachi-1824/goblin-ai)

<br>

*© 2026 [Itachi-1824](https://github.com/Itachi-1824) • [PyPI](https://pypi.org/project/goblin-ai/) • [GitHub](https://github.com/Itachi-1824/goblin-ai)*

</div>
