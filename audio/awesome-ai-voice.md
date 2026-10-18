# Awesome TTS & Voice Generation Models

A curated list of open-source Text-to-Speech (TTS) and voice cloning models. Models are sorted by release date (newest first).

![logo-tts2](https://user-attachments/assets/132b105b-b894-4150-bace-e84ef70ed2be)

---

## Table of Contents

- [Text-to-Speech (TTS) Models](#text-to-speech-tts-models)
- [Anything to Audio](#anything-to-audio)
- [Audio Restoration & Enhancement](#audio-restoration--enhancement)
- [Speech Recognition (ASR)](#speech-recognition-asr)
- [Audio Codecs & Tokenizers](#audio-codecs--tokenizers)
- [Audio Transcription Models](#audio-transcription-models)
- [Additional Resources](#additional-resources)

---

## Text-to-Speech (TTS) Models

### TTS Quick Comparison

| Model | Voice Cloning | ASR | Languages | Streaming | License |
| :--- | :---: | :---: | :--- | :---: | :--- |
| [Audio8-TTS-Preview-0.6b](#audio8-tts-preview-0-6b) | ✅ | ❌ | Cantonese, Chinese, Dutch, English, French, German, Italian, Japanese, Korean, Polish, Spanish | ❌ | ![Apache 2.0][license-apache-2.0] |
| [NeuTTS-2E](#neutts-2e) | ❌ | ❌ | English | ✅ | ![Unknown][license-unknown] |
| [Scylla's Band](#scyllasband) | ❌ | ❌ | en_us, en_gb, es, it | ✅ | ![Apache 2.0][license-apache-2.0] |
| [sanoTTS](#sanotts) | ❌ | ❌ | English, Nepali, Hindi, Vietnamese, Indonesian, Chinese | ❌ | ![Unknown][license-unknown] |
| [FreyaTTS](#freyatts) | ❌ | ❌ | Turkish | ❌ | ![Apache 2.0][license-apache-2.0] |
| [Inflect-Nano-v2](#inflect-nano-v2) | ❌ | ❌ | English | ❌ | ![Apache 2.0][license-apache-2.0] |
| [Gepard](#gepard) | ✅ | ❌ | English, Spanish, Portuguese, Dutch | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Higgs Audio v3 TTS](#higgs-audio-v3-tts) | ✅ | ❌ | 102 | ✅ | ![Research Only][license-research-only] |
| [dots.tts](#dots-tts) | ✅ | ❌ | Multilingual | ❌ | ![Apache 2.0][license-apache-2.0] |
| [Confucius4-TTS](#confucius4-tts) | ✅ | ❌ | 14 | ❌ | ![Apache 2.0][license-apache-2.0] |
| [WavTTS](#wavtts) | ✅ | ❌ | English, Chinese | ❌ | ![CC BY-NC 4.0][license-cc-by-nc-4.0] |
| [MOSS-TTS](#moss-tts) | ✅ | ❌ | 31 | ✅ | ![Apache 2.0][license-apache-2.0] |
| [VoxFlash-TTS](#voxflash-tts) | ✅ | ❌ | Chinese, English | ❌ | ![Apache 2.0][license-apache-2.0] |
| [Miso TTS](#misotts) | ✅ | ❌ | English | ❌ | ![MIT][license-mit] |
| [OronTTS](#oron-tts) | ✅ | ❌ | Mongolian, Kazakh | ❌ | ![MIT][license-mit] |
| [Supertonic 3](#supertonic-3) | ✅ | ❌ | 31 | ✅ | ![OpenRAIL-M][license-openrail-m] |
| [Scenema Audio](#scenema-audio) | ✅ | ❌ | English, German, French, Spanish, Italian, Portuguese, Japanese, Chinese, Korean, Russian, Arabic, Hindi, Swahili | ❌ | ![Unknown][license-unknown] |
| [Dramabox](#dramabox) | ✅ | ❌ | English | ❌ | ![Unknown][license-unknown] |
| [Sarashina2.2-TTS](#sarashina22-tts) | ✅ | ❌ | Japanese, English | ❌ | ![Research Only][license-research-only] |
| [LongCat-AudioDiT](#longcat-audiodit) | ✅ | ❌ | Chinese, English | ❌ | ![MIT][license-mit] |
| [Fish Audio S2 Pro](#fish-audio-s2-pro) | ✅ | ❌ | 80+ | ✅ | ![Research Only][license-research-only] |
| [LongCat-Next](#longcat-next) | ✅ | ✅ | Chinese, English | ✅ | ![MIT][license-mit] |
| [Voxtral-4B-TTS](#voxtral-4b-tts) | ✅ | ❌ | 9 | ✅ | ![CC BY-NC 4.0][license-cc-by-nc-4.0] |
| [Blue (Light Blue) TTS](#blue-tts) | ✅ | ❌ | Hebrew, English, Spanish, Italian, German | ❌ | ![MIT][license-mit] |
| [KittenTTS](#kittenTTS) | ✅ | ❌ | English, Multiple | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Ming-omni-tts](#ming-omni-tts) | ✅ | ❌ | Chinese, English | ❌ | ![Apache 2.0][license-apache-2.0] |
| [SoulX-Singer](#soulx-singer) | ✅ | ❌ | Mandarin, English, Cantonese | ✅ | ![Apache 2.0][license-apache-2.0] |
| [SoproTTS](#soprotts) | ✅ | ❌ | English | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Qwen3-TTS](#qwen3-tts) | ✅ | ❌ | 10 | ✅ | ![Apache 2.0][license-apache-2.0] |
| [TADA](#tada-1b) | ❌ | ❌ | English | ❌ | ![Unknown][license-unknown] |
| [Irodori-TTS-500M-v2](#irodori-tts-500m-v2) | ✅ | ❌ | Japanese | ❌ | ![MIT][license-mit] |
| [KugelAudio](#kugelaudio) | ✅ | ❌ | 23 European languages | ✅ | ![MIT][license-mit] |
| [LEMAS-TTS](#lemas-tts) | ✅ | ❌ | 10 | ❌ | ![Apache 2.0][license-apache-2.0] |
| [MioTTS-2.6B](#miotts-26b) | ✅ | ❌ | English, Japanese | ✅ | ![LFM][license-lfm] |
| [MOSS-TTS-Nano](#moss-tts-nano) | ✅ | ❌ | 20 | ✅ | ![Apache 2.0][license-apache-2.0] |
| [NeuTTS](#neutts) | ✅ | ❌ | English, Spanish, German, French | ✅ | ![Apache 2.0][license-apache-2.0] |
| [OmniVoice](#omnivoice) | ✅ | ❌ | 600+ | ❌ | ![Apache 2.0][license-apache-2.0] |
| [T5Gemma-TTS](#t5gemma-tts) | ✅ | ❌ | English, Chinese, Japanese | ❌ | ![MIT][license-mit] |
| [TinyTTS](#tinytts) | ❌ | ❌ | English | ✅ | ![Apache 2.0][license-apache-2.0] |
| [VoxCPM2](#voxcpm2) | ✅ | ❌ | 30 | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Soprano](#soprano) | ❌ | ❌ | English | ✅ | ![Apache 2.0][license-apache-2.0] |
| [GLM-TTS](#glm-tts) | ✅ | ❌ | Chinese, English | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Echo-TTS](#echo-tts) | ✅ | ❌ | English | ❌ | ![MIT][license-mit] |
| [VibeVoice-Realtime](#vibevoice-realtime) | ✅ | ❌ | Multilingual | ✅ | ![MIT][license-mit] |
| [Fun-CosyVoice 3.0](#fun-cosyvoice-30) | ✅ | ❌ | 9 + 18+ Chinese dialects | ✅ | ![Apache 2.0][license-apache-2.0] |
| [LFM2-Audio-1.5B](#lfm2-audio-15b) | ✅ | ✅ | English | ✅ | ![LFM][license-lfm] |
| [Marvis-TTS](#marvis-tts) | ✅ | ❌ | English, French, German | ✅ | ![Apache 2.0][license-apache-2.0] |
| [IndexTTS2](#indextts2) | ✅ | ❌ | Chinese, English | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Maya1](#maya1) | ✅ | ❌ | English | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Step-Audio-EditX](#step-audio-editx) | ✅ | ❌ | Mandarin, English, Sichuanese, Cantonese, Japanese, Korean | ✅ | ![Apache 2.0][license-apache-2.0] |
| [KaniTTS](#kani-tts) | ❌ | ❌ | English, German, Chinese, Korean, Arabic, Spanish | ✅ | ![LFM][license-lfm] |
| [VibeVoice-Finetuning](#vibevoice-finetuning) | ❌ | ❌ | — | ❌ | ![MIT][license-mit] |
| [VoxCPM](#voxcpm) | ✅ | ❌ | Chinese, English | ✅ | ![Apache 2.0][license-apache-2.0] |
| [FireRedTTS2](#fireredtts2) | ✅ | ❌ | EN, ZH, JP, KO, FR, DE, RU | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Audio Flamingo 3 (AF3) / Audio Flamingo Next](#audio-flamingo-3) | ❌ | ✅ | Multi-lingual | ✅ | ![Apache 2.0][license-apache-2.0] |
| [ZipVoice](#zipvoice) | — | — | Chinese, English | — | ![Apache 2.0][license-apache-2.0] |
| [Fish Speech](#fish-speech) | ✅ | ❌ | 8 | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Chatterbox](#chatterbox) | ✅ | ❌ | 23+ | ❌ | ![MIT][license-mit] |
| [Orpheus-TTS](#orpheus-tts) | ✅ | ❌ | Multilingual | ✅ | ![Apache 2.0][license-apache-2.0] |
| [MegaTTS3](#megatts3) | ✅ | ❌ | Chinese, English | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Spark-TTS](#spark-tts) | ✅ | ❌ | Chinese, English | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Step-Audio](#step-audio) | ✅ | ✅ | Chinese, English, Japanese | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Kokoro-82M](#kokoro-82m) | ✅ | ❌ | 8 | ✅ | ![Apache 2.0][license-apache-2.0] |
| [KokoClone](#kokoclone) | ✅ | ❌ | 7 | ✅ | ![Apache 2.0][license-apache-2.0] |
| [LuxTTS](#luxtts) | ✅ | ❌ | - | ✅ | ![Apache 2.0][license-apache-2.0] |
| [MiMo-Audio](#mimo-audio) | ✅ | ✅ | Multi-lingual | ✅ | ![Apache 2.0][license-apache-2.0] |
| [SoulX-Podcast](#soulx-podcast) | ✅ | ❌ | Mandarin, English, Cantonese, Sichuanese, Henanese | ✅ | ![Apache 2.0][license-apache-2.0] |
| [VieNeu-TTS](#vieneu-tts) | ✅ | ❌ | Vietnamese | ✅ | ![Apache 2.0][license-apache-2.0] |
| [Dia](#dia) | ✅ | ❌ | English | ✅ | ![Apache 2.0][license-apache-2.0] |
| [MeloTTS](#melotts) | ❌ | ❌ | English, Spanish, French, Chinese, Japanese, Korean | ❌ | ![MIT][license-mit] |
| [Kimi-Audio](#kimi-audio) | ✅ | ✅ | Multi-lingual | ✅ | ![MIT][license-mit]<br>![Apache 2.0][license-apache-2.0] |
| [eSpeak-NG](#espeak-ng) | ❌ | ❌ | 100+ | ✅ | ![Unknown][license-unknown] |

<!-- MODEL:audio8-tts-preview-0-6b.md -->
<details id="audio8-tts-preview-0-6b">
<summary>Audio8-TTS-Preview-0.6b</summary>

### Audio8-TTS-Preview-0.6b

**Description:** **Audio8 TTS Preview 0.6B** is a 0.6B-parameter multilingual text-to-speech model with **zero-shot voice cloning**. It uses a **DualAR architecture** inspired by [Fish Audio S2 Pro](https://fishaudio/fish-speech): a **slow AR transformer** predicts one semantic token per audio frame, and a **fast AR transformer** predicts the frame's codec codebooks conditioned on the slow hidden state and preceding codebooks. The bundled **44.1 kHz neural audio codec** handles both reference-audio encoding and waveform decoding — no additional codec checkpoint is required. The model supports **11 recommended languages** (Cantonese, Chinese, Dutch, English, French, German, Italian, Japanese, Korean, Polish, Spanish) with zero-shot voice cloning from a reference audio clip + matching transcript.

**Release Date:** July 28, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 601,159,424 (0.6B, excluding the codec) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Languages** | Cantonese, Chinese, Dutch, English, French, German, Italian, Japanese, Korean, Polish, Spanish (11) |
| **Streaming** | ❌ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Architecture** | DualAR (slow AR + fast AR), inspired by Fish Audio S2 Pro |
| **Slow Ar** | 24 layers, width 896, 14 attention heads, 2 KV heads |
| **Fast Ar** | 4 layers, width 896, 14 attention heads, 2 KV heads |
| **Acoustic Tokens** | 10 codebooks, 4,096 entries per codebook |
| **Codec** | 44.1 kHz, 2,048 samples per model frame (~21.5 frames/s), bundled (no external codec needed) |
| **Context Length** | up to 2,048 packed text/audio positions |
| **Sample Rate** | 44,100 Hz |
| **Inference** | transformers with trust_remote_code=True; CUDA-capable GPU recommended |
| **Dependencies** | torch>=2.5.0, torchaudio>=2.5.0, transformers>=4.57.0,<5, soundfile, safetensors |
| **Preview Status** | language coverage intentionally limited; broader multilingual + Chinese dialect support planned |
| **Library Name** | transformers (custom_code) |
| **Pipeline Tag** | text-to-speech |
| **Createdat** | 2026-07-28T07:53:00Z |

**Features:** The DualAR architecture is the technical centerpiece: rather than
a single autoregressive decoder predicting all codebook levels
sequentially (the standard codec-LLM TTS pattern), Audio8 splits
the work into a **slow AR** that predicts one semantic token per
audio frame and a **fast AR** that predicts the frame's remaining
codec codebooks conditioned on the slow hidden state. This
separation lets the semantic-level reasoning happen at the slow
AR's 24-layer depth while the acoustic codebook prediction stays
lightweight at 4 layers — reducing the total compute per frame
without sacrificing semantic quality. The **bundled 44.1 kHz
codec** (no external codec checkpoint needed) and the 10-codebook
/ 4,096-entry acoustic token design give the model self-contained
high-fidelity output at a compact 0.6B scale, making it one of
the smallest multilingual zero-shot-cloning TTS systems shipping
at 44.1 kHz.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/Audio8/Audio8-TTS-Preview-0.6b)
[![GitHub][link-github]](https://Audio8-AI/Audio8_TTS)
[![Website][link-website]](https://audio8-ai.github.io/Audio8_TTS/)

</details>
<!-- /MODEL:audio8-tts-preview-0-6b.md -->
<!-- MODEL:neutts-2e.md -->
<details id="neutts-2e">
<summary>NeuTTS-2E</summary>

### NeuTTS-2E

**Description:** **NeuTTS-2E** is a super-fast, highly realistic, **on-device** emotional text-to-speech model from Neuphonic. It is the next generation after **NeuTTS Air / Nano** (which continue to ship for multilingual + zero-shot-cloning contexts) — narrowed in scope to an **English-only alpha** focused on:

**Release Date:** July 21, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 0.2B (compact LM backbone + codec) |
| **Voice Cloning** | ❌ |
| **Asr** | ❌ |
| **Languages** | English (English-only alpha) |
| **Streaming** | ✅ |
| **License** | ![Unknown][license-unknown] |
| **Backbone** | compact LM backbone tuned for emotional TTS token generation |
| **Codec** | efficient codec (compact, paired with the LM) |
| **Speakers** | 4 fixed (`emily`, `paul`, `sophie`, `steven`) |
| **Emotions** | 6 + neutral (`angry`, `disgusted`, `fearful`, `happy`, `sad`, `surprised`, `neutral`) |
| **Emotion Control Mode** | single-argument selection (no composable multi-axis axes like Scylla's Band) |
| **Input Format** | text only — no phonemizer, no system dependencies |
| **On Device** | yes (laptop-class CPU real-time / better-than-real-time) |
| **Distribution Formats** | safetensors (torch), Q4 GGUF, Q8 GGUF |
| **Formats In Collection** | `neuphonic/neutts-2e` (safetensors), `neuphonic/neutts-2e-q4-gguf` (smallest footprint), `neuphonic/neutts-2e-q8-gguf` (mid-tier compression) |
| **Gguf Features** | imatrix, conversational, endpoints_compatible |
| **Pipeline Tag** | text-to-speech |
| **Library Name** | (HF tag does not declare transformers / safetensors stem beyond safetensors itself) |
| **Downloads** | 194 / 241 / 216 (torch / q4 / q8) |
| **Intended Use** | embedded voice agents, on-device assistants, toys, privacy-sensitive applications |
| **Comparison With Air Nano** | Air/Nano continue to ship for zero-shot cloning + multilingual contexts; 2E is the next-gen focused English emotional variant |
| **Safety Note** | model is alpha; legitimate project landing is `neuphonic.com` (not `neutts.com`) |

**Features:** The technical center of NeuTTS-2E is *maximum speed per parameter*
at on-device budgets — the 0.2B LM + codec pair delivers
**real-time-or-better on laptop-class CPUs** while exposing
**discrete categorical emotion control** (`angry` / `disgusted` /
`fearful` / `happy` / `sad` / `surprised` / `neutral`) plus a
**fixed four-speaker cast** for consistency in agent / toy /
accessibility voice personas. Two design choices distinguish it from
the surrounding TTS field:

First, the **categorical emotion surface is single-axis and
discrete** (one emotion per call), not the continuous multi-axis
composable vector surface used by models like Scylla's Band
([neurotica base + 6-axis continuous strengths]). The project's
positioning — production-grade agents + toys + accessibility —
benefits from a one-argument API where `emotion="happy"` is the
explicit operational state. The release locks emotional mode at
generation time, which simplifies downstream filtering / guardrails.

Second, the **distribution-shape design** (one model, three
deployment formats) is a deliberate on-device-first posture: the
`safetensors` torch build for max-quality GPU/server; `Q8 GGUF` for
mid-tier compression; `Q4 GGUF` for the small-footprint embedded
target. All three are direct llama.cpp-compatible drops of the
same model — no retraining-per-format — letting users pick size vs
quality at deployment time without changing the production API.
The combined CPU-first + GGUF-first design pattern is the
opposite of the cloud-first TTS systems in this list — and is what
makes 2E suitable for embedded voice agents, toys, and
privacy-sensitive applications where audio + text must remain
on-device.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/neuphonic/neutts-2e)
[![GitHub][link-github]](https://neuphonic/neutts)
[![Demo][link-demo]](https://huggingface.co/spaces/neuphonic/neutts-2e)
[![Collection][link-collection]](https://huggingface.co/collections/neuphonic/neutts-2e)

</details>
<!-- /MODEL:neutts-2e.md -->
<!-- MODEL:scyllasband.md -->
<details id="scyllasband">
<summary>Scylla's Band</summary>

### Scylla's Band

**Description:** **Scylla's Band** is a multilingual, multi-voice, **expressive** TTS model from Spybyscript, designed specifically for **local and self-hosted inference** through ONNX Runtime (with an experimental LiteRT backend for explicit native / mobile use). The architecture is a continuous-latent TTS family:

**Release Date:** July 19, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | not stated (architecture: 4-layer duration predictor (192 hidden) + 12-layer rectified-flow acoustic generator (512 hidden, AdaLN, QK norm)) |
| **Voice Cloning** | ❌ |
| **Asr** | ❌ |
| **Languages** | en_us, en_gb, es, it (4 public text-input languages) |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Sample Rate** | 24,000 Hz |
| **Managed Voices** | 10 (ariadne, felix, gwen, ink, max, orpheus, rex, scylla, stone, tuesday) |
| **Voice Default Locale** | en_us for most; ink / orpheus / tuesday default to en_gb |
| **Voice Style Dim** | 128 (style features) + 32 (prosody features) |
| **Affect Axes** | 6 (calm, joy, anger, sadness, sarcasm, questioning — all continuous in `[0, 1]`) |
| **Affect Overlay Axes** | sarcasm, questioning (mixable with any core delivery) |
| **Affect Cfg Scope** | duration + acoustic-flow prediction (preserves voice / reference) |
| **Encoders Default** | ONNX Runtime (Python CLI / Python API / Android sample / `libscyllasband` native) |
| **Encoders Experimental** | LiteRT (experimental / explicit-selection) |
| **Cli Quality Default** | 8-step Heun sampling |
| **Graph Budgets** | 512 G2P text tokens / 512 phone frames / 640 latent frames |
| **Latent Target Buckets** | 256 / 384 / 512 / 640 (smallest-fit selection) |
| **Vocoder** | Scylla's Band acoustic adapter + frozen `charactr/vocos-mel-24khz` |
| **Hop Lengths** | 256 (waveform) / 512 (latent) |
| **Text Frontend** | phrase-level multilingual G2P (74-phone vocabulary) |
| **Span Context** | 3 segments over up to 768 phones with 512-dim context state |
| **Prefix Context** | up to 24 acoustic latent frames from preceding chunk |
| **Long Form Features** | boundary metadata + punctuation pause floors + prefix-latent carryover + span context |
| **Group Speak Input** | `[voice]`, `[voice:language]`, `[voice:language:axis=value,...]` annotations |
| **Bundle Contract** | 1.0.0 / `scyllasband-duration-flow` |
| **Intended Use** | single-voice speech synthesis (10 voices); en/es/it; long-form narration; multi-voice dialogue from tagged text; continuous affect control; ONNX desktop/server; ONNX + LiteRT native/mobile |
| **Not Intended** | arbitrary-speaker cloning / impersonation / fraud / deceptive speech |
| **Distributions** | training data, trainer checkpoints, and export tooling not distributed |
| **Cli Commands** | download, validate-bundle, list-voices, normalize-text, speak, group-speak, stream, plan |
| **Library Name** | onnxruntime (tags include onnx, tflite, litert, duration-flow) |

**Features:** Three design decisions distinguish Scylla's Band in the multilingual
TTS class. First, **decoupling duration and acoustic flow as
separate rectified-flow stages** — duration is a 192-hidden, 4-layer
predictor operating on a 512-phone window, acoustic latents a
512-hidden, 12-layer AdaLN / QK-norm generator at 24-dim. This split
lets affect-CFG act on **both** stages independently while retaining
voice / reference conditioning, supporting the 6-axis continuous
composability. Second, **6 affect axes** (with `sarcasm` and
`questioning` as overlays mixed with any core delivery) instead of
mutually-exclusive discrete emotion classes — `calm=0.5, joy=0.5` is
a valid input, and axes stay in `[0, 1]` so multi-axis states are
expressible without combinatorial blow-up. Third, the **ONNX-first
runtime** design with `libscyllasband` native + an experimental
LiteRT backend sits at a budget most neural TTS systems don't
target — the 8-step Heun default and 512/512/640 fixed graph budget
keep the model usable on CPU and mobile, and the inference-only
release surface (training data + checkpoints not distributed) is the
complement of the latency / mobile inference focus.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/spybyscript/scyllasband)
[![GitHub][link-github]](https://lowkeytea/scyllasband)
[![Website][link-website]](https://lowkeytea.github.io/scyllasband/)

</details>
<!-- /MODEL:scyllasband.md -->
<!-- MODEL:sanotts.md -->
<details id="sanotts">
<summary>sanoTTS</summary>

### sanoTTS

**Description:** **sanoTTS** is the smallest known neural text-to-speech family. The name *sano* (सानो) is Nepali for **"small"**. Each voice weighs **745k to 1.8M parameters** — smaller than the smallest voice in prior families (TinyTTS at 1.62M; Inflect Nano at 4.63M; Kokoro at 82M) and the family fits in **under 4 MB per voice** with zero runtime dependencies (the espeak-ng phonemizer is bundled). Voices run **real-time on a ~$3 ESP32-S3 microcontroller** (output through a GPIO into an LM386 and a speaker) and **live in the browser via WebAssembly** — no server, no upload, no NPU. The full neural stack is **duration → acoustic → decoder**, quantized to int8, with the espeak-ng phonemizer included. **9 voices** across **6 languages** ship: English (4 voices — including a 745k on-device "robot" voice), Nepali, Hindi, Vietnamese, Indonesian, and Chinese. The project page at [ampixa.github.io/sanoTTS](https://ampixa.github.io/sanoTTS/) hosts a live browser synthesis demo for every voice.

**Release Date:** July 13, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 745k–1.8M per voice (smallest = the 745k on-device "robot" voice) |
| **Voice Cloning** | ❌ |
| **Asr** | ❌ |
| **Languages** | English, Nepali, Hindi, Vietnamese, Indonesian, Chinese (6 languages, 9 voices) |
| **Streaming** | ❌ |
| **License** | ![Unknown][license-unknown] |
| **Architecture** | full neural stack — duration model → acoustic model → decoder |
| **Quantization** | int8 |
| **Runtime Microcontroller** | ESP32-S3 (real-time, GPIO → LM386 → speaker) |
| **Runtime Browser** | WebAssembly (no server, no upload, no NPU) |
| **Runtime Footprint** | under 4 MB per voice, zero dependencies |
| **Voices** | 9 (English: amy / kristin / hfc / amy-small / robot; one voice each for NE / HI / VI / ID / ZH) |
| **Phonemizer** | espeak-ng (bundled) |
| **Library Name** | sanotts |
| **Training Method** | distillation (per voice) |

**Features:** The hard constraint — be the smallest neural TTS family known,
real-time on a $3 microcontroller — drives the entire stack.
Conventional sub-100M TTS systems are too large for an ESP32's flash
and RAM. sanoTTS keeps the full **duration → acoustic → decoder**
neural pipeline (no espeak-NG-only fallback, no concatenative
hybrid), quantizes everything to int8, and *bundles the phonemizer*
so the whole voice ships in under 4 MB with zero runtime dependencies.
The result is a per-voice footprint 100× smaller than Kokoro and
2× smaller than TinyTTS while still scoring competitively on the
authors' SCOREQ / UTMOS / DNSMOS-SIG no-reference 24-sentence harness
— and the demo synthesizes every voice **live in the browser via
WASM**, so the smallest-known neural TTS is also the only one that
runs unattended on a $3 chip and a $0 web page.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/ampixa/sanoTTS)
[![GitHub][link-github]](https://Ampixa/sanoTTS)
[![Website][link-website]](https://ampixa.github.io/sanoTTS/)

</details>
<!-- /MODEL:sanotts.md -->
<!-- MODEL:freyatts.md -->
<details id="freyatts">
<summary>FreyaTTS</summary>

### FreyaTTS

**Description:** **FreyaTTS** is a 183M-parameter Turkish text-to-speech model. It is **tokenizer-free at the character level** — 92 symbols in its Turkish vocabulary — so there is no phonemizer or G2P step in either training or inference. Speech is generated with a **non-autoregressive conditional flow-matching DiT** in the frozen [AudioVAE2](https://huggingface.co/openbmb/VoxCPM2) latent space (25 Hz, 64-dim latents, 16 kHz encode / 48 kHz decode). Training runs from scratch on Turkish speech: a pretraining stage followed by SFT stage 1/2 for voice lock and short-utterance coverage. Output is 48 kHz mono. On the project's Freya-TR-Eval benchmark the model reports **WER 8.0% / CER 3.0%**, ranking 3rd of 7 among open sub-1B Turkish TTS systems — a deliberate **single-target-speaker, no-cloning** design choice for a focused foundation release. The evaluation dataset is [freya-tr-eval](https://huggingface.co/datasets/freyavoice/freya-tr-eval).

**Release Date:** July 7, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 183.2M |
| **Voice Cloning** | ❌ |
| **Asr** | ❌ |
| **Languages** | Turkish (tr) |
| **Streaming** | ❌ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Architecture** | conditional flow-matching diffusion transformer (DiT), non-autoregressive, 32-step Euler ODE, no CFG |
| **Tokenizer** | character-level (92 Turkish symbols; no phonemizer, no G2P) |
| **Latent Space** | frozen AudioVAE2 (Apache-2.0, openbmb/VoxCPM2), 64-dim at 25 Hz |
| **Codec Io** | 16 kHz encode / 48 kHz decode |
| **Sample Rate** | 48,000 Hz |
| **Training** | from scratch on Turkish speech; pretraining + SFT stage 1/2 (voice lock + short-utterance coverage) |
| **Evaluation** | Freya-TR-Eval — WER 8.0% / CER 3.0%, 3rd of 7 open sub-1B Turkish TTS |
| **Library Name** | freyatts |

**Features:** Two design choices are worth flagging. First, **tokenizer-free
character-level Turkish**: by training directly on the 92-symbol
Turkish alphabet with no phonemizer or G2P grapheme-to-phoneme step,
the model removes a dependency that is fragile for agglutinative
Turkish morphology and that often degrades quality when ported to
low-resource Turkic relatives. Second, **non-autoregressive
conditional flow-matching in a frozen AudioVAE2 latent space**:
the 25 Hz / 64-dim bottleneck keeps the DiT small (183M) while
inheriting a separately-trained audio codec's representation,
letting a focused single-language-non-multilingual release ship at
a fraction of the parameter budget of multilingual foundation TTS
systems. The deliberate "no cloning, single target speaker" choice
is a scope-lowering move that lets the foundation release put all
its capacity into Turkish speech quality rather than spread it
across zero-shot speaker adaptation.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/freyavoice/Freya-TTS)
[![GitHub][link-github]](https://freyavoiceai/FreyaTTS)
[![Paper][link-paper]](https://arxiv.org/abs/2607.09530)

</details>
<!-- /MODEL:freyatts.md -->
<!-- MODEL:inflect-nano-v2.md -->
<details id="inflect-nano-v2">
<summary>Inflect-Nano-v2</summary>

### Inflect-Nano-v2

**Description:** **Inflect-Nano-v2** is a complete local text-to-waveform speech synthesis model with **3,966,721 deployable parameters** — under 4M total. It is a **VITS**-architecture fixed-voice English TTS designed for **CPU or CUDA inference** with deterministic seeds, long-text handling, and **24 kHz mono output**. The full FP32 checkpoint is **15.97 MB**, making it one of the smallest complete neural TTS systems that produces natural-sounding speech without a separate vocoder or phonemizer dependency. The model ships with a public **adaptation toolkit** for preparing data, auditing train/validation splits, adapting a fixed voice or language, resuming training, evaluating checkpoints, and exporting PyTorch or ONNX packages. A sibling **Inflect-Micro-v2** (9.36M parameters) prioritizes quality below 10M; Nano prioritizes footprint below 4M. Both share one public API.

**Release Date:** June 25, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 3,966,721 (3.97M deployable) |
| **Voice Cloning** | ❌ |
| **Asr** | ❌ |
| **Languages** | English |
| **Streaming** | ❌ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Architecture** | VITS (end-to-end text-to-waveform) |
| **Sample Rate** | 24,000 Hz |
| **Footprint** | 15.97 MB FP32 |
| **Inference** | CPU or CUDA; PyTorch + ONNX export |
| **Determinism** | deterministic seeds for reproducible generation |
| **Long Text** | automatic text splitting and handling |
| **Input Format** | text (no phonemizer or system dependencies) |
| **Adaptation Toolkit** | data prep, split auditing, voice/language adaptation, training resume, checkpoint eval, PyTorch/ONNX export |
| **Sibling Model** | Inflect-Micro-v2 (9.36M params, quality-prioritized below 10M) |
| **Api** | one public API across Micro and Nano sizes |
| **Library** | pytorch |
| **Metrics** | WER |
| **Inference False On Hf** | yes (no hosted HF inference endpoint; local-only) |

**Features:** Inflect-Nano-v2's defining constraint is **completeness under 4M
parameters**: the entire text-to-waveform pipeline — no separate
vocoder, no phonemizer, no system dependencies — fits in 3.97M
deployable parameters and a 15.97 MB FP32 checkpoint. This is
smaller than even sanoTTS's smallest voice (745k) when measured
by *complete-pipeline* footprint, though sanoTTS ships per-voice
weights rather than a single fixed-voice checkpoint. The VITS
end-to-end architecture is the enabler: by folding the acoustic
model and vocoder into a single jointly-trained network, Inflect
avoids the multi-stage pipeline overhead that makes most neural
TTS systems larger. The public **adaptation toolkit** extends the
fixed-voice design into a customizable platform — users can
prepare data, adapt a voice or language, resume training, and
export PyTorch or ONNX packages — making the 4M-parameter
footprint a starting point for domain-specific TTS rather than a
dead-end fixed-voice release.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/owensong/Inflect-Nano-v2)
[![GitHub][link-github]](https://owenawsong/Inflect)
[![Demo][link-demo]](https://huggingface.co/spaces/owensong/Inflect-v2)

</details>
<!-- /MODEL:inflect-nano-v2.md -->
<!-- MODEL:gepard.md -->
<details id="gepard">
<summary>Gepard</summary>

### Gepard

**Description:** **GE**nerative, **P**rosody-aware, **A**utoregressive text-to-speech model for **R**ealtime **D**ialogue. Gepard is built for low-latency, high-throughput streaming conversation: the model starts speaking the moment text begins arriving, generating audio piece by piece instead of waiting for a full sentence. It is a single decoder-only autoregressive language model built on Qwen3.5 (14 layers, hidden 1024, 8 heads) with ≈556M total parameters (backbone + audio interface + voice-cloning compressor). Audio is produced through NVIDIA NeMo NanoCodec — Finite Scalar Quantization at 22.05 kHz, 21.5 frames/s, 1.89 kbps — with the full 32-channel FSQ frame sampled in one step. Reports ~25× real time on a single RTX 5090 with first-audio-chunk latency around 50 ms; a 96 GB Blackwell card serves up to 256 concurrent conversations. CFG refinement is baked into the weights so quality gain comes at no extra two-pass cost at inference, though the two-pass mode is still selectable as a quality dial.

**Release Date:** June 22, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | ~556M (Qwen3.5-14 backbone + audio interface + voice-cloning compressor) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ❌ |
| **Languages** | English (US/UK), Spanish (es-MX), Portuguese (pt-BR), Dutch (NL) |
| **Streaming** | ✅ |
| **License** | ![Research Only][license-research-only] |
| **Audio Codec** | NVIDIA NeMo NanoCodec (FSQ, 22.05 kHz, 21.5 fps, 1.89 kbps) |
| **Sample Rate** | 22,050 Hz |
| **Backbone** | Qwen3.5 full-attention transformer (14 layers, hidden 1024, 8 heads; ~500M params) |
| **Inference** | vLLM |
| **Throughput** | 256 conversations on one 96 GB Blackwell (RTX Pro 6000) GPU |

**Features:** A prosody-aware autoregressive single-pass frame generator: the whole
32-channel FSQ audio frame is sampled in one step (no depth transformer),
and CFG quality refinement is **baked into the weights** rather than
incurred at inference as a two-pass cost — so the publicly reported TTFA
of ~50 ms and 25× real time on a single RTX 5090 represent the
quality-on path, not a cheap-fast preview. Voice cloning is decoupled
into a separate up-front compressor, which means cloning is "free" at
run-time once the reference clip is encoded — a structural choice that
supports serving hundreds of conversations per GPU.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/nineninesix/gepard-1.0)
[![Demo][link-demo]](https://huggingface.co/spaces/nineninesix/gepard)
[![Paper][link-paper]](https://huggingface.co/nineninesix/gepard-1.0/resolve/main/gepard_techreport.pdf)
[![Website][link-website]](https://www.nineninesix.ai/)

</details>
<!-- /MODEL:gepard.md -->
<!-- MODEL:higgs-audio-v3-tts.md -->
<details id="higgs-audio-v3-tts">
<summary>Higgs Audio v3 TTS</summary>

### Higgs Audio v3 TTS

**Description:** Boson AI's flagship conversational TTS: an ~4B autoregressive decoder over interleaved text and audio tokens from the Higgs Tokenizer (8 codebooks at 25 fps / 24 kHz). Built for voice chat rather than narration, it covers 102 languages with zero-shot voice cloning and inline control over emotion, style, prosody, pauses, and sound effects.

**Release Date:** June 4, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 4B (BF16, 36 layers, hidden=2560, GQA 32/8) |
| **Architecture** | Autoregressive decoder (Qwen3-style) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | 102 (85 with WER/CER <5, 17 between 5-10) |
| **Streaming** | ✅ |
| **Audio Output** | 24 kHz |
| **License** | ![Research Only][license-research-only] |

**Features:** Interleaved text/audio token modelling with a delay-pattern multi-codebook embedding/head: a single autoregressive stack emits both modalities and supports inline `<|category:value|>` control tags (emotion/style/sfx/prosody) inserted at any point in the target text.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)
[![GitHub][link-github]](https://sgl-project/sglang-omni)
[![Blog][link-blog]](https://www.boson.ai/blog/higgs-audio-v3-tts)
[![Demo][link-demo]](https://huggingface.co/spaces/multimodalart/higgs-audio-v3-tts)

</details>
<!-- /MODEL:higgs-audio-v3-tts.md -->
<!-- MODEL:dots-tts.md -->
<details id="dots-tts">
<summary>dots.tts</summary>

### dots.tts

**Description:** dots.tts is a 2B-parameter fully continuous, end-to-end autoregressive TTS system from Rednote-HiLab. The backbone pairs a semantic encoder, an LLM, and an autoregressive flow-matching acoustic head over a 48 kHz AudioVAE, with no discrete tokens anywhere in the pipeline. It achieves the best average performance on Seed-TTS-Eval (WER 0.94 / 1.30 / 6.60 on zh / en / zh-hard) and the highest speaker similarity on a 24-language MiniMax multilingual benchmark, with broad cross-lingual voice cloning.

**Release Date:** June 3, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 2B (semantic encoder + LLM + AR flow-matching acoustic head) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Languages** | Multilingual (24+ languages; zh / en focus) |
| **Streaming** | ❌ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Sample Rate** | 48 kHz |
| **Tokenizer** | 48 kHz AudioVAE (continuous, no discrete tokens) |

**Features:** A fully continuous autoregressive pipeline that keeps generation in waveform-latent space end-to-end (no discrete-code phase), pairing an LLM-side semantic encoder with an autoregressive flow-matching acoustic head over a 48 kHz AudioVAE — yielding SOTA seed-TTS-Eval scores and the strongest speaker-similarity number (83.9 avg) on the 24-language MiniMax multilingual benchmark.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/rednote-hilab/dots.tts-base)
[![GitHub][link-github]](https://rednote-hilab/dots.tts)
[![Website][link-website]](https://rednote-hilab.github.io/dots.tts-demo/)
[![Demo][link-demo]](https://huggingface.co/spaces/rednote-hilab/dots.tts)

</details>
<!-- /MODEL:dots-tts.md -->
<!-- MODEL:confucius4-tts.md -->
<details id="confucius4-tts">
<summary>Confucius4-TTS</summary>

### Confucius4-TTS

**Description:** Confucius4-TTS is an LLM-based text-to-speech system from NetEase Youdao designed for multilingual and cross-lingual synthesis. It uses a speech encoder + LLM (Text2Semantic) + flow-matching Semantic2Acoustic architecture that allows zero-shot voice cloning without a required reference transcript and explicit cross-lingual voice transfer with unaccented output across languages. Covers Chinese, English, Japanese, Korean, German, French, Spanish, Indonesian, Italian, Thai, Portuguese, Russian, Malay, and Vietnamese with code-switching and emotion transfer.

**Release Date:** June 2, 2026

| Feature | Value |
|---------|-------|
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | 14 (zh, en, ja, ko, de, fr, es, id, vi, th, pt, it, ru, ms) |
| **Streaming** | ❌ |
| **License** | ![Unknown][license-unknown] |
| **Architecture** | speech encoder + LLM (T2S) + flow-matching head (S2A) |

**Features:** Cross-lingual voice transfer without accent drift: the same reference voice stays consistent when the speaker switches languages — backed by a speech encoder + LLM backbone pipeline (T2S) with a flow-matching acoustic decoder (S2A) and training that bundles 14 languages with code-switched, emotion-preserving decoding.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/netease-youdao/Confucius4-TTS)
[![GitHub][link-github]](https://netease-youdao/Confucius4-TTS)
[![Demo][link-demo]](https://confucius4-tts.youdao.com/gradio)

</details>
<!-- /MODEL:confucius4-tts.md -->
<!-- MODEL:wavtts.md -->
<details id="wavtts">
<summary>WavTTS</summary>

### WavTTS

**Description:** WavTTS is an end-to-end zero-shot TTS framework that synthesizes speech directly in the raw waveform space — explicitly skipping the intermediate mel-spectrogram, VAE-latent, or codec-token representations that most modern TTS stacks use. It is built on a flow-matching diffusion transformer (DiT) with waveform patchification, multi-scale mel-spectrogram supervision, and an optimized noise schedule. Forked from F5-TTS at the codebase level but replaces the whole acoustic pipeline.

**Release Date:** May 28, 2026

| Feature | Value |
|---------|-------|
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Languages** | English, Chinese |
| **Streaming** | ❌ |
| **License** | ![CC BY-NC 4.0][license-cc-by-nc-4.0]<br>![MIT][license-mit] |
| **Sample Rate** | 16 kHz |
| **Training Data** | Emilia |
| **Architecture** | Flow-matching DiT, raw waveform patchification, multi-scale mel supervision |
| **Training Steps** | 1.2M |

**Features:** Skip every intermediate waveform representation (no mel, no VAE, no codec tokens): a flow-matching DiT produces raw-waveform patches directly, supervised at multiple mel scales and an optimized noise schedule — yielding high-quality zero-shot TTS at 16 kHz from a single end-to-end stack.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/worstchan/WavTTS)
[![GitHub][link-github]](https://cwx-worst-one/WavTTS)
[![Demo][link-demo]](https://wavtts.github.io/)
[![Paper][link-paper]](https://arxiv.org/abs/2606.03455)

</details>
<!-- /MODEL:wavtts.md -->
<!-- MODEL:moss-tts.md -->
<details id="moss-tts">
<summary>MOSS-TTS</summary>

### MOSS-TTS

**Description:** MOSS-TTS is a production-grade Text-to-Speech foundation model developed by the OpenMOSS Team and MOSI.AI. The current public v1.5 release preserves the original 1.0 capabilities — zero-shot voice cloning, long-form speech generation, token-level duration control, Pinyin/IPA pronunciation supervision, multilingual synthesis, and code-switching — and extends multilingual continued training from 20 languages to **31 languages** including Cantonese, Dutch, Finnish, Hindi, Macedonian, Malay, Romanian, Swahili, Tagalog, Thai, and Vietnamese. v1.5 improves speaker similarity, reduces cloning variance on long-reference / short-text scenarios, follows punctuation-driven prosody more reliably, and adds explicit inline pause markers (e.g., `[pause 3.2s]`).

**Release Date:** May 25, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 8B (Delay), 1.7B (Local) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | 31 (extended from v1.0's 20) |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Max Duration** | 1 hour |
| **Pause Control** | yes (inline markers like `[pause 3.2s]`) |
| **Lang Tag Control** | yes (set `language=` in user message) |

**Features:** v1.5 widens MOSS-TTS from 20 → 31 languages with stronger per-language multilingual synthesis (control via a language tag in the user message), more stable cloning under long-reference / short-text conditions, punctuation-driven prosody that holds up across long sentences, and explicit inline pause tokens (`[pause 3.2s]`) for scripted narration control.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-v1.5)
[![HuggingFace][link-huggingface]](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Local-Transformer-v1.5)
[![GitHub][link-github]](https://OpenMOSS/MOSS-TTS)
[![Website][link-website]](https://mosi.cn/#models)
[![Paper][link-paper]](https://arxiv.org/abs/2603.18090)
[![Demo][link-demo]](https://studio.mosi.cn)

</details>
<!-- /MODEL:moss-tts.md -->
<!-- MODEL:voxflash-tts.md -->
<details id="voxflash-tts">
<summary>VoxFlash-TTS</summary>

### VoxFlash-TTS

**Description:** **VoxFlash-TTS** is a zero-shot voice-cloning text-to-speech engine built around extreme latent compression. The VAE encodes 24 kHz waveforms into a **9 frames/s** latent space — roughly 8× more compressed than EnCodec (75 fps) and 2.4× more than Stable Audio (21.5 fps). Generating 10 s of audio therefore requires the diffusion model to produce just **90 latent vectors** rather than hundreds or thousands of tokens, with downstream quadratic savings in attention cost. A ConvNeXtV2-based phoneme encoder followed by a novel coarse-alignment algorithm (cheaper than cross-attention) maps text into the latent sequence; a modern diffusion head then iteratively refines speech latents that the lightweight VAE decoder renders back to waveforms. The architecture targets low-latency, low-resource deployment — consumer-grade GPUs and edge devices — with Chinese and English zero-shot cloning. The project card lists `inference: false` on HF (no hosted inference endpoint), but the project page at [voxflash.github.io](https://voxflash.github.io/) carries the abstract, demo examples, and ablations.

**Release Date:** May 22, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | not stated (ConvNeXtV2 phoneme encoder + diffusion head + lightweight VAE decoder) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Languages** | Chinese, English |
| **Streaming** | ❌ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Audio Codec** | VoxFlash VAE (9 Hz / 9 fps latent, 24 kHz input) |
| **Compression Ratio** | ~8× tighter than EnCodec (75 fps), ~2.4× tighter than Stable Audio (21.5 fps) |
| **Phoneme Encoder** | ConvNeXtV2 + coarse-alignment algorithm (no cross-attention) |
| **Diffusion Head** | modern multi-step iterative refinement |
| **Decoder** | lightweight VAE decoder |
| **Sample Rate** | 24,000 Hz |
| **Inference** | local CUDA ≥ 12.3.2; no HF hosted endpoint |
| **Training Dataset** | seed-tts-eval |
| **Metrics** | word_error_rate, speaker_similarity |

**Features:** The central technical move is **compressing the audio latent
space to 9 frames/s instead of the conventional 75 fps (EnCodec)
or 21.5 fps (Stable Audio)**. This is not a quantization tweak —
it is a temporal-decimation architectural choice that shrinks the
sequence length the diffusion model has to traverse, and because
attention cost scales quadratically with sequence length the
end-to-end compute drops by orders of magnitude. Combined with a
**coarse-alignment phoneme-to-latent map that avoids cross-attention
entirely** (using a ConvNeXtV2 phoneme encoder instead), VoxFlash
hits millisecond-level inference latency on consumer-grade and
edge hardware for zero-shot Chinese + English cloning, where
conventional latent-diffusion TTS systems are too slow for real-time
edge deployment.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/VoxFlashTTS/VoxFlashTTS)
[![GitHub][link-github]](https://VoxFlash/VoxFlashTTS)
[![Website][link-website]](https://voxflash.github.io/)
[![Paper][link-paper]](https://arxiv.org/abs/2406.02430)

</details>
<!-- /MODEL:voxflash-tts.md -->
<!-- MODEL:misotts.md -->
<details id="misotts">
<summary>Miso TTS</summary>

### Miso TTS

**Description:** Miso TTS 8B is a text-to-speech model from Miso Labs built on the Sesame Conversational Speech Model (CSM) architecture. A large Llama-3.2-style backbone consumes text/audio-frame embeddings and predicts codebook 0 of the Mimi audio token stream, while a smaller 300M autoregressive audio decoder predicts codebooks 1–31 in codebook depth. The model is designed for high-quality conversational speech and voice continuation from a short prompt audio clip.

**Release Date:** May 21, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 8B (backbone llama-3.2-style) + 300M (audio decoder) = 8.3B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Languages** | English |
| **Streaming** | ❌ |
| **License** | ![Unknown][license-unknown] |
| **Architecture** | Sesame-style CSM (two transformer stack: backbone + audio decoder) |
| **Audio Tokenizer** | Mimi (32 codebooks, vocab 2051, max seq 2048) |
| **Library** | pytorch |

**Features:** A two-transformer Sesame-style CSM (Llama 8B backbone consumes text + audio frames and produces backbone codebook-0 prediction; a 300M audio decoder autoregresses over codebook depth via Mimi's 32-codebook stack) — letting the larger backbone spend capacity on linguistic / speaker conditioning while a leaner decoder handles fine-grained codebook-by-codebook generation.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/MisoLabs/MisoTTS)
[![GitHub][link-github]](https://MisoLabsAI/MisoTTS)
[![Website][link-website]](https://misolabs.ai)

</details>
<!-- /MODEL:misotts.md -->
<!-- MODEL:oron-tts.md -->
<details id="oron-tts">
<summary>OronTTS</summary>

### OronTTS

**Description:** OronTTS is a non-autoregressive text-to-speech model from `btsee`, an F5-TTS fork specialized for Mongolian (Khalkha Cyrillic) and Kazakh (Cyrillic). It uses Flow Matching + Diffusion Transformer + Vocos (dim 1024, depth 22, 16 heads, vocab 65, 24 kHz sample rate), trained on the btsee/mbspeech_mn corpus (3,846 Mongolian speech samples) and outputs zero-shot synthesis from a short reference audio + language tag.

**Release Date:** May 16, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | (not stated) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Languages** | Mongolian (Khalkha Cyrillic), Kazakh (Cyrillic) |
| **Streaming** | ❌ |
| **License** | ![MIT][license-mit] |
| **Architecture** | F5-TTS (OT-CFM + DiT + Vocos) |
| **Dim** | 1024 |
| **Depth** | 22 |
| **Heads** | 16 |
| **Vocab Size** | 65 |
| **Sample Rate** | 24000 Hz |
| **Mel Bins** | 100 |
| **Training Data** | btsee/mbspeech_mn (3,846 Mongolian speech samples) |

**Features:** F5-TTS re-purposed for low-resource Cyrillic languages (Mongolian + Kazakh) — non-autoregressive flow-matching DiT over a tight 65-word vocab. Trained on a small (~3.8k sample) Mongolian corpus; the architecture is small enough that Khalkha Cyrillic and Kazakh Cyrillic share the same checkpoint via the `lang` tag at inference time.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/btsee/oron-tts)

</details>
<!-- /MODEL:oron-tts.md -->
<!-- MODEL:supertonic-3.md -->
<details id="supertonic-3">
<summary>Supertonic 3</summary>

### Supertonic 3

**Description:** Supertonic 3 is the third-generation open-weight release from Supertone. It is a lightweight, on-device text-to-speech system that runs with ONNX Runtime entirely on the user's machine (no network, no API call) and ships as a Python SDK (`pip install supertonic`). Compared with the Supertonic 2 base (5 languages, 66 M params), v3 expands to **31 languages** and adds expression tags (`<laugh>`, `<breath>`, `<sigh>`), more stable reading on long utterances, and higher speaker similarity across the core language set.

**Release Date:** May 6, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | (not stated on card; Supertonic 2 baseline 66 M — likely similar or smaller weight class) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | 31 (expanded from Supertonic 2's 5) |
| **Streaming** | ✅ |
| **License** | ![OpenRAIL-M][license-openrail-m] |
| **On Device** | yes (ONNX Runtime, no cloud call) |
| **Expression Tags** | yes (`<laugh>`, `<breath>`, `<sigh>`) |

**Features:** A more compact on-device multilingual TTS: ONNX-Runtime inference everywhere, 31 languages from a single small open-weight encoder, and discrete expression tags that the decoder interprets inline — without a separate speaker-emotion control path or a cloud-rendered audio round-trip.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/Supertone/supertonic-3)
[![GitHub][link-github]](https://supertone-inc/supertonic)
[![Demo][link-demo]](https://huggingface.co/spaces/Supertone/supertonic-3)
[![PyPI][link-pypi]](https://pypi.org/project/supertonic/)

</details>
<!-- /MODEL:supertonic-3.md -->
<!-- MODEL:scenema-audio.md -->
<details id="scenema-audio">
<summary>Scenema Audio</summary>

### Scenema Audio

**Description:** Scenema Audio is a zero-shot expressive voice cloning and speech generation model from ScenemaAI. It is built on an audio diffusion transformer extracted from the audio branch of Lightricks' LTX 2.3 (a 22B audiovisual model) — keeping the in-the-wild acoustic quality the bigger model learned while specializing for speech output. Generation is **prompt-driven**: a `<speak>` tag carries a `voice` description, `gender`, optional `scene` (ambient audio around the voice), and `language`; an `<action>` tag shifts emotional state mid-generation. Action tags cover rage, grief, joy, fear, exhaustion; voice prompt can describe timbre/pitch/breathiness/rasp/resonance plus character archetypes ("Tony Soprano having a breakdown"). Supports zero-shot voice cloning from 10-20 seconds of reference audio with some emotional variability, automatic long-form narration by splitting text and maintaining voice continuity, and 13 multilingual built-ins.

**Release Date:** April 26, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | (audio diffusion transformer of LTX 2.3, weights ~9.8 GB bf16 / ~4.9 GB INT8 + ~6.7 GB pipeline) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | 13 (en, de, fr, es, it, pt, ja, zh, ko, ru, ar, hi, sw) |
| **Streaming** | ❌ |
| **License** | ![Unknown][license-unknown] |
| **Parent Model** | Lightricks LTX-2.3 (audio branch) |
| **Prompt Format** | `<speak voice=… gender=… scene=… language=…>` XML with `<action>` tag for shifting emotion |
| **Long Form Narration** | yes (auto-splits text while preserving voice continuity) |
| **Quantized** | yes (INT8 weights at ~4.9 GB, identical quality) |

**Features:** A standalone audio diffusion transformer extracted from a much bigger multimodal source: the model inherits how people actually sound in real scenes (angry, laughing, whispering, crying, exhausted, terrified) and exposes that capacity through a `<speak>` + `<action>` prompt interface — emotional state shifts within a single generation, instead of being a token-level or speaker-level conditioning problem.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/ScenemaAI/scenema-audio)
[![GitHub][link-github]](https://ScenemaAI/scenema-audio)
[![Website][link-website]](https://scenema.ai/audio)

</details>
<!-- /MODEL:scenema-audio.md -->
<!-- MODEL:dramabox.md -->
<details id="dramabox">
<summary>Dramabox</summary>

### Dramabox

**Description:** Dramabox is Resemble AI's expressive TTS, distributed under the LTX-2 Community License. It is an IC-LoRA fine-tune of the LTX-2.3 3.3B audio-only branch (Diffusion Transformer + flow matching), conditioned on Gemma 3 12B text embeddings. Generation is **prompt-driven**: speaker identity, emotion, delivery, laughs, sighs, breaths, pauses, and transitions are all expressed inside a natural-language description, with an optional 10-second voice reference that clones the target timbre.

**Release Date:** April 17, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 3.3B (LTX-2.3 audio backbone, IC-LoRA fine-tune) + 12B Gemma 3 text encoder (conditioning only) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | English |
| **Streaming** | ❌ |
| **License** | ![Unknown][license-unknown] |
| **Base Model** | Lightricks/LTX-2.3 (audio branch) |
| **Architecture** | DiT + flow matching, IC-LoRA fine-tune, Gemma 3 12B text embeddings |
| **Inference Time** | ~2.5 s / generation (warm server) |

**Features:** IC-LoRA fine-tune of LTX-2.3's audio branch leaves the heavy text-understanding work to Gemma 3 12B and lets the DiT do the expressive rendering — so what's normally multimodal-stage orchestration collapses into a single prompt-driven TTS where speaker identity, emotion, and delivery are encoded in the prompt itself, and the timbre comes from a 10-second voice reference when present.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/ResembleAI/Dramabox)
[![GitHub][link-github]](https://resemble-ai/DramaBox)
[![Demo][link-demo]](https://huggingface.co/spaces/ResembleAI/Dramabox)
[![Website][link-website]](https://www.resemble.ai/learn/models/dramabox)

</details>
<!-- /MODEL:dramabox.md -->
<!-- MODEL:sarashina22-tts.md -->
<details id="sarashina22-tts">
<summary>Sarashina2.2-TTS</summary>

### Sarashina2.2-TTS

**Description:** Sarashina2.2-TTS is a Japanese-centric text-to-speech system from SB Intuitions built on a large language model. It supports both Japanese and English, delivers strong pronunciation accuracy on Japanese text through large-scale end-to-end training, and reproduces a speaker's voice, speaking style, and acoustic characteristics from a short reference clip (zero-shot). Training data is sourced exclusively from legitimately acquired, properly licensed speech archives per the Sarashina Model NonCommercial License Agreement v2.0 (released April 24, 2026).

**Release Date:** April 16, 2026

| Feature | Value |
|---------|-------|
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | Japanese, English |
| **Streaming** | ❌ |
| **License** | ![Research Only][license-research-only] |
| **Base Model** | sbintuitions/sarashina2.2-0.5b-instruct-v0.1 |
| **Cross Lingual** | yes (Japanese ↔ English, code switching) |

**Features:** Japanese-optimized TTS fine-tuned on responsibly-licensed Japanese training corpora with explicit cross-lingual code-switching to English in a single utterance; reference audio carries speaking style and speaker identity together, so the same prompt yields narration, broadcast, conversation, or customer-service delivery without separate style conditioning.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/sbintuitions/sarashina2.2-tts)
[![GitHub][link-github]](https://sbintuitions/sarashina2.2-tts)
[![Paper][link-paper]](https://arxiv.org/abs/2606.25369)

</details>
<!-- /MODEL:sarashina22-tts.md -->
<!-- MODEL:longcat-audiodit.md -->
<details id="longcat-audiodit">
<summary>LongCat-AudioDiT</summary>

### LongCat-AudioDiT

**Description:** State-of-the-art diffusion-based TTS model operating directly in waveform latent space. Developed by Meituan's LongCat team, it requires only a Waveform VAE and Diffusion backbone, effectively mitigating compounding errors.

**Release Date:** March 30, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 1B / 3.5B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ❌ |
| **Emotion Control** | ❌ |
| **Languages** | Chinese, English |
| **Streaming** | ❌ |
| **Audio Output** | 24000 Hz |
| **License** | ![MIT][license-mit] |

**Features:** Adaptive Projection Guidance (APG) replaces traditional classifier-free guidance for elevated generation quality. Outperforms Seed-TTS on zero-shot voice cloning benchmarks.

**Links:**
[![GitHub][link-github]](https://meituan-longcat/LongCat-AudioDiT)
[![HuggingFace][link-huggingface]](https://huggingface.co/meituan-longcat/LongCat-AudioDiT-1B)
[![HuggingFace][link-huggingface]](https://huggingface.co/meituan-longcat/LongCat-AudioDiT-3.5B)

</details>
<!-- /MODEL:longcat-audiodit.md -->
<!-- MODEL:fish-audio-s2-pro.md -->
<details id="fish-audio-s2-pro">
<summary>Fish Audio S2 Pro</summary>

### Fish Audio S2 Pro

**Description:** Fish Audio S2 Pro is a leading text-to-speech model with fine-grained inline control of prosody and emotion. It combines reinforcement learning alignment with a dual-autoregressive architecture for high-quality speech synthesis.

**Release Date:** March 10, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | ~10 GB (BF16) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | 80+ (Tier 1: En, Zh, Jp) |
| **Streaming** | ✅ |
| **License** | ![Research Only][license-research-only] |

**Links:**
[![GitHub][link-github]](https://fishaudio/fish-speech)
[![HuggingFace][link-huggingface]](https://huggingface.co/fishaudio/s2-pro)

</details>
<!-- /MODEL:fish-audio-s2-pro.md -->
<!-- MODEL:longcat-next.md -->
<details id="longcat-next">
<summary>LongCat-Next</summary>

### LongCat-Next

**Description:** Native multimodal foundation model by Meituan LongCat Team processing text, vision, and audio under a single autoregressive objective. Industrial-strength model with strong speech synthesis and voice cloning.

**Release Date:** March 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 3B (MoE A3B) |
| **Voice Cloning** | ✅ |
| **Asr** | ✅ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | Chinese, English |
| **Streaming** | ✅ |
| **Audio Output** | 24 kHz |
| **License** | ![MIT][license-mit] |

**Features:** Discrete Native Autoregression Paradigm (DiNA) unifying modalities in shared discrete token space. Combines visual understanding, generation, and audio processing in single model.

**Links:**
[![GitHub][link-github]](https://meituan-longcat/LongCat-Next)
[![HuggingFace][link-huggingface]](https://huggingface.co/meituan-longcat/LongCat-Next)

</details>
<!-- /MODEL:longcat-next.md -->
<!-- MODEL:voxtral-4b-tts.md -->
<details id="voxtral-4b-tts">
<summary>Voxtral-4B-TTS</summary>

### Voxtral-4B-TTS

**Description:** Frontier, open-weights text-to-speech model developed by Mistral AI. Designed to be fast, instantly adaptable, and produces lifelike speech with natural prosody and emotional range.

**Release Date:** March 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 4B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | 9 (En, Fr, Es, De, It, Pt, Nl, Ar, Hi) |
| **Streaming** | ✅ |
| **Audio Output** | 24 kHz |
| **License** | ![CC BY-NC 4.0][license-cc-by-nc-4.0] |

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)
[![Demo][link-demo]](https://console.mistral.ai/build/audio/text-to-speech)
[![Blog][link-blog]](https://mistral.ai/news/voxtral-tts)

</details>
<!-- /MODEL:voxtral-4b-tts.md -->
<!-- MODEL:blue-tts.md -->
<details id="blue-tts">
<summary>Blue (Light Blue) TTS</summary>

### Blue (Light Blue) TTS

**Description:** BlueTTS (project page: lightbluetts.com) is a multilingual text-to-speech library. Built around slim ONNX graphs that run on **ONNX Runtime** with first-class CPU support and optional accelerators — **OpenVINO** (Intel), **CUDA ORT** (NVIDIA), **TensorRT**, and **ONNX Runtime** stock CPU. Targets five languages — **Hebrew, English, Spanish, Italian, German** — including inline mixed-language with XML-style tags in the text prompt. Inference is deliverable as a PyPI package (`blue-onnx`), a Rust crate, or directly from the pinned ONNX graphs on the HF Hub; the v2 release ships a slimmed opset-17 ONNX bundle (notmax123/blue-onnx-v2) that's intended for both FP32 production and the experimental INT8 weight-only fallback.

**Release Date:** February 27, 2026

| Feature | Value |
|---------|-------|
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ❌ |
| **Languages** | Hebrew, English, Spanish, Italian, German |
| **Streaming** | ❌ |
| **License** | ![MIT][license-mit] |
| **Runtime** | ONNX Runtime (stock CPU; OpenVINO / CUDA / TensorRT optional) |
| **Speed** | "fastest open-source TTS" (per project description) |
| **Graph Format** | ONNX opset 17 (slim, full-precision; experimental weight-only INT8 fallback) |
| **Distribution** | PyPI + HuggingFace + Rust |

**Features:** A **CPU-first multilingual TTS** that ships both slimmed ONNX graphs and a Python package where the same code path runs on **stock CPU ONNX Runtime** by default — *and* optionally accelerates on OpenVINO / CUDA ORT / TensorRT — so deployment doesn't gate on GPU availability. Languages include **Hebrew** (with explicit G2P normalization) — a comparatively rare open-source TTS target — plus standard European languages, all from MIT-licensed weights distributed via both Hugging Face and PyPI.

**Links:**
[![GitHub][link-github]](https://maxmelichov/BlueTTS)
[![HuggingFace][link-huggingface]](https://huggingface.co/notmax123/blue-onnx-v2)
[![PyPI][link-pypi]](https://pypi.org/project/blue-onnx/)
[![Website][link-website]](https://lightbluetts.com/)
[![Demo][link-demo]](https://huggingface.co/spaces/notmax123/BlueV2)

</details>
<!-- /MODEL:blue-tts.md -->
<!-- MODEL:kittenTTS.md -->
<details id="kittenTTS">
<summary>KittenTTS</summary>

### KittenTTS

**Description:** KittenTTS is an open-source realistic text-to-speech model designed for lightweight deployment. It is a state-of-the-art TTS model under 25MB with just 15 million parameters, running without GPU on any device.

**Release Date:** February 24, 2026 (v0.8.1)

| Feature | Value |
|---------|-------|
| **Parameters** | 15M-80M |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | English, Multiple |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Links:**
[![GitHub][link-github]](https://KittenML/KittenTTS)
[![HuggingFace][link-huggingface]](https://huggingface.co/spaces/KittenML/KittenTTS-Demo)

</details>
<!-- /MODEL:kittenTTS.md -->
<!-- MODEL:ming-omni-tts.md -->
<details id="ming-omni-tts">
<summary>Ming-omni-tts</summary>

### Ming-omni-tts

**Description:** Ming-omni-tts is a high-performance unified audio generation model in the Ming 2.0 series. It uses a custom 12.5 Hz continuous tokenizer and a Patch-by-Patch compression strategy that drives the LLM inference frame rate down to 3.1 Hz, enabling fine-grained control over speech rate, pitch, volume, emotion, and dialect (notably Cantonese at ~93 % accuracy). It supports 100+ premium built-in voices plus zero-shot voice design from natural-language prompts and is the first autoregressive model that jointly generates speech, ambient sound, and music in a single channel.

**Release Date:** February 11, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 16.8B (3B active, MoE; A3B) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | Chinese, English, Cantonese |
| **Streaming** | ❌ |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Features:** Patch-by-Patch compression drives the inference frame rate to 3.1 Hz, drastically cutting LLM-side latency for podcast-style audio while preserving naturalness. A custom 12.5 Hz continuous tokenizer plus a DiT head jointly produce speech, ambient sound, and music in a single output channel — an "in-the-scene" listening experience rather than TTS-on-top-of-a-track.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/inclusionAI/Ming-omni-tts-16.8B-A3B)
[![GitHub][link-github]](https://inclusionAI/Ming-omni-tts)
[![Website][link-website]](https://xqacmer.github.io/Ming-omni-tts/)

</details>
<!-- /MODEL:ming-omni-tts.md -->
<!-- MODEL:soulx-singer.md -->
<details id="soulx-singer">
<summary>SoulX-Singer</summary>

### SoulX-Singer

**Description:** SoulX-Singer is a high-fidelity, zero-shot singing voice synthesis model for generating realistic singing voices for unseen singers without fine-tuning.

**Release Date:** February 6, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | - |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | Mandarin, English, Cantonese |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Links:**
[![GitHub][link-github]](https://Soul-AILab/SoulX-Singer)
[![HuggingFace][link-huggingface]](https://huggingface.co/spaces/Soul-AILab/SoulX-Singer)
[![arXiv][link-arxiv]](https://arxiv.org/abs/2602.07803)

</details>
<!-- /MODEL:soulx-singer.md -->
<!-- MODEL:soprotts.md -->
<details id="soprotts">
<summary>SoproTTS</summary>

### SoproTTS

**Description:** SoproTTS is a lightweight English text-to-speech model with zero-shot voice cloning. It uses dilated convolutions (WaveNet-style) and lightweight cross-attention layers instead of the common Transformer architecture.

**Release Date:** February 4, 2026 (v1.5)

| Feature | Value |
|---------|-------|
| **Parameters** | 135M |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | English |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Rtf** | 0.05 (CPU M3) |
| **Training-Cost** | ~$100 |

**Links:**
[![GitHub][link-github]](https://samuel-vitorino/sopro)
[![HuggingFace][link-huggingface]](https://huggingface.co/samuel-vitorino/sopro)

</details>
<!-- /MODEL:soprotts.md -->
<!-- MODEL:qwen3-tts.md -->
<details id="qwen3-tts">
<summary>Qwen3-TTS</summary>

### Qwen3-TTS

**Description:** Qwen3-TTS is an open-source series of Text-to-Speech models developed by Alibaba Cloud. Supports stable, expressive, and streaming speech generation with free-form voice design.

**Release Date:** January 22, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 0.6B-1.7B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | 10 (Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian) |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Links:**
[![GitHub][link-github]](https://QwenLM/Qwen3-TTS)
[![HuggingFace][link-huggingface]](https://huggingface.co/collections/Qwen/qwen3-tts)
[![arXiv][link-arxiv]](https://arxiv.org/abs/2601.15621)

</details>
<!-- /MODEL:qwen3-tts.md -->
<!-- MODEL:tada-1b.md -->
<details id="tada-1b">
<summary>TADA</summary>

### TADA

**Description:** TADA is a unified speech-language model from Hume AI built around a *Text-Acoustic Dual-Alignment* tokenizer: for every text/subword token there is exactly one corresponding speech vector, so the audio stream stays 1:1 aligned with text. As a TTS model, each autoregressive step covers one text token and dynamically determines the duration and prosody for that token, breaking the fixed-frames-per-second constraint that drives most modern TTS backbones. As a speech-language model, it generates a text token and the speech for the preceding token in the same dual step.

**Release Date:** January 12, 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 1B (Llama 3.2 1B base) |
| **Voice Cloning** | ❌ |
| **Asr** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | English |
| **Streaming** | ❌ |
| **License** | ![Unknown][license-unknown] |
| **Base Model** | meta-llama/Llama-3.2-1B |
| **Tokenization** | 1:1 text–acoustic dual alignment (one speech vector per text token) |
| **Dynamic Duration** | yes (each autoregressive step covers one text token, duration is determined per-token) |

**Features:** A dual-alignment speech–text tokenizer that decouples autoregression from a fixed audio frame rate: each text token owns exactly one speech vector, and the model synthesizes the *whole segment for that token* in one step, regardless of how long the spoken form is — eliminating transcript hallucination and the latency overhead of constant-frame-rate codecs while staying as compact as Llama 3.2 1B.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/HumeAI/tada-1b)
[![GitHub][link-github]](https://HumeAI/tada)
[![Demo][link-demo]](https://huggingface.co/spaces/HumeAI/tada)
[![PyPI][link-pypi]](https://pypi.org/project/hume-tada/)
[![Paper][link-paper]](https://arxiv.org/abs/2602.23068)
[![Blog][link-blog]](https://www.hume.ai/blog/opensource-tada)

</details>
<!-- /MODEL:tada-1b.md -->
<!-- MODEL:irodori-tts-500m-v2.md -->
<details id="irodori-tts-500m-v2">
<summary>Irodori-TTS-500M-v2</summary>

### Irodori-TTS-500M-v2

**Description:** Japanese Text-to-Speech model based on Rectified Flow Diffusion Transformer. Features emoji-based style and sound effect control by embedding emojis in input text for expressive speech generation.

**Release Date:** 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 500M |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ❌ |
| **Emotion Control** | ✅ |
| **Languages** | Japanese |
| **Streaming** | ❌ |
| **Audio Output** | 48kHz waveform |
| **License** | ![MIT][license-mit] |

**Features:** **Key Feature:** Emoji annotation control - insert specific emojis into text to control speaking styles, emotions, and sound effects.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/Aratako/Irodori-TTS-500M-v2)
[![GitHub][link-github]](https://Aratako/Irodori-TTS)
[![Demo][link-demo]](https://huggingface.co/spaces/Aratako/Irodori-TTS-500M-v2-Demo)

</details>
<!-- /MODEL:irodori-tts-500m-v2.md -->
<!-- MODEL:kugelaudio.md -->
<details id="kugelaudio">
<summary>KugelAudio</summary>

### KugelAudio

**Description:** Open-source TTS for European languages with 7B parameters. Outperformed ElevenLabs in human preference testing.

**Release Date:** Early 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 7B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | 23 European languages |
| **Streaming** | ✅ |
| **License** | ![MIT][license-mit] |

**Links:**
[![GitHub][link-github]](https://Kugelaudio/kugelaudio-open)
[![HuggingFace][link-huggingface]](https://huggingface.co/kugelaudio/kugelaudio-0-open)
[![Website][link-website]](https://kugelaudio.com)

</details>
<!-- /MODEL:kugelaudio.md -->
<!-- MODEL:lemas-tts.md -->
<details id="lemas-tts">
<summary>LEMAS-TTS</summary>

### LEMAS-TTS

**Description:** Part of the LEMAS (Large-scale Extensible Multilingual Audio Suite) project. Zero-shot multilingual TTS with 0.3B parameters supporting 10 languages with word-level precise editing capabilities.

**Release Date:** 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 0.3B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | 10 (zh/en/de/fr/es/pt/it/ru/id/vi) |
| **Streaming** | ❌ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Special-Feature** | Word-level editing (LEMAS-Edit) |

**Features:** Built on 150,000+ hours of multilingual speech data with word-level timestamps. Includes LEMAS-Edit for precise word-level speech editing via masked token infilling.

**Links:**
[![Website][link-website]](https://lemas-project.github.io/LEMAS-Project/)
[![HuggingFace][link-huggingface]](https://huggingface.co/LEMAS-Project/LEMAS-TTS)
[![HuggingFace][link-huggingface]](https://huggingface.co/LEMAS-Project/LEMAS-Edit)

</details>
<!-- /MODEL:lemas-tts.md -->
<!-- MODEL:miotts-26b.md -->
<details id="miotts-26b">
<summary>MioTTS-2.6B</summary>

### MioTTS-2.6B

**Description:** Lightweight, high-speed LLM-based TTS model for English and Japanese with minimal resource usage.

**Release Date:** 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 2.6B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ❌ |
| **Emotion Control** | ❌ |
| **Languages** | English, Japanese |
| **Streaming** | ✅ |
| **License** | ![LFM][license-lfm] |
| **Rtf** | 0.135-0.145 |

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/Aratako/MioTTS-2.6B)
[![GitHub][link-github]](https://Aratako/MioTTS-Inference)

</details>
<!-- /MODEL:miotts-26b.md -->
<!-- MODEL:moss-tts-nano.md -->
<details id="moss-tts-nano">
<summary>MOSS-TTS-Nano</summary>

### MOSS-TTS-Nano

**Description:** Ultra-lightweight open-source multilingual speech generation model with only 0.1B parameters. Designed for realtime speech generation that runs directly on CPU without GPU.

**Release Date:** 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 0.1B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ❌ |
| **Emotion Control** | ❌ |
| **Languages** | 20 |
| **Streaming** | ✅ |
| **Audio Output** | 48 kHz Stereo |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Features:** Pure autoregressive architecture with MOSS-Audio-Tokenizer-Nano. Compresses audio to 12.5 Hz token stream using RVQ with 16 codebooks. Runs on 4-core CPU.

**Links:**
[![GitHub][link-github]](https://OpenMOSS/MOSS-TTS-Nano)
[![HuggingFace][link-huggingface]](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Nano-100M)
[![Demo][link-demo]](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-TTS-Nano)

</details>
<!-- /MODEL:moss-tts-nano.md -->
<!-- MODEL:neutts.md -->
<details id="neutts">
<summary>NeuTTS</summary>

### NeuTTS

**Description:** NeuTTS is a collection of open-source on-device TTS models with instant voice cloning. Built off LLM backbones with GGUF format quantizations for efficient on-device deployment.

**Release Date:** Early 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 360M (Air), 120M (Nano) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ❌ |
| **Emotion Control** | ❌ |
| **Languages** | English, Spanish, German, French |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **On-Device** | yes (GGUF quantizations) |

**Links:**
[![GitHub][link-github]](https://neuphonic/neutts)
[![HuggingFace][link-huggingface]](https://huggingface.co/neuphonic/neutts-air)
[![HuggingFace][link-huggingface]](https://huggingface.co/neuphonic/neutts-nano)

</details>
<!-- /MODEL:neutts.md -->
<!-- MODEL:omnivoice.md -->
<details id="omnivoice">
<summary>OmniVoice</summary>

### OmniVoice

**Description:** Massive multilingual zero-shot TTS model scaling to 600+ languages. Uses diffusion language model-style discrete non-autoregressive architecture with single-stage text-to-acoustic mapping.

**Release Date:** 2026

| Feature | Value |
|---------|-------|
| **Parameters** | - |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | 600+ |
| **Streaming** | ❌ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Training-Data** | 581k hours |

**Features:** Simplified single-stage architecture vs conventional two-stage pipelines. Full-codebook random masking strategy with LLM initialization for superior intelligibility. Noise-robust prompt processing.

**Links:**
[![Website][link-website]](https://zhu-han.github.io/omnivoice/)
[![HuggingFace][link-huggingface]](https://huggingface.co/k2-fsa/OmniVoice)

</details>
<!-- /MODEL:omnivoice.md -->
<!-- MODEL:t5gemma-tts.md -->
<details id="t5gemma-tts">
<summary>T5Gemma-TTS</summary>

### T5Gemma-TTS

**Description:** Multilingual TTS model with voice cloning and duration control, built on the T5Gemma encoder-decoder LLM architecture. Supports batch generation for multiple audio variations.

**Release Date:** 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 2B-2B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ❌ |
| **Languages** | English, Chinese, Japanese |
| **Streaming** | ❌ |
| **License** | ![MIT][license-mit] |
| **Vram** | 7.6-10.6 GB |

**Features:** PM-RoPE positional encoding with XCodec2 audio codec. Low-VRAM options with CPU offloading. Batch inference efficiency with single encoder pass.

**Links:**
[![GitHub][link-github]](https://Aratako/T5Gemma-TTS)
[![HuggingFace][link-huggingface]](https://huggingface.co/Aratako/T5Gemma-TTS-2b-2b)
[![Demo][link-demo]](https://huggingface.co/spaces/Aratako/T5Gemma-TTS-Demo)

</details>
<!-- /MODEL:t5gemma-tts.md -->
<!-- MODEL:tinytts.md -->
<details id="tinytts">
<summary>TinyTTS</summary>

### TinyTTS

**Description:** The smallest English TTS model with only 1.6 million parameters. End-to-end neural network achieving ~53x real-time synthesis speed on CPU via ONNX optimization.

**Release Date:** 2026

| Feature | Value |
|---------|-------|
| **Parameters** | ~3.4 MB (ONNX FP16) |
| **Voice Cloning** | ❌ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ❌ |
| **Languages** | English |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Features:** Ultra-compact architecture optimized for CPU-only deployment. Multi-platform support via Python and Node.js APIs. Works on laptops, edge devices, and embedded systems.

**Links:**
[![GitHub][link-github]](https://tronghieuit/tiny-tts)
[![HuggingFace][link-huggingface]](https://huggingface.co/backtracking/tiny-tts)
[![Demo][link-demo]](https://huggingface.co/spaces/backtracking/tiny-tts-demo)

</details>
<!-- /MODEL:tinytts.md -->
<!-- MODEL:voxcpm2.md -->
<details id="voxcpm2">
<summary>VoxCPM2</summary>

### VoxCPM2

**Description:** OpenBMB's next-generation tokenizer-free diffusion autoregressive TTS model with 2 billion parameters. Supports 30 languages with automatic detection, voice design from text descriptions, and high-fidelity voice cloning.

**Release Date:** 2026

| Feature | Value |
|---------|-------|
| **Parameters** | 2B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | 30 (+ 9 Chinese dialects) |
| **Streaming** | ✅ |
| **Audio Output** | 48 kHz |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Features:** Tokenizer-free design with LocEnc → TSLM → RALM → LocDiT pipeline. Built-in super-resolution via AudioVAE V2 for 48kHz output.

**Links:**
[![GitHub][link-github]](https://OpenBMB/VoxCPM)
[![HuggingFace][link-huggingface]](https://huggingface.co/openbmb/VoxCPM2)
[![Demo][link-demo]](https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo)

</details>
<!-- /MODEL:voxcpm2.md -->
<!-- MODEL:soprano.md -->
<details id="soprano">
<summary>Soprano</summary>

### Soprano

**Description:** **Soprano** is an ultra-lightweight, on-device text-to-speech (TTS) model designed for expressive, high-fidelity speech synthesis at unprecedented speed. The 1.1 release ships an 80M-parameter backbone that achieves up to **20× real-time generation on CPU** and **2000× real-time on GPU**, with **lossless streaming** (<250 ms latency on CPU, <15 ms on GPU), **<1 GB memory usage** at inference, and **infinite generation length** (automatic text splitting). Output sample rate is **32 kHz**, with widespread device support (CUDA / CPU / MPS on Windows, Linux, and Mac). Inference is production-ready through an OpenAI-compatible endpoint, ONNX, WebUI, CLI, and ComfyUI nodes. The base 1.1 model is `ekwek/Soprano-1.1-80M` on HuggingFace; a fine-tuning toolkit (`soprano-factory`) was released January 13 2026 alongside the 1.1 weights — the 1.1 release reports **95% fewer hallucinations** and a **63% preference rate** over 1.0 (Soprano-80M). A live demo runs on `ekwek/Soprano-TTS` HF Space.

**Release Date:** December 22, 2025

| Feature | Value |
|---------|-------|
| **Parameters** | 80M (Soprano-1.1-80M) |
| **Voice Cloning** | ❌ |
| **Asr** | ❌ |
| **Languages** | English (US/UK family voices, per HF Space) |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Sample Rate** | 32,000 Hz |
| **Inference Targets** | OpenAI-compatible endpoint, ONNX, WebUI, CLI, ComfyUI |
| **Performance Cpu** | up to 20× real-time |
| **Performance Gpu** | up to 2000× real-time |
| **Memory** | <1 GB at inference |
| **Text Length** | infinite (automatic text splitting) |
| **Devices** | CUDA, CPU, MPS (Windows, Linux, Mac) |
| **Training Toolkit** | soprano-factory (https://ekwek1/soprano-factory) |
| **History 1 1** | Soprano-1.1-80M released 2026-01-14 (95% fewer hallucinations; 63% preference over 1.0) |
| **History 1 0** | Soprano-80M released 2025-12-22 |

**Features:** The defining trade-off of this release is **extreme on-device
efficiency at sub-100M scale**: an 80M-parameter backbone hits
**<250 ms CPU latency** and **<15 ms GPU** for lossless streaming
while keeping inference within <1 GB of memory — well under the
multi-billion-parameter budget that newer conversational TTS
systems require. The release pairs the model with `soprano-factory`
(open-source training/fine-tuning toolkit) so users can build their
own voices on top of the same backbone, and one installation can
drive OpenAI-compatible / ONNX / WebUI / CLI / ComfyUI inference.
The 1.1 update is a measured iteration: 95% fewer hallucinations
and a 63% preference over 1.0 at the same parameter budget, so the
measurable quality jump ships with no added inference cost.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/ekwek/Soprano-1.1-80M)
[![GitHub][link-github]](https://ekwek1/soprano)
[![Demo][link-demo]](https://huggingface.co/spaces/ekwek/Soprano-TTS)

</details>
<!-- /MODEL:soprano.md -->
<!-- MODEL:glm-tts.md -->
<details id="glm-tts">
<summary>GLM-TTS</summary>

### GLM-TTS

**Description:** High-quality TTS synthesis system based on LLMs from ZhipuAI, supporting zero-shot voice cloning with Multi-Reward Reinforcement Learning.

**Release Date:** December 11, 2025

| Feature | Value |
|---------|-------|
| **Parameters** | - |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | Chinese, English |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Links:**
[![GitHub][link-github]](https://zai-org/GLM-TTS)
[![HuggingFace][link-huggingface]](https://huggingface.co/zai-org/GLM-TTS)
[![arXiv][link-arxiv]](https://arxiv.org/abs/2512.14291)

</details>
<!-- /MODEL:glm-tts.md -->
<!-- MODEL:echo-tts.md -->
<details id="echo-tts">
<summary>Echo-TTS</summary>

### Echo-TTS

**Description:** **Echo** is a 2.4B-parameter **diffusion-based diffusion transformer (DiT)** text-to-speech model. It conditions on target text and up to **two minutes of speaker reference audio**, generates Fish Speech S1-DAC latents, and decodes to **44.1 kHz** audio. Output length is up to **30 seconds per segment**. The model is fast at single-sample generation: on one A100, generating 30 seconds of audio from a 120-second prompt takes **~1.45 seconds** (RTF < 0.05) — substantially faster than frontier autoregressive approaches at similar quality. The architecture is a deliberate pivot from the author's prior autoregressive-in-DAC-space model **Parakeet**, which struggled with semantic-consistency retries and weak voice cloning; Echo's diffusion approach trades off real-time interactivity for **fast, high-fidelity zero-shot voice cloning** in offline synthesis. Trained via the TPU Research Cloud (TRC). Demo (preview) hosted on `jordand/echo-tts-preview` HF Space; base model on `jordand/echo-tts-base`.

**Release Date:** December 4, 2025

| Feature | Value |
|---------|-------|
| **Parameters** | 2.4B (DiT) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Languages** | English (per demo samples) |
| **Streaming** | ❌ |
| **License** | ![MIT][license-mit] |
| **Architecture** | diffusion transformer (DiT) in Fish Speech S1-DAC latent space |
| **Max Segment Duration** | 30 s |
| **Sample Rate** | 44,100 Hz |
| **Speaker Reference Max** | 120 s |
| **Performance A100 Rt** | 30 s output in ~1.45 s (RTF < 0.05) |
| **Audio Codec** | Fish Speech S1-DAC |
| **Prior Model** | Parakeet (autoregressive in DAC space) |
| **Training Infrastructure** | TPU Research Cloud (TRC) |
| **Inference Requirements** | CUDA-capable GPU with at least 8 GB VRAM; Python 3.10+ |
| **Sampler** | euler CFG with independent guidances for text (3.0) and speaker (8.0); 40 steps; sequence_length 640 default |
| **License Clarification** | MIT (per GH repo license) |

**Features:** Echo is a deliberate **next-step pivot from autoregressive-in-DAC-space
TTS to a full diffusion approach**. The author's prior model,
Parakeet, generated DAC tokens autoregressively but suffered the
classic AR weakness — semantic-consistency retries — and weak
voice cloning. Echo keeps Fish Speech S1-DAC latents (so the audio
representation is the same proven codec) but moves the generator
*upstream* to a 2.4B DiT operating directly on those latents,
conditioned on a long (up to 2-minute) speaker reference. The
result: 30-second outputs in ~1.45 s on a single A100 (RTF < 0.05)
with high-fidelity zero-shot cloning — fast enough that the
"diffusion is too slow" objection no longer applies at the segment
length that matters for offline content generation, while the AR
class's retry-induced inconsistency is gone by construction.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/jordand/echo-tts-base)
[![GitHub][link-github]](https://jordandare/echo-tts)
[![Demo][link-demo]](https://huggingface.co/spaces/jordand/echo-tts-preview)
[![Blog][link-blog]](https://jordandarefsky.com/blog/2025/echo/)

</details>
<!-- /MODEL:echo-tts.md -->
<!-- MODEL:vibevoice-realtime.md -->
<details id="vibevoice-realtime">
<summary>VibeVoice-Realtime</summary>

### VibeVoice-Realtime

**Description:** Real-time TTS model from Microsoft with streaming text input and ultra-low latency (~300ms).

**Release Date:** December 3, 2025

| Feature | Value |
|---------|-------|
| **Parameters** | 0.5B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | Multilingual |
| **Streaming** | ✅ |
| **License** | ![MIT][license-mit] |
| **Max Duration** | ~10 minutes |

**Links:**
[![GitHub][link-github]](https://microsoft/VibeVoice)
[![HuggingFace][link-huggingface]](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)

</details>
<!-- /MODEL:vibevoice-realtime.md -->
<!-- MODEL:fun-cosyvoice-30.md -->
<details id="fun-cosyvoice-30">
<summary>Fun-CosyVoice 3.0</summary>

### Fun-CosyVoice 3.0

**Description:** Advanced TTS system based on LLMs for zero-shot multilingual speech synthesis from FunAudioLLM.

**Release Date:** December 2025

| Feature | Value |
|---------|-------|
| **Parameters** | 0.5B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | 9 + 18+ Chinese dialects |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Links:**
[![GitHub][link-github]](https://FunAudioLLM/CosyVoice)
[![HuggingFace][link-huggingface]](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512)
[![arXiv][link-arxiv]](https://arxiv.org/abs/2505.17589)

</details>
<!-- /MODEL:fun-cosyvoice-30.md -->
<!-- MODEL:lfm2-audio-15b.md -->
<details id="lfm2-audio-15b">
<summary>LFM2-Audio-1.5B</summary>

### LFM2-Audio-1.5B

**Description:** Liquid AI's first end-to-end audio foundation model with low latency and real-time conversation.

**Release Date:** November 28, 2025

| Feature | Value |
|---------|-------|
| **Parameters** | 1.5B |
| **Voice Cloning** | ✅ |
| **Asr** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | English |
| **Streaming** | ✅ |
| **License** | ![LFM][license-lfm] |

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/LiquidAI/LFM2-Audio-1.5B)
[![Website][link-website]](https://docs.liquid.ai/lfm)

</details>
<!-- /MODEL:lfm2-audio-15b.md -->
<!-- MODEL:marvis-tts.md -->
<details id="marvis-tts">
<summary>Marvis-TTS</summary>

### Marvis-TTS

**Description:** **Marvis** is a conversational real-time streaming TTS from Marvis-Labs. The architecture inherits Sesame's **CSM-1B** (Conversational Speech Model): a 250M-parameter **multimodal backbone** that processes interleaved text + audio tokens and a smaller 60M-parameter **audio decoder** that models the remaining 31 RVQ codebook levels to reconstruct high-quality speech from the backbone's representations. Audio tokens come from **Kyutai's mimi codec** (RVQ tokens). The dual-transformer split — semantic backbone + small decoder — yields sub-second latency, and the model is built for **on-edge / on-device** deployment (Apple Silicon / iPad / iPhone / Mac). Two operational choices distinguish Marvis:

**Release Date:** November 6, 2025

| Feature | Value |
|---------|-------|
| **Parameters** | 250M (multimodal backbone) + 60M (audio decoder) = 310M total |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Languages** | English, French, German |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Architecture** | dual-transformer CSM-1B (Conversational Speech Model) — multimodal backbone + audio decoder |
| **Audio Codec** | Kyutai mimi codec (RVQ tokens; backbone models codebook 0, decoder models codebook 1–31) |
| **Quantized Size** | ~500 MB (4-bit MLX) |
| **Training Dataset** | amphion/Emilia-Dataset |
| **Library Name** | transformers, mlx, mlx-audio |
| **Inference Cli** | `mlx_audio.tts.generate --model Marvis-AI/marvis-tts-250m-v0.2 --stream --text "..." [--ref_audio ./x.wav]` |
| **Variants In Collection** | 250m-v0.2, 250m-v0.2-MLX-{4bit,6bit,8bit}, 100m-v0.2 (+ MLX variants), 250m-v0.2-transformers |
| **Emits Text Chunking** | no (full-sequence contextual processing) |

**Features:** Two operational choices make Marvis stand out among conversational
TTS. First, **no regex chunking**: most streaming TTS engines
pre-split sentences by regex patterns before feeding them to the
generator, which can disrupt flow / intonation; Marvis processes
the entire text contextually, treating the text as a single
interleaved multimodal sequence. Second, the **dual-transformer
CSM-1B design** — a 250M backbone for codebook 0 (semantic) and a
smaller 60M audio decoder for codebooks 1-31 (acoustic) — produces
a quantized footprint of ~500 MB, enabling **on-device Apple-Silicon
inference** (iPad / iPhone / Mac) with real-time streaming. The
architecture makes a high-quality CSM-style TTS with zero-shot
cloning actually deployable at the edge, while the official
collection's 4 / 6 / 8-bit MLX variants let users trade footprint
for fidelity on a per-device basis.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/Marvis-AI/marvis-tts-250m-v0.2)
[![GitHub][link-github]](https://Marvis-Labs/marvis-tts)

</details>
<!-- /MODEL:marvis-tts.md -->
<!-- MODEL:indextts2.md -->
<details id="indextts2">
<summary>IndexTTS2</summary>

### IndexTTS2

**Description:** AI-Enhanced Text-to-Speech System with Intelligent Optimization and self-learning capabilities.

**Release Date:** November 2025

| Feature | Value |
|---------|-------|
| **Parameters** | - |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | Chinese, English |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |
| **Multi-Speaker** | yes (1-4 speakers) |

**Links:**
[![GitHub][link-github]](https://xuchenxu168/Comfyui-Index-TTS2)
[![HuggingFace][link-huggingface]](https://huggingface.co/IndexTeam/IndexTTS-2)

</details>
<!-- /MODEL:indextts2.md -->
<!-- MODEL:maya1.md -->
<details id="maya1">
<summary>Maya1</summary>

### Maya1

**Description:** State-of-the-art speech model for expressive voice generation with natural language voice control.

**Release Date:** November 2025

| Feature | Value |
|---------|-------|
| **Parameters** | 3B |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | English (Multi-accent) |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/maya-research/maya1)
[![Website][link-website]](https://mayaresearch.ai)

</details>
<!-- /MODEL:maya1.md -->
<!-- MODEL:step-audio-editx.md -->
<details id="step-audio-editx">
<summary>Step-Audio-EditX</summary>

### Step-Audio-EditX

**Description:** 3B-parameter LLM-based RL audio model specialized in expressive and iterative audio editing.

**Release Date:** November 2025

| Feature | Value |
|---------|-------|
| **Parameters** | 3B (4B BF16) |
| **Voice Cloning** | ✅ |
| **Asr** | ❌ |
| **Pronunciation** | ✅ |
| **Emotion Control** | ✅ |
| **Languages** | Mandarin, English, Sichuanese, Cantonese, Japanese, Korean |
| **Streaming** | ✅ |
| **License** | ![Apache 2.0][license-apache-2.0] |

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/stepfun-ai/Step-Audio-EditX)
[![arXiv][link-arxiv]](https://arxiv.org/abs/2511.03601)

</details>
<!-- /MODEL:step-audio-editx.md -->
<!-- MODEL:kani-tts.md -->
<details id="kani-tts">
<summary>KaniTTS</summary>

### KaniTTS

**Description:** **KaniTTS** is a 370M-parameter two-stage text-to-speech model from nineninesix-ai. The architecture pairs an **LFM-2 backbone LLM** (Liquid Foundation Model v2 — a non-transformer, structured state-space architecture) with a **neural audio codec** for output waveform synthesis. The LLM generates compressed audio-token representations and the codec renders them to 22 kHz waveforms, yielding low-latency generation: **~1 s to produce 15 s of audio on a single RTX 5080**, with **2 GB GPU VRAM** at inference, and **MOS 4.3 / WER < 5%** quality on the project's benchmarks. Languages covered: **English, German, Chinese, Korean, Arabic, Spanish** across multiple per-language voices (English, German, Chinese, Korean, Arabic, Spanish each ship a 400M checkpoint; Japanese ships a 370M "Expo-2025-Osaka" variant; a multilingual 370M checkpoint is also available). MLX variants exist for Apple-Silicon inference. The codec is the same author's `nemo-nano-codec-22kHz-0.6kbps-12.5fps-MLX` (NVIDIA NeMo NanoCodec, MLX-ported to ~12.5 fps / 0.6 kbps). The model is part of the nineninesix-ai family alongside Gepard.

**Release Date:** September 30, 2025

| Feature | Value |
|---------|-------|
| **Parameters** | 370M (kani-tts-370m multilingual); 400M per-language (en / de / zh / ko / ar / es); 370M (expo2025-osaka-ja) |
| **Voice Cloning** | ❌ |
| **Asr** | ❌ |
| **Languages** | English, German, Chinese, Korean, Arabic, Spanish (multilingual 370M checkpoint); Japanese (Expo-2025-Osaka variant) |
| **Streaming** | ✅ |
| **License** | ![Unknown][license-unknown] |
| **Sample Rate** | 22,000 Hz |
| **Backbone Llm** | LFM-2 (Liquid Foundation Model; non-transformer structured state-space architecture) |
| **Audio Codec** | nineninesix/nemo-nano-codec-22khz-0.6kbps-12.5fps-MLX (NVIDIA NeMo NanoCodec, MLX-ported) |
| **Performance Rt 5080** | ~1 s for 15 s audio on RTX 5080 |
| **Memory** | 2 GB GPU VRAM at inference |
| **Quality Mos** | 4.3 / 5 (naturalness) |
| **Quality Wer** | <5% (accuracy) |
| **Training Dataset** | ~80k hours (LibriTTS, Common Voice, Emilia) |
| **Training Hardware** | 8x H100 GPUs, 45 hours on Lambda AI |
| **Per Language Models** | kani-tts-400m-{en,zh,de,ar,es,ko} on HuggingFace |
| **Pretrained Checkpoints** | 0.2-pt (450M), 0.3-pt (400M) for custom posttraining / fine-tuning |
| **Mlx Variants** | kani-tts-370m-MLX (Apple Silicon) |
| **Arxiv** | 2505.20506 |

**Features:** KaniTTS's design choice worth flagging: it pairs a **non-transformer
LFM-2 backbone** (Liquid Foundation Model — structured state-space
rather than attention) with a **neural audio codec for output** at
the **370M scale**. The choice lets the model hit a ~1 s / 15 s
audio generation rate on a **2 GB GPU VRAM budget** — sub-1B
parameters, sub-entry-tier GPU requirement, but still multilingual
across six languages. The two-stage approach (LLM → codec) is
conventional; what's less conventional is the choice of a
state-space backbone over the usual transformer decoder at this
scale, hitting latency / VRAM numbers that open up sub-1B real-time
TTS on consumer-grade hardware. The same author ships `soprano-factory`-style
companion assets (pretrained v0.2-pt / v0.3-pt checkpoints, a
NeMo NanoCodec MLX port) to lower the bar for fine-tuning on custom
datasets.

**Links:**
[![HuggingFace][link-huggingface]](https://huggingface.co/nineninesix/kani-tts-370m)
[![GitHub][link-github]](https://nineninesix-ai/kani-tts)

</details>
<!-- /MODEL:kani-tts.md -->
<!-- MODEL:vibevoice-finetuning.md -->
<details id="vibevoice-finetuning">
<summary>VibeVoice-Finetuning</summary>

### VibeVoice-Finetuning

**Description:** This is an **unofficial, work-in-progress LoRA fine-tuning toolkit** for the VibeVoice TTS / speech model (1.5B-base and 7B-base checkpoints). The base VibeVoice checkpoints are the same ones covered in this list's [a separate entry](#modelvibevoice-realtimemd): audio-conditioned diffusion TTS for spoken dialogue, streaming, etc. This toolkit takes **pretrained VibeVoice** weights + a paired (text, audio, optional reference-audio) dataset and trains a **LoRA adapter** against two losses simultaneously:

**Release Date:** September 16, 2025

| Feature | Value |
|---------|-------|
| **Parameters** | 1.5B (LoRA-adapted) / 7B (LoRA-adapted) |
| **Voice Cloning** | ❌ |
| **Asr** | ❌ |
| **Languages** | inherits base VibeVoice coverage |
| **Streaming** | not directly (toolkit output is a LoRA adapter; the adapter inherits VibeVoice inference sh