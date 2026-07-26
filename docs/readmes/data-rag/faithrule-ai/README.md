<!-- source: https://github.com/AsadRaza067/FaithRule-AI.git sha: 7e9b80c01d7fa6597aafc15d5df7f8de2da28648 readme: main/README.md -->
# AsadRaza067/FaithRule-AI

FaithRule AI: A clinical decision support system using faithful rule extraction from LLMs. Extracts symbolic IF-THEN rules from chain-of-thought reasoning for clinical trial eligibility screening. Features a FastAPI backend and Next.js frontend with faithfulness scoring, experiment tracking, and evidence retrieval.

---

# Faithful Rule Extraction from Large Language Models For High-Stakes Decision Support — A Pilot Study on Clinical Trial Eligibility

<div align="center">

![FaithRule AI](https://img.shields.io/badge/FaithRule-AI-blue?style=for-the-badge&logo=medical-cross)
![Python](https://img.shields.io/badge/Python-3.9+-green?style=for-the-badge&logo=python)
![Next.js](https://img.shields.io/badge/Next.js-15-black?style=for-the-badge&logo=next.js)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-teal?style=for-the-badge&logo=fastapi)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A clinical decision support system that extracts transparent, auditable IF-THEN rules from LLM chain-of-thought reasoning for clinical trial eligibility screening.**

</div>

---

## Overview

Large language models show real promise for automating clinical trial eligibility screening, but their opaque reasoning makes them difficult to trust in safety-critical settings. **FaithRule AI** addresses this by implementing **RuleDistill** — a post-hoc pipeline that converts LLM chain-of-thought explanations into symbolic IF-THEN rules, scored by a custom **Faithfulness Score (𝒻)** that measures how grounded each rule is in its source reasoning.

A pilot study on **50 manually annotated eligibility triplets** from **92 real ClinicalTrials.gov trials** demonstrated:

| Metric | Result |
|---|---|
| Mean Faithfulness Score (𝒻) | **0.714** |
| LLM Baseline Accuracy | **68.0%** |
| Rule Accuracy Retention | **93%** |
| Average Rule Complexity (κ) | **2.5 antecedents** |

---

## Features

- **Clinical Trial Eligibility Chat** — Ask any eligibility question in natural language
- **Experiment Tracking** — Full experiment history with faithfulness metrics and methodology transparency
- **Research Analytics Dashboard** — Faithfulness trends, baseline comparisons, performance metrics
- **Evidence Viewer** — Browse and export clinical evidence with source tracing
- **Rules Explorer** — View and explain extracted IF-THEN rules
- **AI-Powered Q&A** — Ask the AI to explain any rule or experiment result
- **Demo Mode** — Fully functional frontend with local AI fallback (no cloud API needed)

---

## Interface Screenshots

### Landing Page
<div align="center">
  <img src="docs/images/landing-1.png" alt="Landing Page Hero" width="800"/>
  <img src="docs/images/landing-2.png" alt="Features Section" width="800"/>
  <img src="docs/images/landing-3.png" alt="Pipeline Architecture" width="800"/>
  <img src="docs/images/landing-4.png" alt="Experimental Results" width="800"/>
  <img src="docs/images/landing-5.png" alt="Call to Action" width="800"/>
</div>

### Authentication
<div align="center">
  <img src="docs/images/auth-1.png" alt="Login Page" width="800"/>
  <img src="docs/images/auth-2.png" alt="Signup Page" width="800"/>
</div>

### Clinical Chat Interface
<div align="center">
  <img src="docs/images/chat-1.png" alt="Chat Interface" width="800"/>
  <img src="docs/images/chat-2.png" alt="Chat with AI Response" width="800"/>
  <img src="docs/images/chat-3.png" alt="Chat with Evidence" width="800"/>
  <img src="docs/images/chat-4.png" alt="Chat with Metrics" width="800"/>
</div>

### Analytics Dashboard
<div align="center">
  <img src="docs/images/analytics-1.png" alt="Analytics Overview" width="800"/>
  <img src="docs/images/analytics-2.png" alt="Faithfulness Trends" width="800"/>
  <img src="docs/images/analytics-3.png" alt="Baseline Comparison" width="800"/>
  <img src="docs/images/analytics-4.png" alt="Experiment History" width="800"/>
</div>

### Experiments Tracking
<div align="center">
  <img src="docs/images/experiments-1.png" alt="Experiments List" width="800"/>
  <img src="docs/images/experiments-2.png" alt="Experiment Detail - Metrics" width="800"/>
  <img src="docs/images/experiments-3.png" alt="Experiment Detail - Methodology" width="800"/>
  <img src="docs/images/experiments-4.png" alt="Faithfulness Formula" width="800"/>
  <img src="docs/images/experiments-5.png" alt="Signal Breakdown" width="800"/>
  <img src="docs/images/experiments-6.png" alt="Ask AI" width="800"/>
</div>

### Rules Explorer
<div align="center">
  <img src="docs/images/rules-1.png" alt="Rules List" width="800"/>
  <img src="docs/images/rules-2.png" alt="Rule Detail" width="800"/>
  <img src="docs/images/rules-3.png" alt="Add Rule Modal" width="800"/>
  <img src="docs/images/rules-4.png" alt="Rules Statistics" width="800"/>
</div>

### Evidence Viewer
<div align="center">
  <img src="docs/images/evidence-1.png" alt="Evidence List" width="800"/>
  <img src="docs/images/evidence-2.png" alt="Evidence Detail" width="800"/>
  <img src="docs/images/evidence-3.png" alt="Evidence Sources" width="800"/>
  <img src="docs/images/evidence-4.png" alt="Evidence Rules" width="800"/>
  <img src="docs/images/evidence-5.png" alt="Evidence Export" width="800"/>
</div>

### Comparison Dashboard
<div align="center">
  <img src="docs/images/comparison-1.png" alt="Comparison Overview" width="800"/>
  <img src="docs/images/comparison-2.png" alt="Model Comparison" width="800"/>
  <img src="docs/images/comparison-3.png" alt="Performance Metrics" width="800"/>
</div>

### Clinical Trials Explorer
<div align="center">
  <img src="docs/images/trials-1.png" alt="Trials List" width="800"/>
  <img src="docs/images/trials-2.png" alt="Trial Detail" width="800"/>
</div>

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 15, TypeScript, Tailwind CSS |
| Backend | FastAPI, Python 3.9+ |
| LLM | Llama-3-8B-Instruct via Ollama (local, zero cost) |
| Database | SQLite (faithrule.db) |
| Deployment | Docker, Docker Compose, Kubernetes (k8s/) |

---

## Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- [Ollama](https://ollama.ai) with `llama3` model (optional — demo mode works without it)

### One-Click Launch (Windows)
```bash
# Double-click START.bat
# OR run in PowerShell:
.\START.ps1
```

### Manual Setup
```bash
# Backend
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 8001

# Frontend (separate terminal)
cd frontend
npm install
npm run dev
```

Open **http://localhost:3000** in your browser.

---

## Project Structure

```
FaithRule-AI/
├── api/                  # FastAPI backend
│   ├── main.py           # App entry point
│   ├── database.py       # Database models & queries
│   ├── routes/           # API route handlers
│   ├── services/         # Business logic
│   └── schemas/          # Pydantic models
├── frontend/             # Next.js frontend
│   └── app/
│       ├── chat/         # Clinical chat interface
│       ├── analytics/    # Research analytics dashboard
│       ├── experiments/  # Experiment tracking
│       ├── evidence/     # Evidence viewer
│       ├── trials/       # Clinical trials explorer
│       └── rules/        # Rules explorer
├── faithfulness/         # Faithfulness Score computation
├── confidence/           # Confidence scoring
├── consistency/          # Consistency checking
├── rule_extractor/       # IF-THEN rule extraction engine
├── retriever/            # Evidence retrieval
├── embeddings/           # Embedding generation
├── vector_db/            # Vector database
├── llm/                  # LLM interface (Ollama)
├── explainability/       # Explainability modules
├── evidence/             # Evidence processing
├── config/               # App configuration
├── data/                 # Data pipeline
├── nginx/                # Nginx reverse proxy config
├── k8s/                  # Kubernetes deployment manifests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── START.bat / START.ps1 # One-click launchers
```

---

## The Faithfulness Score

The core contribution of this system is the **Faithfulness Score 𝒻**, defined as:

$$\mathcal{F}(\rho, R) = \frac{2 \cdot \mathcal{S}(\rho, R) \cdot \mathcal{E}(\rho, R)}{\mathcal{S}(\rho, R) + \mathcal{E}(\rho, R)}$$

Where:
- **𝒮(ρ, R)** — Word-overlap semantic similarity between extracted rule ρ and source reasoning chain R
- **𝓔(ρ, R)** — Entailment score: fraction of content words in ρ that appear in R

Rules with 𝒻 < 0.60 are automatically flagged for human review.

---

## Research Paper

This system is the implementation of the research paper:

> **Faithful Rule Extraction from Large Language Models for High-Stakes Decision Support: A Pilot Study on Clinical Trial Eligibility**
> Asad Raza

---

## Keywords

`large-language-models` `clinical-NLP` `rule-extraction` `explainable-AI` `chain-of-thought` `clinical-trials` `faithfulness` `trustworthy-AI` `symbolic-distillation` `llama3` `ollama` `fastapi` `nextjs` `clinical-decision-support` `eligibility-screening`

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

## Author

**Asad Raza**
📧 asadraza0667@gmail.com
