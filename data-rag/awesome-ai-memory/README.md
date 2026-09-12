# Awesome-AI-Memory

<p align="center">
    【English | <a href="README_cn.md">中文</a></a>】
</p>

<div align="center">
    <img src="assets/Gemini_Generated_Image_hretabhretabhret.png" alt="Survey Framework" width="82%">
</div>

[![Awesome](https://awesome.re/badge.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/PRs-Welcome-red)
[![Papers](https://img.shields.io/badge/Papers-540-blue.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/papers)
[![Open Source Projects](https://img.shields.io/badge/Open%20Source%20Projects-110-green.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/projects)


## 👋 Introduction
Large Language Models (LLMs) have rapidly evolved into powerful general-purpose reasoning and generation engines. Nevertheless, despite their continuously advancing capabilities, LLMs remain fundamentally constrained by a critical limitation: the finite length of their context window. This constraint defines the scope of information directly accessible during a single inference process, endowing models with only short-term memory capabilities. Consequently, they struggle to support extended conversations, personalized interactions, continuous learning, and complex multi-stage tasks.

To transcend the inherent limitations of context windows, AI memory and memory systems for LLMs have emerged as a vital and active research and engineering frontier. By introducing external, persistent, and controllable memory structures beyond model parameters, these systems enable large models to store, retrieve, compress, and manage historical information during generation processes. This capability allows models to continuously leverage long-term experiences within limited context windows, achieving cross-session consistency and continuous reasoning abilities.

Awesome-AI-Memory is a comprehensive repository dedicated to AI memory and memory systems for large language models, systematically curating relevant research papers, framework tools, and practical implementations. This repository endeavors to map the rapidly evolving research landscape in LLM memory systems, bridging multiple disciplines including natural language processing, information retrieval, intelligent agent systems, and cognitive science.


---

## 🎯 Goal of Repository
Our mission is to establish a centralized, continuously evolving knowledge base that serves as a valuable reference for researchers and practitioners, ultimately accelerating the development of intelligent systems capable of long-term memory retention, sustained reasoning, and adaptive evolution over time.

---

## 📏 Project Scope
This repository focuses on memory mechanisms and system designs that extend or augment the context window capabilities of large language models, rather than merely addressing model pre-training or general knowledge learning. The content encompasses both theoretical research and engineering practices.

🌀 Included Content (In Scope)
- Memory and memory system designs for large language models
- External explicit memory beyond model parameters
- Short-term memory, long-term memory, episodic memory, and semantic memory
- Retrieval-Augmented Generation (RAG) as a memory access mechanism
- Memory management strategies (writing, updating, forgetting, compression)
- Memory systems in intelligent agents (Agents)
- Shared and collaborative memory in multi-agent systems
- Memory models inspired by cognitive science and biological memory
- Evaluation methods, benchmarks, and datasets related to LLM memory
- Open-source frameworks and tools for memory-enhanced LLMs

🌀 Excluded Content (Out of Scope)
- General model pre-training or scaling research without direct memory relevance
- Purely parameterized knowledge learning without memory interaction
- Traditional databases or information retrieval systems unrelated to LLMs
- Generic memory systems outside the LLM context (unless demonstrating direct transfer value)

---

<!-- ## 🗂️ AI-Memory Taxonomy

To systematically organize the diverse research and practical resources in the field of AI large model memory, this repository categorizes memory systems across multiple orthogonal dimensions, reflecting variations in storage methods, temporal scales, content forms, operational processes, and system architectures.
1. Memory by Storage Location
- Parametric Memory
  - Knowledge implicitly encoded within model weights
  - Static and not directly editable during inference
- External / Explicit Memory
  - Memory stored outside model parameters
  - Readable, writable, and dynamically updatable
2. Memory by Temporal Scope
- Short-Term Memory
  - Entirely dependent on context window
  - Session-level, temporary information
- Long-Term Memory
  - Persistent memory across sessions and time scales
  - Supports long-term consistency and personalization
3. Memory by Content Type
- Episodic Memory
  - Event-based historical interaction memory
  - Preserves temporal sequence and contextual relationships
- Semantic Memory
  - Facts, rules, and preferences abstracted from multiple experiences
  - Typically derived from compression or induction of episodic memory
- Procedural Memory
  - Memory related to action patterns, skills, and task execution strategies
4. Memory Operations
- Writing: Determining which information should be stored
- Retrieval: Selecting relevant memories for current tasks
- Updating: Correcting or merging existing memories
- Forgetting: Removing or weakening low-value information
- Compression: Summarizing historical information to fit context windows
5. Memory Mechanisms & Architectures
- Retrieval-Augmented Generation (RAG)
- Summary-based memory mechanisms
- Vectorized semantic retrieval
- Symbolic-neural hybrid memory systems
- Event-driven and trigger-based memory mechanisms
- Reinforcement learning-based memory strategy optimization
6. Memory in Agent Systems
- Single-agent memory
- Multi-agent shared memory
- Tool-augmented memory
- Planning-aware memory
- Personality and emotion-related memory
7. Evaluation & Benchmarks
- Long-term consistency evaluation
- Continuous interaction and long-term task benchmarks
- Memory recall and utilization efficiency metrics
- Personalization and user preference retention evaluation

--- -->

## 🔔 Recent hot research and news
+ 2026-07-06 - 🎉 Updated 25 papers, including 4 on Datasets & Benchmark, and 23 on Framework & Methods
+ 2026-06-14 - 🎉 Updated 24 papers, including 2 on Survey, 4 on Systems & Models, 2 on Datasets & Benchmark, and 16 on Framework & Methods
+ 2026-06-06 - 🎉 Updated 45 papers, including 1 on Survey, 6 on Systems & Models, 12 on Datasets & Benchmark, and 26 on Framework & Methods
+ 2026-05-10 - 🎉 Updated 16 papers, including 3 on systems and models, 1 on benchmarks, and 12 on methods; also added 1 new project under systems and open sources
+ 2026-05-06 - 🎉 Updated 16 papers, including 2 on systems and models, 2 on benchmarks, and 12 on methods
+ 2026-04-27 - 🎉 Updated 15 papers, including 2 on survey, 3 on systems and models, and 10 on methods
+ 2026-04-17 - 🎉 Updated 46 papers, including 1 on survey, 5 on systems and models, 3 on benchmarks, and 37 on methods
+ 2026-04-07 - 🎉 Updated 16 papers, including 15 on methods, and 1 on benchmarks
+ 2026-03-15 - 🎉 Updated 14 papers, including 14 on methods
+ 2026-03-08 - 🎉 Updated 15 papers, including 3 on survey, 2 on systems and models, 5 on benchmarks, and 5 on methods
+ 2026-03-02 - 🎉 Add a new code agent to this repo
+ 2026-02-27 - 🎉 Updated 20 papers, including 1 on survey, 2 on systems and models, 2 on benchmarks, and 15 on methods
+ 2026-02-26 - 🎉 Updated 14 papers, including 14 on methods
+ 2026-02-14 - 🎉 Updated 15 papers, including 1 on survey, 12 on methods, 1 on benchmarks, and 1 on systems and models
+ 2026-02-09 - 🎉 Updated 15 papers
+ 2026-02-01 - 🎉 Updated 16 papers, including 9 on methods, 4 on benchmarks, and 3 on systems and models
+ 2025-12-24 – 🎉 Release Repository V(1.0)
+ 2025-12-10 – 🎉 Initial Repo

---

🗺️ Table of Contents
- [Awesome-AI-Memory](#awesome-ai-memory)
  - [👋 Introduction](#-introduction)
  - [🎯 Goal of Repository](#-goal-of-repository)
  - [📏 Project Scope](#-project-scope)
  - [🔔 Recent hot research and news](#-recent-hot-research-and-news)
  - [🧠 Core Concepts](#-core-concepts)
  - [📚 Paper List](#-paper-list)
  - [🧰 Resources](#-resources)
    - [📊 Benchmarks and Tasks](#-benchmarks-and-tasks)
    - [💻 Systems and Open Sources](#-systems-and-open-sources)
    - [🎥 Multi-media resource](#-multi-media-resource)
    - [🧠 Adam Framework](#-adam-framework)
  - [🤝  Make a Contribution](#--make-a-contribution)
  - [💬 Community \& Support](#-community--support)
  - [🌟 Star Trends](#-star-trends)

---

## 🧠 Core Concepts

- LLM Memory: A fusion of implicit knowledge encoded within parameters (acquired during training) and explicit storage outside parameters (retrieved at runtime), enabling models to transcend token limitations and possess human-like abilities to "remember the past, understand the present, and predict the future."

- Memory System: The complete technical stack implementing memory functionality for large language models, comprising four core components:
  - Memory Storage Layer: Vector databases (e.g., Chroma, Weaviate), graph databases, or hybrid storage solutions
  - Memory Processing Layer: Embedding models, summarization generators, and memory segmenters
  - Memory Retrieval Layer: Multi-stage retrievers, reranking modules, and context injectors
  - Memory Control Layer: Memory prioritization managers, forgetting controllers, and consistency coordinators

- Memory Operations: Atomic memory operations executed through tool calling in memory systems:
  - Writing: Converting dialogue content into vectors for storage, often combined with summarization to reduce noise
  - Retrieval: Generating queries based on current context to obtain Top-K relevant memories
  - Updating: Finding relevant memories via vector similarity and replacing or enhancing them
  - Deletion: Removing specific memories based on user instructions or automatic policies (e.g., privacy expiration)
  - Compression: Merging multiple related memories into summaries to free storage space

- Memory Management: The methodology for managing memories within memory systems, including:
  - Memory Lifecycle: End-to-end management from creation, active usage, infrequent access, to archiving/deletion
  - Conflict Resolution: Arbitration mechanisms for contradictory information (e.g., timestamp priority, source credibility weighting)
  - Resource Budgeting: Allocating memory quotas to different users/tasks to prevent resource abuse
  - Security Governance: Automatic detection and de-identification of PII (Personally Identifiable Information)

- Memory Classification: A multi-dimensional classification system unique to memory systems:
  - By Access Frequency: Working memory (current tasks), frequent memory (personal preferences), archived memory (historical records)
  - By Structured Degree: Structured memory (database records), semi-structured memory (dialogue summaries), unstructured memory (raw conversations)
  - By Sharing Scope: Personal memory (single user), team memory (collaborative spaces), public memory (shared knowledge bases)
  - By Temporal Validity: Permanent memory (core facts), temporary memory (conversation context), time-sensitive memory (e.g., "user is in a bad mood today")

- Memory Mechanisms: Core technical components enabling memory system functionality:
  - Retrieval-Augmented Generation (RAG): Enhancing generation by retrieving relevant information from knowledge bases
  - Memory Reflection Loop: Models periodically "review" conversation history to generate high-level summaries
  - Memory Routing: Automatically selecting retrieval sources based on query type (personal memory/public knowledge base)

- Explicit Memory: Memory stored as raw text outside the model, implemented through vector databases with hybrid indexing strategies:
  - Dense Vector Indexing: Handling semantic similarity queries
  - Sparse Keyword Indexing: Processing exact match queries
  - Multi-vector Indexing: Segmenting long documents into multiple parts, each independently indexed

- Parametric Memory: Knowledge and capabilities stored within the fixed weights of a language model's architecture, characterized by:
  - Serving as the model's core long-term semantic memory carrier
  - Being activatable without external retrieval or explicit contextual support
  - Providing the foundational capability for zero-shot reasoning, general responses, and language generation

- Long-Term Memory: Key information designed for persistent storage, typically implemented as external knowledge bases with capabilities including:
  - Automatic Summarization: Distilling multi-turn dialogues into structured memory
  - Context Binding: Recording memory context to prevent erroneous generalization
  - Multimodal Storage: Simultaneously preserving text, images, audio, and other multimodal memories

- Short-Term Memory: Active information within the LLM's context window, constrained by attention mechanisms. Key techniques include:
  - KV Cache Management: Reusing key-value caches to reduce redundant computation
  - Context Compression: Using summaries instead of detailed history (e.g., "the previous 5 dialogue rounds discussed project budget")
  - Sliding Window Attention: Focusing only on the most recent N tokens while preserving special markers
  - Memory Summary Injection: Dynamically inserting summaries of long-term memory into short-term context

- Episodic Memory: Memory type recording specific user interaction history, fundamental to personalized AI:
  - User Identity Recognition: Identifying the same user across sessions
  - Interaction Trajectory Recording: Preserving user decision paths and feedback
  - Emotional State Tracking: Recording patterns of user mood changes
  - Preference Evolution Modeling: Capturing long-term changes in user interests

- Memory Forgetting: Deliberately designed forgetting mechanisms in large models, including:
  - Selective Forgetting (Machine Unlearning): Removing the influence of specific information from training data, such as covering specific knowledge with forgetting layers
  - Privacy-Driven Forgetting: Automatically identifying and deleting PII information, or setting automatic expiration
  - Memory Decay: Automatically lowering the priority of infrequently accessed memories based on usage frequency
  - Conflict-Driven Forgetting: Strategically updating or discarding old memories when new evidence conflicts with them

- Memory Retrieval: The complex process of precisely locating relevant information from massive memory repositories:
  - Semantic Pre-filtering: Vector similarity matching to obtain Top-100 candidates
  - Contextual Reranking: Reordering results based on current query context
  - Temporal Filtering: Prioritizing the most recent relevant information

- Memory Compression: A collection of techniques maximizing memory utility under limited resources:
  - Content-level Compression: Extracting core information while discarding redundant details
  - Representation-level Compression: Vector quantization (e.g., PQ coding), dimensionality reduction
  - Organization-level Compression: Clustering similar memories, building hierarchical memory structures
  - Knowledge Distillation: Transferring key patterns from external memory into parametric memory

---

## 📚 Paper List
Papers below are ordered by **publication date**:

<details>
  <summary><strong>Survey</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
    </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-25</td>
        <td style="width: 55%;"><strong>Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Survey-4A90E2" alt="Survey">
          <img src="https://img.shields.io/badge/Agent%20Privacy-F5A623" alt="Agent Privacy">
          <img src="https://img.shields.io/badge/Data%20Governance-7ED321" alt="Data Governance">
          <img src="https://img.shields.io/badge/Memory%20Risk-D0021B" alt="Memory Risk">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.26627v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • This survey frames privacy in LLM agents from a data-centric perspective, focusing on the data an agent queries, stores, remembers, exchanges, and acts upon rather than only on attack categories.<br>
          • It organizes risks across databases, document collections, APIs, cross-session memory, intermediate workflow state, and multi-agent communication, showing how sensitive information can leak before the final response is produced.<br>
          • The paper highlights that agent privacy requires lifecycle-level controls over memory writes, retrieval, delegation, logging, and tool use, making persistent state and data governance central to safe agent deployment.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-23</td>
        <td style="width: 55%;"><strong>Are We Ready For An Agent-Native Memory System?</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Memory%20System-green" alt="Memory System">
          <img src="https://img.shields.io/badge/Evaluation-orange" alt="Evaluation">
          <img src="https://img.shields.io/badge/Data%20Management-purple" alt="Data Management">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.24775v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • This paper studies agent memory from a data-management perspective, arguing that memory for LLM agents should be evaluated as a system supporting persistent storage, retrieval, update, consolidation, and lifecycle governance rather than as a monolithic retrieval add-on.<br>
          • It decomposes an agent-native memory system into four modules: representation and storage, extraction, retrieval and routing, and maintenance. Under this framework, the authors evaluate 12 representative memory systems and two baselines across five benchmark workloads spanning 11 datasets.<br>
          • The experiments show that no single memory architecture dominates across all settings; effectiveness depends on the alignment between memory structure and workload bottlenecks. Fine-grained ablations quantify effects on representation fidelity, retrieval precision, update correctness, and long-horizon stability, while cost analysis shows that localized maintenance can be more efficient than global reorganization.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-10</td>
        <td style="width: 55%;"><strong>Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Agents-F5A623" alt="LLM Agents">
          <img src="https://img.shields.io/badge/Environment%20Modeling-7ED321" alt="Environment Modeling">
          <img src="https://img.shields.io/badge/Synthesis-D0021B" alt="Synthesis">
          <img src="https://img.shields.io/badge/Evaluation-9013FE" alt="Evaluation">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.12191">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • This survey systematically frames LLM agent environments across a full lifecycle, including environment modeling, synthesis, evaluation, and application. <br>
          • It introduces symbolic and neural paradigms for environment synthesis and analyzes environment design through structural properties and capability evolution. <br>
          • The work highlights co-evolution between agents and environments (memory, workflows, trajectories, and exploration) and points toward future directions such as environment-as-a-service and multi-agent ecosystems.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-09</td>
        <td style="width: 55%;"><strong>Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Security-%2350E3C2" alt="LLM Security">
          <img src="https://img.shields.io/badge/Attacks-%23F8E71C" alt="Attacks">
          <img src="https://img.shields.io/badge/Defenses-%23FF6FB5" alt="Defenses">
          <img src="https://img.shields.io/badge/Evaluation-%239B9B9B" alt="Evaluation">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.10749">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • This paper analyzes security risks of LLM agents from a lifecycle perspective and formalizes key interactions including information flow, delegated authority, and persistent state. <br>
          • Based on a review of 247 studies, it organizes attack surfaces, defense mechanisms, and evaluation methods, showing that current defenses remain weak and incomplete. <br>
          • It emphasizes the need for clearly defined trust boundaries, principled permission control, and realistic long-horizon security evaluation frameworks aligned with real-world environments.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/LLM-orange" alt="LLM">
          <img src="https://img.shields.io/badge/Memory%20Systems-green" alt="Memory Systems">
          <img src="https://img.shields.io/badge/Long--Horizon%20Tasks-red" alt="Long-Horizon Tasks">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.06448">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • Characterizes agent memory as a stateful long-horizon systems workload rather than only a retrieval add-on.<br>
          • Introduces a system-oriented taxonomy and a phase-aware profiler for construction, retrieval, and generation cost.<br>
          • Analyzes ten representative systems and distills practical recommendations for scalable, freshness-aware memory deployment.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-23</td>
        <td style="width: 55%;"><strong>MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multimodal%20Memory-blue" alt="Multimodal Memory">
          <img src="https://img.shields.io/badge/Visual%20Benchmark-red" alt="Visual Benchmark">
          <img src="https://img.shields.io/badge/Evaluation%20Framework-green" alt="Evaluation Framework">
          <img src="https://img.shields.io/badge/Long--term%20Memory-orange" alt="Long-term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.15128">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • Proposes MemEye, a visual-centric benchmark evaluating multimodal agents' long-term memory beyond text-dominated shortcuts.<br>
          • Designs a 2D evaluation matrix (X-axis: Scene/Region/Instance/Pixel granularity; Y-axis: Atomic/Relational/Evolutionary reasoning depth).<br>
          • Introduces three-stage validation gates ensuring questions cannot be solved via textual context, captions, or beyond VLM capabilities.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-01</td>
        <td style="width: 55%;"><strong>EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--term%20Memory-blue" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/Memory%20OS-orange" alt="Memory OS">
          <img src="https://img.shields.io/badge/Self--Organizing-green" alt="Self-Organizing">
          <img src="https://img.shields.io/badge/Semantic%20Consolidation-red" alt="Semantic Consolidation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2601.02163">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • Proposes EverMemOS, a three-stage memory lifecycle (Episodic Trace Formation → Semantic Consolidation → Reconstructive Recollection) that organizes fragmented conversations into structured, evolving memory units (MemCell/MemScene).<br>
          • Introduces MemCell as atomic memory unit containing Episode + Atomic Facts + Foresight + Metadata, and MemScene for scene-level consolidation enabling long-term user profile evolution.<br>
          • Designs a reconstructive retrieval paradigm with MemScene-guided retrieval, foresight validity filtering, and sufficiency verification to achieve "necessary and sufficient" context for long-horizon reasoning.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-19</td>
        <td style="width: 55%;"><strong>An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Experience--RAG-yellow" alt="Experience-RAG">
          <img src="https://img.shields.io/badge/Retrieval%20Strategy-orange" alt="Retrieval Strategy">
          <img src="https://img.shields.io/badge/Skill%20Orchestration-green" alt="Skill Orchestration">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03989">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • Identifies three engineering problems in pipeline-based retrieval: non-reusable strategy logic, non-observable routing decisions, and non-evolvable workflow coupling.<br>
          • Proposes Experience-RAG Skill with six modules (interface, scene analyzer, experience memory, strategy router, retriever pool, result packer) to encapsulate retrieval strategy selection as a pluggable agent skill.<br>
          • Shows rule-based routing outperforms learned routing (0.8924 vs 0.8778/0.8627) under limited experience memory; experience memory records (scene_features, score_vector, best_margin) enable future upgrade to learning-based routing.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-17</td>
        <td style="width: 55%;"><strong>Human Cognition in Machines: A Unified Perspective of World Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/World%20Models-brightgreen" alt="World Models">
          <img src="https://img.shields.io/badge/Cognitive%20Architecture-yellow" alt="Cognitive Architecture">
          <img src="https://img.shields.io/badge/Meta--cognition-teal" alt="Meta-cognition">
          <img src="https://img.shields.io/badge/Structured%20Knowledge-orange" alt="Structured Knowledge">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16592">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • Surveys memory, perception, language, reasoning, imagination, motivation, and metacognition in world models from a unified cognitive-architecture perspective.<br>
          • Introduces Epistemic World Models for structured knowledge agents in scientific discovery, with taxonomy and future directions across video, embodied, and cognitive world models.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-17</td>
        <td style="width: 55%;"><strong>Agentic Frameworks for Reasoning Tasks: An Empirical Study</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Context%20Management-brightgreen" alt="Context Management">
          <img src="https://img.shields.io/badge/Agentic%20Framework-yellow" alt="Agentic Framework">
          <img src="https://img.shields.io/badge/Orchestration-teal" alt="Orchestration">
          <img src="https://img.shields.io/badge/Memory%20Control-orange" alt="Memory Control">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16646">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • Evaluates 22 common agentic frameworks on BBH, GSM8K, and ARC, comparing accuracy, latency, cost, and cross-benchmark consistency.<br>
          • Finds that performance differences mainly come from orchestration quality, especially memory control, context growth, and failure-retry mechanisms.
        </td>
      </tr>
<tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Survey-red" alt="Survey">
            <img src="https://img.shields.io/badge/Externalization-teal" alt="Externalization">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08224">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • Surveys LLM agent externalization from the perspective of memory, skills, protocols, and harness engineering.<br>
            • Argues that memory externalizes cross-time state, skills externalize procedural capability, protocols externalize interaction structure, and harnesses orchestrate these components together.<br>
            • Maps the evolution from model parameters to context and then to external infrastructure, while discussing the key trade-offs and open challenges across these layers.
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-05</td>
        <td style="width: 55%;"><strong>Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Long%20Context-blue" alt="Long Context">
            <img src="https://img.shields.io/badge/Cost%20Analysis-brightgreen" alt="Cost Analysis">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04814">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • Addresses the ongoing industry debate over the performance and cost trade-offs between long-context models and external memory systems for building persistent agents.<br>
            • Conducts a systematic cross-benchmark evaluation of long-context approaches and fact-based external memory solutions across three major memory benchmarks, assessing both accuracy and cumulative API inference cost.<br>
            • Long-context models demonstrate advantages in factual recall, but their costs increase with each interaction turn; at a 100k context length, memory systems surpass them in cost efficiency after approximately 10 turns, providing a quantitative basis for real-world engineering decisions.
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-02</td>
        <td style="width: 55%;"><strong>Modular Memory is the Key to Continual Learning Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Continual%20Learning-blue" alt="Continual Learning">
            <img src="https://img.shields.io/badge/Architecture-brightgreen" alt="Architecture">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01761">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • Traditional foundation models rely on weight updates for continual learning, which can easily lead to catastrophic forgetting and makes large-scale experience accumulation difficult.<br>
            • Proposes a roadmap for a modular memory architecture that integrates in-context learning with learning encoded in model weights.<br>
            • This architecture leverages in-context learning for rapid adaptation and weight updates for capability consolidation, offering theoretical guidance for building truly lifelong learning agents.
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-02</td>
        <td style="width: 55%;"><strong>Emerging Human-like Strategies for Semantic Memory Foraging in Large Language Models</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Cognitive%20Alignment-blue" alt="Cognitive Alignment">
            <img src="https://img.shields.io/badge/Interpretability-brightgreen" alt="Interpretability">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01822">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • Investigates whether large language models possess human-like, efficient strategic access mechanisms when processing vast amounts of semantic memory.<br>
            • Uses mechanistic interpretability techniques to analyze semantic fluency tasks, rigorously examining convergent and divergent memory search patterns within the model.<br>
            • Confirms the presence of human-like strategic memory search behavior across different layers of LLMs, laying an interpretability foundation for research on cognitive alignment and enhanced human-AI collaboration.
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-26</td>
        <td style="width: 55%;"><strong>Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Personalized%20Agents-blue" alt="Personalized Agents">
            <img src="https://img.shields.io/badge/User%20Adaptation-brightgreen" alt="User Adaptation">
            <img src="https://img.shields.io/badge/Evaluation-yellow" alt="Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.22680.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • This paper explores the foundations, evaluation, and future directions of personalized LLM-driven agents, providing a capability-oriented systematic review of their underlying principles, assessment methodologies, and prospective developments.<br>
            • It constructs a taxonomy centered on four interdependent core components: user profile modeling, memory, planning, and action execution.<br>
            • The paper offers a comprehensive analysis of how user signals are represented, propagated, and utilized, and discusses application scenarios and design trade-offs ranging from general-purpose assistance to specialized domains.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-14</td>
      <td style="width: 55%;">
      <strong>Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms Badge">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2602.06052">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • This paper proposes a unified taxonomy for foundation agent memory across three dimensions: memory substrate, cognitive mechanism, and memory subject.<br>
          • It analyzes memory operation mechanisms in single-agent and multi-agent systems while categorizing memory learning policies into prompting, fine-tuning, and reinforcement learning paradigms.<br>
          • It provides a comprehensive review of evaluation metrics and benchmarks across various applications, outlining critical future directions such as memory efficiency, life-long personalization, and multimodal integration.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-15</td>
      <td style="width: 55%;">
      <strong>Memory in the Age of AI Agents: A Survey</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
        <img src="https://img.shields.io/badge/Forms--Functions--Dynamics-purple" alt="Forms-Functions-Dynamics">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2512.13564">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • Provides a comprehensive and up-to-date landscape of agent memory, explicitly distinguishing it from related concepts like LLM memory, RAG, and context engineering.<br>
          • Introduces a unified taxonomy examining memory through three lenses: <strong>Forms</strong> (token-level, parametric, latent), <strong>Functions</strong> (factual, experiential, working), and <strong>Dynamics</strong> (formation, evolution, retrieval).<br>
          • Discusses emerging research frontiers such as automation-oriented memory design, reinforcement learning integration, and trustworthiness, while compiling representative benchmarks and frameworks.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-18</td>
      <td style="width: 55%;">
      <strong>A Survey of Machine Unlearning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting"></td>
      <td style="width: 15%;">
        <a href="https://dl.acm.org/doi/full/10.1145/3749987">
        <img src="https://img.shields.io/badge/ACM-Paper-black?labelColor=blue" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • Provides an in-depth exploration of the concept and background of machine unlearning, highlighting its importance in modern machine learning.<br>
          • Machine unlearning aims to enable learning algorithms to effectively remove the influence of specific data without requiring full model retraining.<br>
          • The paper analyzes the necessity, challenges, and design requirements of machine unlearning, reviews current research progress, and emphasizes the field’s complexity and diversity in terms of algorithmic effectiveness, fairness, and privacy protection.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-02</td>
      <td style="width: 55%;">
      <strong>A Survey on the Memory Mechanism of Large Language Model based Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms Badge">
      <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules Badge">
      <td style="width: 15%;">
        <a href="https://dl.acm.org/doi/pdf/10.1145/3748302">
        <img src="https://img.shields.io/badge/ACM-Paper-black?labelColor=blue" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • Explores the memory mechanisms of LLM-based agents, emphasizing the crucial role of memory in agent self-evolution and complex interactions.<br>
          • Systematically summarizes and categorizes existing memory module designs and evaluation methods, while analyzing their roles and limitations across different application scenarios.<br>
          • Such agents are able to improve decision-making and task execution.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-31</td>
      <td style="width: 55%;">
      <strong>A Survey of Machine Unlearning in Large Language Models: Methods, Challenges and Future Directions</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting"></td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2503.01854v2">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • The paper investigates machine unlearning in large language models (LLMs), aiming to effectively remove the influence of undesirable data (e.g., sensitive or illegal information) without full retraining, while preserving overall model utility.<br>
          • It defines the objectives and paradigms of LLM unlearning and establishes a comprehensive taxonomy.<br>
          • The paper reviews existing approaches, evaluates their strengths and limitations, and discusses opportunities for future research.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-27</td>
      <td style="width: 55%;">
      <strong>Rethinking Memory in AI Taxonomy, Operations, Topics, and Future Directions</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
      <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
      <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2505.00675">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • Explores multidimensional research on memory in artificial intelligence (AI), with a particular focus on memory operations and management in large language models (LLMs).<br>
          • Categorizes various types of memory representations and operations—including integration, updating, indexing, forgetting, retrieval, and compression—and provides a systematic analysis of the importance of memory in AI and how it is implemented.<br>
          • Through an extensive review of the literature, the paper identifies four key research themes: long-term memory, parametric memory, long-context memory, and multi-source memory integration.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-24</td>
      <td style="width: 55%;">
      <strong>Cognitive Memory in Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2504.02441">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • Provides a comprehensive examination of memory mechanisms in large language models (LLMs), with a particular focus on different types of memory and their roles within the models.<br>
          • While LLMs excel at information retrieval and interaction summarization, their long-term memory remains unstable.<br>
          • Integrating memory into AI systems is crucial for delivering context-rich responses, reducing hallucinations, improving data processing efficiency, and enabling the self-evolution of AI systems.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-23</td>
      <td style="width: 55%;"><strong>From Human Memory to AI Memory A Survey on Memory Mechanisms in the Era of LLMs </strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Human%20Memory-red" alt="Human Memory">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2504.15965">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • Explores the relationship between human memory and the memory mechanisms of LLM-based artificial intelligence (AI) systems.<br>
          • The main contributions include a systematic definition of memory in LLM-driven AI systems and its conceptual linkage to human memory.<br>
          • The paper proposes a three-dimensional memory taxonomy based on object, form, and time, and summarizes key open issues in current research on personal memory and system memory.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-02</td>
      <td style="width: 55%;"><strong>Digital Forgetting in Large Language Models: A Survey of Unlearning Methods</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2404.02062">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • The paper explores digital forgetting in large language models (LLMs) and corresponding unlearning methods, with a focus on addressing issues related to privacy, copyright, and social ethics.<br>
          • It analyzes different types of model architectures and training processes, as well as practical approaches to digital forgetting, including data retraining, machine unlearning, and prompt engineering.<br>
          • By introducing the concept of “forgetting guarantees,” the paper emphasizes effective mechanisms for both exact and approximate forgetting.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-01-12</td>
      <td style="width: 55%;"><strong>Human-inspired Perspectives: A Survey on AI Long-term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      <img src="https://img.shields.io/badge/Non--Parametric%20Memory-green" alt="Non-Parametric Memory">
      <img src="https://img.shields.io/badge/Sensory%20Memory-brown" alt="Sensory Memory">
      <img src="https://img.shields.io/badge/Working%20Memory-blueviolet" alt="Working Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2411.00489">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • This paper systematically examines the interplay between human long-term memory mechanisms and AI long-term memory, and proposes an adaptive long-term memory cognitive architecture (SALM).<br>
          • It introduces the structure of human memory, including sensory memory, working memory, and different types of long-term memory (episodic, semantic, and procedural memory).<br>
          • The paper analyzes the classification of AI long-term memory—parametric and non-parametric memory—as well as their storage and retrieval mechanisms.
        </td>
    </tr>
  </table>
</details>



<details>
  <summary><strong>Framework & Methods</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
    </tr>
    <tr>
    <td rowspan="2" style="width: 15%;">2026-07-02</td>
    <td style="width: 55%;"><strong>DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models</strong></td>
    <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory_Drift-blue" alt="Memory Drift">
        <img src="https://img.shields.io/badge/Personalization-brightgreen" alt="Personalization">
    </td>
    <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.02374v1">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
    </a></td>
</tr>
  <tr>
      <td colspan="3">
          • DRIFTLENS is a ground-truth-free framework that maps each expressed reasoning step to a value-ontology symbol and measures divergence between a question's no-memory trajectory and its trajectory under injected user-attribute memory, revealing that personalization memory silently reshapes how a model reasons ("symbolic drift"), not just its answer.<br>
          • Measures per-instance reasoning stability of personalized LLMs under memory perturbations using a value ontology and two drift metrics (DTW and SRI) on a benchmark of unverifiable, persona-indifferent questions, and evaluates GRPO- and DPO-based post-training as mitigation.<br>
          • Across four LLMs and 10 user-attribute categories, irrelevant persona memory induces medium-to-large reasoning drift (Cohen's d ≈ 0.35–0.98); GRPO and DPO both reduce drift but neither dominates (e.g., GRPO lowers DTW to 0.186 vs. 0.309 on Gemma2-2B; DPO reaches 0.204 on Qwen3-4B).
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>InduceKV: Fixed-Footprint Continual Adaptation of Multimodal LLMs via Inducing KV Memories</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/KV_Memory-blue" alt="KV Memory">
          <img src="https://img.shields.io/badge/Continual_Learning-brightgreen" alt="Continual Learning">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.02010v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Reframes continual multimodal-LLM adaptation as budgeted online inducing-set selection: task increments are stored as attention-compatible external KV memories (a frozen retrieval key plus compact layerwise KV payloads) injected into self-attention, keeping the backbone frozen under a strict fixed memory budget.<br>
          • Fixed-footprint continual adaptation of MLLMs (task-incremental tuning, continual VQA, domain-incremental, lifelong tuning); extracts attention-ready memory entries and builds a compact inducing set via bilevel optimization (inner retrieval calibration; outer weight selection).<br>
          • Consistently beats PEFT, MoE, replay, and prompt-retrieval baselines under matched budgets; improves over HiDe-LLaVA by 0.88 Avg/1.12 Last on UCIT and 1.35/1.43 on COIN, and raises continual-VQA AP 51.34→52.64 over CL-MoE while outperforming QUAD on VQACL.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--term_Memory-blue" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/State--Aware-brightgreen" alt="State-Aware">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.01935v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Identifies "ghost memory" — a state-coordination failure where old, current, and transition facts coexist and mislead answers — and proposes A-TMA (Adaptive Truth Maintenance Auditing), a state-aware overlay that decouples memory into three diagnosable levels (bank maintenance, retrieval, answer-time resolution).<br>
          • Long-term agent memory under changing user facts; A-TMA keeps superseded/transition records with typed links (a lightweight Sentry gate plus a Qwen2.5-3B Judge), builds state-aligned evidence packets, and conditions QA on explicit labels, alongside a new conflict-heavy benchmark LTP (LoCoMo Temporal Plus).<br>
          • On LTP, Graphiti/Zep +A-TMA improves conflict accuracy by 0.240 absolute (0.480→0.720) and InsideOut+A-TMA lifts Acc from 0.117 to 0.662; on LoCoMo, Graphiti/Zep +A-TMA raises temporal F1 from 0.0295 to 0.1705.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>Learning User-Aware Recall: Personalized Retrieval in Long-Term Conversational Memory</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--term_Memory-blue" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/Personalized_Retrieval-brightgreen" alt="Personalized Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.00017v2">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Profile-guided Personalized Retrieval Optimization (PPRO) makes long-term conversational memory retrieval both user-aware and optimizable by injecting a derived user-profile embedding as an explicit personalized prior into the retrieval ranking score.<br>
          • Personalized long-term conversational QA; PPRO builds episodic and semantic memory banks plus a user profile offline, performs profile-guided dual-path retrieval, and trains a query rewriter with GRPO using evidence-retrieval and answer quality as rewards while keeping memory banks and answer model frozen.<br>
          • On LoCoMo, PPRO gives the best overall F1 across three backbones, beating prior-best SimpleMem by 7–19 points (e.g., GPT-4o overall F1 48.16 vs. 40.87); on LongMemEval-S it reaches 81.5 overall accuracy vs. 75.9 for the best baseline.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>ISM: Self-Improving Strategy Memory for Continual Mathematical Reasoning</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Strategy_Memory-blue" alt="Strategy Memory">
          <img src="https://img.shields.io/badge/Continual_Learning-brightgreen" alt="Continual Learning">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.31191v3">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Intelligent Schema Memory (ISM) is a self-evolving external memory that lets a frozen LLM improve at math reasoning under hard episodic resets by maintaining a compact, bounded bank of strategy schemas with dual representation (stable content + online-adapting feature hook), where every update is gated by symbolic verification.<br>
          • Continual mathematical reasoning under a streaming episode protocol with frozen parameters; ISM uses two-stage retrieval (operator filter + soft scoring), symmetric success/failure learning, and seven self-improvement mechanisms plus conditional schema synthesis.<br>
          • 80.67% on MATH-Hard and 61.67% on OlympiadBench over a 300-episode stream, beating the strongest baseline by +2.00 points on each while storing 64% and 86% fewer schemas (up to 23× fewer entries), with positive backward transfer (+0.03) on OlympiadBench.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-01</td>
      <td style="width: 55%;"><strong>Multi-Head Recurrent Memory Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Recurrent_Memory-blue" alt="Recurrent Memory">
          <img src="https://img.shields.io/badge/Long_Context-brightgreen" alt="Long Context">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.01523v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Decomposes recurrent-memory performance into capture vs. retention, diagnoses retention as the dominant bottleneck (caused by monolithic memory blocks), and proposes Multi-Head Recurrent Memory (MHM) — a training-free framework partitioning memory into independent heads with a stage-wise select-then-update strategy that structurally shields unselected heads from overwriting.<br>
          • Reliable long-context reasoning over 100K–1M tokens; MHM-LRU is a lightweight instantiation that selects the least-recently-updated head each step, guaranteeing uniform head utilization with zero extra token overhead and no retraining.<br>
          • On RULER-HQA at 896K tokens, MHM-LRU lifts retention from less than 30% to 73.96% and accuracy to 49.74% (vs. 21.62% MemAgent, 0.00% native LLM); on BABILong at 1M tokens it reaches 41.41% vs. 25.26% for MemAgent, staying stable where baselines collapse.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-01</td>
      <td style="width: 55%;"><strong>AUTOMEM: Automated Learning of Memory as a Cognitive Skill</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent_Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Metamemory-brightgreen" alt="Metamemory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.01224v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Reframes memory management as an independently trainable "metamemory" skill by promoting file-system operations (read/write/search/append/create) to first-class memory actions alongside task actions, then automates its improvement along scaffold structure and model proficiency via meta-LLM-driven outer loops.<br>
          • Long-horizon procedurally generated games (Crafter, MiniHack, NetHack); Loop 1 (a meta-LLM revises the agent scaffold/file schema) and Loop 2 (a meta-LLM curates good memory decisions to LoRA-finetune a dedicated "memory specialist" while the gameplay model stays frozen).<br>
          • Optimizing memory alone yields ~2×–4× gains on a Qwen2.5-32B base — Crafter 25.0→51.36%, MiniHack 7.5→30.0%, NetHack 0.42→1.85% — bringing the 32B model to the level of frontier systems like Claude Opus 4.5 and Gemini 3.1 Pro Thinking.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-01</td>
      <td style="width: 55%;"><strong>Imprint: Online Memory Compression for Long-Horizon Egocentric QA</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory_Compression-blue" alt="Memory Compression">
          <img src="https://img.shields.io/badge/Egocentric_QA-brightgreen" alt="Egocentric QA">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.00696v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Imprint reframes long-horizon egocentric memory as an online memory compression problem (rather than hierarchical text summarization), representing observations as structured Interaction Records and consolidating them using cognitively-inspired signals of recurrence, recency, and distinctiveness.<br>
          • Long-horizon egocentric QA; parses captions into (person, action, object, timestamps) records via Qwen2.5-7B-Instruct, groups them into event prototypes, scores importance, and consolidates online into a compact retrieval-oriented memory.<br>
          • On the EgoLifeQA 7-day benchmark, improves QA accuracy 31.0%→35.8% and grounded accuracy 10.8%→64.8% (6× more evidence-grounded answers than EgoRAG), while reducing memory footprint 2.3× (109 MB vs. 254 MB) and retrieval latency 11.8× (1.7s vs. 20.1s/query).
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-30</td>
      <td style="width: 55%;"><strong>From Signals to Structure: How Memory Architecture Drives Language Emergence in LLM Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory_Architecture-blue" alt="Memory Architecture">
          <img src="https://img.shields.io/badge/Language_Emergence-brightgreen" alt="Language Emergence">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.00233v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Demonstrates that in Lewis signaling games with frozen LLM agents, memory architecture matters more than channel capacity for language emergence — a persistent private notebook lets agents externalize learned conventions and avoid the high-capacity collapse seen in stateless agents.<br>
          • A two-agent referential signaling game (sender/receiver coordinating a code from scratch) run with gpt-5.4-mini; compares five memory architectures (memory only, env board, scratchpad, codebook, codebook meta) across channel capacities from 4 to 125.<br>
          • The scratchpad notebook achieves the most reliable coordination (0.867 ± 0.023 at capacity=25) while stateless "memory only" peaks at cap=25 then collapses (collision 1.0 at cap=64); the information-bottleneck point (cap=8) is a bimodal fragility point, not a compositional optimum.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-30</td>
      <td style="width: 55%;"><strong>The Past Is Prologue: A Plug-in Controller for Selective Updates in Sequentially Evolving LLM Memory</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent_Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Memory_Update-brightgreen" alt="Memory Update">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.31121v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Janus is a method-agnostic plug-in memory controller that treats each candidate memory update as an accept/reject deployment decision, combining a Memory Momentum Trigger (when to compare old vs. new memory) with a compact hybrid evaluation set of coverage, boundary, and fresh tasks (what to compare on).<br>
          • Sequentially evolving LLM memory for task-solving agents; Janus wraps existing memory updaters (e.g., DC-RS, ExpeL) without changing their update rules, using directional deviation of the memory-update trajectory to trigger bounded-cost old-vs-new validation.<br>
          • Across six datasets, two LLMs (Qwen3-8B, DeepSeek-V4-Flash), and two updaters, Janus improves average accuracy by +2.7 to +4.6 points (e.g., DC-RS 79.5→83.2 and ExpeL 78.3→81.5 on Qwen3-8B).
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-29</td>
      <td style="width: 55%;"><strong>Forensic Trajectory Signatures for Agent Memory Poisoning Detection</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory_Poisoning-blue" alt="Memory Poisoning">
          <img src="https://img.shields.io/badge/Agent_Security-brightgreen" alt="Agent Security">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.30566v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Discovers a mechanistically-forced behavioral invariant ("recall fact before send email") that persistent memory-poisoning attacks imprint on an LLM agent's tool-call trajectory, enabling detection from operation-only tool logs without access to memory contents, model weights, or activations.<br>
          • Detects memory-channel (delayed-trigger) poisoning by extracting 19 trajectory features from trigger-session tool logs and training LR/RF/GBM classifiers, evaluated via 5-fold CV, BCa bootstrap, and leave-one-model-out hold-out on 2,520 runs across 9 models (7B–120B).<br>
          • The single invariant rule alone reaches AUC=0.9563; the full Random Forest reaches AUC=0.9904 (Recall 0.984), with AUC=1.000 on 6/9 cross-model hold-outs and zero-retraining transfer to GPT-4.1/GPT-4o; a prefix-only variant hits AUC=0.934 for inline blocking.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-29</td>
      <td style="width: 55%;"><strong>Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Procedural_Memory-blue" alt="Procedural Memory">
          <img src="https://img.shields.io/badge/Activation_Steering-brightgreen" alt="Activation Steering">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.29824v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • NPM is a training-free framework that represents agent procedural memory as implicit activation-steering vectors in the residual stream rather than explicit textual instructions, distilled from dual-granularity contrastive experiences to overcome the text-action disconnect of RAG-injected guidelines.<br>
          • Procedural memory for LLM agents; pre-computes steering vectors from contrastive success/failure trajectories, then retrieves and dynamically synthesizes a task-specific vector injected at inference time to modulate reasoning and action selection without parameter updates or context expansion.<br>
          • On four benchmarks (ALFWorld, WebShop, ScienceWorld, BabyAI), NPM matches/exceeds explicit textual baselines (e.g., MiniCPM3-4B avg 22.60→28.87; Qwen3-8B 30.63→36.32) and the hybrid NPM+Workflows setting is best overall (Qwen3-8B avg 41.89, ALFWorld 66.42%).
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-29</td>
      <td style="width: 55%;"><strong>Mandol: An Agglomerative Agent Memory System for Long-Term Conversations</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent_Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Long--term_Conversation-brightgreen" alt="Long-term Conversation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.29778v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Mandol consolidates fragmented vector/graph memory into a unified memory-native architecture combining a hierarchical memory model, an agglomerative SemanticMap/SemanticGraph structure that natively fuses key-value/vector/graph storage, and a quantitative retrieval mechanism that runs without invoking LLMs.<br>
          • Long-term cross-session conversational memory; replaces RAG-style recall-then-rank with query-adaptive routing, MAD-based denoising/conflict resolution, and MMR token-constrained context generation over an in-memory unified store (with DuckDB persistence).<br>
          • Best overall accuracy on LoCoMo (92.21%) and LongMemEval (88.40%), with ~5.4× mean retrieval and ~4.8× mean insertion speedup under 10 QPS load, cutting tokens 17.4–20.0% vs. EverMemOS.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-28</td>
      <td style="width: 55%;"><strong>Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory_Consolidation-blue" alt="Memory Consolidation">
          <img src="https://img.shields.io/badge/Memory_Poisoning-brightgreen" alt="Memory Poisoning">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.29279v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Diagnoses "manufactured confidence" — memory-consolidation products (mem0, LangMem) rewrite hedged, casual remarks into confident, dated standalone "facts" that agents then obey, showing agents key on the confidence of phrasing rather than the source, needing no attacker.<br>
          • Uses judge-free access-control and budget-approval agents across five models/four providers to isolate the failure, running the same poisoning protocol against mem0, LangMem, and a verbatim-storage control, and testing framings, source attribution, uncertainty tags, and a hedge-preserving extraction prompt.<br>
          • mem0 and LangMem launder hedged injections into confident facts at 100% (verbatim control 0%); confident framings grant unauthorized access ~0.81 while hedges collapse to ~0.00; a redundant directory restores 0.00 wrong-grant, and hedge-preserving extraction cuts wrong-grant from 0.45 to 0.10.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-28</td>
      <td style="width: 55%;"><strong>Selective Memory Retention for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory_Retention-blue" alt="Memory Retention">
          <img src="https://img.shields.io/badge/Long--Horizon_Agent-brightgreen" alt="Long-Horizon Agent">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.29178v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • TraceRetain is a lightweight capacity-bounded memory-retention framework for frozen LLM agents that scores memory entries by interpretable features (success, age, access frequency, redundancy, specificity, similarity, downstream utility) and evicts the lowest-scoring ones.<br>
          • Formulates external-memory management as a capacity-constrained retention problem on ALFWorld (gpt-5-mini, ReAct-style), comparing TraceRetain-Linear/CEM against cache heuristics (FIFO/LRU/LFU/Random/Ebbinghaus) and unbounded memory under a 75%-distractor noisy-write stress.<br>
          • Methods saturate on clean ALFWorld (47–49/50 vs. 39/50 no-memory); under noisy writes, unbounded and FIFO Precision@5 collapse while TraceRetain-CEM stays stable (16.9%→16.6%) and preserves 97/100 task success, with bounded K=50 matching unbounded K=100.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-27</td>
      <td style="width: 55%;"><strong>Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory_Attack-blue" alt="Memory Attack">
          <img src="https://img.shields.io/badge/Agent_Security-brightgreen" alt="Agent Security">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.29030v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Frames the external memory of LLM agents as an attack surface, showing that misleading or corrupted memories inserted through ordinary natural-language interactions can silently flip an agent's answer even when the current query is clean.<br>
          • Builds a planner-guided LLM QA agent with external memory for four-option MCQ, then applies two attacks — false-information memory injection and interaction-based answer-choice steering — across ML, cybersecurity, and networking on GPT-5.4/GPT-4o mini, Gemma2-9B, and Phi3-14B.<br>
          • Clean baselines average 91.85% (closed) vs. 77.10% (open); false-memory injection causes 82/1064 answer changes (7.80% ASR) with Phi3-14B most vulnerable (34.48% shift in cybersecurity); feedback reinforcement biases answers more than example exposure.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-25</td>
      <td style="width: 55%;"><strong>Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory_Update-blue" alt="Memory Update">
          <img src="https://img.shields.io/badge/RL_Environment-brightgreen" alt="RL Environment">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.27472v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Introduces "supersession" (keeping the current value of a changed fact) as a distinct, trainable failure mode, and releases Supersede — the first RL environment whose reward directly targets temporal fact-currency rather than a proxy, reframing the FAMA metric as a dense training signal.<br>
          • Handling superseded facts in long multi-session dialogue under a bounded, self-maintained memory; diagnoses the gap on the LongMemEval knowledge-update subset and trains it down via GRPO fine-tuning of Qwen2.5-3B with a programmatic supersession-aware reward.<br>
          • Bounded memory drops knowledge-update accuracy 92%→77% on frontier gpt-5.4 (p=0.0033); accuracy falls further as conversations grow 24× (68%→28%); GRPO training nearly doubles held-out supersession accuracy on real unseen conversations (9.0%→16.7%).
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-25</td>
      <td style="width: 55%;"><strong>Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Temporal_Validity-blue" alt="Temporal Validity">
          <img src="https://img.shields.io/badge/Retrieval_Memory-brightgreen" alt="Retrieval Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.26511v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • MemStrata maintains temporal validity via a deterministic (subject, relation, object) supersession rule in a bi-temporal ledger — retiring stale facts with no similarity threshold and no LLM call on the read path — backed by a proof that cosine similarity cannot separate contradictions from duplicates (AUROC 0.59).<br>
          • Keeps agent memory current under evolving knowledge (code renames, config/dependency/API changes); stores facts like RAG for full static recall but supersedes contradicted values, evaluated fully deterministically on a local 7B model across 6 benchmarks.<br>
          • Ties RAG on static knowledge yet reaches 0.95–1.00 accuracy on evolving knowledge vs. RAG's 0.20–0.47 (2–5× gain), drives stale-fact-error rate from 15–40% to ~0%, and runs ~8× faster than LLM-reranking baselines (~2.1s vs. ~16–18s).
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-24</td>
      <td style="width: 55%;"><strong>Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Conversational_Memory-blue" alt="Conversational Memory">
          <img src="https://img.shields.io/badge/Memory_Taxonomy-brightgreen" alt="Memory Taxonomy">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.25361v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Introduces the first fine-grained taxonomy of conversational memory by functional role (answer, clarifying, enriching, distracting, irrelevant) plus a user-centric, context-aware LLM-as-judge evaluation framework covering accuracy, relevance, and informativeness.<br>
          • Controlled comparative experiments on conversational RAG over two long-term multi-session datasets (LongMemEval-m, Long-MT-Bench+) with three frontier LLMs and three retrievers, varying context size and memory-type composition.<br>
          • Clarifying memory reliably improves factual accuracy; distracting memory substantially harms accuracy/relevance; irrelevant memory reduces topic relevance; performance rises then declines as context grows (information overload), and answer memory remains essential.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-23</td>
      <td style="width: 55%;"><strong>Reasoning as Attractor Dynamics: Latent Memory Retrieval via Gibbs-Weighted Energy Minimization</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Associative_Memory-blue" alt="Associative Memory">
          <img src="https://img.shields.io/badge/Test--Time_Compute-brightgreen" alt="Test-Time Compute">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.24543v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Reframes LLM reasoning as retrieval from a Dense Associative Memory — correct chains as flat-minima attractor basins, hallucinations as sharp minima — and introduces a Gibbs-Weighted Basin Selection operator that reweights sampled paths by inverse-square spectral entropy (W ∝ E⁻²).<br>
          • Math reasoning (GSM8K); sample K high-temperature trajectories, compute each path's trajectory energy as length-normalized NLL, then reweight via a post-hoc Gibbs measure to relax into the dominant attractor basin.<br>
          • On GSM8K with Phi-3.5-mini (3.8B), Gibbs-Weighted Retrieval (K=12) reaches 90.07% vs. Standard Sampling/majority-vote 84.69% and Greedy Decoding 78.4% — a +5.38% gain over self-consistency.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-23</td>
      <td style="width: 55%;"><strong>ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Reasoning_Memory-blue" alt="Reasoning Memory">
          <img src="https://img.shields.io/badge/Mixture--of--Agents-brightgreen" alt="Mixture-of-Agents">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.24437v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • A memory-augmented Mixture-of-Agents framework built on a Ranked Reasoning Memory that persistently stores/ranks cross-layer reasoning traces via a comparative Reviewer Agent, paired with Curated Diversified Memory Routing to preserve both reasoning quality and exploration diversity.<br>
          • Scalable multi-agent LLM reasoning; at each layer a Reviewer Agent comparatively scores traces with rationales and later agents receive distinct high/low/contrastive trace subsets, with an optional frontier-model (GPT-5.5) LoRA distillation pipeline to upgrade the Reviewer.<br>
          • Across five reasoning benchmarks (MATH, MMLU-redux, Formal Logic, CRUX, HellaSwag) it consistently beats prior MoA variants and the gap widens with depth — e.g., MATH at L=9: ReM-MoA* 84.0% vs. AttentionMoA 76.9% vs. Standard MoA 61.0%.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-19</td>
      <td style="width: 55%;"><strong>When Does Overlap Help? OSU-Mem and a Cell-Conditional Analysis of Trajectory Memory for LLM Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent_Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Trajectory_Retrieval-brightgreen" alt="Trajectory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.28376v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • OSU-Mem organizes agent trajectory memory into overlapping semantic units with budgeted coarse-to-fine retrieval, and shows via cell-conditional analysis that overlap helps only when evidence steps share tool calls or entities (T+E+) and hurts when they share neither (T−E−).<br>
          • Budgeted retrieval from long-horizon LLM-agent trajectories under a strict token budget; builds OSUs from entity/tool/subgoal/similarity views, then query-adaptive centroid-scored expansion, evaluated on a synthetic benchmark, τ-bench, and ToolBench with a 2×2 tool/entity cross-tabulation.<br>
          • +39.9% Recall and +61.5% Hit@2 over the strongest baseline at B=256 on the synthetic benchmark; wins on T+E+ but loses on T−E− in τ-bench; on ToolBench overlap beats disjoint construction with a monotonic dose-response.
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-05-30</td>
      <td style="width: 55%;"><strong>Memory Shot for Long-Term Dialogue</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Dialogue_Memory-blue" alt="Dialogue Memory">
          <img src="https://img.shields.io/badge/Visual_Memory-brightgreen" alt="Visual Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.28338v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • MemShot renders raw dialogue spans directly into structured visual "memory shots" (images preserving speaker turns, timestamps, and turn boundaries) and leverages an MLLM's internal visual reasoning, avoiding fragile, heavyweight text-based memory construction.<br>
          • Long-term dialogue memory-augmented QA; segments dialogue into contiguous spans, renders each into a hierarchical header+chat visual unit, retrieves top-k units (Qwen3-VL-Embedding-8B), and answers with Qwen3-VL-Instruct MLLMs (2B/8B/32B).<br>
          • Competitive-to-superior on LoCoMo (79.61 overall Acc @32B) and LongMemEval (74.80 overall Acc @32B) while delivering ~70× faster memory construction (≈9.56s), beating visual-memory baseline MemOCR by over 10%.
      </td>
  </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-25</td>
        <td style="width: 55%;"><strong>MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agentic%20RAG-4A90E2" alt="Agentic RAG">
          <img src="https://img.shields.io/badge/Red%20Teaming-F5A623" alt="Red Teaming">
          <img src="https://img.shields.io/badge/Memory%20Guided%20Search-7ED321" alt="Memory Guided Search">
          <img src="https://img.shields.io/badge/Security-D0021B" alt="Security">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.26793v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • This paper studies red-teaming for multimodal agentic RAG systems whose attack surface spans retrieved text, images, direct user queries, and orchestrator-level tool manipulation.<br>
          • MIRROR combines an episodic memory bank of successful attack traces with Monte Carlo tree search; retrieved memories provide search priors, while a deterministic novelty gate blocks copying from known or retrieved attacks.<br>
          • Across four attack surfaces, the framework validates candidates through deterministic replay or structured tool-call parsing, aiming to make memory-guided adversarial search both more effective and less dependent on recycled templates.
        </td>
      </tr>
        <tr>
          <td rowspan="2" style="width: 15%;">2026-06-23</td>
          <td style="width: 55%;"><strong>Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning</strong></td>
          <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Experience%20Learning-4A90E2" alt="Experience Learning">
            <img src="https://img.shields.io/badge/Agent%20Memory-F5A623" alt="Agent Memory">
            <img src="https://img.shields.io/badge/Verification-7ED321" alt="Verification">
            <img src="https://img.shields.io/badge/Self--Evolution-D0021B" alt="Self-Evolution">
          </td>
          <td style="width: 15%;">
            <a href="https://arxiv.org/pdf/2606.24428v1">
              <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
            </a>
          </td>
        </tr>
        <tr>
          <td colspan="3">
            • This paper studies experience-driven self-evolution for LLM agents and identifies a Self-Confirmation Trap: single-agent loops may treat wrong-but-self-consistent trajectories as successful experience, causing erroneous memories to be retrieved and reused later.<br>
            • It proposes EDV, an Execute-Distill-Verify framework in which multiple heterogeneous agents first explore the same task space, a third-party distillation agent compares candidate trajectories to produce experience candidates, and an execution group verifies them through consensus before memory insertion.<br>
            • By decoupling execution, experience distillation, and verification, EDV turns isolated self-reflection into collaborative experience construction and filters noisy or erroneous content before it enters shared or private memory. Experiments on tau2-bench, Mind2Web, and MMTB show consistent improvements over strong baselines, highlighting the importance of reliable memory construction for agent self-evolution.
          </td>
        </tr>
        <tr>
          <td rowspan="2" style="width: 15%;">2026-06-18</td>
          <td style="width: 55%;"><strong>Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention</strong></td>
          <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Self--Attention-4A90E2" alt="Self-Attention">
            <img src="https://img.shields.io/badge/Mixture--of--Experts-F5A623" alt="Mixture-of-Experts">
            <img src="https://img.shields.io/badge/Grouped--Query%20Attention-7ED321" alt="Grouped-Query Attention">
            <img src="https://img.shields.io/badge/Long%20Context-D0021B" alt="Long Context">
          </td>
          <td style="width: 15%;">
            <a href="https://arxiv.org/pdf/2606.20945v2">
              <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
            </a>
          </td>
        </tr>
        <tr>
          <td colspan="3">
            • This paper proposes Grouped Query Experts (GQE), a mixture-of-experts layer on top of grouped-query attention that targets the high cost of dense self-attention at long context lengths.<br>
            • Within each GQA group, a router selects k query-head experts per token while leaving all key-value heads dense and unchanged. This preserves the KV-cache advantages of GQA while reducing active query-head computation according to token difficulty or information content.<br>
            • On a fixed 30B token budget at the 250M parameter scale, GQE matches the downstream accuracy of an all-active GQA baseline while activating only half of the query heads per token, suggesting a path to more efficient long-context processing.
          </td>
        </tr>
        <tr>
          <td rowspan="2" style="width: 15%;">2026-06-18</td>
          <td style="width: 55%;"><strong>Multi-Agent Transactive Memory</strong></td>
          <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Multi%20Agent%20Systems-4A90E2" alt="Multi-Agent Systems">
            <img src="https://img.shields.io/badge/Transactive%20Memory-F5A623" alt="Transactive Memory">
            <img src="https://img.shields.io/badge/Trajectory%20Retrieval-7ED321" alt="Trajectory Retrieval">
            <img src="https://img.shields.io/badge/Knowledge%20Sharing-D0021B" alt="Knowledge Sharing">
          </td>
          <td style="width: 15%;">
            <a href="https://arxiv.org/pdf/2606.19911v1">
              <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
            </a>
          </td>
        </tr>
        <tr>
          <td colspan="3">
            • This paper introduces Multi-Agent Transactive Memory (MATM), which organizes action–observation trajectories generated by heterogeneous agents into group-level shared memory. Producer agents contribute execution experience, while consumer agents retrieve prior trajectories, enabling the reuse of procedural knowledge that would otherwise be discarded after a single task.<br>
            • MATM employs a state-conditioned key–value index, using the current task and recent interaction history as retrieval keys and subsequent trajectory segments as values. It further applies a learning-to-rank model that integrates producer reliability, consumer characteristics, retrieval scores, and trajectory attributes to perform personalized reranking.<br>
            • Experiments in ALFWorld and WebArena demonstrate that retrieving shared trajectories improves task performance and reduces interaction steps without requiring direct inter-agent coordination or joint training, with benefits extending across agents of varying capability levels. The work thereby extends individual experiential memory into a collective knowledge infrastructure for open agent ecosystems.
          </td>
        </tr>
        <tr>
          <td rowspan="2" style="width: 15%;">2026-06-17</td>
          <td style="width: 55%;"><strong>What Must Generalist Agents Remember?</strong></td>
          <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Theoretical%20Analysis-4A90E2" alt="Theoretical Analysis">
            <img src="https://img.shields.io/badge/Memory%20Necessity-F5A623" alt="Memory Necessity">
            <img src="https://img.shields.io/badge/Domain%20Disambiguation-7ED321" alt="Domain Disambiguation">
            <img src="https://img.shields.io/badge/Model%20Reconstruction-D0021B" alt="Model Reconstruction">
          </td>
          <td style="width: 15%;">
            <a href="https://arxiv.org/pdf/2606.18746">
              <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
            </a>
          </td>
        </tr>
        <tr>
          <td colspan="3">
            • This paper formally investigates the information that generalist agents must retain to sustain near-optimal behavior across multiple environments and objectives. It defines states with identical observations but conflicting optimal actions as observational bottlenecks that reveal the necessity of memory.<br>
            • The separation theorem establishes that when different domains require mutually incompatible optimal actions at such a bottleneck, any unified near-optimal policy must induce distinct memory distributions. Consequently, a memoryless policy that relies solely on the current observation cannot simultaneously maintain a high success rate and cross-domain robustness.<br>
            • The paper further proves that if memory is sufficient to estimate the value functions of a set of relevant objectives, local transition dynamics can be approximately reconstructed from it. Memory therefore serves simultaneously as a mechanism for domain disambiguation, environment-model reconstruction, and a substrate for planning. These findings establish theoretical necessity but do not directly prescribe a specific engineering architecture for memory.
          </td>
        </tr>
        <tr>
          <td rowspan="2" style="width: 15%;">2026-06-17</td>
          <td style="width: 55%;"><strong>User as Engram: Internalizing Per-User Memory as Local Parametric Edits</strong></td>
          <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Personalized%20Memory-4A90E2" alt="Personalized Memory">
            <img src="https://img.shields.io/badge/Local%20Parametric%20Edits-F5A623" alt="Local Parametric Edits">
            <img src="https://img.shields.io/badge/Content%20Skill%20Separation-7ED321" alt="Content-Skill Separation">
            <img src="https://img.shields.io/badge/Engram%20Architecture-D0021B" alt="Engram Architecture">
          </td>
          <td style="width: 15%;">
            <a href="https://arxiv.org/pdf/2606.19172">
              <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
            </a>
          </td>
        </tr>
        <tr>
          <td colspan="3">
            • This paper decomposes personalized memory into user-specific content and reasoning skills shared across users. It proposes storing user facts through localized row edits in the hash-keyed memory table of the Engram model, while a single shared adapter provides fact interpretation and indirect reasoning capabilities.<br>
            • Unlike per-user LoRA modules, which exert dense effects on global weights, localized Engram edits operate only at precisely triggered positions and leave all other positions unchanged. Facts belonging to different users are written into non-overlapping hash slots, enabling additive and lossless multi-user composition within a shared table.<br>
            • The paper reports that the proposed design matches per-user LoRA in direct recall, improves indirect-reasoning accuracy by an average factor of 5.6, and reduces memory consumption by approximately 33,000 times. After roughly 100 facts, it also outperforms retrieval pipelines using larger models. Its applicability, however, depends on the underlying model possessing an editable Engram memory architecture.
          </td>
        </tr>
        <tr>
          <td rowspan="2" style="width: 15%;">2026-06-16</td>
          <td style="width: 55%;"><strong>Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning</strong></td>
          <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Verbal%20Reinforcement%20Learning-4A90E2" alt="Verbal Reinforcement Learning">
            <img src="https://img.shields.io/badge/Insight%20Governance-F5A623" alt="Insight Governance">
            <img src="https://img.shields.io/badge/Structured%20Evidence-7ED321" alt="Structured Evidence">
            <img src="https://img.shields.io/badge/Nonstationary%20Environments-D0021B" alt="Non-stationary Environments">
          </td>
          <td style="width: 15%;">
            <a href="https://arxiv.org/pdf/2606.17591">
              <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
            </a>
          </td>
        </tr>
        <tr>
          <td colspan="3">
            • This paper identifies a retention–forgetting dilemma faced by parameter-free verbal reinforcement learning in non-stationary environments: retaining obsolet