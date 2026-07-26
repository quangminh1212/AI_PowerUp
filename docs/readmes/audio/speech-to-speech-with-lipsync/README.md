<!-- source: https://github.com/M-SRIKAR-VARDHAN/speech-to-speech-with-lipsync.git sha: e95b28957618416ed3958953db0ed4c2af58e82f readme: main/README.md -->
# M-SRIKAR-VARDHAN/speech-to-speech-with-lipsync

End-to-end speech-to-speech translation pipeline with voice cloning (RVC) and automatic lip-sync (Wav2Lip).

---

# 🎤 Speech-to-Speech Translation with Lip Sync

<p align="center">
  <a href="https://github.com/M-SRIKAR-VARDHAN">
    <img src="https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/srikar-vardhan/">
    <img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn">
  </a>
  <a href="mailto:srikarvardhan2005@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact_Me-red?style=for-the-badge&logo=gmail" alt="Email">
  </a>
</p>

Hello everyone 👋, my name is **[Srikar Vardhan](https://github.com/M-SRIKAR-VARDHAN)**, and I'm a final-year student at **NIT Silchar**.  
This project is my attempt at building an **end-to-end speech-to-speech translation pipeline with lip-syncing**.  
The system translates English speech into Telugu (or other languages), **preserves the speaker’s voice**, and **synchronizes lip movements** for a natural dubbed video.  

I’ll walk you through the idea, implementation, challenges, and how to run it yourself.  
If you like this project, please ⭐ star the repo and give credit 🙏. 

you can read my medium blog about this [project](https://medium.com/@srikarvardhan2005/speech-to-speech-translation-with-lip-sync-425d8bb74530)

---

## 📊 Pipeline Overview

The pipeline is a multi-stage process where the output of one model becomes the input for the next. This modular approach allows for flexibility and high-quality results at each step.

| Stage | Model/Tool | Input | Output |
| :--- | :--- | :--- | :--- |
| **1. Transcription** | 🗣️ **Whisper ASR** | Video with English Speech | `English Text` |
| **2. Translation** | 🌐 **NLLB NMT** | `English Text` | `Telugu Text` |
| **3. Speech Synthesis** | 🔊 **MMS-TTS** | `Telugu Text` | `Telugu Audio (Generic Voice)` |
| **4. Voice Conversion**| 🧬 **RVC** | `Generic Audio` + `Speaker's Voice Sample` | `Telugu Audio (Original Voice)` |
| **5. Lip Syncing** | 👄 **Wav2Lip** | `Original Video` + `Final Audio` | **Final Video (Synced)** |

---



## ✨ Demo & Results

Click on the images below to watch the full videos hosted on Google Drive.

| Original Video (English) | Translated & Dubbed Video (Telugu) |
| :---: | :---: |
| [![Original Video Thumbnail](https://github.com/M-SRIKAR-VARDHAN/speech-to-speech-with-lipsync/blob/main/image.png?raw=true)](https://drive.google.com/file/d/12hOrIere-IdES-9-VQ7HRIjh4kXfWadI/view?usp=sharing) | [![Dubbed Video Thumbnail](https://github.com/M-SRIKAR-VARDHAN/speech-to-speech-with-lipsync/blob/main/image.png?raw=true)](https://drive.google.com/file/d/18RxxDv5S_4EN4nDw3uQ054U8FWisKBw7/view?usp=sharing) |
| **[Watch Original Video](https://drive.google.com/file/d/12hOrIere-IdES-9-VQ7HRIjh4kXfWadI/view?usp=sharing)** | **[Watch Dubbed Video](https://drive.google.com/file/d/18RxxDv5S_4EN4nDw3uQ054U8FWisKBw7/view?usp=sharing)** |



---
## 📂 Repository Structure

```bash
📂 demo
├── 1.py                        # Translation pipeline (video → translated audio)
├── 1.txt
├── 3.py
├── Advanced-RVC-Inference      # Voice conversion (RVC)
│   ├── config.py
│   ├── configs/
│   │   ├── 32k.json
│   │   ├── 40k.json
│   │   └── 48k.json
│   ├── hubert_base.pt
│   ├── lib/
│   │   ├── audio.py
│   │   ├── commons.py
│   │   ├── data_utils.py
│   │   └── ...
│   ├── my_convert.py
│   ├── requirements.txt
│   ├── vc_infer_pipeline.py
│   └── weights/
│       ├── modi.pth
│       ├── model.index
│       └── ...
├── dubbed_test.mp4
├── lip.py                      # Lip-sync module (Wav2Lip)
├── main.py                     # Orchestration script (runs everything end-to-end)
├── models/
│   ├── translation/
│   │   └── nllb-en-te/
│   │       ├── config.json
│   │       ├── model.safetensors
│   │       └── ...
│   ├── tts/
│   │   └── mms-tel/
│   │       ├── config.json
│   │       ├── model.safetensors
│   │       └── ...
│   └── whisper/
│       └── base.en.pt
├── output.mp4
├── requirment.txt
├── temp/
│   └── result.avi
├── test.mp4
├── test_converted.wav
├── test_translated.wav
└── wav2Lip
    ├── checkpoints/
    │   ├── wav2lip.pth
    │   └── wav2lip_gan.pth
    ├── face_detection/
    │   ├── api.py
    │   ├── core.py
    │   └── sfd/
    │       ├── net_s3fd.py
    │       └── s3fd.pth
    ├── inference.py
    ├── models/
    │   ├── conv.py
    │   ├── syncnet.py
    │   └── wav2lip.py
    ├── preprocess.py
    └── requirements.txt
```
---

## ⚙️ Setup Instructions

### 1\. Clone the Repository

```bash
git clone [https://github.com/M-SRIKAR-VARDHAN/speech-to-speech-with-lipsync.git](https://github.com/M-SRIKAR-VARDHAN/speech-to-speech-with-lipsync.git)
cd speech-to-speech-with-lipsync
```
---

### 2\. Create a Python Environment

It’s recommended to use Python 3.10+ in a virtual environment.

```bash
conda create -n lipsync python=3.10 -y
conda activate lipsync
```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4\. Download Pre-trained Models

The large model files (ASR, NMT, TTS, RVC, Wav2Lip) are not included in the repo. You must download them and extract them into the correct folders as shown in the repository structure.

  - **[Download All Models](https://drive.google.com/file/d/1IfW__wQJzXtK4Bfmasa64UZSDGYEmGSk/view?usp=sharing)** 
  - **[Full Project](https://drive.google.com/file/d/11edT6o4tqc_-JZXA8T22hJvRbFS-OGrj/view?usp=drive_link)**

-----

## 🚀 How to Run

### Full End-to-End Pipeline

To run the entire process, use `main.py`.

```bash
python main.py --video_file "test.mp4" --output_file "output.mp4"
```

This command will:

1.  Extract audio and transcribe with **Whisper**.
2.  Translate English → Telugu using **NLLB**.
3.  Generate Telugu speech with **MMS-TTS**.
4.  Convert to the original speaker’s voice with **RVC**.
5.  Sync lips with **Wav2Lip** and save the final video.

### Lip-Sync Only

If you already have a dubbed video and the target audio, you can run the lip-sync module alone.

```bash
python lip.py --input_video dubbed_test.mp4 --audio translated_audio.wav --output_video final_output.mp4
```

-----

## 🧠 My Development Journey

### Idea 1: Direct Speech-to-Speech

  - **Approach**: Use a model like Google's Translatotron for direct audio-to-audio translation.
  - **Result**: Failed in practice. The model was too complex and unreliable, especially with limited compute.

### Idea 2: ASR → NMT → TTS → Voice Cloning

  - **Approach**: A standard pipeline, but using a voice cloning model at the end.
  - **Result**: This worked for English but failed when cloning for Telugu. Training a custom voice cloning model was not feasible.

### Idea 3: Voice Conversion with RVC (Breakthrough 💡)

  - **Approach**: Instead of full voice cloning, I used **RVC (Retrieval-based Voice Conversion)**.
  - **Result**: Success\! I trained a model on \~15 minutes of speech and it worked remarkably well. This approach is practical, efficient, and language-independent.

-----

## 📌 Additional Notes

  - The default resolution for lip-sync is **480p**, which is CPU-friendly. You can increase it to **1080p** if you have a GPU.
  - The `wav2lip_gan.pth` checkpoint gives sharper facial results.
  - You can swap models to support any target language and retrain RVC for any speaker's voice.
-----

## Special Thanks to

A thank you to **[Revelli Eshwar](https://github.com/EshwarRevelli)** for their support in this project.

  - **📧 [Email](mailto:revellieshwar@gmail.com)**
  - **💻 [GitHub](https://github.com/EshwarRevelli)**
  - **🔗 [LinkedIn](https://www.linkedin.com/in/eshwar-revelli-75b1a12aa/)**
-----

## 📬 Let’s Connect

  - **📧 [Email](mailto:srikarvardhan2005@gmail.com)**
  - **💻 [GitHub](https://github.com/M-SRIKAR-VARDHAN)**
  - **🔗 [LinkedIn](https://www.linkedin.com/in/srikar-vardhan/)**
  - **📚 [Google Scholar](https://scholar.google.com/citations?user=3X9GIJ8AAAAJ&hl=en)** 
  - **📄 [Resume](https://drive.google.com/file/d/1TKS_ZcytGK2MEh5jNeRXatgfw2FPMYoA/view?usp=sharing)** 
-----

[![Star History Chart](https://api.star-history.com/svg?repos=M-SRIKAR-VARDHAN/speech-to-speech-with-lipsync&type=Date)](https://star-history.com/#M-SRIKAR-VARDHAN/speech-to-speech-with-lipsync&Date)
<!-- end list -->

