<!-- source: https://github.com/The-Adimension/Agent-ProSAT.git sha: 84c548c5c5ccef3af86a6c26787fea70ef91aaa3 readme: main/README.md -->
# The-Adimension/Agent-ProSAT

Agent-driven Programmatic Solver Traces for Alice in Wonderland puzzles!

---

<div align="center">
  
# Agent-ProSAT: Programmatic Solver Augmented Traces
**The Agent-Driven Base for Programmatic Verifiable CoT for Alice in Wonderland**
Complete CoT & Latest prosat.py are available on 

[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20Dataset-prosat--nemotron--alice--in--wonderland--traces-blue)](https://huggingface.co/datasets/The-Adimension/prosat-nemotron-alice-in-wonderland-traces/)

---
## Example: Agent-ProSAT runs for 20-Minute Agent Iteration Showcase

> Watch how Agent-ProSAT can iteratively develop programmatic verifiable solvers. The run below took approximately 20 minutes using the Gemini CLI (Model: Gemini 1.5 Pro High).

https://github.com/user-attachments/assets/e5828d97-b6d1-4642-9ab4-1e095f6de74f


| **At Baseline:** | **After 20 Minutes of Autonomous Iteration:** |
| :---: | :---: |
| <img width="100%" alt="Baseline metrics" src="https://github.com/user-attachments/assets/a897eedb-eb99-4cc0-ae77-2a49ab0d80a3" /> | <img width="100%" alt="Metrics after 20 minutes" src="https://github.com/user-attachments/assets/49f267c1-1535-4f9a-81d0-7ce9be11997c" /> |

## **Complete Run and Dataset Output:**
The Agent-ProSAT local runs iteratively developed the prosat.py & dataset on HuggingFace

---

[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20Dataset-prosat--nemotron--alice--in--wonderland--traces-blue)](https://huggingface.co/datasets/The-Adimension/prosat-nemotron-alice-in-wonderland-traces/)

---

| &nbsp; | &nbsp; |
| :---: | :---: |
| <img width="100%" alt="image" src="https://github.com/user-attachments/assets/930ae1f4-ca91-474d-bc9c-adcb73d6e5c1" /> | <img width="100%" alt="image" src="https://github.com/user-attachments/assets/e7db7ddc-ca2a-4da8-add8-1659eaabd1da" /> |

---

</div>


## System Overview

In programmatic solver augmentation, an autonomous loop (`agent.py`) iteratively modifies a Python solver engine (`prosat.py`) using feedback from an evaluation script (`assess.py`). The solver engine discovers structural rules from prompt input examples (`data_set`), builds symbolic or constraint-propagation representations, and computes solutions.

When a puzzle is solved, `prosat.py` outputs a structured item containing:
- `computed_answer`: The string result produced by the programmatic solver.
- `reasoning`: A step-by-step trace documenting intermediate algorithmic states (such as linear system matrices, character lookup tables, or ordinal arithmetic sequences).

---

## System Architecture & Core Files

```text
├── prosat.py              # Programmatic solver & trace synthesis engine (mutable target)
├── agent.py               # Autonomous modification loop with TSV trajectory parsing
├── assess.py              # Evaluation script with target answer isolation verification
├── preflight.py           # Environment, Python version, and compilation checks
├── directives.md          # Instructions and constraints for the coding agent
├── runs.tsv               # Iteration metrics log (solved counts, trace lengths, git hashes)
├── tests/                 # Verification and comparative evaluation scripts
│   ├── verify_blind.py    # Evaluates computed_answer equality under dummy target inputs
│   └── compare_solvers.py # Side-by-side execution comparison against historical script
├── AIWL/                  # Benchmark dataset CSV files (train.csv, test.csv)
├── benchmark_splits/      # Held-out evaluation and validation ID splits
├── materials/             # Historical base scripts and human reference documentation
└── Outputs/               # Timestamped session logs, generated scripts, and backups

```

### 1. Solver Engine: `prosat.py`

Implements modular sub-solvers across 6 puzzle categories:

* **`solve_numeral`**: Multi-base numeric and Roman numeral conversions.
* **`solve_unit_conversion` & `solve_gravity**`: Physical equation evaluation and linear regressions (`_solve_unit_round_fallback`, `_solve_gravity_round_fallback`).
* **`solve_cipher` & `solve_binary**`: Caesar/substitution cipher mappings and linear equation solvers over $\mathbb{F}_2$.
* **`solve_equation_transform`**: Symbolic transformation framework evaluating operator templates, position transducers, ordinal transformations, and lookup tables.

> **Target Answer Isolation Requirement (T1 Check):**
> Solvers receive the dataset ground-truth string (`answer`) as an argument for post-hoc validation (`--validate`) or trace formatting. **Solvers do not access or condition logic on `answer` during pattern detection, rule deduction, or prediction computation.**

### 2. Evaluation Script: `assess.py`

Measures quantitative metrics across benchmark datasets:

* **Coverage:** Solved puzzle count and percentage (`total_solved / total_puzzles`).
* **Correctness:** Exact string match percentage (`correct / total_solved`).
* **Trace Metrics:** Average character count (`avg_chars`) and estimated token count (`avg_tokens`).
* **Twin Blind Check:** Evaluates whether `computed_answer` is independent of the target answer argument:
1. *Unblinded Pass:* Evaluates `prosat.py` passing the real dataset `answer`.
2. *Blinded Pass:* Re-evaluates `prosat.py` passing `answer = "BLIND_DUMMY_GATE_CHECK"`.


*Note: If any solved puzzle returns a different `computed_answer` between unblinded and blinded passes, `assess.py` sets `twin_blind_check = False`, scores `correctness_pct = 0.0`, and records the mismatch count (`peeking_violations`).*

### 3. Autonomous Driver: `agent.py`

Executes the iterative modification loop using a coding agent (`claude`, `codex`, or `aider`):

* Identifies the category with the lowest current solve coverage (`coverage_pct`).
* Reads the last 5 entries from `runs.tsv` (`get_trajectory_feedback`) and formats them into the prompt so the agent sees past `[ACCEPTED]` vs. `[REJECTED]` statuses and exact notes.
* Evaluates modified code via `assess.py`. If `twin_blind_check` is True, `correctness_pct` is 100.0%, and `total_solved` increases (or stays equal with shorter traces), `agent.py` executes `git commit`. Otherwise, it executes `git checkout` to revert the edit.

### 4. Verification Scripts (`tests/`)

* **`tests/verify_blind.py`**: Executes unblinded vs. blinded passes across random samples (e.g., `-n 1000` or `--all`) under controlled random seeds (`random.seed(12345)`). Reports the exact count of computed answer matches and mismatches per puzzle category.
* **`tests/compare_solvers.py`**: Runs `prosat.py` alongside the historical base script (`materials/base_prosat_script.txt`) across 6 dataset puzzles under unblinded vs. blinded target answer conditions and displays the resulting `computed_answer` strings.

---

## 🚀 Quickstart & Operational Commands

All scripts use relative path resolution (`Path(__file__)`) and run from any working directory across Windows, Linux, and macOS.

### 1. Environment & Preflight Check

Verify Python version (>=3.10), dependency imports (`numpy`, `tqdm`), and syntax compilation:

```bash
python preflight.py

```

### 2. Baseline Evaluation

Compute coverage, correctness, trace metrics, and the real vs. dummy target answer check:

```bash
python assess.py --engine prosat.py

```

*(Optional) To format output as JSON:*

```bash
python assess.py --json

```

### 3. Run Audit Scripts

Evaluate computed answer equality across unblinded vs. blinded passes on 1,000 samples:

```bash
python tests/verify_blind.py -n 1000

```

Compare `prosat.py` execution against the historical base script across 6 dataset puzzles:

```bash
python tests/compare_solvers.py

```

### 4. Execute Autonomous Modification Loop

**Step 1:** Launch your preferred agent and direct them to read `START.md`.

**Step 2:** Start the script-driven modification loop (`agent.py`) for a specified number of iterations:

```bash
python agent.py -n 20

```

*(Optional) To run a baseline evaluation only without invoking the coding agent:*

```bash
python agent.py --dry-run

```

---

## The `materials/` Directory

The `materials/` directory contains historical scripts (like `base_prosat_script.txt`) to serve as a baseline reference for human users and comparative scripts (used by `compare_solvers.py`). The autonomous loop (`agent.py`) modifies `prosat.py` and evaluates via `assess.py`.

```
