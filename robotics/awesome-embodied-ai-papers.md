<div align="center">

# 🤖 Awesome Embodied AI Papers

**A curated top-conference-oriented map of embodied AI research across VLN, VLA, WAM, planning, embodiment, and deployment.**

English | [Chinese](README.zh-CN.md)

[![Awesome](https://img.shields.io/badge/Awesome-Embodied%20AI-fc60a8?style=for-the-badge)](https://awesome.re)
[![Survey Entries](https://img.shields.io/badge/Survey%20Entries-707-0984e3?style=for-the-badge)](README.md)
[![Last Commit](https://img.shields.io/github/last-commit/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=00b894)](https://neardws/awesome-embodied-ai-papers/commits)
[![Stars](https://img.shields.io/github/stars/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=fdcb6e&logo=github)](https://neardws/awesome-embodied-ai-papers/stargazers)
[![Forks](https://img.shields.io/github/forks/neardws/awesome-embodied-ai-papers?style=for-the-badge&color=e17055&logo=github)](https://neardws/awesome-embodied-ai-papers/network/members)

Updated: 2026-07-10

</div>

## 📋 Table of Contents

| | Section | Description |
|:---:|:---|:---|
| 🏷️ | [Tag Legend](#tag-legend) | Tags used to group embodied AI directions |
| 🧭 | [Overall View](#overall-view) | High-level system route and field framing |
| 🗺️ | [Direction Overview](#direction-overview) | Six-track overview with paper counts |
| 🔎 | [Reading Order](#reading-order) | Suggested priority list for deeper reading |
| 🧾 | [Data Sources](#data-sources) | Source traceability and reference metadata |
| 🦿 | [Humanoid & Biped Hardware Reference](#humanoid--biped-hardware-reference) | Biped platforms and dexterous-hand configurations; papers are consolidated into the humanoid master table |
| 📚 | [Detailed Tables](#detailed-tables) | Paper-level tables by direction and subdirection |

> [!NOTE]
> Entries are scoped to reviewed public sources, including CCF-A venues and robotics flagship conferences such as ICRA/IROS.

> [!TIP]
> Missing papers or resources can be suggested through Issues or Pull Requests.

## Tag Legend

| Tag | Meaning |
| --- | --- |
| `VLN` | Large-scale navigation |
| `VLA` | Vision-language-action manipulation policies |
| `WAM` | World action models |
| `Planning` | Task decomposition, memory, failure recovery, and constrained planning |
| `Embodiment` | Humanoids, bimanual systems, dexterous hands, and tactile interaction |
| `Deployment` | Efficiency, evaluation, data, sim2real, and safety |

## Overall View

The current embodied AI frontier can be grouped into six tracks: large-scale VLN, VLA manipulation policies, WAM/world models, agentic planning, embodiment expansion, and deployment-oriented efficiency/evaluation/data.

The system direction worth tracking is:

```text
task understanding and fine-grained planning agent
        -> WAM / world model for imagination, verification, and failure prediction
        -> small VLA, diffusion policy, skill library, or classical controller
        -> local robot safety loop
```

The reason is straightforward: monolithic VLA models matter, but real robots also need interpretable planning, executable constraints, low-latency control, failure recovery, and on-device autonomy.

### Taxonomy & Evidence Map

<p align="center">
  <img src="figs/embodied-ai-taxonomy-v3.svg" alt="Taxonomy and evidence map for 707 embodied AI papers across six directions and 29 subdirections." width="100%">
</p>

### Evolution & Method Lineage

<p align="center">
  <img src="figs/embodied-ai-lineage-v3.svg" alt="Evolution and method lineage for embodied AI methods from 2022 to 2026." width="100%">
</p>

### System Roadmap & Trend Matrix

<p align="center">
  <img src="figs/embodied-ai-system-roadmap-v3.svg" alt="System roadmap and trend matrix for embodied AI capability layers, method anchors, interface signals, and trend pressure." width="100%">
</p>

### Research Direction: Verifiable Closed-Loop Action

The next research thread worth highlighting is not a single module, but a closed loop: spatial memory supports planning, planning grounds executable action, world models verify consequences, and failure feedback updates the next plan.

<p align="center">
  <img src="figs/embodied-ai-closed-loop-action-v3.svg" alt="Research direction figure for embodied AI as verifiable closed-loop action across spatial memory, planning, action, world prediction, and failure feedback." width="100%">
</p>

| Direction | Trend |
| --- | --- |
| VLN | VLN is moving from discrete graph navigation toward continuous, memory-backed, physically executable, open-world navigation, while on-device variants are still early. |
| VLA | VLA growth is led by generalist policies and diffusion/flow action generation, with action representation, 3D grounding, online tuning, and safety becoming the practical bottlenecks. |
| WAM | WAM is emerging as an imagination and verification layer between planning and controllers, with cascaded and video/latent models ahead of fully joint world-action modeling. |
| Planning | Agentic planning is moving from instruction decomposition toward memory, failure monitoring, executable constraints, and self-improving loops. |
| Embodiment | Embodiment expansion tests whether policies survive new bodies, contacts, and coordination demands, with humanoid and dexterous-hand work leading the volume. |
| Deployment | Deployment work is led by benchmark/data credibility, efficiency, and sim2real transfer, with real-time execution and safety evaluation as smaller but necessary readiness checks. |

| Direction | Subdirection | Trend |
| --- | --- | --- |
| VLN | Continuous VLN | Continuous observations, multimodal goals, and online adaptation are replacing the clean discrete-graph assumption. |
| VLN | Map Memory | Semantic maps, topological memory, 3D memory, retrieval, and caching are becoming the navigation substrate. |
| VLN | Physically Executable Navigation | Navigation research is adding body constraints, dynamic scenes, and safety decoding so plans can be executed. |
| VLN | Urban / Open-world Navigation | The setting is expanding toward streets, crowds, implicit human needs, lifelong navigation, and open-world exploration. |
| VLN | Low-cost / On-device Navigation | The deployment track compresses navigation into smaller memories, cheaper data, and on-device inference. |
| VLA | generalist VLA | Generalist policies consolidate many tasks and datasets into reusable robot foundation policies. |
| VLA | action representation | Action tokens, waypoints, constraints, and motion primitives bridge language/image understanding with executable control. |
| VLA | diffusion/flow policy | Diffusion and flow models are becoming a major action-generation route for robust manipulation. |
| VLA | 3D grounding | Object-centric geometry, spatial localization, and affordance priors are moving VLA from pixels toward physical scenes. |
| VLA | online/RL fine-tuning | Post-pretraining adaptation uses RL, online feedback, and test-time optimization to close execution gaps. |
| VLA | Safety and Robustness | Robustness work is shifting from benchmark accuracy to attacks, uncertainty, unsafe actions, and physical failure modes. |
| WAM | cascaded WAM | Cascaded systems imagine or predict first, then act, making WAM easier to attach to existing planners and controllers. |
| WAM | joint WAM | Joint WAM is small but important because it tries to model vision, state, and action in one coupled system. |
| WAM | video/latent world model | Video and latent prediction are the main path for future-state imagination, reward shaping, and interactive simulation. |
| WAM | world model for VLA | World models are being used to improve VLA generalization, action selection, and failure recovery. |
| Planning | Task Decomposition | Planners translate high-level language into subgoals, programs, skills, or executable task graphs. |
| Planning | memory | Persistent scene, task, and personalization memory supports long-horizon interaction beyond a single episode. |
| Planning | failure monitor | Failure monitors make embodied agents detect, explain, and recover from execution errors instead of assuming success. |
| Planning | constraint / affordance planning | Constraints, affordances, PDDL-like structure, and code policies make high-level plans physically executable. |
| Planning | self-improving planning | Feedback, RL, reflection, and experience revision are turning planning into an iterative improvement loop. |
| Embodiment | humanoid | Humanoid work stresses whole-body control, mobile manipulation, sim2real transfer, and generalization across full-body skills. |
| Embodiment | bimanual | Bimanual research focuses on coordinated dual-arm manipulation and longer-horizon interaction. |
| Embodiment | dexterous hand | Dexterous-hand work expands grasping and manipulation into high-DOF action spaces and transfer-heavy settings. |
| Embodiment | tactile/contact-rich | Tactile and contact-rich research brings force, touch, and fine-grained feedback into manipulation policies. |
| Deployment | quantization/cache/tokenization | Efficiency work compresses models and action representations through quantization, caching, and tokenization. |
| Deployment | real-time execution | Real-time execution focuses on latency-aware control and edge deployment constraints. |
| Deployment | benchmark/dataset | Benchmarks and datasets define coverage, credibility, and whether progress is measurable across robots and tasks. |
| Deployment | sim2real | Sim2real work bridges generated/simulated assets, dynamics, and policies into physical robot execution. |
| Deployment | safety evaluation | Safety evaluation builds tests for physical risk, robustness, and alignment under embodied interaction. |

## Direction Overview

<table>
<thead>
<tr>
<th nowrap>Tag</th>
<th nowrap>Direction</th>
<th nowrap>Subdirection</th>
<th nowrap>Entries</th>
<th nowrap>Takeaway</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap><code>VLN</code></td>
<td nowrap>VLN / Large-scale Navigation</td>
<td nowrap>continuous VLN, map memory, physically executable navigation, urban/open-world navigation, low-cost/on-device navigation</td>
<td nowrap>92</td>
<td nowrap>VLN focuses on language goals, spatial maps, memory, exploration, and navigation decisions. The core problem is turning natural-language tasks into executable large-scale movement plans. Current survey entries show a shift from discrete navigation graphs toward continuous environments, physically executable navigation, open urban settings, and lower-cost on-device navigation.</td>
</tr>
<tr>
<td nowrap><code>VLA</code></td>
<td nowrap>VLA / Manipulation Policies</td>
<td nowrap>generalist VLA, action representation, diffusion/flow policy, 3D grounding, online/RL fine-tuning, safety/robustness</td>
<td nowrap>251</td>
<td nowrap>VLA is the main track for robotic arms and mobile manipulation, but it is not just an action head attached to a large model. Survey papers concentrate on action representation, diffusion/flow policies, 3D grounding, online/RL fine-tuning, and robustness.</td>
</tr>
<tr>
<td nowrap><code>WAM</code></td>
<td nowrap>WAM / World Models</td>
<td nowrap>cascaded WAM, joint WAM, video/latent world model, world model for VLA</td>
<td nowrap>70</td>
<td nowrap>WAM combines future world-state prediction with action generation and fits naturally between agent planning and low-level control. Its value is not replacing every controller, but providing an intermediate layer for imagination, verification, and recovery.</td>
</tr>
<tr>
<td nowrap><code>Planning</code></td>
<td nowrap>Agentic Planning / Reasoning and Planning</td>
<td nowrap>task decomposition, memory, failure monitor, constraint / affordance planning, self-improving planning</td>
<td nowrap>103</td>
<td nowrap>This direction emphasizes task decomposition, memory, failure monitoring, constraint/affordance planning, and self-improving planning. It is closest to the practical system route of agent planning plus smaller execution modules.</td>
</tr>
<tr>
<td nowrap><code>Embodiment</code></td>
<td nowrap>Embodiment Expansion / Dexterous Manipulation</td>
<td nowrap>humanoid, bimanual, dexterous hand, tactile/contact-rich</td>
<td nowrap>146</td>
<td nowrap>Embodiment expansion determines whether embodied AI can move beyond single-arm systems toward humanoids, bimanual robots, dexterous hands, and tactile/contact-rich tasks. These papers show how action spaces, sensing, and control objectives become more complex as the body changes.</td>
</tr>
<tr>
<td nowrap><code>Deployment</code></td>
<td nowrap>Efficiency / Evaluation / Data</td>
<td nowrap>quantization/cache/tokenization, real-time execution, benchmark/dataset, sim2real, safety evaluation</td>
<td nowrap>105</td>
<td nowrap>This direction determines whether systems can actually be deployed: on-device inference, caching/quantization/action tokenization, real-time execution, sim2real, benchmarks, and safety evaluation are all necessary conditions.</td>
</tr>
</tbody>
</table>

## Reading Order

1. Start with VLN and Agentic Planning to separate large-scale planning from fine-grained task planning.
2. Then read VLA and WAM to distinguish direct action generation from imagination/prediction before execution.
3. Finish with embodiment expansion, efficiency, and evaluation because they determine whether a route can be deployed on real robots.

## Data Sources

GitHub source repository metadata and README snapshots are recorded in [`sources/github/repos.json`](sources/github/repos.json); historical source IDs are kept there for traceability.

<table>
<thead>
<tr>
<th nowrap>Source</th>
<th nowrap>Use</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap><a href="https://ccf.atom.im/">CCF 2026 Recommended List</a></td>
<td nowrap>Verify the 2026 CCF-A artificial intelligence conference classification.</td>
</tr>
<tr>
<td nowrap><a href="https://Songwxuan/Embodied-AI-Paper-TopConf">Songwxuan/Embodied-AI-Paper-TopConf</a></td>
<td nowrap>Main source for CCF-A papers, classified by conference and direction; paper, code, and project-page links preferentially use resources already provided in that repository.</td>
</tr>
<tr>
<td nowrap><a href="https://openreview.net/group?id=ICLR.cc/2026/Conference">ICLR 2026 OpenReview</a></td>
<td nowrap>Verify ICLR 2026 public paper pages and PDF resources.</td>
</tr>
<tr>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/issue/view/703">AAAI-26 Intelligent Robotics proceedings</a></td>
<td nowrap>Verify and add AAAI 2026 robotics-track papers.</td>
</tr>
<tr>
<td nowrap><a href="https://ras.papercept.net/conferences/scripts/start.pl">IEEE RAS PaperCept programs</a></td>
<td nowrap>Verify ICRA 2026 and IROS 2025 official program entries; ICRA 2025 PaperCept returned access denied in this environment.</td>
</tr>
<tr>
<td nowrap><a href="https://arxiv.org/">arXiv and author project pages for ICRA/IROS papers</a></td>
<td nowrap>Cross-check ICRA 2025 and IROS 2026 papers when official proceedings or full paper lists are not yet publicly stable.</td>
</tr>
<tr>
<td nowrap><a href="https://jonyzhang2023/awesome-embodied-vla-va-vln">jonyzhang2023/awesome-embodied-vla-va-vln</a></td>
<td nowrap>Reference the organization of VLA, WAM, VLN, VA, and surveys.</td>
</tr>
<tr>
<td nowrap><a href="https://OpenMOSS/Awesome-WAM">OpenMOSS/Awesome-WAM</a></td>
<td nowrap>Reference WAM categories such as cascaded/joint, autoregressive/diffusion, and evaluation/training data.</td>
</tr>
<tr>
<td nowrap><a href="https://UCSB-AI/awesome-vision-language-navigation">UCSB-AI/awesome-vision-language-navigation</a></td>
<td nowrap>Reference VLN categories such as dataset, evaluation, representation, action strategy, planning, and asking for help.</td>
</tr>
<tr>
<td nowrap><a href="https://DelinQu/awesome-vision-language-action-model">DelinQu/awesome-vision-language-action-model</a></td>
<td nowrap>Reference the VLA milestone timeline.</td>
</tr>
<tr>
<td nowrap><a href="https://yueen-ma/Awesome-VLA">yueen-ma/Awesome-VLA</a></td>
<td nowrap>Reference VLA categories such as components, world models, reasoning, policy steering, and low-level/high-level planners.</td>
</tr>
<tr>
<td nowrap><a href="https://www.unitree.com/H2plus/">Unitree official humanoid and dexterous-hand pages</a></td>
<td nowrap>Verify current H1/H1-2, G1, R1, H2/H2 Plus and modular hand specifications; living product figures were checked on 2026-07-10.</td>
</tr>
<tr>
<td nowrap><a href="https://open.agibot.com/docs/en/aimdk/a3/v3_1/dev_guide/01-a3_overview">AgiBot official product and AimDK documentation</a></td>
<td nowrap>Verify the bipedal A2, A3, X1 and X2 families, distinguish wheeled variants, and trace OmniHand/end-effector configurations.</td>
</tr>
</tbody>
</table>

## Detailed Tables

### VLN / Large-scale Navigation

VLN focuses on language goals, spatial maps, memory, exploration, and navigation decisions. The core problem is turning natural-language tasks into executable large-scale movement plans. Current survey entries show a shift from discrete navigation graphs toward continuous environments, physically executable navigation, open urban settings, and lower-cost on-device navigation.

Subdirections: continuous VLN, map memory, physically executable navigation, urban/open-world navigation, and low-cost/on-device navigation.

Total: 92 papers.

<table>
<thead>
<tr>
<th nowrap>Subdirection</th>
<th nowrap>Entries</th>
<th nowrap>Focus</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>Continuous VLN</td>
<td nowrap>39</td>
<td nowrap>Focus: whether navigation moves from discrete graphs toward continuous observations and real-time decisions.</td>
</tr>
<tr>
<td nowrap>Map Memory</td>
<td nowrap>23</td>
<td nowrap>Focus: map representation, semantic memory, caching, and retrieval.</td>
</tr>
<tr>
<td nowrap>Physically Executable Navigation</td>
<td nowrap>7</td>
<td nowrap>Focus: real embodiment constraints, dynamic environments, and safety decoding.</td>
</tr>
<tr>
<td nowrap>Urban / Open-world Navigation</td>
<td nowrap>20</td>
<td nowrap>Focus: open worlds, cities, crowded environments, and long-horizon navigation.</td>
</tr>
<tr>
<td nowrap>Low-cost / On-device Navigation</td>
<td nowrap>3</td>
<td nowrap>Focus: on-device inference, low-cost memory, and data efficiency.</td>
</tr>
</tbody>
</table>

#### Continuous VLN

Total: 39 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Task Type</th>
<th nowrap>Environment</th>
<th nowrap>Map/Memory</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=LM-Nav%3A+Robotic+Navigation+with+Large+Pre-Trained+Models+of+Language%2C+Vision%2C+and+Action">LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action</a></td>
<td nowrap>LM-Nav composes pretrained language, vision, and action models for robotic navigation.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>embodied navigation</td>
<td nowrap>language/spatial context</td>
<td nowrap>CoRL navigation method</td>
<td nowrap>VLN / embodied navigation benchmarks</td>
<td nowrap>Add CoRL navigation coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=LM-Nav%3A+Robotic+Navigation+with+Large+Pre-Trained+Models+of+Language%2C+Vision%2C+and+Action">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2020</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Vision-and-Dialog+Navigation">Vision-and-Dialog Navigation</a></td>
<td nowrap>Vision-and-Dialog Navigation extends VLN with dialog interaction during navigation.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>embodied navigation</td>
<td nowrap>language/spatial context</td>
<td nowrap>CoRL navigation method</td>
<td nowrap>VLN / embodied navigation benchmarks</td>
<td nowrap>Add CoRL navigation coverage.</td>
<td nowrap><a href="https://scholar.google.com/scholar?q=Vision-and-Dialog+Navigation">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2509.10454">GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation</a></td>
<td nowrap>GC-VLN treats instructions as graph constraints for training-free VLN.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>embodied navigation</td>
<td nowrap>language/spatial context</td>
<td nowrap>CoRL navigation method</td>
<td nowrap>VLN / embodied navigation benchmarks</td>
<td nowrap>Add CoRL navigation coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.10454">paper</a></td>
<td nowrap><a href="https://bagh2178.github.io/GC-VLN/">project</a></td>
<td nowrap><a href="https://bagh2178/GC-VLN">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11350">Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild</a></td>
<td nowrap>Search-TTA adapts multimodal visual-search agents at test time in open environments.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>embodied navigation</td>
<td nowrap>language/spatial context</td>
<td nowrap>CoRL navigation method</td>
<td nowrap>VLN / embodied navigation benchmarks</td>
<td nowrap>Add CoRL navigation coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11350">paper</a></td>
<td nowrap><a href="https://search-tta.github.io/">project</a></td>
<td nowrap><a href="https://marmotlab/Search-TTA-VLN">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2023</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2023/html/Gao_Adaptive_Zone-Aware_Hierarchical_Planner_for_Vision-Language_Navigation_CVPR_2023_paper.html">Adaptive Zone-Aware Hierarchical Planner for Vision-Language Navigation</a></td>
<td nowrap>AZHP plans navigation by adapting hierarchy and local zones for language-conditioned visual navigation.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>continuous indoor navigation</td>
<td nowrap>zone-aware hierarchical memory</td>
<td nowrap>hierarchical planning</td>
<td nowrap>VLN benchmarks</td>
<td nowrap>Use zone-level structure to make long-horizon VLN decisions more reliable.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Gao_Adaptive_Zone-Aware_Hierarchical_Planner_for_Vision-Language_Navigation_CVPR_2023_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2024</td>
<td nowrap><a href="https://proceedings.mlr.press/v235/gao24p.html">Fast-Slow Test-Time Adaptation for Online Vision-and-Language Navigation</a></td>
<td nowrap>Fast-Slow TTA adapts VLN agents online using complementary fast and slow adaptation signals.</td>
<td nowrap>Online VLN</td>
<td nowrap>continuous navigation</td>
<td nowrap>episodic adaptation memory</td>
<td nowrap>test-time adaptation</td>
<td nowrap>VLN benchmarks</td>
<td nowrap>Improve online VLN robustness under distribution shift.</td>
<td nowrap><a href="https://proceedings.mlr.press/v235/gao24p/gao24p.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICRA 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2509.19480">OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation</a></td>
<td nowrap>OmniVLA unifies language, goal images, and 2D pose goals, learning robot navigation policies through a VLA formulation.</td>
<td nowrap>Vision-language-action navigation</td>
<td nowrap>continuous navigation</td>
<td nowrap>multimodal goal context</td>
<td nowrap>navigation VLA training</td>
<td nowrap>Sim + Real</td>
<td nowrap>Train a generalizable navigation VLA with multimodal goal specifications.</td>
<td nowrap><a href="https://arxiv.org/abs/2509.19480">paper</a></td>
<td nowrap><a href="https://omnivla-nav.github.io/">project</a></td>
<td nowrap><a href="https://NHirose/OmniVLA">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICRA 2025</td>
<td nowrap><a href="https://sites.google.com/view/opennav/home">Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs</a></td>
<td nowrap>Open-Nav uses open-source LLMs for spatio-temporal chain-of-thought reasoning, progress estimation, and action decisions for zero-shot VLN in continuous environments.</td>
<td nowrap>Continuous VLN</td>
<td nowrap>continuous indoor environment</td>
<td nowrap>spatio-temporal CoT</td>
<td nowrap>zero-shot LLM planning</td>
<td nowrap>VLN-CE benchmark</td>
<td nowrap>Enable open-source LLMs to navigate continuous environments from language instructions.</td>
<td nowrap><a href="https://sites.google.com/view/opennav/home">paper</a></td>
<td nowrap><a href="https://sites.google.com/view/opennav/home">project</a></td>
<td nowrap><a href="https://YanyuanQiao/Open-Nav">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=kkBOIsrCXh">Embodied Navigation Foundation Model</a></td>
<td nowrap>NavFoM trains a unified navigation foundation model on 8 million cross-embodiment navigation samples, covering VLN, goal search, tracking, and autonomous driving.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>multimodal history/trajectory context</td>
<td nowrap>large-scale supervised pretraining</td>
<td nowrap>cross-embodiment benchmark</td>
<td nowrap>Cross-embodiment and cross-task generalization</td>
<td nowrap><a href="https://openreview.net/forum?id=kkBOIsrCXh">paper</a></td>
<td nowrap><a href="https://pku-epic.github.io/NavFoM-Web/">project</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://pku-epic.github.io/NavFoM-Web/">data</a></td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=GK4rznYwhn">Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-Language Navigation</a></td>
<td nowrap>DualVLN combines a slow vision-language global planner with a fast diffusion-based low-level controller to improve smooth execution for continuous real-world VLN.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>VLM waypoint planner + diffusion policy</td>
<td nowrap>sim+real robot</td>
<td nowrap>Addresses fragmented actions, high latency, and poor dynamic obstacle avoidance in end-to-end VLN.</td>
<td nowrap><a href="https://openreview.net/forum?id=GK4rznYwhn">paper</a></td>
<td nowrap><a href="https://internrobotics.github.io/internvla-n1-dualvln.github.io/">project</a></td>
<td nowrap><a href="https://InternRobotics/InternNav">code</a></td>
<td nowrap>InternData-N1</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=eqcDckWHik">CompassNav: Steering From Path Imitation to Decision Understanding In Navigation</a></td>
<td nowrap>CompassNav shifts from trajectory imitation to action-feasibility understanding, improving VLN decisions with Compass-Data-22k and gap-aware training.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>RFT + action feasibility supervision</td>
<td nowrap>Compass-Data-22k</td>
<td nowrap>From path imitation to decision understanding</td>
<td nowrap><a href="https://openreview.net/forum?id=eqcDckWHik">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=pFh5ygjN3V">M$^3$E: Continual Vision-and-Language Navigation via Mixture of Macro and Micro Experts</a></td>
<td nowrap>M3E separately models macro scene experts and micro perception experts, mitigating catastrophic forgetting in continual VLN cross-environment adaptation.</td>
<td nowrap>Continual VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>hierarchical MoE continual learning</td>
<td nowrap>-</td>
<td nowrap>Cross-environment continual learning and anti-forgetting</td>
<td nowrap><a href="https://openreview.net/forum?id=pFh5ygjN3V">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=zGtTQTD1zu">OmniNav: A Unified Framework for Prospective Exploration and Visual-Language Navigation</a></td>
<td nowrap>OmniNav uses a unified waypoint policy to handle instruction-goal navigation, object-goal navigation, point-goal navigation, and frontier exploration.</td>
<td nowrap>Unified Navigation/Exploration</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>continuous waypoint policy</td>
<td nowrap>real-time 5Hz deployment claimed</td>
<td nowrap>Unifies multiple navigation paradigms and supports low-latency continuous-space waypoint outputs.</td>
<td nowrap><a href="https://openreview.net/forum?id=zGtTQTD1zu">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=0c7nAZjyr5">From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning</a></td>
<td nowrap>S2E post-trains offline video-pretrained navigation models with reinforcement learning to learn action consequences, obstacle avoidance, and urban interaction behaviors.</td>
<td nowrap>continuous VLN</td>
<td nowrap>urban/dynamic environment</td>
<td nowrap>-</td>
<td nowrap>offline pretraining + RL post-training</td>
<td nowrap>-</td>
<td nowrap>Interactive safe navigation generalization</td>
<td nowrap><a href="https://openreview.net/forum?id=0c7nAZjyr5">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=apaLoTumdO">CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation</a></td>
<td nowrap>CE-Nav first uses a flow model to learn cross-embodiment feasible action distributions, then refines them with RL for specific robot dynamics.</td>
<td nowrap>Cross-embodiment Local Navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>IL + RL, conditional normalizing flow</td>
<td nowrap>-</td>
<td nowrap>Cross-morphology local navigation generalization</td>
<td nowrap><a href="https://openreview.net/forum?id=apaLoTumdO">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=bMrH2PFMsi">CoNavBench: Collaborative Long-Horizon Vision-Language Navigation Benchmark</a></td>
<td nowrap>CoNavBench provides 4,048 single-agent/collaborative long-horizon VLN episodes for evaluating handoffs, congestion, and collaborative navigation.</td>
<td nowrap>Collaborative Long-horizon VLN Benchmark</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>VLN policy</td>
<td nowrap>Benchmark</td>
<td nowrap>Collaborative VLN evaluation</td>
<td nowrap><a href="https://openreview.net/forum?id=bMrH2PFMsi">paper</a></td>
<td nowrap><a href="https://navcraft.github.io">project</a></td>
<td nowrap>-</td>
<td nowrap>CoNavBench/NavCraft</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38886">NaVLA$^2$: A Vision-Language-Audio-Action Model for Multimodal Instruction Navigation</a></td>
<td nowrap>NaVLA2 proposes the MINav task, using language, image, and audio cues to disambiguate navigation instructions and build 43.9K episodes.</td>
<td nowrap>Multimodal Instruction Navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>vision-language-audio-action policy</td>
<td nowrap>MINav benchmark</td>
<td nowrap>Addresses target grounding ambiguity caused by language-only instructions being insufficient in scenes with multiple similar objects.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38886">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38888">VPN: Visual Prompt Navigation</a></td>
<td nowrap>VPN replaces natural-language instructions with 2D top-down visual prompts and extends R2R/R2R-CE to form the VP dataset.</td>
<td nowrap>visual prompt navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>top-view map prompt</td>
<td nowrap>VLN policy</td>
<td nowrap>R2R-VP/R2R-CE-VP</td>
<td nowrap>Studies navigation guided by user-drawn/marked visual path prompts.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38888">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38891">SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning</a></td>
<td nowrap>SeqWalker targets long-horizon multi-task instructions, using high-level sub-instruction selection and low-level exploration verification to reduce information overload.</td>
<td nowrap>Long-horizon/Sequential VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>hierarchical planning</td>
<td nowrap>-</td>
<td nowrap>Long-instruction decomposition and execution</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38891">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38895">UNeMo: Collaborative Visual-Language Reasoning and Navigation via a Multimodal World Model</a></td>
<td nowrap>UNeMo jointly optimizes visual state reasoning and navigation decisions with a multimodal world model, filling the gap in VLN methods that reason only with language.</td>
<td nowrap>World-model VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>multimodal world model collaborative optimization</td>
<td nowrap>-</td>
<td nowrap>Addresses the separation between LLM reasoning modules and navigation policies, and the lack of visual reasoning.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38895">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38914">DNOI-4DRO: Deep 4D Radar Odometry with Differentiable Neural-Optimization Iterations</a></td>
<td nowrap>DNOI-4DRO combines a 4D radar motion-flow network with differentiable Gauss-Newton optimization to improve radar odometry accuracy.</td>
<td nowrap>4D radar odometry, not VLN</td>
<td nowrap>Mobile robot/autonomous-driving radar localization</td>
<td nowrap>-</td>
<td nowrap>differentiable neural optimization</td>
<td nowrap>VoD/Snail-Radar</td>
<td nowrap>Addresses self-localization/odometry estimation in sparse 4D radar point clouds.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38914">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38954">Run, Ruminate, and Regulate: A Dual-process Thinking System for Vision-and-Language Navigation</a></td>
<td nowrap>R3 combines fast execution, slow LLM reflection, and a regulation module to improve zero-shot VLN reasoning and efficiency.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>dual-process LLM reasoning</td>
<td nowrap>-</td>
<td nowrap>Zero-shot VLN reasoning efficiency and performance</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38954">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61535">AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation</a></td>
<td nowrap>AdaNav triggers uncertainty-aware reasoning with action entropy, avoiding extra computation and performance loss from fixed-interval reasoning.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>uncertainty-adaptive reasoning + RL refinement</td>
<td nowrap>-</td>
<td nowrap>Adaptive reasoning trigger</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61535">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61535">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64780">Instruction Decomposition and Action Alignment for Vision-Language Navigation</a></td>
<td nowrap>IDEAL-VLN decomposes long instructions into causal execution chains and performs action alignment to reduce irrelevant text interference and visual token latency.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>instruction decomposition + action alignment</td>
<td nowrap>-</td>
<td nowrap>Long-horizon instruction decomposition and execution</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64780">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64780">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65809">TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments</a></td>
<td nowrap>TIC-VLA explicitly models semantic reasoning latency and feeds delayed vision-language states into real-time action control.</td>
<td nowrap>VLA robot navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>latency-aware VLA control</td>
<td nowrap>-</td>
<td nowrap>Enables language instruction following and real-time reactive control in dynamic human environments.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/65809">paper</a></td>
<td nowrap><a href="https://ucla-mobility.github.io/TIC-VLA/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61357">Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning</a></td>
<td nowrap>Hydra-Nav adaptively switches between slow history-based reasoning and fast reactions in object navigation, balancing success rate and computational efficiency.</td>
<td nowrap>ObjectNav</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>adaptive dual-process VLM reasoning</td>
<td nowrap>-</td>
<td nowrap>Addresses weak spatiotemporal reasoning and high reasoning overhead in unseen object navigation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/61357">paper</a></td>
<td nowrap><a href="https://zixuan-wang99.github.io/Hydra-Nav/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60775">SafeDec: Constrained Decoding for Safe Autoregressive Generalist Robot Navigation Policies</a></td>
<td nowrap>SafeDec performs constraint decoding for autoregressive robot navigation policies, enforcing safety constraints while generating action sequences.</td>
<td nowrap>Safety-constrained robot navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>constrained decoding</td>
<td nowrap>-</td>
<td nowrap>Adds explicit safety correctness to physically executable general navigation policies.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/60775">paper</a></td>
<td nowrap><a href="https://constrained-robot-fms.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20620">Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI</a></td>
<td nowrap>Wanderland is a real-to-sim framework that uses multi-sensor capture and geometrically reliable reconstruction to build open-world navigation simulation benchmarks.</td>
<td nowrap>Simulation/evaluation platform</td>
<td nowrap>Open-city simulation</td>
<td nowrap>-</td>
<td nowrap>planning / RL</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>Provides a geometrically grounded open-city closed-loop evaluation environment for embodied AI.</td>
<td nowrap><a href="https://arxiv.org/abs/2511.20620">paper</a></td>
<td nowrap><a href="https://ai4ce.github.io/wanderland/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2512.04069">SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL</a></td>
<td nowrap>SpaceTools uses dual-interaction RL to learn tool calls for depth, segmentation, pose, and other tools to enhance VLM metric spatial reasoning.</td>
<td nowrap>Tool-augmented spatial reasoning</td>
<td nowrap>mobile robot/navigation environment</td>
<td nowrap>-</td>
<td nowrap>double interactive RL</td>
<td nowrap>-</td>
<td nowrap>Addresses VLMs' lack of precise metric ability in embodied spatial reasoning.</td>
<td nowrap><a href="https://arxiv.org/abs/2512.04069">paper</a></td>
<td nowrap><a href="https://spacetools.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2512.17907">Dexterous World Models</a></td>
<td nowrap>DWM is a scene-action-conditioned video diffusion world model that uses hand actions to drive static 3D scenes into dynamic interaction videos.</td>
<td nowrap>Dexterous-interaction world model, not VLN</td>
<td nowrap>egocentric hand-scene interaction</td>
<td nowrap>-</td>
<td nowrap>world model / planning / RL</td>
<td nowrap>-</td>
<td nowrap>Predicts dynamic changes after dexterous human-hand interaction with 3D scenes.</td>
<td nowrap><a href="https://arxiv.org/abs/2512.17907">paper</a></td>
<td nowrap><a href="https://snuvclab.github.io/dwm/">project</a></td>
<td nowrap><a href="https://snuvclab/dwm">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2508.09423">Distilling LLM Prior to Flow Model for Generalizable Agent’s Imagination in Object Goal Navigation</a></td>
<td nowrap>GOAL distills LLM spatial priors into a flow model, using generative semantic-map imagination to support ObjectNav.</td>
<td nowrap>ObjectNav/semantic map imagination</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>flow matching + LLM prior</td>
<td nowrap>-</td>
<td nowrap>Completes unobserved areas in unseen indoor environments to improve object-goal navigation.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.09423">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://Badi-Li/GOAL">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2511.17225">TP-MDDN: Task-Preferenced Multi-Demand-Driven Navigation with Autonomous Decision-Making</a></td>
<td nowrap>TP-MDDN proposes a multi-demand, preference-aware long-horizon navigation benchmark and uses AWMSystem to decompose demands, select goals, monitor state, and correct errors.</td>
<td nowrap>multi-demand-driven navigation benchmark</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>MASMap 3D point cloud + 2D semantic map</td>
<td nowrap>LLM/MLLM autonomous decision system</td>
<td nowrap>-</td>
<td nowrap>Addresses long-horizon demand-driven navigation under multiple sub-demands and explicit preference constraints.</td>
<td nowrap><a href="https://arxiv.org/abs/2511.17225">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.06630">Active Test-time Vision-Language Navigation</a></td>
<td nowrap>ATENA actively learns at test time and reduces uncertainty with entropy minimization, reducing accumulated errors when VLN is deployed in new environments.</td>
<td nowrap>continuous VLN</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>test-time active learning/adaptation</td>
<td nowrap>-</td>
<td nowrap>Performs VLN test-time adaptation without external feedback.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.06630">paper</a></td>
<td nowrap><a href="https://kuai-lab.github.io/neurips2025atena/">project</a></td>
<td nowrap><a href="https://kuai-lab/NeurIPS25_att_vln">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.00441">Seeing through Uncertainty: Robust Task-Oriented Optimization in Visual Navigation</a></td>
<td nowrap>NeuRO couples perception networks with task-level robust optimization to handle noise and OOD generalization in few-shot visual navigation.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>learning-to-optimize robust optimization</td>
<td nowrap>-</td>
<td nowrap>Addresses overfitting in long-horizon multi-goal visual navigation policies under data scarcity.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.00441">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://PyyWill/NeuRO">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.18525">RoboTron-Nav: A Unified Framework for Embodied Navigation Integrating Perception, Planning, and Prediction</a></td>
<td nowrap>RoboTron-Nav integrates perception, planning, and prediction through multitask collaboration between navigation and embodied QA, reducing history redundancy.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>multitask navigation + EQA</td>
<td nowrap>-</td>
<td nowrap>Improves perception, planning, and prediction in unseen environments for language-guided visual navigation.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.18525">paper</a></td>
<td nowrap><a href="https://yvfengzhong.github.io/RoboTron-Nav">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05552">SAME: Learning Generic Language-Guided Visual Navigation with State-Adaptive Mixture of Experts</a></td>
<td nowrap>SAME uses state-adaptive MoE to unify high-level category search and low-level language-guided navigation.</td>
<td nowrap>generic language-guided visual navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>state-adaptive MoE</td>
<td nowrap>-</td>
<td nowrap>Learns a general policy that can be shared across multiple categories of language-guided navigation tasks.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.05552">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://GengzeZhou/SAME">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1984">Embodied Navigation with Auxiliary Task of Action Description Prediction</a></td>
<td nowrap>This paper uses language descriptions of actions as an auxiliary RL task, allowing the navigation policy to explain its own actions while maintaining performance.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>RL + action description auxiliary task</td>
<td nowrap>-</td>
<td nowrap>Interpretable navigation action prediction</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1984">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2412.10439">CogNav: Cognitive Process Modeling for Object Goal Navigation with LLMs</a></td>
<td nowrap>CogNav uses an LLM to model goal memory and cognitive update processes, strengthening high-level decision-making in ObjectNav.</td>
<td nowrap>ObjectNav</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>cognitive memory</td>
<td nowrap>LLM planning</td>
<td nowrap>-</td>
<td nowrap>Enables an ObjectNav agent to have human-like cognitive map updates and goal reasoning.</td>
<td nowrap><a href="https://arxiv.org/abs/2412.10439">paper</a></td>
<td nowrap><a href="https://yhancao.github.io/CogNav/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11081">MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation</a></td>
<td nowrap>MoMa-Kitchen provides 100K+ kitchen samples, annotating the final navigation stop pose that benefits subsequent manipulation.</td>
<td nowrap>mobile manipulation last-mile navigation benchmark</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>affordance-grounded labels</td>
<td nowrap>affordance</td>
<td nowrap>Benchmark</td>
<td nowrap>Evaluates whether mobile manipulation can stop at a manipulable position after approaching the target.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.11081">paper</a></td>
<td nowrap><a href="https://momakitchen.github.io/">project</a></td>
<td nowrap><a href="https://MoMaKitchen/MoMaKitchen">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/IPEC-COMMUNITY/MoMa-Kitchen-Data">hf</a></td>
</tr>
</tbody>
</table>

#### Map Memory

Total: 23 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Task Type</th>
<th nowrap>Environment</th>
<th nowrap>Map/Memory</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CoRL 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2407.07775">Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs</a></td>
<td nowrap>Mobility VLA combines long-context VLMs with topological graphs for instruction navigation.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>embodied navigation</td>
<td nowrap>language/spatial context</td>
<td nowrap>CoRL navigation method</td>
<td nowrap>VLN / embodied navigation benchmarks</td>
<td nowrap>Add CoRL navigation coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2407.07775">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ACL 2024</td>
<td nowrap><a href="https://aclanthology.org/2024.acl-long.529/">MapGPT: Map-Guided Prompting for Unified Vision-and-Language Navigation</a></td>
<td nowrap>MapGPT uses map-guided prompting to connect language instructions with spatial navigation decisions.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>indoor VLN</td>
<td nowrap>map-guided prompt memory</td>
<td nowrap>LLM prompting + navigation</td>
<td nowrap>VLN benchmarks</td>
<td nowrap>Use explicit maps to ground LLM navigation decisions.</td>
<td nowrap><a href="https://aclanthology.org/2024.acl-long.529.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_OVER-NAV_Elevating_Iterative_Vision-and-Language_Navigation_with_Open-Vocabulary_Detection_and_StructurEd_CVPR_2024_paper.html">OVER-NAV: Elevating Iterative Vision-and-Language Navigation with Open-Vocabulary Detection and Structured Representation</a></td>
<td nowrap>OVER-NAV combines open-vocabulary detection with structured scene memory for iterative VLN.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>indoor VLN</td>
<td nowrap>open-vocabulary structured memory</td>
<td nowrap>iterative navigation planning</td>
<td nowrap>VLN benchmarks</td>
<td nowrap>Improve VLN grounding with open-vocabulary object and scene structure.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_OVER-NAV_Elevating_Iterative_Vision-and-Language_Navigation_with_Open-Vocabulary_Detection_and_StructurEd_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2403.14158">Volumetric Environment Representation for Vision-Language Navigation</a></td>
<td nowrap>VER builds volumetric scene representations to improve spatial memory and grounding in VLN.</td>
<td nowrap>Vision-language navigation</td>
<td nowrap>3D indoor navigation</td>
<td nowrap>volumetric map memory</td>
<td nowrap>3D representation learning</td>
<td nowrap>VLN benchmarks</td>
<td nowrap>Represent navigable space volumetrically for language-guided navigation.</td>
<td nowrap><a href="https://arxiv.org/abs/2403.14158">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>IROS 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2606.25497">SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation</a></td>
<td nowrap>SAGE-Nav combines LLM high-level planning with hierarchical scene graphs to guide object-goal navigation.</td>
<td nowrap>Object-goal navigation</td>
<td nowrap>indoor navigation</td>
<td nowrap>hierarchical scene graph</td>
<td nowrap>LLM planning + alignment fusion</td>
<td nowrap>Benchmark</td>
<td nowrap>Ground language planning in target navigation through scene-graph memory.</td>
<td nowrap><a href="https://arxiv.org/abs/2606.25497">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>IROS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.02247">WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation</a></td>
<td nowrap>WMNav integrates VLMs into a navigation world model to predict future states and maintain navigation memory for better target search.</td>
<td nowrap>Object-goal navigation</td>
<td nowrap>indoor navigation</td>
<td nowrap>world-model memory</td>
<td nowrap>VLM-guided world model</td>
<td nowrap>Benchmark</td>
<td nowrap>Use world-model imagination and feedback to support object-goal navigation.</td>
<td nowrap><a href="https://arxiv.org/abs/2503.02247">paper</a></td>
<td nowrap><a href="https://b0b8k1ng.github.io/WMNav/">project</a></td>
<td nowrap><a href="https://B0B8K1ng/WMNavigation">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=HB6KvsqcAn">Towards Physically Executable 3D Gaussian for Embodied Navigation</a></td>
<td nowrap>SAGE-3D upgrades 3DGS into a navigation-environment representation with object semantics and physical executability.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>semantic and physically aligned 3D Gaussian</td>
<td nowrap>3DGS environment construction</td>
<td nowrap>-</td>
<td nowrap>3DGS-executable navigation environment</td>
<td nowrap><a href="https://openreview.net/forum?id=HB6KvsqcAn">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=LPv59noPAy">Uncertainty-Aware Gaussian Map for Vision-Language Navigation</a></td>
<td nowrap>This paper builds a semantic Gaussian Map and explicitly encodes geometric, semantic, and appearance uncertainty to guide VLN actions.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>uncertainty-aware semantic Gaussian map</td>
<td nowrap>uncertainty-informed policy</td>
<td nowrap>-</td>
<td nowrap>Uses perception uncertainty in VLN decisions instead of ignoring ambiguous observations.</td>
<td nowrap><a href="https://openreview.net/forum?id=LPv59noPAy">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=RnuB0Nlbd5">JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation</a></td>
<td nowrap>JanusVLN uses dual implicit memories to separately model semantic and spatial information, reducing redundancy and spatial loss from explicit text/frame memories.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>Map/memory</td>
<td nowrap>dual implicit neural memory; KV-cache incremental update</td>
<td nowrap>VLN benchmark</td>
<td nowrap>Addresses explicit memory bloat and spatial information loss in MLLM-VLN.</td>
<td nowrap><a href="https://openreview.net/forum?id=RnuB0Nlbd5">paper</a></td>
<td nowrap><a href="https://miv-xjtu.github.io/JanusVLN.github.io/">project</a></td>
<td nowrap><a href="https://MIV-XJTU/JanusVLN">code</a></td>
<td nowrap><a href="https://miv-xjtu.github.io/JanusVLN.github.io/">data</a></td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=li1vfqDzRD">Emergence of Spatial Representation in an Actor-Critic Agent with Hippocampus-Inspired Sequence Generator</a></td>
<td nowrap>This paper uses a hippocampus-inspired sequence generator as a temporal memory buffer to explain the emergence of spatial representations in actor-critic navigation agents.</td>
<td nowrap>Neuro-inspired visual navigation/RL</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>hippocampus-inspired temporal sequence memory</td>
<td nowrap>actor-critic RL</td>
<td nowrap>-</td>
<td nowrap>Studies how spatial representations emerge from sequence-memory mechanisms in continuous maze visual navigation.</td>
<td nowrap><a href="https://openreview.net/forum?id=li1vfqDzRD">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=KcC5mwfGf0">GRL-SNAM: Geometric Reinforcement Learning with Differential Hamiltonians for Navigation and Mapping in Unknown Environments</a></td>
<td nowrap>GRL-SNAM uses local perception to construct a Hamiltonian energy landscape, jointly navigating and mapping in unknown environments without building a global map.</td>
<td nowrap>simultaneous navigation and mapping</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>local energy landscape/no global map</td>
<td nowrap>geometric RL</td>
<td nowrap>-</td>
<td nowrap>Performs simultaneous navigation and mapping in unknown environments.</td>
<td nowrap><a href="https://openreview.net/forum?id=KcC5mwfGf0">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38884">RflyPano: A Panoramic Benchmark for Ultra-low Altitude UAV Localization Powered by RflySim</a></td>
<td nowrap>RflyPano is a panoramic dataset for UAV visual localization below 120 meters, generated from RflySim with four fisheye cameras.</td>
<td nowrap>UAV localization benchmark</td>
<td nowrap>Ultra-low-altitude UAV / RflySim simulation</td>
<td nowrap>Evaluation/data rather than map memory</td>
<td nowrap>localization</td>
<td nowrap>Benchmark</td>
<td nowrap>Provides a panoramic visual localization benchmark for low-altitude UAV scenarios with unreliable GNSS.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38884">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://DUNDAI1998/RflyPano">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38887">MHED-SLAM: Multi-Scale Hybrid Encoding-Based Decoupled SLAM</a></td>
<td nowrap>MHED-SLAM uses multiscale hybrid encoding and decoupled geometry/color modeling to improve NeRF-SLAM mapping and tracking quality.</td>
<td nowrap>SLAM</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>neural scene representation</td>
<td nowrap>NeRF/TSDF SLAM</td>
<td nowrap>-</td>
<td nowrap>Visual SLAM mapping and localization</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38887">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38893">LOG-Nav: Efficient Layout-Aware Object-Goal Navigation with Hierarchical Planning</a></td>
<td nowrap>LOG-Nav uses global topological layout maps and local scene memory for hierarchical planning, improving multi-room ObjectNav efficiency.</td>
<td nowrap>ObjectNav</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>topological layout map + local scene memory</td>
<td nowrap>LLM hierarchical planning/no costly training</td>
<td nowrap>-</td>
<td nowrap>Enables an LLM agent to efficiently find objects in complex indoor multi-room environments.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38893">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38899">PanoNav: Mapless Zero-Shot Object Navigation with Panoramic Scene Parsing and Dynamic Memory</a></td>
<td nowrap>PanoNav uses RGB-only panoramic scene parsing and dynamic memory to achieve map-free zero-shot ObjectNav.</td>
<td nowrap>zero-shot ObjectNav</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>dynamic memory/mapless RGB-only</td>
<td nowrap>MLLM reasoning</td>
<td nowrap>-</td>
<td nowrap>Performs zero-shot object navigation without depth or prebuilt maps.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38899">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38901">Lightweight Adaptive Topological Layout and Semantic Mapping in Vision-and-Language Navigation on Websites</a></td>
<td nowrap>ATLAS builds a lightweight adaptive topological layout and semantic graph for website VLN, improving web navigation accuracy and inference speed.</td>
<td nowrap>Map/memory</td>
<td nowrap>Web navigation, not physical robotics</td>
<td nowrap>adaptive topological layout + semantic map</td>
<td nowrap>LLM web navigation</td>
<td nowrap>-</td>
<td nowrap>Addresses navigation and QA for web agents in open, dynamic webpage structures.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38901">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38929">Expand Your SCOPE: Semantic Cognition over Potential-Based Exploration for Embodied Visual Navigation</a></td>
<td nowrap>SCOPE models the relationship between local observations and navigation goals with frontier boundaries and potential-based exploration, performing zero-shot visual navigation.</td>
<td nowrap>zero-shot embodied visual navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>frontier/potential-based semantic memory</td>
<td nowrap>zero-shot framework</td>
<td nowrap>-</td>
<td nowrap>Improves long-horizon planning for goal-directed exploration in unknown environments.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38929">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38948">Agent Journey Beyond RGB: Hierarchical Semantic-Spatial Representation Enrichment for Vision-and-Language Navigation</a></td>
<td nowrap>SUSA fuses non-RGB representations with hierarchical semantic understanding and spatial awareness to strengthen semantic-spatial grounding in VLN.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>hierarchical semantic-spatial representation</td>
<td nowrap>representation enrichment</td>
<td nowrap>-</td>
<td nowrap>Addresses insufficient use of multimodal environment representations in egocentric VLN.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38948">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64902">MapDream: Task-Driven Map Learning for Vision-Language Navigation</a></td>
<td nowrap>MapDream formulates map building as task-driven BEV image autoregressive generation rather than manual map reconstruction.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>learned task-driven BEV map</td>
<td nowrap>map-in-the-loop autoregressive BEV synthesis</td>
<td nowrap>-</td>
<td nowrap>Learns map representations that directly serve navigation goals.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64902">paper</a></td>
<td nowrap><a href="https://horizonrobotics.github.io/robot_lab/mapdream/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2026</td>
<td nowrap><a href="https://arxiv.org/abs/2605.01736">GLMap: Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning</a></td>
<td nowrap>GLMap uses multiscale semantic units to store natural-language descriptions and 3D Gaussian simultaneously, enabling zero-shot navigation and reasoning.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>multi-scale Gaussian-language map</td>
<td nowrap>zero-shot navigation/reasoning</td>
<td nowrap>-</td>
<td nowrap>Provides large models with a geometrically explicit, semantically multiscale 3D map interface.</td>
<td nowrap><a href="https://arxiv.org/abs/2605.01736">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://sx-zhang/GLMap">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.18546">EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval</a></td>
<td nowrap>EfficientNav uses navigation-map caching and retrieval to reduce long prompts and latency when local small LLMs perform ObjectNav.</td>
<td nowrap>on-device ObjectNav</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>navigation map caching/retrieval</td>
<td nowrap>small LLM planning</td>
<td nowrap>-</td>
<td nowrap>Efficiently performs zero-shot ObjectNav on edge devices.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.18546">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://PKU-SEC-Lab/EfficientNav">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04047">Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation</a></td>
<td nowrap>MTU3D combines active exploration with 3D vision-language grounding, letting the agent complete scene understanding through movement.</td>
<td nowrap>active 3D scene understanding/navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>3D-VL active perception</td>
<td nowrap>3D representation</td>
<td nowrap>-</td>
<td nowrap>Decides where to look to improve 3D scene grounding and navigation efficiency.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.04047">paper</a></td>
<td nowrap><a href="https://mtu3d.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/944">NavQ: Learning a Q-Model for Foresighted Vision-and-Language Navigation</a></td>
<td nowrap>NavQ trains a Q-model on large-scale unlabeled trajectories to estimate future visible information for candidate actions and support look-ahead decisions.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>foresighted Q-feature from trajectory data</td>
<td nowrap>Q-learning on unlabeled trajectories</td>
<td nowrap>-</td>
<td nowrap>Look-ahead VLN decision-making</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/944">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
</tbody>
</table>

#### Physically Executable Navigation

Total: 7 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Task Type</th>
<th nowrap>Environment</th>
<th nowrap>Map/Memory</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.html">SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World</a></td>
<td nowrap>SPOC trains embodied agents from simulated shortest paths and transfers the behavior to navigation and manipulation.</td>
<td nowrap>Navigation + manipulation</td>
<td nowrap>physical embodied environments</td>
<td nowrap>implicit spatial policy memory</td>
<td nowrap>imitation from shortest paths</td>
<td nowrap>Sim + Real</td>
<td nowrap>Convert shortest-path supervision into physically executable embodied behavior.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38942">CorrectNav: Self-Correction Flywheel Empowers Vision-Language-Action Navigation Model</a></td>
<td nowrap>CorrectNav automatically generates perception and action self-correction data from model error trajectories, then post-trains VLA navigation models.</td>
<td nowrap>VLA navigation self-correction</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>self-correction flywheel/post-training</td>
<td nowrap>-</td>
<td nowrap>Enables VLA navigation models to recover after deviating from the correct trajectory.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38942">paper</a></td>
<td nowrap><a href="https://correctnav.github.io/">project</a></td>
<td nowrap><a href="https://owlet914/CorrectNav">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64257">SC$^{2}$-WM: A Self-Correcting World Model with Closed-Loop Feedback for Vision-and-Language Navigation in Continuous Environments</a></td>
<td nowrap>SC2-WM uses world-model look-ahead to generate internal feedback, correcting state drift and plans in a closed loop during VLN-CE inference.</td>
<td nowrap>World-model Navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>world-model foresight/internal feedback</td>
<td nowrap>closed-loop self-correcting world model</td>
<td nowrap>-</td>
<td nowrap>Addresses the inability of open-loop execution in continuous VLN to detect and correct internal state drift.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64257">paper</a></td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/64257">project</a></td>
<td nowrap><a href="https://sunrise-ikun/SC2_WM">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2507.13019">Rethinking the Embodied Gap in Vision-and-Language Navigation: A Holistic Study of Physical and Visual Disparities</a></td>
<td nowrap>VLN-PE systematically evaluates how visual and physical differences across humanoid, quadruped, and wheeled robots affect VLN.</td>
<td nowrap>physical VLN evaluation</td>
<td nowrap>humanoid/quadruped/wheeled robots</td>
<td nowrap>-</td>
<td nowrap>embodied navigation</td>
<td nowrap>physical robotic settings</td>
<td nowrap>Measures the embodied gap between ideal VLN assumptions and real robot execution.</td>
<td nowrap><a href="https://arxiv.org/abs/2507.13019">paper</a></td>
<td nowrap><a href="https://crystalsixone.github.io/vln_pe.github.io/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23468">NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments</a></td>
<td nowrap>NavMorph uses a self-evolving world model and contextual evolving memory to model VLN-CE environment dynamics ahead of time and refine policies.</td>
<td nowrap>World-model Navigation</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>contextual evolution memory</td>
<td nowrap>self-evolving world model/RL</td>
<td nowrap>-</td>
<td nowrap>Improves adaptive planning for continuous VLN in new environments and process changes.</td>
<td nowrap><a href="https://arxiv.org/abs/2506.23468">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://Feliciaxyao/NavMorph">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/299">3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation</a></td>
<td nowrap>This paper uses open-set semantic grouping to unify 3D geometric priors and open semantics in a Gaussian map.</td>
<td nowrap>Map/memory</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>3D Gaussian map + open-set semantic grouping</td>
<td nowrap>3D representation</td>
<td nowrap>-</td>
<td nowrap>Open-semantic 3D map for VLN</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/299">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1792">monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation</a></td>
<td nowrap>monoVLN uses 3DGS to complete missing regions in monocular RGBD observations, narrowing the observation gap between monocular robots and panoramic VLN settings.</td>
<td nowrap>monocular VLN</td>
<td nowrap>monocular RGBD robot</td>
<td nowrap>3DGS implicit partial completion</td>
<td nowrap>embodied navigation</td>
<td nowrap>-</td>
<td nowrap>Enables robots with only a monocular camera to perform VLN that originally relied on panoramic observations.</td>
<td nowrap><a href="https://iccv.thecvf.com/virtual/2025/poster/1792">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
</tbody>
</table>

#### Urban / Open-world Navigation

Total: 20 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Task Type</th>
<th nowrap>Environment</th>
<th nowrap>Map/Memory</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>CVPR 2024</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Khanna_GOAT-Bench_A_Benchmark_for_Multi-Modal_Lifelong_Navigation_CVPR_2024_paper.html">GOAT-Bench: A Benchmark for Multi-Modal Lifelong Navigation</a></td>
<td nowrap>GOAT-Bench evaluates lifelong navigation with multimodal goals and open-ended object/place targets.</td>
<td nowrap>Lifelong navigation benchmark</td>
<td nowrap>open-world indoor scenes</td>
<td nowrap>goal-conditioned memory</td>
<td nowrap>benchmark evaluation</td>
<td nowrap>GOAT-Bench</td>
<td nowrap>Measure multimodal lifelong navigation beyond single instruction episodes.</td>
<td nowrap><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Khanna_GOAT-Bench_A_Benchmark_for_Multi-Modal_Lifelong_Navigation_CVPR_2024_paper.pdf">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ECCV 2024</td>
<td nowrap><a href="https://arxiv.org/pdf/2407.14758">DISCO: Embodied Navigation and Interaction via Differentiable Scene-Conditioned Options</a></td>
<td nowrap>DISCO learns scene-conditioned options for embodied navigation and interaction in open environments.</td>
<td nowrap>Navigation + interaction</td>
<td nowrap>open embodied scenes</td>
<td nowrap>scene-conditioned options</td>
<td nowrap>option learning</td>
<td nowrap>Embodied interaction benchmarks</td>
<td nowrap>Tie navigation and interaction through reusable scene-conditioned options.</td>
<td nowrap><a href="https://arxiv.org/pdf/2407.14758">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=88RKxlFUNY">AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild</a></td>
<td nowrap>AutoFly is an end-to-end UAV VLA model that uses pseudo-depth encoding and two-stage training to support continuous outdoor planning and obstacle avoidance.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>-</td>
<td nowrap>two-stage VLA training</td>
<td nowrap>sim+real UAV</td>
<td nowrap>Shifts from explicit route following to autonomous UAV navigation under coarse-grained instructions.</td>
<td nowrap><a href="https://arxiv.org/abs/2602.09657">paper</a></td>
<td nowrap><a href="https://xiaolousun.github.io/AutoFly/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=OKm3w71ymP">OpenFly: A Comprehensive Platform for Aerial Vision-Language Navigation</a></td>
<td nowrap>OpenFly integrates UE, GTA V, Google Earth, and 3DGS to generate large-scale aerial VLN data and platforms.</td>
<td nowrap>aerial VLN platform/benchmark</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>Reduces the cost of collecting UAV VLN data and provides an aerial navigation evaluation platform.</td>
<td nowrap><a href="https://openreview.net/forum?id=OKm3w71ymP">paper</a></td>
<td nowrap><a href="https://shailab-ipec.github.io/openfly/">project</a></td>
<td nowrap><a href="https://Eziotic/OpenFly">code</a></td>
<td nowrap><a href="https://shailab-ipec.github.io/openfly/">data</a></td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=qSak1Hjfdq">All-day Multi-scenes Lifelong Vision-and-Language Navigation with Tucker Adaptation</a></td>
<td nowrap>TuKA represents multi-scene, multi-time navigation knowledge as Tucker-decomposition adapters, mitigating forgetting in all-day multi-scene VLN.</td>
<td nowrap>lifelong VLN</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>-</td>
<td nowrap>Tucker Adaptation/parameter-efficient tuning</td>
<td nowrap>-</td>
<td nowrap>All-day multi-scene continual adaptation</td>
<td nowrap><a href="https://openreview.net/forum?id=qSak1Hjfdq">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=PaYo96rjij">Lifelong Embodied Navigation Learning</a></td>
<td nowrap>Uni-Walker uses DE-LoRA to separate shared and task-specific navigation knowledge, supporting continual learning over multi-task sequences.</td>
<td nowrap>lifelong embodied navigation</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>-</td>
<td nowrap>DE-LoRA continual learning</td>
<td nowrap>-</td>
<td nowrap>Continual learning of navigation skills</td>
<td nowrap><a href="https://openreview.net/forum?id=PaYo96rjij">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICLR 2026</td>
<td nowrap><a href="https://openreview.net/forum?id=hzf23XSDcs">CitySeeker: How Do VLMs Explore Embodied Urban Navigation with Implicit Human Needs?</a></td>
<td nowrap>CitySeeker uses 6,440 trajectories across 8 cities to evaluate whether a VLM can turn implicit needs such as "I'm thirsty" into urban navigation goals.</td>
<td nowrap>urban implicit-need navigation benchmark</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>Evaluates a VLM's ability to understand implicit human needs in urban environments and find target places.</td>
<td nowrap><a href="https://openreview.net/forum?id=hzf23XSDcs">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>CitySeeker 6,440 trajectories/8 cities</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38878">AerialVLA: A Vision-Language-Action Model for Aerial Navigation with Online Dialogue</a></td>
<td nowrap>AerialVLA targets UAV vision-dialog navigation, supporting active questioning and route correction using historical landmarks.</td>
<td nowrap>aerial visual dialogue navigation</td>
<td nowrap>UAV</td>
<td nowrap>-</td>
<td nowrap>online dialogue VLA</td>
<td nowrap>-</td>
<td nowrap>Enables UAVs to reach goals through online dialogue and actively correct navigation.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38878">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38885">History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation</a></td>
<td nowrap>HETT first uses historical grid maps for coarse target localization, then fine-grained visual analysis to optimize UAV actions.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>large-scale urban UAV</td>
<td nowrap>historical grid map</td>
<td nowrap>coarse-to-fine two-stage transformer</td>
<td nowrap>-</td>
<td nowrap>Balances global environment reasoning and local scene understanding in aerial VLN.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38885">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38897">RENEW: Risk- and Energy-Aware Navigation in Dynamic Waterways</a></td>
<td nowrap>RENEW plans risk- and energy-aware paths for ASVs under dynamic water-flow disturbances and adds adaptive safety constraints.</td>
<td nowrap>ASV global path planning</td>
<td nowrap>dynamic waterways</td>
<td nowrap>-</td>
<td nowrap>risk/energy-aware planning</td>
<td nowrap>-</td>
<td nowrap>Water navigation rather than VLN</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38897">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38898">Towards Autonomous UAV Visual Object Search in City Space: Benchmark and Agentic Methodology</a></td>
<td nowrap>CityAVOS provides 2,420 urban UAV visual target-search tasks and uses PRPSearcher for perception-reasoning-planning search.</td>
<td nowrap>UAV visual object search benchmark</td>
<td nowrap>UAV/urban environment</td>
<td nowrap>3D cognitive/uncertainty/dynamic semantic maps</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>Enables UAVs to autonomously search for static target objects in urban spaces.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38898">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>CityAVOS 2,420 tasks</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38916">UrbanNav: Learning Language-Guided Embodied Urban Navigation from Web-Scale Human Trajectories</a></td>
<td nowrap>UrbanNav aligns webpage-scale urban walking videos with language trajectories, training agents to navigate cities by free-form language.</td>
<td nowrap>language-guided urban navigation</td>
<td nowrap>ground urban robot</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>-</td>
<td nowrap>Supports last-mile robots in navigating unfamiliar urban streetscapes by natural language.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38916">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://CASIA-IVA-Lab/UrbanNav">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/Vigar001/UrbanNav">hf</a></td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38917">Autonomous Vehicle Path Planning by Searching with Differentiable Simulation</a></td>
<td nowrap>DSS uses the differentiable Waymax simulator as a state predictor and critic, searching autonomous-driving action sequences through gradients.</td>
<td nowrap>autonomous driving path planning</td>
<td nowrap>Waymax/traffic scenarios</td>
<td nowrap>-</td>
<td nowrap>differentiable simulation search</td>
<td nowrap>-</td>
<td nowrap>Autonomous-driving planning rather than VLN</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38917">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38920">Real-Time Path Planning for UAVs in Windy Environments Without Computational Fluid Dynamics</a></td>
<td nowrap>GZS avoids CFD and uses point-cloud local topology plus physics-inspired wind-risk modeling for real-time UAV path planning.</td>
<td nowrap>UAV real-time path planning</td>
<td nowrap>windy cluttered 3D environments</td>
<td nowrap>-</td>
<td nowrap>zero-shot training-free planning</td>
<td nowrap>-</td>
<td nowrap>Performs onboard real-time UAV planning in windy 3D environments with obstacles.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38920">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38938">ReflexDiffusion: Reflection-Enhanced Trajectory Planning for High-lateral-acceleration Scenarios in Autonomous Driving</a></td>
<td nowrap>ReflexDiffusion adds reflective gradient adjustment during diffusion trajectory-planning inference to handle long-tail high-lateral-acceleration scenarios.</td>
<td nowrap>autonomous driving trajectory planning</td>
<td nowrap>high-lateral-acceleration driving</td>
<td nowrap>-</td>
<td nowrap>inference-stage diffusion reflection</td>
<td nowrap>-</td>
<td nowrap>Autonomous-driving planning rather than open VLN</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38938">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>AAAI 2026</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38941">Learning from Human Gaze: Human-like Robot Social Navigation in Dense Crowds</a></td>
<td nowrap>GazeNav/Gaze2Nav uses human eye-tracking data to predict socially attended objects and injects that attention into motion planning in crowded spaces.</td>
<td nowrap>social navigation</td>
<td nowrap>dense crowds</td>
<td nowrap>gaze/semantic attention</td>
<td nowrap>open-world navigation</td>
<td nowrap>GazeNav dataset</td>
<td nowrap>Enables robots to perform more human-like social navigation in dense crowds.</td>
<td nowrap><a href="https://ojs.aaai.org/index.php/AAAI/article/view/38941">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICML 2026</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63554">Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation</a></td>
<td nowrap>SAGE lets agents learn in a physically grounded semantic abstraction sandbox and then transfer to open-world navigation.</td>
<td nowrap>Open-world Environment</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>physics-grounded abstracted experience/RL</td>
<td nowrap>-</td>
<td nowrap>Uses abstract physical experience to reduce reliance on realistic simulation and improve open-world navigation.</td>
<td nowrap><a href="https://icml.cc/virtual/2026/poster/63554">paper</a></td>
<td nowrap><a href="https://frankzxshen.github.io/SAGE">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2510.20685">C-NAV: Towards Self-Evolving Continual Object Navigation in Open World</a></td>
<td nowrap>C-Nav proposes a continual ObjectNav benchmark and uses a dual-path anti-forgetting mechanism to learn new object categories while preserving old knowledge.</td>
<td nowrap>continual ObjectNav benchmark</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>dual-path anti-forgetting/RL</td>
<td nowrap>-</td>
<td nowrap>Continually learns object navigation for new target categories in dynamic open worlds.</td>
<td nowrap><a href="https://arxiv.org/abs/2510.20685">paper</a></td>
<td nowrap><a href="https://bigtree765.github.io/C-Nav-project/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2512.10046">SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration</a></td>
<td nowrap>SimWorld-Robotics uses UE5 procedural generation for dynamic cities and provides a multimodal instruction navigation and multi-robot search collaboration benchmark.</td>
<td nowrap>urban simulation benchmark</td>
<td nowrap>Unmanned vehicles/urban environments</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Sim/Benchmark</td>
<td nowrap>Builds large-scale realistic urban simulation to evaluate robot open-environment navigation and collaboration.</td>
<td nowrap><a href="https://arxiv.org/abs/2512.10046">paper</a></td>
<td nowrap><a href="https://scai.cs.jhu.edu/projects/SimWorldRobotics/">project</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CVPR 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2408.15503">RoboSense: Large-scale Dataset and Benchmark for Egocentric Robot Perception and Navigation in Crowded and Unstructured Environments</a></td>
<td nowrap>RoboSense provides multi-sensor egocentric data from cameras, LiDAR, fisheye cameras, and more, evaluating perception and navigation in crowded unstructured environments.</td>
<td nowrap>Evaluation/Data</td>
<td nowrap>crowded/unstructured egocentric robot environments</td>
<td nowrap>-</td>
<td nowrap>open-world navigation</td>
<td nowrap>Benchmark</td>
<td nowrap>Builds a dataset and benchmark for near-field perception and navigation of mobile robots.</td>
<td nowrap><a href="https://arxiv.org/abs/2408.15503">paper</a></td>
<td nowrap>-</td>
<td nowrap><a href="https://suhaisheng/RoboSense">code</a></td>
<td nowrap><a href="https://huggingface.co/datasets/suhaisheng0527/RoboSense">hf</a></td>
</tr>
</tbody>
</table>

#### Low-cost / On-device Navigation

Total: 3 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Task Type</th>
<th nowrap>Environment</th>
<th nowrap>Map/Memory</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Sim/Real/Benchmark</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>NeurIPS 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11886">Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation</a></td>
<td nowrap>Aux-Think systematically compares No/Pre/Post-Think reasoning strategies, finds that reasoning in VLN may collapse, and builds R2R-CoT-320k.</td>
<td nowrap>data-efficient VLN reasoning</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>reasoning strategy evaluation</td>
<td nowrap>-</td>
<td nowrap>Studies which reasoning strategies are actually useful in data-efficient VLN.</td>
<td nowrap><a href="https://arxiv.org/abs/2505.11886">paper</a></td>
<td nowrap><a href="https://horizonrobotics.github.io/robot_lab/aux-think/">project</a></td>
<td nowrap>-</td>
<td nowrap>R2R-CoT-320k</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://openreview.net/pdf?id=5gptKWnVPF">Harnessing Input-Adaptive Inference for Efficient VLN</a></td>
<td nowrap>This paper applies input-adaptive reasoning at three levels: viewpoint selection, early-exit thresholds, and history-view caching, reducing VLN computation by more than 2x.</td>
<td nowrap>On-device/Low-cost</td>
<td nowrap>mobile robot/navigation environment</td>
<td nowrap>-</td>
<td nowrap>efficient navigation</td>
<td nowrap>7 VLN benchmarks</td>
<td nowrap>Reduces the inference cost of history-aware transformer VLN agents while maintaining performance.</td>
<td nowrap><a href="https://arxiv.org/abs/2508.09262">paper</a></td>
<td nowrap><a href="https://true-lab.ai/efficient_vln/">project</a></td>
<td nowrap><a href="https://secure-ai-systems-group/adaptive-vision-and-language-navigation">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>ICCV 2025</td>
<td nowrap><a href="https://arxiv.org/abs/2503.24065">COSMO: Combination of Selective Memorization for Low-cost Vision-and-Language Navigation</a></td>
<td nowrap>COSMO combines state-space modules and transformer, and designs RSS and cross-modal selective memory to reduce VLN computational cost.</td>
<td nowrap>On-device/Low-cost</td>
<td nowrap>mobile robot/mobile manipulation</td>
<td nowrap>-</td>
<td nowrap>selective state-space memorization + transformer</td>
<td nowrap>-</td>
<td nowrap>Low-cost VLN model architecture</td>
<td nowrap><a href="https://arxiv.org/abs/2503.24065">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>-</td>
</tr>
</tbody>
</table>

### VLA / Manipulation Policies

VLA is the main track for robotic arms and mobile manipulation, but it is not just an action head attached to a large model. Survey papers concentrate on action representation, diffusion/flow policies, 3D grounding, online/RL fine-tuning, and robustness.

Subdirections: generalist VLA, action representation, diffusion/flow policy, 3D grounding, online/RL fine-tuning, and safety/robustness.

Total: 251 papers.

<table>
<thead>
<tr>
<th nowrap>Subdirection</th>
<th nowrap>Entries</th>
<th nowrap>Focus</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>generalist VLA</td>
<td nowrap>80</td>
<td nowrap>Focus: cross-task generalization, real-robot validation, and general manipulation ability.</td>
</tr>
<tr>
<td nowrap>action representation</td>
<td nowrap>30</td>
<td nowrap>Focus: action tokens, latent actions, chunking, and action-space design.</td>
</tr>
<tr>
<td nowrap>diffusion/flow policy</td>
<td nowrap>72</td>
<td nowrap>Focus: continuous action generation, stable control, and smooth execution.</td>
</tr>
<tr>
<td nowrap>3D grounding</td>
<td nowrap>41</td>
<td nowrap>Focus: point clouds, geometry, affordance, and manipulation localization.</td>
</tr>
<tr>
<td nowrap>online/RL fine-tuning</td>
<td nowrap>21</td>
<td nowrap>Focus: online RL, human-in-the-loop learning, and test-time adaptation.</td>
</tr>
<tr>
<td nowrap>Safety and Robustness</td>
<td nowrap>7</td>
<td nowrap>Focus: attack robustness, safety alignment, and risk exposure.</td>
</tr>
</tbody>
</table>

#### generalist VLA

Total: 80 papers.

<table>
<thead>
<tr>
<th nowrap>Venue/Year</th>
<th nowrap>Paper/Method</th>
<th nowrap>Abstract</th>
<th nowrap>Base VLA</th>
<th nowrap>Action</th>
<th nowrap>Training/Feedback</th>
<th nowrap>Algorithm</th>
<th nowrap>Policy/Type</th>
<th nowrap>Sim/Real</th>
<th nowrap>Paper Task/Goal</th>
<th nowrap>Paper</th>
<th nowrap>Project</th>
<th nowrap>Code</th>
<th nowrap>Data/Bench</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap>LangRob @ CoRL 2023</td>
<td nowrap><a href="https://openreview.net/forum?id=3mKb5iyZ2V">Reasoning Tuning Grasp: Adapting Multi-Modal Large Language Models for Robotic Grasping</a></td>
<td nowrap>Tunes an MLLM to reason about and emit numerical planar grasp poses for a two-finger gripper.</td>
<td nowrap>LLaVA-7B-v0 + CLIP ViT-L/14</td>
<td nowrap>image grasp point [x,y] + end-effector rotation</td>
<td nowrap>Cornell: 885 images/240 objects with 74 reasoning categories; LoRA reasoning tuning; 135 real trials</td>
<td nowrap>reasoning-tuned multimodal LLM grasp prediction</td>
<td nowrap>parallel-gripper grasp-pose VLM; not a dexterous-hand controller</td>
<td nowrap>offline benchmark + Real; no physics simulator</td>
<td nowrap>Cornell image/object accuracy 84.05±0.78/77.02±0.93%; real LoRA 113/135 = 83.7%</td>
<td nowrap><a href="https://openreview.net/forum?id=3mKb5iyZ2V">paper</a></td>
<td nowrap>-</td>
<td nowrap>-</td>
<td nowrap>Cornell Grasp Dataset; 27 unseen objects × 5 poses</td>
</tr>
<tr>
<td nowrap>CoRL 2022</td>
<td nowrap><a href="https://arxiv.org/abs/2109.12098">CLIPort: What and Where Pathways for Robotic Manipulation</a></td>
<td nowrap>CLIPort combines CLIP semantics with transport-style spatial manipulation policies.</td>
<td nowrap>CLIPort</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2109.12098">paper</a></td>
<td nowrap><a href="https://cliport.github.io">project</a></td>
<td nowrap><a href="https://cliport/cliport">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2024</td>
<td nowrap><a href="https://arxiv.org/abs/2406.09246">OpenVLA: An Open-Source Vision-Language-Action Model</a></td>
<td nowrap>OpenVLA is an open-source VLA model for general robot manipulation.</td>
<td nowrap>OpenVLA</td>
<td nowrap>robot action</td>
<td nowrap>VLA / generalist VLA</td>
<td nowrap>CoRL robot-learning method</td>
<td nowrap>robot policy</td>
<td nowrap>robot benchmarks</td>
<td nowrap>Add CoRL VLA coverage.</td>
<td nowrap><a href="https://arxiv.org/abs/2406.09246">paper</a></td>
<td nowrap><a href="https://openvla.github.io">project</a></td>
<td nowrap><a href="https://openvla/openvla">code</a></td>
<td nowrap>-</td>
</tr>
<tr>
<td nowrap>CoRL 2023</td>
<td nowrap><a href="https://arxiv.org/abs/2307.15818">RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control</a><