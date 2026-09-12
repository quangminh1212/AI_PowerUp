<p align="center">
  <img src="assets/awesome-egocentric-atlas-cover.png" alt="Awesome Egocentric Atlas cover" width="100%">
</p>

<h1 align="center">Awesome Egocentric Atlas</h1>

<p align="center">
  <img src="assets/awesome-egocentric-logo.png" alt="Awesome Egocentric Atlas logo" width="118">
</p>

<p align="center">
  <strong>Datasets, benchmarks, models, and tools for egocentric AI.</strong>
</p>

<!-- LANG-BAR:START -->
<p align="center">
  <a href="README.md"><b>English</b></a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.es.md">Español</a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.pt.md">Português</a> ·
  <a href="CONTRIBUTING.md">Help translate</a> ·
  <a href="https://chaoyue0307.github.io/awesome-egocentric-atlas/">Landing page</a> ·
  <a href="https://huggingface.co/datasets/cy0307/awesome-egocentric-atlas">Hugging Face mirror</a>
</p>
<!-- LANG-BAR:END -->

<p align="center">
  <a href="https://github.com/sindresorhus/awesome"><img alt="awesome" src="https://awesome.re/badge-flat2.svg"></a>
  <a href="https://github.com/ChaoYue0307/awesome-egocentric-atlas/actions/workflows/validate.yml"><img alt="validate" src="https://github.com/ChaoYue0307/awesome-egocentric-atlas/actions/workflows/validate.yml/badge.svg"></a>
  <a href="https://chaoyue0307.github.io/awesome-egocentric-atlas/"><img alt="project site" src="https://img.shields.io/badge/site-GitHub%20Pages-067882"></a>
  <a href="https://huggingface.co/datasets/cy0307/awesome-egocentric-atlas"><img alt="Hugging Face mirror" src="https://img.shields.io/badge/Hugging%20Face-mirror-ffcc4d"></a>
  <a href="data/resources.yml"><img alt="resources" src="https://img.shields.io/badge/resources-808-0097A7"></a>
  <a href="README.md#dataset-atlas"><img alt="datasets" src="https://img.shields.io/badge/datasets-vision%20%7C%20robotics%20%7C%20memory-344054"></a>
  <a href="README.md#models-tools-and-baselines"><img alt="models and tools" src="https://img.shields.io/badge/models-and%20tools-F5A623"></a>
  <a href="LICENSE"><img alt="license" src="https://img.shields.io/badge/license-MIT-667085"></a>
  <a href="CONTRIBUTING.md"><img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-22A06B"></a>
</p>

**Awesome Egocentric Atlas** is a practical catalog of egocentric (first-person) datasets, benchmarks, models, and tools for egocentric vision, embodied AI and robotics, vision-language-action, world models, long-context memory, AR/VR, and hand-object interaction. Every entry shows its public-access status, so you can tell at a glance what you can download today and what is still just a paper.

**Updated:** 2026-07-30.
**Scope:** the main atlas is **human or animal first-person capture** from head, glasses, headset, body, wrist, handheld, or synchronized ego-exo rigs (where the ego view is central). Related but non-egocentric resources — robot-only datasets, multi-view robotic benchmarks, autonomous-driving 4D data, and general long-video reasoning — are listed separately under [Adjacent and Related Resources](#adjacent-and-related-resources) rather than in the main tables.

<p align="center">
  <img src="assets/awesome-egocentric-atlas-map.png" alt="Awesome Egocentric Atlas catalog overview" width="100%">
</p>

## Contents

- [How to Use This Atlas](#how-to-use-this-atlas)
- [At a Glance](#at-a-glance)
- [Milestones](#milestones)
- [Start Here](#start-here)
- [Landscape Snapshot](#landscape-snapshot)
- [Creator and Release Notes](#creator-and-release-notes)
- [Status Legend](#status-legend)
- [Fast Task Map](#fast-task-map)
- [Recipes and Reference](#recipes-and-reference)
- [Dataset Atlas](#dataset-atlas)
- [Benchmarks and Derived Annotations](#benchmarks-and-derived-annotations)
- [Models, Tools, and Baselines](#models-tools-and-baselines)
- [Adjacent and Related Resources](#adjacent-and-related-resources)
- [Surveys, Papers, and Context](#surveys-papers-and-context)
- [Workshops and Challenges](#workshops-and-challenges)
- [Watchlist](#watchlist)
- [Inclusion Rules](#inclusion-rules)
- [Contributing](#contributing)
- [Cite This Atlas](#cite-this-atlas)

## How to Use This Atlas

Use the first two tables to orient yourself, then jump into the detailed atlas section that matches your task. Each entry is deliberately short: name, release date (year-month, from the first public/arXiv posting where known), venue (conference/journal where published, or `arXiv`/source for preprints), scale/signal, best use, and public status. For filtering by task, modality, status, or date, use the catalog in [`data/resources.yml`](data/resources.yml), where every entry carries a `released` field; label meanings and filter groups are explained in [docs/taxonomy.md](docs/taxonomy.md). Task-oriented [research recipes](#recipes-and-reference) walk you from goal to experiment.

Prefer a browsable view? The [interactive site](https://chaoyue0307.github.io/awesome-egocentric-atlas/) lets you filter the catalog by task, status, and date in eight languages, and the same catalog is mirrored as a dataset on [Hugging Face](https://huggingface.co/datasets/cy0307/awesome-egocentric-atlas).

<p align="center">
  <img src="assets/awesome-egocentric-reader-route.png" alt="Awesome Egocentric Atlas reader route" width="100%">
</p>

## At a Glance

| Signal | What it means for readers |
| :--- | :--- |
| 808 egocentric resources | 208 datasets, 137 benchmarks, 415 models, and 42 toolkits, plus 3 collection hubs — across vision, robotics, memory, and AR. 150 related non-egocentric resources are listed separately. |
| 6 research areas | Foundation video, procedure/action, hands and 3D, memory/reasoning, robotics/VLA, and AR/wearable sensing. |
| 5 access states | `open`, `request`, `benchmark`, `partial`, and `watch` keep availability visible before you plan experiments. |
| Machine-checked catalog | [`data/resources.yml`](data/resources.yml) is the source for type, year, status, URL, tasks, and provenance — and CI keeps the public artifacts in sync. |
| Reader-first tables | Each entry is short enough to scan, then links out to the official page, paper, code, or dataset portal. |

<p align="center">
  <img src="assets/awesome-egocentric-timeline.png" alt="Egocentric resources by era" width="100%">
</p>

## Milestones

Representative works to read first, from early egocentric activity datasets to recent models and large-scale corpora.

<p align="center">
  <img src="assets/awesome-egocentric-milestones.png" alt="Illustrated milestone timeline for representative egocentric AI works" width="100%">
</p>

<!-- MILESTONES:START (generated by build_artifacts.rb — do not edit by hand) -->

<!-- MILESTONES:END -->

## Start Here

| Reader | Best first move | Then go deeper |
| :--- | :--- | :--- |
| New to egocentric vision | Read Ego4D, EPIC-KITCHENS-100, Ego-Exo4D, and EgoSchema first. | Add EgoClip/EgoVLP for video-language, VISOR for masks, and HOT3D/HOI4D for 3D hand-object work. |
| Building a benchmark table | Start from the `open` and `benchmark` entries, then inspect `request` licenses. | Use the YAML catalog to filter by task and modality. |
| Building an assistant or agent | Start with Ego4D, Xperience-10M, EgoLife, TeleEgo, EgoSchema, MyEgo, EgoIntrospect, EgoBench, UCS-Bench, and Ego2Web. | Track Ego-R1, X-LeBench, EgoMemReason, StreamMemBench, ReFocus, EgoCoT-Bench, EgoBlind, EgoSound, and NoRA for reasoning diagnostics. |
| Building a robot/VLA system | Start with Xperience-10M, EgoDex, EgoVerse, Ego-Exo4D, HoloAssist, HOI4D, HOT3D, Assembly101, OpenEgo, UMI, FastUMI-100K, EgoPAT3D, HUG, and WiYH. | Add Dobb-E, FastUMI, MV-UMI, UMIGen, YUBI, Hoi!, EgoVLA, EgoEngine, HumanEgo, EgoGuide, Ego-Pi, EgoAERO, H2O, ARCTIC, HOMIE-toolkit, Xperience task baselines, and EgoHandTrajPred for policy/action supervision. For robot-only corpora see [Adjacent and Related](#adjacent-and-related-resources). |
| Studying hands, objects, and 3D | Start with HOT3D, HOI4D, H2O, ARCTIC, FPHA, EgoHOS, EgoBody, GIMO, EgoHumans, EgoTactile, and UnrealEgo. | Add EgoTracks/TREK-150 for tracking, EgoForce for monocular 3D hand pose, and EgoEMG/EgoEVHands/EgoPressDiff for emerging sensors and contact. |

## Landscape Snapshot

<p align="center">
  <img src="assets/awesome-egocentric-task-matrix.png" alt="Egocentric AI task matrix" width="100%">
</p>

| Area | What to compare | Canonical anchors |
| :--- | :--- | :--- |
| Foundation video | scale, license, modalities, benchmark maturity | Xperience-10M, Ego4D, Ego-Exo4D, EPIC-KITCHENS-100, EgoClip |
| Procedure and action | action granularity, mistakes, anticipation, gaze | EPIC-KITCHENS, Assembly101, MECCANO, EgoProceL, HoloAssist |
| Hand-object and 3D | hands, objects, contact, pose, meshes, scene geometry | HOT3D, HOI4D, H2O, ARCTIC, FPHA, EgoHOS |
| Memory and reasoning | clip length, grounding, QA type, streaming constraints | EgoSchema, EgoLife, TeleEgo, MyEgo, X-LeBench, EgoMemReason, UCS-Bench, StreamMemBench, EgoSound, Ego-R1 |
| Robotics and VLA | action labels, hand trajectories, robot transfer, task diversity | Xperience-10M, EgoDex, EgoVerse, OpenEgo, UMI, FastUMI-100K, YUBI, EgoPAT3D, HUG, WiYH, EgoVLA |
| AR/wearable sensing | gaze, IMU, SLAM, audio, physiological signals | Project Aria, ADT, AEA, Nymeria, PROSE, EgoIntrospect, EasyCom |

> **Origins.** Egocentric vision grew out of wearable computing: [Steve Mann](http://wearcam.org/) pioneered continuous first-person ("sousveillance") cameras through the 1980s–90s and is widely credited with opening up the field, and Microsoft's SenseCam (2006) popularized lifelogging capture. The modern computer-vision wave began at the first IEEE Workshop on Egocentric Vision (CVPR 2009), where Spriggs, De La Torre, and Hebert introduced egocentric activity recognition on the [CMU-MMAC](http://kitchen.cs.cmu.edu/) database (2009) — the earliest dataset in this atlas — followed by the foundational GTEA (2011) and ADL (2012) datasets that launched first-person activity and object research.

## Creator and Release Notes

| Resource | Created / stewarded by | Release channel and access note |
| :--- | :--- | :--- |
| [Xperience-10M](https://huggingface.co/datasets/ropedia-ai/xperience-10m) | Ropedia | Released under `ropedia-ai` on Hugging Face. Full dataset uses controlled non-commercial access; the [sample](https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample) is open, [HOMIE-toolkit](https://github.com/Ropedia/HOMIE-toolkit) loads/visualizes annotations, and [Xperience task baselines](https://huggingface.co/cy0307/ropedia-xperience-10m-task-baselines) provide a public evaluation artifact. |
| [Ego4D](https://ego4d-data.org/) | Meta AI / Facebook AI with an international academic consortium | Official data portal with license-gated downloads and benchmark tasks. |
| [Ego-Exo4D](https://ego-exo4d-data.org/) | Meta and academic partners across the Ego-Exo4D consortium | Official data portal with application/download tooling for synchronized ego-exo data. |
| [EPIC-KITCHENS](https://epic-kitchens.github.io/) | University of Bristol-centered EPIC-KITCHENS team | Official challenge/dataset portal with public annotations and benchmark splits. |
| [Project Aria datasets](https://www.projectaria.com/datasets/) | Meta / Project Aria | Official Project Aria dataset portal and tooling for AR-glasses sensor data. |

## Status Legend

| Status | Meaning |
| :---: | :--- |
| `open` | Public download, public annotations, public code, or application-based access is clearly documented. |
| `request` | Public project exists, but dataset access requires license, form, approval, or institutional agreement. |
| `benchmark` | Mainly a benchmark, challenge, labels, or evaluation over existing videos. |
| `partial` | Some assets are public, but full raw data, license, or long-term availability is unclear. |
| `watch` | Recent or important resource whose release state still needs verification. |

For how each status is decided, see [docs/status_policy.md](docs/status_policy.md).

<p align="center">
  <img src="assets/awesome-egocentric-access-funnel.png" alt="Egocentric resources by access state" width="100%">
</p>

## Fast Task Map

| Research goal | Strong starting points |
| :--- | :--- |
| General egocentric foundation data | [Xperience-10M](https://huggingface.co/datasets/ropedia-ai/xperience-10m), [Ego4D](https://ego4d-data.org/), [Ego-Exo4D](https://ego-exo4d-data.org/), [EPIC-KITCHENS-100](https://epic-kitchens.github.io/), [EgoClip](https://github.com/showlab/EgoVLP) |
| Ego-exo and skill learning | [Ego-Exo4D](https://ego-exo4d-data.org/), [EgoExoLearn](https://github.com/OpenGVLab/EgoExoLearn), [Assembly101](https://assembly-101.github.io/), [Look and Tell](https://arxiv.org/abs/2510.22672) |
| Robot manipulation / VLA | [Xperience-10M](https://huggingface.co/datasets/ropedia-ai/xperience-10m), [EgoDex](https://arxiv.org/abs/2505.11709), [EgoVerse](https://egoverse.ai/), [OpenEgo](https://arxiv.org/abs/2509.05513), [UMI](https://umi-gripper.github.io/), [FastUMI-100K](https://huggingface.co/datasets/IPEC-COMMUNITY/FastUMI_100k_lerobot), [YUBI](https://arxiv.org/abs/2606.10244), [HUG](https://grasping.io/), [EgoVLA](https://rchalyang.github.io/EgoVLA/), [EgoEngine](https://egoengine.github.io/), [HumanEgo](https://humanego-ai.github.io) |
| Long-context QA and memory | [EgoSchema](http://egoschema.github.io/), [EgoLife](https://arxiv.org/abs/2503.03803), [EgoMemReason](https://arxiv.org/abs/2605.09874), [UCS-Bench](https://github.com/cocowy1/UCS-Bench), [StreamMemBench](https://arxiv.org/abs/2606.14571), [Ego-EXTRA](https://fpv-iplab.github.io/Ego-EXTRA/), [EgoStream](https://arxiv.org/abs/2605.31557), [EgoBench](https://arxiv.org/abs/2605.27820) |
| Hand-object and 3D HOI | [HOT3D](https://facebookresearch.github.io/hot3d/), [HOI4D](https://hoi4d.github.io/), [EgoHOS](https://github.com/owenzlz/EgoHOS), [FPHA](https://guiggh.github.io/publications/first-person-hands/), [HUG](https://grasping.io/), [EgoTactile](https://egotactile.github.io/), [EgoForce](https://dfki-av.github.io/EgoForce), [EgoEMG](https://arxiv.org/abs/2605.05712) |
| Audio, speech, and social interaction | [Ego4D AV tasks](https://ego4d-data.org/), [EasyCom](https://arxiv.org/abs/2107.04174), [EgoCom / audio-visual correspondence](http://vision.cs.utexas.edu/projects/ego_av_corr/), [AV-CONV](https://vjwq.github.io/AV-CONV/) |
| AR glasses and scene understanding | [Project Aria Datasets](https://www.projectaria.com/datasets/), [Aria Digital Twin](https://www.projectaria.com/datasets/adt/), [AEA](https://www.projectaria.com/datasets/aea/), [Nymeria](https://www.projectaria.com/datasets/nymeria/), [DTC](https://www.projectaria.com/datasets/dtc/) |

## Recipes and Reference

Task-oriented starting points and the references that keep the catalog usable.

**Research recipes** — each gives a goal, what to start with, what to add, benchmarks, baselines, a minimum viable experiment, common pitfalls, and a reporting checklist:

- [Long-context egocentric video QA](docs/recipes/long-context-egocentric-qa.md)
- [Robot / VLA from egocentric human video](docs/recipes/robot-vla-from-ego-video.md)
- [Hand-object 3D HOI](docs/recipes/hand-object-3d-hoi.md)
- [AR-glasses and wearable sensing](docs/recipes/ar-glasses-sensing.md)
- [Audio and social egocentric understanding](docs/recipes/audio-social-egocentric.md)

**Reference**

- [Taxonomy](docs/taxonomy.md) — task/modality families and how to filter the catalog.
- [Access Matrix](docs/access_matrix.md) — data, code, license, and leaderboard per key resource.
- [Status Policy](docs/status_policy.md) — how `open`/`request`/`benchmark`/`partial`/`watch` are decided.
- [Resource Schema](docs/resource_schema.md) — every field in `data/resources.yml`.
- [Maintenance](docs/maintenance.md) — the add → verify → validate workflow.

## Dataset Atlas

### Foundational and Large-Scale Ego Video

Broad, large-scale first-person corpora that most egocentric pipelines pretrain or benchmark on.

| Resource | Released | Venue | Scale / signal | Best for | Status |
| :--- | :---: | :---: | :--- | :--- | :---: |
| [RetailSMV](https://arxiv.org/abs/2607.00310) | 2026-06 | arXiv | 32,105 captioned synchronized retail clips from five supermarkets with staff-perspective egocentric and exocentric views | Retail world-model adaptation and ego/exo viewpoint comparison | watch |
| [EgoCS-400K](https://arxiv.org/abs/2606.18180) | 2026-06 | arXiv | 400K+ first-person Counter-Strike gameplay videos (10K hours, 13 maps) with aligned actions, player state, camera motion, and game events | Action-conditioned interactive world models from first-person gameplay | watch |
| [HumanNet](https://arxiv.org/abs/2605.06747) | 2026-05 | arXiv | 1M-hour human-centric video corpus spanning first-person and third-person views, with captions, motion descriptions, hand/body signals, and a reported 1K-hour egocentric subset for VLA-style validation | Large-scale human-video pretraining, interaction understanding, and human-to-robot transfer | watch |
| [EgoInteract](https://arxiv.org/abs/2605.18214) | 2026-05 | arXiv | Controllable egocentric-video simulator and synthetic dataset with dense spatial and temporal annotations | Synthetic temporal segmentation, next-active-object detection, anticipation, and EHOI | watch |
| [PRISM](https://dreamvu.ai/prism) | 2026-03 | arXiv | Paper reports 270K multi-view retail SFT samples; the gated PRISM-100K release provides 100K samples, 25,173 ego/exo videos, 21 task types, and about 772 GB | Embodied VLM spatial, physical, and action reasoning in retail settings | request |
| [Ego-1K](https://huggingface.co/datasets/facebook/ego-1k) | 2026-03 | CVPR 2026 | Nearly 1,000 synchronized multiview egocentric videos from a custom 12-camera plus VR-headset rig | Dynamic 3D/4D scene understanding and novel view synthesis from ego rigs | open |
| [EgoCrowds / CrowdEraser](https://arxiv.org/abs/2603.29036) | 2026-03 | arXiv | Semi-synthetic paired crowded/empty clips from real egocentric walking-tour video; CrowdEraser diffusion removes crowds for humanless walkthroughs | First-person walking-tour video editing and environment modeling | watch |
| [Xperience-10M](https://huggingface.co/datasets/ropedia-ai/xperience-10m) | 2026-03 | Hugging Face | Ropedia release on Hugging Face; 10M experiences, 10K hours, six video streams, audio, stereo depth, camera pose, hand/body mocap, IMU, hierarchical language, ~1 PB total | Embodied AI, world models, robot learning from human experience, sensor fusion, 3D/4D understanding | request |
| [Xperience-10M Sample](https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample) | 2026-03 | Hugging Face | Public sample episode for Xperience-10M with six rows on Hugging Face and `cc-by-nc-4.0` terms | Loader testing, demos, task-suite prototyping, annotation inspection | open |
| [Egocentric-100K](https://huggingface.co/datasets/builddotai/Egocentric-100K) | 2025-12 | Hugging Face | 100,405-hour manual-labor egocentric video corpus with 10.8B frames, 2.01M clips, intrinsics, and WebDataset shards | Industrial/manual-labor pretraining, robot learning, and active manipulation density analysis | request |
| [Egocentric-10K](https://huggingface.co/datasets/builddotai/Egocentric-10K) | 2025-11 | Hugging Face | 10,000-hour factory-only egocentric video corpus with 1.08B frames, intrinsics, and WebDataset-style shards | Industrial egocentric pretraining and active-manipulation density analysis | request |
| [Voxel51 Egocentric-10K Subset](https://huggingface.co/datasets/Voxel51/Egocentric_10K_subset) | 2025-11 | Hugging Face | Open FiftyOne package for a Factory 51 subset of Egocentric-10K, with the card reporting 416 1080p head-mounted industrial clips | Lightweight inspection, prototyping, and visualization of Egocentric-10K-style factory footage | open |
| [Look and Tell](https://arxiv.org/abs/2510.22672) | 2025-10 | NeurIPS 2025 Workshop | 25 participants, Project Aria plus stationary cameras, gaze/speech/video, 3D reconstructions | Referential communication across ego and exo viewpoints | watch |
| [EgoBlind](https://arxiv.org/abs/2503.08221) | 2025-03 | NeurIPS 2025 D&B | 1,392 first-person videos from blind and visually impaired users, 5,311 questions posed or verified by blind users | Assistive egocentric VideoQA for blind users | watch |
| [HD-EPIC](https://arxiv.org/abs/2502.04144) | 2025-02 | CVPR 2025 | 41 hours, 9 kitchens, dense fine-grained labels, 3D fixture annotations, audio events, VQA | Detailed kitchen understanding, VQA, 3D-aware ego reasoning, audio-event recognition | open |
| [EgoVid-5M](https://egovid.github.io/) | 2024-11 | NeurIPS 2025 | 5M curated egocentric clips at 1080p with fine-grained kinematic and high-level text action annotations (NeurIPS 2025) | Egocentric video generation and action-conditioned world models | open |
| [Ego-Exo4D](https://ego-exo4d-data.org/) | 2023-11 | CVPR 2024 | 1,286 hours, 740 participants, synchronized first- and third-person views, audio, gaze, IMU, 3D point clouds, language commentary | Skilled activity, ego-exo transfer, cross-view translation, pose, proficiency, robotics | request |
| [HoloAssist](https://holoassist.github.io/) | 2023-09 | ICCV 2023 | 166 hours, 350 instructor-performer pairs, 7 synchronized streams from mixed-reality headsets | Interactive assistance, mistake detection, intervention prediction, procedural collaboration | open |
| [EgoObjects](https://github.com/facebookresearch/EgoObjects) | 2023-09 | ICCV 2023 | Pilot release with 9K+ videos, 250 participants, 50+ countries, 650K annotations, 368 categories | Category and instance-level egocentric object understanding, continual object detection | open |
| [EgoCom / Ego audio-visual correspondence](http://vision.cs.utexas.edu/projects/ego_av_corr/) | 2023-07 | CVPR 2024 | Egocentric video with spatial audio for conversation and audio-visual correspondence tasks | Active speaker detection, spatial audio denoising, conversational graph reasoning | open |
| [Assembly101](https://assembly-101.github.io/) | 2022-03 | CVPR 2022 | 4,321 videos, 8 static plus 4 egocentric views, 100K coarse and 1M fine action segments, 18M 3D hand poses | Procedural action, anticipation, mistake detection, cross-view transfer | open |
| [Ego4D](https://ego4d-data.org/) | 2021-10 | CVPR 2022 | 3,670+ hours from 900+ camera wearers, multiple countries, video/audio/gaze/stereo/3D/narrations depending on subset | Long-form ego video, episodic memory, social, hand-object, forecasting, audio-visual tasks | request |
| [EasyCom](https://arxiv.org/abs/2107.04174) | 2021-07 | arXiv | AR glasses egocentric multi-channel audio and wide-FOV RGB for noisy conversations | Speech enhancement, source localization, conversation assistance | open |
| [EPIC-KITCHENS-100](https://epic-kitchens.github.io/) | 2020-06 | IJCV 2022 | 100 hours, 20M frames, 90K actions, 45 kitchens, narrations and dense action labels | Kitchen action recognition, anticipation, action detection, retrieval | open |
| [From Third Person to First Person](https://arxiv.org/abs/1812.00104) | 2018-12 | CVPR 2019 | Ego/exo video synthesis and retrieval datasets plus baselines for bridging third-person social video to first-person views | Cross-view synthesis, retrieval, and ego-exo transfer | watch |
| [EPIC-KITCHENS](https://epic-kitchens.github.io/) | 2018-04 | ECCV 2018 | 55 hours / 11.5M frames from 32 kitchens with narrations, 39.6K action segments, and object boxes | Original large-scale kitchen action recognition and anticipation benchmark | open |

### Robotics, Manipulation, and VLA

Egocentric human-manipulation and wrist-camera data aimed at vision-language-action models and human-to-robot transfer.

| Resource | Released | Venue | Scale / signal | Best for | Status |
| :--- | :---: | :---: | :--- | :--- | :---: |
| [HiFi-UMI-2K](https://huggingface.co/datasets/simple-world-lab/HiFi-UMI-2K) | 2026-07 | arXiv | 2,000 open hours from a high-fidelity UMI rig with head stereo-inertial SLAM, native inter-gripper pose, microsecond synchronization, and two ultra-wide cameras per hand | Robot-free VLA/WAM pretraining and direct manipulation-policy deployment | open |
| [EgoRecovery](https://arxiv.org/abs/2607.19745) | 2026-07 | arXiv | Egocentric human recovery demonstrations collected at more than 10x robot-teleoperation throughput and aligned with a shared corrective-intent space | Learning when and how robots should recover from manipulation failures | watch |
| [DDD Egocentric Stereo Manipulation Sample](https://huggingface.co/datasets/DDD-Cambodia/ego-centric-sample-dataset) | 2026-07 | Hugging Face | Ten open LeRobot v2 episodes (about 2.37 GB) with stereo first-person video and high-frequency hand/head pose | Stereo human-demonstration loaders, hand tracking, and sensor fusion | open |
| [Showway Egocentric Origami Series](https://huggingface.co/datasets/showway-ego/egocentric-origami-001) | 2026-07 | Hugging Face | Nine open neck-mounted iPhone origami episodes across three LeRobot v3 repositories, with 3D hand joints and reviewed narration | Compact procedural HOI and imitation-learning experiments | open |
| [EGXO Household Egocentric Video Evaluation](https://huggingface.co/datasets/egxodata/egxo-household-egocentric-video-evaluation) | 2026-07 | Hugging Face | 71 household-task videos totaling 10 hours; six previews are public and the complete 43.4 GiB media package is licensed by request | Household procedure and hand-object video evaluation | request |
| [Let the Body Follow](https://arxiv.org/abs/2607.16095) | 2026-07 | arXiv | Coupled egocentric TIAGo teleoperation maps head and arm motion to coordinated torso and mobile-base control, reducing explicit controls and user workload | Whole-body mobile-manipulator teleoperation and HRI | watch |
| [EgoHTR](https://egohtr.github.io/) | 2026-07 | arXiv | 55 scene-aligned 4D human-terrain sequences across seven environments, totaling 1.37 hours and about 150K frames from eight participants, with multiview and mocap ground truth | Scene-aware human-motion reconstruction and humanoid terrain traversal | watch |
| [Open-AoE](https://huggingface.co/datasets/inclusionAI/OpenAoE-2000h) | 2026-07 | Hugging Face | Public nano and tiny tiers provide 2,821 smartphone first-person clips and about 103 hours with video, metric SLAM trajectories, MANO hands, and atomic actions; 2,000 hours remains a roadmap | Large-scale hand-motion, camera-trajectory, and manipulation pretraining | partial |
| [SenseXperience Raw MCAP Sample](https://huggingface.co/datasets/io-intelligence/SenseXperience_WristCam_SampleData) | 2026-07 | Hugging Face | 12 public raw ROS 2 MCAP episodes with four synchronized cameras, head IMU near 120 Hz, calibration, metadata, and recorder diagnostics | Raw multimodal capture-pipeline and sensor-synchronization testing | open |
| [Ego Data by Object](https://huggingface.co/datasets/Kavin60606/ego-data-by-object) | 2026-07 | Hugging Face | 4,110 pick-and-place episodes over 51 object labels with egocentric RGB and HDF5 hand/body transforms, intrinsics, task attributes, and descriptions; source licensing is unclear | Object-conditioned hand tracking and imitation-data experiments | partial |
| [EgoExo-Wreck](https://huggingface.co/datasets/WreckVegas/EgoExo-Wreck) | 2026-07 | Hugging Face | Commercial card reports 150+ synchronized ego-exo hours of object destruction, debris handling, cleanup, and reset; only a gated 1 GB evaluation sample is hosted | Physics-rich HOI, state-change, world-model, and cleanup demonstrations | request |
| [Verbose Industrial Egocentric Sample Series](https://huggingface.co/VerboseTechLabs) | 2026-07 | Hugging Face | Six open industrial sample repositories with 53 first-person clips, 4.86 hours, and about 17.0 GB across textile, metal, electronics assembly, skilled work, and manufacturing operations | Compact industrial action and human-demonstration experiments | open |
| [Verbose Cooking and Chopping Egocentric Video](https://huggingface.co/datasets/VerboseTechLabs/cooking-chopping-egocentric) | 2026-07 | Hugging Face | 11 head- or chest-mounted kitchen clips totaling 101.7 minutes in a public 6.09 GB ZIP, with audio and clip metadata across cooking and chopping | Open kitchen action, procedure, and hand-object video experiments | open |
| [Verbose Household Cleaning Egocentric Video](https://huggingface.co/datasets/VerboseTechLabs/household-cleaning-egocentric) | 2026-07 | Hugging Face | 12 head- or chest-mounted 1080p/30 fps cleaning clips totaling 104.3 minutes in a public 5.74 GB ZIP, with audio and three sub-activity labels | Open domestic-action and assistive-robotics video experiments | open |
| [Flikforge Egocentric Household Tasks](https://huggingface.co/datasets/FlikforgeInc/egocentric-household-tasks) | 2026-07 | Hugging Face | Card claims about 100 rights-cleared household clips with dense customizable annotations, but the repository currently has no media or annotation files and its LICENSE is empty | Monitoring a prospective commercial household-demonstration sample release | watch |
| [AgenticFocus](https://arxiv.org/abs/2607.08857) | 2026-07 | arXiv | Restores occluded object geometry and full-hand motion from ordinary first-person human videos, then retargets and composites robot-aligned observations, actions, and states | Mixed-reality human-to-humanoid demonstration synthesis | watch |
| [Hub Egocentric GoPro RGB+IMU](https://huggingface.co/datasets/Hubdata/egocentric-gopro-rgb-imu) | 2026-07 | Hugging Face | 19 GoPro HERO13 manipulation clips totaling 3.72 hours, with RGB, approximately 200 Hz GPMF IMU, sensor sidecars, and MCAP | High-rate visual-inertial human-demonstration prototyping | partial |
| [Hub Egocentric iPhone RGB+IMU](https://huggingface.co/datasets/Hubdata/egocentric-iphone-rgb-imu) | 2026-07 | Hugging Face | 12 iPhone manipulation clips totaling 2.96 hours, with 1080p RGB, CoreMotion/ARKit IMU and attitude, intrinsics, sidecars, and MCAP | Smartphone RGB-IMU synchronization and sensor-fusion experiments | partial |
| [Hub Egocentric Stereo RGB-D](https://huggingface.co/datasets/Hubdata/egocentric-stereo-rgbd) | 2026-07 | Hugging Face | 9 ZED X Mini clips with stereo RGB, metric depth, IMU, 6DoF VIO, calibration, MCAP, and per-clip LeRobot v3.0 packages | RGB-D/VIO pipelines and multimodal imitation-learning loaders | partial |
| [Hub Egocentric iPhone RGB](https://huggingface.co/datasets/Hubdata/egocentric-iphone-rgb) | 2026-07 | Hugging Face | 40 household-manipulation clips totaling 1.60 hours, delivered as 1080p H.264 RGB without IMU, depth, pose, or robot actions | Lightweight first-person manipulation-video baselines | partial |
| [Datoric Residential Egocentric Video](https://huggingface.co/datasets/Datoric/egocentric-residential-video-100000h) | 2026-07 | Hugging Face | Commercial card claims 100,000 hours of 1080p+ household first-person video from Brazilian homes with task, action, object, HOI, and completion-state annotations; public files are specification/sample metadata | Reviewing large-scale household capture specifications and requesting production data | request |
| [Datoric Industrial Egocentric Video](https://huggingface.co/datasets/Datoric/industrial-egocentric-video-50000h) | 2026-07 | Hugging Face | Commercial card claims 50,000 hours of workplace first-person video across logistics, inspection, assembly, and cleaning; public files are specification/sample metadata | Reviewing industrial capture specifications and requesting production data | request |
| [EgoWAM](https://gatech-rl2.github.io/egowam.github.io/) | 2026-07 | arXiv | Controlled human-robot WAM co-training study comparing pixel, DINO, and 3D-flow targets on three real bimanual tasks, with up to 4x OOD gains reported for DINO | Human-to-robot world-representation transfer | watch |
| [USA Egocentric](https://huggingface.co/datasets/Grably/usa-egocentric) | 2026-07 | Hugging Face | Three iPhone kitchen-manipulation episodes with RGB videos, camera trajectories, hand outputs, action segments, object/contact tracks, and quality reports | Open manipulation-pipeline debugging and VLA annotation prototyping | open |
| [RynnWorld-4D](https://arxiv.org/abs/2607.06559) | 2026-07 | arXiv | 4D embodied world model over future RGB, depth, and optical flow; reports Rynn4DDataset 1.0 with 254.4M+ frames across egocentric human and robotic manipulation videos | Robot manipulation world modeling and action-conditioned 4D prediction | watch |
| [RynnWorld-Teleop](https://arxiv.org/abs/2607.06558) | 2026-07 | arXiv | Digital-teleoperation world model driven by operator hand-pose streams to synthesize egocentric videos and action labels | Scalable bimanual robot data generation from human pose streams | watch |
| [LingBot-VLA 2.0](https://arxiv.org/abs/2607.06403) | 2026-07 | arXiv | VLA update trained with around 60K hours, including 10K hours of egocentric human videos and 50K hours of robot trajectories | Whole-body VLA pretraining and practical robot deployment | watch |
| [LingBot-Video](https://arxiv.org/abs/2607.07675) | 2026-07 | arXiv | MoE DiT video foundation model for embodied intelligence, adding robot-oriented manipulation/navigation and egocentric-perspective footage plus physically grounded rewards | Embodied video pretraining and robot/world-model generation | watch |
| [LIME](https://arxiv.org/abs/2607.02417) | 2026-07 | arXiv | Intent-aware camera-motion generator mined from egocentric video, pairing language intents with relative SE(3) target poses | Active camera control and next-view prediction for embodied agents | watch |
| [H-Tac / TTP](https://arxiv.org/abs/2607.01067) | 2026-07 | arXiv | 160-hour egocentric human tactile-action dataset with 300+ tasks and 135K episodes, plus transferable tactile pretraining | Contact-rich dexterous manipulation from human tactile demonstrations | watch |
| [HomER v2](https://huggingface.co/datasets/toloka/homer-v2) | 2026-06 | Hugging Face | 765 public first-person household videos totaling 99.60 hours from 420 participants across 49 countries and 10 activity categories | Diverse everyday activity, hand-object interaction, video-language, and robot-learning research | open |
| [Ego-Tactile Manipulation](https://huggingface.co/datasets/OpenGraphLabs-Research/ego-tactile-manipulation) | 2026-06 | Hugging Face | 72 public episodes totaling 1.28 hours and 138,629 frames with 1080p ego video, 160-channel dual-hand pressure, head/wrist IMU, and contact-derived action segments | Open tactile-grounded manipulation, contact, and action-segmentation research | open |
| [EgoSteer](https://egosteer.github.io/) | 2026-06 | arXiv | Open full-stack dexterous VLA system using 9.6K hours of curated egocentric human video, with EgoSmith, a robot stack, and two released 3B checkpoints | Steerable dexterous manipulation and human-video-to-robot pretraining | open |
| [Poseidon First-Person Task Video Samples](https://huggingface.co/datasets/psdn-ai/first-person-task-video-samples) | 2026-06 | Hugging Face | Five auto-gated 1080p clips totaling 174 seconds across kitchen, gardening, maintenance, fine-motor, and cleaning tasks | Reviewing task diversity, hand-object visibility, and capture quality | request |
| [WT-UMI](https://arxiv.org/abs/2606.13232) | 2026-06 | arXiv | Wearable whole-body tactile UMI interface aligning human demonstrations and teleoperation through tactile images, contact forces, and end-effector poses | Contact-aware humanoid whole-body manipulation | watch |
| [Human-as-Humanoid](https://zgc-embodyai.github.io/Human-as-Humanoid) | 2026-06 | arXiv | Synchronized ego-exo human videos converted through motion recovery, IK, and FK-aware supervision into 60-DoF humanoid action chunks | Zero-shot humanoid VLA learning from human demonstrations | watch |
| [UMI-Bench 1.0](https://arxiv.org/abs/2606.10382) | 2026-06 | arXiv | Local-first real-robot evaluation protocol dedicated to UMI-style data collection, deployment, reset, logging, and task-factor analysis | Reproducible UMI policy benchmarking | watch |
| [VISTA UMI](https://arxiv.org/abs/2606.04708) | 2026-06 | arXiv | Adapts UMI data for VLA training with wrist-fisheye UMI-VQA visual grounding plus physics-based trajectory validation | Making UMI demonstrations usable for VLAs | watch |
| [Pose6DAug](https://arxiv.org/abs/2606.20118) | 2026-06 | arXiv | Physically plausible multi-view object-swapping augmentation for VLA policies under occlusion and egocentric viewpoints | Robust manipulation data augmentation | watch |
| [MotionWAM](https://arxiv.org/abs/2606.09215) | 2026-06 | arXiv | Real-time humanoid world-action model driven by a single egocentric camera and unified whole-body motion tokens | Humanoid loco-manipulation from egocentric perception | watch |
| [OSCAR](https://arxiv.org/abs/2606.04463) | 2026-06 | arXiv | Omni-embodiment action-conditioned video world model trained across robotics and egocentric human datasets | Robot policy evaluation and cross-embodiment world modeling | watch |
| [Mem-World](https://arxiv.org/abs/2606.18960) | 2026-06 | arXiv | Wrist-view-centered 4D surfel memory for persistent action-conditioned manipulation world models | Long-horizon wrist-camera world modeling | watch |
| [PAIWorld](https://arxiv.org/abs/2606.18375) | 2026-06 | arXiv | 3D-consistent multi-view world foundation model across egocentric, eye-to-hand, and wrist cameras | Multi-view robotic world modeling | watch |
| [Qwen-RobotManip](https://arxiv.org/abs/2606.17846) | 2026-06 | arXiv | 38,100-hour manipulation pretraining corpus converting egocentric hand demonstrations into robot trajectories across 15 platforms | Scalable VLA robot manipulation | watch |
| [CAIP](https://arxiv.org/abs/2606.17256) | 2026-06 | arXiv | Contrastive action-image pretraining from 32,041 hours of egocentric human video with 3D hand-keypoint action proxies | Action-centric visual pretraining for robotics | watch |
| [YUBI](https://arxiv.org/abs/2606.10244) | 2026-06 | arXiv | Reported 8,434 hours, 1.20M episodes, and 119 tasks from a finger-aligned UMI-style bimanual interface | Scalable bimanual dexterous data collection | watch |
| [HumanoidUMI](https://arxiv.org/abs/2606.27239) | 2026-06 | arXiv | VR-assisted egocentric data capture for whole-body humanoid imitation, using sparse human keypoint trajectories and wrist-view observations for whole-body transfer | Whole-body humanoid transfer from egocentric human demonstrations | watch |
| [BRIDGE State-Gated Experts](https://arxiv.org/abs/2606.26603) | 2026-06 | arXiv | Combines handheld UMI demonstrations with targeted teleoperated segments through state-gated diffusion-policy experts | Contact-rich manipulation with mixed UMI and teleoperation supervision | watch |
| [ForceBand](https://forceband-emg.github.io) | 2026-06 | arXiv | 10-hour wrist-worn sEMG, egocentric video, IMU, and fingertip-force dataset for force-enriched demonstrations | Force-aware human demonstration collection for robot policies | watch |
| [EgoEngine](https://egoengine.github.io/) | 2026-06 | arXiv | Converts egocentric human manipulation videos into high-fidelity robot observation videos and executable robot action trajectories | Human-to-robot data generation, dexterous imitation | watch |
| [EgoAERO](https://arxiv.org/abs/2606.08057) | 2026-06 | arXiv | Asset-free conversion from a single egocentric RGB-D demonstration; introduces EgoDex-R in the paper | Single-demo dexterous robot learning | watch |
| [1M-HUGs / HUG](https://grasping.io/) | 2026-06 | arXiv | 1M frames / 27.8 hours of smart-glasses human grasps over 6,707 object instances, plus HUG-Bench with 90 unseen objects | Human grasp modeling and zero-shot robot grasping | open |
| [HALOMI](https://arxiv.org/abs/2606.18772) | 2026-06 | arXiv | Extends UMI-style demonstration collection with egocentric head/wrist observations and head-hand trajectories for humanoid loco-manipulation | Active-perception humanoid manipulation from human demonstrations | watch |
| [HumanoidArena](https://arxiv.org/abs/2606.17833) | 2026-06 | arXiv | Benchmark for egocentric hierarchical whole-body learning across seven leg-critical humanoid-object and humanoid-scene interaction tasks | Whole-body humanoid control from egocentric perception | watch |
| [Luel IMU Egocentric 250k](https://huggingface.co/datasets/Luel-ai/imu-egocentric-250k) | 2026-05 | Hugging Face | Commercial card reports 250K hours and 46,340 tasks; the gated Hub repository exposes a verifiable 10-clip, 30-minute sample plus the full task taxonomy | Reviewing industrial RGB-IMU capture scope and requesting the proprietary full corpus | request |
| [RoboX-EgoTask](https://huggingface.co/datasets/RoboXTechnologies/RoboX-EgoTask) | 2026-05 | Hugging Face | 17 public RGB-D task clips from five recordings with hand signals, camera pose, IMU, action segments, trajectories, segmentation, and quality reports | Open multimodal hand-object interaction and human-demonstration prototyping | open |
| [SenseXperience UMI Human Demonstrations](https://huggingface.co/datasets/ICRA-WBCD/IO-AI-SenseXperience-UMI) | 2026-05 | Hugging Face | 1,051 public human-demonstration episodes, 220,963 frames, and 92 tasks with six synchronized head, wrist, depth, and gripper views plus 7-DoF poses in LeRobot format | Open human-to-robot transfer, bimanual manipulation, and VLA data | open |
| [tau0-WM](https://arxiv.org/abs/2606.01027) | 2026-05 | arXiv | Unified video-action world model trained on real-robot teleoperation, UMI-style interaction, egocentric human video, and rollout/failure data | Future-aware robot action generation and action-conditioned simulation | watch |
| [SABER](https://arxiv.org/abs/2605.09613) | 2026-05 | arXiv | 100+ hours of in-store retail egocentric action capture paired with 360-degree exocentric context | Retail-domain VLA adaptation and manipulation data scaling | watch |
| [Qwen-VLA](https://arxiv.org/abs/2605.30280) | 2026-05 | arXiv | Unified VLA model trained over manipulation trajectories, egocentric human demonstrations, simulation, navigation, and trajectory supervision | General embodied action modeling | watch |
| [Gaze2Act](https://arxiv.org/abs/2605.30282) | 2026-05 | arXiv | Maps first-person gaze into robot perspective for target specification in interactive manipulation | Gaze-conditioned VLA manipulation | watch |
| [DeMiAn](https://arxiv.org/abs/2605.17077) | 2026-05 | arXiv | Dense multi-aspect language re-annotation over 1M robot clips and 50K EgoVerse human-egocentric videos | Language-dense robot policy learning | watch |
| [Grid Egocentric Residential Samples](https://huggingface.co/datasets/aryan56789gridai/grid-egocentric-residential-samples) | 2026-05 | Hugging Face | Public first-person residential manipulation preview pack with full-length 1080p household task videos | Household VLA capture-quality review and imitation-learning samples | open |
| [Industrial Workplace Egocentric FHD Samples](https://huggingface.co/datasets/TrainThemAI/Industrial-Workplace-Egocentric-FHD-Samples) | 2026-05 | Hugging Face | 21 rights-cleared head-mounted workplace clips with paired JSON metadata across factory, construction, services, retail, transit, and food-service domains | Industrial and vocational human-demonstration samples for VLA/WAM prototyping | open |
| [UniDataPro Egocentric Video Preview](https://huggingface.co/datasets/UniDataPro/egocentric-video) | 2026-05 | Hugging Face | Commercial preview card for a claimed 4,050-hour VR-headset/Zed first-person robotics collection; public files expose a sample video, CSV, and tracking text | Market scan and modality reference for large-scale egocentric robotics capture | partial |
| [Lo6yu Egocentric RGB-D + EMG/IMU](https://huggingface.co/datasets/Lo6yu/egocentric_dataset) | 2026-05 | Hugging Face | Eight household activity packages with RGB-D, wrist EMG/IMU, hand keypoints, masks, contact, per-finger force, semantic segments, and training-ready exports | Multimodal contact-aware imitation learning and sensor-fusion robot data | open |
| [Egocentric Adjust Bottle LeRobot](https://huggingface.co/datasets/suz22/egocentric_adjust_bottle) | 2026-05 | Hugging Face | LeRobot-format human_mano adjust-bottle task with 500 episodes and 36,897 frames across image, text, timeseries, and video exports | Loader tests and small-scale LeRobot manipulation policy prototyping | open |
| [Low-Resolution Active Perception BC](https://arxiv.org/abs/2605.14106) | 2026-05 | arXiv | Behavior cloning with low-resolution wrist-mounted egocentric RGB for object finding and grasp triggering | Active perception under low compute | watch |
| [EgoSPT / SPOT](https://arxiv.org/abs/2605.20085) | 2026-05 | arXiv | Egocentric spatially prompted manipulation trajectories with first-frame object/target grounding and 3D end-effector motion | Spatially grounded manipulation trajectory prediction | watch |
| [Mobile UMI](https://arxiv.org/abs/2605.20894) | 2026-05 | arXiv | Robot-free mobile manipulation capture with chest-centric context, wrist-centric interaction, decoupled kinematics, and latency-aware diffusion policy | Mobile manipulation from portable demonstrations | watch |
| [BifrostUMI](https://arxiv.org/abs/2605.03452) | 2026-05 | arXiv | VR-device robot-free demonstrations with sparse keypoint trajectories, wrist-mounted visual data, and humanoid retargeting | Humanoid whole-body demonstration collection | watch |
| [UniT](https://arxiv.org/abs/2604.19734) | 2026-04 | arXiv | Unified latent action tokenizer anchoring massive egocentric human data to humanoid policy learning and world modeling | Human-to-humanoid transfer | watch |
| [XRZero-G0](https://github.com/X-Square-Robot/XRZero-G0) | 2026-04 | arXiv | VR and dual-gripper robot-free collection system with a reported 2,000-hour dataset and data-mixing study | Scalable robot-free manipulation data collection | watch |
| [EgoVerse](https://egoverse.ai/) | 2026-04 | arXiv | 1,362 hours, 80K episodes, 1,965 tasks, 240 scenes, 2,087 demonstrators | Human demonstration scaling for robot learning and VLA | watch |
| [RoboX Egocentric Collection](https://huggingface.co/datasets/RoboXTechnologies/RoboX-Egocentric-Collection-v0.2) | 2026-04 | Hugging Face | 7,342 auto-gated first-person clips across grasping, daily activities, scene capture, and navigation with metadata, hand keypoints, object tracks, action segments, IMU, and camera pose | Multi-task robotics imitation data and navigation/manipulation benchmark prototyping | request |
| [EgoLive](https://arxiv.org/abs/2604.23570) | 2026-04 | arXiv | Large-scale real-world task-oriented egocentric routines for robot manipulation | Home service, retail, and real-world work-task manipulation | watch |
| [GazeVLA](https://gazevla.github.io/) | 2026-04 | arXiv | VLA policy that pretrains on large-scale egocentric human data to capture gaze, intention, and action before robot fine-tuning | Gaze- and intent-aware robot manipulation | watch |
| [WARPED](https://arxiv.org/abs/2604.10809) | 2026-04 | arXiv | Wrist-aligned rendering converts monocular egocentric human demonstrations into robot policy observations with 3D Gaussian Splatting | Cross-embodiment imitation from human ego video | watch |
| [UMI-3D](https://umi-3d.github.io/) | 2026-04 | arXiv | Extends UMI with wrist LiDAR, LiDAR-centric SLAM, synchronized sensing, and spatiotemporal calibration for robust 3D demonstration capture | 3D-aware UMI data collection | watch |
| [OmniUMI](https://arxiv.org/abs/2604.10647) | 2026-04 | arXiv | Adds RGB, depth, trajectory, tactile sensing, grasp force, and external wrench signals to a human-aligned UMI-style handheld system | Contact-rich multimodal UMI demonstrations | watch |
| [HRDexDB](https://arxiv.org/abs/2604.14944) | 2026-04 | arXiv | 1.4K human/robot grasping trials, tactile, multiview video, egocentric video streams | Cross-domain dexterous grasp learning | watch |
| [UMI-Underwater](https://umi-under-water.github.io/) | 2026-03 | arXiv | Transfers on-land handheld human demonstrations to underwater grasping through depth-based affordance representations | Underwater manipulation without underwater teleoperation | watch |
| [HoMMI](https://hommi-robot.github.io/) | 2026-03 | arXiv | Whole-body mobile manipulation interface augmenting UMI with egocentric sensing, relaxed head actions, and cross-embodiment hand-eye policy design | Robot-free mobile manipulation demonstrations | watch |
| [Ego-Exo Manufacturing](https://huggingface.co/datasets/third-origin/ego-exo-manufacturing) | 2026-03 | Hugging Face | Gated 275-hour shoe-manufacturing corpus with 40 synchronized ego-exo groups, 80 standalone ego sessions, 137 exo sessions, and procedure/proficiency/mistake annotations | Industrial ego-exo learning, skill assessment, and procedural modeling | request |
| [OBayData Egocentric Dexterous Manipulation Demo](https://huggingface.co/datasets/obaydata/egocentric-dexterous-manipulation-demo) | 2026-03 | Hugging Face | 500 train and 100 test first-person manipulation sessions with head and wrist videos, 3D hand joints, camera extrinsics, action labels, and language annotations | Quality review and prototyping for dexterous human-demonstration pipelines | open |
| [HuMI](https://humanoid-manipulation-interface.github.io/) | 2026-02 | arXiv | Portable robot-free whole-body demonstration interface with open code and seven Hugging Face datasets across kneeling, squatting, tossing, walking, and bimanual tasks | Humanoid whole-body manipulation from portable human demonstrations | open |
| [Seesaw Video Subset](https://huggingface.co/datasets/SeesawVideos/Video_Subset) | 2026-02 | Hugging Face | 763 gated LeRobot-compatible indoor episodes, including 243 ego and 520 exo views, 321,178 frames, four room settings, and smartphone AR camera pose | Ego-exo robot learning, action recognition, and data-conversion experiments | request |
| [CoMe-VLA](https://arxiv.org/abs/2602.04600) | 2026-02 | arXiv | Cognitive and memory-aware VLA that learns active-perception strategies from large-scale egocentric human data | Non-Markovian active perception and manipulation | watch |
| [EgoAVFlow](https://arxiv.org/abs/2602.22461) | 2026-02 | arXiv | Learns manipulation and active camera control from egocentric human videos through shared 3D flow | Active-vision robot policy transfer | watch |
| [EgoHumanoid](https://arxiv.org/abs/2602.10106) | 2026-02 | arXiv | Co-trains humanoid VLA policies from robot-free egocentric human demonstrations and limited robot data | Humanoid loco-manipulation | watch |
| [EgoActor](https://arxiv.org/abs/2602.04515) | 2026-02 | arXiv | Grounds high-level instructions into spatially aware egocentric humanoid actions | Humanoid task planning and action grounding | watch |
| [AoE: Always-on Egocentric](https://arxiv.org/abs/2602.23893) | 2026-02 | arXiv | Always-on egocentric human-video collection pipeline and corpus for embodied AI | Scaling human-video data for robot learning | watch |
| [EgoScale](https://arxiv.org/abs/2602.16710) | 2026-02 | arXiv | 20,854 hours of action-labeled egocentric human video with a human-to-robot two-stage transfer recipe and a log-linear data-scaling law | Scaling dexterous manipulation from human video | watch |
| [Manus Egocentric Sample](https://huggingface.co/datasets/OpenGraphLabs-Research/manus-egocentric-sample) | 2026-01 | Hugging Face | 20 LeRobot-format manipulation episodes with egocentric RGB/depth, Manus glove tracking, IMU, timeseries, and videos | Open egocentric manipulation loader tests and sensor-fusion policy prototyping | open |
| [HoyerChou Egocentric Bimanual Videos](https://huggingface.co/datasets/HoyerChou/EgocentricVideos) | 2026-01 | Hugging Face | YOTO/YOTO++ release with three raw first-person bimanual videos, 119 segmented demos, 241 rows, MANO hand meshes, 3D keypoints, calibration, and camera/world transforms | One-shot bimanual manipulation and hand-trajectory extraction from human video | open |
| [Egocentric Specialties](https://huggingface.co/datasets/ThisIsPepper/EgocentricSpecialties) | 2026-01 | Hugging Face | Auto-gated skilled-jewelry manufacturing data card describing synchronized egocentric and top-down footage for diamond setting and specialty workflows | Skilled industrial manipulation and fine-grained manufacturing demonstrations | request |
| [X-Humanoid](https://arxiv.org/abs/2512.04537) | 2025-12 | arXiv | Applies human-to-humanoid video translation to 60 hours of Ego-Exo4D, releasing 3.6M robotized humanoid frames | Humanoid video/world-model data generation | watch |
| [DreamTacVLA](https://arxiv.org/abs/2512.23864) | 2025-12 | arXiv | Grounds VLA policies in contact physics using tactile images, wrist-camera local vision, and third-person macro vision | Contact-rich VLA manipulation | watch |
| [TacThru-UMI](https://arxiv.org/abs/2512.09851) | 2025-12 | arXiv | See-through-skin tactile-visual sensing plus a UMI-style imitation-learning framework for multimodal manipulation | Tactile-visual robot policy learning | watch |
| [Mitty](https://arxiv.org/abs/2512.17253) | 2025-12 | arXiv | Diffusion Transformer for translating human demonstrations into robot-execution videos, with synthesis from large egocentric datasets | Human-to-robot video generation | watch |
| [World in Your Hands / WiYH](https://arxiv.org/abs/2512.24310) | 2025-12 | arXiv | Reported 1,000-hour egocentric manipulation ecosystem with multiview/depth/hand/wrist signals | VLA, manipulation representation learning | watch |
| [Hoi!](https://arxiv.org/abs/2512.04884) | 2025-12 | arXiv | 3,048 force-grounded articulated-manipulation sequences over human, wrist-camera, UMI, and Hoi-gripper embodiments | Force/contact-grounded cross-view manipulation | watch |
| [METIS](https://arxiv.org/abs/2511.17366) | 2025-11 | arXiv | Dexterous VLA pretrained on multi-source egocentric human and robotic data unified under one action space | Dexterous egocentric-VLA pretraining | watch |
| [Let Me Show You / RfV](https://arxiv.org/abs/2511.05199) | 2025-11 | IROS 2025 | Retrieves egocentric human demonstrations and extracts affordance masks plus hand trajectories for robot policies | Retrieval-from-video robot manipulation | watch |
| [UMIGen](https://arxiv.org/abs/2511.09302) | 2025-11 | arXiv | Cloud-UMI plus visibility-aware egocentric point-cloud generation | 3D-aware cross-embodiment imitation learning | watch |
| [EgoMI](https://arxiv.org/abs/2511.00153) | 2025-10 | arXiv | Egocentric manipulation interface capturing synchronized end-effector and active-head trajectories for semi-humanoid robots | Active-vision whole-body manipulation | watch |
| [FARM](https://tactile-farm.github.io) | 2025-10 | arXiv | Force-aware diffusion policy using a modified tactile UMI gripper and matched actuated deployment gripper | Force- and tactile-grounded manipulation | watch |
| [UMI-on-Air](https://arxiv.org/abs/2510.02614) | 2025-10 | arXiv | Embodiment-aware diffusion policy adapting handheld UMI demonstrations to aerial manipulators | UMI transfer under embodiment dynamics | watch |
| [EmbodiSwap](https://arxiv.org/abs/2510.03706) | 2025-10 | arXiv | Photorealistic robot overlays over ego-centric human video for synthetic robot imitation datasets | Zero-shot human-video-to-robot imitation | watch |
| [Hand-VLA Pretraining](https://arxiv.org/abs/2510.21571) | 2025-10 | arXiv | Converts unscripted real-life egocentric hand videos into 1M VLA-aligned action-language episodes | Robot pretraining from human activity video | watch |
| [ActiveUMI](https://arxiv.org/abs/2510.01607) | 2025-10 | arXiv | Portable VR/UMI-style system capturing active egocentric perception for bimanual manipulation | Active-perception UMI-style data collection | watch |
| [FastUMI-100K](https://huggingface.co/datasets/IPEC-COMMUNITY/FastUMI_100k_lerobot) | 2025-10 | arXiv | 100K+ UMI-style trajectories across 54 tasks in LeRobot format with multi-view wrist fisheye images | Large-scale UMI-style robot policy training | open |
| [BiNoMaP](https://hnuzhy.github.io/projects/BiNoMaP/) | 2025-09 | arXiv | Category-level bimanual non-prehensile primitives learned from egocentric hand trajectories and transferred across two dual-arm platforms | Contact-rich bimanual skill extraction from human demonstrations | watch |
| [EMMA](https://arxiv.org/abs/2509.04443) | 2025-09 | IEEE RA-L 2025 | Co-trains egocentric human mobile-manipulation data with static robot data to avoid mobile teleoperation bottlenecks | Scalable mobile manipulation from human data | watch |
| [OpenEgo](https://arxiv.org/abs/2509.05513) | 2025-09 | arXiv | 1,107 hours unified across six public egocentric datasets, 290 manipulation tasks, hand-pose/action primitives | Standardized dexterous manipulation pretraining and evaluation | watch |
| [MV-UMI](https://arxiv.org/abs/2509.18757) | 2025-09 | arXiv | Multi-view UMI adds third-person context to wrist egocentric observations | Broad-scene context for cross-embodiment manipulation | watch |
| [InterVLA](https://arxiv.org/abs/2508.04681) | 2025-08 | ICCV 2025 | 11.4 hours and 1.2M frames with 2 ego and 5 exo views, human/object motions, and verbal commands | Vision-language-action and motion estimation | watch |
| [EgoVLA](https://rchalyang.github.io/EgoVLA/) | 2025-07 | arXiv | VLA training from egocentric human videos plus robot fine-tuning | Human-video-to-robot policy transfer | watch |
| [EgoDex](https://arxiv.org/abs/2505.11709) | 2025-05 | ICLR 2026 | 829 hours of Apple Vision Pro egocentric video, 194 tabletop tasks, 3D hand/finger tracking | Dexterous manipulation, imitation learning, human-to-robot hand trajectory prediction | watch |
| [TASTE-Rob](https://arxiv.org/abs/2503.11423) | 2025-03 | CVPR 2025 | 100,856 task-oriented ego-centric hand-object interaction videos aligned with language instructions | Video generation and robot imitation learning | watch |
| [Kaiwu](https://arxiv.org/abs/2503.05231) | 2025-03 | IEEE RA-L 2025 | 11,664 synchronized assembling-action instances with first-person video, gaze, hand motion, pressure, audio, EMG, mocap, and robot streams | Multimodal robot learning and HRI | watch |
| [Humanoid-VLA](https://arxiv.org/abs/2502.14795) | 2025-02 | arXiv | Combines language, egocentric scene perception, and motion control for universal humanoid control | Humanoid VLA and motion generation | watch |
| [Immersive Social Interaction with VR and LLM-Assisted Humanoids](https://arxiv.org/abs/2607.07430) | 2024-11 | Humanoids 2024 Workshop | Apple Vision Pro teleoperation with egocentric robot feedback, voice locomotion, wrist/finger retargeting, and RGB, gaze, command, joint-state, and hand-motion recording on a Unitree H1 | Immersive humanoid teleoperation and multimodal demonstration capture | watch |
| [EgoMimic](https://arxiv.org/abs/2410.24221) | 2024-10 | ICRA 2025 | Project Aria human videos with 3D hand tracking and robot co-training for unified imitation learning | Human-to-robot imitation from ego video | watch |
| [FastUMI](https://arxiv.org/abs/2409.19499) | 2024-09 | arXiv | UMI redesign reporting 10K+ real-world trajectories across 22 everyday tasks | Faster hardware-independent UMI-style collection | watch |
| [R+X](https://arxiv.org/abs/2407.12957) | 2024-07 | ICRA 2025 | Retrieves executable skills from long unlabeled first-person videos of everyday human tasks | Robot imitation from everyday first-person video | watch |
| [UMI on Legs](https://umi-on-legs.github.io) | 2024-07 | arXiv | Combines handheld UMI task demonstrations with simulation-trained whole-body controllers for quadruped manipulation | Mobile cross-embodiment UMI transfer | watch |
| [EgoPAT3D / EgoPAT3Dv2](https://arxiv.org/abs/2403.05046) | 2024-03 | ICRA 2024 | 1M+ RGB-D/IMU frames in the original task; v2 expands egocentric 3D action-target prediction | Human-robot interaction, 3D target anticipation, manipulation safety | open |
| [Universal Manipulation Interface / UMI](https://umi-gripper.github.io/) | 2024-02 | RSS 2024 | Hand-held GoPro gripper interface and policy stack for in-the-wild robot teaching | Wrist-view robot-free demonstrations and cross-embodiment policy transfer | open |
| [Dobb-E / HoNY](https://dobb-e.com/) | 2023-11 | arXiv | 13 hours, 22 homes, 5,620 trajectories, and 1.5M RGB-D frames collected with an iPhone-based Stick | Household robot learning from handheld in-home demonstrations | partial |
| [VIP](https://arxiv.org/abs/2210.00030) | 2022-09 | ICLR 2023 | Value-Implicit Pre-Training learns visual rewards and representations from Ego4D human video for few-shot robot manipulation | Ego4D-to-robot reward learning | open |
| [R3M](https://arxiv.org/abs/2203.12601) | 2022-03 | CoRL 2022 | Robot-manipulation visual representation pretrained on Ego4D with time-contrastive and video-language objectives | Ego4D-to-robot representation learning | open |

### Hands, Objects, Pose, Tracking, and 3D

Fine-grained hand, object, contact, and 3D-pose datasets, including emerging event-camera and EMG sensing.

| Resource | Released | Venue | Scale / signal | Best for | Status |
| :--- | :---: | :---: | :--- | :--- | :---: |
| [ReViV](https://reviv4d.github.io/) | 2026-07 | ECCV 2026 | Open unified feed-forward reconstruction of camera trajectory, gaze, body, hands, depth, and view dynamics from one monocular egocentric RGB stream | Holistic and efficient viewer-plus-scene 4D reconstruction | open |
| [Egocentric Hand Benchmark Annotations](https://huggingface.co/datasets/macrodata/egocentric-hand-benchmark) | 2026-07 | Hugging Face | 100,427 public annotation rows combining 95,002 EgoDaily hand boxes and 5,425 HOT3D virtual hand-crop camera records; source RGB is not redistributed | Hand detection, crop-camera geometry, and derived benchmark evaluation | partial |
| [EgoExoMoCap](https://arxiv.org/abs/2607.15868) | 2026-07 | ECCV 2026 | Distributed mocap from two or more smart-glasses wearers, fusing head/wrist tracking with context-aware image features on two in-the-wild datasets | Lightweight ego-exo body-motion reconstruction | watch |
| [Exo2EgoPose](https://arxiv.org/abs/2607.15890) | 2026-07 | ACM MM 2026 | Vision-language-guided egocentric 3D hand-pose forecasting using reconstructed exocentric demonstrations, evaluated on AssemblyHands, Ego-Exo4D, EgoMe-pose, and CALVIN | Hand forecasting and human-to-robot transfer | watch |
| [EgoObjects-Camera](https://huggingface.co/datasets/KangLiao/EgoObjects-Camera) | 2026-07 | Hugging Face | Public camera-parameter annotations for 241,554 EgoObjects images across 49 shards, including roll, pitch, vertical field of view, and radial distortion; reuse terms are undeclared | Camera-aware egocentric modeling and dataset analysis | partial |
| [TSR-Ego](https://arxiv.org/abs/2607.09169) | 2026-07 | arXiv | Causal temporal stereo refinement with fisheye deformable cross-attention for online egocentric 3D body pose on UnrealEgo2 and UnrealEgo-RW | Head-mounted stereo pose recovery under occlusion and truncation | watch |
| [CI-HOI / DEHOI](https://arxiv.org/abs/2607.08514) | 2026-07 | arXiv | Cue-isolated HOI evaluation and inpainted testbed that separate hand and object evidence to expose contextual shortcuts in egocentric VLMs | Diagnosing hand- versus object-centric action understanding | watch |
| [Whareformer](https://jacobchalk.github.io/Whareformer/) | 2026-07 | ECCV 2026 | First learned OSNOM tracker, trained on 56 videos and tested on 260 long EPIC-KITCHENS-100, IT3DEgo, and HD-EPIC videos; MIT code, weights, features, and training data are live | Long-term 3D object tracking through occlusion and out-of-view periods | open |
| [HandsOnWorld](https://arxiv.org/abs/2607.02075) | 2026-07 | arXiv | Camera-disentangled hand-controlled egocentric video generation with EgoVid-Pro: 103K clips and roughly 12M frames of protagonist-only hand trajectories | Unconstrained egocentric HOI video generation | watch |
| [SAGE Action-Gaze](https://arxiv.org/abs/2607.04017) | 2026-07 | arXiv | Unified action-gaze recognition and anticipation framework linking HOI, gaze, egocentric close-up views, and exocentric context | Joint gaze/action anticipation for human behavior understanding | watch |
| [Ego3DLM / Ego-Human Motion Prediction](https://arxiv.org/abs/2607.07001) | 2026-07 | ECCV 2026 | 3D-aware LLM that jointly predicts past/future human pose and narration from egocentric video, three-point tracking, and scene features on Nymeria | Scene-grounded egocentric human-motion forecasting | watch |
| [Humanola Egocentric Hand-Pose Sample](https://huggingface.co/datasets/humanola-inc/egocentric-sample) | 2026-07 | Hugging Face | LeRobot v2.1 sample with 9 episodes, 48,272 frames, four synchronized cameras, 200 Hz IMU, 3D hands, poses, overlays, and Rerun logs | Open hand-pose and sensor-fusion loader tests for manipulation pipelines | open |
| [InterPet4D](https://huggingface.co/datasets/ohicarip/interpet4d) | 2026-06 | Hugging Face | 6.8M-frame human-dog capture; public 10.7 GB v1 provides 227 headset clips with audio and aligned SMPL, MANO, pet skeleton, SMAL, and MERT features | Multimodal 4D human-pet interaction, motion generation, and pose analysis | open |
| [ViDiHand](https://vidihand.github.io) | 2026-06 | arXiv | 4D two-hand motion reconstruction from full-frame egocentric video using video-diffusion representations; evaluated on ARCTIC, HOT3D, and HOI4D | Egocentric hand-motion reconstruction without detector/test-time optimization | watch |
| [HT-Bench / HandTouch](https://arxiv.org/abs/2606.19161) | 2026-06 | arXiv | 10M RGB frames and 7.8M tactile frames across 226 dexterous full-hand tasks | Vision-tactile representation learning for dexterous manipulation | watch |
| [EPIC-Contact / HOPformer](https://sid2697.github.io/epic-contact/) | 2026-06 | ECCV 2026 | 2.3K EPIC-KITCHENS clips and 62.3K frames with dense 3D hand-object contact, posed meshes, code, dataset, and checkpoints | In-the-wild egocentric 3D hand-object pose and contact estimation | open |
| [GhostHandEgoNet](https://doi.org/10.1142/s0218001426550116) | 2026-06 | IJPRAI 2026 | Lightweight egocentric hand-pose and hygiene-monitoring pipeline with 2.56M parameters for embedded deployment | Egocentric hand pose under occlusion and clinical hand-hygiene monitoring | watch |
| [Hand-4DGS](https://jeongminb.github.io/hand-4dgs/) | 2026-06 | arXiv | Feed-forward 4D hand reconstruction from egocentric video with 3D Gaussian Splatting, evaluated on H2O and ARCTIC | Fast egocentric 4D hand reconstruction | watch |
| [A multimodal RGB/events FPV hand dataset](https://arxiv.org/abs/2606.10790) | 2026-06 | arXiv | Synthetic event-based first-person hand detection from EgoHands plus v2e | Event/RGB hand detection benchmarking | watch |
| [SIGNIQ Egocentric Hand-Pose Sample](https://huggingface.co/datasets/jackji/signiq-egocentric-handpose-sample) | 2026-06 | Hugging Face | Five short head-mounted GoPro manipulation clips with Label Studio import metadata for hand-pose and action-segment annotation | Hand-pose annotation and manipulation-labeling workflow tests | open |
| [Leveraging Synthetic Data for Egocentric HOI Detection](https://doi.org/10.1007/s11263-026-02838-8) | 2026-05 | IJCV 2026 | Synthetic-data augmentation study for hand-object interaction detection on VISOR, EgoHOS, and ENIGMA-51 | HOI detection when real labels are scarce | watch |
| [Causal-Inspired Fourier Egocentric Action Recognition](https://doi.org/10.1109/tcsvt.2026.3653125) | 2026-05 | IEEE TCSVT 2026 | Causal-inspired Fourier representation learning for wearable IMUs and egocentric action recognition | Wearable-sensor action recognition | watch |
| [EgoSMPLX](https://github.com/naso06/EgoSMPLX) | 2026-05 | arXiv | Prior-guided whole-body human mesh recovery from monocular head-mounted egocentric images, with released code and annotations | Egocentric whole-body mesh recovery | watch |
| [DexGloveHOI](https://arxiv.org/abs/2605.21714) | 2026-05 | arXiv | 100K+ synchronized egocentric vision and on-glove IMU samples with marker-based mocap 3D hand-pose ground truth across dexterous daily manipulation | Vision-IMU fusion for 3D hand tracking | watch |
| [EggHand](https://jyoun9.github.io/EggHand/) | 2026-05 | CVPR 2026 Findings | Multimodal foundation model for egocentric hand-pose forecasting over EgoExo4D-style video-language and action signals | Hand-pose forecasting and VLA action decoding | watch |
| [Map-Mono-Ego](https://arxiv.org/abs/2605.20889) | 2026-05 | ICIP 2026 | Map-grounded global human-pose estimation from monocular egocentric video, with AIST-Living paired ego video and scanned environments | Scene-aware egocentric body-pose localization | watch |
| [EgoForce Motion](https://arxiv.org/abs/2605.13041) | 2026-05 | arXiv | Online full-body motion reconstruction from sparse egocentric observations using diffusion forcing | Real-time egocentric body-motion reconstruction | watch |
| [EgoEMG](https://arxiv.org/abs/2605.05712) | 2026-05 | arXiv | 41 participants, bilateral EMG, IMU, RGB, external RGB-D, mocap hand labels | EMG plus egocentric vision hand pose estimation | watch |
| [EgoTouch / TouchAnything](https://jianyi2004.github.io/TouchAnything-Website/) | 2026-05 | arXiv | 302 tasks, 4,530 episodes with egocentric + dual wrist cameras, bimanual 3D hand pose, and dense tactile pressure maps | Tactile estimation and contact modeling from egocentric video | watch |
| [EgoEVHands](https://github.com/ZJUWang01/EgoEV-HandPose) | 2026-05 | arXiv | Stereo event-camera egocentric hand dataset with 5,419 sequences and 3D/2D keypoints | Event-based bimanual hand pose and gesture recognition | watch |
| [TouchMoment](https://arxiv.org/abs/2604.12343) | 2026-04 | CVPR 2026 Findings | 4,021 egocentric videos, 8,456 annotated hand-object contact moments | Precise contact moment detection | watch |
| [TAIHRI](https://github.com/Tencent/TAIHRI) | 2026-04 | arXiv | Task-aware VLM for localizing task-relevant 3D human keypoints in close-range egocentric HRI | Metric-scale human keypoints for robot interaction | watch |
| [MASS](https://arxiv.org/abs/2604.08943) | 2026-04 | arXiv | Deformable surfel splatting for high-fidelity 3D hand reconstruction and rendering from egocentric monocular video | Egocentric hand reconstruction and rendering | watch |
| [E-3DPSM](https://arxiv.org/abs/2604.08543) | 2026-04 | arXiv | Event-driven continuous pose state machine for real-time egocentric 3D human-pose estimation from head-mounted devices | Event-based egocentric body-pose estimation | watch |
| [EgoFun3D](https://arxiv.org/abs/2604.11038) | 2026-04 | arXiv | 271 egocentric videos with 3D geometry, part segmentation, articulation and function-template annotations | Interactive 3D object modeling from ego video | watch |
| [FunRec](https://arxiv.org/abs/2604.05621) | 2026-04 | CVPR 2026 | Functional 3D digital-twin reconstruction from in-the-wild egocentric RGB-D interaction videos with articulated parts and kinematics | Interactive scene reconstruction for simulation and robot learning | watch |
| [DP-DeGauss](https://arxiv.org/abs/2604.07986) | 2026-04 | ICASSP 2026 | Dynamic probabilistic Gaussian decomposition for egocentric 4D scene reconstruction, separating background, hands, and objects | First-person 4D interaction reconstruction | watch |
| [Towards Egocentric 3D Hand Pose Estimation in Unseen Domains](https://doi.org/10.1109/wacv61042.2026.00560) | 2026-03 | WACV 2026 | Egocentric 3D hand-pose estimation study focused on unseen-domain generalization | Robust first-person hand tracking outside training domains | watch |
| [Controllable Egocentric Video Generation](https://arxiv.org/abs/2603.11755) | 2026-03 | ECCV 2026 | Occlusion-aware sparse 3D hand-joint control for realistic egocentric hand-object video generation, with a 1M-clip annotation pipeline | Controllable egocentric HOI video generation and world models | watch |
| [SHOW3D](https://huggingface.co/datasets/facebook/show3d-dataset) | 2026-03 | CVPR 2026 | Open 20-hour, 2,137-scene release from 38 participants with eight exo and two Quest 3 ego views, 3D hand/object annotations, shape, and text | In-the-wild 3D hand-object reconstruction | open |
| [EgoXtreme](https://arxiv.org/abs/2603.25135) | 2026-03 | CVPR 2026 | Smart-glasses egocentric 6D object-pose dataset across industrial, sports, and rescue scenes with extreme motion blur, dynamic lighting, and occlusion | Robust 6D object pose under extreme egocentric conditions | watch |
| [AG-EgoPose](https://arxiv.org/abs/2603.25175) | 2026-03 | arXiv | Attention-guided egocentric 3D human-pose estimation from fisheye camera input with dual motion/spatial streams | Fisheye egocentric 3D pose estimation | watch |
| [FEEL](https://huggingface.co/datasets/FeelAuthors/FEEL-Benchmark) | 2026-03 | arXiv | Open 26-trial, 700-episode benchmark with 39,497 Aria frames and synchronized gaze, hand, IMU, and Paxini grasp-force totals; the paper reports a larger full collection | Contact-rich physical action and hand-object understanding | open |
| [Person Identification from Egocentric HOI](https://doi.org/10.1007/s42486-025-00215-x) | 2026-02 | CCF TPCI 2026 | Uses 3D hand pose from egocentric human-object interactions as a person-identification signal | Identity and behavior analysis from first-person hand-object motion | watch |
| [WHOLE](https://arxiv.org/abs/2602.22209) | 2026-02 | arXiv | Joint world-grounded hand-object motion reconstruction from egocentric video using a generative HOI prior | Holistic hand-object pose recovery | watch |
| [AirGlove](https://arxiv.org/abs/2602.05159) | 2026-02 | ICASSP 2026 | Egocentric 3D hand-tracking evaluation for gloved hands and sensing-glove appearance shifts | Gloved-hand tracking for teleoperation | watch |
| [Eva-3M / EvaPose](https://arxiv.org/abs/2602.23618) | 2026-02 | CVPR 2026 | 3.0M+ egocentric HPE frames, including 435K keypoint-visibility labels, plus visibility-aware pose estimation | Visibility-aware egocentric human pose | watch |
| [WristPP](https://zhenqis123.github.io/WristPP/) | 2026-02 | CHI 2026 submission | Wrist-worn wide-FOV RGB system with a 133K-frame pose-pressure dataset from 20 subjects | Mobile hand pose and pressure interaction | watch |
| [Egocentric Affordance Dataset](https://huggingface.co/datasets/Kavin60606/egocentric-affordance-dataset) | 2026-02 | Hugging Face | 48,400 egocentric frames across household, workshop, factory, gardening, and healthcare scenes with Qwen3-VL affordance labels | Affordance and HOI supervision for embodied VLMs and robot learning | open |
| [Industrial Egocentric HOI Detection](https://doi.org/10.1007/978-3-032-11317-7_38) | 2026-01 | ICIAP 2025 Workshops | Real-time egocentric hand-object interaction detection for industrial workflows | Industrial first-person HOI monitoring | watch |
| [EgoGrasp](https://arxiv.org/abs/2601.01050) | 2026-01 | arXiv | World-space open-vocabulary hand-object interaction reconstruction from dynamic egoview videos | HOI reconstruction in world coordinates | watch |
| [GlovEgo-HOI](https://doi.org/10.5220/0014466400004084) | 2026 | VISAPP 2026 | Synthetic-to-real egocentric HOI detection for gloved industrial hand-object scenarios | Industrial HOI detection under gloves and domain shift | watch |
| [OpenTouch](https://opentouch-tactile.github.io/) | 2025-12 | arXiv | 5.1 hours of synchronized egocentric video-touch-pose data, 2,900 curated clips, text annotations, and retrieval/classification benchmarks | Full-hand tactile grounding for real-world interaction | watch |
| [ROHIT](https://arxiv.org/abs/2512.07394) | 2025-12 | arXiv | Reconstructs objects along hand-interaction timelines from HOT3D and EPIC-KITCHENS stable-grasp clips | Object pose propagation through hand contact | watch |
| [EvHand-FPV](https://arxiv.org/abs/2509.13883) | 2025-09 | arXiv | Event-based first-person 3D hand-tracking dataset and lightweight wrist-ROI tracking framework | Low-power FPV hand tracking | watch |
| [THOR](https://arxiv.org/abs/2507.06442) | 2025-07 | arXiv | Thermal-guided adaptive RGB sampling for wearable hand-object monitoring, using about 3% of RGB frames while preserving activity segments | Low-power longitudinal hand-object activity recognition | watch |
| [Egocentric HOI Detection](https://arxiv.org/abs/2506.14189) | 2025-06 | Expert Systems with Applications | New benchmark and method for detecting hand-object interactions in egocentric video | Egocentric hand-object interaction detection | open |
| [EgoBrain](https://huggingface.co/datasets/ut-vision/EgoBrain) | 2025-06 | ICLR 2026 | Complete gated 1.6 TB release from 40 participants with synchronized 4K egocentric video, EEG, IMU, interval markers, and surveys | Brain-signal plus first-person action understanding | request |
| [EventEgoHands](https://arxiv.org/abs/2505.19169) | 2025-05 | ICIP 2025 | Event-based egocentric 3D hand mesh reconstruction benchmark over N-HOT3D | Low-light and motion-blur hand reconstruction | watch |
| [EgoEvGesture](https://arxiv.org/abs/2503.12419) | 2025-03 | arXiv | First large-scale egocentric event-camera gesture-recognition dataset with a head-motion-robust 7M-param model (62.7% unseen-subject accuracy) | Event-camera egocentric gesture recognition | watch |
| [EgoCast](https://arxiv.org/abs/2412.02903) | 2024-12 | WACV 2025 | 3D pose forecasting from egocentric video and proprioceptive data on Ego-Exo4D / Aria Digital Twin | Future body-pose forecasting | watch |
| [Ego3DT](https://arxiv.org/abs/2410.08530) | 2024-10 | ACM MM 2024 | Zero-shot 3D reconstruction and tracking of all objects in ego-centric videos | 3D object tracking in first person | watch |
| [EgoPressure](https://yiming-zhao.github.io/EgoPressure/) | 2024-09 | CVPR 2025 | 5.0 hours, 21 participants, a moving egocentric camera plus 7 stationary RGB-D cameras, hand pose meshes, and fine-grained per-contact touch pressure (CVPR 2025) | Hand pressure and pose from egocentric vision | open |
| [AFF-ttention / STAformer](https://arxiv.org/abs/2406.01194) | 2024-06 | ECCV 2024 | Affordance- and attention-aware short-term object-interaction anticipation from egocentric video | Short-term active-object anticipation | watch |
| [HOT3D](https://facebookresearch.github.io/hot3d/) | 2024-06 | CVPR 2025 | 833+ minutes, 3.7M+ images, Aria and Quest 3, gaze, point clouds, 3D hand/object/camera poses | 3D hand-object tracking for AR/VR manipulation | open |
| [EMAG](https://arxiv.org/abs/2405.20030) | 2024-05 | ECCV 2024 HANDS Workshop | Ego-motion-aware 2D hand forecasting for egocentric videos | Hand trajectory anticipation | watch |
| [UnrealEgo2 / UnrealEgo-RW](https://arxiv.org/abs/2401.00889) | 2024-01 | CVPR 2024 | Expanded stereo egocentric pose datasets from synthetic and real-world capture | Stereo egocentric human pose estimation | watch |
| [POV-Surgery](https://batfacewayne.github.io/POV_Surgery_io/) | 2023-07 | MICCAI 2023 | Egocentric surgical video for hand and tool pose estimation during operating-room activities | Surgical hand-tool pose and interaction understanding | open |
| [EgoHumans](https://arxiv.org/abs/2305.16487) | 2023-05 | ICCV 2023 | 125K+ egocentric images for in-the-wild multi-human tracking, 2D/3D pose, and mesh recovery | Egocentric multi-human perception and tracking | partial |
| [AssemblyHands](https://arxiv.org/abs/2304.12301) | 2023-04 | CVPR 2023 | 3.0M 3D hand-pose annotations from Assembly101, including 490K egocentric images | Egocentric 3D hand pose and pose-aware action recognition | benchmark |
| [EgoTracks](https://arxiv.org/abs/2301.03213) | 2023-01 | NeurIPS 2023 | Long-term egocentric visual object tracking annotations from Ego4D | Tracking, re-detection, embodied object persistence | open |
| [EgoGTA / EgoPW-Scene](https://arxiv.org/abs/2212.11684) | 2022-12 | CVPR 2023 | Synthetic EgoGTA plus EgoPW-based in-the-wild scene-aware pose data | Scene-aware egocentric 3D human pose estimation | partial |
| [EgoHOS](https://github.com/owenzlz/EgoHOS) | 2022-08 | ECCV 2022 | 11,243 egocentric images with detailed hand/object/contact segmentation | Hand-object segmentation and contact-aware foreground modeling | open |
| [UnrealEgo](https://4dqv.mpi-inf.mpg.de/UnrealEgo/) | 2022-08 | ECCV 2022 | Synthetic stereo eyeglass egocentric dataset with 3D human pose | Robust egocentric 3D human motion capture | open |
| [Ego2HandsPose](https://arxiv.org/abs/2206.04927) | 2022-06 | WACV 2024 | Extension of Ego2Hands with 3D global hand pose annotations | Two-hand RGB 3D pose in global coordinates | open |
| [ARCTIC](https://arctic.is.tue.mpg.de/) | 2022-04 | CVPR 2023 | 2.1M frames with bimanual hand/object meshes, articulated objects, and contact | Dexterous bimanual manipulation, contact, reconstruction | request |
| [GIMO](https://github.com/y-zheng18/GIMO) | 2022-04 | ECCV 2022 | Ego-centric views, gaze, scene scans, and high-quality body pose sequences | Gaze-informed human motion prediction in scene context | open |
| [HOI4D](https://hoi4d.github.io/) | 2022-03 | CVPR 2022 | 2.4M RGB-D egocentric frames, 4,000+ sequences, 800 objects, 16 categories, 610 rooms | 4D human-object interaction, segmentation, object pose tracking, action segmentation | open |
| [EgoBody](https://sanweiliti.github.io/egobody/egobody.html) | 2021-12 | ECCV 2022 | HoloLens2 egocentric RGB/depth/eye/head/hand data with 3D body pose and shape | Egocentric human pose, shape, motion, social interaction | open |
| [TREK-150](https://machinelearning.uniud.it/datasets/trek150/) | 2021-08 | project page | 150 egocentric tracking sequences derived from EPIC-KITCHENS | Single-object tracking in egocentric video | open |
| [H2O: Two Hands and Objects](https://arxiv.org/abs/2104.11181) | 2021-04 | ICCV 2021 | Synchronized multi-view RGB-D, two-hand 3D pose, 6D object pose, object meshes, camera poses | First-person two-hand interaction recognition and pose-aware HOI | open |
| [Ego2Hands](https://arxiv.org/abs/2011.07252) | 2020-11 | arXiv | Large-scale composited RGB egocentric two-hand segmentation/detection | Robust unconstrained hand segmentation | open |
| [xR-EgoPose](https://github.com/facebookresearch/xR-EgoPose) | 2019-07 | GitHub | Synthetic egocentric body pose data for XR headset viewpoints | 3D human pose from head-mounted cameras | open |
| [You2Me](https://arxiv.org/abs/1904.09882) | 2019-04 | CVPR 2020 | Infers second-person body pose in egocentric video from first- and second-person interaction cues | Social interaction and body-pose inference | watch |
| [H+O](https://arxiv.org/abs/1904.05349) | 2019-04 | CVPR 2019 Oral | Unified egocentric RGB model for 3D hand pose, object pose, interactions, objects, and actions | 3D hand-object pose and interaction recognition | watch |
| [EgoReID Dataset](https://arxiv.org/abs/1812.09570) | 2018-12 | arXiv | 900 identities, about 10.2K tracks, 176K detections from mobile first-person cameras with sensor metadata | Person re-identification from first-person video | watch |
| [EgoYouTubeHands / HandOverFace](https://arxiv.org/abs/1803.03317) | 2018-03 | CVPR 2018 | In-the-wild egocentric hand-segmentation study built around EgoYouTubeHands, HandOverFace, EGTEA, and EgoHands-style supervision | Hand detection and segmentation beyond lab capture | watch |
| [FPHA / First-Person Hand Action](https://guiggh.github.io/publications/first-person-hands/) | 2017-04 | CVPR 2018 | 100K+ RGB-D frames, 45 action classes, 26 objects, 3D hand/object poses | 3D hand pose and first-person hand action recognition | open |
| [EgoGesture](https://ieeexplore.ieee.org/document/8299578/) | 2017-01 | IEEE TMM 2018 | 24K+ gesture samples, 3M RGB-D frames, 50 subjects, 83 static and dynamic gestures across six scenes | First-person gesture recognition for wearable interaction | open |
| [Left/Right Hand Segmentation](https://arxiv.org/abs/1607.06264) | 2016-07 | CVIU 2016 | Classic first-person method that separates left/right hands and handles hand-to-hand occlusion with temporal superpixels | Hand segmentation and wearable interaction | watch |
| [EgoHands](http://vision.soic.indiana.edu/projects/egohands/) | 2015-12 | ICCV 2015 | 48 Google Glass videos, 4,800 annotated hand images | Hand detection and segmentation | open |
| [BEOID](https://dimadamen.github.io/BEOID/) | 2014-09 | BMVC 2014 | Gaze-tracked egocentric video of 8 users interacting with objects across 6 everyday locations (kitchen, workspace, printer, corridor, gym) | Discovering task-relevant objects and interaction modes | open |

### Daily Life, Memory, Assistance, and QA

Long-horizon daily-life capture and the question-answering benchmarks that probe memory, reasoning, and assistance.

| Resource | Released | Venue | Scale / signal | Best for | Status |
| :--- | :---: | :---: | :--- | :--- | :---: |
| [Sidewalk Moments](https://arxiv.org/abs/2607.20903) | 2026-07 | arXiv | 61 first-person city walks segmented into more than 50K ten-second clips with video, averaged-image, audio, and text representations | Human-aligned urban engagement and multimodal temporal-compression studies | watch |
| [Vinci2 / EgoServe](https://sitonggong.github.io/EgoServe-page/) | 2026-07 | ECCV 2026 | 3,000+ proactive-service instances across 11 categories and four memory horizons, with public annotations and the training-free EgoMemo agent | Deciding when an egocentric assistant should intervene and grounding its response in memory | open |
| [VEGAS](https://arxiv.org/abs/2607.08489) | 2026-07 | arXiv | Training-free gaze-aware caption metric plus egocentric activities and instructional slides paired with synchronized gaze and reference captions | Human-attention-aligned caption evaluation and retrieval | watch |
| [CoMind](https://comind.ethz.ch/) | 2026-07 | ECCV 2026 | Dual-view collaborative-cooking dataset with two synchronized head-mounted cameras, two exo views, audio, gaze, 3D scene/object scans, and social/interaction annotations; download is marked coming soon | Social reasoning, joint attention, handover prediction, and collaborative assistance | watch |
| [Imprint](https://arxiv.org/abs/2607.00696) | 2026-07 | arXiv | Online interaction-centric memory compression for seven-day egocentric QA on EgoLifeQA | Scalable long-horizon memory retrieval | watch |
| [EgoGapBench](https://github.com/jhCOR/EgoGapBench) | 2026-07 | arXiv | Diagnostic benchmark for whether models select actions from the camera-wearer's perspective in multi-agent scenes | Egocentric perspective and action-selection evaluation | open |
| [EgoSafetyBench](https://arxiv.org/abs/2607.00218) | 2026-06 | arXiv | 1,200 egocentric robot-view safety scenarios with half-second labels and misleading in-scene text controls | Streaming VLM safety-guard evaluation | watch |
| [BinaryTracking / GangnamLoop](https://github.com/ndb796/BinaryTracking) | 2026-06 | arXiv | Spatial QA and navigation benchmark for long egocentric robot routes, with GangnamLoop route data and the BinTrack implementation | Open spatial memory and navigation QA | open |
| [Egocentric Pedestrian Crossing Intention](https://arxiv.org/abs/2606.09142) | 2026-06 | arXiv | VLM-based VQA formulation for predicting pedestrian crossing intention from short egocentric traffic-safety clips | Wearable traffic-safety intent reasoning | watch |
| [Face-vs-Body HRI Tracking](https://arxiv.org/abs/2606.03694) | 2026-06 | arXiv | Custom-annotated egocentric HRI dataset from a social robot, comparing face and body tracking under occlusion and engagement changes | Social-robot engagement tracking | watch |
| [VL-MemKnG / WalkieKnowledgeT+](https://arxiv.org/abs/2606.17183) | 2026-06 | arXiv | Hybrid spatio-temporal knowledge graph plus segment memory for QA over long egocentric navigation trajectories | Navigation memory, long-horizon evidence retrieval, spatial QA | watch |
| [V-RAGBench / CARVE](https://arxiv.org/abs/2606.13141) | 2026-06 | arXiv | Query, evidence-chunk, answer triplets for decoupled retrieval/generation evaluation in long egocentric video RAG | Retrieval-augmented long-video QA | watch |
| [OVO-S-Bench](https://arxiv.org/abs/2606.03890) | 2026-06 | arXiv | 1,680 spatial-reasoning questions over 348 continuous egocentric videos with query timestamps and evidence intervals | Streaming spatial intelligence, tracking, simulation, and allocentric mapping | watch |
| [Astra](https://arxiv.org/abs/2606.06476) | 2026-06 | arXiv | Agentic VLM spatial reasoning with a view-consistent world simulator that supplies imagined novel-view evidence from limited egocentric observations | World-model-augmented spatial reasoning | watch |
| [VLESA](https://github.com/HanjiangHu/VLESA) | 2026-06 | arXiv | Goal-conditioned safety annotations over egocentric human-activity video for safety-aware assistance | Safety monitoring and situated activity assistance | open |
| [Causal-Plan-1M](https://arxiv.org/abs/2606.01810) | 2026-06 | arXiv | Reported million-scale corpus of explicit causal reasoning traces over egocentric videos | Causal and planning-oriented ego reasoning | watch |
| [NoRA](https://arxiv.org/abs/2606.04806) | 2026-06 | arXiv | 1,420 first-person video clips for normative action reasoning with fact-reason-action support graphs | Grounded reasonableness and safety-oriented action generation | watch |
| [Pause and Think](https://arxiv.org/abs/2606.00616) | 2026-06 | arXiv | Reasoning-centric training data and benchmark for video-grounded assistive action suggestions | Scene-grounded assistance, planning, and temporal consistency | watch |
| [SuperMemory-VQA](https://arxiv.org/abs/2606.00825) | 2026-06 | arXiv | 52.9 hours of AI-glasses activity with RGB, audio, gaze, IMU, SLAM, and 4,853 human-verified QA pairs across object/location/intent/scene memory | Long-horizon memory for AR assistants | watch |
| [EgoMonth](https://huggingface.co/datasets/anonymous-egomonth/egomonth-dataset) | 2026-05 | Hugging Face | 1,443 long-horizon memory QA records with event/object/place annotations and eight public sample videos; the full 20-120-day corpus uses external research access | Month-scale episodic memory, spatial reasoning, and personal QA | partial |
| [VISTA Daily Assistance](https://arxiv.org/abs/2605.10579) | 2026-05 | arXiv | Generative egocentric-video framework for reactive and proactive daily-assistance scenarios | Synthetic training/evaluation for assistants | watch |
| [EgoMemReason](https://huggingface.co/datasets/Ted412/EgoMemReason) | 2026-05 | COLM 2026 | 500 public questions over week-long EgoLife video with entity, event, and behavior memory, open evaluation code, and a leaderboard | Memory-driven reasoning across sparse evidence over hours or days | open |
| [EgoBench](https://arxiv.org/abs/2605.27820) | 2026-05 | arXiv | 1,045 egocentric-video-grounded interactive tasks with tools and simulated users | Tool-using multimodal agents with dynamic interaction | watch |
| [EyeCue](https://github.com/langzhang2000/EyeCue) | 2026-05 | arXiv | Gaze-empowered egocentric video model plus CogDrive annotations for driver cognitive-distraction detection | Gaze-context reasoning for safety and internal-state inference | watch |
| [Minerva-Ego](https://github.com/google-deepmind/neptune) | 2026-05 | arXiv | Complex egocentric visual-reasoning benchmark with multi-step multimodal questions, dense reasoning traces, and spatiotemporal object masks | Grounded multi-step egocentric reasoning | open |
| [EgoPro-Bench](https://arxiv.org/abs/2605.07299) | 2026-05 | arXiv | Personalized proactive-interaction benchmark with 2,400 evaluation videos, 12K+ training videos, and 12 domains | Streaming intent prediction and proactive assistance timing | watch |
| [Pro2Assist](https://arxiv.org/abs/2605.04227) | 2026-05 | arXiv | Continuous step-aware proactive assistance with multimodal egocentric perception and an AR-glasses testbed | Real-time step-aware assistance | watch |
| [Personal Visual Context Learning / Personal-VCL-Bench](https://vision.cs.utexas.edu/projects/PersonalVCL/) | 2026-05 | arXiv | Smart-glasses benchmark for using wearer-specific visual context at prompt time over continuous first-person streams | Personalized visual memory for wearable assistants | watch |
| [AwareLLM](https://arxiv.org/abs/2605.09625) | 2026-05 | arXiv | Proactive assistant using egocentric vision, pupillometry, gaze, posture, heart activity, and LLM reasoning | Personalized productivity and cognitive-state-aware assistance | watch |
| [GazeMind / CogLoad-Bench](https://arxiv.org/abs/2605.05790) | 2026-05 | arXiv | Gaze-guided LLM agent and cognitive-load benchmark for smart glasses, reporting 152 participants, 40+ hours, and 10K+ annotations | Cognitive-load-aware assistance | watch |
| [Dietary Behavior Change Receptivity](https://arxiv.org/abs/2605.27950) | 2026-05 | arXiv | Pilot AIM-2 wearable-camera study using egocentric eating images to infer receptivity for just-in-time dietary interventions | Nutrition and health-oriented lifelogging | watch |
| [EgoBabyVLM](https://arxiv.org/abs/2605.19130) | 2026-05 | arXiv | Benchmarking cross-modal learning from naturalistic infant and adult egocentric video, including Machine-DevBench and challenge tracks | Developmental egocentric VLM learning | watch |
| [EgoIntrospect](https://ego-introspect.github.io/) | 2026-05 | arXiv | 180 hours from 60 subjects with synchronized video, audio, gaze, motion, physiological signals | Internal-state reasoning, affect, intent, cognitive memory for wearable assistants | watch |
| [EgoExoMem](https://arxiv.org/abs/2605.18734) | 2026-05 | arXiv | 2.6K MCQs across synchronized ego-exo videos | Cross-view memory reasoning | watch |
| [EgoCoT-Bench](https://dstardust.github.io/EgoCoT/) | 2026-05 | arXiv | 3,172 verifiable QA pairs over 351 videos with operation-centric rationale annotations | Grounded chain-of-thought and evidence consistency | open |
| [EgoStream](https://arxiv.org/abs/2605.31557) | 2026-05 | arXiv | 2,250 questions across seven memory dimensions with Answer Validity Windows, expanded to 8,528 recall-conditioned evaluations over streams up to 45.3 hours | Diagnosing streaming episodic memory | watch |
| [ChildLens](https://www.eva.mpg.de/comparative-cultural-psychology/technical-development/childlens/) | 2026-04 | Behavior Research Methods 2026 | 109 hours of vest-mounted first-person video/audio from 62 children aged 3-5 at home, with five location and 14 activity classes | Naturalistic child activity, temporal localization, and voice analysis | request |
| [MyEgo](https://github.com/Ryougetsu3606/MyEgo) | 2026-04 | CVPR 2026 | 541 long videos and 5K personalized questions about the camera wearer, belongings, activities, and past | Personalized ego-grounding and long-range memory QA | open |
| [EgoEsportsQA](https://arxiv.org/abs/2604.12320) | 2026-04 | arXiv | 1,745 QA pairs from professional first-person shooter matches across three games | High-speed first-person perception and tactical reasoning in virtual environments | watch |
| [EgoEverything](https://arxiv.org/abs/2604.08342) | 2026-04 | arXiv | 5,000+ MCQ pairs over 100+ hours, with gaze-attention-inspired question generation for AR | Human-behavior-inspired long-context egocentric understanding | watch |
| [LifeDialBench / EgoMem](https://arxiv.org/abs/2604.11182) | 2026-04 | arXiv | Real egocentric video plus synthetic lifelog conversations | Online temporal-causality evaluation for continuous lifelog memory systems | watch |
| [EgoScreen-Emotion / ESE](https://arxiv.org/abs/2604.15823) | 2026-04 | arXiv | 224 egocentric screen-view movie trailers with 28,667 confidence-aware emotion keyframe annotations | Emotion understanding from realistic first-person viewing | watch |
| [Gaze-to-Guidance Assistants](https://arxiv.org/abs/2604.08062) | 2026-04 | arXiv | Gaze-grounded multimodal LLM assistance study using egocentric video and gaze overlays to infer reading difficulty | Cognitive-need-aware wearable assistance | watch |
| [EgoTL](https://arxiv.org/abs/2604.09535) | 2026-04 | arXiv | Think-aloud (say-before-act) egocentric capture with word-level spoken reasoning and metric-scale spatial annotations over 100+ household tasks | Long-horizon reasoning for VLMs and world models | watch |
| [EgoSelf](https://abie-e.github.io/egoself_project/) | 2026-04 | arXiv | Personalized egocentric assistant framework with graph memory | Personalization from long-term egocentric interaction memory | watch |
| [MA-EgoQA](https://ma-egoqa.github.io/) | 2026-03 | arXiv | 1.7K questions over multiple long-horizon egocentric streams | Multi-agent egocentric memory reasoning | open |
| [Ego2Web](https://arxiv.org/abs/2603.22529) | 2026-03 | CVPR 2026 | Egocentric videos paired with web tasks requiring physical-scene understanding and online execution | Web agents grounded in first-person physical context | watch |
| [Egocentric Co-Pilot](https://arxiv.org/abs/2603.01104) | 2026-03 | WWW 2026 | Web-native smart-glasses agent framework with temporal reasoning, context compression, speech/gaze intent, and streaming WebRTC/WebSocket pipelines | Assistive always-on egocentric web agents | watch |
| [LifeEval](https://arxiv.org/abs/2603.00490) | 2026-03 | arXiv | 4,075 QA pairs over continuous first-person streams for real-time task-oriented human-AI collaboration in daily life | Daily-life multimodal assistance evaluation | watch |
| [Gesture-Based Egocentric Video QA](https://arxiv.org/abs/2603.12533) | 2026-03 | CVPR 2026 | Egocentric video QA grounded in the camera wearer's pointing and deictic gestures | Gesture-grounded referential QA | watch |
| [EgoIntent](https://arxiv.org/abs/2603.12147) | 2026-03 | arXiv | 3,014 steps over 15 daily-life scenarios for local intent (What), global intent (Why), and next-step plan (Next) | Step-level intent and anticipatory assistance | watch |
| [SAW-Bench](https://huggingface.co/datasets/ucsbai/SAW-Bench) | 2026-02 | ICML 2026 | Open 3.30 GB benchmark with 786 Ray-Ban Meta smart-glasses videos and 2,071 QA pairs across six situated-awareness tasks | First-person situated spatial reasoning | open |
| [EgoGraph](https://arxiv.org/abs/2602.23709) | 2026-02 | arXiv | Dynamic temporal knowledge graph framework evaluated on EgoLifeQA and EgoR1-bench | Training-free ultra-long egocentric video memory | watch |
| [EgoSound](https://arxiv.org/abs/2602.14122) | 2026-02 | CVPR 2026 | 7,315 validated QA pairs across 900 Ego4D/EgoBlind videos | Sound perception, spatial localization, causal audio-visual reasoning | watch |
| [SuperGlasses](https://arxiv.org/abs/2602.22683) | 2026-02 | CVPR 2026 Findings | Evaluates VLMs as intelligent agents for AI smart glasses across realistic wearable assistant tasks | Smart-glasses agent evaluation | watch |
| [Gazeify Then Voiceify](https://arxiv.org/abs/2601.19281) | 2026-01 | IUI 2026 | Displayless smart-glasses object referencing via gaze selection, mask generation, voice descriptions, and conversational correction | Gaze-plus-voice physical object grounding | watch |
| [Wearable Product Localization](https://arxiv.org/abs/2601.12486) | 2026-01 | arXiv | Wearable assistive shopping system combining detection, VLM guidance, spatialized sonification, and corrective feedback | Product search and navigation for blind or low-vision users | watch |
| [Egocentric Clinical Intent](https://arxiv.org/abs/2601.06750) | 2026-01 | arXiv | Benchmark for egocentric clinical intent understanding by medical multimodal LLMs over first-person clinical procedure video | Clinical intent reasoning for medical assistants | watch |
| [WearVox](https://arxiv.org/abs/2601.02391) | 2026-01 | arXiv | Egocentric multich