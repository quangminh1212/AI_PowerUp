<div align="center">

[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/ibm-assetopsbench-badge.png)](https://mseep.ai/app/ibm-assetopsbench)

# AssetOpsBench

### AI Agents for Industrial Asset Operations & Maintenance

*A unified, open framework for building, orchestrating, and evaluating domain-specific AI agents in Industry 4.0.*

[![Stars](https://img.shields.io/github/stars/IBM/AssetOpsBench?style=for-the-badge&logo=github&color=yellow)](https://IBM/AssetOpsBench/stargazers)
[![Forks](https://img.shields.io/github/forks/IBM/AssetOpsBench?style=for-the-badge&logo=github)](https://IBM/AssetOpsBench/network/members)
[![License](https://img.shields.io/badge/License-Apache_2.0-green?style=for-the-badge)](LICENSE)
[![KDD 2026](https://img.shields.io/badge/KDD%202026-Accepted-0f62fe?style=for-the-badge)](#publications)
[![IJCAI 2026](https://img.shields.io/badge/IJCAI%202026-Live%20Competition-d02670?style=for-the-badge)](#ai-competitions)
[![CODS 2025](https://img.shields.io/badge/CODS%202025-500%2B%20Submissions-007d79?style=for-the-badge)](#ai-competitions)

[![AssetOps](https://img.shields.io/badge/Domain-Asset_Operations-blue)](#)
[![MultiAgentBench](https://img.shields.io/badge/Domain-Multi--agent_Bench-blue)](#)
[![EMNLP 2025](https://img.shields.io/badge/EMNLP--2025-Accepted-blueviolet)](#publications)
[![NeurIPS 2025](https://img.shields.io/badge/NeurIPS--2025-Accepted-blueviolet)](#publications)
[![AAAI 2026](https://img.shields.io/badge/AAAI--2026-Accepted-blueviolet)](#publications)
[![IAAI 2026](https://img.shields.io/badge/IAAI--2026-Accepted-blueviolet)](#publications)
[![ICLR 2026](https://img.shields.io/badge/ICLR--2026-Accepted-blueviolet)](#publications)
[![ACL 2026](https://img.shields.io/badge/ACL--2026-Accepted-blueviolet)](#publications)



📄 [**Paper**](https://arxiv.org/pdf/2506.03828) · 🤗 [**Dataset**](https://huggingface.co/datasets/ibm-research/AssetOpsBench) · 🎮 [**Playground**](https://huggingface.co/spaces/ibm-research/AssetOps-Bench) · 📢 [**IBM Blog**](https://research.ibm.com/blog/asset-ops-benchmark) · 🎥 [**Video**](https://www.youtube.com/watch?v=kXmBDMrKFjs) · 📊 [**Kaggle**](https://www.kaggle.com/benchmarks/ibm-research/asset-ops-bench) · 🚀 [**Colab**](https://colab.research.google.com/github/IBM/AssetOpsBench/blob/main-0.x/notebook/LLM_Agent.ipynb)

</div>

> [!IMPORTANT]
> 🎉 **AssetOpsBench is officially accepted at KDD 2026** (Datasets & Benchmarks Track), Jeju, South Korea, alongside our hands-on tutorial *Building Reliable Industrial Agents with MCP*. See [Publications](#publications) for the full list of 2025–2026 work.

---

## At a Glance

<table>
  <tr>
    <td align="center" width="16%"><b>9</b><br><sub>Asset classes</sub></td>
    <td align="center" width="16%"><b>141+</b><br><sub>Scenarios</sub></td>
    <td align="center" width="16%"><b>5</b><br><sub>Domain agents</sub></td>
    <td align="center" width="16%"><b>2</b><br><sub>Orchestration frameworks</sub></td>
    <td align="center" width="16%"><b>20+</b><br><sub>University extensions</sub></td>
    <td align="center" width="16%"><b>500+</b><br><sub>Competition submissions</sub></td>
  </tr>
</table>

**Built for:** maintenance engineers, reliability specialists, facility planners, and Industry 4.0 researchers.
**Powered by:** LLMs + Time Series Foundation Models, orchestrated over live sensor data and Industry 4.0 records (FMEA, work orders, alerts).
**Now with:** simplified interface and native **MCP (Model Context Protocol)** support.

---

## Quick Start

```bash
# Clone and install
git clone https://IBM/AssetOpsBench.git
cd AssetOpsBench
pip install -e .

# Try a scenario (to be enabled)
python -m assetopsbench.run --scenario "List all sensors of Chiller 6 in MAIN site"
```

Or jump in instantly:
- 🚀 **[Run on Colab](https://colab.research.google.com/github/IBM/AssetOpsBench/blob/main-0.x/notebook/LLM_Agent.ipynb)** — no install required (illustration of LLM Agent)
- 🎮 **[Try the HF Playground](https://huggingface.co/spaces/ibm-research/AssetOps-Bench)** — interactive demo
- 📖 **[Read INSTRUCTIONS.md](./INSTRUCTIONS.md)** — full setup, MCP servers, plan-execute runner

> [!NOTE]
> Active development is on `main`. The codebase used for various publication venues continues to be maintained on separate branches, for example, ACL 2026 [`IndustryAssetEQA`](https://IBM/AssetOpsBench/tree/IndustryAssetEQA) and prior experimental work is maintained on [`main-0.x`](https://IBM/AssetOpsBench/tree/main-0.x).

---

## What is AssetOpsBench?

AssetOpsBench is a **unified framework for developing, orchestrating, and evaluating domain-specific AI agents** in industrial asset operations and maintenance. It provides reproducible scenarios, agent tooling, and evaluation pipelines for multi-step workflows in simulated industrial environments.

### Domain-Specific MCP Servers

| MCP Servers | Important tools |
|---|---|
| **IoT** | `sites`, `asset_ids`, `asset_detail`, `assets`, `find_assets_by_sensors`, `installed_sensors`, `measured_sensors` |
| **FMSR** | `get_failure_modes`, `generate_failure_modes`, `add_failure_modes` |
| **TSFM** | Tasks/evidence: `list_tasks`, `profile_series`, `characterize_series`, `data_quality`; model catalog: `list_models`, `search_models`, `find_models`, `resolve_model`, `model_template`, `register_model`, `register_finetuned`, `hf_stats`; feature catalog: `list_features`, `search_features`, `extract_features`, `select_features`; run/eval ledger: `recipe_template`, `run_recipe`, `run_tabular_recipe`, `run_plan`, `evaluate`, `list_runs`, `list_results` |
| **WO** | `get_work_order_distribution`, `predict_next_work_order`, ... |
| **Vibration** | `compute_fft_spectrum`, `compute_envelope_spectrum`, ... |
| **...** | **...** |

The full TSFM MCP surface currently contains 41 tools covering model cards, feature cards, recipe execution, evaluation, and result/run lookup. See [docs/mcp-servers.md](./docs/mcp-servers.md#tsfm--time-series-model-and-feature-catalogs) for the complete reference.

### Agent Frameworks

- **[Plan Execute](./src/agent/plan_execute)** — plan-and-execute sequential workflow to work with any LLM
- **[Deep Agent](./src/agent/deep_agent)** — planning, sub-agents, and virtual filesystem for long-horizon tasks
- **[Claude Agent](./src/agent/claude_agent)** — ReAct-based orchestrator using Claude with agent-as-tool delegation
- **[OpenAI Agent](./src/agent/openai_agent)** — ReAct-based orchestrator using OpenAI models with agent-as-tool delegation


### MCP Environment

The `src/` directory contains MCP servers and a plan-execute runner built on the [Model Context Protocol](https://modelcontextprotocol.io/). See **[INSTRUCTIONS.md](./INSTRUCTIONS.md)** for setup.


---

## Example Scenarios

| Domain | Example Task |
|---|---|
| **IoT** | "List all assets in MAIN site" |
| **FMSR** | "List known failure modes for asset class pump" |
| **TSFM** | "Find a forecasting model for Chiller 6 and check it can be loaded" |
| **WO** | "Generate a work order for Chiller 6 anomaly detection" |

Some tasks focus on a single domain, others are multi-step end-to-end workflows. Explore all scenarios on [Hugging Face](https://huggingface.co/datasets/ibm-research/AssetOpsBench).

---

## Leaderboards

- To be revised (WIP with latest models)
- Evaluated with **7 Large Language Models**
- Trajectories scored using **LLM Judge (Llama-4-Maverick-17B)**
- **6-dimensional criteria** measuring reasoning, execution, and data handling

Example: MetaAgent leaderboard

![meta_agent_leaderboard](https://user-attachments/assets/615059be-e296-40d3-90ec-97ee6cb00412)

---

## Publications

**12+ contributions across 7 top venues** in 2025–2026 from the team behind AssetOpsBench.

<details>
<summary><b>⭐ KDD 2026 — Jeju, South Korea</b> (click to expand)</summary>

- **[D&B]** **AssetOpsBench: A Benchmark for Industrial Asset Operations Agents** · *D. Patel, S. Lin, et al.* · [📄 Paper](https://arxiv.org/pdf/2506.03828)
- **[Tutorial]** **Building Reliable Industrial Agents with MCP: A Hands-on AssetOpsBench Tutorial for AI-Driven Operations** · *D. Patel, C. Shyalika, et al.*

</details>

<details>
<summary><b>ACL 2026 - San Diego, USA</b></summary>

- **[Industry]** **IndustryAssetEQA: A Neurosymbolic Operational Intelligence System for Embodied Question Answering in Industrial Asset Maintenance** · *C. Shyalika, D. Patel, A. Sheth* · [arXiv:2604.23446](https://arxiv.org/abs/2604.23446)

</details>

<details>
<summary><b>ICLR 2026 - Brazil</b></summary>

- **[Main]** **Adaptive Conformal Anomaly Detection with Time Series Foundation Models for Signal Monitoring** · *N. Martinez, F. O'Donncha, W. M. Gifford, N. Zhou, D. C. Patel, R. Vaculin*

</details>

<details>
<summary><b>AAAI 2026 — Singapore</b></summary>

- **[Demo]** **AssetOpsBench-Live: Privacy-Aware Online Evaluation of Multi-Agent Performance in Industrial Operations** · *D. Patel, N. Zhou, S. Lin, J. T. Rayfield, C. Shyalika, S. R. Yarrabothula* · [🎥 Demo](https://www.youtube.com/watch?v=JcKlS5v5fGY)
- **[Main]** **SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search** · *Y. Zhang, G. Ganapavarapu, S. Jayaraman, B. Agrawal, D. Patel, A. Fokoue* · [💻 Code](https://IBM/SPIRAL)
- **[Bridge]** **Knowledge-Guided AI for Industrial Asset Health Monitoring** · *S. Lin, D. Patel*
- **[Tutorial]** **From Inception to Productization: Hands-on Lab for the Lifecycle of Multimodal Agentic AI in Industry 4.0** · *C. Shyalika, S. Ahuja, S. Lin, R. Wickramarachchi, D. Patel, A. Sheth* · [🌐 Website](https://ibm.github.io/AssetOpsBench/aaaiwebsite/) · [📊 Slides](https://drive.google.com/file/d/16GaYxBQ2FsVqKpkKOU0PI_ZCTCsowenF/view?usp=sharing)
- **[Workshop(AABA4ET)]** **Agentic Code Generation for Heuristic Rules in Equipment Monitoring** · *F. Lorenzi, A. Langbridge, F. O'Donncha, J. Rayfield, B. Eck, S. Rosato*

</details>

<details>
<summary><b>IAAI 2026 - Singapore</b></summary>

- **[Deployed]** **Deployed AI Agents for Industrial Asset Management: CodeReAct Framework for Event Analysis and Work Order Automation** · *N. Zhou, D. Patel, A. Bhattacharyya*
- **[Emmerging]** **Diversity Meets Relevancy: Multi-Agent Knowledge Probing for Industry 4.0 Applications** · *C. Constantinides, D. Patel, S. Kimbleton, N. Garg, M. Paracha*

</details>

<details>
<summary><b>NeurIPS 2025 — San Diego, USA</b></summary>

- **[D&B Track]** **FailureSensorIQ: A Multi-Choice QA Dataset for Understanding Sensor Relationships and Failure Modes** · *C. Constantinides, D. Patel, S. Lin, C. Guerrero, S. D. Patil, J. Kalagnanam* · [📄 arXiv](https://arxiv.org/abs/2506.03278) · [💻 Code](https://IBM/FailureSensorIQ)
- **[Social]** **Building Reliable Agentic Benchmarks: Insights from AssetOpsBench** *(invited talk, 2000+ registered)* · *D. Patel* · [📅 Luma](https://luma.com/mkyyvypm?tk=AkGVp5)

</details>

<details>
<summary><b>EMNLP 2025 — Suzhou, China</b></summary>

- **[Main]** **ReAct Meets Industrial IoT: Language Agents for Data Access** · *J. T. Rayfield, S. Lin, N. Zhou, D. C. Patel*
- **[Main]** **Generalized Embedding Models for Industry 4.0 Applications** · *C. Constantinides, S. Lin, D. C. Patel* · [📄 arXiv](https://arxiv.org/abs/2506.12607)
- **[Findings]** **Fine-Tuned Thoughts: Leveraging Chain-of-Thought Reasoning for Industrial Asset Health Monitoring** · *S. Lin, D. Patel, C. Constantinides* · [📄 ACL Anthology](https://aclanthology.org/2025.findings-emnlp.1126/) · [💻 Code](https://IBM/FailureSensorIQ)

</details>

---

## Tutorials & Technical Material

📘 Hands-on guides from our team:

- [**ReActXen IoT Agent**](https://IBM/ReActXen/blob/main/docs/tutorial/ReActXen_IoT_Agent_EMNLP_2025.pdf) (EMNLP 2025)
- [**FailureSensorIQ**](https://IBM/FailureSensorIQ) (NeurIPS 2025)
- [**AssetOpsBench Lab**](https://ibm.github.io/AssetOpsBench/aaaiwebsite/) (AAAI 2026)
- [**SPIRAL**](https://IBM/SPIRAL) (AAAI 2026)
- [**AssetOpsBench Technical Material**](https://IBM/AssetOpsBench/blob/main/docs/tutorial/AssetOpsBench_Technical_Material.pdf)

---

## AI Competitions

AssetOpsBench powers public AI agent competitions that bring together researchers, students, and practitioners worldwide.

### 🔴 Live — IJCAI 2026

**Industrial Automation Challenge: Benchmarking Physics-Grounded LLMs for Task Reasoning**

A new challenge co-located with **IJCAI 2026** that pushes LLM agents on physics-grounded industrial reasoning.

- 🌐 **Challenge site:** [ai-industrial-challenge-ijcai](https://sites.google.com/view/ai-industrial-challenge-ijcai/home)
- 📋 **IJCAI 2026 competitions:** [2026.ijcai.org/competitions](https://2026.ijcai.org/competitions/)

### ✅ Completed — CODS 2025

**AssetOpsBench-Live: AI Agentic Challenge**

Launched in September 2025 at CODS 2025, the competition evaluated multi-agent systems on live industrial scenarios.

- 🏆 **Competition page:** [codabench.org/competitions/10206](https://www.codabench.org/competitions/10206/)
- 👥 **365 participants** · **500+ agent submissions**

---

## Talks & Events

| Date | Event |
|---|---|
| 2026-08 | **KDD 2026** — AssetOpsBench paper + MCP tutorial · *Jeju, South Korea* |
| 2026-05-10 | [NUS Seminar: AssetOpsBench Applications](https://events.comp.nus.edu.sg/view/25423) |
| 2025-12 | NeurIPS 2025 Social: *Building Reliable Agentic Benchmarks* (2000+ registered) |
| 2025-10-03 | 2-Hour Workshop: *AI Agents and Their Role in Industry 4.0 Applications* · NJIT ACM |
| 2025-09-01 | [CODS 2025 Competition Launch — AssetOpsBench-Live](https://www.codabench.org/competitions/10206/) |
| 2025-06-01 | AssetOpsBench v1.0 released — 141 industrial scenarios |

---

## University Projects & Extensions

AssetOpsBench is being extended by university research groups exploring new asset classes, evaluation paradigms, and agentic architectures. **To list your project, open a PR.**

- **Calibrated Coordination Reduces Overconfident Errors in Multi-Agent LLM Systems** – Confidence-weighted aggregation and abstention framework for reducing hallucinated confidence events in multi-agent industrial troubleshooting and operational decision-making benchmarks. Chand Sahil Mansuri, Sadamori Kojaku, Binghamton University.
- **Internalizing MCP Tool Knowledge in Small LLMs via QLoRA Fine-Tuning** — HPML project using AssetOpsBench to fine-tune ~4B models to internalize MCP tool knowledge and reduce prompt schema overhead. [Ayal Yakobe](https://yakobeayal), Columbia University · [repo](https://YuvalShemla/hpml-2026-project)
- **SPIN — Structural LLM Planning via Iterative Navigation for Industrial Tasks.** [Yusuke Ozaki](https://ozatamago), University at Albany · [paper](https://arxiv.org/abs/2605.14051) · [repo](https://ozatamago/AssetOpsBench/tree/UACap10)
- **Synthetic Scenario Generation for Evaluation of Industry 4.0 Agents** — Automated scenario generation, transformer asset integration, and scenario quality evaluation. [Rohith Kanathur](https://Rohith-Kanathur), [Sagar Chethan Kumar](https://Sagar-CK), Columbia University · [repo](https://Rohith-Kanathur/AssetOpsBench) · [paper](https://arxiv.org/abs/2607.22563)
- **AgentOpsBench** — High-throughput battery analytics MCP server with DNN prognostics (RUL prediction) and 3.3× latency optimization. [Siddharth Gowda, Rushin Bhatt, Aryaman Agrawal, Winston Li](https://siddharthgowda), Columbia University · [repo](https://siddharthgowda/AssetOpsBench)
- **Skill-Knowledge-Augmented Agents on AssetOpsBench** — Confidence-gated skill execution with scoped knowledge plugins for industrial fault diagnosis. [Vera Mazeeva](https://verammaz), [Sanskruti Shejwal](https://Sans-Shej), [Shrey Arora](https://shreyarora2198), [Mana Abbaszadeh](https://Manazd), Columbia University · [repo](https://shreyarora2198/AssetOpsBench/tree/team14-final)
- **Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines.** [Krish Veera](https://www.github.com/krishrveera/), [Alimurtaza Mustafa Merchant](https://alimurtaza0411/), [Sajal Kumar Goyla](https://SajalGoyla/), [Shambhawi Bhure](https://ShambhawiBhure/), Columbia University · [paper](https://arxiv.org/abs/2605.20630) · [repo](https://alimurtaza0411/Latency-Optimized-AssetOpsBench/tree/feature/ablation-study)
- **Towards Multi-Turn Dialog Systems for Industrial Asset Operations and Maintenance** - Improved response quality and reduced redundant tool calls and multi-turn latency. [Chengrui Li](https://Coderlicr), [Rujing Li](https://rujing-li), [Yitong Bai](https://BrianBai093), [Rui Li](https://Rui2026), Columbia University ·[paper](https://arxiv.org/abs/2605.24953)· [repo](https://Coderlicr/Multi-Turn-AssetOps)
- **Skills and Knowledge Plugin MCP Servers for Optimized Industrial O&M Agents** - reducing planning overhead and improving retrieval grounding in industrial asset maintenance agents through an MCP Skills Server that exposes reusable multi-step operational workflows and a Knowledge Plugin Server that enables injection of context-specific documentation. [Andrew Li](https://andli28), [Kirthana Natarajan](https://kmn01), [Thai On](https://tq-o), [Trisha Maturi](https://trishamaturi), [Yeshitha Bhuvanesh](https://Yeshitha-co), Columbia University · [repo](https://kmn01/AssetOpsBench/)
- **Profiling and Optimizing the TSFM MCP Server** - Developed a reproducible benchmarking harness, stage-level profiling system, and interchangeable model interface that identified preprocessing and inference bottlenecks, achieving up to 12.8× faster forecasting and 12.2% lower fine-tuning latency while supporting forecasting, fine-tuning, and anomaly detection workflows. [Tomas Pasiecznik](https://tomaspasie), [Sam Colman](https://samccolman), [Byeolah Kwon](https://Byeolah-Kwon), [Sally Go](https://yugo9081), Columbia University · [repo](https://Lion-Latency/AssetOpsBench)
- **Profiling and Optimizing the AssetOpsBench Plan-Execute Pipeline** - Provides the first systematic performance characterization of the AssetOpsBench plan-execute pipeline to quantify the latency-accuracy tradeoff of thinking mode on Gemma 4 26B for industrial asset operations tasks. Implemented and evaluated scenario-based routing optimizations to balance the tradeoff. [Shen Li](https://jasonlee-1024), [Charles Xu](https://Char15Xu), [Ann Li](https://anncli), [Caroline Cahill](https://caroline-cahill), Columbia University · [repo](https://jasonlee-1024/AssetOpsBench)
- **Performance Optimzation of the TSFM Agent in an Industrial Agentic Benchmark** - Developed an optimization framework for IBM's TinyTimeMixer(TTM) model by implementing model pre-loading, torch.compile graph fusion, and replacing Huggingface abstractions with direct batched model calls. We achieved 3.3X reduction in workflow latency and 68% decrease in total execution time while maintaining zero-shot forecast quality on industrial sensor data. [Alisha Vinod](https://alishavinod), [Jonathan Ang](https://mao1e), [Sanjaii Vijayakumar](https://sanjaiiv04), [Thomas Ajai](https://thomasajai), Columbia University . [repo](https://alishavinod/AssetOpsBench)
- **Visual Inspection Agent for AssetOpsBench** - Adds a vision modality to AssetOpsBench via an MCP-connected Visual Inspection Agent and 22 hand-authored visual inspection scenarios across pumps, induction motors, power transformers, and wind turbine blades. Benchmarks AWQ W4A16 quantization and vLLM serving optimizations on Qwen2.5-VL-7B and Llama-3-LLaVA-NeXT-8B, with an LLM-as-a-judge scoring pipeline for accuracy evaluation. [Amaan Sheikh](https://amaan784), [Aman Upganlawar](https://amanupg), [Madhav Rajkondawar](https://madhavrajk), [Yang-Jung (Eric) Chen](https://ericyangchen), Columbia University · [repo](https://amaan784/hpml-final-project)
- **Agentic AI Workflows for Naval Operations and Maintenance** — Exploring AssetOpsBench for evaluating agentic AI workflows, with future extensions using digital-twin-generated synthetic data. [Priyam Dalmia](https://priyamDalmia), [Chin-Teng Lin](https://profiles.uts.edu.au/Chin-Teng.Lin), [Fred Chang](https://profiles.uts.edu.au/Fred.Chang), University of Technology Sydney
 - **Knowledge Graphs as the Missing Data Layer for LLM-Based Industrial Asset Operations** — Treats a typed knowledge graph as the *data layer* for AssetOpsBench agents: holding the model and orchestration fixed, the same GPT-4 rises from 65% to 82–83% with LLM-generated Cypher and to 99% with deterministic graph handlers on the 139-scenario snapshot, plus Generation-Augmented Knowledge (GAK) — provenance-tagged enrichment — for the non-deterministic FMSR scenarios. Accepted at Agents+Graph @ VLDB 2026. Madhulatha Mandarapu, Sandeep Kunkunuru (VaidhyaMegha / Samyama) · [paper](https://arxiv.org/abs/2605.26874) · [repo](https://samyama-ai/assetops-kg)
---

## Call for Scenario Contribution

We are expanding **AssetOpsBench** to cover a broader range of industrial challenges. We invite researchers and practitioners to contribute new scenarios, particularly in:

- **Asset Classes:** Turbines, HVAC systems, Pumps, Transformers, CNC Machines, Robotics, Engines
- **Task Domains:** Prognostics and Health Management, Remaining Useful Life (RUL) estimation, Root Cause Analysis (RCA), Diagnostic Analysis, Predictive Maintenance

**How to contribute:**

1. **Define** your scenario following our [Utterance Guideline](docs/guideline/utterance_design_guideline.md) and [Ground Truth Guideline](docs/guideline/ground_truth_design_guideline.md)
2. **Explore** the [Hugging Face dataset](https://huggingface.co/datasets/ibm-research/AssetOpsBench) for examples
   - For external public sources and starter asset-class mappings, see [External Industrial Dataset Guide](docs/external-industrial-datasets.md)
3. **Submit** a Pull Request or open an [Issue](https://IBM/AssetOpsBench/issues) with the tag `new-scenario`
4. **Contact us** with questions:
   - Dhaval Patel — [pateldha@us.ibm.com](mailto:pateldha@us.ibm.com)
   - Nianjun Zhou — [jzhou@us.ibm.com](mailto:jzhou@us.ibm.com)

---

## Infrastructure Support

Model API access for AssetOpsBench 2.0 is enabled by [TokenRouter](https://tokenrouter.com) (PaleBlueDot AI), a unified API platform providing access to leading AI models through a single API endpoint.

---

## Contributors

Thanks to these wonderful people ✨

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://ShuxinLin">
          <img src="https://ShuxinLin.png?s=50" width="30px;" alt="ShuxinLin"/><br />
          <sub><b>ShuxinLin</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=ShuxinLin" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://DhavalRepo18">
          <img src="https://DhavalRepo18.png?s=50" width="30px;" alt="DhavalRepo18"/><br />
          <sub><b>DhavalRepo18</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=DhavalRepo18" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://ChathurangiShyalika">
          <img src="https://ChathurangiShyalika.png?s=50" width="30px;" alt="ChathurangiShyalika"/><br />
          <sub><b>ChathurangiShyalika</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=ChathurangiShyalika" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://nianjunz">
          <img src="https://nianjunz.png?s=50" width="30px;" alt="nianjunz"/><br />
          <sub><b>nianjunz</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=nianjunz" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://PUSHPAK-JAISWAL">
          <img src="https://PUSHPAK-JAISWAL.png?s=50" width="30px;" alt="PUSHPAK-JAISWAL"/><br />
          <sub><b>PUSHPAK-JAISWAL</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=PUSHPAK-JAISWAL" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://LGDiMaggio">
          <img src="https://LGDiMaggio.png?s=50" width="30px;" alt="LGDiMaggio"/><br />
          <sub><b>LGDiMaggio</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=LGDiMaggio" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://DeveloperMindset123">
          <img src="https://DeveloperMindset123.png?s=50" width="30px;" alt="Ayan Das"/><br />
          <sub><b>Ayan Das</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=DeveloperMindset123" title="Code">💻</a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://jdsheehan">
          <img src="https://jdsheehan.png?s=50" width="30px;" alt="jdsheehan"/><br />
          <sub><b>jdsheehan</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=jdsheehan" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://bradleyjeck">
          <img src="https://bradleyjeck.png?s=50" width="30px;" alt="bradleyjeck"/><br />
          <sub><b>bradleyjeck</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=bradleyjeck" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://jtrayfield">
          <img src="https://jtrayfield.png?s=50" width="30px;" alt="jtrayfield"/><br />
          <sub><b>jtrayfield</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=jtrayfield" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://florenzi002">
          <img src="https://florenzi002.png?s=50" width="30px;" alt="florenzi002"/><br />
          <sub><b>florenzi002</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=florenzi002" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://flamehaven01">
          <img src="https://flamehaven01.png?s=50" width="30px;" alt="flamehaven01"/><br />
          <sub><b>flamehaven01</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=flamehaven01" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://kushwaha001">
          <img src="https://kushwaha001.png?s=50" width="30px;" alt="kushwaha001"/><br />
          <sub><b>kushwaha001</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=kushwaha001" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://Rohith-Kanathur">
          <img src="https://Rohith-Kanathur.png?s=50" width="30px;" alt="Rohith-Kanathur"/><br />
          <sub><b>Rohith-Kanathur</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=Rohith-Kanathur" title="Code">💻</a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://Mohit-15">
          <img src="https://Mohit-15.png?s=50" width="30px;" alt="Mohit Gupta"/><br />
          <sub><b>Mohit Gupta</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=Mohit-15" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://jellyfishing2346">
          <img src="https://jellyfishing2346.png?s=50" width="30px;" alt="jellyfishing2346"/><br />
          <sub><b>jellyfishing2346</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=jellyfishing2346" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://anncli">
          <img src="https://anncli.png?s=50" width="30px;" alt="anncli"/><br />
          <sub><b>anncli</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=anncli" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://ozatamago">
          <img src="https://ozatamago.png?s=50" width="30px;" alt="ozatamago"/><br />
          <sub><b>ozatamago</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=ozatamago" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://tomaspasie">
          <img src="https://tomaspasie.png?s=50" width="30px;" alt="tomaspasie"/><br />
          <sub><b>tomaspasie</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=tomaspasie" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://Sans-Shej">
          <img src="https://Sans-Shej.png?s=50" width="30px;" alt="Sans-Shej"/><br />
          <sub><b>Sans-Shej</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=Sans-Shej" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://sanjaiiv04">
          <img src="https://sanjaiiv04.png?s=50" width="30px;" alt="sanjaiiv04"/><br />
          <sub><b>sanjaiiv04</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=sanjaiiv04" title="Code">💻</a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://SajalGoyla">
          <img src="https://SajalGoyla.png?s=50" width="30px;" alt="SajalGoyla"/><br />
          <sub><b>SajalGoyla</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=SajalGoyla" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://priyamDalmia">
          <img src="https://priyamDalmia.png?s=50" width="30px;" alt="priyamDalmia"/><br />
          <sub><b>priyamDalmia</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=priyamDalmia" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://krishrveera">
          <img src="https://krishrveera.png?s=50" width="30px;" alt="krishrveera"/><br />
          <sub><b>krishrveera</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=krishrveera" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://kmn01">
          <img src="https://kmn01.png?s=50" width="30px;" alt="kmn01"/><br />
          <sub><b>kmn01</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=kmn01" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://Coderlicr">
          <img src="https://Coderlicr.png?s=50" width="30px;" alt="Coderlicr"/><br />
          <sub><b>Coderlicr</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=Coderlicr" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://BrianBai093">
          <img src="https://BrianBai093.png?s=50" width="30px;" alt="BrianBai093"/><br />
          <sub><b>BrianBai093</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=BrianBai093" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://AyalYakobe">
          <img src="https://AyalYakobe.png?s=50" width="30px;" alt="AyalYakobe"/><br />
          <sub><b>AyalYakobe</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=AyalYakobe" title="Code">💻</a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://amaan784">
          <img src="https://amaan784.png?s=50" width="30px;" alt="amaan784"/><br />
          <sub><b>amaan784</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=amaan784" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://Dev-Scodes5">
          <img src="https://Dev-Scodes5.png?s=50" width="30px;" alt="Dev-Scodes5"/><br />
          <sub><b>Dev-Scodes5</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=Dev-Scodes5" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://jack-pfeifer">
          <img src="https://jack-pfeifer.png?s=50" width="30px;" alt="jack-pfeifer"/><br />
          <sub><b>jack-pfeifer</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=jack-pfeifer" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://sandeepkunkunuru">
          <img src="https://sandeepkunkunuru.png?s=50" width="30px;" alt="sandeepkunkunuru"/><br />
          <sub><b>sandeepkunkunuru</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=sandeepkunkunuru" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://srutanik">
          <img src="https://srutanik.png?s=50" width="30px;" alt="srutanik"/><br />
          <sub><b>srutanik</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=srutanik" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://thedgarg31">
          <img src="https://thedgarg31.png?s=50" width="30px;" alt="thedgarg31"/><br />
          <sub><b>thedgarg31</b></sub>
        </a><br />
        <a href="https://IBM/AssetOpsBench/commits?author=thedgarg31" title="Code">💻</a>
      </td>
      <td></td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=IBM/AssetOpsBench&type=Date)](https://star-history.com/#IBM/AssetOpsBench&Date)

---

<div align="center">

**If AssetOpsBench is useful to your work, please ⭐ star the repo, 🍴 fork it, and tell us what you're building.**

</div>
