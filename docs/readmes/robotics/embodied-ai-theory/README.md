<!-- source: https://github.com/xiang-ao-data/embodied-ai-theory.git sha: dcf5e134679deacab3be8dac20804f5174de09fa readme: main/README.md -->
# xiang-ao-data/embodied-ai-theory

具身智能理论精讲 | Transformer · Flow Matching · World Models · SLAM · VLA · MANO — 从零读懂 τ₀-WM、HaWoR、DreamDojo 等前沿论文

---

<div align="center">

# 🤖 具身智能理论精讲

### Embodied AI · World Models · Robot Learning

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Topics](https://img.shields.io/badge/Topics-7_Modules-blue)
![Files](https://img.shields.io/badge/Notes-12_Files-green)
![Lines](https://img.shields.io/badge/Content-5800+_Lines-orange)
![Papers](https://img.shields.io/badge/Papers-30+-red)

<br>

> **从零掌握具身智能所需的全部理论**
> 覆盖 Transformer · 扩散模型 · Flow Matching · 世界模型 · SLAM · VLA

<br>

```
τ₀-WM · HaWoR · DreamDojo · Genie Envisioner · HaMeR · WHAM · UniHOPE
          ↑ 读懂这些论文所需的所有理论，全在这里 ↑
```

</div>

---

## 📖 为什么要有这个项目

2024–2025 年，具身智能领域论文爆炸式增长。但大多数教程要么停留在 Hello World，要么直接丢给你一篇满是公式的论文。

这个项目做一件事：**把论文里每一个公式背后的来龙去脉讲清楚**。

- ✅ 每个概念先给直觉，再给严格推导
- ✅ 每个公式逐项解释，不跳步骤
- ✅ 每章末尾对应到具体论文的具体位置
- ✅ 公式用 LaTeX 书写，配合 [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) 完整渲染

---

## 🗺️ 知识地图

```
┌─────────────────────────────────────────────────────────────────┐
│                        目标论文层                                 │
│   τ₀-WM  HaWoR  DreamDojo  Genie Envisioner  HaMeR  UniHOPE    │
└──────┬──────┬──────┬──────┬──────┬──────┬──────┬───────────────┘
       │      │      │      │      │      │      │
       ▼      ▼      ▼      ▼      ▼      ▼      ▼
┌──────────────────────────────────────────────────────────────────┐
│                        应用层                                      │
│  [07] VLA架构演化        [07] 模仿学习基础        [05] MANO模型    │
└──────────────────────┬───────────────┬──────────────────────────┘
                       │               │
                       ▼               ▼
┌──────────────────────────────────────────────────────────────────┐
│                        核心技术层                                  │
│  [04] 世界模型理论    [04] 潜在动作    [03] 视频生成与DiT          │
│  [06] SLAM与相机估计                                               │
└──────────────────────┬───────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────────┐
│                        生成模型层                                  │
│      [02] VAE & 信息瓶颈    [02] 扩散模型    [02] Flow Matching   │
└──────────────────────┬────────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────────┐
│                        基础层（必读）                              │
│           [01] 注意力机制            [01] ViT & DiT               │
└──────────────────────────────────────────────────────────────────┘
```

---

## 📚 学习路径与模块索引

### 推荐顺序（8–12 周）

| # | 模块 | 文件 | 核心内容 | 建议时间 |
|---|------|------|---------|---------|
| 1 | **Transformer 基础** | [注意力机制](01_Transformer/01_attention_mechanism.md) | QKV推导、多头注意力、RoPE位置编码 | 1周 |
| 2 | **Transformer 架构** | [ViT & DiT](01_Transformer/02_vit_dit.md) | Patch Embedding、AdaLN-Zero、Wan2.2架构 | 1周 |
| 3 | **变分自编码器** | [VAE](02_生成模型/01_VAE.md) | ELBO完整推导、重参数化、信息瓶颈 | 1周 |
| 4 | **扩散模型** | [Diffusion Models](02_生成模型/02_diffusion_models.md) | DDPM/DDIM/CFG完整推导 | 1.5周 |
| 5 | **Flow Matching** ⭐ | [Flow Matching](02_生成模型/03_flow_matching.md) | CFM、Rectified Flow、与DDPM对比 | 1.5周 |
| 6 | **视频生成** | [视频DiT](03_视频生成与DiT/01_latent_diffusion_video.md) | 视频VAE、时序压缩、跨视角注意力 | 1周 |
| 7 | **世界模型理论** | [世界模型](04_世界模型/01_world_model_theory.md) | RSSM、DreamerV3、互动世界模型 | 1周 |
| 8 | **潜在动作模型** ⭐ | [潜在动作](04_世界模型/02_latent_action_models.md) | IDM、LAPA、DreamDojo信息瓶颈 | 1周 |
| 9 | **手部参数化模型** | [MANO](05_手部与人体模型/01_MANO.md) | LBS公式、6D旋转、PA-MPJPE | 0.5周 |
| 10 | **视觉SLAM** | [SLAM基础](06_SLAM与相机/01_visual_slam_basics.md) | 对极几何、BA、DROID-SLAM、尺度歧义 | 1周 |
| 11 | **模仿学习** | [Imitation Learning](07_机器人学习基础/01_imitation_learning.md) | BC、Diffusion Policy、Action Chunking | 0.5周 |
| 12 | **VLA架构** | [VLA](07_机器人学习基础/02_VLA_architecture.md) | RT-2→π₀→ViLLA演化、多视角融合 | 0.5周 |

> ⭐ = 当前领域最核心，优先掌握

---

## 🔍 按论文查找所需知识

| 目标论文 | 必读章节 |
|---------|---------|
| **τ₀-WM**（统一视频动作世界模型）| Flow Matching → 视频DiT → 潜在动作 → VLA架构 |
| **HaWoR**（世界坐标系手部运动）| MANO → SLAM基础 → 视频DiT |
| **DreamDojo**（NVIDIA，人类视频世界模型）| VAE → 潜在动作 → 视频DiT → 世界模型 |
| **Genie Envisioner**（智元世界模型平台）| Flow Matching → 视频DiT → 世界模型 |
| **HaMeR / HandOS**（手部重建）| ViT & DiT → MANO → 注意力机制 |
| **WHAM / Dyn-HaMR**（全局轨迹重建）| SLAM基础 → MANO → Flow Matching |

---

## 📐 公式渲染说明

本项目所有数学公式使用 LaTeX 书写。在 VSCode 中需安装插件方可正常渲染：

```
扩展名：Markdown Preview Enhanced
ID：shd101wyy.markdown-preview-enhanced
```

安装后，右键任意 `.md` 文件 → **Markdown Preview Enhanced: Open Preview**

示例公式（安装插件后可见渲染效果）：

$$\mathcal{L}_{\text{CFM}} = \mathbb{E}_{t, x_0, x_1}\left[\left\| u_\theta(x_t, t) - (x_1 - x_0) \right\|^2 \right]$$

$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

---

## 📂 目录结构

```
理论学习/
│
├── 📋 README.md                              ← 你在这里
│
├── 01_Transformer/
│   ├── 01_attention_mechanism.md            ← 注意力机制完整推导
│   └── 02_vit_dit.md                        ← ViT/DiT/AdaLN-Zero
│
├── 02_生成模型/
│   ├── 01_VAE.md                            ← 变分自编码器
│   ├── 02_diffusion_models.md               ← 扩散模型
│   └── 03_flow_matching.md                  ← Flow Matching ⭐
│
├── 03_视频生成与DiT/
│   └── 01_latent_diffusion_video.md         ← 视频生成技术
│
├── 04_世界模型/
│   ├── 01_world_model_theory.md             ← 世界模型理论体系
│   └── 02_latent_action_models.md           ← 潜在动作模型 ⭐
│
├── 05_手部与人体模型/
│   └── 01_MANO.md                           ← MANO手部模型
│
├── 06_SLAM与相机/
│   └── 01_visual_slam_basics.md             ← 视觉SLAM基础
│
└── 07_机器人学习基础/
    ├── 01_imitation_learning.md             ← 模仿学习
    └── 02_VLA_architecture.md               ← VLA架构演化
```

---

## 📑 涵盖的核心论文

### 基础理论
- **Attention Is All You Need** (Vaswani et al., 2017)
- **An Image is Worth 16x16 Words: ViT** (Dosovitskiy et al., 2020)
- **Scalable Diffusion Models with Transformers: DiT** (Peebles & Xie, 2023)
- **Auto-Encoding Variational Bayes: VAE** (Kingma & Welling, 2013)
- **DDPM** (Ho et al., 2020) · **DDIM** (Song et al., 2020)
- **Flow Matching for Generative Modeling** (Lipman et al., 2022)
- **Rectified Flow** (Liu et al., 2022)
- **RoPE** (Su et al., 2021)

### 世界模型
- **PlaNet / DreamerV3** (Hafner et al., 2018–2023)
- **LAPA** (ICLR 2025) · **Moto** (ICCV 2025)
- **τ₀-WM** (2025) · **DreamDojo** (NVIDIA, 2026)
- **Genie Envisioner** (AgiBot, 2025)

### 手部与人体重建
- **MANO** (Romero et al., 2017) · **SMPL** (Loper et al., 2015)
- **HaMeR** (CVPR 2024) · **WiLoR** (2024) · **HandOS** (2025)
- **HaWoR** (CVPR 2025) · **Dyn-HaMR** (CVPR 2025 Highlight)
- **WHAM** (CVPR 2024) · **UniHOPE** (CVPR 2025)

### 机器人学习
- **Diffusion Policy** (Chi et al., 2023)
- **π₀ / π₀.₅** (Physical Intelligence, 2024–2025)
- **RT-2** (Google DeepMind, 2023)
- **GO-1 / ViLLA** (AgiBot, 2025)
- **DROID-SLAM** (Teed & Deng, 2021)
- **Metric3D** (Yin et al., 2023)

---

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/xiang-ao-data/embodied-ai-theory.git
cd embodied-ai-theory

# 在 VSCode 中打开
code .

# 安装 Markdown Preview Enhanced 后
# 右键任意 .md 文件 → Open Preview
```

---

## 🤝 说明

本项目为个人学习笔记，整理自原始论文与公开资料。
如有错误欢迎提 Issue 指正。

---

<div align="center">

**持续更新中** · 如果对你有帮助，欢迎 ⭐ Star

*Built with ❤️ for the Embodied AI community*

</div>

---

<!-- 以下为原始详细索引内容 -->

## 学习目标

本学习路径旨在帮助读者从零开始系统掌握以下前沿论文所需的全部理论基础：

| 论文 | 核心技术 | 依赖模块 |
|------|----------|----------|
| **τ₀-WM** (tau-zero World Model) | 视频DiT世界模型、动作条件生成、Wan2.2架构 | 01, 02, 03, 04 |
| **HaWoR** (Hand World Model) | 手部运动重建、ViT特征提取、世界坐标系预测 | 01, 03, 05, 06 |
| **DreamDojo** | 扩散策略、机器人动作合成、视频生成 | 02, 03, 04, 07 |
| **Genie Envisioner** | 交互式世界模型、潜在动作空间、视频预测 | 02, 03, 04, 07 |
| **HaMeR / HandOS** | ViT-H骨干网络、MANO手部参数化、Transformer回归头 | 01, 05 |

---

## 推荐学习顺序

```
基础层（必须先掌握）
    01_Transformer  ──────────────────────────────┐
                                                  │
生成模型层（并行可学）                              │
    02_生成模型 ──► 03_视频生成与DiT ◄─────────────┘
         │                  │
         ▼                  ▼
应用层（需要以上基础）
    04_世界模型 ◄─────────────────────────────────┐
    05_手部与人体模型 ◄───────────────────────────┤
    06_SLAM与相机 ────────────────────────────────┤
    07_机器人学习基础 ────────────────────────────┘
```

**强烈建议按顺序学习**：前三个模块是一切的基础，后四个模块彼此相对独立，可根据目标论文选择性深入。

---

## 模块详情

### 模块 01 — Transformer & Attention
**目录**：[01_Transformer/](./01_Transformer/)
**预计时间**：10–15 小时

Transformer 是现代 VLA（Vision-Language-Action）模型和世界模型的核心骨架。本模块彻底讲清注意力机制的数学本质，以及 ViT/DiT 这两个在视觉领域最重要的变体。

| 文件 | 内容简介 | 建议时间 |
|------|----------|----------|
| [01_attention_mechanism.md](./01_Transformer/01_attention_mechanism.md) | Scaled Dot-Product Attention 完整推导、Multi-Head Attention、位置编码（正弦 + RoPE）、Transformer Block 完整结构、复杂度分析 | 5–7 小时 |
| [02_vit_dit.md](./01_Transformer/02_vit_dit.md) | ViT 图像分块与 CLS token、ViT 缩放规律、DiT 架构与 AdaLN 条件注入、与 τ₀-WM / HaMeR 的具体联系 | 5–7 小时 |

**学完后你能做什么**：读懂任意基于 Transformer 的视觉模型（ViT-H、MAE、DiT-XL），理解 AdaLN 如何将时间步/文本条件注入扩散模型。

---

### 模块 02 — 生成模型：VAE、Diffusion、Flow Matching
**目录**：[02_生成模型/](./02_生成模型/)
**预计时间**：12–18 小时

扩散模型是 τ₀-WM、DreamDojo、Genie Envisioner 的生成核心。本模块从变分推断出发，推导 ELBO、DDPM 训练目标、DDIM 采样，再到 Flow Matching 的速度场视角，最终理解为何现代模型偏好 Rectified Flow。

| 文件 | 内容简介 | 建议时间 |
|------|----------|----------|
| 01_vae.md | 变分自编码器：ELBO 推导、重参数化技巧、KL 散度 closed form | 3–4 小时 |
| 02_ddpm.md | DDPM：前向加噪过程、逆向去噪、$L_\text{simple}$ 损失、$\epsilon$-预测 vs $x_0$-预测 | 4–5 小时 |
| 03_ddim_cfg.md | DDIM 确定性采样、Classifier-Free Guidance（CFG）原理与实现 | 3–4 小时 |
| 04_flow_matching.md | Continuous Normalizing Flows、Flow Matching 速度场、Rectified Flow | 3–4 小时 |

**学完后你能做什么**：理解 Wan2.2 为何使用 Rectified Flow 训练，读懂 DreamDojo 的扩散策略损失函数。

---

### 模块 03 — 视频生成与 DiT
**目录**：[03_视频生成与DiT/](./03_视频生成与DiT/)
**预计时间**：8–12 小时

视频扩散模型在时间维度上拓展了图像 DiT 的框架。本模块讲解时空注意力、3D VAE 潜在空间压缩，以及 τ₀-WM 使用的 Wan2.2 视频生成骨架。

| 文件 | 内容简介 | 建议时间 |
|------|----------|----------|
| 01_video_diffusion.md | 视频扩散模型发展脉络：VDM → Make-A-Video → Sora → Wan | 3–4 小时 |
| 02_temporal_attention.md | 时间注意力 vs 空间注意力、3D Full Attention、因果掩码 | 3–4 小时 |
| 03_wan22_architecture.md | Wan2.2 架构详解、3D VAE、RoPE 3D、τ₀-WM 如何在其上构建世界模型 | 2–4 小时 |

**学完后你能做什么**：完整读懂 τ₀-WM 论文的模型架构章节，理解动作条件如何注入视频扩散流。

---

### 模块 04 — 世界模型理论
**目录**：[04_世界模型/](./04_世界模型/)
**预计时间**：10–14 小时

世界模型是智能体对环境动态的内部表示。本模块从 RSSM（Dreamer）出发，讲解潜在动态模型、视频预测世界模型，以及 Genie/τ₀-WM 等基于大规模视频预训练的新范式。

| 文件 | 内容简介 | 建议时间 |
|------|----------|----------|
| 01_world_model_foundations.md | 世界模型定义、Dreamer/RSSM 架构、潜在状态预测 | 4–5 小时 |
| 02_video_world_models.md | GAIA-1、Genie、UniSim、τ₀-WM 的设计哲学与技术路线对比 | 3–4 小时 |
| 03_action_conditioned_generation.md | 动作条件视频生成、潜在动作空间、逆动力学模型 | 3–4 小时 |

**学完后你能做什么**：理解 τ₀-WM 为何是世界模型而不仅仅是视频生成器，能够分析其训练目标和推理流程。

---

### 模块 05 — 手部与人体参数化模型
**目录**：[05_手部与人体模型/](./05_手部与人体模型/)
**预计时间**：8–10 小时

HaWoR 和 HaMeR 的核心是将 ViT 特征回归到参数化手部模型（MANO）的参数上。本模块讲清 SMPL/MANO 的线性蒙皮（LBS）、形状/姿态参数空间，以及 HaWoR 如何在世界坐标系中重建连续手部运动。

| 文件 | 内容简介 | 建议时间 |
|------|----------|----------|
| 01_mano_model.md | MANO 手部模型：形状参数 $\beta$、姿态参数 $\theta$、线性蒙皮公式 | 3–4 小时 |
| 02_smpl_body.md | SMPL 人体模型、关节回归、Shape Blend Shapes | 2–3 小时 |
| 03_hawor_reconstruction.md | HaWoR 世界坐标系重建、WHAM 运动先验、时序 Transformer 回归 | 3–4 小时 |

**学完后你能做什么**：完整读懂 HaWoR 和 HaMeR 的方法章节，理解为什么需要参数化模型而不直接预测关节点。

---

### 模块 06 — SLAM 与相机模型
**目录**：[06_SLAM与相机/](./06_SLAM与相机/)
**预计时间**：8–12 小时

HaWoR 需要从单目视频中恢复相机运动，这涉及经典 SLAM 和现代学习方法（DPVO、DROID-SLAM）。本模块讲清相机投影模型、对极几何、Bundle Adjustment，以及如何把它们整合进手部重建流程。

| 文件 | 内容简介 | 建议时间 |
|------|----------|----------|
| 01_camera_model.md | 针孔相机模型、内参/外参矩阵、畸变、齐次坐标 | 2–3 小时 |
| 02_epipolar_geometry.md | 基础矩阵、本质矩阵、对极约束 | 2–3 小时 |
| 03_slam_foundations.md | 经典 SLAM 框架（前端+后端）、Bundle Adjustment、g2o/GTSAM | 2–3 小时 |
| 04_learning_slam.md | DPVO、DROID-SLAM 架构、HaWoR 中的相机轨迹估计 | 2–3 小时 |

**学完后你能做什么**：理解 HaWoR 相机运动模块的实现原理，知道 SLAM 在手部重建中起到什么角色。

---

### 模块 07 — 机器人学习基础
**目录**：[07_机器人学习基础/](./07_机器人学习基础/)
**预计时间**：10–15 小时

DreamDojo 和 τ₀-WM 都服务于机器人操控任务。本模块讲清模仿学习（BC、DAgger）、强化学习基础（策略梯度、Actor-Critic），以及扩散策略（Diffusion Policy）如何统一动作生成与物理约束。

| 文件 | 内容简介 | 建议时间 |
|------|----------|----------|
| 01_imitation_learning.md | 行为克隆、协方差偏移、DAgger、ACT | 3–4 小时 |
| 02_rl_foundations.md | MDP、策略梯度（REINFORCE/PPO）、Q-learning、SAC | 3–5 小时 |
| 03_diffusion_policy.md | 扩散策略架构、动作 chunk 预测、条件注入、与 ACT 的对比 | 2–3 小时 |
| 04_vla_models.md | RT-2、OpenVLA、π₀ 的 VLA 范式，动作 token vs 连续动作头 | 2–3 小时 |

**学完后你能做什么**：理解 DreamDojo 为何用扩散策略，能够分析 τ₀-WM 产生的合成轨迹如何用于策略训练。

---

## 学习资源汇总

### 必读综述
- Lecun, Y. (2022). A Path Towards Autonomous Machine Intelligence. *OpenReview*.
- Ha, D., & Schmidhuber, J. (2018). World Models. *arXiv:1803.10122*.
- Yang, Z., et al. (2024). Video Diffusion Models: A Survey. *arXiv*.

### 核心工具论文
- Vaswani, A., et al. (2017). Attention Is All You Need. *NeurIPS 2017*.
- Dosovitskiy, A., et al. (2021). An Image Is Worth 16x16 Words. *ICLR 2021*.
- Peebles, W., & Xie, S. (2023). Scalable Diffusion Models with Transformers. *ICCV 2023*.
- Ho, J., et al. (2020). Denoising Diffusion Probabilistic Models. *NeurIPS 2020*.
- Lipman, Y., et al. (2022). Flow Matching for Generative Modeling. *ICLR 2023*.

### 目标论文（最终要读懂的）
- τ₀-WM: *tau-zero World Model* (2025)
- HaWoR: *Hand World Model for Reconstruction* (2025)
- DreamDojo: *Learning Robot Skills via Video Dreaming* (2025)
- Genie Envisioner (2025)
- HaMeR: *Hand Mesh Recovery using ViT* (2024)

---

## 学习建议

1. **主动推导**：每个公式都自己在纸上推一遍。光看懂和能推导是两个层次。
2. **代码对照**：每学完一个模块，找对应的开源实现（如 `timm` 中的 ViT，`diffusers` 中的 DiT）对照代码验证理解。
3. **论文递进**：先读综述了解全貌，再读原始论文看细节，最后看代码确认实现。
4. **总时间估算**：全部模块约 **66–96 小时**（8–12 周，每天 1–2 小时）。
