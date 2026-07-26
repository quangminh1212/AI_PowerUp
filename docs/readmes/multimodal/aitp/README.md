<!-- source: https://github.com/Songan-Lab/AITP.git sha: ffd2b508fd53f25c31a2ddfa1ebc9bfeafe543fd readme: main/README.md -->
# Songan-Lab/AITP

[CVPR 2026 Findings] AITP: Traffic Accident Responsibility Allocation via Multimodal Large Language Models

---

# AITP: Artificial Intelligence Traffic Police

Official repository for **AITP: Traffic Accident Responsibility Allocation via Multimodal Large Language Model**.

## Overview

Traffic Accident Responsibility Allocation (TARA) is a challenging task that requires not only accident perception, but also causal reasoning and regulation-grounded judgment.  
To address this problem, we propose **AITP**, a multimodal large language model for traffic accident responsibility reasoning and allocation.

AITP improves traffic accident understanding through:
- **Progressive fine-tuning** from accident perception to responsibility reasoning
- **MCoT (Multimodal Chain-of-Thought)** for step-by-step reasoning
- **RAG (Retrieval-Augmented Generation)** for traffic regulation grounding

We further introduce **DecaTARA**, a unified benchmark covering ten interrelated traffic accident reasoning tasks.

## Status

This repository is currently under construction.

- [ ] Training code
- [ ] Inference code
- [ ] Evaluation scripts
- [ ] Dataset preparation pipeline
- [ ] Benchmark release

Code and benchmark will be released soon.

## Benchmark: DecaTARA

DecaTARA is a decathlon-style benchmark for multimodal traffic accident reasoning, containing:
- **67,941** annotated videos
- **195,821** question-answer pairs
- **10** interrelated traffic accident reasoning tasks

More details will be provided in the dataset release.

## Method

AITP is built upon Qwen3-VL and trained with a progressive four-stage strategy:
1. Non-accident initialization
2. Traffic accident detection
3. Traffic accident understanding
4. Traffic accident responsibility allocation

At inference time, AITP performs structured reasoning with MCoT and incorporates retrieved traffic regulations with RAG.

## Paper

**AITP: Traffic Accident Responsibility Allocation via Multimodal Large Language Model**  
Findings of CVPR 2026

> Paper link: coming soon

## Dataset

> Hugging Face: coming soon

## Citation

If you find this project useful, please consider citing:

```bibtex
@inproceedings{zhou2026aitp,
  title={AITP: Traffic Accident Responsibility Allocation via Multimodal Large Language Model},
  author={Zhou, Zijin and Zhang, Songan},
  booktitle={Findings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2026}
}
