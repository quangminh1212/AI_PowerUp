<!-- source: https://github.com/joeseesun/AI_Papers_2025.git sha: dabcc09201e825362dbc76c0eb0cad8d1191ec4c readme: main/README.md -->
# joeseesun/AI_Papers_2025

📚 2025 AI Engineering Reading List - 120+ curated AI research papers covering LLMs, Multimodal, RAG, Agents, Diffusion Models and more

---

# 2025 AI Engineering Reading List - 论文索引

> 本索引整理自 [Latent Space 2025 AI Papers Reading List](https://www.latent.space/p/2025-papers)
>
> 共收录 **120+ 篇** AI 领域重要论文，涵盖大语言模型、多模态、Agent、RAG、扩散模型等前沿方向

## 目录

- [1. Frontier LLMs - 前沿大语言模型](#1-frontier-llms---前沿大语言模型)
- [2. Benchmarks & Evaluations - 基准测试与评估](#2-benchmarks--evaluations---基准测试与评估)
- [3. Prompting & Chain-of-Thought - 提示工程与思维链](#3-prompting--chain-of-thought---提示工程与思维链)
- [4. Retrieval Augmented Generation - 检索增强生成](#4-retrieval-augmented-generation---检索增强生成)
- [5. Agents - 智能体](#5-agents---智能体)
- [6. Code Generation - 代码生成](#6-code-generation---代码生成)
- [7. Vision - 视觉模型](#7-vision---视觉模型)
- [8. Voice & Audio - 语音与音频](#8-voice--audio---语音与音频)
- [9. Image/Video Diffusion - 图像视频扩散模型](#9-imagevideo-diffusion---图像视频扩散模型)
- [10. Finetuning - 微调技术](#10-finetuning---微调技术)

---

## 1. Frontier LLMs - 前沿大语言模型

### GPT 系列

#### ⭐⭐⭐⭐⭐ [GPT-1](GPT1_Improving_Language_Understanding_OpenAI_2018.pdf)
**一句话介绍**: 开创性地证明了无监督预训练+有监督微调的范式在 NLP 任务上的有效性
**推荐理由**: 奠定了现代大语言模型的基础范式，必读的历史性论文

#### ⭐⭐⭐⭐⭐ [GPT-2](GPT2_Language_Models_Unsupervised_Multitask_Learners_OpenAI_2019.pdf)
**一句话介绍**: 展示了更大规模语言模型的零样本学习能力
**推荐理由**: 提出"语言模型即多任务学习器"的重要观点，引发行业对模型规模的重新思考

#### ⭐⭐⭐⭐⭐ [GPT-3](GPT3_Language_Models_Few_Shot_Learners_OpenAI_2020.pdf)
**一句话介绍**: 证明了 175B 参数规模模型具有强大的少样本学习能力
**推荐理由**: 开启大模型时代，展示了 in-context learning 的惊人能力，必读经典

#### ⭐⭐⭐⭐⭐ [Codex](Codex_Evaluating_Large_Language_Models_Trained_on_Code_OpenAI_2021.pdf)
**一句话介绍**: GPT-3 在代码数据上微调，开创了 AI 辅助编程的新时代
**推荐理由**: GitHub Copilot 的技术基础，证明了 LLM 在代码生成上的潜力

#### ⭐⭐⭐⭐⭐ [InstructGPT](InstructGPT_Training_Language_Models_Follow_Instructions_OpenAI_2022.pdf)
**一句话介绍**: 通过 RLHF 让模型更好地遵循人类指令
**推荐理由**: 奠定了 ChatGPT 的技术基础，RLHF 成为业界标准做法

#### ⭐⭐⭐⭐⭐ [GPT-4](GPT4_Technical_Report_OpenAI_2023.pdf)
**一句话介绍**: OpenAI 首个多模态大模型，在多项基准测试上达到人类水平
**推荐理由**: 展示了多模态能力和更强的推理能力，定义了 GPT 时代的新标准

### Claude 系列

#### ⭐⭐⭐⭐ [Claude 3](Claude3_Model_Card_Anthropic_2024.pdf)
**一句话介绍**: Anthropic 推出的高性能 LLM，强调安全性和有用性
**推荐理由**: 在多项基准上与 GPT-4 竞争，提供了更长的上下文窗口

#### ⭐⭐⭐⭐⭐ [Claude 4](Claude4_Model_Card_Anthropic_2025.pdf)
**一句话介绍**: Claude 最新一代模型，在推理和长文本处理上有显著提升
**推荐理由**: 代表了当前 AI 安全对齐的最高水平，值得研究其技术细节

### Google 系列

#### ⭐⭐⭐⭐⭐ [Gemini 1.0](Gemini1_Capabilities_Multimodal_Models_Google_2023.pdf)
**一句话介绍**: Google 原生多模态模型，设计之初就考虑了文本、图像、视频等多种模态
**推荐理由**: 展示了原生多模态架构的优势，在多项测试中超越 GPT-4V

#### ⭐⭐⭐⭐ [Gemini 2.5](Gemini2.5_Flash_Thinking_Experimental_Google_2025.pdf)
**一句话介绍**: 加入思维过程展示的实验性版本，提升推理透明度
**推荐理由**: 探索了 LLM 推理过程可解释性的新方向

#### ⭐⭐⭐⭐ [Gemma 2](Gemma2_Improving_Open_Language_Models_Google_2024.pdf)
**一句话介绍**: Google 开源的轻量级高性能语言模型
**推荐理由**: 证明了小模型也能达到优秀性能，适合资源受限场景

#### ⭐⭐⭐ [Gemma 3](Gemma3_Technical_Report_Google_2025.pdf)
**一句话介绍**: Gemma 系列最新版本，进一步优化效率和性能
**推荐理由**: 持续推进开源小模型的性能边界

### Meta Llama 系列

#### ⭐⭐⭐⭐ [Llama 1](Llama1_Open_Foundation_Language_Models_Meta_2023.pdf)
**一句话介绍**: Meta 开源的基础语言模型，引发开源 LLM 浪潮
**推荐理由**: 开源运动的里程碑，展示了开源模型的潜力

#### ⭐⭐⭐⭐⭐ [Llama 2](Llama2_Open_Foundation_Fine_Tuned_Chat_Models_Meta_2023.pdf)
**一句话介绍**: 加入 RLHF 的 Llama 版本，可商用的高质量开源模型
**推荐理由**: 开源社区的基石，详细披露了 RLHF 训练细节

#### ⭐⭐⭐⭐⭐ [Llama 3](Llama3_Herd_of_Models_Meta_2024.pdf)
**一句话介绍**: Meta 最强开源模型系列，包含多种规模和能力变体
**推荐理由**: 在多项基准上接近闭源模型，推动了开源 AI 的发展

### Mistral 系列

#### ⭐⭐⭐⭐ [Mistral 7B](Mistral_7B_Mistral_2023.pdf)
**一句话介绍**: 7B 参数的高效语言模型，性能超越 Llama 2 13B
**推荐理由**: 证明了架构优化的重要性，小模型也能有大性能

#### ⭐⭐⭐⭐⭐ [Mixtral](Mixtral_Sparse_Mixture_of_Experts_Mistral_2024.pdf)
**一句话介绍**: 采用稀疏混合专家架构的开源模型，效率极高
**推荐理由**: MoE 架构在开源领域的成功应用，值得深入研究

#### ⭐⭐⭐ [Pixtral](Pixtral_12B_Mistral_2024.pdf)
**一句话介绍**: Mistral 的多模态版本，支持图像理解
**推荐理由**: 展示了如何将现有 LLM 扩展到多模态

### DeepSeek 系列

#### ⭐⭐⭐⭐ [DeepSeek V1](DeepSeek_V1_Scaling_Open_Source_Language_Models_2024.pdf)
**一句话介绍**: 中国团队开源的大规模语言模型
**推荐理由**: 展示了中国 AI 团队的技术实力

#### ⭐⭐⭐⭐⭐ [DeepSeek Coder](DeepSeek_Coder_When_LLM_Meets_Programming_2024.pdf)
**一句话介绍**: 专注代码生成的开源模型，性能接近 Codex
**推荐理由**: 开源代码模型的标杆，详细披露了代码预训练技术

#### ⭐⭐⭐⭐ [DeepSeek Math](DeepSeek_Math_Pushing_Limits_Mathematical_Reasoning_2024.pdf)
**一句话介绍**: 专注数学推理的语言模型
**推荐理由**: 在数学问题上表现优异，揭示了数学推理的训练方法

#### ⭐⭐⭐⭐ [DeepSeek MoE](DeepSeek_MoE_Towards_Ultimate_Expert_Specialization_2024.pdf)
**一句话介绍**: 探索混合专家架构的极限专家化
**推荐理由**: MoE 架构的深入研究，提出了新的专家分配策略

#### ⭐⭐⭐⭐⭐ [DeepSeek V2](DeepSeek_V2_Strong_Economical_Efficient_Mixture_of_Experts_2024.pdf)
**一句话介绍**: 结合 MoE 和新架构的高效强大模型
**推荐理由**: 在效率和性能上达到新的平衡点，技术报告详实

### AI2 开源系列

#### ⭐⭐⭐⭐ [OLMo](OLMo_Accelerating_Science_of_Language_Models_AI2_2024.pdf)
**一句话介绍**: AI2 完全开源的语言模型，包括数据、代码、训练过程
**推荐理由**: 真正的全栈开源，对研究社区极具价值

#### ⭐⭐⭐ [Molmo](Molmo_Open_Weights_State_of_Art_Multimodal_AI2_2024.pdf)
**一句话介绍**: AI2 开源的多模态模型
**推荐理由**: 开源多模态模型的重要贡献

#### ⭐⭐⭐⭐ [OLMoE](OLMoE_Open_Mixture_of_Experts_Language_Models_AI2_2024.pdf)
**一句话介绍**: 开源的混合专家语言模型
**推荐理由**: 为研究 MoE 架构提供了完整的开源实现

### Scaling Laws & 优化

#### ⭐⭐⭐⭐⭐ [Scaling Laws (Kaplan)](Scaling_Laws_Neural_Language_Models_Kaplan_OpenAI_2020.pdf)
**一句话介绍**: 首次系统性研究语言模型的缩放规律
**推荐理由**: 奠定了大模型时代的理论基础，必读经典

#### ⭐⭐⭐⭐⭐ [Chinchilla](Chinchilla_Training_Compute_Optimal_Large_LMs_DeepMind_2022.pdf)
**一句话介绍**: 证明了之前的模型都训练不足，提出新的最优缩放规律
**推荐理由**: 改变了行业对模型规模和训练数据的认知

#### ⭐⭐⭐⭐ [Emergent Abilities](Emergent_Abilities_Large_Language_Models_Google_2022.pdf)
**一句话介绍**: 研究大模型的涌现能力现象
**推荐理由**: 揭示了模型规模增长带来的质变

#### ⭐⭐⭐ [The Mirage of Emergence](Mirage_Emergent_Abilities_LLMs_Stanford_2023.pdf)
**一句话介绍**: 质疑涌现能力，认为可能是评估指标导致的假象
**推荐理由**: 提供了批判性视角，引发重要学术讨论

#### ⭐⭐⭐ [Post-Chinchilla Scaling Laws](Post_Chinchilla_Scaling_Laws_Revised_Approach_2024.pdf)
**一句话介绍**: 重新审视 Chinchilla 之后的缩放规律
**推荐理由**: 持续更新对 scaling laws 的理解

#### ⭐⭐⭐⭐ [Muon Optimizer](Muon_Optimizer_Momentum_Orthogonalized_Newton_2025.pdf)
**一句话介绍**: 新型优化器，结合动量和正交化牛顿方法
**推荐理由**: 可能改进大模型训练效率的新方向

#### ⭐⭐⭐⭐ [Let's Verify Step by Step](Lets_Verify_Step_by_Step_Process_Supervision_OpenAI_2023.pdf)
**一句话介绍**: 通过过程监督提升数学推理能力
**推荐理由**: 重要的对齐技术，改进了模型推理质量

#### ⭐⭐⭐⭐ [s1 - Scaling Test-Time Compute](s1_Scaling_Test_Time_Compute_Efficiently_2025.pdf)
**一句话介绍**: 研究如何有效扩展测试时计算以提升性能
**推荐理由**: 探索了训练之外提升模型能力的新维度

---

## 2. Benchmarks & Evaluations - 基准测试与评估

### 通用能力测试

#### ⭐⭐⭐⭐⭐ [MMLU](MMLU_Massive_Multitask_Language_Understanding_2020.pdf)
**一句话介绍**: 涵盖 57 个学科的大规模多任务理解基准
**推荐理由**: 业界最广泛使用的通用能力测试，必须了解

#### ⭐⭐⭐⭐ [MMLU Pro](MMLU_Pro_Robust_Challenging_Reasoning_Benchmark_2024.pdf)
**一句话介绍**: MMLU 的加强版，更难、更具挑战性
**推荐理由**: 提高了测试难度，减少了题目泄露问题

#### ⭐⭐⭐⭐ [GPQA](GPQA_Graduate_Level_Google_Proof_QA_Benchmark_2023.pdf)
**一句话介绍**: 研究生级别的问答基准，专家都难以作弊
**推荐理由**: 测试真正的深度理解和推理能力

#### ⭐⭐⭐⭐ [BIG-Bench](BIG_Bench_Beyond_Imitation_Game_Benchmark_Google_2022.pdf)
**一句话介绍**: 包含 200+ 任务的大规模基准测试集
**推荐理由**: 多样化的任务设计，全面评估模型能力

#### ⭐⭐⭐⭐ [BIG-Bench Hard](BIG_Bench_Hard_Challenging_Tasks_from_BIG_Bench_2022.pdf)
**一句话介绍**: BIG-Bench 中模型表现不佳的困难任务子集
**推荐理由**: 聚焦模型弱点，推动能力边界

### 推理与理解

#### ⭐⭐⭐ [MRCR](MRCR_Multimodal Reverse_Chain_Reasoning_2024.pdf)
**一句话介绍**: 多模态逆向链式推理基准
**推荐理由**: 测试逆向思维和因果推理能力

#### ⭐⭐⭐⭐ [MuSR](MuSR_Multistep_Soft_Reasoning_Benchmark_2023.pdf)
**一句话介绍**: 多步骤软推理基准测试
**推荐理由**: 评估复杂推理链的处理能力

### 长文本处理

#### ⭐⭐⭐⭐ [LongBench](LongBench_Bilingual_Multitask_Benchmark_Long_Context_2024.pdf)
**一句话介绍**: 双语多任务长文本基准，支持中英文
**推荐理由**: 全面评估长上下文理解能力

#### ⭐⭐⭐ [BABILong](BABILong_Testing_Language_Models_Long_Context_Reasoning_2024.pdf)
**一句话介绍**: 测试超长上下文中的推理能力
**推荐理由**: 挑战模型在海量信息中的检索和推理

### 数学能力

#### ⭐⭐⭐⭐⭐ [MATH](MATH_Dataset_Measuring_Mathematical_Problem_Solving_2021.pdf)
**一句话介绍**: 高中竞赛级数学问题数据集
**推荐理由**: 数学推理能力的黄金标准

#### ⭐⭐⭐⭐⭐ [FrontierMath](FrontierMath_Benchmark_Extreme_Scale_Unsolved_Mathematics_2024.pdf)
**一句话介绍**: 包含前沿未解决数学问题的极难基准
**推荐理由**: 展示了 AI 数学能力的真实天花板

### 指令遵循

#### ⭐⭐⭐⭐ [IFEval](IFEval_Instruction_Following_Evaluation_Google_2023.pdf)
**一句话介绍**: 评估模型遵循复杂指令的能力
**推荐理由**: 指令遵循是实用性的关键指标

#### ⭐⭐⭐ [Multi-IF](Multi_IF_Multifaceted_Instruction_Following_2024.pdf)
**一句话介绍**: 多方面指令遵循评估
**推荐理由**: 更全面地测试指令理解和执行

#### ⭐⭐⭐⭐ [Scale MultiChallenge](Scale_MultiChallenge_Evaluating_LLMs_Multifaceted_Understanding_2025.pdf)
**一句话介绍**: Scale AI 推出的多维度挑战基准
**推荐理由**: 综合评估模型的多方面能力

---

## 3. Prompting & Chain-of-Thought - 提示工程与思维链

#### ⭐⭐⭐⭐⭐ [The Prompt Report](Prompt_Report_Systematic_Survey_Prompting_Techniques_2024.pdf)
**一句话介绍**: 系统性总结提示工程技术的综述论文
**推荐理由**: 全面了解提示工程的必读综述

#### ⭐⭐⭐⭐⭐ [Chain-of-Thought Prompting](Chain_of_Thought_Prompting_Elicits_Reasoning_LLMs_Google_2022.pdf)
**一句话介绍**: 通过引导模型展示推理步骤来提升推理能力
**推荐理由**: 开创性工作，CoT 成为标准技术

#### ⭐⭐⭐⭐ [Show Your Work: Scratchpads](Show_Your_Work_Scratchpads_Intermediate_Computation_LMs_2021.pdf)
**一句话介绍**: 让模型使用"草稿纸"进行中间计算
**推荐理由**: CoT 的早期探索，启发性强

#### ⭐⭐⭐⭐ [Let's Think Step by Step](Large_Language_Models_Zero_Shot_Reasoners_2022.pdf)
**一句话介绍**: 证明简单的提示词就能激发零样本推理能力
**推荐理由**: 极简但有效的技术，广泛应用

#### ⭐⭐⭐⭐ [Tree of Thoughts](Tree_of_Thoughts_Deliberate_Problem_Solving_LLMs_2023.pdf)
**一句话介绍**: 通过树状搜索探索多条推理路径
**推荐理由**: 扩展了 CoT，适合复杂问题求解

#### ⭐⭐⭐ [Prefix-Tuning](Prefix_Tuning_Optimizing_Continuous_Prompts_Generation_2021.pdf)
**一句话介绍**: 通过优化连续前缀向量来适配任务
**推荐理由**: 参数高效的提示优化方法

#### ⭐⭐⭐ [Adjusting Decoding](In_Context_Learning_Adjusting_Decoding_2024.pdf)
**一句话介绍**: 通过调整解码策略改进 ICL 效果
**推荐理由**: 从解码角度优化提示学习

#### ⭐⭐⭐⭐ [Automatic Prompt Engineering](Automatic_Prompt_Engineer_Optimization_LLMs_2022.pdf)
**一句话介绍**: 自动搜索和优化提示词
**推荐理由**: 减少人工设计提示的成本

#### ⭐⭐⭐⭐⭐ [DSPy](DSPy_Programming_Foundation_Models_Stanford_2023.pdf)
**一句话介绍**: 将提示工程系统化为可编程框架
**推荐理由**: 改变提示工程的工作方式，值得深入学习

---

## 4. Retrieval Augmented Generation - 检索增强生成

#### ⭐⭐⭐⭐⭐ [RAG (Meta)](RAG_Retrieval_Augmented_Generation_Knowledge_Intensive_NLP_Meta_2020.pdf)
**一句话介绍**: 提出结合检索和生成的 RAG 范式
**推荐理由**: 开创性工作，解决了 LLM 知识更新问题

#### ⭐⭐⭐⭐ [MTEB](MTEB_Massive_Text_Embedding_Benchmark_2022.pdf)
**一句话介绍**: 大规模文本嵌入基准测试
**推荐理由**: 评估检索模型的标准基准

#### ⭐⭐⭐⭐ [GraphRAG](GraphRAG_From_Local_to_Global_Graph_Based_Text_Processing_2024.pdf)
**一句话介绍**: 基于知识图谱的 RAG，支持全局推理
**推荐理由**: 突破传统 RAG 的局部检索限制

#### ⭐⭐⭐⭐ [RAGAS](RAGAS_Automated_Evaluation_RAG_2023.pdf)
**一句话介绍**: RAG 系统的自动化评估框架
**推荐理由**: 系统化评估 RAG 质量的工具

#### ⭐⭐⭐ [Nvidia FACTS Framework](Nvidia_FACTS_Framework_Factuality_Consistency_Systems_2024.pdf)
**一句话介绍**: 评估 RAG 系统事实性和一致性
**推荐理由**: 关注 RAG 的关键质量指标

#### ⭐⭐⭐⭐ [RAG vs Long Context](RAG_vs_Long_Context_Which_Better_QA_2024.pdf)
**一句话介绍**: 对比 RAG 和长上下文在 QA 任务上的效果
**推荐理由**: 帮助选择合适的技术方案

---

## 5. Agents - 智能体

### 编程 Agent

#### ⭐⭐⭐⭐⭐ [SWE-Bench](SWE_Bench_Can_Language_Models_Resolve_Real_GitHub_Issues_2023.pdf)
**一句话介绍**: 基于真实 GitHub issue 的软件工程基准
**推荐理由**: 编程 Agent 的黄金标准，极具实用价值

#### ⭐⭐⭐⭐⭐ [SWE-Agent](SWE_Agent_Agent_Computer_Interfaces_Software_Engineering_2024.pdf)
**一句话介绍**: 为软件工程任务设计的 Agent 系统
**推荐理由**: 展示了 Agent-Computer Interface 的设计原则

#### ⭐⭐⭐⭐ [SWE-Bench Multimodal](SWE_Bench_Multimodal_Coding_Agents_See_Better_2024.pdf)
**一句话介绍**: 加入视觉能力的编程基准
**推荐理由**: 证明视觉对编程任务的帮助

### Agent 基准

#### ⭐⭐⭐⭐ [TauBench](TauBench_Benchmarking_Tool_Agent_Learning_Usability_2024.pdf)
**一句话介绍**: 测试 Agent 工具学习和使用能力
**推荐理由**: 评估 Agent 的工具使用能力

#### ⭐⭐⭐⭐ [GAIA](GAIA_Benchmark_Suite_General_AI_Assistants_2023.pdf)
**一句话介绍**: 通用 AI 助手的基准测试套件
**推荐理由**: 全面评估 Agent 的实际应用能力

### Agent 架构

#### ⭐⭐⭐⭐⭐ [ReAct](ReAct_Synergizing_Reasoning_Acting_Language_Models_2022.pdf)
**一句话介绍**: 结合推理和行动的 Agent 范式
**推荐理由**: Agent 架构的奠基性工作，影响深远

#### ⭐⭐⭐⭐ [Toolformer](Toolformer_Language_Models_Teach_Themselves_Use_Tools_2023.pdf)
**一句话介绍**: 让 LLM 自学如何使用工具
**推荐理由**: 工具使用的自监督学习方法

#### ⭐⭐⭐ [HuggingGPT](HuggingGPT_Solving_AI_Tasks_ChatGPT_Friends_HuggingFace_2023.pdf)
**一句话介绍**: 用 LLM 协调多个 AI 模型完成任务
**推荐理由**: 展示了 LLM 作为控制器的潜力

#### ⭐⭐⭐⭐ [MemGPT](MemGPT_Towards_LLMs_Operating_Systems_2023.pdf)
**一句话介绍**: 将操作系统的内存管理思想应用到 LLM
**推荐理由**: 创新性地解决了上下文限制问题

#### ⭐⭐⭐⭐ [MetaGPT](MetaGPT_Meta_Programming_Multi_Agent_Collaborative_Framework_2023.pdf)
**一句话介绍**: 多 Agent 协作的元编程框架
**推荐理由**: 软件开发流程的 Agent 化

#### ⭐⭐⭐⭐⭐ [AutoGen](AutoGen_Enabling_Next_Gen_LLM_Applications_Multi_Agent_Conversation_2023.pdf)
**一句话介绍**: 微软推出的多 Agent 对话框架
**推荐理由**: 工程化程度高，易于使用的 Agent 框架

#### ⭐⭐⭐⭐ [Voyager](Voyager_Open_Ended_Embodied_Agent_LLM_2023.pdf)
**一句话介绍**: 在 Minecraft 中持续学习的具身 Agent
**推荐理由**: 展示了 Agent 的持续学习和探索能力

#### ⭐⭐⭐⭐ [Cognitive Architectures](Cognitive_Architectures_Language_Agents_2023.pdf)
**一句话介绍**: 语言 Agent 的认知架构综述
**推荐理由**: 系统化理解 Agent 设计的理论框架

#### ⭐⭐⭐ [Agent Workflow Memory](Agent_Workflow_Memory_AWM_2024.pdf)
**一句话介绍**: Agent 的工作流记忆机制
**推荐理由**: 改进 Agent 的任务规划和执行

---

## 6. Code Generation - 代码生成

### 代码数据集

#### ⭐⭐⭐⭐ [The Stack](The_Stack_3TB_Permissively_Licensed_Source_Code_2022.pdf)
**一句话介绍**: 3TB 的开源代码数据集
**推荐理由**: 代码预训练的重要数据来源

### 代码模型

#### ⭐⭐⭐⭐ [StarCoder 2](StarCoder_2_New_Generation_Code_LLMs_2024.pdf)
**一句话介绍**: 新一代开源代码生成模型
**推荐理由**: 高质量的开源代码模型

#### ⭐⭐⭐⭐ [Qwen2.5-Coder](Qwen2.5_Coder_Technical_Report_2024.pdf)
**一句话介绍**: 阿里云推出的强大代码模型
**推荐理由**: 在多项代码基准上表现优异

### 代码生成技术

#### ⭐⭐⭐⭐ [AlphaCodeium](AlphaCodeium_Code_Generation_Flow_Engineering_2024.pdf)
**一句话介绍**: 通过流程工程提升代码生成质量
**推荐理由**: 展示了工程化方法在代码生成上的价值

#### ⭐⭐⭐⭐ [Codeforces](Codeforces_Programming_Competitions_Evaluating_LLMs_2023.pdf)
**一句话介绍**: 用编程竞赛题评估 LLM 代码能力
**推荐理由**: 高难度的代码生成基准

### 代码安全

#### ⭐⭐⭐⭐ [Do AI Code Assistants Introduce Security Vulnerabilities?](Do_AI_Code_Assistants_Introduce_Security_Vulnerabilities_2024.pdf)
**一句话介绍**: 研究 AI 编程助手引入的安全漏洞
**推荐理由**: 关注 AI 生成代码的安全性，实用性强

---

## 7. Vision - 视觉模型

### 目标检测

#### ⭐⭐⭐⭐ [YOLO](YOLO_You_Only_Look_Once_Real_Time_Object_Detection_2015.pdf)
**一句话介绍**: 实时目标检测的开创性工作
**推荐理由**: 计算机视觉的经典，影响了整个领域

#### ⭐⭐⭐⭐ [DETRs Beat YOLOs](DETRs_Beat_YOLOs_Real_Time_End_to_End_Detection_2023.pdf)
**一句话介绍**: 基于 Transformer 的检测器超越 YOLO
**推荐理由**: 展示了 Transformer 在视觉任务上的优势

### 视觉-语言模型

#### ⭐⭐⭐⭐⭐ [CLIP](CLIP_Learning_Transferable_Visual_Models_Natural_Language_OpenAI_2021.pdf)
**一句话介绍**: 通过对比学习连接图像和文本
**推荐理由**: 多模态基础模型的里程碑

#### ⭐⭐⭐⭐⭐ [Vision Transformer (ViT)](Vision_Transformer_ViT_Image_Worth_16x16_Words_Google_2020.pdf)
**一句话介绍**: 将 Transformer 应用到视觉任务
**推荐理由**: 改变了计算机视觉的范式

#### ⭐⭐⭐⭐ [BLIP](BLIP_Bootstrapping_Language_Image_Pretraining_2022.pdf)
**一句话介绍**: 统一理解和生成的视觉-语言预训练
**推荐理由**: 高效的多模态预训练方法

#### ⭐⭐⭐⭐ [BLIP-2](BLIP2_Bootstrapping_LLMs_Vision_Language_Pretraining_2023.pdf)
**一句话介绍**: 用 Q-Former 连接冻结的视觉和语言模型
**推荐理由**: 参数高效的多模态模型训练

### 多模态基准

#### ⭐⭐⭐ [MMVP](MMVP_Eyes_Wide_Shut_Multimodal_LLMs_Visual_Prompts_2024.pdf)
**一句话介绍**: 测试多模态 LLM 对视觉提示的理解
**推荐理由**: 揭示了多模态模型的弱点

#### ⭐⭐⭐⭐ [MMMU](MMMU_Massive_Multi_Discipline_Multimodal_Understanding_2023.pdf)
**一句话介绍**: 大规模多学科多模态理解基准
**推荐理由**: 全面评估多模态推理能力

### 图像分割

#### ⭐⭐⭐⭐⭐ [Segment Anything (SAM)](SAM_Segment_Anything_Model_Meta_2023.pdf)
**一句话介绍**: 通用的图像分割基础模型
**推荐理由**: Zero-shot 分割的突破，应用广泛

#### ⭐⭐⭐⭐ [SAM 2](SAM2_Segment_Anything_Images_Videos_Meta_2024.pdf)
**一句话介绍**: 扩展到视频的 SAM 版本
**推荐理由**: 将分割能力扩展到时序维度

### 多模态 LLM

#### ⭐⭐⭐⭐ [Chameleon](Chameleon_Mixed_Modal_Early_Fusion_Foundation_Models_Meta_2024.pdf)
**一句话介绍**: 早期融合的混合模态基础模型
**推荐理由**: 探索了不同的多模态架构

#### ⭐⭐⭐ [AIMv2](AIMv2_Autoregressive_Image_Models_Self_Supervised_Visual_Pretraining_2024.pdf)
**一句话介绍**: 自回归图像模型用于自监督视觉预训练
**推荐理由**: 视觉预训练的新思路

#### ⭐⭐⭐ [Reka Core](Reka_Core_Multimodal_Language_Model_2024.pdf)
**一句话介绍**: Reka 公司的多模态语言模型
**推荐理由**: 多模态领域的竞争者

#### ⭐⭐⭐⭐ [GPT-4V System Card](GPT4V_System_Card_Vision_OpenAI_2023.pdf)
**一句话介绍**: GPT-4 视觉能力的系统卡片
**推荐理由**: 了解 GPT-4V 的能力和限制

#### ⭐⭐⭐⭐ [LLaVA](LLaVA_Visual_Instruction_Tuning_Microsoft_2023.pdf)
**一句话介绍**: 通过视觉指令调优构建多模态 LLM
**推荐理由**: 开源多模态模型的重要工作

---

## 8. Voice & Audio - 语音与音频

#### ⭐⭐⭐⭐⭐ [Whisper](Whisper_Robust_Speech_Recognition_Weak_Supervision_OpenAI_2022.pdf)
**一句话介绍**: 鲁棒的大规模语音识别模型
**推荐理由**: 语音识别的新标准，开源且效果优异

#### ⭐⭐⭐⭐ [NaturalSpeech](NaturalSpeech_End_to_End_Text_to_Speech_Synthesis_Human_Level_Quality_2022.pdf)
**一句话介绍**: 达到人类水平的端到端 TTS 系统
**推荐理由**: TTS 质量的重要突破

#### ⭐⭐⭐⭐ [NaturalSpeech 3](NaturalSpeech3_Zero_Shot_Speech_Synthesis_Factorized_Codec_Diffusion_2024.pdf)
**一句话介绍**: 零样本语音合成，支持多种风格
**推荐理由**: TTS 灵活性的提升

#### ⭐⭐⭐⭐ [Llama 3 Speech](Llama_3_Speech_Omni_Seamlessly_Integrating_Speech_Llama_3_2024.pdf)
**一句话介绍**: 将语音能力集成到 Llama 3
**推荐理由**: 多模态 LLM 的语音扩展

#### ⭐⭐⭐⭐ [wav2vec 2.0](wav2vec_2.0_Self_Supervised_Learning_Speech_Representations_2020.pdf)
**一句话介绍**: 语音表示的自监督学习
**推荐理由**: 奠定了语音预训练的基础

---

## 9. Image/Video Diffusion - 图像视频扩散模型

### 扩散模型基础

#### ⭐⭐⭐⭐⭐ [Latent Diffusion Models](Latent_Diffusion_High_Resolution_Image_Synthesis_2021.pdf)
**一句话介绍**: 在潜在空间进行扩散，大幅降低计算成本
**推荐理由**: Stable Diffusion 的理论基础，必读

#### ⭐⭐⭐⭐ [SDXL](SDXL_Improving_Latent_Diffusion_Models_High_Resolution_Synthesis_2023.pdf)
**一句话介绍**: 改进的 Stable Diffusion，支持更高分辨率
**推荐理由**: SD 系列的重要升级

#### ⭐⭐⭐⭐ [Stable Diffusion 3](SD3_Scaling_Rectified_Flow_Transformers_High_Resolution_Image_Synthesis_2024.pdf)
**一句话介绍**: 采用整流流和 Transformer 的 SD3
**推荐理由**: 架构创新，性能提升

### OpenAI DALL-E 系列

#### ⭐⭐⭐⭐ [DALL-E](DALL_E_Zero_Shot_Text_to_Image_Generation_OpenAI_2021.pdf)
**一句话介绍**: 开创性的文本到图像生成模型
**推荐理由**: 首次展示了 zero-shot 文生图的潜力

#### ⭐⭐⭐⭐⭐ [DALL-E 2](DALL_E_2_Hierarchical_Text_Conditional_Image_Generation_OpenAI_2022.pdf)
**一句话介绍**: 引入 CLIP 的层次化文生图模型
**推荐理由**: 质量的巨大飞跃，影响深远

#### ⭐⭐⭐⭐ [DALL-E 3](DALL_E_3_Improving_Image_Generation_Better_Captions_OpenAI_2023.pdf)
**一句话介绍**: 通过改进文本理解提升生成质量
**推荐理由**: 提示词遵循能力大幅提升

### Google Imagen 系列

#### ⭐⭐⭐⭐ [Imagen](Imagen_Photorealistic_Text_to_Image_Diffusion_Models_Google_2022.pdf)
**一句话介绍**: 照片级真实感的文生图扩散模型
**推荐理由**: 展示了大语言模型编码器的威力

#### ⭐⭐⭐⭐ [Imagen 3](Imagen3_Technical_Report_Google_2024.pdf)
**一句话介绍**: Imagen 最新版本技术报告
**推荐理由**: 持续改进的生成质量

### 加速技术

#### ⭐⭐⭐⭐ [Consistency Models](Consistency_Models_2023.pdf)
**一句话介绍**: 单步或少步生成的扩散模型
**推荐理由**: 大幅加速生成过程

#### ⭐⭐⭐⭐ [Latent Consistency Models](LCM_Latent_Consistency_Models_Few_Step_Inference_Diffusion_2023.pdf)
**一句话介绍**: 潜在空间的一致性模型
**推荐理由**: 实时生成的关键技术

#### ⭐⭐⭐ [Improved Consistency Models](sCM_Improved_Techniques_Consistency_Models_2024.pdf)
**一句话介绍**: 改进的一致性模型训练技术
**推荐理由**: 进一步优化生成质量和速度

### 架构创新

#### ⭐⭐⭐⭐⭐ [Diffusion Transformers (DiT)](DiT_Scalable_Diffusion_Models_Transformers_2022.pdf)
**一句话介绍**: 用 Transformer 替换 UNet 的扩散模型
**推荐理由**: 架构范式转变，可扩展性强

#### ⭐⭐⭐ [OpenSora](OpenSora_Democratizing_Efficient_Video_Production_All_2024.pdf)
**一句话介绍**: 开源的视频生成模型
**推荐理由**: 降低视频生成的门槛

#### ⭐⭐⭐ [Llama Native Image Generation](Llama_Native_Image_Generation_Generative_Models_2024.pdf)
**一句话介绍**: Llama 原生支持的图像生成
**推荐理由**: 探索统一架构的可能性

---

## 10. Finetuning - 微调技术

#### ⭐⭐⭐⭐⭐ [LoRA](LoRA_Low_Rank_Adaptation_Large_Language_Models_2021.pdf)
**一句话介绍**: 通过低秩矩阵高效微调大模型
**推荐理由**: 最流行的参数高效微调方法，必学

#### ⭐⭐⭐⭐⭐ [QLoRA](QLoRA_Efficient_Finetuning_Quantized_LLMs_2023.pdf)
**一句话介绍**: 结合量化的 LoRA，进一步降低显存需求
**推荐理由**: 让消费级 GPU 也能微调大模型

#### ⭐⭐⭐⭐⭐ [DPO](DPO_Direct_Preference_Optimization_Language_Models_2023.pdf)
**一句话介绍**: 无需 RL 的偏好对齐方法
**推荐理由**: 简化了 RLHF 流程，效果优异

#### ⭐⭐⭐⭐ [PPO](PPO_Proximal_Policy_Optimization_Algorithms_2017.pdf)
**一句话介绍**: 近端策略优化，RLHF 的核心算法
**推荐理由**: 理解 RLHF 的理论基础

#### ⭐⭐⭐⭐ [ReFT](ReFT_Representation_Finetuning_Parameter_Efficient_LLM_Training_2024.pdf)
**一句话介绍**: 通过调整表示层进行参数高效微调
**推荐理由**: 微调技术的新思路

---

## 使用说明

### Obsidian 使用技巧

1. **快速导航**: 使用 `Ctrl/Cmd + O` 快速打开论文
2. **反向链接**: 在笔记中引用论文时使用 `[[论文标题]]`
3. **标签系统**: 可以为论文添加自定义标签，如 `#必读` `#入门` `#进阶`
4. **搜索功能**: 使用 `Ctrl/Cmd + Shift + F` 全局搜索论文内容

### 推荐阅读路径

#### 入门路径（⭐⭐⭐⭐⭐标记的论文）
1. GPT 系列 (GPT-1 → GPT-2 → GPT-3)
2. Scaling Laws & Chinchilla
3. Chain-of-Thought Prompting
4. LoRA & QLoRA
5. CLIP & Vision Transformer

#### 实战路径
1. Llama 2/3 技术报告
2. RAG 论文
3. ReAct & AutoGen
4. SWE-Bench & SWE-Agent
5. DSPy

#### 前沿探索路径
1. DeepSeek 系列
2. Mixtral (MoE)
3. GraphRAG
4. Diffusion Transformers
5. s1 (Test-Time Compute)

### 更新日志

- **2025-01-04**: 初始版本，收录 120+ 篇论文

---

## 贡献

如发现链接失效或有新的重要论文推荐，欢迎提 Issue 或 PR。

## License

本索引文件采用 CC BY-NC-SA 4.0 协议。论文版权归原作者所有。
