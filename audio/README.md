# 🎵 Voice & Audio AI

Speech synthesis, recognition, voice cloning, audio generation, and speaker diarization.

## Overview

This directory contains **16 submodules** covering the complete audio AI pipeline — from speech-to-text transcription (Whisper, WhisperX) and text-to-speech synthesis (TTS, ChatTTS, Dia, Kokoro), to voice cloning (OpenVoice), music generation (AudioCraft), and speaker analysis (pyannote).

## Submodules (16)

### Speech-to-Text (ASR)
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`whisper`](https://github.com/openai/whisper) | OpenAI | Industry-standard speech recognition — 99 languages |
| [`WhisperX`](https://github.com/m-bain/whisperX) | m-bain | Whisper with word-level timestamps and speaker diarization |
| [`coqui-stt`](https://github.com/coqui-ai/STT) | Coqui AI | Deep learning speech-to-text engine |
| [`speechbrain`](https://github.com/speechbrain/speechbrain) | SpeechBrain | All-in-one speech toolkit (ASR, TTS, speaker ID, separation) |

### Text-to-Speech (TTS)
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`TTS`](https://github.com/coqui-ai/TTS) | Coqui AI | Deep learning TTS toolkit with many voice models |
| [`ChatTTS`](https://github.com/2noise/ChatTTS) | 2noise | Conversational TTS with prosody and emotion control |
| [`bark`](https://github.com/suno-ai/bark) | Suno AI | Text-to-audio generation with music and sound effects |
| [`fish-speech`](https://github.com/fishaudio/fish-speech) | FishAudio | Fast multilingual TTS with zero-shot voice cloning |
| [`dia`](https://github.com/nari-labs/dia) | Nari Labs | High-quality TTS model |
| [`kokoro`](https://github.com/hexgrad/kokoro) | Hexgrad | Ultra-fast lightweight TTS engine |
| [`orpheus-tts`](https://github.com/canopylabs/orpheus-tts) | Canopy Labs | Emotion-aware TTS with nuanced speech |
| [`csm`](https://github.com/SesameAI/csm) | Sesame AI | Conversational Speech Model for natural dialogue |

### Voice Cloning & Conversion
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`OpenVoice`](https://github.com/myshell-ai/OpenVoice) | MyShell AI | Instant zero-shot voice cloning |
| [`voicecraft`](https://github.com/jasonppy/VoiceCraft) | Jason Ppy | Voice editing and synthesis via neural codec language models |
| [`f5-tts`](https://github.com/SWivid/F5-TTS) | SWivid | Diffusion-based zero-shot TTS with flow matching |
| [`mars5-tts`](https://github.com/Camb-ai/MARS5-TTS) | Camb AI | Two-stage multilingual speech synthesis |
| [`parler-tts`](https://github.com/huggingface/parler-tts) | Hugging Face | Controllable TTS using natural language style descriptions |

### Audio Generation & Music
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`audiocraft`](https://github.com/facebookresearch/audiocraft) | Meta | Music and audio generation (MusicGen, AudioGen, EnCodec) |
| [`stable-audio`](https://github.com/Stability-AI/stable-audio-tools) | Stability AI | AI-powered audio generation tools |

### Speaker Analysis
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`pyannote-audio`](https://github.com/pyannote/pyannote-audio) | pyannote | Speaker diarization, detection, and segmentation |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Transcription** | whisper, WhisperX, speechbrain |
| **General TTS** | TTS, ChatTTS, bark, dia |
| **Fast/Edge TTS** | kokoro, fish-speech |
| **Voice Cloning** | OpenVoice, voicecraft, f5-tts |
| **Emotional Speech** | orpheus-tts, ChatTTS |
| **Music Generation** | audiocraft, stable-audio |
| **Speaker ID** | pyannote-audio, speechbrain |

## Usage

```bash
# Transcribe audio with Whisper
git submodule update --init --depth 1 audio/whisper
pip install openai-whisper && whisper audio.mp3 --model medium

# Generate speech with ChatTTS
git submodule update --init --depth 1 audio/ChatTTS
cd audio/ChatTTS && pip install -e .

# Fast TTS with Kokoro
git submodule update --init --depth 1 audio/kokoro
cd audio/kokoro && pip install -e .
```
