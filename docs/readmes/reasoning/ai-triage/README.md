<!-- source: https://github.com/zhiruiluo/ai-triage.git sha: 30be1a9c13f0e7160484aebccaa5b24515b26823 readme: main/README.md -->
# zhiruiluo/ai-triage

AI-powered triage system for Emergency Severity Index (ESI) classification using LLMs with chain-of-thought reasoning and skill-based architecture.

---

# AI Triage System

**Emergency Severity Index (ESI) Classification using Large Language Models**

![Python](https://img.shields.io/badge/Python-3.8+-green)
![Framework](https://img.shields.io/badge/Framework-LangChain-orange)
![Status](https://img.shields.io/badge/Status-Active-blue)

---

## Overview

An AI system that classifies emergency department patients into ESI levels (1-5) based on clinical vignettes using large language models. The system is built on a modular skill framework with support for multiple reasoning modes, API endpoints, and web interface.

### Key Components

- **LLM-based Classification**: Multiple classifier modes for ESI assignment
- **Skill Framework**: Modular, composable clinical reasoning skills
- **Evaluation Framework**: Batch experiment execution with metrics tracking
- **API Server**: FastAPI backend for programmatic access
- **Web Interface**: Streamlit UI for interactive classification
- **Configuration System**: YAML-based configuration for models, prompts, and parameters

---

## Installation

### Requirements
- Python 3.8+
- pip

### Basic Installation

```bash
pip install -e "."
```

### Installation with Extras

```bash
# For API server
pip install -e ".[api]"

# For web UI
pip install -e ".[web]"

# For development
pip install -e ".[dev]"

# For all features
pip install -e ".[all]"
```

---

## Quick Start

### Single Classification

```python
from triage_agent.classifier import classify_esi

result = classify_esi(
    patient_record="55-year-old with chest pain, BP 90/60, HR 120",
    llm_provider="openai",
    model_name="gpt-4"
)

print(f"ESI Level: {result['esi_level']}")
print(f"Rationale: {result['rationale']}")
```

### Batch Evaluation

```bash
python -m triage_agent.evaluation \
  --dataset dataset/test.tsv \
  --output results/
```

### API Server

```bash
# Start the API server
uvicorn triage_agent.api.app:app --host 0.0.0.0 --port 8000

# Example request
curl -X POST http://localhost:8000/classify \
  -H "Content-Type: application/json" \
  -d '{"patient_record": "Clinical vignette here"}'
```

### Web Interface

```bash
# Terminal 1: Start API
uvicorn triage_agent.api.app:app --reload

# Terminal 2: Start Web UI
streamlit run web_ui/app.py
```

Access the interface at http://localhost:8501

---

## Project Structure

```
TriageAgent/
├── src/triage_agent/
│   ├── skills/                 # Skill framework implementations
│   ├── api/                    # FastAPI server
│   ├── evaluation/             # Evaluation framework
│   ├── classifier.py           # Main classification function
│   └── utils/                  # Utility functions
├── web_ui/                     # Streamlit web interface
├── skills/                     # Skill configurations
│   ├── esi-extraction/         # Clinical fact extraction
│   ├── esi-composition/        # ESI assignment logic
│   └── esi-pipeline/           # Combined pipeline
├── tests/                      # Test suite
├── docs/                       # Documentation
├── config/                     # Configuration files
├── pyproject.toml              # Project metadata
└── README.md                   # This file
```

---

## Documentation

### Finding the Right Document

- **Getting Started?** → [Quick Start Guide](docs/guides/QUICK_START.md)
- **Want to Run Evaluation?** → [Evaluation Guide](docs/guides/EVALUATION_GUIDE.md)
- **Building with the API?** → [API Integration Guide](docs/guides/API_GUIDE.md)
- **Deploying to Production?** → [Deployment Guide](docs/guides/DEPLOYMENT.md)
- **Understanding the System Architecture?** → [System Overview](docs/architecture/SYSTEM_OVERVIEW.md)
- **Deep dive into a Component?** → [Architecture Docs](docs/architecture/)
- **Viewing Project History?** → [Phase Reports](docs/phase-reports/)
- **Looking for Historical Analysis?** → [Archive](docs/archive/)
- **Reviewing All Standards?** → [Documentation Protocol](DOCUMENTATION_PROTOCOL.md)

### Complete Documentation Index

**Root Documentation** (Single Source of Truth):
- [README.md](README.md) - Project overview, performance data, and quick start
- [TODO.md](TODO.md) - Active roadmap and current tasks
- [DOCUMENTATION_PROTOCOL.md](DOCUMENTATION_PROTOCOL.md) - Documentation standards and organization

**Performance & Evaluation**:
- 🏆 [Comprehensive Evaluation Metrics Report](../report/comprehensive_evaluation_metrics_20260202.md) - Complete Feb 2 evaluation with 7 approaches, 300 cases, detailed analysis
- [Archive Index](docs/archive/ARCHIVE_INDEX.md) - Historical documentation reference

**Guides** (Step-by-step instructions):
- [Evaluation Guide](docs/guides/EVALUATION_GUIDE.md) - How to run evaluations
- [Quick Start Guide](docs/guides/QUICK_START.md)
- [Installation Guides](docs/guides/) - Docker, Conda, pip setup
- [API Integration Guide](docs/guides/API_GUIDE.md)
- [Deployment Guide](docs/guides/DEPLOYMENT.md)

**Architecture** (Technical design & specifications):
- [System Overview](docs/architecture/SYSTEM_OVERVIEW.md)
- **Core Systems**:
  - [Skill Framework Architecture](docs/architecture/SKILL_FRAMEWORK_DESIGN.md) - Modular, composable skill framework
  - [Worker Process & Execution](docs/architecture/WORKER_EXECUTION_DESIGN.md) - Experiment execution with checkpointing
  - [REST API Specification](docs/architecture/API_SPECIFICATION.md) - API endpoint documentation
- **Analysis Systems**:
  - [Analysis Pipeline Design](docs/architecture/ANALYSIS_PIPELINE_DESIGN.md) - 5-step orchestrator
  - [Composition Engine Design](docs/architecture/COMPOSITION_ENGINE_DESIGN.md) - ESI decision tree
  - [Metrics Framework Design](docs/architecture/METRICS_FRAMEWORK.md) - Clinical safety & performance metrics
- **Data & Pipelines**:
  - [Experiment Persistence Design](docs/architecture/EXPERIMENT_PERSISTENCE_DESIGN.md)
  - [Hybrid Pipeline Design](docs/architecture/HYBRID_PIPELINE_DESIGN.md)
  - [RAG Pipeline Design](docs/architecture/RAG_PIPELINE_DESIGN.md)
  - [Vital Signs System Design](docs/architecture/VITAL_SIGNS_SYSTEM_DESIGN.md)

---

## Classifier Modes

The system implements **7 evaluated ESI classification approaches** (from Feb 2, 2026 comprehensive evaluation):

**Traditional Approaches**:
1. **one-round** - Single-shot baseline classification (0.58s, 55.1% accuracy)
2. **cot** - Chain-of-thought reasoning (1.97s, 45.8% accuracy)
3. **selfcheck** - Self-verification reasoning (3.28s, 58.3% accuracy)
4. **decomposite** - Task decomposition approach (3.13s, 58.2% accuracy)
5. **rag_prompt** - RAG with direct classification (1.60s, 46.8% accuracy)

**RAG-based Approaches** (Recommended):
6. **rag_baseline** - Selective context retrieval (0.95s, 62.6% accuracy, 31.6% under-triage)
7. **rag_full** 🥇 - Full ESI handbook context (1.55s, **67.4% accuracy, 10.5% under-triage**)

✨ **Note**: All classifiers now report accurate metrics. Fixed Feb 2, 2026: Traditional approaches previously showed 0% accuracy due to ESI level extraction bug in response parsing.

See [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) for complete implementation details of all classifiers.

---

## Evaluation Framework

Batch evaluation capabilities include:

- Experiment execution on datasets
- Metric computation (accuracy, precision, recall, F1)
- Performance tracking across classifier modes
- Result persistence and resumption
- Cross-model comparison

---

## API Endpoints

REST API provided via FastAPI:

- `POST /classify` - Single patient classification
- `POST /evaluate` - Batch evaluation on dataset
- `GET /experiments` - List completed experiments
- `GET /experiments/{id}` - Experiment details
- `GET /health` - API health check

Full API documentation available at `/docs` when server is running.

---

## Configuration

Configuration is managed via YAML files in the `skills/` directory:

```yaml
model:
  provider: "openai"
  name: "gpt-4-turbo"
  temperature: 0.7

pipeline:
  extraction:
    enabled: true
  composition:
    enabled: true
```

Environment variables override YAML settings.

---

## Testing

Run the test suite:

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_classifier.py

# Run with verbose output
pytest -v tests/
```

---

## Requirements

- Python 3.8+
- LangChain 0.1.0+
- Pandas 1.5.0+
- Pydantic 2.0.0+
- FastAPI 0.109.0+ (for API)
- Streamlit (for Web UI)

See `requirements.txt` for complete dependency list.

---

## Development

### Setup Development Environment

```bash
pip install -e ".[dev]"
pre-commit install
```

### Code Style

- **Black** for formatting
- **Ruff** for linting
- **MyPy** for type checking

```bash
make format  # Auto-format code
make lint    # Run linters
make type    # Run type checker
```

---

## Performance Evaluation

### 🎯 Latest Comprehensive Evaluation (Feb 2, 2026)

**Evaluation Summary**: 7 approaches tested on 300 clinical vignettes across 4 datasets

#### Performance Rankings

| Approach | Accuracy | Under-triage | Over-triage | Cost | Latency |
|----------|----------|--------------|-------------|------|----------|
| **rag_full** 🥇 | **67.4%** | **10.5%** | 22.1% | $0.000155 | 1.55s |
| rag_baseline | 62.6% | 31.6% | 5.9% | $0.000094 | 0.95s |
| decomposite | 58.2% | 26.9% | 15.0% | $0.000313 | 3.13s |
| selfcheck | 58.3% | 26.3% | 13.9% | $0.000328 | 3.28s |
| one-round | 55.1% | 36.2% | 8.5% | $0.000058 | 0.58s |
| rag_prompt | 46.8% | 34.6% | 18.6% | $0.000160 | 1.60s |
| cot | 45.8% | 35.9% | 18.4% | $0.000197 | 1.97s |

#### Key Findings

✅ **Best Overall**: `rag_full` with 67.4% accuracy and 10.5% under-triage rate

⚠️ **Clinical Safety**: Only `rag_full` maintains under-triage below 15% across all datasets (prevents dangerous under-treatment)

🔧 **Critical Bug Fixed**: Traditional approaches (cot, selfcheck, decomposite) previously showed 0% accuracy due to ESI extraction bug - now reporting correct metrics

📊 **Dataset Performance**:
- **Train_scenario** (85): rag_full 72.9%
- **Test-1** (71): rag_full 63.4%
- **Test-2** (72): rag_full 65.3% (most challenging)
- **Test-3** (72): rag_full 68.1%

### Production Recommendation

**Deploy `rag_full`** with these characteristics:
- ✅ Highest accuracy and lowest under-triage
- ✅ Acceptable latency (1.55s per case)
- ✅ Negligible cost ($1.55/month per 10K ED visits)
- ⚠️ Requires clinician review process for low-confidence cases

### Cost-Benefit Analysis

For a typical mid-size ED (10,000 cases/month):
- **one-round**: $0.58/month cost, but 3,620 under-triaged cases (UNSAFE)
- **rag_full**: $1.55/month cost, only 1,050 under-triaged cases (SAFE) ✅
- **Net benefit**: $0.97/month prevents 2,570 dangerous under-triaged cases

### Comprehensive Evaluation Report

For complete analysis including:
- Per-dataset breakdowns by ESI level
- Under-triage safety analysis
- Technical insights and limitations
- Deployment recommendations
- Roadmap for continued improvement

**See**: [Comprehensive Evaluation Metrics Report](../report/comprehensive_evaluation_metrics_20260202.md)

### Implementation Details

For complete technical documentation of all approaches:
- Function signatures and parameters
- Algorithm descriptions
- Prompt configurations
- Code references

See: [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)

### Run Your Own Evaluation

To run a comprehensive evaluation:

```bash
# Quick test (10 samples, ~2 minutes)
python comprehensive_evaluation.py --max-samples 10

# Full evaluation (300 samples, ~1 hour)
python comprehensive_evaluation.py
```

Results are saved to `comprehensive_results/` directory and timestamped JSON files.

---

## File Organization

The repository contains:

- Source code in `src/triage_agent/`
- Skills in `skills/`
- Web UI in `web_ui/`
- Tests in `tests/`
- Configuration in YAML files
- Documentation in `docs/`

---

## License

MIT License - See [LICENSE](LICENSE) file

---

## Support

For questions and support:

1. Check `docs/` for documentation
2. Review configuration examples in `skills/`
3. Consult test files in `tests/` for usage patterns
4. Review API documentation at `http://localhost:8000/docs`

---

**Version**: 0.6.0
**Status**: Beta
