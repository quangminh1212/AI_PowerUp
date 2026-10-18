<p align="center"><img width="40%" src="the_incredible_pytorch.png" /></p>

--------------------------------------------------------------------------------
<p align="center">
	<img src="https://img.shields.io/badge/stars-10000+-blue.svg"/>
	<img src="https://img.shields.io/badge/forks-1900+-blue.svg"/>
	<img src="https://img.shields.io/badge/license-MIT-blue.svg"/>
</p>

This is a curated list of tutorials, projects, libraries, videos, papers, books and anything related to the incredible [PyTorch](http://pytorch.org/). Feel free to make a pull request to contribute to this list.


# Table Of Contents
<!-- vscode-markdown-toc -->

- [Table Of Contents](#table-of-contents)
  - [Tutorials](#tutorials)
  - [Large Language Models (LLMs)](#large-language-models-llms)
  - [Agentic AI](#agentic-ai)
  - [Guardrails and AI Safety](#guardrails-and-ai-safety)
  - [Tabular Data](#tabular-data)

- [TabGAN](https://Diyago/Tabular-data-generation): Synthetic tabular data generation using CTGAN, ForestDiffusion, and GReaT (LLMs) with adversarial filtering and privacy metrics.
  - [Visualization](#visualization)
  - [Explainability](#explainability)
  - [Object Detection](#object-detection)
  - [Long-Tailed / Out-of-Distribution Recognition](#long-tailed--out-of-distribution-recognition)
  - [Activation Functions](#activation-functions)
  - [Energy-Based Learning](#energy-based-learning)
  - [Missing Data](#missing-data)
  - [Architecture Search](#architecture-search)
  - [Continual Learning](#continual-learning)
  - [Optimization](#optimization)
  - [Quantization](#quantization)
  - [Quantum Machine Learning](#quantum-machine-learning)
  - [Neural Network Compression](#neural-network-compression)
  - [Facial, Action and Pose Recognition](#facial-action-and-pose-recognition)
  - [Super resolution](#super-resolution)
  - [Synthetesizing Views](#synthetesizing-views)
  - [Voice](#voice)
  - [Medical](#medical)
  - [3D Segmentation, Classification and Regression](#3d-segmentation-classification-and-regression)
  - [Video Recognition](#video-recognition)
  - [Recurrent Neural Networks (RNNs)](#recurrent-neural-networks-rnns)
  - [Convolutional Neural Networks (CNNs)](#convolutional-neural-networks-cnns)
  - [Segmentation](#segmentation)
  - [Geometric Deep Learning: Graph \& Irregular Structures](#geometric-deep-learning-graph--irregular-structures)
  - [Sorting](#sorting)
  - [Ordinary Differential Equations Networks](#ordinary-differential-equations-networks)
  - [Multi-task Learning](#multi-task-learning)
  - [GANs, VAEs, and AEs](#gans-vaes-and-aes)
  - [Unsupervised Learning](#unsupervised-learning)
  - [Adversarial Attacks](#adversarial-attacks)
  - [Style Transfer](#style-transfer)
  - [Image Captioning](#image-captioning)
  - [Transformers](#transformers)
  - [Similarity Networks and Functions](#similarity-networks-and-functions)
  - [Reasoning](#reasoning)
  - [General NLP](#general-nlp)
  - [Question and Answering](#question-and-answering)
  - [Speech Generation and Recognition](#speech-generation-and-recognition)
  - [Document and Text Classification](#document-and-text-classification)
  - [Text Generation](#text-generation)
  - [Text to Image](#text-to-image)
  - [Translation](#translation)
  - [Sentiment Analysis](#sentiment-analysis)
  - [Deep Reinforcement Learning](#deep-reinforcement-learning)
  - [Deep Bayesian Learning and Probabilistic Programmming](#deep-bayesian-learning-and-probabilistic-programmming)
  - [Spiking Neural Networks](#spiking-neural-networks)
  - [Anomaly Detection](#anomaly-detection)
  - [Regression Types](#regression-types)
  - [Time Series](#time-series)
  - [Financial Machine Learning](#financial-machine-learning)
  - [Synthetic Datasets](#synthetic-datasets)
  - [Neural Network General Improvements](#neural-network-general-improvements)
  - [DNN Applications in Chemistry and Physics](#dnn-applications-in-chemistry-and-physics)
  - [New Thinking on General Neural Network Architecture](#new-thinking-on-general-neural-network-architecture)
  - [Linear Algebra](#linear-algebra)
  - [API Abstraction](#api-abstraction)
  - [Low Level Utilities](#low-level-utilities)
  - [PyTorch Utilities](#pytorch-utilities)
  - [PyTorch Video Tutorials](#pytorch-video-tutorials)
  - [Community](#community)
  - [To be Classified](#to-be-classified)
  - [Links to This Repository](#links-to-this-repository)
  - [Contributions](#contributions)
  - [New Special Dedicated List to AI Agents | The Incredible AI Agents](#new-special-dedicated-list-to-ai-agents--the-incredible-ai-agents)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Tutorials'></a>Tutorials
- [Official PyTorch Tutorials](https://pytorch/tutorials)
- [Official PyTorch Examples](https://pytorch/examples)
- [The Math Behind Artificial Intelligence: A Guide to AI Foundations [Full Book]](https://www.freecodecamp.org/news/the-math-behind-artificial-intelligence-book/)
- [Dive Into Deep Learning with PyTorch](https://d2l-ai/d2l-en)
- [How to Read Pytorch](https://davidbau/how-to-read-pytorch)
- [Minicourse in Deep Learning with PyTorch (Multi-language)](https://Atcold/pytorch-Deep-Learning-Minicourse)
- [Practical Deep Learning with PyTorch](https://ritchieng/deep-learning-wizard)
- [Deep Learning Models](https://rasbt/deeplearning-models)
- [C++ Implementation of PyTorch Tutorial](https://prabhuomkar/pytorch-cpp)
- [Simple Examples to Introduce PyTorch](https://jcjohnson/pytorch-examples)
- [Mini Tutorials in PyTorch](https://vinhkhuc/PyTorch-Mini-Tutorials)
- [Deep Learning for NLP](https://rguthrie3/DeepLearningForNLPInPytorch)
- [Deep Learning Tutorial for Researchers](https://yunjey/pytorch-tutorial)
- [Fully Convolutional Networks implemented with PyTorch](https://wkentaro/pytorch-fcn)
- [Simple PyTorch Tutorials Zero to ALL](https://hunkim/PyTorchZeroToAll)
- [DeepNLP-models-Pytorch](https://DSKSD/DeepNLP-models-Pytorch)
- [MILA PyTorch Welcome Tutorials](https://mila-udem/welcome_tutorials)
- [Effective PyTorch, Optimizing Runtime with TorchScript and Numerical Stability Optimization](https://vahidk/EffectivePyTorch)
- [Practical PyTorch](https://spro/practical-pytorch)
- [PyTorch Project Template](https://moemen95/PyTorch-Project-Template)
- [Semantic Search with PyTorch](https://kuutsav/information-retrieval)

## <a name='LargeLanguageModels'></a>Large Language Models (LLMs)
- LLM Tutorials
  - [Build a Large Language Model (From Scratch)](https://rasbt/LLMs-from-scratch)
  - [Hugginface LLM Training Book, a collection of methodologies to help with successful training of large language models](https://huggingface/llm_training_handbook)
- General
  - [Starcoder 2, family of code generation models](https://bigcode-project/starcoder2)
  - [GPT Fast, fast and hackable pytorch native transformer inference](https://pytorch-labs/gpt-fast)
  - [Mixtral Offloading, run Mixtral-8x7B models in Colab or consumer desktops](https://dvmazur/mixtral-offloading)
  - [Llama](https://facebookresearch/llama)
  - [Llama Recipes](https://facebookresearch/llama-recipes)
  - [TinyLlama](https://jzhang38/TinyLlama)
  - [Mosaic Pretrained Transformers (MPT)](https://mosaicml/llm-foundry)
  - [VLLM, high-throughput and memory-efficient inference and serving engine for LLMs](https://vllm-project/vllm)
  - [Dolly](https://databrickslabs/dolly)
  - [Vicuna](https://lm-sys/FastChat)
  - [Mistral 7B](https://mistralai/mistral-src)
  - [BigDL LLM, library for running LLM (large language model) on Intel XPU (from Laptop to GPU to Cloud) using INT4 with very low latency1 (for any PyTorch model)](https://intel-analytics/BigDL)
  - [Simple LLM Finetuner](https://lxe/simple-llm-finetuner)
  - [Petals, run LLMs at home, BitTorrent-style, fine-tuning and inference up to 10x faster than offloading](https://bigscience-workshop/petals)
  - [Gemma, Google's family of lightweight, state-of-the-art open models](https://google/gemma_pytorch)
  - [Qwen, Alibaba Cloud's large language model](https://QwenLM/Qwen)
  - [CodeT5, code-aware encoder-decoder model for code understanding and generation](https://salesforce/CodeT5)
  - [OpenLLaMA, permissively licensed open source reproduction of Meta AI's LLaMA](https://openlm-research/open_llama)
  - [RedPajama, leading open-source models with package to reproduce LLaMA training dataset](https://togethercomputer/RedPajama-Data)
  - [MosaicML LLM Foundry, codebase for training, finetuning, and deploying LLMs](https://mosaicml/llm-foundry)
  - [TECS-L (Golden MoE), dense-to-MoE conversion framework with optimal inhibition ratio I≈1/e for PyTorch LLMs](https://need-singularity/TECS-L)
- Japanese
  - [Japanese Llama](https://masa3141/japanese-alpaca-lora)
  - [Japanese GPT Neox and Open Calm](https://hppRC/llm-lora-classification)
- Chinese
  - [Chinese Llamma-2 7B](https://LinkSoul-AI/Chinese-Llama-2-7b)
  - [Chinese Vicuna](https://Facico/Chinese-Vicuna)
- Retrieval Augmented Generation (RAG)
  - [LlamaIndex, data framework for your LLM application](https://run-llama/llama_index)
- Embeddings
  - [ChromaDB, open-source embedding database](https://chroma-core/chroma)
- Applications
  - [Langchain, building applications with LLMs through composability](https://langchain-ai/langchain)
  - [LangSmith, platform for building production-grade LLM applications](https://langchain-ai/langsmith-sdk)
  - [LiteLLM, call all LLM APIs using the OpenAI format](https://BerriAI/litellm)
  - [OpenAI Python, official Python library for the OpenAI API](https://openai/openai-python)
  - [Guidance, library for controlling large language models](https://microsoft/guidance)
- Finetuning
  - [Huggingface PEFT, State-of-the-art Parameter-Efficient Fine-Tuning](https://huggingface/peft)
  - [Unsloth, finetune LLMs 2-5x faster with 80% less memory](https://unslothai/unsloth)
  - [LoRA, Low-Rank Adaptation of Large Language Models](https://microsoft/LoRA)
  - [QLoRA, efficient finetuning of quantized LLMs](https://artidoro/qlora)
  - [Axolotl, tool designed to streamline the fine-tuning of various AI models](https://OpenAccess-AI-Collective/axolotl)
  - [LLaMA-Factory, unified efficient fine-tuning of 100+ LLMs](https://hiyouga/LLaMA-Factory)
- Training
  - [Higgsfield, Fault-tolerant, highly scalable GPU orchestration, and a machine learning framework designed for training models with billions to trillions of parameters](https://higgsfield-ai/higgsfield)
  - [DeepSpeed, deep learning optimization library](https://microsoft/DeepSpeed)
  - [FairScale, PyTorch extensions for high performance and large scale training](https://facebookresearch/fairscale)
  - [Accelerate, simple way to train and use PyTorch models with multi-GPU, TPU, mixed-precision](https://huggingface/accelerate)
  - [ColossalAI, unified deep learning system for large-scale model training and inference](https://hpcaitech/ColossalAI)
- Quantization
  - [AutoGPTQ, easy-to-use LLMs quantization package with user-friendly apis, based on GPTQ algorithm](https://PanQiWei/AutoGPTQ)
  - [BitsAndBytes, accessible large language models via k-bit quantization](https://TimDettmers/bitsandbytes)
  - [GPTQ-for-LLaMa, 4 bits quantization of LLaMA using GPTQ](https://qwopqwop200/GPTQ-for-LLaMa)
  - [Optimum, acceleration of 🤗 Transformers and 🤗 Diffusers](https://huggingface/optimum)

## <a name='AgenticAI'></a>Agentic AI
- Multi-Agent Systems
  - [LangGraph, library for building stateful, multi-actor applications with LLMs](https://langchain-ai/langgraph)
  - [AutoGen, library that enables the creation of applications using multiple agents that can converse with each other](https://microsoft/autogen)
  - [CrewAI, framework for orchestrating role-playing, autonomous AI agents](https://joaomdmoura/crewAI)
  - [MetaGPT, multi-agent framework for software company simulation](https://geekan/MetaGPT)
  - [AgentScope, user-friendly multi-agent platform](https://modelscope/agentscope)
  - [Swarm, educational framework for building and deploying multi-agent systems](https://openai/swarm)
- Autonomous Agents
  - [AutoGPT, autonomous GPT-4 experiment to make GPT-4 fully autonomous](https://Significant-Gravitas/AutoGPT)
  - [BabyAGI, example of an AI-powered task management system](https://yoheinakajima/babyagi)
  - [LangChain Agents, building agents with LangChain](https://langchain-ai/langchain/tree/master/libs/langchain/langchain/agents)
  - [ReAct: Reasoning and Acting with Language Models](https://princeton-nlp/react)
  - [Voyager, open-ended embodied agent with large language models](https://MineDojo/Voyager)
- Agent Orchestration and Frameworks  
  - [Semantic Kernel, lightweight SDK for integrating AI services](https://microsoft/semantic-kernel)
  - [OpenAI Function Calling, tools for function calling with OpenAI models](https://openai/openai-python)
  - [LlamaIndex Agents, data agents with LlamaIndex](https://run-llama/llama_index/tree/main/llama-index-core/llama_index/core/agent)
  - [Haystack Agents, building search and QA agents](https://deepset-ai/haystack)
  - [DSPy, framework for algorithmically optimizing LM prompts and weights](https://stanfordnlp/dspy)
- Planning and Reasoning
  - [Tree of Thoughts, deliberate problem solving with large language models](https://princeton-nlp/tree-of-thought-llm)
  - [ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models](https://billxbf/ReWOO)
  - [Plan-and-Solve Prompting](https://AGI-Edgerunners/Plan-and-Solve-Prompting)
- Memory and Learning
  - [MemGPT, creating LLM agents with long-term memory](https://cpacker/MemGPT)
  - [Zep, fast, scalable building blocks for production LLM apps](https://getzep/zep)

## <a name='GuardrailsandAISafety'></a>Guardrails and AI Safety
- Content Filtering and Moderation
  - [Guardrails AI, framework for building reliable AI applications](https://guardrails-ai/guardrails)
  - [NeMo Guardrails, toolkit for building trustworthy, safe and secure LLM applications](https://NVIDIA/NeMo-Guardrails)
  - [OpenAI Moderation API Tools](https://openai/moderation-api-release)
  - [Detoxify, toxic comment classification using transformer models](https://unitaryai/detoxify)
  - [Perspective API PyTorch Implementation, toxicity detection](https://conversationai/perspectiveapi)
- Prompt Injection Defense
  - [Prompt Injection Detector, detecting prompt injection attacks](https://protectai/rebuff)
  - [LLM Guard, security toolkit for LLM interactions](https://protectai/llm-guard)
  - [Garak, LLM vulnerability scanner](https://leondz/garak)
- Bias Detection and Mitigation
  - [FairLearn, toolkit for assessing and improving fairness](https://fairlearn/fairlearn)
  - [AIF360, comprehensive set of fairness metrics and bias mitigation algorithms](https://Trusted-AI/AIF360)
  - [What-If Tool, tool for analyzing and understanding ML models](https://PAIR-code/what-if-tool)
- Privacy and Security
  - [Opacus, library for training PyTorch models with differential privacy](https://pytorch/opacus)
  - [PySyft, secure and private Deep Learning framework](https://OpenMined/PySyft)
  - [CrypTen, framework for Privacy Preserving Machine Learning](https://facebookresearch/CrypTen)
  - [Adversarial Robustness Toolbox, library for adversarial attacks and defenses](https://Trusted-AI/adversarial-robustness-toolbox)
- Model Interpretability and Explainability
  - [LIME, explaining the predictions of machine learning classifiers](https://marcotcr/lime)
  - [SHAP, unified approach to explain the output of machine learning models](https://slundberg/shap)
  - [InterpretML, interpret and understand machine learning models](https://interpretml/interpret)
  - [Alibi, algorithms for explaining machine learning models](https://SeldonIO/alibi)
- Safety Evaluation and Testing
  - [AI Safety Gym, environments and tools for AI safety research](https://openai/safety-gym)
  - [Anthropic's Constitutional AI implementations](https://anthropics/constitutional-ai)
  - [HarmBench, standardized evaluation framework for automated red teaming](https://centerforaisafety/HarmBench)

## <a name='TabularData'></a>Tabular Data
- [PyTorch Frame: A Modular Framework for Multi-Modal Tabular Learning](https://pyg-team/pytorch-frame)
- [Pytorch Tabular,standard framework for modelling Deep Learning Models for tabular data](https://manujosephv/pytorch_tabular)
- [Tab Transformer](https://lucidrains/tab-transformer-pytorch)
- [PyTorch-TabNet: Attentive Interpretable Tabular Learning](https://dreamquark-ai/tabnet)
- [carefree-learn: A minimal Automatic Machine Learning (AutoML) solution for tabular datasets based on PyTorch](https://carefree0910/carefree-learn)

## <a name='Visualization'></a>Visualization
- [Loss Visualization](https://tomgoldstein/loss-landscape)
- [Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization](https://jacobgil/pytorch-grad-cam)
- [Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps](https://utkuozbulak/pytorch-cnn-visualizations)
- [SmoothGrad: removing noise by adding noise](https://utkuozbulak/pytorch-cnn-visualizations)
- [DeepDream: dream-like hallucinogenic visuals](https://ProGamerGov/neural-dream)
- [FlashTorch: Visualization toolkit for neural networks in PyTorch](https://MisaOgura/flashtorch)
- [Lucent: Lucid adapted for PyTorch](https://greentfrapp/lucent)
- [DreamCreator: Training GoogleNet models for DeepDream with custom datasets made simple](https://ProGamerGov/dream-creator)
- [CNN Feature Map Visualisation](https://lewis-morris/mapextrackt)

## <a name='Explainability'></a>Explainability
- [Neural-Backed Decision Trees](https://alvinwan/neural-backed-decision-trees)
- [Efficient Covariance Estimation from Temporal Data](https://hrayrhar/T-CorEx)
- [Hierarchical interpretations for neural network predictions](https://csinva/hierarchical-dnn-interpretations)
- [Shap, a unified approach to explain the output of any machine learning model](https://slundberg/shap)
- [VIsualizing PyTorch saved .pth deep learning models with netron](https://lutzroeder/netron)
- [Distilling a Neural Network Into a Soft Decision Tree](https://kimhc6028/soft-decision-tree)
- [Captum, A unified model interpretability library for PyTorch](https://pytorch/captum)
- [bnnr, XAI failure reports with OptiCAM saliency overlays and ICD/AICD augmentation search for PyTorch vision models](https://bnnr-team/bnnr)

## <a name='ObjectDetection'></a>Object Detection
- [MMDetection Object Detection Toolbox](https://open-mmlab/mmdetection)
- [Mask R-CNN Benchmark: Faster R-CNN and Mask R-CNN in PyTorch 1.0](https://facebookresearch/maskrcnn-benchmark)
- [YOLO-World](https://AILab-CVC/YOLO-World)
- [YOLOS](https://hustvl/YOLOS)
- [YOLOF](https://megvii-model/YOLOF)
- [YOLOX](https://Megvii-BaseDetection/YOLOX)
- [YOLOv12: Attention-Centric Real-Time Object Detectors](https://sunsmarterjie/yolov12)
- [YOLOv11](https://ultralytics/ultralytics)
- [YOLOv10](https://THU-MIG/yolov10)
- [YOLOv9](https://WongKinYiu/yolov9)
- [YOLOv8](https://ultralytics/ultralytics)
- [Yolov7](https://WongKinYiu/yolov7)
- [YOLOv6](https://meituan/YOLOv6)
- [Yolov5](https://ultralytics/yolov5)
- [Yolov4](https://AlexeyAB/darknet)
- [YOLOv3](https://ultralytics/yolov3)
- [YOLOv2: Real-Time Object Detection](https://longcw/yolo2-pytorch)
- [SSD: Single Shot MultiBox Detector](https://amdegroot/ssd.pytorch)
- [Detectron models for Object Detection](https://ignacio-rocco/detectorch)
- [Multi-digit Number Recognition from Street View Imagery using Deep Convolutional Neural Networks](https://potterhsu/SVHNClassifier-PyTorch)
- [Whale Detector](https://TarinZ/whale-detector)
- [Catalyst.Detection](https://catalyst-team/detection)

## <a name='Long-TailedOut-of-DistributionRecognition'></a>Long-Tailed / Out-of-Distribution Recognition
- [Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization](https://kohpangwei/group_DRO)
- [Invariant Risk Minimization](https://facebookresearch/InvariantRiskMinimization)
- [Training Confidence-Calibrated Classifier for Detecting Out-of-Distribution Samples](https://alinlab/Confident_classifier)
- [Deep Anomaly Detection with Outlier Exposure](https://hendrycks/outlier-exposure)
- [Large-Scale Long-Tailed Recognition in an Open World](https://zhmiao/OpenLongTailRecognition-OLTR)
- [Principled Detection of Out-of-Distribution Examples in Neural Networks](https://ShiyuLiang/odin-pytorch)
- [Learning Confidence for Out-of-Distribution Detection in Neural Networks](https://uoguelph-mlrg/confidence_estimation)
- [PyTorch Imbalanced Class Sampler](https://ufoym/imbalanced-dataset-sampler)

## <a name='ActivationFunctions'></a>Activation Functions
- [Rational Activations - Learnable Rational Activation Functions](https://ml-research/rational_activations)
- [FreeGrad, PyTorch library for custom backward passes, straight-through estimators and gradient transforms.](https://tbox98/FreeGrad)

## <a name='Energy-BasedLearning'></a>Energy-Based Learning
- [EBGAN, Energy-Based GANs](https://eriklindernoren/PyTorch-GAN/blob/master/implementations/ebgan/ebgan.py)
- [Maximum Entropy Generators for Energy-based Models](https://ritheshkumar95/energy_based_generative_models)


## <a name='MissingData'></a>Missing Data
 - [BRITS: Bidirectional Recurrent Imputation for Time Series](http://papers.nips.cc/paper/7911-brits-bidirectional-recurrent-imputation-for-time-series)

## <a name='ArchitectureSearch'></a>Architecture Search
- [EfficientNetV2](https://lukemelas/EfficientNet-PyTorch)
- [DenseNAS](https://JaminFong/DenseNAS)
- [DARTS: Differentiable Architecture Search](https://quark0/darts)
- [Efficient Neural Architecture Search (ENAS)](https://carpedm20/ENAS-pytorch)
- [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://zsef123/EfficientNets-PyTorch)

## <a name='ContinualLearning'></a>Continual Learning
- [Renate, Automatic Retraining of Neural Networks](https://awslabs/renate)

## <a name='Optimization'></a>Optimization
- [AccSGD, AdaBound, AdaMod, DiffGrad, Lamb, NovoGrad, RAdam, SGDW, Yogi and more](https://jettify/pytorch-optimizer)
- [Lookahead Optimizer: k steps forward, 1 step back](https://alphadl/lookahead.pytorch)
- [RAdam, On the Variance of the Adaptive Learning Rate and Beyond](https://LiyuanLucasLiu/RAdam)
- [Over9000, Comparison of RAdam, Lookahead, Novograd, and combinations](https://mgrankin/over9000)
- [AdaBound, Train As Fast as Adam As Good as SGD](https://Luolc/AdaBound)
- [Riemannian Adaptive Optimization Methods](https://ferrine/geoopt)
- [L-BFGS](https://hjmshi/PyTorch-LBFGS)
- [OptNet: Differentiable Optimization as a Layer in Neural Networks](https://locuslab/optnet)
- [Learning to learn by gradient descent by gradient descent](https://ikostrikov/pytorch-meta-optimizer)
- [Surrogate Gradient Learning in Spiking Neural Networks](https://fzenke/spytorch)
- [TorchOpt: An Efficient Library for Differentiable Optimization](https://metaopt/torchopt)
- [ph-training: Automatic Training with Persistent Homology](https://need-singularity/ph-training) - Uses topological data analysis (H0 persistence) to predict difficulty, find optimal LR, and detect overfitting in real-time (r=0.998).
- [zij](https://junaidaliop/zij) - A canon of deep learning optimization algorithms.
## <a name='Quantization'></a>Quantization
- [Additive Power-of-Two Quantization: An Efficient Non-uniform Discretization For Neural Networks](https://yhhhli/APoT_Quantization)

## <a name='QuantumMachineLearning'></a>Quantum Machine Learning
- [Tor10, generic tensor-network library for quantum simulation in PyTorch](https://kaihsin/Tor10)
- [PennyLane, cross-platform Python library for quantum machine learning with PyTorch interface](https://XanaduAI/pennylane)
- [QQA4CO, GPU-parallel Quasi-Quantum Annealing for combinatorial optimisation in PyTorch (ICLR 2025)](https://Yuma-Ichikawa/QQA4CO)

## <a name='NeuralNetworkCompression'></a>Neural Network Compression
- [Bayesian Compression for Deep Learning](https://KarenUllrich/Tutorial_BayesianCompressionForDL)
- [Neural Network Distiller by Intel AI Lab: a Python package for neural network compression research](https://NervanaSystems/distiller)
- [Learning Sparse Neural Networks through L0 regularization](https://AMLab-Amsterdam/L0_regularization)
- [Energy-constrained Compression for Deep Neural Networks via Weighted Sparse Projection and Layer Input Masking](https://hyang1990/model_based_energy_constrained_compression)
- [EigenDamage: Structured Pruning in the Kronecker-Factored Eigenbasis](https://alecwangcq/EigenDamage-Pytorch)
- [Pruning Convolutional Neural Networks for Resource Efficient Inference](https://jacobgil/pytorch-pruning)
- [Pruning neural networks: is it time to nip it in the bud? (showing reduced networks work better)](https://BayesWatch/pytorch-prunes)

## <a name='FacialActionandPoseRecognition'></a>Facial, Action and Pose Recognition
- [Facenet: Pretrained Pytorch face detection and recognition models](https://timesler/facenet-pytorch)
- [DGC-Net: Dense Geometric Correspondence Network](https://AaltoVision/DGC-Net)
- [High performance facial recognition library on PyTorch](https://ZhaoJ9014/face.evoLVe.PyTorch)
- [FaceBoxes, a CPU real-time face detector with high accuracy](https://zisianw/FaceBoxes.PyTorch)
- [How far are we from solving the 2D & 3D Face Alignment problem? (and a dataset of 230,000 3D facial landmarks)](https://1adrianb/face-alignment)
- [Learning Spatio-Temporal Features with 3D Residual Networks for Action Recognition](https://kenshohara/3D-ResNets-PyTorch)
- [PyTorch Realtime Multi-Person Pose Estimation](https://DavexPro/pytorch-pose-estimation)
- [SphereFace: Deep Hypersphere Embedding for Face Recognition](https://clcarwin/sphereface_pytorch)
- [GANimation: Anatomically-aware Facial Animation from a Single Image](https://albertpumarola/GANimation)
- [Shufflenet V2 by Face++ with better results than paper](https://ericsun99/Shufflenet-v2-Pytorch)
- [Towards 3D Human Pose Estimation in the Wild: a Weakly-supervised Approach](https://xingyizhou/pytorch-pose-hg-3d)
- [Unsupervised Learning of Depth and Ego-Motion from Video](https://ClementPinard/SfmLearner-Pytorch)
- [FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks](https://NVIDIA/flownet2-pytorch)
- [FlowNet: Learning Optical Flow with Convolutional Networks](https://ClementPinard/FlowNetPytorch)
- [Optical Flow Estimation using a Spatial Pyramid Network](https://sniklaus/pytorch-spynet)
- [OpenFace in PyTorch](https://thnkim/OpenFacePytorch)
- [Deep Face Recognition in PyTorch](https://grib0ed0v/face_recognition.pytorch)

## <a name='Superresolution'></a>Super resolution
- [Enhanced Deep Residual Networks for Single Image Super-Resolution](https://thstkdgus35/EDSR-PyTorch)
- [Superresolution using an efficient sub-pixel convolutional neural network](https://pytorch/examples/tree/master/super_resolution)
- [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://bengxy/FastNeuralStyle)

## <a name='SynthetesizingViews'></a>Synthetesizing Views
- [NeRF, Neural Radian Fields, Synthesizing Novels Views of Complex Scenes](https://yenchenlin/nerf-pytorch)

## <a name='Voice'></a>Voice
- [Google AI VoiceFilter: Targeted Voice Separatation by Speaker-Conditioned Spectrogram Masking](https://mindslab-ai/voicefilter)

## <a name='Medical'></a>Medical
- [Medical Zoo, 3D multi-modal medical image segmentation library in PyTorch]( https://black0017/MedicalZooPytorch)
- [U-Net for FLAIR Abnormality Segmentation in Brain MRI](https://mateuszbuda/brain-segmentation-pytorch)
- [Genomic Classification via ULMFiT](https://kheyer/Genomic-ULMFiT)
- [Deep Neural Networks Improve Radiologists' Performance in Breast Cancer Screening](https://nyukat/breast_cancer_classifier)
- [Delira, lightweight framework for medical imaging prototyping](https://justusschock/delira)
- [V-Net: Fully Convolutional Neural Networks for Volumetric Medical Image Segmentation](https://mattmacy/vnet.pytorch)
- [Medical Torch, medical imaging framework for PyTorch](https://perone/medicaltorch)
- [TorchXRayVision - A library for chest X-ray datasets and models. Including pre-trainined models.](https://mlmed/torchxrayvision)

## <a name='DSegmentationClassificationandRegression'></a>3D Segmentation, Classification and Regression
- [Kaolin, Library for Accelerating 3D Deep Learning Research](https://NVIDIAGameWorks/kaolin)
- [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](https://fxia22/pointnet.pytorch)
- [3D segmentation with MONAI and Catalyst](https://colab.research.google.com/drive/15wJus5WZPYxTYE51yBhIBNhk9Tj4k3BT?usp=sharing)

## <a name='VideoRecognition'></a>Video Recognition
- [Dancing to Music](https://NVlabs/Dancing2Music)
- [Devil Is in the Edges: Learning Semantic Boundaries from Noisy Annotations](https://nv-tlabs/STEAL)
- [Deep Video Analytics](https://AKSHAYUBHAT/DeepVideoAnalytics)
- [PredRNN: Recurrent Neural Networks for Predictive Learning using Spatiotemporal LSTMs](https://thuml/predrnn-pytorch)

## <a name='RecurrentNeuralNetworksRNNs'></a>Recurrent Neural Networks (RNNs)
- [SRU: training RNNs as fast as CNNs](https://asappresearch/sru)
- [Ordered Neurons: Integrating Tree Structures into Recurrent Neural Networks](https://yikangshen/Ordered-Neurons)
- [Averaged Stochastic Gradient Descent with Weight Dropped LSTM](https://salesforce/awd-lstm-lm)
- [Training RNNs as Fast as CNNs](https://taolei87/sru)
- [Quasi-Recurrent Neural Network (QRNN)](https://salesforce/pytorch-qrnn)
- [ReSeg: A Recurrent Neural Network-based Model for Semantic Segmentation](https://Wizaron/reseg-pytorch)
- [A Recurrent Latent Variable Model for Sequential Data (VRNN)](https://emited/VariationalRecurrentNeuralNetwork)
- [Improved Semantic Representations From Tree-Structured Long Short-Term Memory Networks](https://dasguptar/treelstm.pytorch)
- [Attention-Based Recurrent Neural Network Models for Joint Intent Detection and Slot Filling](https://DSKSD/RNN-for-Joint-NLU)
- [Attentive Recurrent Comparators](https://sanyam5/arc-pytorch)
- [Collection of Sequence to Sequence Models with PyTorch](https://MaximumEntropy/Seq2Seq-PyTorch)
	1. Vanilla Sequence to Sequence models
	2. Attention based Sequence to Sequence models
	3. Faster attention mechanisms using dot products between the final encoder and decoder hidden states

## <a name='ConvolutionalNeuralNetworksCNNs'></a>Convolutional Neural Networks (CNNs)
- [LegoNet: Efficient Convolutional Neural Networks with Lego Filters](https://huawei-noah/LegoNet)
- [MeshCNN, a convolutional neural network designed specifically for triangular meshes](https://ranahanocka/MeshCNN)
- [Octave Convolution](https://d-li14/octconv.pytorch)
- [PyTorch Image Models, ResNet/ResNeXT, DPN, MobileNet-V3/V2/V1, MNASNet, Single-Path NAS, FBNet](https://rwightman/pytorch-image-models)
- [Deep Neural Networks with Box Convolutions](https://shrubb/box-convolutions)
- [Invertible Residual Networks](https://jarrelscy/iResnet)
- [Stochastic Downsampling for Cost-Adjustable Inference and Improved Regularization in Convolutional Networks ](https://xternalz/SDPoint)
- [Faster Faster R-CNN Implementation](https://jwyang/faster-rcnn.pytorch)
	- [Faster R-CNN Another Implementation](https://longcw/faster_rcnn_pytorch)
- [Paying More Attention to Attention: Improving the Performance of Convolutional Neural Networks via Attention Transfer](https://szagoruyko/attention-transfer)
- [Wide ResNet model in PyTorch](https://szagoruyko/functional-zoo)
	-[DiracNets: Training Very Deep Neural Networks Without Skip-Connections](https://szagoruyko/diracnets)
- [An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition](https://bgshih/crnn)
- [Efficient Densenet](https://gpleiss/efficient_densenet_pytorch)
- [Video Frame Interpolation via Adaptive Separable Convolution](https://sniklaus/pytorch-sepconv)
- [Learning local feature descriptors with triplets and shallow convolutional neural networks](https://edgarriba/examples/tree/master/triplet)
- [Densely Connected Convolutional Networks](https://bamos/densenet.pytorch)
- [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://jcjohnson/pytorch-vgg)
- [SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and \<0.5MB model size](https://gsp-27/pytorch_Squeezenet)
- [Deep Residual Learning for Image Recognition](https://szagoruyko/functional-zoo)
- [Training Wide ResNets for CIFAR-10 and CIFAR-100 in PyTorch](https://xternalz/WideResNet-pytorch)
- [Deformable Convolutional Network](https://oeway/pytorch-deform-conv)
- [Convolutional Neural Fabrics](https://vabh/convolutional-neural-fabrics)
- [Deformable Convolutional Networks in PyTorch](https://1zb/deformable-convolution-pytorch)
- [Dilated ResNet combination with Dilated Convolutions](https://fyu/drn)
- [Striving for Simplicity: The All Convolutional Net](https://utkuozbulak/pytorch-cnn-visualizations)
- [Convolutional LSTM Network](https://automan000/Convolution_LSTM_pytorch)
- [Big collection of pretrained classification models](https://osmr/imgclsmob)
- [PyTorch Image Classification with Kaggle Dogs vs Cats Dataset](https://rdcolema/pytorch-image-classification)
- [CIFAR-10 on Pytorch with VGG, ResNet and DenseNet](https://kuangliu/pytorch-cifar)
- [Base pretrained models and datasets in pytorch (MNIST, SVHN, CIFAR10, CIFAR100, STL10, AlexNet, VGG16, VGG19, ResNet, Inception, SqueezeNet)](https://aaron-xichen/pytorch-playground)
- [NVIDIA/unsupervised-video-interpolation](https://NVIDIA/unsupervised-video-interpolation)

## <a name='Segmentation'></a>Segmentation
- [Detectron2 by FAIR](https://facebookresearch/detectron2)
- [Pixel-wise Segmentation on VOC2012 Dataset using PyTorch](https://bodokaiser/piwise)
- [Pywick - High-level batteries-included neural network training library for Pytorch](https://achaiah/pywick)
- [Improving Semantic Segmentation via Video Propagation and Label Relaxation](https://NVIDIA/semantic-segmentation)
- [Super-BPD: Super Boundary-to-Pixel Direction for Fast Image Segmentation](https://JianqiangWan/Super-BPD)
- [Catalyst.Segmentation](https://catalyst-team/segmentation)
- [Segmentation models with pretrained backbones](https://qubvel/segmentation_models.pytorch)

## <a name='GeometricDeepLearning:GraphIrregularStructures'></a>Geometric Deep Learning: Graph & Irregular Structures
- [PyTorch Geometric, Deep Learning Extension](https://rusty1s/pytorch_geometric)
- [PyTorch Geometric Temporal: A Temporal Extension Library for PyTorch Geometric](https://benedekrozemberczki/pytorch_geometric_temporal)
- [PyTorch Geometric Signed Directed: A Signed & Directed Extension Library for PyTorch Geometric](https://SherylHYX/pytorch_geometric_signed_directed)
- [ChemicalX: A PyTorch Based Deep Learning Library for Drug Pair Scoring](https://AstraZeneca/chemicalx)
- [Self-Attention Graph Pooling](https://inyeoplee77/SAGPool)
- [Position-aware Graph Neural Networks](https://JiaxuanYou/P-GNN)
- [Signed Graph Convolutional Neural Network](https://benedekrozemberczki/SGCN)
- [Graph U-Nets](https://HongyangGao/gunet)
- [Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks](https://benedekrozemberczki/ClusterGCN)
- [MixHop: Higher-Order Graph Convolutional Architectures via Sparsified Neighborhood Mixing](https://benedekrozemberczki/MixHop-and-N-GCN)
- [Semi-Supervised Graph Classification: A Hierarchical Graph Perspective](https://benedekrozemberczki/SEAL-CI)
- [PyTorch BigGraph by FAIR for Generating Embeddings From Large-scale Graph Data](https://facebookresearch/PyTorch-BigGraph)
- [Capsule Graph Neural Network](https://benedekrozemberczki/CapsGNN)
- [Splitter: Learning Node Representations that Capture Multiple Social Contexts](https://benedekrozemberczki/Splitter)
- [A Higher-Order Graph Convolutional Layer](https://benedekrozemberczki/MixHop-and-N-GCN)
- [Predict then Propagate: Graph Neural Networks meet Personalized PageRank](https://benedekrozemberczki/APPNP)
- [Lorentz Embeddings: Learn Continuous Hierarchies in Hyperbolic Space](https://theSage21/lorentz-embeddings)
- [Graph Wavelet Neural Network](https://benedekrozemberczki/GraphWaveletNeuralNetwork)
- [Watch Your Step: Learning Node Embeddings via Graph Attention](https://benedekrozemberczki/AttentionWalk)
- [Signed Graph Convolutional Network](https://benedekrozemberczki/SGCN)
- [Graph Classification Using Structural Attention](https://benedekrozemberczki/GAM)
- [SimGNN: A Neural Network Approach to Fast Graph Similarity Computation](https://benedekrozemberczki/SimGNN)
- [SINE: Scalable Incomplete Network Embedding](https://benedekrozemberczki/SINE)
- [HypER: Hypernetwork Knowledge Graph Embeddings](https://ibalazevic/HypER)
- [TuckER: Tensor Factorization for Knowledge Graph Completion](https://ibalazevic/TuckER)
- [PyKEEN: A Python library for learning and evaluating knowledge graph embeddings](https://pykeen/pykeen/)
- [Pathfinder Discovery Networks for Neural Message Passing](https://benedekrozemberczki/PDN)
- [SSSNET: Semi-Supervised Signed Network Clustering](https://SherylHYX/SSSNET_Signed_Clustering)
- [MagNet: A Neural Network for Directed Graphs](https://matthew-hirn/magnet)
- [PyTorch Geopooling: Geospatial Pooling Modules for Neural Networks in PyTorch](https://ybubnov/torch_geopooling)

## <a name='Sorting'></a>Sorting
- [Stochastic Optimization of Sorting Networks via Continuous Relaxations](https://ermongroup/neuralsort)

## <a name='OrdinaryDifferentialEquationsNetworks'></a>Ordinary Differential Equations Networks
- [Latent ODEs for Irregularly-Sampled Time Series](https://YuliaRubanova/latent_ode)
- [GRU-ODE-Bayes: continuous modelling of sporadically-observed time series](https://edebrouwer/gru_ode_bayes)

## <a name='Multi-taskLearning'></a>Multi-task Learning
- [Hierarchical Multi-Task Learning Model](https://huggingface/hmtl)
- [Task-based End-to-end Model Learning](https://locuslab/e2e-model-learning)
- [torchMTL: A lightweight module for Multi-Task Learning in pytorch](https://chrisby/torchMTL)

## <a name='GANsVAEsandAEs'></a>GANs, VAEs, and AEs
- [BigGAN: Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://ajbrock/BigGAN-PyTorch)
- [High Fidelity Performance Metrics for Generative Models in PyTorch](https://toshas/torch-fidelity)
- [Mimicry, PyTorch Library for Reproducibility of GAN Research](https://kwotsin/mimicry)
- [Clean Readable CycleGAN](https://aitorzip/PyTorch-CycleGAN)
- [StarGAN](https://yunjey/stargan)
- [Block Neural Autoregressive Flow](https://nicola-decao/BNAF)
- [High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs](https://NVIDIA/pix2pixHD)
- [A Style-Based Generator Architecture for Generative Adversarial Networks](https://rosinality/style-based-gan-pytorch)
- [GANDissect, PyTorch Tool for Visualizing Neurons in GANs](https://CSAILVision/gandissect)
- [Learning deep representations by mutual information estimation and maximization](https://DuaneNielsen/DeepInfomaxPytorch)
- [Variational Laplace Autoencoders](https://yookoon/VLAE)
- [VeGANS, library for easily training GANs](https://unit8co/vegans)
- [Progressive Growing of GANs for Improved Quality, Stability, and Variation](https://github-pengge/PyTorch-progressive_growing_of_gans)
- [Conditional GAN](https://kmualim/CGAN-Pytorch/)
- [Wasserstein GAN](https://martinarjovsky/WassersteinGAN)
- [Adversarial Generator-Encoder Network](https://DmitryUlyanov/AGE)
- [Image-to-Image Translation with Conditional Adversarial Networks](https://junyanz/pytorch-CycleGAN-and-pix2pix)
- [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://junyanz/pytorch-CycleGAN-and-pix2pix)
- [On the Effects of Batch and Weight Normalization in Generative Adversarial Networks](https://stormraiser/GAN-weight-norm)
- [Improved Training of Wasserstein GANs](https://jalola/improved-wgan-pytorch)
- [Collection of Generative Models with PyTorch](https://wiseodd/generative-models)
	- Generative Adversarial Nets (GAN)
		1. [Vanilla GAN](https://arxiv.org/abs/1406.2661)
		2. [Conditional GAN](https://arxiv.org/abs/1411.1784)
		3. [InfoGAN](https://arxiv.org/abs/1606.03657)
		4. [Wasserstein GAN](https://arxiv.org/abs/1701.07875)
		5. [Mode Regularized GAN](https://arxiv.org/abs/1612.02136)
	- Variational Autoencoder (VAE)
		1. [Vanilla VAE](https://arxiv.org/abs/1312.6114)
		2. [Conditional VAE](https://arxiv.org/abs/1406.5298)
		3. [Denoising VAE](https://arxiv.org/abs/1511.06406)
		4. [Adversarial Autoencoder](https://arxiv.org/abs/1511.05644)
		5. [Adversarial Variational Bayes](https://arxiv.org/abs/1701.04722)
- [Improved Training of Wasserstein GANs](https://caogang/wgan-gp)
- [CycleGAN and Semi-Supervised GAN](https://yunjey/mnist-svhn-transfer)
- [Improving Variational Auto-Encoders using Householder Flow and using convex combination linear Inverse Autoregressive Flow](https://jmtomczak/vae_vpflows)
- [PyTorch GAN Collection](https://znxlwm/pytorch-generative-model-collections)
- [Generative Adversarial Networks, focusing on anime face drawing](https://jayleicn/animeGAN)
- [Simple Generative Adversarial Networks](https://mailmahee/pytorch-generative-adversarial-networks)
- [Adversarial Auto-encoders](https://fducau/AAE_pytorch)
- [torchgan: Framework for modelling Generative Adversarial Networks in Pytorch](https://torchgan/torchgan)
- [Evaluating Lossy Compression Rates of Deep Generative Models](https://huangsicong/rate_distortion)
- [Catalyst.GAN](https://catalyst-team/gan)
    1. [Vanilla GAN](https://arxiv.org/abs/1406.2661)
    2. [Conditional GAN](https://arxiv.org/abs/1411.1784)
    3. [Wasserstein GAN](https://arxiv.org/abs/1701.07875)
    4. [Improved Training of Wasserstein GANs](https://arxiv.org/abs/1704.00028)

## <a name='UnsupervisedLearning'></a>Unsupervised Learning
- [Unsupervised Embedding Learning via Invariant and Spreading Instance Feature](https://mangye16/Unsupervised_Embedding_Learning)
- [AND: Anchor Neighbourhood Discovery](https://Raymond-sci/AND)

## <a name='AdversarialAttacks'></a>Adversarial Attacks
- [Deep Neural Networks are Easily Fooled: High Confidence Predictions for Unrecognizable Images](https://utkuozbulak/pytorch-cnn-adversarial-attacks)
- [Explaining and Harnessing Adversarial Examples](https://utkuozbulak/pytorch-cnn-adversarial-attacks)
- [AdverTorch - A Toolbox for Adversarial Robustness Research](https://BorealisAI/advertorch)

## <a name='StyleTransfer'></a>Style Transfer
- [Pystiche: Framework for Neural Style Transfer](https://pystiche/pystiche)
- [Detecting Adversarial Examples via Neural Fingerprinting](https://StephanZheng/neural-fingerprinting)
- [A Neural Algorithm of Artistic Style](https://alexis-jacq/Pytorch-Tutorials)
- [Multi-style Generative Network for Real-time Transfer](https://zhanghang1989/PyTorch-Style-Transfer)
- [DeOldify, Coloring Old Images](https://jantic/DeOldify)
- [Neural Style Transfer](https://ProGamerGov/neural-style-pt)
- [Fast Neural Style Transfer](https://darkstar112358/fast-neural-style)
- [Draw like Bob Ross](https://kendricktan/drawlikebobross)

## <a name='ImageCaptioning'></a>Image Captioning
- [CLIP (Contrastive Language-Image Pre-Training)](https://openai/CLIP)
- [Neuraltalk 2, Image Captioning Model, in PyTorch](https://ruotianluo/neuraltalk2.pytorch)
- [Generate captions from an image with PyTorch](https://eladhoffer/captionGen)
- [DenseCap: Fully Convolutional Localization Networks for Dense Captioning](https://jcjohnson/densecap)

## <a name='Transformers'></a>Transformers
- [Attention is all you need](https://jadore801120/attention-is-all-you-need-pytorch)
- [Spatial Transformer Networks](https://fxia22/stn.pytorch)

## <a name='SimilarityNetworksandFunctions'></a>Similarity Networks and Functions
- [Conditional Similarity Networks](https://andreasveit/conditional-similarity-networks)

## <a name='Reasoning'></a>Reasoning
- [Inferring and Executing Programs for Visual Reasoning](https://facebookresearch/clevr-iep)

## <a name='GeneralNLP'></a>General NLP
- [nanoGPT, fastest repository for training/finetuning medium-sized GPTs](https://karpathy/nanoGPT)
- [llm.c, LLM training in simple, pure C/CUDA — GPT-2 in ~1000 lines of code with no PyTorch dependency](https://karpathy/llm.c)
- [minGPT, Re-implementation of GPT to be small, clean, interpretable and educational](https://karpathy/minGPT)
- [Espresso, Module Neural Automatic Speech Recognition Toolkit](https://freewym/espresso)
- [Label-aware Document Representation via Hybrid Attention for Extreme Multi-Label Text Classification](https://HX-idiot/Hybrid_Attention_XML)
- [XLNet](https://graykode/xlnet-Pytorch)
- [Conversing by Reading: Contentful Neural Conversation with On-demand Machine Reading](https://qkaren/converse_reading_cmr)
- [Cross-lingual Language Model Pretraining](https://facebookresearch/XLM)
- [Libre Office Translate via PyTorch NMT](https://lernapparat/lotranslate)
- [BERT](https://huggingface/pytorch-pretrained-BERT)
- [VSE++: Improved Visual-Semantic Embeddings](https://fartashf/vsepp)
- [A Structured Self-Attentive Sentence Embedding](https://ExplorerFreda/Structured-Self-Attentive-Sentence-Embedding)
- [Neural Sequence labeling model](https://jiesutd/PyTorchSeqLabel)
- [Skip-Thought Vectors](https://sanyam5/skip-thoughts)
- [Complete Suite for Training Seq2Seq Models in PyTorch](https://eladhoffer/seq2seq.pytorch)
- [MUSE: Multilingual Unsupervised and Supervised Embeddings](https://facebookresearch/MUSE)
- [TorchMoji: PyTorch Implementation of DeepMoji to under Language used to Express Emotions](https://huggingface/torchMoji)

## <a name='QuestionandAnswering'></a>Question and Answering
- [Visual Question Answering in Pytorch](https://Cadene/vqa.pytorch)
- [Reading Wikipedia to Answer Open-Domain Questions](https://facebookresearch/DrQA)
- [Deal or No Deal? End-to-End Learning for Negotiation Dialogues](https://facebookresearch/end-to-end-negotiator)
- [Interpretable Counting for Visual Question Answering](https://sanyam5/irlc-vqa)
- [Open Source Chatbot with PyTorch](https://jinfagang/pytorch_chatbot)

## <a name='SpeechGenerationandRecognition'></a>Speech Generation and Recognition
- [PyTorch-Kaldi Speech Recognition Toolkit](https://mravanelli/pytorch-kaldi)
- [WaveGlow: A Flow-based Generative Network for Speech Synthesis](https://NVIDIA/waveglow)
- [OpenNMT](https://OpenNMT/OpenNMT-py)
- [Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](https://SeanNaren/deepspeech.pytorch)
- [WeNet: Production First and Production Ready End-to-End Speech Recognition Toolkit](https://mobvoi/wenet)

## <a name='DocumentandTextClassification'></a>Document and Text Classification
- [Hierarchical Attention Network for Document Classification](https://cedias/HAN-pytorch)
- [Hierarchical Attention Networks for Document Classification](https://EdGENetworks/attention-networks-for-classification)
- [CNN Based Text Classification](https://xiayandi/Pytorch_text_classification)

## <a name='TextGeneration'></a>Text Generation
- [Pytorch Poetry Generation](https://jhave/pytorch-poetry-generation)

## <a name='TexttoImage'></a>Text to Image
- [Stable Diffusion](https://CompVis/stable-diffusion)
- [Dall-E 2](https://lucidrains/DALLE2-pytorch)
- [Dall-E](https://lucidrains/DALLE-pytorch)

## <a name='Translation'></a>Translation
- [Open-source (MIT) Neural Machine Translation (NMT) System](https://OpenNMT/OpenNMT-py)

## <a name='SentimentAnalysis'></a>Sentiment Analysis
- [Recurrent Neural Networks for Sentiment Analysis (Aspect-Based) on SemEval 2014](https://vanzytay/pytorch_sentiment_rnn)
- [Seq2Seq Intent Parsing](https://spro/pytorch-seq2seq-intent-parsing)
- [Finetuning BERT for Sentiment Analysis](https://barissayil/SentimentAnalysis)

## <a name='DeepReinforcementLearning'></a>Deep Reinforcement Learning
- [Image Augmentation Is All You Need: Regularizing Deep Reinforcement Learning from Pixels](https://denisyarats/drq)
- [Exploration by Random Network Distillation](https://openai/random-network-distillation)
- [EGG: Emergence of lanGuage in Games, quickly implement multi-agent games with discrete channel communication](https://facebookresearch/EGG)
- [Temporal Difference VAE](https://openreview.net/pdf?id=S1x4ghC9tQ)
- [High-performance Atari A3C Agent in 180 Lines PyTorch](https://greydanus/baby-a3c)
- [Learning when to communicate at scale in multiagent cooperative and competitive tasks](https://IC3Net/IC3Net)
- [Actor-Attention-Critic for Multi-Agent Reinforcement Learning](https://shariqiqbal2810/MAAC)
- [PPO in PyTorch C++](https://mhubii/ppo_pytorch_cpp)
- [Reinforcement Learning for Bandit Neural Machine Translation with Simulated Human Feedback](https://khanhptnk/bandit-nmt)
- [Asynchronous Methods for Deep Reinforcement Learning](https://ikostrikov/pytorch-a3c)
- [Continuous Deep Q-Learning with Model-based Acceleration](https://ikostrikov/pytorch-naf)
- [Asynchronous Methods for Deep Reinforcement Learning for Atari 2600](https://dgriff777/rl_a3c_pytorch)
- [Trust Region Policy Optimization](https://mjacar/pytorch-trpo)
- [Neural Combinatorial Optimization with Reinforcement Learning](https://pemami4911/neural-combinatorial-rl-pytorch)
- [Noisy Networks for Exploration](https://Kaixhin/NoisyNet-A3C)
- [Distributed Proximal Policy Optimization](https://alexis-jacq/Pytorch-DPPO)
- [Reinforcement learning models in ViZDoom environment with PyTorch](https://akolishchak/doom-net-pytorch)
- [Reinforcement learning models using Gym and Pytorch](https://jingweiz/pytorch-rl)
- [SLM-Lab: Modular Deep Reinforcement Learning framework in PyTorch](https://kengz/SLM-Lab)
- [Catalyst.RL](https://catalyst-team/catalyst-rl)

## <a name='DeepBayesianLearningandProbabilisticProgrammming'></a>Deep Bayesian Learning and Probabilistic Programmming
- [BatchBALD: Efficient and Diverse Batch Acquisition for Deep Bayesian Active Learning](https://BlackHC/BatchBALD)
- [Subspace Inference for Bayesian Deep Learning](https://wjmaddox/drbayes)
- [Bayesian Deep Learning with Variational Inference Package](https://ctallec/pyvarinf)
- [Probabilistic Programming and Statistical Inference in PyTorch](https://stepelu/ptstat)
- [Bayesian CNN with Variational Inferece in PyTorch](https://kumar-shridhar/PyTorch-BayesianCNN)

## <a name='SpikingNeuralNetworks'></a>Spiking Neural Networks
- [Norse, Library for Deep Learning with Spiking Neural Networks](https://norse/norse)

## <a name='AnomalyDetection'></a>Anomaly Detection
- [Detection of Accounting Anomalies using Deep Autoencoder Neural Networks](https://GitiHubi/deepAI)

## <a name='RegressionTypes'></a>Regression Types
- [Quantile Regression DQN](https://ars-ashuha/quantile-regression-dqn-pytorch)

## <a name='TimeSeries'></a>Time Series
- [Dual Self-Attention Network for Multivariate Time Series Forecasting](https://bighuang624/DSANet)
- [DILATE: DIstortion Loss with shApe and tImE](https://vincent-leguen/DILATE)
- [Variational Recurrent Autoencoder for Timeseries Clustering](https://tejaslodaya/timeseries-clustering-vae)
- [Spatio-Temporal Neural Networks for Space-Time Series Modeling and Relations Discovery](https://edouardelasalles/stnn)
- [Flow Forecast: A deep learning for time series forecasting framework built in PyTorch](https://AIStream-Peelout/flow-forecast)

## <a name='FinancialMachineLearning'></a>Financial Machine Learning
- [ml-quant-trading, PyTorch research stack for multi-factor trading with 213 factors, bias correction, portfolio optimization, and vectorized backtesting](https://initial-d/ml-quant-trading)

## <a name='SyntheticDatasets'></a>Synthetic Datasets
- [Meta-Sim: Learning to Generate Synthetic Datasets](https://nv-tlabs/meta-sim)

## <a name='NeuralNetworkGeneralImprovements'></a>Neural Network General Improvements
- [PH Training, persistent homology-based training monitor that detects overfitting early using topological data analysis](https://need-singularity/ph-training)
- [The Artificial Dendrite Network Library for PyTorch](https://PerforatedAI/PerforatedAI)
- [In-Place Activated BatchNorm for Memory-Optimized Training of DNNs](https://mapillary/inplace_abn)
- [Train longer, generalize better: closing the generalization gap in large batch training of neural networks](https://eladhoffer/bigBatch)
- [FreezeOut: Accelerate Training by Progressively Freezing Layers](https://ajbrock/FreezeOut)
- [Binary Stochastic Neurons](https://Wizaron/binary-stochastic-neurons)
- [Compact Bilinear Pooling](https://DeepInsight-PCALab/CompactBilinearPooling-Pytorch)
- [Mixed Precision Training in PyTorch](https://suvojit-0x55aa/mixed-precision-pytorch)

## <a name='DNNApplicationsinChemistryandPhysics'></a>DNN Applications in Chemistry and Physics
- [Wave Physics as an Analog Recurrent Neural Network](https://fancompute/wavetorch)
- [Neural Message Passing for Quantum Chemistry](https://priba/nmp_qc)
- [Automatic chemical design using a data-driven continuous representation of molecules](https://cxhernandez/molencoder)
- [Deep Learning for Physical Processes: Integrating Prior Scientific Knowledge](https://emited/flow)
- [Differentiable Molecular Simulation for Learning and Control](https://wwang2/torchmd)

## <a name='NewThinkingonGeneralNeuralNetworkArchitecture'></a>New Thinking on General Neural Network Architecture
- [Complement Objective Training](https://henry8527/COT)
- [Decoupled Neural Interfaces using Synthetic Gradients](https://andrewliao11/dni.pytorch)

## <a name='LinearAlgebra'></a>Linear Algebra
- [Eigenvectors from Eigenvalues](https://ritchieng/eigenvectors-from-eigenvalues)

## <a name='APIAbstraction'></a>API Abstraction
- [Torch Layers, Shape inference for PyTorch, SOTA Layers](https://szymonmaszke/torchlayers)
- [Hummingbird, run trained scikit-learn models on GPU with PyTorch](https://microsoft/hummingbird)

## <a name='LowLevelUtilities'></a>Low Level Utilities
- [TorchSharp, .NET API with access to underlying library powering PyTorch](https://interesaaat/TorchSharp)

## <a name='PyTorchUtilities'></a>PyTorch Utilities
- [Functorch: prototype of JAX-like composable Function transformers for PyTorch](https://zou3519/functorch)
- [Poutyne: Simplified Framework for Training Neural Networks](https://GRAAL-Research/poutyne)
- [PyTorch Metric Learning](https://KevinMusgrave/pytorch-metric-learning)
- [Kornia: an Open Source Differentiable Computer Vision Library for PyTorch](https://kornia.org/)
- [BackPACK to easily Extract Variance, Diagonal of Gauss-Newton, and KFAC](https://f-dangel.github.io/backpack/)
- [PyHessian for Computing Hessian Eigenvalues, trace of matrix, and ESD](https://amirgholami/PyHessian)
- [Hessian in PyTorch](https://mariogeiger/hessian)
- [Differentiable Convex Layers](https://cvxgrp/cvxpylayers)
- [Albumentations: Fast Image Augmentation Library](https://albu/albumentations)
- [Higher, obtain higher order gradients over losses spanning training loops](https://facebookresearch/higher)
- [Neural Pipeline, Training Pipeline for PyTorch](https://toodef/neural-pipeline)
- [Layer-by-layer PyTorch Model Profiler for Checking Model Time Consumption](https://awwong1/torchprof)
- [Sparse Distributions](https://probabll/sparse-distributions)
- [Diffdist, Adds Support for Differentiable Communication allowing distributed model parallelism](https://ag14774/diffdist)
- [HessianFlow, Library for Hessian Based Algorithms](https://amirgholami/HessianFlow)
- [Texar, PyTorch Toolkit for Text Generation](https://asyml/texar-pytorch)
- [PyTorch FLOPs counter](https://Lyken17/pytorch-OpCounter)
- [PyTorch Inference on C++ in Windows](https://zccyman/pytorch-inference)
- [EuclidesDB, Multi-Model Machine Learning Feature Database](https://perone/euclidesdb)
- [Data Augmentation and Sampling for Pytorch](https://ncullen93/torchsample)
- [PyText, deep learning based NLP modelling framework officially maintained by FAIR](https://facebookresearch/pytext)
- [Torchstat for Statistics on PyTorch Models](https://Swall0w/torchstat)
- [Load Audio files directly into PyTorch Tensors](https://pytorch/audio)
- [Weight Initializations](https://pytorch/pytorch/blob/master/torch/nn/init.py)
- [Spatial transformer implemented in PyTorch](https://fxia22/stn.pytorch)
- [PyTorch AWS AMI, run PyTorch with GPU support in less than 5 minutes](https://ritchieng/dlami)
- [Use tensorboard with PyTorch](https://lanpa/tensorboard-pytorch)
- [Simple Fit Module in PyTorch, similar to Keras](https://henryre/pytorch-fitmodule)
- [torchbearer: A model fitting library for PyTorch](https://ecs-vlc/torchbearer)
- [PyTorch to Keras model converter](https://nerox8664/pytorch2keras)
- [Gluon to PyTorch model converter with code generation](https://nerox8664/gluon2pytorch)
- [Catalyst: High-level utils for PyTorch DL & RL research](https://catalyst-team/catalyst)
- [PyTorch Lightning: Scalable and lightweight deep learning research framework](https://PyTorchLightning/pytorch-lightning)
- [Determined: Scalable deep learning platform with PyTorch support](https://determined-ai/determined)
- [PyTorch-Ignite: High-level library to help with training and evaluating neural networks in PyTorch flexibly and transparently](https://pytorch/ignite)
- [torchvision: A package consisting of popular datasets, model architectures, and common image transformations for computer vision.](https://pytorch/vision)
- [Poutyne: A Keras-like framework for PyTorch and handles much of the boilerplating code needed to train neural networks.](https://GRAAL-Research/poutyne)
- [torchensemble: Scikit-Learn like ensemble methods in PyTorch](https://AaronX121/Ensemble-Pytorch)
- [TorchFix - a linter for PyTorch-using code with autofix support](https://pytorch-labs/torchfix)
- [pytorch360convert - Differentiable image conversions between 360° equirectangular images, cubemaps, and perspective projections](https://ProGamerGov/pytorch360convert)
- [torchcurves - differentiable parametric curve modules for PyTorch](https://alexshtf/torchcurves)


## <a name='PyTorchVideoTutorials'></a>PyTorch Video Tutorials
- [PyTorch Zero to All Lectures](http://bit.ly/PyTorchVideo)
- [PyTorch For Deep Learning Full Course](https://www.youtube.com/watch?v=GIsg-ZUy0MY)
- [PyTorch Lightning 101 with Alfredo Canziani and William Falcon](https://www.youtube.com/playlist?list=PLaMu-SDt_RB5NUm67hU2pdE75j6KaIOv2)
- [Practical Deep Learning with PyTorch](https://www.udemy.com/practical-deep-learning-with-pytorch)


## <a name='Community'></a>Community
- [PyTorch Discussion Forum](https://discuss.pytorch.org/)
- [StackOverflow PyTorch Tags](http://stackoverflow.com/questions/tagged/pytorch)
- [Catalyst.Slack](https://join.slack.com/t/catalyst-team-core/shared_invite/zt-d9miirnn-z86oKDzFMKlMG4fgFdZafw)


## <a name='TobeClassified'></a>To be Classified
- [Perturbative Neural Networks](https://michaelklachko/pnn.pytorch)
- [Accurate Neural Network Potential](https://aiqm/torchani)
- [Scaling the Scattering Transform: Deep Hybrid Networks](https://edouardoyallon/pyscatwave)
- [CortexNet: a Generic Network Family for Robust Visual Temporal Representations](https://e-lab/pytorch-CortexNet)
- [Oriented Response Networks](https://ZhouYanzhao/ORN)
- [Associative Compression Networks](https://jalexvig/associative_compression_networks)
- [Clarinet](https://ksw0306/ClariNet)
- [Continuous Wavelet Transforms](https://tomrunia/PyTorchWavelets)
- [mixup: Beyond Empirical Risk Minimization](https://leehomyc/mixup_pytorch)
- [Network In Network](https://szagoruyko/functional-zoo)
- [Highway Networks](https://c0nn3r/pytorch_highway_networks)
- [Hybrid computing using a neural network with dynamic external memory](https://ypxie/pytorch-NeuCom)
- [Value Iteration Networks](https://onlytailei/PyTorch-value-iteration-networks)
- [Differentiable Neural Computer](https://jingweiz/pytorch-dnc)
- [A Neural Representation of Sketch Drawings](https://alexis-jacq/Pytorch-Sketch-RNN)
- [Understanding Deep Image Representations by Inverting Them](https://utkuozbulak/pytorch-cnn-visualizations)
- [NIMA: Neural Image Assessment](https://truskovskiyk/nima.pytorch)
- [NASNet-A-Mobile. Ported weights](https://veronikayurchuk/pretrained-models.pytorch)
- [Graphics code generating model using Processing](https://jtoy/sketchnet)

## <a name='LinkstoThisRepository'></a>Links to This Repository
- [Github Repository](https://ritchieng/the-incredible-pytorch)
- [Website](https://www.ritchieng.com/the-incredible-pytorch/)


## <a name='Contributions'></a>Contributions
Do feel free to contribute!

You can raise an issue or submit a pull request, whichever is more convenient for you. The guideline is simple: just follow the format of the previous bullet point or create a new section if it's a new category.

## New Special Dedicated List to AI Agents | The Incredible AI Agents
Feel free to visit [The Incredible AI Agents](https://ritchieng/the-incredible-ai-agents), a curated list of resources on building, evaluating, deploying, monitoring AI Agents. Feel free to view, star, share and/or contribute!
