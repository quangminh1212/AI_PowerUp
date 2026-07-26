<!-- source: https://github.com/numairh2/A-Constitutional-AI-Faithfulness-Detector.git sha: b51f0bd4faf271370daf01a2a70ddca986247076 readme: main/README.md -->
# numairh2/A-Constitutional-AI-Faithfulness-Detector

This project studies faithfulness in chain-of-thought reasoning by testing whether unfaithful reasoning forms a distinct representational direction in large language models. We fine-tune models on unfaithful CoT data, use model diffing to find correlated features, and develop methods to detect or steer faithfulness for more transparent AI reasoning

---

# Quick Start Guide - Constitutional AI Faithfulness Detector

## 🚀 Get Running in 30 Minutes

This is the fastest path to get the project working. For detailed explanations, see [SETUP.md](SETUP.md).

---

## Prerequisites

- Python 3.9+
- 50GB free disk space
- (Optional) NVIDIA GPU with 16GB+ VRAM

---

## Setup Commands

Copy and paste these commands in order:

### 1. Create Project (2 minutes)

```bash
# Create directory
mkdir constitutional-ai-faithfulness
cd constitutional-ai-faithfulness

# Initialize git
git init
git remote add origin https://github.com/YOUR_USERNAME/constitutional-ai-faithfulness.git
```

### 2. Create Environment (3 minutes)

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Upgrade pip
pip install --upgrade pip
```

### 3. Install Packages (5 minutes)

Create `requirements.txt`:
```txt
torch>=2.0.0
transformers>=4.35.0
accelerate>=0.24.0
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
tqdm>=4.66.0
jupyter>=1.0.0
wandb>=0.15.0
pyyaml>=6.0
```

Install:
```bash
pip install -r requirements.txt
```

### 4. Create Structure (1 minute)

```bash
# Create directories
mkdir -p data/{raw,processed,synthetic}
mkdir -p models/{base,finetuned,diffed}
mkdir -p src/experiments
mkdir -p scripts notebooks results docs examples

# Create Python package files
touch src/__init__.py
touch src/experiments/__init__.py
```

### 5. Download Files (Copy from provided outputs)

Copy these files to your repo:

```bash
# From provided files:
cp generate_full_dataset.py scripts/
cp download_model.py scripts/
cp setup_tracking.py scripts/
cp run_baseline.py src/experiments/
cp 02_baseline_experiments.ipynb notebooks/
```

### 6. Generate Data (2 minutes)

```bash
python scripts/generate_full_dataset.py
```

Output:
```
✓ Saved data/raw/comparative_all.json (250 pairs)
✓ Saved data/processed/train.json (525 examples)
✓ Saved data/processed/test.json (112 examples)
```

### 7. Download Model (10-15 minutes)

```bash
# For Llama (needs HuggingFace access)
huggingface-cli login  # Enter your token
python scripts/download_model.py

# Or smaller model (no login needed)
python scripts/download_model.py --model microsoft/Phi-3-mini-4k-instruct
```

### 8. Setup Tracking (3 minutes)

```bash
python scripts/setup_tracking.py
# Follow prompts to login to WandB
```

### 9. Run First Experiment (5 minutes)

```bash
# Test with 10 examples
python src/experiments/run_baseline.py --num-samples 10
```

Expected output:
```
IPHR Rate: 20.00%
Avg Faithfulness: 0.68
✓ Results saved to results/baseline/
```

---

## Verify Setup

```bash
# Check everything works
python -c "
import torch
import transformers
import json

print('✓ PyTorch:', torch.__version__)
print('✓ CUDA:', torch.cuda.is_available())
print('✓ Model:', Path('models/model_info.json').exists())
print('✓ Data:', len(json.load(open('data/processed/test.json'))))
"
```

---

## What You Have Now

```
constitutional-ai-faithfulness/
├── data/
│   ├── raw/comparative_all.json        # 250 question pairs
│   ├── processed/test.json             # Test set
│   └── synthetic/unfaithful_*.json     # 250+ examples
├── models/
│   ├── base/                           # Downloaded model
│   └── model_info.json                 # Model details
├── results/
│   └── baseline/
│       ├── baseline_summary.json       # Key metrics
│       └── baseline_results.json       # Full results
├── src/experiments/run_baseline.py     # Baseline script
├── notebooks/02_baseline_experiments.ipynb
└── scripts/
    ├── generate_full_dataset.py
    ├── download_model.py
    └── setup_tracking.py
```

---

## Next Steps

### Run Full Baseline (15 minutes)

```bash
python src/experiments/run_baseline.py
```

### Or Use Interactive Notebook

```bash
jupyter notebook notebooks/02_baseline_experiments.ipynb
```

### View Results

```bash
# Summary
cat results/baseline/baseline_summary.json

# WandB dashboard
open https://wandb.ai
```

---

## Quick Reference

### Activate Environment
```bash
source venv/bin/activate  # Do this every time
```

### Run Experiments
```bash
# Small test
python src/experiments/run_baseline.py --num-samples 10

# Full run
python src/experiments/run_baseline.py
```

### Check Status
```bash
# Model info
ls -lh models/

# Data info
ls -lh data/processed/

# Results
ls -lh results/baseline/
```

---

## Troubleshooting Quick Fixes

### Out of Memory
```bash
python scripts/download_model.py --use-8bit
```

### Import Errors
```bash
source venv/bin/activate
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### CUDA Not Found
```bash
# Install PyTorch with CUDA
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### Model Access Denied
```bash
# For Llama models:
# 1. Go to https://huggingface.co/meta-llama/Llama-3-8B-Instruct
# 2. Request access
# 3. Run: huggingface-cli login
```

---

## 📚 Full Documentation

- **Setup Details**: [SETUP.md](SETUP.md)
- **Phase 2 Guide**: [PHASE2_GUIDE.md](PHASE2_GUIDE.md)
- **Dataset Info**: [DATASET_README.md](DATASET_README.md)

---

## ✅ Success Checklist

After following this guide:

- [ ] Virtual environment activated
- [ ] All packages installed
- [ ] Data generated (750+ examples)
- [ ] Model downloaded (~15GB)
- [ ] Tracking setup (WandB)
- [ ] Baseline experiments run
- [ ] Results in `results/baseline/`

**All done?** You're ready for Phase 2! 🎉

---

**Time**: ~30 minutes  
**Difficulty**: Beginner  
**Next**: See [PHASE2_GUIDE.md](PHASE2_GUIDE.md) for experiments

For detailed explanations of each step, see the full [SETUP.md](SETUP.md) guide.