# Awesome Deliberative Prompting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [!NOTE]
> _Deliberative prompting_, _chain-of-thought_, _self-reflection_ and _thinking_ have become mainstream techniques in AI. This archived opinionated reading lists documents the journey the community has taken to achieve this feat in less than 4 years, from the beginnings in 2021 to January 2025, when Deepseek R1 has been released. Thanks for following.

**How to ask Large Language Models (LLMs) to produce reliable reasoning and make reason-responsive decisions.**

> **deliberation**, n.
>
> The action of thinking carefully about something, esp. in order to reach a decision; careful consideration; an act or instance of this. (OED)


## Contents

- [Success Stories](#success-stories)
- [Prompting Patterns and Strategies](#prompting-patterns-and-strategies)
  - [Beyond "Let's think step by step"](#beyond-lets-think-step-by-step)
  - [Multi-Agent Deliberation](#multi-agent-deliberation)
  - [Reflection and Meta-Cognition](#reflection-and-meta-cognition)
- [Text Generation Techniques](#text-generation-techniques)
- [Self-Correction](#self-correction)
- [Reasoning Analytics](#reasoning-analytics)
- [Limitations, Failures, Puzzles](#limitations-failures-puzzles)
- [Datasets](#datasets)
- [Tools and Frameworks](#tools-and-frameworks)
- [Other Resources](#other-resources)


## Success Stories

_Striking evidence for effectiveness of deliberative prompting._

- 🎓 One of the first attempts to elicit reasoning traces from LLMs to improve performance, includes experiments with GPT-2. "Thinking Aloud: Dynamic Context Generation Improves Zero-Shot Reasoning Performance of GPT-2." 2021-03-24. [[>paper](https://arxiv.org/abs/2103.13033)]
- 🎓 The original "chain of though" (CoT) paper, first to give clear evidence that deliberative prompting works. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." 2022-01-28. [[>paper](https://arxiv.org/abs/2201.11903)]
- 🎓 Deliberative prompting improves ability of Google's LLMs to solve unseen difficult problems, and instruction-finetuned (Flan-) models are much better at it.
  - "Scaling Instruction-Finetuned Language Models." 2022-12-06. [[>paper](https://arxiv.org/abs/2210.11416)]
  - "PaLM 2 Technical Report." 2023-05-17. [[>paper](https://arxiv.org/abs/2305.10403)]
- 🎓 Deliberative prompting is highly effective for OpenAI's models (Text-Davinci-003, ChatGPT, GPT-4), increasing accuracy in many (yet not all) reasoning tasks in the EvalAGI benchmark. "AGIEval: A Human-Centric Benchmark for
Evaluating Foundation Models." 2023-04-13. [[>paper](https://arxiv.org/abs/2304.06364)]
- 🎓 Deliberative prompting unlocks latent cognitive skills and is more effective for bigger models. "Challenging BIG-Bench tasks and whether chain-of-thought can solve them." 2022-10-17. [[>paper](https://arxiv.org/abs/2210.09261)]
- 🎓 Experimentally introducing errors in CoT reasoning traces decreases decision accuracy, which provides indirect evidence for reason-responsiveness of LLMs. "Stress Testing Chain-of-Thought Prompting for Large Language Models." 2023-09-28. [[>paper](https://arxiv.org/abs/2309.16621)]
- 🎓 Reasoning (about retrieval candidates) improves RAG. "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection." 2023-10-17. [[>paper](https://arxiv.org/abs/2310.11511)]
- 🎓 Deliberative reading notes improve RAG. "Chain-of-Note: Enhancing Robustness in Retrieval-Augmented Language Models." 2023-11-15. [[>paper](https://arxiv.org/abs/2311.09210)]
- 🎓 Good reasoning (CoT) causes good answers (i.e., LLMs are reason-responsive). "Causal Abstraction for Chain-of-Thought Reasoning in Arithmetic Word Problems." 2023-12-07. [[>paper](https://aclanthology.org/2023.blackboxnlp-1.12.pdf)]
- 🎓 Logical interpretation of internal layer-wise processing of reasoning tasks yields further evidence for reason-responsiveness. "Towards a Mechanistic Interpretation of Multi-Step Reasoning Capabilities of Language Model." 2023-12-07. [[>paper](https://arxiv.org/abs/2310.14491)]
- 🎓 Reasoning about alternative drafts improves text generation. "Self-Evaluation Improves Selective Generation in Large Language Models." 2023-12-14. [[>paper](https://arxiv.org/abs/2312.09300)]
- 🎓 CoT with carefully retrieved, diverse reasoning demonstrations boosts multi-modal LLMs. "Retrieval-augmented Multi-modal Chain-of-Thoughts Reasoning for Large Language Models." 2023-12-04. [[>paper](https://arxiv.org/abs/2312.01714)]
- 🎓 Effective multi-hop CoT for visual question answering. "II-MMR: Identifying and Improving Multi-modal Multi-hop Reasoning in Visual Question Answering." 2024-02-16. [[>paper](https://arxiv.org/abs/2402.11058)]
- 🎓 👩‍💻 DPO on synthetic CoT traces increases reason-responsiveness of small LLMs. "Making Reasoning Matter:
Measuring and Improving Faithfulness of Chain-of-Thought Reasoning" 2024-02-23. [[>paper](https://arxiv.org/abs/2402.13950)] [[>code](https://debjitpaul.github.io/reasoningmatter)]
- 🎓 The impressive Deepseek R1 demonstrates that LLMs can learn effective problem solving, reflection, self-validation and self-correction through RL alone. "Deepseek R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" 2025-02-03. [[>paper](https://deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf)]


## Prompting Patterns and Strategies 

_Prompting strategies and patterns to make LLMs deliberate._


### Beyond "Let's think step by step" 

_Instructing LLMs to reason (in a specific way)._


- 🎓 Asking GPT-4 to provide a correct and a wrong answers boosts accuracy. "Large Language Models are Contrastive Reasoners." 2024-03-13. [[>paper](https://arxiv.org/abs/2403.08211)]
- 🔥🎓 Guided dynamic prompting increases GPT-4 CoT performance by up to 30 percentage points. "Structure Guided Prompt: Instructing Large Language Model in Multi-Step Reasoning by Exploring Graph Structure of the Text" 2024-02-20. [[>paper](https://arxiv.org/abs/2402.13415)]
- 🎓 Letting LLMs choose and combine reasoning strategies is cost-efficient and improves performance. "SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures." 2024-02-06. [[>paper](https://arxiv.org/abs/2402.03620)]
- 🎓 CoA: Produce an abstract reasoning trace first, and fill in the details (using tools) later. "Efficient Tool Use with Chain-of-Abstraction Reasoning." 2024-01-30. [[>paper](https://arxiv.org/abs/2401.17464)]
- 🎓 Reason over and over again until verification test is passed. "Plan, Verify and Switch: Integrated Reasoning with Diverse X-of-Thoughts." 2023-10-23. [[>paper](https://arxiv.org/abs/2310.14628)]
- 🎓 Generate multiple diverse deliberations, then synthesize those in a single reasoning path. "Ask One More Time: Self-Agreement Improves Reasoning of Language Models in (Almost) All Scenarios." 2023-11-14. [[>paper](https://arxiv.org/abs/2311.08154)]
- 🎓 Survey of CoT regarding task types, prompt designs, and reasoning quality metrics. "Towards Better Chain-of-Thought Prompting Strategies: A Survey." 2023-10-08. [[>paper](https://arxiv.org/abs/2310.04959)]
- 🎓 Asking a LLM about a problem's broader context leads to better answers. "Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models." 2023-10-09. [[>paper](https://arxiv.org/abs/2310.06117)]
- Weighing Pros and Cons: This universal deliberation paradigm can be implemented with LLMs.
  - 👩‍💻 A _{{guidance}}_ program that does: 1. Identify Options → 2. Generate Pros and Cons → 3. Weigh Reasons → 4. Decide. [[>code](https://guidance-ai/guidance/blob/main/README.md#role-based-chat-model-example-notebook)]
- 🎓 👩‍💻 Plan-and-Solve Prompting. "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought
Reasoning by Large Language Models." 2023-05-06. [[>paper](https://aclanthology.org/2023.acl-long.147.pdf)] [[>code](https://AGI-Edgerunners/Plan-and-Solve-Prompting)]
- 🎓 Note-Taking. "Learning to Reason and Memorize with Self-Notes." 2023-05-01. [[>paper](https://arxiv.org/abs/2305.00833)]
- 🎓 Deliberate-then-Generate improves text quality. "Deliberate then Generate: Enhanced Prompting Framework for Text Generation." 2023-05-31. [[>paper](https://arxiv.org/abs/2305.19835)]
- 🎓 Make LLM spontaneously interleave reasoning and Q/A. "ReAct: Synergizing Reasoning and Acting in Language Models." 2022-10-06. [[>paper](https://arxiv.org/abs/2210.03629)]
- 🎓 'Divide-and-Conquer' instructions substantially outperform standard CoT. "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models" 2022-05-21. [[>paper](https://arxiv.org/pdf/2205.10625.pdf)]


### Multi-Agent Deliberation

_Let one (or many) LLMs simulate a free controversy._


- 🎓 👩‍💻 Carefully selected open LLMs that iteratively review and improve their answers outperform GPT4-o. "Mixture-of-Agents Enhances Large Language Model Capabilities." 2024-06-10. [[>paper](https://arxiv.org/abs/2406.04692)] [[>code](https://togethercomputer/moa)]
- 🎓 More elaborate and costly multi-agent-system designs are typically more effective, according to this review: "Are we going MAD? Benchmarking Multi-Agent Debate between Language Models for Medical Q&A." 2023-11-19. [[>paper](https://arxiv.org/abs/2311.17371)]
- 🎓 Systematic peer review is even better than multi-agent debate. "Towards Reasoning in Large Language Models via Multi-Agent Peer Review Collaboration." 2023-11-14. [[>paper](https://arxiv.org/abs/2311.08152)]
- 🎓 Collective critique and reflection reduce factual hallucinations and toxicity. "N-Critics: Self-Refinement of Large Language Models with Ensemble of Critics." 2023-10-28. [[>paper](https://arxiv.org/abs/2310.18679)]
- 🎓 👩‍💻 Delphi-process with diverse LLMs is veristically more valuable than simple debating. "ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs." 2023-09-22. [[>paper](https://arxiv.org/abs/2309.13007)] [[>code](https://dinobby/ReConcile)]
- 🎓 Multi-agent debate increases cognitive diversity increases performance. "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate." 2023-05-30. [[>paper](https://arxiv.org/abs/2305.19118)]
- 🎓 Leverage wisdom of the crowd effects through debate simulation. "Improving Factuality and Reasoning in Language Models through Multiagent Debate." 2023-05-23. [[>paper](https://arxiv.org/abs/2305.14325)] 
- 🎓 👩‍💻 Emulate Socratic dialogue to collaboratively solve problems with multiple AI agents. "The Socratic Method for Self-Discovery in Large Language Models." 2023-05-05. [[>blog](https://princeton-nlp.github.io/SocraticAI/)] [[>code](https://RunzheYang/SocraticAI)]


### Reflection and Meta-Cognition

_Higher-order reasoning strategies that may improve first-order deliberation._


- 🎓 👩‍💻 Keeping track of *general* insights gained from CoT problem solving improves future accuracy and efficiency. "Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models." 2024-06-06. [[>paper](https://arxiv.org/abs/2406.04271)] [[>code](https://YangLing0818/buffer-of-thought-llm)] 
- 🎓 👩‍💻 Processing task in function of self-assessed difficulty boosts CoT effectiveness. "Divide and Conquer for Large Language Models Reasoning." 2024-01-10. [[>paper](https://arxiv.org/abs/2401.05190)] [[>code](https://AiMijie/Divide-and-Conquer)] 
- 🎓 👩‍💻 Reflecting on task allows LLM to autogenerate more effective instructions, demonstration, and reasoning traces. "Meta-CoT: Generalizable Chain-of-Thought Prompting in Mixed-task Scenarios with Large Language Models." 2023-10-11. [[>paper](https://arxiv.org/abs/2310.06692)] [[>code](https://Anni-Zou/Meta-CoT)] 
- 🎓 👩‍💻 LLM-based AI Instructor devises effective first-order CoT-instructions (open source models improve by up to 20%). "Agent Instructs Large Language Models to be General Zero-Shot Reasoners." 2023-10-05. [[>paper](https://arxiv.org/abs/2310.03710)] [[>code](https://wang-research-lab/agentinstruct)]
- 🎓 👩‍💻 Clarify→Judge→Evaluate→Confirm→Qualify Paradigm. "Metacognitive Prompting Improves Understanding in Large Language Models." 2023-08-10. [[>paper](https://arxiv.org/abs/2308.05342)] [[>code](https://EternityYW/Metacognitive-Prompting)]
- 🎓 👩‍💻 Find-then-simulate-an-expert-for-this-problem Strategy. "Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm." 2021-02-15. [[>paper](https://arxiv.org/abs/2102.07350)] [[>lmql][lmql-playground]] 


## Text Generation Techniques 

_Text generation techniques, which can be combined with prompting patterns and strategies._

- 🔥🎓 Iterative revision of reasoning in light of previous CoT traces improves accuracy by 10-20%. "RAT: Retrieval Augmented Thoughts Elicit
Context-Aware Reasoning in Long-Horizon Generation". 2024-03-08. [[>paper](https://arxiv.org/abs/2403.05313)]
- 🎓 Pipeline for self-generating & choosing effective CoT few-shot demonstrations. "Universal Self-adaptive Prompting". 2023-05-24. [[>paper](https://arxiv.org/abs/2305.14926)]
- 🎓 More reasoning (= longer reasoning traces) is better. "The Impact of Reasoning Step Length on Large Language Models". 2024-01-10. [[>paper](https://arxiv.org/abs/2401.04925)]
- 🎓 Having (accordingly labeled) correct _and_ erroneous (few-shot) reasoning demonstrations improves CoT. "Contrastive Chain-of-Thought Prompting." 2023-11-17. [[>paper](https://arxiv.org/abs/2311.09277)]
- 🎓 Better problem-solving and deliberation through few-shot trial-and-error (in-context RL). "Reflexion: Language Agents with Verbal Reinforcement Learning." 2023-03-20. [[>paper](https://arxiv.org/abs/2303.11366)]
- 🎓 External guides that constrain generation of reasoning improve accuracy by up to 35% on selected tasks. "Certified Reasoning with Language Models." 2023-06-06. [[>paper](https://arxiv.org/abs/2306.04031)]
- 🎓 👩‍💻 Highly effective beam search for generating complex, multi-step reasoning episodes. "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." 2023-05-17. [[>paper](https://arxiv.org/abs/2305.10601)] [[>code](https://princeton-nlp/tree-of-thought-llm)]
  - 👩‍💻 A minimalistic implementation of Tree-of-Thoughts as plain prompt. [[>code](https://dave1010/tree-of-thought-prompting)]
  - 👩‍💻 An experimental [LMQL][lmql-site] implementation of Tree-of-Thoughts. [[>code](https://LachlanGray/lmql-tree-of-thoughts)]
- 🎓 👩‍💻 LLM auto-generates diverse reasoning demonstration to-be-used in deliberative prompting. "Automatic Chain of Thought Prompting in Large Language Models." 2022-10-07. [[>paper](https://arxiv.org/abs/2210.03493)] [[>code](https://amazon-science/auto-cot)]

## Self-Correction

_Let LLMs self-correct their deliberation._


- 🎓 Consistency between multiple CoT-traces is an indicator of reasoning reliability, which can be exploited for self-check / aggregation. "Can We Verify Step by Step for Incorrect Answer Detection?" 2024-02-16. [[>paper](https://arxiv.org/abs/2402.10528)]
- 🎓 Turn LLMs into intrinsic self-checkers by appending self-correction steps to standard CoT traces for finetuning. "Small Language Model Can Self-correct." 2024-01-14. [[>paper](https://arxiv.org/abs/2401.07301)]
- 🎓 Reinforced Self-Training improves retrieval-augmented multi-hop Q/A. "ReST meets ReAct: Self-Improvement for Multi-Step Reasoning LLM Agent." 2023-12-15. [[>paper](https://arxiv.org/abs/2312.10003)]
- 🎓 Conditional self-correction depending on whether critical questions have been addressed in reasoning trace. "The ART of LLM Refinement: Ask, Refine, and Trust." 2023-11-14. [[>paper](https://arxiv.org/abs/2311.07961)]
- 🎓 Iteratively refining reasoning given diverse feedback increases accuaracy by up tp 10% (ChatGPT). "MAF: Multi-Aspect Feedback for Improving Reasoning in Large Language Models." 2023-10-19. [[>paper](https://arxiv.org/abs/2310.12426)]
- 🎓 Instructing a model just to "review" its answer and "find problems" doesn't lead to effective self-correction. "Large Language Models Cannot Self-Correct Reasoning Yet." 2023-09-25. [[>paper](https://arxiv.org/abs/2310.01798)]
- 🎓 LLMs can come up with, and address critical questions to improve their drafts. "Chain-of-Verification Reduces Hallucination in Large Language Models." 2023-09-25. [[>paper](https://arxiv.org/abs/2309.11495)]
- 🎓 LogiCoT: Self-check and revision after each CoT step improves performance (for selected tasks and models). "Enhancing Zero-Shot Chain-of-Thought Reasoning in Large Language Models through Logic." 2023-09-23. [[>paper](https://arxiv.org/abs/2309.13339)]
- 🎓 Excellent review about self-correcting LLMs, with application to unfaithful reasoning. "Automatically Correcting Large Language Models: Surveying the landscape of diverse self-correction strategies." 2023-08-06. [[>paper](https://arxiv.org/abs/2308.03188)]


## Reasoning Analytics

_Methods for analysing LLM deliberation and assessing reasoning quality._

- 🎓👩‍💻 Comprehensive LLM-based reasoning analytics that breaks texts down into individual reasons. "DCR-Consistency: Divide-Conquer-Reasoning for Consistency Evaluation and Improvement of Large Language Models." 2024-01-04. [[>paper](https://arxiv.org/abs/2401.02132)] [[>code](https://intuit-ai-research/DCR-consistency)]
- 🎓🤗 Highly performant, open LLM (T5-based) for inference verification. "Minds versus Machines: Rethinking Entailment Verification with Language Models." 2024-02-06. [[>paper](https://arxiv.org/abs/2402.03686)] [[>model](soumyasanyal/entailment-verifier-xxl)]
- 🎓👩‍💻 Test dataset for CoT evaluators. "A Chain-of-Thought Is as Strong as Its Weakest Link: A Benchmark for Verifiers of Reasoning Chains." 2023-11-23. [[>paper](https://arxiv.org/abs/2402.00559)] [[>dataset](https://huggingface.co/datasets/google/reveal)]
- 🎓👩‍💻 Framework for evaluating reasoning chains by viewing them as informal proofs that derive the final answer. "ReCEval: Evaluating Reasoning Chains via Correctness and Informativeness." 2023-11-23. [[>paper](https://arxiv.org/abs/2304.10703)] [[>code](https://archiki/ReCEval)]
- 🎓 GPT-4 is 5x better at predicting whether math reasoning is correct than GPT-3.5. "Challenge LLMs to Reason About Reasoning: A Benchmark to Unveil Cognitive Depth in LLMs." 2023-12-28. [[>paper](https://arxiv.org/abs/2312.17080)]
- 🎓 Minimalistic GPT-4 prompts for assessing reasoning quality. "SocREval: Large Language Models with the Socratic Method for Reference-Free Reasoning Evaluation." 2023-09-29. [[>paper](https://arxiv.org/abs/2310.00074)] [[>code](https://facebookresearch/ParlAI/tree/main/projects/roscoe#meta-evaluation)]
- 🎓👩‍💻 Automatic, semantic-similarity based metrics for assessing CoT traces (redundancy, faithfulness, consistency, etc.). "ROSCOE: A Suite of Metrics for Scoring Step-by-Step Reasoning." 2023-09-12. [[>paper](https://arxiv.org/abs/2212.07919)]


## Limitations, Failures, Puzzles

_Things that don't work, or are poorly understood._

- 🎓 Structured generation risks to degrade reasoning quality and CoT effectiveness. "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models." 2024-08-05. [[>paper](https://arxiv.org/abs/2408.02442)]
- 🎓 Filler tokens can be as effective as sound reasoning traces for eliciting correct answers. "Let's Think Dot by Dot: Hidden Computation in Transformer Language Models." 2024-04-24. [[>paper](https://arxiv.org/abs/2404.15758)]
- 🔥🎓 Causal analysis shows that LLMs sometimes ignore CoT traces, but reason responsiveness increases with model size, and is shaped by fine-tuning. "LLMs with Chain-of-Thought Are Non-Causal Reasoners" 2024-02-25. [[>paper](https://arxiv.org/abs/2402.16048)]
- 🎓 Bad reasoning may lead to correct conclusions, hence better methods for CoT evaluation are needed. "SCORE: A framework for Self-Contradictory Reasoning Evaluation." 2023-11-16. [[>paper](https://arxiv.org/abs/2311.09603)]
- 🎓 LLMs may produce "encoded reasoning" that's unintelligable to humans, which may nullify any XAI gains from deliberative prompting. "Preventing Language Models From Hiding Their Reasoning." 2023-10-27. [[>paper](https://arxiv.org/abs/2310.18512)]
- 🎓 LLMs judge and decide in function of available arguments (reason-responsiveness), but are more strongly influenced by fallacious and deceptive reasons as compared to sound ones. "How susceptible are LLMs to Logical Fallacies?" 2023-08-18. [[>paper](https://arxiv.org/abs/2308.09853)]
- 🎓 Incorrect reasoning improves answer accuracy (nearly) as much as correct one. "Invalid Logic, Equivalent Gains: The Bizarreness of Reasoning in Language Model Prompting." 2023-07-20. [[>paper](https://arxiv.org/abs/2307.10573)]
- 🎓 Zeroshot CoT reasoning in sensitive domains increases a LLM's likelihood to produce harmful or undesirable output. "On Second Thought, Let's Not Think Step by Step! Bias and Toxicity in Zero-Shot Reasoning." 2023-06-23. [[>paper](https://arxiv.org/abs/2212.08061)]
- 🎓 LLMs may systematically fabricate erroneous CoT rationales for wrong answers, NYU/Anthropic team finds. "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting." 2023-05-07. [[>paper](https://arxiv.org/abs/2305.04388)] 
- 🎓 LLMs' practical deliberation is not robust, but easily let astray by re-wording scenarios. "Despite 'super-human' performance, current LLMs are unsuited for decisions about ethics and safety" 2022-12-13. [[>paper](https://arxiv.org/abs/2212.06295)] 


## Datasets

_Datasets containing examples of deliberative prompting, potentially useful for training models / assessing their deliberation skills._

- Instruction-following dataset augmented with "reasoning traces" generated by LLMs.
  - 🎓 _ORCA_ - Microsoft's original paper. "Orca: Progressive Learning from Complex Explanation Traces of GPT-4." 2023-06-05. [[>paper](https://arxiv.org/abs/2306.02707)] 
  - 👩‍💻 _OpenOrca_ - Open source replication of ORCA datasets. [[>dataset](https://huggingface.co/datasets/Open-Orca/OpenOrca)]  
  - 👩‍💻 _Dolphin_ - Open source replication of ORCA datasets. [[>dataset](https://huggingface.co/datasets/ehartford/dolphin)]  
  - 🎓 _ORCA 2_ - Improved Orca by Microsoft, e.g. with meta reasoning. "Orca 2: Teaching Small Language Models How to Reason." 2023-11-18. [[>paper](https://arxiv.org/abs/2311.11045)]
- 🎓👩‍💻 _CoT Collection_ - 1.84 million reasoning traces for 1,060 tasks. "The CoT Collection: Improving Zero-shot and Few-shot Learning of Language Models via Chain-of-Thought Fine-Tuning." [[>paper](https://arxiv.org/abs/2305.14045)] [[>code](https://kaistAI/CoT-Collection)]
- 👩‍💻 _OASST1_ - contains more than 200 instructions to generate pros and cons \(acc. to nomic.ai's [map](https://huggingface.co/spaces/nomic-ai/OpenAssistant_oasst1)\). [[>dataset](https://huggingface.co/datasets/OpenAssistant/oasst1)]
- 🎓 _LegalBench_ - a benchmark for legal reasoning in LLMs [[>paper](https://arxiv.org/abs/2308.11462)]
- 🎓👩‍💻 _ThoughtSource_ - an open resource for data and tools related to chain-of-thought reasoning in large language models. [[>paper](https://www.nature.com/articles/s41597-023-02433-3.pdf)] [[>code](https://OpenBioLink/ThoughtSource)]
- 🎓👩‍💻 Review with lots of hints to CoT relevant datasets. "Datasets for Large Language Models: A Comprehensive Survey" [[>paper](https://arxiv.org/pdf/2402.18041.pdf)] [[>code](https://lmmlzn/Awesome-LLMs-Datasets)]
- 👩‍💻 Maxime Labonne's LLM datasets list [[github](https://mlabonne/llm-datasets)] 

## Tools and Frameworks 

_Tools and Frameworks to implement deliberative prompting._

- 👩‍💻 _LMQL_ - a programming language for language model interaction. [[>site][lmql-site]] ![GitHub Repo stars](https://img.shields.io/github/stars/eth-sri/lmql)
  - 👩‍💻 Interactive LMQL Playground [[>site][lmql-playground]]
  - 🎓 "Prompting Is Programming: A Query Language for Large Language Models." 2022-12-12. [[>paper](https://arxiv.org/abs/2212.06094)] 
- 👩‍💻 _{{guidance}}_ - a language for controlling large language models. [[>code](https://guidance-ai/guidance)] ![GitHub Repo stars](https://img.shields.io/github/stars/guidance-ai/guidance)
- 👩‍💻 <i>outlines ~</i> - a language for guided text generation. [[>code](https://outlines-dev/outlines)] ![GitHub Repo stars](https://img.shields.io/github/stars/outlines-dev/outlines)
- 👩‍💻 _DSPy_ - a programmatic interface to LLMs. [[>code](https://stanfordnlp/dspy)] ![GitHub Repo stars](https://img.shields.io/github/stars/stanfordnlp/dspy)
- 👩‍💻 _llm-reasoners_ – A library for advanced large language model reasoning. [[>code](https://Ber666/llm-reasoners)] ![GitHub Repo stars](https://img.shields.io/github/stars/Ber666/llm-reasoners)
- 👩‍💻 _ThinkGPT_ - framework and building blocks for chain-of-thought workflows. [[>code](https://jina-ai/thinkgpt#readme)] ![GitHub Repo stars](https://img.shields.io/github/stars/jina-ai/thinkgpt)
- 👩‍💻 _LangChain_ - a python library for building LLM chains and agents. [[>code](https://langchain-ai/langchain)] ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langchain)
- 👩‍💻 _PromptBench_ -a unified library for evaluating LLMS, inter alia effectiveness of CoT prompts. [[>code](https://microsoft/promptbench)] ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/promptbench)
- 👩‍💻 _SymbolicAI_ - a library for compositional differentiable programming with LLMs. [[>code](https://ExtensityAI/symbolicai)] ![GitHub Repo stars](https://img.shields.io/github/stars/ExtensityAI/symbolicai)


## Other Resources

_More awesome and useful material._

- 📚 _Survey of Autonomous LLM Agents_ (continuously updated). [[>site](https://Paitesanshi/LLM-Agent-Survey)]
- 👩‍💻 _LLM Dashboard_ - explore task-specific reasoning performance of open LLMs [[>app](https://huggingface.co/spaces/CoreyMorris/MMLU-by-task-Leaderboard)]
- 📚 _Prompt Engineering Guide_ set up by [DAIR](https://dair.ai). [[>site](https://www.promptingguide.ai/)]
- 📚 _ATLAS_ - principles and benchmark for systematic prompting [[>code](https://VILA-Lab/ATLAS)] 
- 📚 _Deliberative Prompting Guide_ set up by [Logikon](https://logikon.ai). [[>site](https://logikon.ai/docs/delib_prompting)]
- 📚 _Arguing with Arguments_ – recent and wonderful piece by H. Siegel discussing what it actually means to evaluate an argument. [[>paper](https://informallogic.ca/index.php/informal_logic/article/download/7667/5647)]


[lmql-site]: https://lmql.ai/
[lmql-playground]: https://lmql.ai/playground
