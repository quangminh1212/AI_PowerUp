# AudioGPT: Understanding and Generating Speech, Music, Sound, and Talking Head

[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2304.12995)
[![GitHub Stars](https://img.shields.io/github/stars/AIGC-Audio/AudioGPT?style=social)](https://AIGC-Audio/AudioGPT)
![visitors](https://visitor-badge.glitch.me/badge?page_id=AIGC-Audio.AudioGPT)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-blue)](https://huggingface.co/spaces/AIGC-Audio/AudioGPT)


We provide our implementation and pretrained models as open source in this repository.


## Get Started

Please refer to [run.md](run.md)


## Capabilities

Here we list the capability of AudioGPT at this time. More supported models and tasks are coming soon. For prompt examples, refer to [asset](assets/README.md).

Currently not every model has repository.
### Speech
|            Task            |   Supported Foundation Models   | Status |
|:--------------------------:|:-------------------------------:|:------:|
|       Text-to-Speech       | [FastSpeech](https://ming024/FastSpeech2), [SyntaSpeech](https://yerfor/SyntaSpeech), [VITS](https://jaywalnut310/vits) |  Yes (WIP)   |
|       Style Transfer       |         [GenerSpeech](https://Rongjiehuang/GenerSpeech)         |  Yes   |
|     Speech Recognition     |           [whisper](https://openai/whisper), [Conformer](https://sooftware/conformer)           |  Yes   |
|     Speech Enhancement     |          [ConvTasNet]()         |  Yes (WIP)   |
|     Speech Separation      |          [TF-GridNet](https://arxiv.org/pdf/2211.12433.pdf)         |  Yes (WIP)   |
|     Speech Translation     |          [Multi-decoder](https://arxiv.org/pdf/2109.12804.pdf)      |  WIP   |
|      Mono-to-Binaural      |          [NeuralWarp](https://fdarmon/NeuralWarp)         |  Yes   |

### Sing

|           Task            |   Supported Foundation Models   | Status |
|:-------------------------:|:-------------------------------:|:------:|
|       Text-to-Sing        |         [DiffSinger](https://MoonInTheRiver/DiffSinger), [VISinger](https://jerryuhoo/VISinger)          |  Yes (WIP)   |

### Audio
|          Task          | Supported Foundation Models | Status |
|:----------------------:|:---------------------------:|:------:|
|     Text-to-Audio      |      [Make-An-Audio]()      |  Yes   |
|    Audio Inpainting    |      [Make-An-Audio]()      |  Yes   |
|     Image-to-Audio     |      [Make-An-Audio]()      |  Yes   |
|    Sound Detection     |    [Audio-transformer](https://RetroCirce/HTS-Audio-Transformer)    | Yes    |
| Target Sound Detection |    [TSDNet](https://gy65896/TSDNet)    |  Yes   |
|    Sound Extraction    |    [LASSNet](https://liuxubo717/LASS)    |  Yes   |


### Talking Head

|           Task            |   Supported Foundation Models   |   Status   |
|:-------------------------:|:-------------------------------:|:----------:|
|  Talking Head Synthesis   |          [GeneFace](https://yerfor/GeneFace)           | Yes (WIP)  |


## Acknowledgement
We appreciate the open source of the following projects:

[ESPNet](https://espnet/espnet) &#8194;
[NATSpeech](https://NATSpeech/NATSpeech) &#8194;
[Visual ChatGPT](https://microsoft/visual-chatgpt) &#8194;
[Hugging Face](https://huggingface) &#8194;
[LangChain](https://hwchase17/langchain) &#8194;
[Stable Diffusion](https://CompVis/stable-diffusion) &#8194;

