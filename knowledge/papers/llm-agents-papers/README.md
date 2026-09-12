# LLM-Agents-Papers
## :writing_hand: Description
Last Updated Time: 2025/7/12

A repo lists papers related to LLM based agent. Includes
- [Survey](#Survey)
- [Technique For Enhancement](#Technique-For-Enhancement)
  - [Planning](#Planning)
  - [Memory Mechanism](#Memory-Mechanism)
  - [Feedback&Reflection](#FeedbackReflection)
  - [RAG](#RAG)
  - [Search](#Search)
- [Interaction](#Interaction)
  - [Role Playing](#Role-Playing)
  - [Conversation](#Conversation)
  - [Game Playing](#Game-Playing)
  - [Human-Agent Interaction](#Human-Agent-Interaction)
  - [Tool Usage](#Tool-Usage)
  - [Simulation](#Simulation)
- [Application](#Application)
  - [Math](#Math)
  - [Chemistry](#Chemistry)
  - [Biology](#Biology)
  - [Physics](#Physics)
  - [Geography](#Geography)
  - [Art](#Art)
  - [Medicine](#Medicine)
  - [Finance](#Finance)
  - [Software Engineering](#Software-Engineering)
  - [Research](#Research)
- [Automation](#Automation)
  - [Workflow](#Workflow)
  - [Automatic Evaluation](#Automatic-Evaluation)
- [Training](#Training)
  - [Fine tuning](#Fine-tuning)
  - [RL](#RL)
  - [DPO](#DPO)
- [Scaling](#Scaling)
  - [Single-Agent Framework](#Single-Agent-Framework)
  - [Multi-Agent System](#Multi-Agent-System)
- [Stability](#Stability)
  - [Safety](#Safety)
  - [Bias](#Bias)
  - [Hallucination](#Hallucination)
- [Infrastructure](#Infrastructure)
  - [Benchmark&Evaluation](#BenchmarkEvaluation)
  - [Environment&Platform](#EnvironmentPlatform)
  - [Dataset](#Dataset)
- [Others](#Others)
## :yellow_heart: Recommendation
For more comprehensive reading, we also recommend other paper lists:
* [zjunlp/LLMAgentPapers](https://github.com/zjunlp/LLMAgentPapers): Must-read Papers on Large Language Model Agents.
* [teacherpeterpan/self-correction-llm-papers](https://github.com/teacherpeterpan/self-correction-llm-papers): This is a collection of research papers for Self-Correcting Large Language Models with Automated Feedback.
* [Paitesanshi/LLM-Agent-Survey](https://github.com/Paitesanshi/LLM-Agent-Survey): A Survey on LLM-based Autonomous Agents.
* [woooodyy/llm-agent-paper-list](https://github.com/woooodyy/llm-agent-paper-list): Must-read papers for LLM-based agents.
* [git-disl/awesome-LLM-game-agent-papers](https://github.com/git-disl/awesome-LLM-game-agent-papers): Must-read papers for LLM-based Game agents.
## :newspaper: Papers
### Survey
- [2025/06/10] **Measuring Data Science Automation: A Survey of Evaluation Tools for AI Assistants and Agents** | [[paper]](https://arxiv.org/abs/2506.08800) | [code]

- [2025/06/06] **Evolutionary Perspectives on the Evaluation of LLM-Based AI Agents: A Comprehensive Survey** | [[paper]](https://arxiv.org/abs/2506.11102) | [code]

- [2025/05/27] **Creativity in LLM-based Multi-Agent Systems: A Survey** | [[paper]](https://arxiv.org/abs/2505.21116) | [code]

- [2025/05/24] **Multi-Party Conversational Agents: A Survey** | [[paper]](https://arxiv.org/abs/2505.18845) | [code]

- [2025/05/16] **A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?** | [[paper]](https://arxiv.org/abs/2505.10924) | [code]

- [2025/05/02] **AI agents may be worth the hype but not the resources (yet): An initial exploration of machine translation quality and costs in three language pairs in the legal and news domains** | [[paper]](https://arxiv.org/abs/2505.01560) | [code]

- [2025/05/01] **A Survey on Large Language Model based Human-Agent Systems** | [[paper]](https://arxiv.org/abs/2505.00753) | [[code]](https://github.com/HenryPengZou/Awesome-LLM-Based-Human-Agent-System-Papers)

- [2025/04/30] **Humanizing LLMs: A Survey of Psychological Measurements with Tools, Datasets, and Human-Agent Applications** | [[paper]](https://arxiv.org/abs/2505.00049) | [code]

- [2025/04/22] **A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment** | [[paper]](https://arxiv.org/abs/2504.15585) | [code]

- [2025/04/20] **Meta-Thinking in LLMs via Multi-Agent Reinforcement Learning: A Survey** | [[paper]](https://arxiv.org/abs/2504.14520) | [code]

- [2025/04/14] **A Survey of Large Language Model-Powered Spatial Intelligence Across Scales: Advances in Embodied Agents, Smart Cities, and Earth Science** | [[paper]](https://arxiv.org/abs/2504.09848) | [code]

- [2025/04/12] **A Survey of Frontiers in LLM Reasoning: Inference Scaling, Learning to Reason, and Agentic Systems** | [[paper]](https://arxiv.org/abs/2504.09037) | [code]

- [2025/03/28] **Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey** | [[paper]](https://arxiv.org/abs/2503.22458) | [code]

- [2025/03/27] **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** | [[paper]](https://arxiv.org/abs/2503.21460) | [code]

- [2025/03/27] **A Survey on (M)LLM-Based GUI Agents** | [[paper]](https://arxiv.org/abs/2504.13865) | [code]

- [2025/03/24] **A Survey of Large Language Model Agents for Question Answering** | [[paper]](https://arxiv.org/abs/2503.19213) | [code]

- [2025/03/20] **Survey on Evaluation of LLM-based Agents** | [[paper]](https://arxiv.org/abs/2503.16416) | [code]

- [2025/03/13] **LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems** | [[paper]](https://arxiv.org/abs/2504.01963) | [code]

- [2025/03/12] **Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions** | [[paper]](https://arxiv.org/abs/2503.08979) | [code]

- [2025/02/20] **Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2502.14321) | [code]

- [2025/02/18] **Towards a Design Guideline for RPA Evaluation: A Survey of Large Language Model-Based Role-Playing Agents** | [[paper]](https://arxiv.org/abs/2502.13012) | [code]

- [2025/02/16] **A Survey of LLM-based Agents in Medicine: How far are we from Baymax?** | [[paper]](https://arxiv.org/abs/2502.11211) | [code]

- [2025/01/15] **Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG** | [[paper]](https://arxiv.org/abs/2501.09136) | [code]

- [2024/12/23] **A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application** | [[paper]](https://arxiv.org/abs/2412.17481) | [code]

- [2024/12/18] **A Survey on Large Language Model-based Agents for Statistics and Data Science** | [[paper]](https://arxiv.org/abs/2412.14222) | [code]

- [2024/12/05] **A Survey on Large Language Model-Based Social Agents in Game-Theoretic Scenarios** | [[paper]](https://arxiv.org/abs/2412.03920) | [code]

- [2024/12/04] **From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents** | [[paper]](https://arxiv.org/abs/2412.03563) | [code]

- [2024/11/27] **Large Language Model-Brained GUI Agents: A Survey** | [[paper]](https://arxiv.org/abs/2411.18279) | [code]

- [2024/09/27] **A Survey on Complex Tasks for Goal-Directed Interactive Agents** | [[paper]](https://arxiv.org/abs/2409.18538) | [code]

- [2024/09/13] **Agents in Software Engineering: Survey, Landscape, and Vision** | [[paper]](https://arxiv.org/abs/2409.09030) | [code]

- [2024/09/04] **A Survey on Emergent Language** | [[paper]](https://arxiv.org/abs/2409.02645) | [code]

- [2024/08/05] **From LLMs to LLM-based Agents for Software Engineering: A Survey of Current, Challenges and Future** | [[paper]](https://arxiv.org/abs/2408.02479) | [code]

- [2024/07/26] **Large Language Model Agent in Financial Trading: A Survey** | [[paper]](https://arxiv.org/abs/2408.06361) | [code]

- [2024/06/03] **Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization** | [[paper]](https://arxiv.org/abs/2406.01171) | [[code]](https://github.com/miulab/personallm-survey)

- [2024/06/01] **Towards Rationality in Language and Multimodal Agents: A Survey** | [[paper]](https://arxiv.org/abs/2406.00252) | [code]

- [2024/04/17] **Advancing Social Intelligence in AI Agents: Technical Challenges and Open Questions** | [[paper]](https://arxiv.org/abs/2404.11023) | [code]

- [2024/04/02] **A Survey on Large Language Model-Based Game Agents** | [[paper]](https://arxiv.org/abs/2404.02039) | [[code]](https://github.com/git-disl/awesome-LLM-game-agent-papers)

- [2024/03/26] **Leveraging Large Language Models in Human-Robot Interaction: A Critical Analysis of Potential and Pitfalls** | [[paper]](https://arxiv.org/abs/2405.00693) | [code]

- [2024/03/07] **Promising and worth-to-try future directions for advancing state-of-the-art surrogates methods of agent-based models in social and health computational sciences** | [[paper]](https://arxiv.org/abs/2403.04417) | [code]

- [2024/02/28] **Large Language Models and Games: A Survey and Roadmap** | [[paper]](https://arxiv.org/abs/2402.18659) | [code]

- [2024/02/28] **A Survey on Recent Advances in LLM-Based Multi-turn Dialogue Systems** | [[paper]](https://arxiv.org/abs/2402.18013) | [code]

- [2024/02/05] **Understanding the planning of LLM agents: A survey** | [[paper]](https://arxiv.org/abs/2402.02716) | [code]

- [2024/01/01] **If LLM Is the Wizard, Then Code Is the Wand: A Survey on How Code Empowers Large Language Models to Serve as Intelligent Agents** | [[paper]](https://arxiv.org/abs/2401.00812) | [code]

- [2023/12/31] **A Survey of Personality, Persona, and Profile in Conversational Agents and Chatbots** | [[paper]](https://arxiv.org/abs/2401.00609) | [code]

- [2023/12/19] **Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives** | [[paper]](https://arxiv.org/abs/2312.11970) | [code]

- [2023/09/14] **The Rise and Potential of Large Language Model Based Agents: A Survey** | [[paper]](https://arxiv.org/abs/2309.07864) | [code]

- [2023/08/22] **A Survey on Large Language Model based Autonomous Agents** | [[paper]](https://arxiv.org/abs/2308.11432) | [code]

- [2023/06/27] **Next Steps for Human-Centered Generative AI: A Technical Perspective** | [[paper]](https://arxiv.org/abs/2306.15774) | [code]

---
### Technique For Enhancement
#### Planning
- [2025/06/30] **Thought-Augmented Planning for LLM-Powered Interactive Recommender Agent** | [[paper]](https://arxiv.org/abs/2506.23485) | [code]

- [2025/06/24] **NaviAgent: Bilevel Planning on Tool Dependency Graphs for Function Calling** | [[paper]](https://arxiv.org/abs/2506.19500) | [code]

- [2025/06/10] **Improving LLM Agent Planning with In-Context Learning via Atomic Fact Augmentation and Lookahead Search** | [[paper]](https://arxiv.org/abs/2506.09171) | [code]

- [2025/06/06] **MAPLE: Multi-Agent Adaptive Planning with Long-Term Memory for Table Reasoning** | [[paper]](https://arxiv.org/abs/2506.05813) | [code]

- [2025/05/22] **T1: A Tool-Oriented Conversational Dataset for Multi-Turn Agentic Planning** | [[paper]](https://arxiv.org/abs/2505.16986) | [code]

- [2025/05/02] **PIPA: A Unified Evaluation Protocol for Diagnosing Interactive Planning Agents** | [[paper]](https://arxiv.org/abs/2505.01592) | [code]

- [2025/04/15] **GraphicBench: A Planning Benchmark for Graphic Design with Language Agents** | [[paper]](https://arxiv.org/abs/2504.11571) | [code]

- [2025/03/12] **Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks** | [[paper]](https://arxiv.org/abs/2503.09572) | [code]

- [2025/03/04] **MPO: Boosting LLM Agents with Meta Plan Optimization** | [[paper]](https://arxiv.org/abs/2503.02682) | [code]

- [2025/03/03] **Improving Retrospective Language Agents via Joint Policy Gradient Optimization** | [[paper]](https://arxiv.org/abs/2503.01490) | [code]

- [2025/02/08] **CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging** | [[paper]](https://arxiv.org/abs/2502.05664) | [code]

- [2025/02/06] **Robotouille: An Asynchronous Planning Benchmark for LLM Agents** | [[paper]](https://arxiv.org/abs/2502.05227) | [code]

- [2025/01/27] **MADP: Multi-Agent Deductive Planning for Enhanced Cognitive-Behavioral Mental Health Question Answer** | [[paper]](https://arxiv.org/abs/2501.15826) | [code]

- [2025/01/14] **Talk to Right Specialists: Routing and Planning in Multi-agent System for Question Answering** | [[paper]](https://arxiv.org/abs/2501.07813) | [code]

- [2024/12/30] **Plancraft: an evaluation dataset for planning with LLM agents** | [[paper]](https://arxiv.org/abs/2412.21033) | [code]

- [2024/12/28] **Efficient Multi-Agent Collaboration with Tool Use for Online Planning in Complex Table Question Answering** | [[paper]](https://arxiv.org/abs/2412.20145) | [code]

- [2024/12/13] **Script-Based Dialog Policy Planning for LLM-Powered Conversational Agents: A Basic Architecture for an &#34;AI Therapist&#34;** | [[paper]](https://arxiv.org/abs/2412.15242) | [code]

- [2024/11/13] **One STEP at a time: Language Agents are Stepwise Planners** | [[paper]](https://arxiv.org/abs/2411.08432) | [code]

- [2024/11/05] **Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent** | [[paper]](https://arxiv.org/abs/2411.02937) | [code]

- [2024/10/12] **CAMPHOR: Collaborative Agents for Multi-input Planning and High-Order Reasoning On Device** | [[paper]](https://arxiv.org/abs/2410.09407) | [code]

- [2024/10/01] **Self-controller: Controlling LLMs with Multi-round Step-by-step Self-awareness** | [[paper]](https://arxiv.org/abs/2410.00359) | [code]

- [2024/09/30] **Interactive Speculative Planning: Enhance Agent Efficiency through Co-design of System and User Interface** | [[paper]](https://arxiv.org/abs/2410.00079) | [code]

- [2024/09/28] **SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models** | [[paper]](https://arxiv.org/abs/2409.19471) | [code]

- [2024/09/25] **MSI-Agent: Incorporating Multi-Scale Insight into Embodied Agents for Superior Planning and Decision-Making** | [[paper]](https://arxiv.org/abs/2409.16686) | [code]

- [2024/08/15] **VerilogCoder: Autonomous Verilog Coding Agents with Graph-based Planning and Abstract Syntax Tree (AST)-based Waveform Tracing Tool** | [[paper]](https://arxiv.org/abs/2408.08927) | [code]

- [2024/08/12] **Towards Autonomous Agents: Adaptive-planning, Reasoning, and Acting in Language Models** | [[paper]](https://arxiv.org/abs/2408.06458) | [code]

- [2024/08/01] **AgentGen: Enhancing Planning Abilities for Large Language Model based Agent via Environment and Task Generation** | [[paper]](https://arxiv.org/abs/2408.00764) | [code]

- [2024/07/04] **Controllable Conversations: Planning-Based Dialogue Agent with Large Language Models** | [[paper]](https://arxiv.org/abs/2407.03884) | [code]

- [2024/06/17] **RePrompt: Planning by Automatic Prompt Engineering for Large Language Models Agents** | [[paper]](https://arxiv.org/abs/2406.11132) | [code]

- [2024/06/09] **A Review of Prominent Paradigms for LLM-Based Agents: Tool Use (Including RAG), Planning, and Feedback Learning** | [[paper]](https://arxiv.org/abs/2406.05804) | [code]

- [2024/06/06] **Tool-Planner: Task Planning with Clusters across Multiple Tools** | [[paper]](https://arxiv.org/abs/2406.03807) | [[code]](https://github.com/OceannTwT/Tool-Planner)

- [2024/05/28] **A Human-Like Reasoning Framework for Multi-Phases Planning Task with Large Language Models** | [[paper]](https://arxiv.org/abs/2405.18208) | [code]

- [2024/05/27] **REVECA: Adaptive Planning and Trajectory-based Validation in Cooperative Language Agents using Information Relevance and Relative Proximity** | [[paper]](https://arxiv.org/abs/2405.16751) | [code]

- [2024/04/21] **Socratic Planner: Inquiry-Based Zero-Shot Planning for Embodied Instruction Following** | [[paper]](https://arxiv.org/abs/2404.15190) | [code]

- [2024/04/17] **The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey** | [[paper]](https://arxiv.org/abs/2404.11584) | [code]

- [2024/03/11] **Strength Lies in Differences! Improving Strategy Planning for Non-collaborative Dialogues via Diversified User Simulation** | [[paper]](https://arxiv.org/abs/2403.06769) | [code]

- [2024/03/10] **TRAD: Enhancing LLM Agents with Step-Wise Thought Retrieval and Aligned Decision** | [[paper]](https://arxiv.org/abs/2403.06221) | [code]

- [2024/03/05] **KnowAgent: Knowledge-Augmented Planning for LLM-Based Agents** | [[paper]](https://arxiv.org/abs/2403.03101) | [code]

- [2024/02/29] **PlanGPT: Enhancing Urban Planning with Tailored Language Model and Efficient Retrieval** | [[paper]](https://arxiv.org/abs/2402.19273) | [code]

- [2024/02/18] **What&#39;s the Plan? Evaluating and Developing Planning-Aware Techniques for Language Models** | [[paper]](https://arxiv.org/abs/2402.11489) | [code]

- [2024/02/18] **PreAct: Prediction Enhances Agent&#39;s Planning Ability** | [[paper]](https://arxiv.org/abs/2402.11534) | [code]

- [2024/02/16] **When is Tree Search Useful for LLM Planning? It Depends on the Discriminator** | [[paper]](https://arxiv.org/abs/2402.10890) | [[code]](https://github.com/osu-nlp-group/llm-planning-eval)

- [2024/02/15] **TDAG: A Multi-Agent Framework based on Dynamic Task Decomposition and Agent Generation** | [[paper]](https://arxiv.org/abs/2402.10178) | [code]

- [2024/02/09] **Introspective Planning: Aligning Robots&#39; Uncertainty with Inherent Task Ambiguity** | [[paper]](https://arxiv.org/abs/2402.06529) | [code]

- [2024/02/06] **RAP: Retrieval-Augmented Planning with Contextual Memory for Multimodal LLM Agents** | [[paper]](https://arxiv.org/abs/2402.03610) | [code]

- [2024/02/02] **TravelPlanner: A Benchmark for Real-World Planning with Language Agents** | [[paper]](https://arxiv.org/abs/2402.01622) | [[code]](https://github.com/OSU-NLP-Group/TravelPlanner)

- [2024/01/10] **AutoAct: Automatic Agent Learning from Scratch for QA via Self-Planning** | [[paper]](https://arxiv.org/abs/2401.05268) | [code]

- [2023/11/19] **TPTU-v2: Boosting Task Planning and Tool Usage of Large Language Model-based Agents in Real-world Systems** | [[paper]](https://arxiv.org/abs/2311.11315) | [code]

- [2023/10/12] **Tree-Planner: Efficient Close-loop Task Planning with Large Language Models** | [[paper]](https://arxiv.org/abs/2310.08582) | [code]

- [2023/10/09] **Put Your Money Where Your Mouth Is: Evaluating Strategic Planning and Execution of LLM Agents in an Auction Arena** | [[paper]](https://arxiv.org/abs/2310.05746) | [code]

- [2023/08/07] **TPTU: Large Language Model-based AI Agents for Task Planning and Tool Usage** | [[paper]](https://arxiv.org/abs/2308.03427) | [code]

- [2023/08/01] **SelfCheck: Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning** | [[paper]](https://arxiv.org/abs/2308.00436) | [code]

- [2023/05/26] **AdaPlanner: Adaptive Planning from Feedback with Language Models** | [[paper]](https://arxiv.org/abs/2305.16653) | [code]

- [2023/05/24] **Reasoning with Language Model is Planning with World Model** | [[paper]](https://arxiv.org/abs/2305.14992) | [code]

- [2023/05/24] **Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning** | [[paper]](https://arxiv.org/abs/2305.14909) | [[code]](https://github.com/GuanSuns/LLMs-World-Models-for-Planning)

- [2023/03/29] **Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks** | [[paper]](https://arxiv.org/abs/2303.16563) | [code]

- [2023/02/03] **Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents** | [[paper]](https://arxiv.org/abs/2302.01560) | [code]

- [2022/12/08] **LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models** | [[paper]](https://arxiv.org/abs/2212.04088) | [code]

#### Memory Mechanism
- [2025/07/10] **MIRIX: Multi-Agent Memory System for LLM-Based Agents** | [[paper]](https://arxiv.org/abs/2507.07957) | [code]

- [2025/07/07] **Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions** | [[paper]](https://arxiv.org/abs/2507.05257) | [code]

- [2025/07/03] **MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent** | [[paper]](https://arxiv.org/abs/2507.02259) | [code]

- [2025/06/30] **Ella: Embodied Social Agents with Lifelong Memory** | [[paper]](https://arxiv.org/abs/2506.24019) | [code]

- [2025/06/30] **State and Memory is All You Need for Robust and Reliable AI Agents** | [[paper]](https://arxiv.org/abs/2507.00081) | [code]

- [2025/06/20] **MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents** | [[paper]](https://arxiv.org/abs/2506.21605) | [code]

- [2025/06/18] **MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents** | [[paper]](https://arxiv.org/abs/2506.15841) | [code]

- [2025/06/17] **Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching** | [[paper]](https://arxiv.org/abs/2506.14852) | [code]

- [2025/06/09] **G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2506.07398) | [code]

- [2025/06/07] **Contextual Experience Replay for Self-Improvement of Language Agents** | [[paper]](https://arxiv.org/abs/2506.06698) | [code]

- [2025/06/06] **MAPLE: Multi-Agent Adaptive Planning with Long-Term Memory for Table Reasoning** | [[paper]](https://arxiv.org/abs/2506.05813) | [code]

- [2025/05/26] **Towards Multi-Granularity Memory Association and Selection for Long-Term Conversational Agents** | [[paper]](https://arxiv.org/abs/2505.19549) | [code]

- [2025/05/26] **Task Memory Engine: Spatial Memory for Robust Multi-Step LLM Agents** | [[paper]](https://arxiv.org/abs/2505.19436) | [code]

- [2025/05/23] **Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control** | [[paper]](https://arxiv.org/abs/2505.18279) | [code]

- [2025/05/22] **Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance** | [[paper]](https://arxiv.org/abs/2505.16348) | [code]

- [2025/04/30] **LLM-Empowered Embodied Agent for Memory-Augmented Task Planning in Household Robotics** | [[paper]](https://arxiv.org/abs/2504.21716) | [code]

- [2025/04/28] **Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory** | [[paper]](https://arxiv.org/abs/2504.19413) | [code]

- [2025/04/11] **Task Memory Engine (TME): A Structured Memory Framework with Graph-Aware Extensions for Multi-Step LLM Agent Tasks** | [[paper]](https://arxiv.org/abs/2504.08525) | [code]

- [2025/03/27] **MemInsight: Autonomous Memory Augmentation for LLM Agents** | [[paper]](https://arxiv.org/abs/2503.21760) | [code]

- [2025/03/25] **MARS: Memory-Enhanced Agents with Reflective Self-improvement** | [[paper]](https://arxiv.org/abs/2503.19271) | [code]

- [2025/03/11] **In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents** | [[paper]](https://arxiv.org/abs/2503.08026) | [code]

- [2025/02/17] **A-MEM: Agentic Memory for LLM Agents** | [[paper]](https://arxiv.org/abs/2502.12110) | [code]

- [2025/02/08] **On Memory Construction and Retrieval for Personalized Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.05589) | [code]

- [2025/01/20] **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** | [[paper]](https://arxiv.org/abs/2501.13956) | [code]

- [2025/01/15] **Doc-Guided Sent2Sent++: A Sent2Sent++ Agent with Doc-Guided memory for Document-level Machine Translation** | [[paper]](https://arxiv.org/abs/2501.08523) | [code]

- [2024/12/17] **On the Structural Memory of LLM Agents** | [[paper]](https://arxiv.org/abs/2412.15266) | [code]

- [2024/12/17] **Memory-Augmented Agent Training for Business Document Understanding** | [[paper]](https://arxiv.org/abs/2412.15274) | [code]

- [2024/10/10] **DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory** | [[paper]](https://arxiv.org/abs/2410.08143) | [code]

- [2024/09/28] **Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs** | [[paper]](https://arxiv.org/abs/2409.19401) | [code]

- [2024/09/11] **Agent Workflow Memory** | [[paper]](https://arxiv.org/abs/2409.07429) | [code]

- [2024/09/01] **Self-evolving Agents with reflective and memory-augmented abilities** | [[paper]](https://arxiv.org/abs/2409.00872) | [code]

- [2024/08/18] **HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model** | [[paper]](https://arxiv.org/abs/2408.09559) | [code]

- [2024/08/07] **Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks** | [[paper]](https://arxiv.org/abs/2408.03615) | [code]

- [2024/05/29] **Toward Conversational Agents with Context and Time Sensitive Long-term Memory** | [[paper]](https://arxiv.org/abs/2406.00057) | [[code]](https://github.com/Zyphra/TemporalMemoryDataset)

- [2024/04/15] **Memory Sharing for Large Language Model based Agents** | [[paper]](https://arxiv.org/abs/2404.09982) | [[code]](https://github.com/GHupppp/MemorySharingLLM)

- [2024/02/19] **Compress to Impress: Unleashing the Potential of Compressive Memory in Real-World Long-Term Conversations** | [[paper]](https://arxiv.org/abs/2402.11975) | [code]

- [2024/02/07] **InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory** | [[paper]](https://arxiv.org/abs/2402.04617) | [code]

- [2024/02/06] **RAP: Retrieval-Augmented Planning with Contextual Memory for Multimodal LLM Agents** | [[paper]](https://arxiv.org/abs/2402.03610) | [code]

- [2024/01/05] **From LLM to Conversational Agent: A Memory Enhanced Architecture with Fine-Tuning of Large Language Models** | [[paper]](https://arxiv.org/abs/2401.02777) | [code]

- [2023/12/22] **Empowering Working Memory for Large Language Model Agents** | [[paper]](https://arxiv.org/abs/2312.17259) | [code]

- [2023/12/22] **Personalized Large Language Model Assistant with Evolving Conditional Memory** | [[paper]](https://arxiv.org/abs/2312.17257) | [code]

- [2023/11/10] **JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models** | [[paper]](https://arxiv.org/abs/2311.05997) | [[code]](https://github.com/CraftJarvis/JARVIS-1)

- [2023/06/06] **ChatDB: Augmenting LLMs with Databases as Their Symbolic Memory** | [[paper]](https://arxiv.org/abs/2306.03901) | [code]

- [2023/05/23] **RET-LLM: Towards a General Read-Write Memory for Large Language Models** | [[paper]](https://arxiv.org/abs/2305.14322) | [code]

- [2023/05/17] **MemoryBank: Enhancing Large Language Models with Long-Term Memory** | [[paper]](https://arxiv.org/abs/2305.10250) | [code]

- [2023/05/02] **The Role of Summarization in Generative Agents: A Preliminary Perspective** | [[paper]](https://arxiv.org/abs/2305.01253) | [code]

- [2023/05/01] **Learning to Reason and Memorize with Self-Notes** | [[paper]](https://arxiv.org/abs/2305.00833) | [code]

- [2023/04/26] **Enhancing Large Language Model with Self-Controlled Memory Framework** | [[paper]](https://arxiv.org/abs/2304.13343) | [code]

- [2023/04/21] **Emergent and Predictable Memorization in Large Language Models** | [[paper]](https://arxiv.org/abs/2304.11158) | [code]

#### Feedback&Reflection
- [2025/07/08] **Conditional Multi-Stage Failure Recovery for Embodied Agents** | [[paper]](https://arxiv.org/abs/2507.06016) | [code]

- [2025/06/10] **Reinforce LLM Reasoning through Multi-Agent Reflection** | [[paper]](https://arxiv.org/abs/2506.08379) | [code]

- [2025/06/04] **Debate, Reflect, and Distill: Multi-Agent Feedback with Tree-Structured Preference Optimization for Efficient Language Model Enhancement** | [[paper]](https://arxiv.org/abs/2506.03541) | [code]

- [2025/06/04] **Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning** | [[paper]](https://arxiv.org/abs/2506.03939) | [code]

- [2025/06/03] **Mitigating Manipulation and Enhancing Persuasion: A Reflective Multi-Agent Approach for Legal Argument Generation** | [[paper]](https://arxiv.org/abs/2506.02992) | [code]

- [2025/05/22] **Optimizing LLM-Based Multi-Agent System with Textual Feedback: A Case Study on Software Development** | [[paper]](https://arxiv.org/abs/2505.16086) | [code]

- [2025/05/21] **ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection** | [[paper]](https://arxiv.org/abs/2505.15182) | [code]

- [2025/05/21] **Aligning Dialogue Agents with Global Feedback via Large Language Model Reward Decomposition** | [[paper]](https://arxiv.org/abs/2505.15922) | [code]

- [2025/05/06] **FRAME: Feedback-Refined Agent Methodology for Enhancing Medical Research Insights** | [[paper]](https://arxiv.org/abs/2505.04649) | [code]

- [2025/04/26] **Stealing Creator&#39;s Workflow: A Creator-Inspired Agentic Framework with Iterative Feedback Loop for Improved Scientific Short-form Generation** | [[paper]](https://arxiv.org/abs/2504.18805) | [code]

- [2025/03/20] **The Lighthouse of Language: Enhancing LLM Agents via Critique-Guided Improvement** | [[paper]](https://arxiv.org/abs/2503.16024) | [code]

- [2025/03/11] **In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents** | [[paper]](https://arxiv.org/abs/2503.08026) | [code]

- [2025/03/04] **Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent** | [[paper]](https://arxiv.org/abs/2503.02519) | [code]

- [2025/03/03] **Improving Retrospective Language Agents via Joint Policy Gradient Optimization** | [[paper]](https://arxiv.org/abs/2503.01490) | [code]

- [2025/02/20] **STeCa: Step-level Trajectory Calibration for LLM Agent Learning** | [[paper]](https://arxiv.org/abs/2502.14276) | [[code]](https://github.com/WangHanLinHenry/STeCa)

- [2025/02/17] **Table-Critic: A Multi-Agent Framework for Collaborative Criticism and Refinement in Table Reasoning** | [[paper]](https://arxiv.org/abs/2502.11799) | [code]

- [2025/02/17] **A Study on Leveraging Search and Self-Feedback for Agent Reasoning** | [[paper]](https://arxiv.org/abs/2502.12094) | [code]

- [2025/02/03] **PlotGen: Multi-Agent LLM-based Scientific Data Visualization via Multimodal Feedback** | [[paper]](https://arxiv.org/abs/2502.00988) | [code]

- [2025/01/26] **Large Language Models as Theory of Mind Aware Generative Agents with Counterfactual Reflection** | [[paper]](https://arxiv.org/abs/2501.15355) | [code]

- [2025/01/23] **AgentRec: Agent Recommendation Using Sentence Embeddings Aligned to Human Feedback** | [[paper]](https://arxiv.org/abs/2501.13333) | [code]

- [2025/01/08] **InfiGUIAgent: A Multimodal Generalist GUI Agent with Native Reasoning and Reflection** | [[paper]](https://arxiv.org/abs/2501.04575) | [code]

- [2024/12/31] **Enhancing LLM Reasoning with Multi-Path Collaborative Reactive and Reflection agents** | [[paper]](https://arxiv.org/abs/2501.00430) | [code]

- [2024/12/22] **A Multi-AI Agent System for Autonomous Optimization of Agentic AI Solutions via Iterative Refinement and LLM-Driven Feedback Loops** | [[paper]](https://arxiv.org/abs/2412.17149) | [code]

- [2024/11/29] **Training Agents with Weakly Supervised Feedback from Large Language Models** | [[paper]](https://arxiv.org/abs/2411.19547) | [code]

- [2024/11/21] **Enhancing LLMs for Power System Simulations: A Feedback-driven Multi-agent Framework** | [[paper]](https://arxiv.org/abs/2411.16707) | [code]

- [2024/11/11] **Using Generative AI and Multi-Agents to Provide Automatic Feedback** | [[paper]](https://arxiv.org/abs/2411.07407) | [code]

- [2024/11/04] **Positive Experience Reflection for Agents in Interactive Text Environments** | [[paper]](https://arxiv.org/abs/2411.02223) | [code]

- [2024/10/29] **Enhancing Financial Question Answering with a Multi-Agent Reflection Framework** | [[paper]](https://arxiv.org/abs/2410.21741) | [code]

- [2024/10/28] **CRAT: A Multi-Agent Framework for Causality-Enhanced Reflective and Retrieval-Augmented Translation with Large Language Models** | [[paper]](https://arxiv.org/abs/2410.21067) | [code]

- [2024/10/25] **OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization** | [[paper]](https://arxiv.org/abs/2410.19609) | [code]

- [2024/10/23] **ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents** | [[paper]](https://arxiv.org/abs/2410.17657) | [code]

- [2024/10/20] **Training Language Models to Critique With Multi-agent Feedback** | [[paper]](https://arxiv.org/abs/2410.15287) | [code]

- [2024/10/16] **PRefLexOR: Preference-based Recursive Language Modeling for Exploratory Optimization of Reasoning and Agentic Thinking** | [[paper]](https://arxiv.org/abs/2410.12375) | [code]

- [2024/10/08] **DataEnvGym: Data Generation Agents in Teacher Environments with Student Feedback** | [[paper]](https://arxiv.org/abs/2410.06215) | [code]

- [2024/10/02] **ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning** | [[paper]](https://arxiv.org/abs/2410.02052) | [code]

- [2024/10/02] **RGD: Multi-LLM Based Agent Debugger via Refinement and Generation Guidance** | [[paper]](https://arxiv.org/abs/2410.01242) | [code]

- [2024/09/18] **MAgICoRe: Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning** | [[paper]](https://arxiv.org/abs/2409.12147) | [code]

- [2024/09/05] **E2CL: Exploration-based Error Correction Learning for Embodied Agents** | [[paper]](https://arxiv.org/abs/2409.03256) | [[code]](https://github.com/WangHanLinHenry/E2CL)

- [2024/09/01] **Self-evolving Agents with reflective and memory-augmented abilities** | [[paper]](https://arxiv.org/abs/2409.00872) | [code]

- [2024/08/30] **Tool-Assisted Agent on SQL Inspection and Refinement in Real-World Scenarios** | [[paper]](https://arxiv.org/abs/2408.16991) | [code]

- [2024/08/15] **MAG-SQL: Multi-Agent Generative Approach with Soft Schema Linking and Iterative Sub-SQL Refinement for Text-to-SQL** | [[paper]](https://arxiv.org/abs/2408.07930) | [code]

- [2024/07/25] **Recursive Introspection: Teaching Language Model Agents How to Self-Improve** | [[paper]](https://arxiv.org/abs/2407.18219) | [code]

- [2024/06/09] **A Review of Prominent Paradigms for LLM-Based Agents: Tool Use (Including RAG), Planning, and Feedback Learning** | [[paper]](https://arxiv.org/abs/2406.05804) | [code]

- [2024/06/05] **LLM-based Rewriting of Inappropriate Argumentation using Reinforcement Learning from Machine Feedback** | [[paper]](https://arxiv.org/abs/2406.03363) | [code]

- [2024/06/03] **Re-ReST: Reflection-Reinforced Self-Training for Language Agents** | [[paper]](https://arxiv.org/abs/2406.01495) | [[code]](https://github.com/PlusLabNLP/Re-ReST)

- [2024/03/18] **QueryAgent: A Reliable and Efficient Reasoning Framework with Environmental Feedback-based Self-Correction** | [[paper]](https://arxiv.org/abs/2403.11886) | [code]

- [2024/03/17] **Improving Dialogue Agents by Decomposing One Global Explicit Annotation with Local Implicit Multimodal Feedback** | [[paper]](https://arxiv.org/abs/2403.11330) | [code]

- [2024/03/08] **ChatASU: Evoking LLM&#39;s Reflexion to Truly Understand Aspect Sentiment in Dialogues** | [[paper]](https://arxiv.org/abs/2403.05326) | [code]

- [2024/03/04] **Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents** | [[paper]](https://arxiv.org/abs/2403.02502) | [code]

- [2024/02/27] **Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization** | [[paper]](https://arxiv.org/abs/2402.17574) | [code]

- [2024/02/26] **SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection** | [[paper]](https://arxiv.org/abs/2402.16705) | [code]

- [2024/02/22] **Mirror: A Multiple-perspective Self-Reflection Method for Knowledge-rich Reasoning** | [[paper]](https://arxiv.org/abs/2402.14963) | [code]

- [2024/02/19] **A Critical Evaluation of AI Feedback for Aligning Large Language Models** | [[paper]](https://arxiv.org/abs/2402.12366) | [code]

- [2024/02/06] **AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Calls** | [[paper]](https://arxiv.org/abs/2402.04253) | [[code]](https://github.com/dyabel/anytool)

- [2024/02/02] **StepCoder: Improve Code Generation with Reinforcement Learning from Compiler Feedback** | [[paper]](https://arxiv.org/abs/2402.01391) | [code]

- [2023/11/14] **The ART of LLM Refinement: Ask, Refine, and Trust** | [[paper]](https://arxiv.org/abs/2311.07961) | [code]

- [2023/10/31] **Learning From Mistakes Makes LLM Better Reasoner** | [[paper]](https://arxiv.org/abs/2310.20689) | [code]

- [2023/10/12] **A Zero-Shot Language Agent for Computer Control with Structured Reflection** | [[paper]](https://arxiv.org/abs/2310.08740) | [code]

- [2023/07/27] **PanGu-Coder2: Boosting Large Language Models for Code with Ranking Feedback** | [[paper]](https://arxiv.org/abs/2307.14936) | [code]

- [2023/05/22] **Making Language Models Better Tool Learners with Execution Feedback** | [[paper]](https://arxiv.org/abs/2305.13068) | [code]

- [2023/05/17] **Improving Language Model Negotiation with Self-Play and In-Context Learning from AI Feedback** | [[paper]](https://arxiv.org/abs/2305.10142) | [code]

- [2023/04/21] **Improving Grounded Language Understanding in a Collaborative Environment by Interacting with Agents Through Help Feedback** | [[paper]](https://arxiv.org/abs/2304.10750) | [code]

- [2023/04/11] **Teaching Large Language Models to Self-Debug** | [[paper]](https://arxiv.org/abs/2304.05128) | [code]

- [2023/03/30] **Self-Refine: Iterative Refinement with Self-Feedback** | [[paper]](https://arxiv.org/abs/2303.17651) | [code]

#### RAG
- [2025/07/09] **Multi-Agent Retrieval-Augmented Framework for Evidence-Based Counterspeech Against Health Misinformation** | [[paper]](https://arxiv.org/abs/2507.07307) | [code]

- [2025/07/04] **AI-VaxGuide: An Agentic RAG-Based LLM for Vaccination Decisions** | [[paper]](https://arxiv.org/abs/2507.03493) | [code]

- [2025/06/28] **Knowledge Augmented Finetuning Matters in both RAG and Agent Based Dialog Systems** | [[paper]](https://arxiv.org/abs/2506.22852) | [code]

- [2025/06/27] **ARAG: Agentic Retrieval Augmented Generation for Personalized Recommendation** | [[paper]](https://arxiv.org/abs/2506.21931) | [code]

- [2025/06/12] **CIIR@LiveRAG 2025: Optimizing Multi-Agent Retrieval Augmented Generation through Self-Training** | [[paper]](https://arxiv.org/abs/2506.10844) | [code]

- [2025/06/04] **Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning** | [[paper]](https://arxiv.org/abs/2506.03939) | [code]

- [2025/05/28] **Agent-UniRAG: A Trainable Open-Source LLM Agent Framework for Unified Retrieval-Augmented Generation Systems** | [[paper]](https://arxiv.org/abs/2505.22571) | [code]

- [2025/05/26] **MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning** | [[paper]](https://arxiv.org/abs/2505.20096) | [code]

- [2025/05/22] **O$^2$-Searcher: A Searching-based Agent Model for Open-Domain Open-Ended Question Answering** | [[paper]](https://arxiv.org/abs/2505.16582) | [code]

- [2025/05/22] **Personalizing Student-Agent Interactions Using Log-Contextualized Retrieval Augmented Generation (RAG)** | [[paper]](https://arxiv.org/abs/2505.17238) | [code]

- [2025/05/22] **Search Wisely: Mitigating Sub-optimal Agentic Searches By Reducing Uncertainty** | [[paper]](https://arxiv.org/abs/2505.17281) | [code]

- [2025/05/21] **InfoDeepSeek: Benchmarking Agentic Information Seeking for Retrieval-Augmented Generation** | [[paper]](https://arxiv.org/abs/2505.15872) | [code]

- [2025/05/13] **ALOHA: Empowering Multilingual Agent for University Orientation with Hierarchical Retrieval** | [[paper]](https://arxiv.org/abs/2505.08130) | [code]

- [2025/05/12] **Reinforced Internal-External Knowledge Synergistic Reasoning for Efficient Adaptive Search Agent** | [[paper]](https://arxiv.org/abs/2505.07596) | [code]

- [2025/04/30] **Talk Before You Retrieve: Agent-Led Discussions for Better RAG in Medical QA** | [[paper]](https://arxiv.org/abs/2504.21252) | [code]

- [2025/04/24] **A RAG-Based Multi-Agent LLM System for Natural Hazard Resilience and Adaptation** | [[paper]](https://arxiv.org/abs/2504.17200) | [code]

- [2025/04/15] **Towards Automated Safety Requirements Derivation Using Agent-based RAG** | [[paper]](https://arxiv.org/abs/2504.11243) | [code]

- [2025/04/13] **HM-RAG: Hierarchical Multi-Agent Multimodal Retrieval Augmented Generation** | [[paper]](https://arxiv.org/abs/2504.12330) | [code]

- [2025/04/11] **TP-RAG: Benchmarking Retrieval-Augmented Large Language Model Agents for Spatiotemporal-Aware Travel Planning** | [[paper]](https://arxiv.org/abs/2504.08694) | [code]

- [2025/04/10] **CollEX -- A Multimodal Agentic RAG System Enabling Interactive Exploration of Scientific Collections** | [[paper]](https://arxiv.org/abs/2504.07643) | [code]

- [2025/03/18] **Retrieval-Augmented Simulacra: Generative Agents for Up-to-date and Knowledge-Adaptive Simulations** | [[paper]](https://arxiv.org/abs/2503.14620) | [code]

- [2025/03/14] **RAG-KG-IL: A Multi-Agent Hybrid Framework for Reducing Hallucinations and Enhancing LLM Reasoning through RAG and Incremental Knowledge Graph Learning Integration** | [[paper]](https://arxiv.org/abs/2503.13514) | [code]

- [2025/03/01] **EXCLAIM: An Explainable Cross-Modal Agentic System for Misinformation Detection with Hierarchical Retrieval** | [[paper]](https://arxiv.org/abs/2504.06269) | [code]

- [2025/02/25] **ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents** | [[paper]](https://arxiv.org/abs/2502.18017) | [code]

- [2025/02/19] **RAG-Gym: Optimizing Reasoning and Search Agents with Process Supervision** | [[paper]](https://arxiv.org/abs/2502.13957) | [code]

- [2025/02/08] **On Memory Construction and Retrieval for Personalized Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.05589) | [code]

- [2025/02/06] **Enhancing Online Learning Efficiency Through Heterogeneous Resource Integration with a Multi-Agent RAG System** | [[paper]](https://arxiv.org/abs/2502.03948) | [code]

- [2025/01/25] **Improving Retrieval-Augmented Generation through Multi-Agent Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2501.15228) | [code]

- [2024/12/31] **MAIN-RAG: Multi-Agent Filtering Retrieval-Augmented Generation** | [[paper]](https://arxiv.org/abs/2501.00332) | [code]

- [2024/12/24] **GeAR: Graph-enhanced Agent for Retrieval-augmented Generation** | [[paper]](https://arxiv.org/abs/2412.18431) | [code]

- [2024/12/20] **Towards Interpretable Radiology Report Generation via Concept Bottlenecks using a Multi-Agentic RAG** | [[paper]](https://arxiv.org/abs/2412.16086) | [code]

- [2024/12/16] **BioRAGent: A Retrieval-Augmented Generation System for Showcasing Generative Query Expansion and Domain-Specific Search for Scientific Q&amp;A** | [[paper]](https://arxiv.org/abs/2412.12358) | [code]

- [2024/12/07] **SLA Management in Reconfigurable Multi-Agent RAG: A Systems Approach to Question Answering** | [[paper]](https://arxiv.org/abs/2412.06832) | [code]

- [2024/11/05] **Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent** | [[paper]](https://arxiv.org/abs/2411.02937) | [code]

- [2024/10/28] **CRAT: A Multi-Agent Framework for Causality-Enhanced Reflective and Retrieval-Augmented Translation with Large Language Models** | [[paper]](https://arxiv.org/abs/2410.21067) | [code]

- [2024/10/18] **Toolshed: Scale Tool-Equipped Agents with Advanced RAG-Tool Fusion and Tool Knowledge Bases** | [[paper]](https://arxiv.org/abs/2410.14594) | [code]

- [2024/10/01] **Conversational Exploratory Search of Scholarly Publications Using Knowledge Graphs** | [[paper]](https://arxiv.org/abs/2410.00427) | [code]

- [2024/09/28] **Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs** | [[paper]](https://arxiv.org/abs/2409.19401) | [code]

- [2024/08/18] **Agentic Retrieval-Augmented Generation for Time Series Analysis** | [[paper]](https://arxiv.org/abs/2408.14484) | [code]

- [2024/08/05] **LLM Agents Improve Semantic Code Search** | [[paper]](https://arxiv.org/abs/2408.11058) | [code]

- [2024/08/03] **MALADE: Orchestration of LLM-powered Agents with Retrieval Augmented Generation for Pharmacovigilance** | [[paper]](https://arxiv.org/abs/2408.01869) | [code]

- [2024/07/20] **Golden-Retriever: High-Fidelity Agentic Retrieval Augmented Generation for Industrial Knowledge Base** | [[paper]](https://arxiv.org/abs/2408.00798) | [code]

- [2024/06/26] **Geode: A Zero-shot Geospatial Question-Answering Agent with Explicit Reasoning and Precise Spatio-Temporal Retrieval** | [[paper]](https://arxiv.org/abs/2407.11014) | [code]

- [2024/06/19] **StackRAG Agent: Improving Developer Answers with Retrieval-Augmented Generation** | [[paper]](https://arxiv.org/abs/2406.13840) | [code]

- [2024/06/09] **A Review of Prominent Paradigms for LLM-Based Agents: Tool Use (Including RAG), Planning, and Feedback Learning** | [[paper]](https://arxiv.org/abs/2406.05804) | [code]

- [2024/03/05] **AgentsCourt: Building Judicial Decision-Making Agents with Court Debate Simulation and Legal Knowledge Augmentation** | [[paper]](https://arxiv.org/abs/2403.02959) | [code]

- [2024/02/06] **RAP: Retrieval-Augmented Planning with Contextual Memory for Multimodal LLM Agents** | [[paper]](https://arxiv.org/abs/2402.03610) | [code]

- [2023/12/27] **Automating Knowledge Acquisition for Content-Centric Cognitive Agents Using LLMs** | [[paper]](https://arxiv.org/abs/2312.16378) | [code]

#### Search
- [2025/06/09] **CheMatAgent: Enhancing LLMs for Chemistry and Materials Science through Tree-Search Based Tool Learning** | [[paper]](https://arxiv.org/abs/2506.07551) | [code]

- [2025/06/06] **AgentSwift: Efficient LLM Agent Design via Value-guided Hierarchical Search** | [[paper]](https://arxiv.org/abs/2506.06017) | [code]

- [2025/05/26] **T^2Agent A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search** | [[paper]](https://arxiv.org/abs/2505.19768) | [code]

- [2025/05/12] **Structural Entropy Guided Agent for Detecting and Repairing Knowledge Deficiencies in LLMs** | [[paper]](https://arxiv.org/abs/2505.07184) | [code]

- [2025/04/10] **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** | [[paper]](https://arxiv.org/abs/2504.08066) | [code]

- [2025/04/04] **SynWorld: Virtual Scenario Synthesis for Agentic Action Knowledge Refinement** | [[paper]](https://arxiv.org/abs/2504.03561) | [code]

- [2025/03/18] **DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performance by Adaptive Tree Traversal** | [[paper]](https://arxiv.org/abs/2503.14269) | [code]

- [2025/02/20] **I-MCTS: Enhancing Agentic AutoML via Introspective Monte Carlo Tree Search** | [[paper]](https://arxiv.org/abs/2502.14693) | [code]

- [2025/02/18] **R2-KG: General-Purpose Dual-Agent Framework for Reliable Reasoning on Knowledge Graphs** | [[paper]](https://arxiv.org/abs/2502.12767) | [code]

- [2025/02/18] **Agentic Deep Graph Reasoning Yields Self-Organizing Knowledge Networks** | [[paper]](https://arxiv.org/abs/2502.13025) | [code]

- [2025/02/17] **A Study on Leveraging Search and Self-Feedback for Agent Reasoning** | [[paper]](https://arxiv.org/abs/2502.12094) | [code]

- [2025/02/05] **SymAgent: A Neural-Symbolic Self-Learning Agent Framework for Complex Reasoning over Knowledge Graphs** | [[paper]](https://arxiv.org/abs/2502.03283) | [code]

- [2025/02/02] **Efficient Multi-Agent System Training with Data Influence-Oriented Tree Search** | [[paper]](https://arxiv.org/abs/2502.00955) | [code]

- [2025/01/31] **KBQA-o1: Agentic Knowledge Base Question Answering with Monte Carlo Tree Search** | [[paper]](https://arxiv.org/abs/2501.18922) | [code]

- [2025/01/09] **Search-o1: Agentic Search-Enhanced Large Reasoning Models** | [[paper]](https://arxiv.org/abs/2501.05366) | [code]

- [2024/12/24] **A Novel Task-Driven Method with Evolvable Interactive Agents Using Event Trees for Enhanced Emergency Decision Support** | [[paper]](https://arxiv.org/abs/2501.06193) | [code]

- [2024/12/22] **Multi-Agent Sampling: Scaling Inference Compute for Data Synthesis with Tree Search-Based Agentic Collaboration** | [[paper]](https://arxiv.org/abs/2412.17061) | [code]

- [2024/12/05] **Agent AI with LangGraph: A Modular Framework for Enhancing Machine Translation Using Large Language Models** | [[paper]](https://arxiv.org/abs/2412.03801) | [code]

- [2024/11/07] **CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models** | [[paper]](https://arxiv.org/abs/2411.04329) | [code]

- [2024/10/29] **Synergizing LLM Agents and Knowledge Graph for Socioeconomic Prediction in LBSN** | [[paper]](https://arxiv.org/abs/2411.00028) | [code]

- [2024/10/25] **AGENT-CQ: Automatic Generation and Evaluation of Clarifying Questions for Conversational Search with LLMs** | [[paper]](https://arxiv.org/abs/2410.19692) | [code]

- [2024/10/22] **SELA: Tree-Search Enhanced LLM Agents for Automated Machine Learning** | [[paper]](https://arxiv.org/abs/2410.17238) | [code]

- [2024/10/13] **Expanding Search Space with Diverse Prompting Agents: An Efficient Sampling Approach for LLM Mathematical Reasoning** | [[paper]](https://arxiv.org/abs/2410.09780) | [code]

- [2024/10/13] **LLM-Based Multi-Agent Systems are Scalable Graph Generative Models** | [[paper]](https://arxiv.org/abs/2410.09824) | [code]

- [2024/10/02] **ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning** | [[paper]](https://arxiv.org/abs/2410.02052) | [code]

- [2024/09/09] **SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning** | [[paper]](https://arxiv.org/abs/2409.05556) | [code]

- [2024/07/01] **Tree Search for Language Model Agents** | [[paper]](https://arxiv.org/abs/2407.01476) | [code]

- [2024/06/17] **Input Conditioned Graph Generation for Language Agents** | [[paper]](https://arxiv.org/abs/2406.11555) | [[code]](https://github.com/lukasvierling/dynamicgptswarm)

- [2024/02/17] **KG-Agent: An Efficient Autonomous Agent Framework for Complex Reasoning over Knowledge Graph** | [[paper]](https://arxiv.org/abs/2402.11163) | [code]

- [2024/02/16] **When is Tree Search Useful for LLM Planning? It Depends on the Discriminator** | [[paper]](https://arxiv.org/abs/2402.10890) | [[code]](https://github.com/osu-nlp-group/llm-planning-eval)

- [2024/02/09] **CoSearchAgent: A Lightweight Collaborative Search Agent with Large Language Models** | [[paper]](https://arxiv.org/abs/2402.06360) | [code]

- [2023/05/17] **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** | [[paper]](https://arxiv.org/abs/2305.10601) | [code]

### Interaction
#### Role Playing
- [2025/06/28] **Agent-to-Agent Theory of Mind: Testing Interlocutor Awareness among Large Language Models** | [[paper]](https://arxiv.org/abs/2506.22957) | [code]

- [2025/06/24] **MAM: Modular Multi-Agent Framework for Multi-Modal Medical Diagnosis via Role-Specialized Collaboration** | [[paper]](https://arxiv.org/abs/2506.19835) | [code]

- [2025/06/20] **Language-Informed Synthesis of Rational Agent Models for Grounded Theory-of-Mind Reasoning On-The-Fly** | [[paper]](https://arxiv.org/abs/2506.16755) | [code]

- [2025/06/06] **PersonaAgent: When Large Language Model Agents Meet Personalization at Test Time** | [[paper]](https://arxiv.org/abs/2506.06254) | [code]

- [2025/06/02] **Thinking in Character: Advancing Role-Playing Agents with Role-Aware Reasoning** | [[paper]](https://arxiv.org/abs/2506.01748) | [code]

- [2025/05/30] **Context-Aware Sentiment Forecasting via LLM-based Multi-Perspective Role-Playing Agents** | [[paper]](https://arxiv.org/abs/2505.24331) | [code]

- [2025/05/29] **ChARM: Character-based Act-adaptive Reward Modeling for Advanced Role-Playing Language Agents** | [[paper]](https://arxiv.org/abs/2505.23923) | [code]

- [2025/05/26] **OmniCharacter: Towards Immersive Role-Playing Agents with Seamless Speech-Language Personality Interaction** | [[paper]](https://arxiv.org/abs/2505.20277) | [code]

- [2025/05/20] **Inter(sectional) Alia(s): Ambiguity in Voice Agent Identity via Intersectional Japanese Self-Referents** | [[paper]](https://arxiv.org/abs/2506.01998) | [code]

- [2025/04/29] **BrAIcht, a theatrical agent that speaks like Bertolt Brecht&#39;s characters** | [[paper]](https://arxiv.org/abs/2504.20552) | [code]

- [2025/04/25] **Exploring Personality-Aware Interactions in Salesperson Dialogue Agents** | [[paper]](https://arxiv.org/abs/2504.18058) | [code]

- [2025/04/13] **UXAgent: A System for Simulating Usability Testing of Web Design with LLM Agents** | [[paper]](https://arxiv.org/abs/2504.09407) | [code]

- [2025/04/03] **LLMs as Deceptive Agents: How Role-Based Prompting Induces Semantic Ambiguity in Puzzle Tasks** | [[paper]](https://arxiv.org/abs/2504.02254) | [code]

- [2025/03/14] **AIstorian lets AI be a historian: A KG-powered multi-agent system for accurate biography generation** | [[paper]](https://arxiv.org/abs/2503.11346) | [code]

- [2025/02/20] **InstructAgent: Building User Controllable Recommender via LLM Agent** | [[paper]](https://arxiv.org/abs/2502.14662) | [code]

- [2025/02/18] **SEFL: Harnessing Large Language Model Agents to Improve Educational Feedback Systems** | [[paper]](https://arxiv.org/abs/2502.12927) | [code]

- [2025/02/17] **Can LLM Agents Maintain a Persona in Discourse?** | [[paper]](https://arxiv.org/abs/2502.11843) | [code]

- [2025/02/17] **LM Agents for Coordinating Multi-User Information Gathering** | [[paper]](https://arxiv.org/abs/2502.12328) | [code]

- [2025/02/16] **SCALE: Towards Collaborative Content Analysis in Social Science with Large Language Model Agents and Human Intervention** | [[paper]](https://arxiv.org/abs/2502.10937) | [code]

- [2025/02/13] **Language Agents as Digital Representatives in Collective Decision-Making** | [[paper]](https://arxiv.org/abs/2502.09369) | [code]

- [2025/02/06] **PsyPlay: Personality-Infused Role-Playing Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.03821) | [code]

- [2025/02/03] **Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant** | [[paper]](https://arxiv.org/abs/2502.01390) | [code]

- [2025/01/23] **AgentRec: Agent Recommendation Using Sentence Embeddings Aligned to Human Feedback** | [[paper]](https://arxiv.org/abs/2501.13333) | [code]

- [2025/01/15] **Personality Modeling for Persuasion of Misinformation using AI Agent** | [[paper]](https://arxiv.org/abs/2501.08985) | [code]

- [2024/12/28] **BaiJia: A Large-Scale Role-Playing Agent Corpus of Chinese Historical Characters** | [[paper]](https://arxiv.org/abs/2412.20024) | [code]

- [2024/12/22] **Modular Conversational Agents for Surveys and Interviews** | [[paper]](https://arxiv.org/abs/2412.17049) | [code]

- [2024/12/11] **SweetieChat: A Strategy-Enhanced Role-playing Framework for Diverse Scenarios Handling Emotional Support Agent** | [[paper]](https://arxiv.org/abs/2412.08389) | [code]

- [2024/12/10] **My Words Imply Your Opinion: Reader Agent-Based Propagation Enhancement for Personalized Implicit Emotion Analysis** | [[paper]](https://arxiv.org/abs/2412.07367) | [code]

- [2024/11/21] **Towards Full Delegation: Designing Ideal Agentic Behaviors for Travel Planning** | [[paper]](https://arxiv.org/abs/2411.13904) | [code]

- [2024/11/19] **Probing the Capacity of Language Model Agents to Operationalize Disparate Experiential Context Despite Distraction** | [[paper]](https://arxiv.org/abs/2411.12828) | [code]

- [2024/11/12] **SHARP: Unlocking Interactive Hallucination via Stance Transfer in Role-Playing Agents** | [[paper]](https://arxiv.org/abs/2411.07965) | [code]

- [2024/11/04] **A Multi-Task Role-Playing Agent Capable of Imitating Character Linguistic Styles** | [[paper]](https://arxiv.org/abs/2411.02457) | [code]

- [2024/10/28] **Guide-LLM: An Embodied LLM Agent and Text-Based Topological Map for Robotic Guidance of People with Visual Impairments** | [[paper]](https://arxiv.org/abs/2410.20666) | [code]

- [2024/10/24] **Schema-Guided Culture-Aware Complex Event Simulation with Multi-Agent Role-Play** | [[paper]](https://arxiv.org/abs/2410.18935) | [code]

- [2024/09/23] **ERABAL: Enhancing Role-Playing Agents through Boundary-Aware Learning** | [[paper]](https://arxiv.org/abs/2409.14710) | [code]

- [2024/09/19] **FoodPuzzle: Developing Large Language Model Agents as Flavor Scientists** | [[paper]](https://arxiv.org/abs/2409.12832) | [code]

- [2024/09/12] **TravelAgent: An AI Assistant for Personalized Travel Planning** | [[paper]](https://arxiv.org/abs/2409.08069) | [code]

- [2024/09/11] **Using Generative Agents to Create Tip Sheets for Investigative Data Reporting** | [[paper]](https://arxiv.org/abs/2409.07286) | [code]

- [2024/08/28] **Interactive Agents: Simulating Counselor-Client Psychological Counseling via Role-Playing LLM-to-LLM Interactions** | [[paper]](https://arxiv.org/abs/2408.15787) | [code]

- [2024/08/21] **Drama Engine: A Framework for Narrative Agents** | [[paper]](https://arxiv.org/abs/2408.11574) | [code]

- [2024/06/24] **The Effects of Embodiment and Personality Expression on Learning in LLM-based Educational Agents** | [[paper]](https://arxiv.org/abs/2407.10993) | [code]

- [2024/06/17] **HoLLMwood: Unleashing the Creativity of Large Language Models in Screenwriting via Role Playing** | [[paper]](https://arxiv.org/abs/2406.11683) | [code]

- [2024/06/11] **Agent-SiMT: Agent-assisted Simultaneous Machine Translation with Large Language Models** | [[paper]](https://arxiv.org/abs/2406.06910) | [code]

- [2024/06/09] **Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions** | [[paper]](https://arxiv.org/abs/2406.05688) | [[code]](https://github.com/chengtan9907/reviewmt)

- [2024/05/28] **TimeChara: Evaluating Point-in-Time Character Hallucination of Role-Playing Large Language Models** | [[paper]](https://arxiv.org/abs/2405.18027) | [code]

- [2024/05/10] **LLM Discussion: Enhancing the Creativity of Large Language Models via Discussion Framework and Role-Play** | [[paper]](https://arxiv.org/abs/2405.06373) | [code]

- [2024/05/08] **LLMs with Personalities in Multi-issue Negotiation Games** | [[paper]](https://arxiv.org/abs/2405.05248) | [code]

- [2024/05/06] **Large Language Models (LLMs) as Agents for Augmented Democracy** | [[paper]](https://arxiv.org/abs/2405.03452) | [code]

- [2024/05/02] **GAIA: A General AI Assistant for Intelligent Accelerator Operations** | [[paper]](https://arxiv.org/abs/2405.01359) | [code]

- [2024/05/01] **&#34;Ask Me Anything&#34;: How Comcast Uses LLMs to Assist Agents in Real Time** | [[paper]](https://arxiv.org/abs/2405.00801) | [code]

- [2024/04/26] **Large Language Model Agent as a Mechanical Designer** | [[paper]](https://arxiv.org/abs/2404.17525) | [code]

- [2024/04/19] **Cooperative Sentiment Agents for Multimodal Sentiment Analysis** | [[paper]](https://arxiv.org/abs/2404.12642) | [[code]](https://github.com/smwanghhh/co-sa)

- [2024/03/31] **DiffAgent: Fast and Accurate Text-to-Image API Selection with Large Language Model** | [[paper]](https://arxiv.org/abs/2404.01342) | [[code]](https://github.com/OpenGVLab/DiffAgent)

- [2024/03/23] **EduAgent: Generative Student Agents in Learning** | [[paper]](https://arxiv.org/abs/2404.07963) | [code]

- [2024/03/19] **Characteristic AI Agents via Large Language Models** | [[paper]](https://arxiv.org/abs/2403.12368) | [code]

- [2024/03/15] **VideoAgent: Long-form Video Understanding with Large Language Model as Agent** | [[paper]](https://arxiv.org/abs/2403.10517) | [code]

- [2024/03/13] **Evaluating Large Language Models as Generative User Simulators for Conversational Recommendation** | [[paper]](https://arxiv.org/abs/2403.09738) | [code]

- [2024/02/29] **On the Decision-Making Abilities in Role-Playing using Large Language Models** | [[paper]](https://arxiv.org/abs/2402.18807) | [code]

- [2024/02/28] **Prospect Personalized Recommendation on Large Language Model-based Agent Platform** | [[paper]](https://arxiv.org/abs/2402.18240) | [code]

- [2024/02/26] **Language Agents as Optimizable Graphs** | [[paper]](https://arxiv.org/abs/2402.16823) | [[code]](https://github.com/metauto-ai/gptswarm)

- [2024/02/22] **Triad: A Framework Leveraging a Multi-Role LLM-based Agent to Solve Knowledge Base Question Answering** | [[paper]](https://arxiv.org/abs/2402.14320) | [code]

- [2024/02/22] **Large Language Models as Urban Residents: An LLM Agent Framework for Personal Mobility Generation** | [[paper]](https://arxiv.org/abs/2402.14744) | [code]

- [2024/02/21] **Neeko: Leveraging Dynamic LoRA for Efficient Multi-Character Role-Playing Agent** | [[paper]](https://arxiv.org/abs/2402.13717) | [code]

- [2024/02/19] **Stick to your Role! Stability of Personal Values Expressed in Large Language Models** | [[paper]](https://arxiv.org/abs/2402.14846) | [code]

- [2024/02/18] **Modelling Political Coalition Negotiations Using LLM-based Agents** | [[paper]](https://arxiv.org/abs/2402.11712) | [code]

- [2024/02/06] **Professional Agents -- Evolving Large Language Models into Autonomous Experts with Human-Level Competencies** | [[paper]](https://arxiv.org/abs/2402.03628) | [code]

- [2024/02/06] **Can Generative Agents Predict Emotion?** | [[paper]](https://arxiv.org/abs/2402.04232) | [code]

- [2024/02/05] **GUARD: Role-playing to Generate Natural-language Jailbreakings to Test Guideline Adherence of Large Language Models** | [[paper]](https://arxiv.org/abs/2402.03299) | [code]

- [2024/01/31] **LLMs Simulate Big Five Personality Traits: Further Evidence** | [[paper]](https://arxiv.org/abs/2402.01765) | [code]

- [2023/12/22] **Personalized Large Language Model Assistant with Evolving Conditional Memory** | [[paper]](https://arxiv.org/abs/2312.17257) | [code]

- [2023/12/21] **ChatGPT as a commenter to the news: can LLMs generate human-like opinions?** | [[paper]](https://arxiv.org/abs/2312.13961) | [code]

- [2023/12/20] **Machine Mindset: An MBTI Exploration of Large Language Models** | [[paper]](https://arxiv.org/abs/2312.12999) | [code]

- [2023/12/19] **Can ChatGPT be Your Personal Medical Assistant?** | [[paper]](https://arxiv.org/abs/2312.12006) | [code]

- [2023/10/13] **AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems** | [[paper]](https://arxiv.org/abs/2310.09233) | [code]

- [2023/10/01] **RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models** | [[paper]](https://arxiv.org/abs/2310.00746) | [code]

- [2023/09/02] **ModelScope-Agent: Building Your Customizable Agent System with Open-source Large Language Models** | [[paper]](https://arxiv.org/abs/2309.00986) | [code]

- [2023/08/22] **Towards an On-device Agent for Text Rewriting** | [[paper]](https://arxiv.org/abs/2308.11807) | [code]

- [2023/08/10] **LLM As DBA** | [[paper]](https://arxiv.org/abs/2308.05481) | [code]

- [2023/08/03] **InterAct: Exploring the Potentials of ChatGPT as a Cooperative Agent** | [[paper]](https://arxiv.org/abs/2308.01552) | [code]

- [2023/07/11] **Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration** | [[paper]](https://arxiv.org/abs/2307.05300) | [code]

- [2023/07/05] **Building Cooperative Embodied Agents Modularly with Large Language Models** | [[paper]](https://arxiv.org/abs/2307.02485) | [code]

- [2023/05/25] **Role-Play with Large Language Models** | [[paper]](https://arxiv.org/abs/2305.16367) | [code]

- [2023/05/09] **TidyBot: Personalized Robot Assistance with Large Language Models** | [[paper]](https://arxiv.org/abs/2305.05658) | [code]

#### Conversation
- [2025/06/28] **Knowledge Augmented Finetuning Matters in both RAG and Agent Based Dialog Systems** | [[paper]](https://arxiv.org/abs/2506.22852) | [code]

- [2025/06/24] **Augmenting Multi-Agent Communication with State Delta Trajectory** | [[paper]](https://arxiv.org/abs/2506.19209) | [code]

- [2025/06/17] **From What to Respond to When to Respond: Timely Response Generation for Open-domain Dialogue Agents** | [[paper]](https://arxiv.org/abs/2506.14285) | [code]

- [2025/06/17] **Expectation Confirmation Preference Optimization for Multi-Turn Conversational Recommendation Agent** | [[paper]](https://arxiv.org/abs/2506.14302) | [code]

- [2025/06/13] **The Behavior Gap: Evaluating Zero-shot LLM Agents in Complex Task-Oriented Dialogs** | [[paper]](https://arxiv.org/abs/2506.12266) | [code]

- [2025/06/11] **Chat-of-Thought: Collaborative Multi-Agent System for Generating Domain Specific Information** | [[paper]](https://arxiv.org/abs/2506.10086) | [code]

- [2025/06/09] **$\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment** | [[paper]](https://arxiv.org/abs/2506.07982) | [code]

- [2025/06/04] **AI Agents for Conversational Patient Triage: Preliminary Simulation-Based Evaluation with Real-World EHR Data** | [[paper]](https://arxiv.org/abs/2506.04032) | [code]

- [2025/06/04] **CLAIM: An Intent-Driven Multi-Agent Framework for Analyzing Manipulation in Courtroom Dialogues** | [[paper]](https://arxiv.org/abs/2506.04131) | [code]

- [2025/05/29] **A Practical Approach for Building Production-Grade Conversational Agents with Workflow Graphs** | [[paper]](https://arxiv.org/abs/2505.23006) | [code]

- [2025/05/28] **ChatCFD: an End-to-End CFD Agent with Domain-specific Structured Thinking** | [[paper]](https://arxiv.org/abs/2506.02019) | [code]

- [2025/05/26] **Towards Multi-Granularity Memory Association and Selection for Long-Term Conversational Agents** | [[paper]](https://arxiv.org/abs/2505.19549) | [code]

- [2025/05/24] **Multi-Party Conversational Agents: A Survey** | [[paper]](https://arxiv.org/abs/2505.18845) | [code]

- [2025/05/21] **Aligning Dialogue Agents with Global Feedback via Large Language Model Reward Decomposition** | [[paper]](https://arxiv.org/abs/2505.15922) | [code]

- [2025/04/29] **BrAIcht, a theatrical agent that speaks like Bertolt Brecht&#39;s characters** | [[paper]](https://arxiv.org/abs/2504.20552) | [code]

- [2025/04/26] **MATCHA: Can Multi-Agent Collaboration Build a Trustworthy Conversational Recommender?** | [[paper]](https://arxiv.org/abs/2504.20094) | [code]

- [2025/04/21] **EducationQ: Evaluating LLMs&#39; Teaching Capabilities Through Multi-Agent Dialogue Framework** | [[paper]](https://arxiv.org/abs/2504.14928) | [code]

- [2025/04/20] **DialogueAgents: A Hybrid Agent-Based Speech Synthesis Framework for Multi-Party Dialogue** | [[paper]](https://arxiv.org/abs/2504.14482) | [code]

- [2025/04/12] **A Multi-view Discourse Framework for Integrating Semantic and Syntactic Features in Dialog Agents** | [[paper]](https://arxiv.org/abs/2504.09073) | [code]

- [2025/04/07] **Bridging Industrial Expertise and XR with LLM-Powered Conversational Agents** | [[paper]](https://arxiv.org/abs/2504.05527) | [code]

- [2025/04/07] **A Desideratum for Conversational Agents: Capabilities, Challenges, and Future Directions** | [[paper]](https://arxiv.org/abs/2504.16939) | [code]

- [2025/03/28] **Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey** | [[paper]](https://arxiv.org/abs/2503.22458) | [code]

- [2025/03/27] **EQ-Negotiator: An Emotion-Reasoning LLM Agent in Credit Dialogues** | [[paper]](https://arxiv.org/abs/2503.21080) | [code]

- [2025/03/26] **3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark** | [[paper]](https://arxiv.org/abs/2504.13861) | [code]

- [2025/03/25] **CoMAC: Conversational Agent for Multi-Source Auxiliary Context with Sparse and Symmetric Latent Interactions** | [[paper]](https://arxiv.org/abs/2503.19274) | [code]

- [2025/03/25] **Substance over Style: Evaluating Proactive Conversational Coaching Agents** | [[paper]](https://arxiv.org/abs/2503.19328) | [code]

- [2025/03/18] **Personalized Attacks of Social Engineering in Multi-turn Conversations -- LLM Agents for Simulation and Detection** | [[paper]](https://arxiv.org/abs/2503.15552) | [code]

- [2025/03/11] **In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents** | [[paper]](https://arxiv.org/abs/2503.08026) | [code]

- [2025/03/05] **Cite Before You Speak: Enhancing Context-Response Grounding in E-commerce Conversational LLM-Agents** | [[paper]](https://arxiv.org/abs/2503.04830) | [code]

- [2025/02/24] **Turning Conversations into Workflows: A Framework to Extract and Evaluate Dialog Workflows for Service AI Agents** | [[paper]](https://arxiv.org/abs/2502.17321) | [code]

- [2025/02/20] **Enhancing Conversational Agents with Theory of Mind: Aligning Beliefs, Desires, and Intentions for Human-Like Interaction** | [[paper]](https://arxiv.org/abs/2502.14171) | [code]

- [2025/02/18] **One Size doesn&#39;t Fit All: A Personalized Conversational Tutoring Agent for Mathematics Instruction** | [[paper]](https://arxiv.org/abs/2502.12633) | [code]

- [2025/02/18] **Training Turn-by-Turn Verifiers for Dialogue Tutoring Agents: The Curious Case of LLMs as Your Coding Tutors** | [[paper]](https://arxiv.org/abs/2502.13311) | [code]

- [2025/02/18] **You need to MIMIC to get FAME: Solving Meeting Transcript Scarcity with a Multi-Agent Conversations** | [[paper]](https://arxiv.org/abs/2502.13001) | [code]

- [2025/02/17] **InfoQuest: Evaluating Multi-Turn Dialogue Agents for Open-Ended Conversations with Hidden Context** | [[paper]](https://arxiv.org/abs/2502.12257) | [code]

- [2025/02/13] **Reliable Conversational Agents under ASP Control that Understand Natural Language** | [[paper]](https://arxiv.org/abs/2502.09237) | [code]

- [2025/02/12] **Can a Single Model Master Both Multi-turn Conversations and Tool Use? CoALM: A Unified Conversational Agentic Language Model** | [[paper]](https://arxiv.org/abs/2502.08820) | [code]

- [2025/02/09] **MTPChat: A Multimodal Time-Aware Persona Dataset for Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.05887) | [code]

- [2025/02/09] **HamRaz: A Culture-Based Persian Conversation Dataset for Person-Centered Therapy Using LLM Agents** | [[paper]](https://arxiv.org/abs/2502.05982) | [code]

- [2025/02/08] **On Memory Construction and Retrieval for Personalized Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.05589) | [code]

- [2025/02/06] **PsyPlay: Personality-Infused Role-Playing Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.03821) | [code]

- [2025/01/24] **Unmasking Conversational Bias in AI Multiagent Systems** | [[paper]](https://arxiv.org/abs/2501.14844) | [code]

- [2025/01/23] **Communicating Activations Between Language Model Agents** | [[paper]](https://arxiv.org/abs/2501.14082) | [code]

- [2025/01/19] **IntellAgent: A Multi-Agent Framework for Evaluating Conversational AI Systems** | [[paper]](https://arxiv.org/abs/2501.11067) | [code]

- [2025/01/14] **Developing Enhanced Conversational Agents for Social Virtual Worlds** | [[paper]](https://arxiv.org/abs/2501.16341) | [code]

- [2025/01/03] **PSYCHE: A Multi-faceted Patient Simulation Framework for Evaluation of Psychiatric Assessment Conversational Agents** | [[paper]](https://arxiv.org/abs/2501.01594) | [code]

- [2024/12/30] **Exploring and Controlling Diversity in LLM-Agent Conversation** | [[paper]](https://arxiv.org/abs/2412.21102) | [code]

- [2024/12/24] **Extracting triples from dialogues for conversational social agents** | [[paper]](https://arxiv.org/abs/2412.18364) | [code]

- [2024/12/22] **Modular Conversational Agents for Surveys and Interviews** | [[paper]](https://arxiv.org/abs/2412.17049) | [code]

- [2024/12/21] **InfoTech Assistant : A Multimodal Conversational Agent for InfoTechnology Web Portal Queries** | [[paper]](https://arxiv.org/abs/2412.16412) | [code]

- [2024/12/13] **Script-Based Dialog Policy Planning for LLM-Powered Conversational Agents: A Basic Architecture for an &#34;AI Therapist&#34;** | [[paper]](https://arxiv.org/abs/2412.15242) | [code]

- [2024/12/06] **CALICO: Conversational Agent Localization via Synthetic Data Generation** | [[paper]](https://arxiv.org/abs/2412.05388) | [code]

- [2024/12/05] **Educational-Psychological Dialogue Robot Based on Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2412.03847) | [code]

- [2024/12/01] **Examining Identity Drift in Conversations of LLM Agents** | [[paper]](https://arxiv.org/abs/2412.00804) | [code]

- [2024/11/07] **Thanos: Enhancing Conversational Agents with Skill-of-Mind-Infused Large Language Model** | [[paper]](https://arxiv.org/abs/2411.04496) | [code]

- [2024/11/07] **Interactive Dialogue Agents via Reinforcement Learning on Hindsight Regenerations** | [[paper]](https://arxiv.org/abs/2411.05194) | [code]

- [2024/11/06] **MRJ-Agent: An Effective Jailbreak Agent for Multi-Round Dialogue** | [[paper]](https://arxiv.org/abs/2411.03814) | [code]

- [2024/11/01] **DARD: A Multi-Agent Approach for Task-Oriented Dialog Systems** | [[paper]](https://arxiv.org/abs/2411.00427) | [code]

- [2024/11/01] **ReSpAct: Harmonizing Reasoning, Speaking, and Acting Towards Building Large Language Model-Based Conversational AI Agents** | [[paper]](https://arxiv.org/abs/2411.00927) | [code]

- [2024/10/29] **MARCO: Multi-Agent Real-time Chat Orchestration** | [[paper]](https://arxiv.org/abs/2410.21784) | [code]

- [2024/10/25] **AGENT-CQ: Automatic Generation and Evaluation of Clarifying Questions for Conversational Search with LLMs** | [[paper]](https://arxiv.org/abs/2410.19692) | [code]

- [2024/10/18] **Coherence-Driven Multimodal Safety Dialogue with Active Learning for Embodied Agents** | [[paper]](https://arxiv.org/abs/2410.14141) | [code]

- [2024/10/15] **HR-Agent: A Task-Oriented Dialogue (TOD) LLM Agent Tailored for HR Applications** | [[paper]](https://arxiv.org/abs/2410.11239) | [code]

- [2024/10/10] **Rewriting Conversational Utterances with Instructed Large Language Models** | [[paper]](https://arxiv.org/abs/2410.07797) | [code]

- [2024/09/24] **Automated test generation to evaluate tool-augmented LLMs as conversational AI agents** | [[paper]](https://arxiv.org/abs/2409.15934) | [code]

- [2024/09/23] **Beyond Turn-Based Interfaces: Synchronous LLMs as Full-Duplex Dialogue Agents** | [[paper]](https://arxiv.org/abs/2409.15594) | [code]

- [2024/09/13] **AI-LieDar: Examine the Trade-off Between Utility and Truthfulness in LLM Agents** | [[paper]](https://arxiv.org/abs/2409.09013) | [code]

- [2024/09/06] **Sparse Rewards Can Self-Train Dialogue Agents** | [[paper]](https://arxiv.org/abs/2409.04617) | [code]

- [2024/09/02] **Co-Learning: Code Learning for Multi-Agent Reinforcement Collaborative Framework with Conversational Natural Language Interfaces** | [[paper]](https://arxiv.org/abs/2409.00985) | [code]

- [2024/08/27] **Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations** | [[paper]](https://arxiv.org/abs/2408.15232) | [code]

- [2024/08/22] **MDD-5k: A New Diagnostic Conversation Dataset for Mental Disorders Synthesized via Neuro-Symbolic LLM Agents** | [[paper]](https://arxiv.org/abs/2408.12142) | [code]

- [2024/08/13] **What should I wear to a party in a Greek taverna? Evaluation for Conversational Agents in the Fashion Domain** | [[paper]](https://arxiv.org/abs/2408.08907) | [code]

- [2024/08/06] **OpenOmni: A Collaborative Open Source Tool for Building Future-Ready Multimodal Conversational Agents** | [[paper]](https://arxiv.org/abs/2408.03047) | [code]

- [2024/08/03] **Self-Emotion Blended Dialogue Generation in Social Simulation Agents** | [[paper]](https://arxiv.org/abs/2408.01633) | [code]

- [2024/07/31] **Towards Achieving Human Parity on End-to-end Simultaneous Speech Translation via LLM Agent** | [[paper]](https://arxiv.org/abs/2407.21646) | [code]

- [2024/07/13] **Cohesive Conversations: Enhancing Authenticity in Multi-Agent Simulated Dialogues** | [[paper]](https://arxiv.org/abs/2407.09897) | [code]

- [2024/07/04] **Controllable Conversations: Planning-Based Dialogue Agent with Large Language Models** | [[paper]](https://arxiv.org/abs/2407.03884) | [code]

- [2024/07/01] **Empathic Grounding: Explorations using Multimodal Interaction and Large Language Models with Conversational Agents** | [[paper]](https://arxiv.org/abs/2407.01824) | [code]

- [2024/06/30] **CAMON: Cooperative Agents for Multi-Object Navigation with LLM-based Conversations** | [[paper]](https://arxiv.org/abs/2407.00632) | [code]

- [2024/06/09] **Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions** | [[paper]](https://arxiv.org/abs/2406.05688) | [[code]](https://github.com/chengtan9907/reviewmt)

- [2024/05/29] **Toward Conversational Agents with Context and Time Sensitive Long-term Memory** | [[paper]](https://arxiv.org/abs/2406.00057) | [[code]](https://github.com/Zyphra/TemporalMemoryDataset)

- [2024/05/16] **Speaker Verification in Agent-Generated Conversations** | [[paper]](https://arxiv.org/abs/2405.10150) | [code]

- [2024/04/19] **Towards Human-centered Proactive Conversational Agents** | [[paper]](https://arxiv.org/abs/2404.12670) | [code]

- [2024/04/10] **Apollonion: Profile-centric Dialog Agent** | [[paper]](https://arxiv.org/abs/2404.08692) | [code]

- [2024/03/17] **Improving Dialogue Agents by Decomposing One Global Explicit Annotation with Local Implicit Multimodal Feedback** | [[paper]](https://arxiv.org/abs/2403.11330) | [code]

- [2024/03/08] **ChatASU: Evoking LLM&#39;s Reflexion to Truly Understand Aspect Sentiment in Dialogues** | [[paper]](https://arxiv.org/abs/2403.05326) | [code]

- [2024/02/25] **Understanding Public Perceptions of AI Conversational Agents: A Cross-Cultural Analysis** | [[paper]](https://arxiv.org/abs/2402.16039) | [code]

- [2024/02/23] **On the Multi-turn Instruction Following for Conversational Web Agents** | [[paper]](https://arxiv.org/abs/2402.15057) | [code]

- [2024/02/20] **CHATATC: Large Language Model-Driven Conversational Agents for Supporting Strategic Air Traffic Flow Management** | [[paper]](https://arxiv.org/abs/2402.14850) | [code]

- [2024/01/29] **Assistive Large Language Model Agents for Socially-Aware Negotiation Dialogues** | [[paper]](https://arxiv.org/abs/2402.01737) | [code]

- [2024/01/10] **Bootstrapping LLM-based Task-Oriented Dialogue Agents via Self-Talk** | [[paper]](https://arxiv.org/abs/2401.05033) | [code]

- [2024/01/02] **CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation** | [[paper]](https://arxiv.org/abs/2401.01275) | [code]

- [2023/12/21] **Team Flow at DRC2023: Building Common Ground and Text-based Turn-taking in a Travel Agent Spoken Dialogue System** | [[paper]](https://arxiv.org/abs/2312.13816) | [code]

- [2023/11/15] **ToolTalk: Evaluating Tool-Usage in a Conversational Setting** | [[paper]](https://arxiv.org/abs/2311.10775) | [code]

- [2023/10/01] **Adapting LLM Agents Through Communication** | [[paper]](https://arxiv.org/abs/2310.01444v2) | [code]

- [2023/06/28] **Inferring the Goals of Communicating Agents from Actions and Instructions** | [[paper]](https://arxiv.org/abs/2306.16207) | [code]

- [2023/04/26] **Multi-Party Chat: Conversational Agents in Group Settings with Humans and Models** | [[paper]](https://arxiv.org/abs/2304.13835) | [code]

- [2023/03/31] **CAMEL: Communicative Agents for &#34;Mind&#34; Exploration of Large Language Model Society** | [[paper]](https://arxiv.org/abs/2303.17760) | [[code]](https://github.com/camel-ai/camel)

#### Game Playing
- [2025/06/30] **SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2506.24119) | [code]

- [2025/06/05] **Time to Talk: LLM Agents for Asynchronous Group Communication in Mafia Games** | [[paper]](https://arxiv.org/abs/2506.05309) | [code]

- [2025/06/04] **TextAtari: 100K Frames Game Playing with Language Agents** | [[paper]](https://arxiv.org/abs/2506.04098) | [code]

- [2025/05/29] **The Automated but Risky Game: Modeling Agent-to-Agent Negotiations and Transactions in Consumer Markets** | [[paper]](https://arxiv.org/abs/2506.00073) | [code]

- [2025/05/28] **First Steps Towards Overhearing LLM Agents: A Case Study With Dungeons &amp; Dragons Gameplay** | [[paper]](https://arxiv.org/abs/2505.22809) | [code]

- [2025/05/25] **When Ethics and Payoffs Diverge: LLM Agents in Morally Charged Social Dilemmas** | [[paper]](https://arxiv.org/abs/2505.19212) | [code]

- [2025/05/23] **CoMet: Metaphor-Driven Covert Communication for Multi-Agent Language Games** | [[paper]](https://arxiv.org/abs/2505.18218) | [code]

- [2025/05/20] **BAR: A Backward Reasoning based Agent for Complex Minecraft Tasks** | [[paper]](https://arxiv.org/abs/2505.14079) | [code]

- [2025/04/23] **Monte Carlo Planning with Large Language Model for Text-Based Game Agents** | [[paper]](https://arxiv.org/abs/2504.16855) | [code]

- [2025/04/15] **TextArena** | [[paper]](https://arxiv.org/abs/2504.11442) | [code]

- [2025/04/09] **Persona Dynamics: Unveiling the Impact of Personality Traits on Agents in Text-Based Games** | [[paper]](https://arxiv.org/abs/2504.06868) | [code]

- [2025/03/08] **DSGBench: A Diverse Strategic Game Benchmark for Evaluating LLM-based Agents in Complex Decision-Making Environments** | [[paper]](https://arxiv.org/abs/2503.06047) | [code]

- [2025/03/06] **VQEL: Enabling Self-Developed Symbolic Language in Agents through Vector Quantization in Emergent Language Games** | [[paper]](https://arxiv.org/abs/2503.04940) | [code]

- [2025/03/06] **Factorio Learning Environment** | [[paper]](https://arxiv.org/abs/2503.09617) | [code]

- [2025/02/05] **Multimodal Transformer Models for Turn-taking Prediction: Effects on Conversational Dynamics of Human-Agent Interaction during Cooperative Gameplay** | [[paper]](https://arxiv.org/abs/2503.16432) | [code]

- [2025/02/01] **Who&#39;s the MVP? A Game-Theoretic Evaluation Benchmark for Modular Attribution in LLM Agents** | [[paper]](https://arxiv.org/abs/2502.00510) | [code]

- [2025/01/24] **Multi-agent KTO: Reinforcing Strategic Interactions of Large Language Model in Language Game** | [[paper]](https://arxiv.org/abs/2501.14225) | [code]

- [2024/12/06] **TeamCraft: A Benchmark for Multi-Modal Multi-Agent Systems in Minecraft** | [[paper]](https://arxiv.org/abs/2412.05255) | [code]

- [2024/11/08] **Game-theoretic LLM: Agent Workflow for Negotiation Games** | [[paper]](https://arxiv.org/abs/2411.05990) | [code]

- [2024/10/28] **Can Machines Think Like Humans? A Behavioral Evaluation of LLM-Agents in Dictator Games** | [[paper]](https://arxiv.org/abs/2410.21359) | [code]

- [2024/09/03] **An Implementation of Werewolf Agent That does not Truly Trust LLMs** | [[paper]](https://arxiv.org/abs/2409.01575) | [code]

- [2024/08/05] **Evaluating and Enhancing LLMs Agent based on Theory of Mind in Guandan: A Multi-Player Cooperative Game under Imperfect Information** | [[paper]](https://arxiv.org/abs/2408.02559) | [code]

- [2024/07/23] **AMONGAGENTS: Evaluating Large Language Models in the Interactive Text-Based Social Deduction Game** | [[paper]](https://arxiv.org/abs/2407.16521) | [code]

- [2024/07/17] **A LLM Benchmark based on the Minecraft Builder Dialog Agent Task** | [[paper]](https://arxiv.org/abs/2407.12734) | [code]

- [2024/06/27] **OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents** | [[paper]](https://arxiv.org/abs/2407.00114) | [code]

- [2024/06/07] **GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents** | [[paper]](https://arxiv.org/abs/2406.06613) | [[code]](https://github.com/Joshuaclymer/GameBench)

- [2024/06/05] **The Good, the Bad, and the Hulk-like GPT: Analyzing Emotional Decisions of Large Language Models in Cooperation and Bargaining Games** | [[paper]](https://arxiv.org/abs/2406.03299) | [code]

- [2024/05/24] **Hacc-Man: An Arcade Game for Jailbreaking LLMs** | [[paper]](https://arxiv.org/abs/2405.15902) | [code]

- [2024/05/23] **Human-Agent Cooperation in Games under Incomplete Information through Natural Language Communication** | [[paper]](https://arxiv.org/abs/2405.14173) | [code]

- [2024/05/08] **LLMs with Personalities in Multi-issue Negotiation Games** | [[paper]](https://arxiv.org/abs/2405.05248) | [code]

- [2024/04/30] **PANGeA: Procedural Artificial Narrative using Generative AI for Turn-Based Video Games** | [[paper]](https://arxiv.org/abs/2404.19721) | [code]

- [2024/04/03] **Learn to Disguise: Avoid Refusal Responses in LLM&#39;s Defense via a Multi-agent Attacker-Disguiser Game** | [[paper]](https://arxiv.org/abs/2404.02532) | [code]

- [2024/03/28] **MineLand: Simulating Large-Scale Multi-Agent Interactions with Limited Multimodal Senses and Physical Needs** | [[paper]](https://arxiv.org/abs/2403.19267) | [[code]](https://github.com/cocacola-lab/mineland)

- [2024/03/18] **How Far Are We on the Decision-Making of LLMs? Evaluating LLMs&#39; Gaming Ability in Multi-Agent Environments** | [[paper]](https://arxiv.org/abs/2403.11807) | [code]

- [2024/02/19] **PsychoGAT: A Novel Psychological Measurement Paradigm through Interactive Fiction Games with LLM Agents** | [[paper]](https://arxiv.org/abs/2402.12326) | [code]

- [2024/02/13] **Large Language Models as Minecraft Agents** | [[paper]](https://arxiv.org/abs/2402.08392) | [code]

- [2024/02/12] **Large Language Models as Agents in Two-Player Games** | [[paper]](https://arxiv.org/abs/2402.08078) | [code]

- [2024/02/04] **Enhance Reasoning for Large Language Models in the Game Werewolf** | [[paper]](https://arxiv.org/abs/2402.02330) | [code]

- [2024/02/02] **PokeLLMon: A Human-Parity Agent for Pokemon Battles with Large Language Models** | [[paper]](https://arxiv.org/abs/2402.01118) | [code]

- [2023/12/29] **Cooperation on the Fly: Exploring Language Agents for Ad Hoc Teamwork in the Avalon Game** | [[paper]](https://arxiv.org/abs/2312.17515) | [code]

- [2023/12/01] **Deciphering Digital Detectives: Understanding LLM Behaviors and Capabilities in Multi-Agent Mystery Games** | [[paper]](https://arxiv.org/abs/2312.00746) | [code]

- [2023/10/31] **Leveraging Word Guessing Games to Assess the Intelligence of Large Language Models** | [[paper]](https://arxiv.org/abs/2310.20499) | [code]

- [2023/09/29] **Suspicion-Agent: Playing Imperfect Information Games with Theory of Mind Aware GPT-4** | [[paper]](https://arxiv.org/abs/2309.17277) | [code]

- [2023/09/18] **MindAgent: Emergent Gaming Interaction** | [[paper]](https://arxiv.org/abs/2309.09971) | [[code]](https://mindagent.github.io/)

- [2023/09/10] **An Appraisal-Based Chain-Of-Emotion Architecture for Affective Language Model Game Agents** | [[paper]](https://arxiv.org/abs/2309.05076) | [code]

- [2023/09/09] **Exploring Large Language Models for Communication Games: An Empirical Study on Werewolf** | [[paper]](https://arxiv.org/abs/2309.04658) | [code]

- [2023/08/23] **Are ChatGPT and GPT-4 Good Poker Players? -- A Pre-Flop Analysis** | [[paper]](https://arxiv.org/abs/2308.12466) | [code]

- [2023/05/31] **Recursive Metropolis-Hastings Naming Game: Symbol Emergence in a Multi-agent System based on Probabilistic Generative Models** | [[paper]](https://arxiv.org/abs/2305.19761) | [code]

- [2023/05/26] **Playing repeated games with Large Language Models** | [[paper]](https://arxiv.org/abs/2305.16867) | [code]

- [2023/05/25] **Ghost in the Minecraft: Generally Capable Agents for Open-World Environments via Large Language Models with Text-based Knowledge and Memory** | [[paper]](https://arxiv.org/abs/2305.17144) | [code]

- [2023/05/08] **Knowledge-enhanced Agents for Interactive Text Games** | [[paper]](https://arxiv.org/abs/2305.05091) | [code]

- [2023/04/06] **Can Large Language Models Play Text Games Well? Current State-of-the-Art and Open Questions** | [[paper]](https://arxiv.org/abs/2304.02868) | [code]

#### Human-Agent Interaction
- [2025/06/11] **A Call for Collaborative Intelligence: Why Human-Agent Systems Should Precede AI Autonomy** | [[paper]](https://arxiv.org/abs/2506.09420) | [code]

- [2025/05/16] **Talk to Your Slides: Language-Driven Agents for Efficient Slide Editing** | [[paper]](https://arxiv.org/abs/2505.11604) | [code]

- [2025/03/26] **TAMA: A Human-AI Collaborative Thematic Analysis Framework Using Multi-Agent LLMs for Clinical Interviews** | [[paper]](https://arxiv.org/abs/2503.20666) | [code]

- [2025/02/17] **Leveraging Dual Process Theory in Language Agent Framework for Real-time Simultaneous Human-AI Collaboration** | [[paper]](https://arxiv.org/abs/2502.11882) | [code]

- [2025/02/05] **Multimodal Transformer Models for Turn-taking Prediction: Effects on Conversational Dynamics of Human-Agent Interaction during Cooperative Gameplay** | [[paper]](https://arxiv.org/abs/2503.16432) | [code]

- [2025/01/28] **CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation** | [[paper]](https://arxiv.org/abs/2501.16609) | [code]

- [2024/12/20] **Collaborative Gym: A Framework for Enabling and Evaluating Human-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2412.15701) | [code]

- [2024/06/28] **Designing and Evaluating Multi-Chatbot Interface for Human-AI Communication: Preliminary Findings from a Persuasion Task** | [[paper]](https://arxiv.org/abs/2406.19648) | [code]

- [2024/06/11] **Towards Human-AI Collaboration in Healthcare: Guided Deferral Systems with Large Language Models** | [[paper]](https://arxiv.org/abs/2406.07212) | [code]

- [2024/06/02] **Towards a copilot in BIM authoring tool using a large language model-based agent for intelligent human-machine interaction** | [[paper]](https://arxiv.org/abs/2406.16903) | [code]

- [2024/03/05] **ChatCite: LLM Agent with Human Workflow Guidance for Comparative Literature Summary** | [[paper]](https://arxiv.org/abs/2403.02574) | [code]

- [2024/02/20] **Large Language Model-based Human-Agent Collaboration for Complex Task Solving** | [[paper]](https://arxiv.org/abs/2402.12914) | [code]

- [2024/02/18] **Shaping Human-AI Collaboration: Varied Scaffolding Levels in Co-writing with Language Models** | [[paper]](https://arxiv.org/abs/2402.11723) | [code]

- [2024/02/17] **MONAL: Model Autophagy Analysis for Modeling Human-AI Interactions** | [[paper]](https://arxiv.org/abs/2402.11271) | [code]

- [2023/09/22] **Learning to Coordinate with Anyone** | [[paper]](https://arxiv.org/abs/2309.12633) | [code]

- [2023/07/31] **HAGRID: A Human-LLM Collaborative Dataset for Generative Information-Seeking with Attribution** | [[paper]](https://arxiv.org/abs/2307.16883) | [code]

- [2023/04/26] **Multi-Party Chat: Conversational Agents in Group Settings with Humans and Models** | [[paper]](https://arxiv.org/abs/2304.13835) | [code]

#### Tool Usage
- [2025/07/10] **PyVision: Agentic Vision with Dynamic Tooling** | [[paper]](https://arxiv.org/abs/2507.07998) | [code]

- [2025/07/09] **VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation** | [[paper]](https://arxiv.org/abs/2507.06899) | [code]

- [2025/07/03] **WebSailor: Navigating Super-human Reasoning for Web Agent** | [[paper]](https://arxiv.org/abs/2507.02592) | [code]

- [2025/07/02] **OpenTable-R1: A Reinforcement Learning Augmented Tool Agent for Open-Domain Table Question Answering** | [[paper]](https://arxiv.org/abs/2507.03018) | [code]

- [2025/06/30] **LineRetriever: Planning-Aware Observation Reduction for Web Agents** | [[paper]](https://arxiv.org/abs/2507.00210) | [code]

- [2025/06/27] **More Vulnerable than You Think: On the Stability of Tool-Integrated LLM Agents** | [[paper]](https://arxiv.org/abs/2506.21967) | [code]

- [2025/06/24] **Doc2Agent: Scalable Generation of Tool-Using Agents from API Documentation** | [[paper]](https://arxiv.org/abs/2506.19998) | [code]

- [2025/06/24] **NaviAgent: Bilevel Planning on Tool Dependency Graphs for Function Calling** | [[paper]](https://arxiv.org/abs/2506.19500) | [code]

- [2025/06/18] **Understanding GUI Agent Localization Biases through Logit Sharpness** | [[paper]](https://arxiv.org/abs/2506.15425) | [code]

- [2025/06/18] **Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence** | [[paper]](https://arxiv.org/abs/2506.15677) | [code]

- [2025/06/17] **AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents** | [[paper]](https://arxiv.org/abs/2506.14205) | [code]

- [2025/06/12] **VideoDeepResearch: Long Video Understanding With Agentic Tool Using** | [[paper]](https://arxiv.org/abs/2506.10821) | [code]

- [2025/06/12] **Build the web for agents, not agents for the web** | [[paper]](https://arxiv.org/abs/2506.10953) | [code]

- [2025/06/10] **Atomic-to-Compositional Generalization for Mobile Agents with A New Benchmark and Scheduling System** | [[paper]](https://arxiv.org/abs/2506.08972) | [code]

- [2025/06/10] **GUIRoboTron-Speech: Towards Automated GUI Agents Based on Speech Instructions** | [[paper]](https://arxiv.org/abs/2506.11127) | [code]

- [2025/06/09] **CheMatAgent: Enhancing LLMs for Chemistry and Materials Science through Tree-Search Based Tool Learning** | [[paper]](https://arxiv.org/abs/2506.07551) | [code]

- [2025/06/04] **Go-Browse: Training Web Agents with Structured Exploration** | [[paper]](https://arxiv.org/abs/2506.03533) | [code]

- [2025/06/03] **GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents** | [[paper]](https://arxiv.org/abs/2506.03143) | [code]

- [2025/06/02] **AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning** | [[paper]](https://arxiv.org/abs/2506.01391) | [code]

- [2025/05/30] **MedOrch: Medical Diagnosis with Tool-Augmented Reasoning Agents for Flexible Extensibility** | [[paper]](https://arxiv.org/abs/2506.00235) | [code]

- [2025/05/28] **RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments** | [[paper]](https://arxiv.org/abs/2505.21936) | [code]

- [2025/05/28] **EvolveSearch: An Iterative Self-Evolving Search Agent** | [[paper]](https://arxiv.org/abs/2505.22501) | [code]

- [2025/05/28] **UI-Evol: Automatic Knowledge Evolving for Computer Use Agents** | [[paper]](https://arxiv.org/abs/2505.21964) | [code]

- [2025/05/28] **WebDancer: Towards Autonomous Information Seeking Agency** | [[paper]](https://arxiv.org/abs/2505.22648) | [[code]](https://github.com/Alibaba-NLP/WebAgent)

- [2025/05/27] **BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism** | [[paper]](https://arxiv.org/abs/2505.20660) | [code]

- [2025/05/27] **UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents** | [[paper]](https://arxiv.org/abs/2505.21496) | [code]

- [2025/05/27] **ChemHAS: Hierarchical Agent Stacking for Enhancing Chemistry Tools** | [[paper]](https://arxiv.org/abs/2505.21569) | [code]

- [2025/05/26] **T^2Agent A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search** | [[paper]](https://arxiv.org/abs/2505.19768) | [code]

- [2025/05/26] **WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback** | [[paper]](https://arxiv.org/abs/2505.20013) | [code]

- [2025/05/23] **Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding** | [[paper]](https://arxiv.org/abs/2505.18079) | [code]

- [2025/05/23] **ProgRM: Build Better GUI Agents with Progress Rewards** | [[paper]](https://arxiv.org/abs/2505.18121) | [code]

- [2025/05/23] **Gaming Tool Preferences in Agentic LLMs** | [[paper]](https://arxiv.org/abs/2505.18135) | [code]

- [2025/05/22] **WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2505.16421) | [code]

- [2025/05/22] **T1: A Tool-Oriented Conversational Dataset for Multi-Turn Agentic Planning** | [[paper]](https://arxiv.org/abs/2505.16986) | [code]

- [2025/05/21] **Web-Shepherd: Advancing PRMs for Reinforcing Web Agents** | [[paper]](https://arxiv.org/abs/2505.15277) | [code]

- [2025/05/21] **X-WebAgentBench: A Multilingual Interactive Web Benchmark for Evaluating Global Agentic System** | [[paper]](https://arxiv.org/abs/2505.15372) | [code]

- [2025/05/21] **GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents** | [[paper]](https://arxiv.org/abs/2505.15810) | [code]

- [2025/05/21] **AgentThink: A Unified Framework for Tool-Augmented Chain-of-Thought Reasoning in Vision-Language Models for Autonomous Driving** | [[paper]](https://arxiv.org/abs/2505.15298) | [code]

- [2025/05/20] **Mobile-Agent-V: A Video-Guided Approach for Effortless and Efficient Operational Knowledge Injection in Mobile Automation** | [[paper]](https://arxiv.org/abs/2505.13887) | [code]

- [2025/05/20] **Efficient Agent Training for Computer Use** | [[paper]](https://arxiv.org/abs/2505.13909) | [code]

- [2025/05/20] **s3: You Don&#39;t Need That Much Data to Train a Search Agent via RL** | [[paper]](https://arxiv.org/abs/2505.14146) | [code]

- [2025/05/19] **GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents** | [[paper]](https://arxiv.org/abs/2505.12842) | [code]

- [2025/05/18] **Enhance Mobile Agents Thinking Process Via Iterative Preference Learning** | [[paper]](https://arxiv.org/abs/2505.12299) | [code]

- [2025/05/17] **Demystifying and Enhancing the Efficiency of Large Language Model Based Search Agents** | [[paper]](https://arxiv.org/abs/2505.12065) | [code]

- [2025/05/16] **EnvInjection: Environmental Prompt Injection Attack to Multi-modal Web Agents** | [[paper]](https://arxiv.org/abs/2505.11717) | [code]

- [2025/05/09] **ScaleMCP: Dynamic and Auto-Synchronizing Model Context Protocol Tools for LLM Agents** | [[paper]](https://arxiv.org/abs/2505.06416) | [code]

- [2025/04/28] **MICE for CATs: Model-Internal Confidence Estimation for Calibrating Agents with Tools** | [[paper]](https://arxiv.org/abs/2504.20168) | [code]

- [2025/04/27] **AndroidGen: Building an Android Language Agent under Data Scarcity** | [[paper]](https://arxiv.org/abs/2504.19298) | [code]

- [2025/04/24] **Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents** | [[paper]](https://arxiv.org/abs/2504.17934) | [code]

- [2025/04/23] **WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model** | [[paper]](https://arxiv.org/abs/2504.21024) | [code]

- [2025/04/22] **Guiding VLM Agents with Process Rewards at Inference Time for GUI Navigation** | [[paper]](https://arxiv.org/abs/2504.16073) | [code]

- [2025/04/19] **InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners** | [[paper]](https://arxiv.org/abs/2504.14239) | [code]

- [2025/04/17] **WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents** | [[paper]](https://arxiv.org/abs/2504.12682) | [code]

- [2025/04/16] **Enhancing Web Agents with Explicit Rollback Mechanisms** | [[paper]](https://arxiv.org/abs/2504.11788) | [code]

- [2025/04/15] **The Obvious Invisible Threat: LLM-Powered GUI Agents&#39; Vulnerability to Fine-Print Injections** | [[paper]](https://arxiv.org/abs/2504.11281) | [code]

- [2025/04/14] **Breaking the Data Barrier -- Building GUI Agents Through Task Generalization** | [[paper]](https://arxiv.org/abs/2504.10127) | [code]

- [2025/04/14] **GUI-R1 : A Generalist R1-Style Vision-Language Action Model For GUI Agents** | [[paper]](https://arxiv.org/abs/2504.10458) | [code]

- [2025/04/09] **Inducing Programmatic Skills for Agentic Tasks** | [[paper]](https://arxiv.org/abs/2504.06821) | [code]

- [2025/