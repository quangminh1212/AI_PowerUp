# Ultimate-Awesome-Transformer-Attention [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

This repo contains a comprehensive paper list of **Vision Transformer & Attention**, including papers, codes, and related websites. <br>
This list is maintained by [Min-Hung Chen](https://minhungchen.netlify.app/). (*Actively* keep updating)

If you find some ignored papers, **feel free to [*create pull requests*](https://github.com/cmhungsteve/Awesome-Transformer-Attention/blob/main/How-to-PR.md), [*open issues*](https://github.com/cmhungsteve/Awesome-Transformer-Attention/issues/new), or [*email* me](mailto:vitec6@gmail.com)**. <br> 
Contributions in any form to make this list more comprehensive are welcome.

If you find this repository useful, please consider **[citing](#citation)** and **★STARing** this list. <br>
Feel free to share this list with others! 

**[Update: January, 2024]** Added all the related papers from *NeurIPS 2023*! <br>
**[Update: December, 2023]** Added all the related papers from *ICCV 2023*! <br>
**[Update: September, 2023]** Split the multi-modal paper list to [README_multimodal.md](README_multimodal.md) <br>
**[Update: June, 2023]** Added all the related papers from *ICML 2023*! <br>
**[Update: June, 2023]** Added all the related papers from *CVPR 2023*! <br>
**[Update: February, 2023]** Added all the related papers from *ICLR 2023*! <br>
**[Update: December, 2022]** Added attention-free papers from [Networks Beyond Attention (GitHub)](https://github.com/FocalNet/Networks-Beyond-Attention) made by [Jianwei Yang](https://github.com/jwyang) <br>
**[Update: November, 2022]** Added all the related papers from *NeurIPS 2022*! <br>
**[Update: October, 2022]** Split the 2nd half of the paper list to [README_2.md](README_2.md) <br>
**[Update: October, 2022]** Added all the related papers from *ECCV 2022*! <br>
**[Update: September, 2022]** Added the [Transformer tutorial slides](http://lucasb.eyer.be/transformer) made by [Lucas Beyer](https://twitter.com/giffmana)! <br>
**[Update: June, 2022]** Added all the related papers from *CVPR 2022*!

---
## Overview

- [Citation](#citation)
- [Survey](#survey)
- [Image Classification / Backbone](#image-classification--backbone)
    - [Replace Conv w/ Attention](#replace-conv-w-attention)
        - [Pure Attention](#pure-attention)
        - [Conv-stem + Attention](#conv-stem--attention)
        - [Conv + Attention](#conv--attention)
    - [Vision Transformer](#vision-transformer)
        - [General Vision Transformer](#general-vision-transformer)
        - [Efficient Vision Transformer](#efficient-vision-transformer)
        - [Conv + Transformer](#conv--transformer)
        - [Training + Transformer](#training--transformer)
        - [Robustness + Transformer](#robustness--transformer)
        - [Model Compression + Transformer](#model-compression--transformer)
    - [Attention-Free](#attention-free)
        - [MLP-Series](#mlp-series)
        - [Other Attention-Free](#other-attention-free)
    - [Analysis for Transformer](#analysis-for-transformer)
- [Detection](#detection)
    - [Object Detection](#object-detection)
    - [3D Object Detection](#3d-object-detection)
    - [Multi-Modal Detection](#multi-modal-detection)
    - [HOI Detection](#hoi-detection)
    - [Salient Object Detection](#salient-object-detection)
    - [Other Detection Tasks](#other-detection-tasks)
- [Segmentation](#segmentation)
    - [Semantic Segmentation](#semantic-segmentation)
    - [Depth Estimation](#depth-estimation)
    - [Object Segmentation](#object-segmentation)
    - [Other Segmentation Tasks](#other-segmentation-tasks)
- [Video (High-level)](#video-high-level)
    - [Action Recognition](#action-recognition)
    - [Action Detection/Localization](#action-detectionlocalization)
    - [Action Prediction/Anticipation](#action-predictionanticipation)
    - [Video Object Segmentation](#video-object-segmentation)
    - [Video Instance Segmentation](#video-instance-segmentation)
    - [Other Video Tasks](#other-video-tasks)
- [References](#references)
 
------ (The following papers are moved to [README_multimodal.md](README_multimodal.md)) ------

- [Multi-Modality](README_multimodal.md#multi-modality)
    - [Visual Captioning](README_multimodal.md#visual-captioning)
    - [Visual Question Answering](README_multimodal.md#visual-question-answering)
    - [Visual Grounding](README_multimodal.md#visual-grounding)
    - [Multi-Modal Representation Learning](README_multimodal.md#multi-modal-representation-learning)
    - [Multi-Modal Retrieval](README_multimodal.md#multi-modal-retrieval)
    - [Multi-Modal Generation](README_multimodal.md#multi-modal-generation)
    - [Prompt Learning/Tuning](README_multimodal.md#prompt-learningtuning)
    - [Visual Document Understanding](README_multimodal.md#visual-document-understanding)
    - [Other Multi-Modal Tasks](README_multimodal.md#other-multi-modal-tasks)

------ (The following papers are moved to [README_2.md](README_2.md)) ------

- [Other High-level Vision Tasks](README_2.md#other-high-level-vision-tasks)
    - [Point Cloud / 3D](README_2.md#point-cloud--3d)
    - [Pose Estimation](README_2.md#pose-estimation)
    - [Tracking](README_2.md#tracking)
    - [Re-ID](README_2.md#re-id)
    - [Face](README_2.md#face)
    - [Scene Graph](README_2.md#scene-graph)
    - [Neural Architecture Search](README_2.md#neural-architecture-search)
- [Transfer / X-Supervised / X-Shot / Continual Learning](README_2.md#transfer--x-supervised--x-shot--continual-learning)
- [Low-level Vision Tasks](README_2.md#low-level-vision-tasks)
    - [Image Restoration](README_2.md#image-restoration)
    - [Video Restoration](README_2.md#video-restoration)
    - [Inpainting / Completion / Outpainting](README_2.md#inpainting--completion--outpainting)
    - [Image Generation](README_2.md#image-generation)
    - [Video Generation](README_2.md#video-generation)
    - [Transfer / Translation / Manipulation](README_2.md#transfer--translation--manipulation)
    - [Other Low-Level Tasks](README_2.md#other-low-level-tasks)
- [Reinforcement Learning](README_2.md#reinforcement-learning)
    - [Navigation](README_2.md#navigation)
    - [Other RL Tasks](README_2.md#other-rl-tasks)
- [Medical](README_2.md#medical)
    - [Medical Segmentation](README_2.md#medical-segmentation)
    - [Medical Classification](README_2.md#medical-classification)
    - [Medical Detection](README_2.md#medical-detection)
    - [Medical Reconstruction](README_2.md#medical-detection)
    - [Medical Low-Level Vision](README_2.md#medical-low-level-vision)
    - [Medical Vision-Language](README_2.md#medical-vision-language)
    - [Medical Others](README_2.md#medical-others)
- [Other Tasks](README_2.md#other-tasks)
- [Attention Mechanisms in Vision/NLP](README_2.md#attention-mechanisms-in-visionnlp)
    - [Attention for Vision](README_2.md#attention-for-vision)
    - [NLP](README_2.md#attention-for-nlp)
    - [Both](README_2.md#attention-for-both)
    - [Others](README_2.md#attention-for-others)

---

## Citation
If you find this repository useful, please consider citing this list:
```
@misc{chen2022transformerpaperlist,
    title = {Ultimate awesome paper list: transformer and attention},
    author = {Chen, Min-Hung},
    journal = {GitHub repository},
    url = {https://github.com/cmhungsteve/Awesome-Transformer-Attention},
    year = {2022},
}
```

---

## Survey
* "A Survey on Multimodal Large Language Models for Autonomous Driving", WACVW, 2024 (*Purdue*). [[Paper](https://arxiv.org/abs/2311.12320)][[GitHub](https://github.com/IrohXu/Awesome-Multimodal-LLM-Autonomous-Driving)]
* "Efficient Multimodal Large Language Models: A Survey", arXiv, 2024 (*Tencent*). [[Paper](https://arxiv.org/abs/2405.10739)][[GitHub](https://github.com/lijiannuist/Efficient-Multimodal-LLMs-Survey)]
* "From Sora What We Can See: A Survey of Text-to-Video Generation", arXiv, 2024 (*Newcastle University, UK*). [[Paper](https://arxiv.org/abs/2405.10674)][[GitHub](https://github.com/soraw-ai/Awesome-Text-to-Video-Generation)]
* "When LLMs step into the 3D World: A Survey and Meta-Analysis of 3D Tasks via Multi-modal Large Language Models", arXiv, 2024 (*Oxford*). [[Paper](https://arxiv.org/abs/2405.10255)][[GitHub](https://github.com/ActiveVisionLab/Awesome-LLM-3D)]
* "Foundation Models for Video Understanding: A Survey", arXiv, 2024 (*Aalborg University, Denmark*). [[Paper](https://arxiv.org/abs/2405.03770)][[GitHub](https://github.com/NeeluMadan/ViFM_Survey)]
* "Vision Mamba: A Comprehensive Survey and Taxonomy", arXiv, 2024 (*Chongqing University*). [[Paper](https://arxiv.org/abs/2405.04404)][[GitHub](https://github.com/lx6c78/Vision-Mamba-A-Comprehensive-Survey-and-Taxonomy)]
* "Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond", arXiv, 2024 (*GigaAI, China*). [[Paper](https://arxiv.org/abs/2405.03520)][[GitHub](https://github.com/GigaAI-research/General-World-Models-Survey)]
* "Video Diffusion Models: A Survey", arXiv, 2024 (*Bielefeld University, Germany*). [[Paper](https://arxiv.org/abs/2405.03150)][[GitHub](https://github.com/ndrwmlnk/Awesome-Video-Diffusion-Models)]
* "Unleashing the Power of Multi-Task Learning: A Comprehensive Survey Spanning Traditional, Deep, and Pretrained Foundation Model Eras", arXiv, 2024 (*Lehigh + UPenn*). [[Paper](https://arxiv.org/abs/2404.18961)]
* "Hallucination of Multimodal Large Language Models: A Survey", arXiv, 2024 (*NUS*). [[Paper](https://arxiv.org/abs/2404.18930)][[GitHub](https://github.com/showlab/Awesome-MLLM-Hallucination)]
* "A Survey on Vision Mamba: Models, Applications and Challenges", arXiv, 2024 (*HKUST*). [[Paper](https://arxiv.org/abs/2404.18861)][[GitHub](https://github.com/Ruixxxx/Awesome-Vision-Mamba-Models)]
* "State Space Model for New-Generation Network Alternative to Transformers: A Survey", arXiv, 2024 (*Anhui University*). [[Paper](https://arxiv.org/abs/2404.09516)][[GitHub](https://github.com/Event-AHU/Mamba_State_Space_Model_Paper_List)]
* "Exploring the Frontier of Vision-Language Models: A Survey of Current Methodologies and Future Directions", arXiv, 2024 (*IIT Patna*). [[Paper](https://arxiv.org/abs/2404.07214)]
* "From Pixels to Insights: A Survey on Automatic Chart Understanding in the Era of Large Foundation Models", arXiv, 2024 (*UIUC*). [[Paper](https://arxiv.org/abs/2403.12027)][[GitHub](https://github.com/khuangaf/Awesome-Chart-Understanding)]
* "Parameter-Efficient Fine-Tuning for Large Models: A Comprehensive Survey", arXiv, 2024 (*Northeastern*). [[Paper](https://arxiv.org/abs/2403.14608)]
* "Sora as an AGI World Model? A Complete Survey on Text-to-Video Generation", arXiv, 2024 (*Kyung Hee University*). [[Paper](https://arxiv.org/abs/2403.05131)]
* "Controllable Generation with Text-to-Image Diffusion Models: A Survey", arXiv, 2024 (*Beijing University of Posts and Telecommunications*). [[Paper](https://arxiv.org/abs/2403.04279)][[GitHub](https://github.com/PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models)]
* "Sora: A Review on Background, Technology, Limitations, and Opportunities of Large Vision Models", arXiv, 2024 (*Lehigh University, Pennsylvania*). [[Paper](https://arxiv.org/abs/2402.17177)][[GitHub](https://github.com/lichao-sun/SoraReview)]
* "Large Multimodal Agents: A Survey", arXiv, 2024 (*CUHK*). [[Paper](https://arxiv.org/abs/2402.15116)][[GitHub](https://github.com/jun0wanan/awesome-large-multimodal-agents)]
* "Parameter-Efficient Fine-Tuning for Pre-Trained Vision Models: A Survey", arXiv, 2024 (*BIGAI*). [[Paper](https://arxiv.org/abs/2402.02242)][[GitHub](https://github.com/synbol/Awesome-Parameter-Efficient-Transfer-Learning)]
* "Vision-Language Navigation with Embodied Intelligence: A Survey", arXiv, 2024 (*Qufu Normal University, China*). [[Paper](https://arxiv.org/abs/2402.14304)]
* "The (R)Evolution of Multimodal Large Language Models: A Survey", arXiv, 2024 (*University of Modena and Reggio Emilia (UniMoRE), Italy*). [[Paper](https://arxiv.org/abs/2402.12451)]
* "Masked Modeling for Self-supervised Representation Learning on Vision and Beyond", arXiv, 2024 (*Westlake University, China*). [[Paper](https://arxiv.org/abs/2401.00897)][[GitHub](https://github.com/Lupin1998/Awesome-MIM)]
* "Transformer for Object Re-Identification: A Survey", arXiv, 2024 (*Wuhan University*). [[Paper](https://arxiv.org/abs/2401.06960)]
* "Forging Vision Foundation Models for Autonomous Driving: Challenges, Methodologies, and Opportunities", arXiv, 2024 (*Huawei*). [[Paper](https://arxiv.org/abs/2401.08045)][[GtiHub](https://github.com/zhanghm1995/Forge_VFM4AD)]
* "MM-LLMs: Recent Advances in MultiModal Large Language Models", arXiv, 2024 (*Tencent*). [[Paper](https://arxiv.org/abs/2401.13601)]
* "From GPT-4 to Gemini and Beyond: Assessing the Landscape of MLLMs on Generalizability, Trustworthiness and Causality through Four Modalities", arXiv, 2024 (*Shanghai AI Lab*). [[Paper](https://arxiv.org/abs/2401.15071)]
* "A Survey on Hallucination in Large Vision-Language Models", arXiv, 2024 (*Huawei*). [[Paper](https://arxiv.org/abs/2402.00253)]
* "A Survey for Foundation Models in Autonomous Driving", arXiv, 2024 (*Motional, Massachusetts*). [[Paper](https://arxiv.org/abs/2402.01105)]
* "A Survey on Transformer Compression", arXiv, 2024 (*Huawei*). [[Paper](https://arxiv.org/abs/2402.05964)]
* "Vision + Language Applications: A Survey", CVPRW, 2023 (*Ritsumeikan University, Japan*). [[Paper](https://arxiv.org/abs/2305.14598)][[GitHub](https://github.com/Yutong-Zhou-cv/Awesome-Text-to-Image)]
* "Multimodal Learning With Transformers: A Survey", TPAMI, 2023 (*Tsinghua & Oxford*). [[Paper](https://arxiv.org/abs/2206.06488)]
* "A Survey of Visual Transformers", TNNLS, 2023 (*CAS*). [[Paper](https://arxiv.org/abs/2111.06091)][[GitHub](https://github.com/arekavandi/Transformer-SOD)]
* "Video Understanding with Large Language Models: A Survey", arXiv, 2023 (*University of Rochester*). [[Paper](https://arxiv.org/abs/2312.17432)][[GitHub](https://github.com/yunlong10/Awesome-LLMs-for-Video-Understanding)]
* "Visual Instruction Tuning towards General-Purpose Multimodal Model: A Survey", arXiv, 2023 (*NTU, Singapore*). [[Paper](https://arxiv.org/abs/2312.16602)]
* "A Survey of Reasoning with Foundation Models: Concepts, Methodologies, and Outlook", arXiv, 2023 (*Huawei*). [[Paper](https://arxiv.org/abs/2312.11562)][[GitHub](https://github.com/reasoning-survey/Awesome-Reasoning-Foundation-Models)]
* "A Challenger to GPT-4V? Early Explorations of Gemini in Visual Expertise", arXiv, 2023 (*Tencent*). [[Paper](https://arxiv.org/abs/2312.12436)][GitHub](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models)]
* "Towards the Unification of Generative and Discriminative Visual Foundation Model: A Survey", arXiv, 2023 (*JHU*). [[Paper](https://arxiv.org/abs/2312.10163)]
* "Explainability of Vision Transformers: A Comprehensive Review and New Perspectives", arXiv, 2023 (*Institute for Research in Fundamental Sciences (IPM), Iran*). [[Paper](https://arxiv.org/abs/2311.06786)]
* "Vision-Language Instruction Tuning: A Review and Analysis", arXiv, 2023 (*Tencent*). [[Paper](https://arxiv.org/abs/2311.08172)][[GitHub (in construction)](https://github.com/palchenli/VL-Instruction-Tuning)]
* "Understanding Video Transformers for Segmentation: A Survey of Application and Interpretability", arXiv, 2023 (*York University*). [[Paper](https://arxiv.org/abs/2310.12296)]
* "Unsupervised Object Localization in the Era of Self-Supervised ViTs: A Survey", arXiv, 2023 (*valeo.ai, France*). [[Paper](https://arxiv.org/abs/2310.12904)][[GitHub](https://github.com/valeoai/Awesome-Unsupervised-Object-Localization)]
* "A Survey on Video Diffusion Models", arXiv, 2023 (*Fudan*). [[Paper](https://arxiv.org/abs/2310.10647)][[GitHub](https://github.com/ChenHsing/Awesome-Video-Diffusion-Models)]
* "The Dawn of LMMs: Preliminary Explorations with GPT-4V(ision)", arXiv, 2023 (*Microsoft*). [[Paper](https://arxiv.org/abs/2309.17421)]
* "Multimodal Foundation Models: From Specialists to General-Purpose Assistants", arXiv, 2023 (*Microsoft*). [[Paper](https://arxiv.org/abs/2309.10020)]
* "Transformers in Small Object Detection: A Benchmark and Survey of State-of-the-Art", arXiv, 2023 (*University of Western Australia*). [[Paper](https://arxiv.org/abs/2309.04902)]
* "RenAIssance: A Survey into AI Text-to-Image Generation in the Era of Large Model", arXiv, 2023 (*University of Sydney*). [[Paper](https://arxiv.org/abs/2309.00810)]
* "A survey on efficient vision transformers: algorithms, techniques, and performance benchmarking", arXiv, 2023 (*The University of Sydney*). [[Paper](https://arxiv.org/abs/2309.02031)]
* "From CNN to Transformer: A Review of Medical Image Segmentation Models", arXiv, 2023 (*UESTC*). [[Paper](https://arxiv.org/abs/2308.05305)]
* "Foundational Models Defining a New Era in Vision: A Survey and Outlook", arXiv, 2023 (*MBZUAI*). [[Paper](https://arxiv.org/abs/2307.13721)][[GitHub](https://github.com/awaisrauf/Awesome-CV-Foundational-Models)]
* "A Systematic Survey of Prompt Engineering on Vision-Language Foundation Models", arXiv, 2023 (*Oxford*). [[Paper](https://arxiv.org/abs/2307.12980)]
* "Robust Visual Question Answering: Datasets, Methods, and Future Challenges", arXiv, 2023 (*Xi'an Jiaotong University*). [[Paper](https://arxiv.org/abs/2307.11471)]
* "A Survey on Open-Vocabulary Detection and Segmentation: Past, Present, and Future", arXiv, 2023 (*HKUST*). [[Paper](https://arxiv.org/abs/2307.09220)]
* "Transformers in Reinforcement Learning: A Survey", arXiv, 2023 (*Mila*). [[Paper](https://arxiv.org/abs/2307.05979)]
* "Vision Language Transformers: A Survey", arXiv, 2023 (*Boise State University, Idaho*). [[Paper](https://arxiv.org/abs/2307.03254)]
* "Towards Open Vocabulary Learning: A Survey", arXiv, 2023 (*Peking*). [[Paper](https://arxiv.org/abs/2306.15880)][[GitHub](https://github.com/jianzongwu/Awesome-Open-Vocabulary)]
* "Large Multimodal Models: Notes on CVPR 2023 Tutorial", arXiv, 2023 (*Microsoft*). [[Paper](https://arxiv.org/abs/2306.14895)]
* "A Survey on Multimodal Large Language Models", arXiv, 2023 (*USTC*). [[Paper](https://arxiv.org/abs/2306.13549)][[GitHub](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models)]
* "2D Object Detection with Transformers: A Review", arXiv, 2023 (*German Research Center for Artificial Intelligence, Germany*). [[Paper](https://arxiv.org/abs/2306.04670)]
* "Visual Question Answering: A Survey on Techniques and Common Trends in Recent Literature", arXiv, 2023 (*Eldorado’s Institute of Technology, Brazil*). [[Paper](https://arxiv.org/abs/2305.11033)]
* "Vision-Language Models in Remote Sensing: Current Progress and Future Trends", arXiv, 2023 (*NYU*). [[Paper](https://arxiv.org/abs/2305.05726)]
* "Visual Tuning", arXiv, 2023 (*The Hong Kong Polytechnic University*). [[Paper](https://arxiv.org/abs/2305.06061)]
* "Self-supervised Learning for Pre-Training 3D Point Clouds: A Survey", arXiv, 2023 (*Fudan University*). [[Paper](https://arxiv.org/abs/2305.04691)]
* "Semantic Segmentation using Vision Transformers: A survey", arXiv, 2023 (*University of Peradeniya, Sri Lanka*). [[Paper](https://arxiv.org/abs/2305.03273)]
* "A Review of Deep Learning for Video Captioning", arXiv, 2023 (*Deakin University, Australia*). [[Paper](https://arxiv.org/abs/2304.11431)]
* "Transformer-Based Visual Segmentation: A Survey", arXiv, 2023 (*NTU, Singapore*). [[Paper](https://arxiv.org/abs/2304.09854)][[GitHub](https://github.com/lxtGH/Awesome-Segmenation-With-Transformer)]
* "Vision-Language Models for Vision Tasks: A Survey", arXiv, 2023 (*?*). [[Paper](https://arxiv.org/abs/2304.00685)][[GitHub (in construction)](https://github.com/jingyi0000/VLM_survey)]
* "Text-to-image Diffusion Model in Generative AI: A Survey", arXiv, 2023 (*KAIST*). [[Paper](https://arxiv.org/abs/2303.07909)]
* "Foundation Models for Decision Making: Problems, Methods, and Opportunities", arXiv, 2023 (*Berkeley + Google*). [[Paper](https://arxiv.org/abs/2303.04129)]
* "Advances in Medical Image Analysis with Vision Transformers: A Comprehensive Review", arXiv, 2023 (*RWTH Aachen University, Germany*). [[Paper](https://arxiv.org/abs/2301.03505)][[GitHub](https://github.com/mindflow-institue/Awesome-Transformer)]
* "Efficiency 360: Efficient Vision Transformers", arXiv, 2023 (*IBM*). [[Paper](https://arxiv.org/abs/2302.08374)][[GitHub](https://github.com/badripatro/efficient360)]
* "Transformer-based Generative Adversarial Networks in Computer Vision: A Comprehensive Survey", arXiv, 2023 (*Indian Institute of Information Technology*). [[Paper](https://arxiv.org/abs/2302.08641)]
* "Large-scale Multi-Modal Pre-trained Models: A Comprehensive Survey", arXiv, 2023 (*Pengcheng Laboratory*). [[Paper](https://arxiv.org/abs/2302.10035)][[GitHub](https://github.com/wangxiao5791509/MultiModal_BigModels_Survey)]
* "A Survey on Visual Transformer", TPAMI, 2022 (*Huawei*). [[Paper](https://arxiv.org/abs/2012.12556)]
* "Attention mechanisms in computer vision: A survey", Computational Visual Media, 2022 (*Tsinghua University, China*). [[Paper](https://arxiv.org/abs/2111.07624)][[Springer](https://link.springer.com/article/10.1007/s41095-022-0271-y)][[Github](https://github.com/MenghaoGuo/Awesome-Vision-Attentions)]
* "A Comprehensive Study of Vision Transformers on Dense Prediction Tasks", VISAP, 2022 (*NavInfo Europe, Netherlands*). [[Paper](https://arxiv.org/abs/2201.08683)]
* "Vision-and-Language Pretrained Models: A Survey", IJCAI, 2022 (*The University of Sydney*). [[Paper](https://arxiv.org/abs/2204.07356)]
* "Vision Transformers in Medical Imaging: A Review", arXiv, 2022 (*Covenant University, Nigeria*). [[Paper](https://arxiv.org/abs/2211.10043)]
* "A Comprehensive Survey of Transformers for Computer Vision", arXiv, 2022 (*Sejong University*). [[Paper](https://arxiv.org/abs/2211.06004)]
* "Vision-Language Pre-training: Basics, Recent Advances, and Future Trends", arXiv, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2210.09263)]
* "Vision+X: A Survey on Multimodal Learning in the Light of Data", arXiv, 2022 (*Illinois Institute of Technology, Chicago*). [[Paper](https://arxiv.org/abs/2210.02884)]
* "Vision Transformers for Action Recognition: A Survey", arXiv, 2022 (*Charles Sturt University, Australia*). [[Paper](https://arxiv.org/abs/2209.05700)]
* "VLP: A Survey on Vision-Language Pre-training", arXiv, 2022 (*CAS*). [[Paper](https://arxiv.org/abs/2202.09061)]
* "Transformers in Remote Sensing: A Survey", arXiv, 2022 (*MBZUAI*). [[Paper](https://arxiv.org/abs/2209.01206)][[Github](https://github.com/VIROBO-15/Transformer-in-Remote-Sensing)]
* "Medical image analysis based on transformer: A Review", arXiv, 2022 (*NUS, Singapore*). [[Paper](https://arxiv.org/abs/2208.06643)]
* "3D Vision with Transformers: A Survey", arXiv, 2022 (*MBZUAI*). [[Paper](https://arxiv.org/abs/2208.04309)][[GitHub](https://github.com/lahoud/3d-vision-transformers)]
* "Vision Transformers: State of the Art and Research Challenges", arXiv, 2022 (*NYCU*). [[Paper](https://arxiv.org/abs/2207.03041)]
* "Transformers in Medical Imaging: A Survey", arXiv, 2022 (*MBZUAI*). [[Paper](https://arxiv.org/abs/2201.09873)][[GitHub](https://github.com/fahadshamshad/awesome-transformers-in-medical-imaging)]
* "Multimodal Learning with Transformers: A Survey", arXiv, 2022 (*Oxford*). [[Paper](https://arxiv.org/abs/2206.06488)]
* "Transforming medical imaging with Transformers? A comparative review of key properties, current progresses, and future perspectives", arXiv, 2022 (*CAS*). [[Paper](https://arxiv.org/abs/2206.01136)]
* "Transformers in 3D Point Clouds: A Survey", arXiv, 2022 (*University of Waterloo*). [[Paper](https://arxiv.org/abs/2205.07417)]
* "A survey on attention mechanisms for medical applications: are we moving towards better algorithms?", arXiv, 2022 (*INESC TEC and University of Porto, Portugal*). [[Paper](https://arxiv.org/abs/2204.12406)]
* "Efficient Transformers: A Survey", arXiv, 2022 (*Google*). [[Paper](https://arxiv.org/abs/2009.06732)]
* "Are we ready for a new paradigm shift? A Survey on Visual Deep MLP", arXiv, 2022 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2111.04060)]
* "Vision Transformers in Medical Computer Vision - A Contemplative Retrospection", arXiv, 2022 (*National University of Sciences and Technology (NUST), Pakistan*). [[Paper](https://arxiv.org/abs/2203.15269)]
* "Video Transformers: A Survey", arXiv, 2022 (*Universitat de Barcelona, Spain*). [[Paper](https://arxiv.org/abs/2201.05991)] 
* "Transformers in Medical Image Analysis: A Review", arXiv, 2022 (*Nanjing University*). [[Paper](https://arxiv.org/abs/2202.12165)]
* "Recent Advances in Vision Transformer: A Survey and Outlook of Recent Work", arXiv, 2022 (*?*). [[Paper](https://arxiv.org/abs/2203.01536)]
* "Transformers Meet Visual Learning Understanding: A Comprehensive Review", arXiv, 2022 (*Xidian University*). [[Paper](https://arxiv.org/abs/2203.12944)]
* "Image Captioning In the Transformer Age", arXiv, 2022 (*Alibaba*). [[Paper](https://arxiv.org/abs/2204.07374)][[GitHub](https://github.com/SjokerLily/awesome-image-captioning)]
* "Visual Attention Methods in Deep Learning: An In-Depth Survey", arXiv, 2022 (*Fayoum University, Egypt*). [[Paper](https://arxiv.org/abs/2204.07756)]
* "Transformers in Vision: A Survey", ACM Computing Surveys, 2021 (*MBZUAI*). [[Paper](https://arxiv.org/abs/2101.01169)]
* "Survey: Transformer based Video-Language Pre-training", arXiv, 2021 (*Renmin University of China*). [[Paper](https://arxiv.org/abs/2109.09920)]
* "A Survey of Transformers", arXiv, 2021 (*Fudan*). [[Paper](https://arxiv.org/abs/2106.04554)]
* "Attention mechanisms and deep learning for machine vision: A survey of the state of the art", arXiv, 2021 (*University of Kashmir, India*). [[Paper](https://arxiv.org/abs/2106.07550)]

[[Back to Overview](#overview)]


## Image Classification / Backbone
### Replace Conv w/ Attention
#### Pure Attention
* **LR-Net**: "Local Relation Networks for Image Recognition", ICCV, 2019 (*Microsoft*). [[Paper](https://arxiv.org/abs/1904.11491)][[PyTorch (gan3sh500)](https://github.com/gan3sh500/local-relational-nets)]
* **SASA**: "Stand-Alone Self-Attention in Vision Models", NeurIPS, 2019 (*Google*). [[Paper](https://arxiv.org/abs/1906.05909)][[PyTorch-1 (leaderj1001)](https://github.com/leaderj1001/Stand-Alone-Self-Attention)][[PyTorch-2 (MerHS)](https://github.com/MerHS/SASA-pytorch)]
* **Axial-Transformer**: "Axial Attention in Multidimensional Transformers", arXiv, 2019 (*Google*). [[Paper](https://openreview.net/forum?id=H1e5GJBtDr)][[PyTorch (lucidrains)](https://github.com/lucidrains/axial-attention)]
* **SAN**: "Exploring Self-attention for Image Recognition", CVPR, 2020 (*CUHK + Intel*). [[Paper](https://arxiv.org/abs/2004.13621)][[PyTorch](https://github.com/hszhao/SAN)]
* **Axial-DeepLab**: "Axial-DeepLab: Stand-Alone Axial-Attention for Panoptic Segmentation", ECCV, 2020 (*Google*). [[Paper](https://arxiv.org/abs/2003.07853)][[PyTorch](https://github.com/csrhddlam/axial-deeplab)]
#### Conv-stem + Attention
* **GSA-Net**: "Global Self-Attention Networks for Image Recognition", arXiv, 2020 (*Google*). [[Paper](https://arxiv.org/abs/2010.03019)][[PyTorch (lucidrains)](https://github.com/lucidrains/global-self-attention-network)]
* **HaloNet**: "Scaling Local Self-Attention For Parameter Efficient Visual Backbones", CVPR, 2021 (*Google*). [[Paper](https://arxiv.org/abs/2103.12731)][[PyTorch (lucidrains)](https://github.com/lucidrains/halonet-pytorch)]
* **CoTNet**: "Contextual Transformer Networks for Visual Recognition", CVPRW, 2021 (*JD*). [[Paper](https://arxiv.org/abs/2107.12292)][[PyTorch](https://github.com/JDAI-CV/CoTNet)]
* **HAT-Net**: "Vision Transformers with Hierarchical Attention", arXiv, 2022 (*ETHZ*). [[Paper](https://arxiv.org/abs/2106.03180)][[PyTorch (in construction)](https://github.com/yun-liu/HAT-Net)]
#### Conv + Attention
* **AA**: "Attention Augmented Convolutional Networks", ICCV, 2019 (*Google*). [[Paper](https://arxiv.org/abs/1904.09925)][[PyTorch (leaderj1001)](https://github.com/leaderj1001/Attention-Augmented-Conv2d)][[Tensorflow (titu1994)](https://github.com/titu1994/keras-attention-augmented-convs)]
* **GCNet**: "Global Context Networks", ICCVW, 2019 (& TPAMI 2020) (*Microsoft*). [[Paper](https://arxiv.org/abs/2012.13375)][[PyTorch](https://github.com/xvjiarui/GCNet)]
* **LambdaNetworks**: "LambdaNetworks: Modeling long-range Interactions without Attention", ICLR, 2021 (*Google*). [[Paper](https://openreview.net/forum?id=xTJEN-ggl1b)][[PyTorch-1 (lucidrains)](https://github.com/lucidrains/lambda-networks)][[PyTorch-2 (leaderj1001)](https://github.com/leaderj1001/LambdaNetworks)]
* **BoTNet**: "Bottleneck Transformers for Visual Recognition", CVPR, 2021 (*Google*). [[Paper](https://arxiv.org/abs/2101.11605)][[PyTorch-1 (lucidrains)](https://github.com/lucidrains/bottleneck-transformer-pytorch)][[PyTorch-2 (leaderj1001)](https://github.com/leaderj1001/BottleneckTransformers)]
* **GCT**: "Gaussian Context Transformer", CVPR, 2021 (*Zhejiang University*). [[Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Ruan_Gaussian_Context_Transformer_CVPR_2021_paper.html)]
* **CoAtNet**: "CoAtNet: Marrying Convolution and Attention for All Data Sizes", NeurIPS, 2021 (*Google*). [[Paper](https://arxiv.org/abs/2106.04803)]
* **ACmix**: "On the Integration of Self-Attention and Convolution", CVPR, 2022 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2111.14556)][[PyTorch](https://github.com/LeapLabTHU/ACmix)]

[[Back to Overview](#overview)]

### Vision Transformer
#### General Vision Transformer
* **ViT**: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale", ICLR, 2021 (*Google*). [[Paper](https://openreview.net/forum?id=YicbFdNTTy)][[Tensorflow](https://github.com/google-research/vision_transformer)][[PyTorch (lucidrains)](https://github.com/lucidrains/vit-pytorch)][[JAX (conceptofmind)](https://github.com/conceptofmind/vit-flax)]
* **Perceiver**: "Perceiver: General Perception with Iterative Attention", ICML, 2021 (*DeepMind*). [[Paper](https://arxiv.org/abs/2103.03206)][[PyTorch (lucidrains)](https://github.com/lucidrains/perceiver-pytorch)]
* **PiT**: "Rethinking Spatial Dimensions of Vision Transformers", ICCV, 2021 (*NAVER*). [[Paper](https://arxiv.org/abs/2103.16302)][[PyTorch](https://github.com/naver-ai/pit)]
* **VT**: "Visual Transformers: Where Do Transformers Really Belong in Vision Models?", ICCV, 2021 (*Facebook*). [[Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Wu_Visual_Transformers_Where_Do_Transformers_Really_Belong_in_Vision_Models_ICCV_2021_paper.html)][[PyTorch (tahmid0007)](https://github.com/tahmid0007/VisualTransformers)] 
* **PVT**: "Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions", ICCV, 2021 (*Nanjing University*). [[Paper](https://arxiv.org/abs/2102.12122)][[PyTorch](https://github.com/whai362/PVT)] 
* **iRPE**: "Rethinking and Improving Relative Position Encoding for Vision Transformer", ICCV, 2021 (*Microsoft*). [[Paper](https://arxiv.org/abs/2107.14222)][[PyTorch](https://github.com/microsoft/Cream/tree/main/iRPE)]
* **CaiT**: "Going deeper with Image Transformers", ICCV, 2021 (*Facebook*). [[Paper](https://arxiv.org/abs/2103.17239)][[PyTorch](https://github.com/facebookresearch/deit)]
* **Swin-Transformer**: "Swin Transformer: Hierarchical Vision Transformer using Shifted Windows", ICCV, 2021 (*Microsoft*). [[Paper](https://arxiv.org/abs/2103.14030)][[PyTorch](https://github.com/microsoft/Swin-Transformer)][[PyTorch (berniwal)](https://github.com/berniwal/swin-transformer-pytorch)]
* **T2T-ViT**: "Tokens-to-Token ViT: Training Vision Transformers from Scratch on ImageNet", ICCV, 2021 (*Yitu*). [[Paper](https://arxiv.org/abs/2101.11986)][[PyTorch](https://github.com/yitu-opensource/T2T-ViT)]
* **FFNBN**: "Leveraging Batch Normalization for Vision Transformers", ICCVW, 2021 (*Microsoft*). [[Paper](https://openaccess.thecvf.com/content/ICCV2021W/NeurArch/html/Yao_Leveraging_Batch_Normalization_for_Vision_Transformers_ICCVW_2021_paper.html)]
* **DPT**: "DPT: Deformable Patch-based Transformer for Visual Recognition", ACMMM, 2021 (*CAS*). [[Paper](https://arxiv.org/abs/2107.14467)][[PyTorch](https://github.com/CASIA-IVA-Lab/DPT)]
* **Focal**: "Focal Attention for Long-Range Interactions in Vision Transformers", NeurIPS, 2021 (*Microsoft*). [[Paper](https://arxiv.org/abs/2107.00641)][[PyTorch](https://github.com/microsoft/Focal-Transformer)]
* **XCiT**: "XCiT: Cross-Covariance Image Transformers", NeurIPS, 2021 (*Facebook*). [[Paper](https://arxiv.org/abs/2106.09681)]
* **Twins**: "Twins: Revisiting Spatial Attention Design in Vision Transformers", NeurIPS, 2021 (*Meituan*). [[Paper](https://arxiv.org/abs/2104.13840)][[PyTorch)](https://github.com/Meituan-AutoML/Twins)]
* **ARM**: "Blending Anti-Aliasing into Vision Transformer", NeurIPS, 2021 (*Amazon*). [[Paper](https://arxiv.org/abs/2110.15156)][[GitHub (in construction)](https://github.com/amazon-research/anti-aliasing-transformer)]
* **DVT**: "Not All Images are Worth 16x16 Words: Dynamic Vision Transformers with Adaptive Sequence Length", NeurIPS, 2021 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2105.15075)][[PyTorch](https://github.com/blackfeather-wang/Dynamic-Vision-Transformer)]
* **Aug-S**: "Augmented Shortcuts for Vision Transformers", NeurIPS, 2021 (*Huawei*). [[Paper](https://arxiv.org/abs/2106.15941)]
* **TNT**: "Transformer in Transformer", NeurIPS, 2021 (*Huawei*). [[Paper](https://arxiv.org/abs/2103.00112)][[PyTorch](https://github.com/huawei-noah/CV-Backbones/tree/master/tnt_pytorch)][[PyTorch (lucidrains)](https://github.com/lucidrains/transformer-in-transformer)]
* **ViTAE**: "ViTAE: Vision Transformer Advanced by Exploring Intrinsic Inductive Bias", NeurIPS, 2021 (*The University of Sydney*). [[Paper](https://arxiv.org/abs/2106.03348)][[PyTorch](https://github.com/Annbless/ViTAE)]
* **DeepViT**: "DeepViT: Towards Deeper Vision Transformer", arXiv, 2021 (*NUS + ByteDance*). [[Paper](https://arxiv.org/abs/2103.11886)][[Code](https://github.com/zhoudaquan/dvit_repo)]
* **So-ViT**: "So-ViT: Mind Visual Tokens for Vision Transformer", arXiv, 2021 (*Dalian University of Technology*). [[Paper](https://arxiv.org/abs/2104.10935)][[PyTorch](https://github.com/jiangtaoxie/So-ViT)]
* **LV-ViT**: "All Tokens Matter: Token Labeling for Training Better Vision Transformers", NeurIPS, 2021 (*ByteDance*). [[Paper](https://arxiv.org/abs/2104.10858)][[PyTorch](https://github.com/zihangJiang/TokenLabeling)]
* **NesT**: "Aggregating Nested Transformers", arXiv, 2021 (*Google*). [[Paper](https://arxiv.org/abs/2105.12723)][[Tensorflow](https://github.com/google-research/nested-transformer)]
* **KVT**: "KVT: k-NN Attention for Boosting Vision Transformers", arXiv, 2021 (*Alibaba*). [[Paper](https://arxiv.org/abs/2106.00515)]
* **Refined-ViT**: "Refiner: Refining Self-attention for Vision Transformers", arXiv, 2021 (*NUS, Singapore*). [[Paper](https://arxiv.org/abs/2106.03714)][[PyTorch](https://github.com/zhoudaquan/Refiner_ViT)]
* **Shuffle-Transformer**: "Shuffle Transformer: Rethinking Spatial Shuffle for Vision Transformer", arXiv, 2021 (*Tencent*). [[Paper](https://arxiv.org/abs/2106.03650)]
* **CAT**: "CAT: Cross Attention in Vision Transformer", arXiv, 2021 (*KuaiShou*). [[Paper](https://arxiv.org/abs/2106.05786)][[PyTorch](https://github.com/linhezheng19/CAT)]
* **V-MoE**: "Scaling Vision with Sparse Mixture of Experts", arXiv, 2021 (*Google*). [[Paper](https://arxiv.org/abs/2106.05974)]
* **P2T**: "P2T: Pyramid Pooling Transformer for Scene Understanding", arXiv, 2021 (*Nankai University*). [[Paper](https://arxiv.org/abs/2106.12011)]
* **PvTv2**: "PVTv2: Improved Baselines with Pyramid Vision Transformer", arXiv, 2021 (*Nanjing University*). [[Paper](https://arxiv.org/abs/2106.13797)][[PyTorch](https://github.com/whai362/PVT)]
* **LG-Transformer**: "Local-to-Global Self-Attention in Vision Transformers", arXiv, 2021 (*IIAI, UAE*). [[Paper](https://arxiv.org/abs/2107.04735)]
* **ViP**: "Visual Parser: Representing Part-whole Hierarchies with Transformers", arXiv, 2021 (*Oxford*). [[Paper](https://arxiv.org/abs/2107.05790)]
* **Scaled-ReLU**: "Scaled ReLU Matters for Training Vision Transformers", AAAI, 2022 (*Alibaba*). [[Paper](https://arxiv.org/abs/2109.03810)]
* **LIT**: "Less is More: Pay Less Attention in Vision Transformers", AAAI, 2022 (*Monash University*). [[Paper](https://arxiv.org/abs/2105.14217)][[PyTorch](https://github.com/zip-group/LIT)]
* **DTN**: "Dynamic Token Normalization Improves Vision Transformer", ICLR, 2022 (*Tencent*). [[Paper](https://arxiv.org/abs/2112.02624)][[PyTorch (in construction)](https://github.com/wqshao126/DTN)]
* **RegionViT**: "RegionViT: Regional-to-Local Attention for Vision Transformers", ICLR, 2022 (*MIT-IBM Watson*). [[Paper](https://arxiv.org/abs/2106.02689)][[PyTorch](https://github.com/ibm/regionvit)]
* **CrossFormer**: "CrossFormer: A Versatile Vision Transformer Based on Cross-scale Attention", ICLR, 2022 (*Zhejiang University*). [[Paper](https://arxiv.org/abs/2108.00154)][[PyTorch](https://github.com/cheerss/CrossFormer)]
* **?**: "Scaling the Depth of Vision Transformers via the Fourier Domain Analysis", ICLR, 2022 (*UT Austin*). [[Paper](https://openreview.net/forum?id=O476oWmiNNp)]
* **ViT-G**: "Scaling Vision Transformers", CVPR, 2022 (*Google*). [[Paper](https://arxiv.org/abs/2106.04560)]
* **CSWin**: "CSWin Transformer: A General Vision Transformer Backbone with Cross-Shaped Windows", CVPR, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2107.00652)][[PyTorch](https://github.com/microsoft/CSWin-Transformer)]
* **MPViT**: "MPViT: Multi-Path Vision Transformer for Dense Prediction", CVPR, 2022 (*KAIST*). [[Paper](https://arxiv.org/abs/2112.11010)][[PyTorch](https://github.com/youngwanLEE/MPViT)]
* **Diverse-ViT**: "The Principle of Diversity: Training Stronger Vision Transformers Calls for Reducing All Levels of Redundancy", CVPR, 2022 (*UT Austin*). [[Paper](https://arxiv.org/abs/2203.06345)][[PyTorch](https://github.com/VITA-Group/Diverse-ViT)]
* **DW-ViT**: "Beyond Fixation: Dynamic Window Visual Transformer", CVPR, 2022 (*Dark Matter AI, China*). [[Paper](https://arxiv.org/abs/2203.12856)][[PyTorch (in construction)](https://github.com/pzhren/DW-ViT)]
* **MixFormer**: "MixFormer: Mixing Features across Windows and Dimensions", CVPR, 2022 (*Baidu*). [[Paper](https://arxiv.org/abs/2204.02557)][[Paddle](https://github.com/PaddlePaddle/PaddleClas)]
* **DAT**: "Vision Transformer with Deformable Attention", CVPR, 2022 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2201.00520)][[PyTorch](https://github.com/LeapLabTHU/DAT)]
* **Swin-Transformer-V2**: "Swin Transformer V2: Scaling Up Capacity and Resolution", CVPR, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2111.09883)][[PyTorch](https://github.com/microsoft/Swin-Transformer)]
* **MSG-Transformer**: "MSG-Transformer: Exchanging Local Spatial Information by Manipulating Messenger Tokens", CVPR, 2022 (*Huazhong University of Science & Technology*). [[Paper](https://arxiv.org/abs/2105.15168)][[PyTorch](https://github.com/hustvl/MSG-Transformer)]
* **NomMer**: "NomMer: Nominate Synergistic Context in Vision Transformer for Visual Recognition", CVPR, 2022 (*Tencent*). [[Paper](https://arxiv.org/abs/2111.12994)][[PyTorch](https://github.com/TencentYoutuResearch/VisualRecognition-NomMer)]
* **Shunted**: "Shunted Self-Attention via Multi-Scale Token Aggregation", CVPR, 2022 (*NUS*). [[Paper](https://arxiv.org/abs/2111.15193)][[PyTorch](https://github.com/OliverRensu/Shunted-Transformer)]
* **PyramidTNT**: "PyramidTNT: Improved Transformer-in-Transformer Baselines with Pyramid Architecture", CVPRW, 2022 (*Huawei*). [[Paper](https://arxiv.org/abs/2201.00978)][[PyTorch](https://github.com/huawei-noah/CV-Backbones/tree/master/tnt_pytorch)]
* **X-ViT**: "X-ViT: High Performance Linear Vision Transformer without Softmax", CVPRW, 2022 (*Kakao*). [[Paper](https://arxiv.org/abs/2205.13805)]
* **ReMixer**: "ReMixer: Object-aware Mixing Layer for Vision Transformers", CVPRW, 2022 (*KAIST*). [[Paper](https://drive.google.com/file/d/1E6rXtj5h6tXiJR8Ae8u1vQcwyNyTZSVc/view)][[PyTorch](https://github.com/alinlab/remixer)]
* **UN**: "Unified Normalization for Accelerating and Stabilizing Transformers", ACMMM, 2022 (*Hikvision*). [[Paper](https://arxiv.org/abs/2208.01313)][[Code (in construction)](https://github.com/hikvision-research/Unified-Normalization)]
* **Wave-ViT**: "Wave-ViT: Unifying Wavelet and Transformers for Visual Representation Learning", ECCV, 2022 (*JD*). [[Paper](https://arxiv.org/abs/2207.04978)][[PyTorch](https://github.com/YehLi/ImageNetModel)]
* **DaViT**: "DaViT: Dual Attention Vision Transformers", ECCV, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2204.03645)][[PyTorch](https://github.com/dingmyu/davit)]
* **ScalableViT**: "ScalableViT: Rethinking the Context-oriented Generalization of Vision Transformer", ECCV, 2022 (*ByteDance*). [[Paper](https://arxiv.org/abs/2203.10790)]
* **MaxViT**: "MaxViT: Multi-Axis Vision Transformer", ECCV, 2022 (*Google*). [[Paper](https://arxiv.org/abs/2204.01697)][[Tensorflow](https://github.com/google-research/maxvit)]
* **VSA**: "VSA: Learning Varied-Size Window Attention in Vision Transformers", ECCV, 2022 (*The University of Sydney*). [[Paper](https://arxiv.org/abs/2204.08446)][[PyTorch](https://github.com/ViTAE-Transformer/ViTAE-VSA)]
* **?**: "Expediting Large-Scale Vision Transformer for Dense Prediction without Fine-tuning", NeurIPS, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2210.01035)]
* **Ortho**: "Orthogonal Transformer: An Efficient Vision Transformer Backbone with Token Orthogonalization", NeurIPS, 2022 (*CAS*). [[Paper](https://openreview.net/forum?id=GGtH47T31ZC)]
* **PerViT**: "Peripheral Vision Transformer", NeurIPS, 2022 (*POSTECH*). [[Paper](https://arxiv.org/abs/2206.06801)]
* **LITv2**: "Fast Vision Transformers with HiLo Attention", NeurIPS, 2022 (*Monash University*). [[Paper](https://arxiv.org/abs/2205.13213)][[PyTorch](https://github.com/zip-group/LITv2)]
* **BViT**: "BViT: Broad Attention based Vision Transformer", arXiv, 2022 (*CAS*). [[Paper](https://arxiv.org/abs/2202.06268)]
* **O-ViT**: "O-ViT: Orthogonal Vision Transformer", arXiv, 2022 (*East China Normal University*). [[Paper](https://arxiv.org/abs/2201.12133)]
* **MOA-Transformer**: "Aggregating Global Features into Local Vision Transformer", arXiv, 2022 (*University of Kansas*). [[Paper](https://arxiv.org/abs/2201.12903)][[PyTorch](https://github.com/krushi1992/MOA-transformer)]
* **BOAT**: "BOAT: Bilateral Local Attention Vision Transformer", arXiv, 2022 (*Baidu + HKU*). [[Paper](https://arxiv.org/abs/2201.13027)]
* **ViTAEv2**: "ViTAEv2: Vision Transformer Advanced by Exploring Inductive Bias for Image Recognition and Beyond", arXiv, 2022 (*The University of Sydney*). [[Paper](https://arxiv.org/abs/2202.10108)]
* **HiP**: "Hierarchical Perceiver", arXiv, 2022 (*DeepMind*). [[Paper](https://arxiv.org/abs/2202.10890)]
* **PatchMerger**: "Learning to Merge Tokens in Vision Transformers", arXiv, 2022 (*Google*). [[Paper](https://arxiv.org/abs/2202.12015)]
* **DGT**: "Dynamic Group Transformer: A General Vision Transformer Backbone with Dynamic Group Attention", arXiv, 2022 (*Baidu*). [[Paper](https://arxiv.org/abs/2203.03937)]
* **NAT**: "Neighborhood Attention Transformer", arXiv, 2022 (*Oregon*). [[Paper](https://arxiv.org/abs/2204.07143)][[PyTorch](https://github.com/SHI-Labs/Neighborhood-Attention-Transformer)]
* **ASF-former**: "Adaptive Split-Fusion Transformer", arXiv, 2022 (*Fudan*). [[Paper](https://arxiv.org/abs/2204.12196)][[PyTorch (in construction)](https://github.com/szx503045266/ASF-former)]
* **SP-ViT**: "SP-ViT: Learning 2D Spatial Priors for Vision Transformers", arXiv, 2022 (*Alibaba*). [[Paper](https://arxiv.org/abs/2206.07662)]
* **EATFormer**: "EATFormer: Improving Vision Transformer Inspired by Evolutionary Algorithm", arXiv, 2022 (*Zhejiang University*). [[Paper](https://arxiv.org/abs/2206.09325)]
* **LinGlo**: "Rethinking Query-Key Pairwise Interactions in Vision Transformers", arXiv, 2022 (*TCL Research Wuhan*). [[Paper](https://arxiv.org/abs/2207.00188)]
* **Dual-ViT**: "Dual Vision Transformer", arXiv, 2022 (*JD*). [[Paper](https://arxiv.org/abs/2207.04976)][[PyTorch](https://github.com/YehLi/ImageNetModel)]
* **MMA**: "Multi-manifold Attention for Vision Transformers", arXiv, 2022 (*Centre for Research and Technology Hellas, Greece*). [[Paper](https://arxiv.org/abs/2207.08569)]
* **MAFormer**: "MAFormer: A Transformer Network with Multi-scale Attention Fusion for Visual Recognition", arXiv, 2022 (*Baidu*). [[Paper](https://arxiv.org/abs/2209.01620)]
* **AEWin**: "Axially Expanded Windows for Local-Global Interaction in Vision Transformers", arXiv, 2022 (*Southwest Jiaotong University*). [[Paper](https://arxiv.org/abs/2209.08726)]
* **GrafT**: "Grafting Vision Transformers", arXiv, 2022 (*Stony Brook*). [[Paper](https://arxiv.org/abs/2210.15943)]
* **?**: "Rethinking Hierarchicies in Pre-trained Plain Vision Transformer", arXiv, 2022 (*The University of Sydney*). [[Paper](https://arxiv.org/abs/2211.01785)]
* **LTH-ViT**: "The Lottery Ticket Hypothesis for Vision Transformers", arXiv, 2022 (*Northeastern University, China*). [[Paper](https://arxiv.org/abs/2211.01484)]
* **TT**: "Token Transformer: Can class token help window-based transformer build better long-range interactions?", arXiv, 2022 (*Hangzhou Dianzi University*). [[Paper](https://arxiv.org/abs/2211.06083)]
* **INTERN**: "INTERN: A New Learning Paradigm Towards General Vision", arXiv, 2022 (*Shanghai AI Lab*). [[Paper](https://arxiv.org/abs/2111.08687)][[Website](https://opengvlab.shlab.org.cn/)]
* **GGeM**: "Group Generalized Mean Pooling for Vision Transformer", arXiv, 2022 (*NAVER*). [[Paper](https://arxiv.org/abs/2212.04114)]
* **GPViT**: "GPViT: A High Resolution Non-Hierarchical Vision Transformer with Group Propagation", ICLR, 2023 (*University of Edinburgh, Scotland + UCSD*). [[Paper](https://arxiv.org/abs/2212.06795)][[PyTorch](https://github.com/ChenhongyiYang/GPViT)]
* **CPVT**: "Conditional Positional Encodings for Vision Transformers", ICLR, 2023 (*Meituan*). [[Paper](https://openreview.net/forum?id=3KWnuT-R1bh)][[Code (in construction)](https://github.com/Meituan-AutoML/CPVT)]
* **LipsFormer**: "LipsFormer: Introducing Lipschitz Continuity to Vision Transformers", ICLR, 2023 (*IDEA, China*). [[Paper](https://arxiv.org/abs/2304.09856)][[Code (in construction)](https://github.com/IDEA-Research/LipsFormer)]
* **BiFormer**: "BiFormer: Vision Transformer with Bi-Level Routing Attention", CVPR, 2023 (*CUHK*). [[Paper](https://arxiv.org/abs/2303.08810)][[PyTorch](https://github.com/rayleizhu/BiFormer)]
* **AbSViT**: "Top-Down Visual Attention from Analysis by Synthesis", CVPR, 2023 (*Berkeley*). [[Paper](https://arxiv.org/abs/2303.13043)][[PyTorch](https://github.com/bfshi/AbSViT)][[Website](https://sites.google.com/view/absvit)]
* **DependencyViT**: "Visual Dependency Transformers: Dependency Tree Emerges From Reversed Attention", CVPR, 2023 (*MIT*). [[Paper](https://arxiv.org/abs/2304.03282)][[Code (in construction)](https://github.com/dingmyu/DependencyViT)]
* **ResFormer**: "ResFormer: Scaling ViTs with Multi-Resolution Training", CVPR, 2023 (*Fudan*). [[Paper](https://arxiv.org/abs/2212.00776)][[PyTorch (in construction)](https://github.com/ruitian12/resformer)]
* **SViT**: "Vision Transformer with Super Token Sampling", CVPR, 2023 (*CAS*). [[Paper](https://arxiv.org/abs/2211.11167)]
* **PaCa-ViT**: "PaCa-ViT: Learning Patch-to-Cluster Attention in Vision Transformers", CVPR, 2023 (*NC State*). [[Paper](https://arxiv.org/abs/2203.11987)][[PyTorch](https://github.com/iVMCL/PaCaViT)]
* **GC-ViT**: "Global Context Vision Transformers", ICML, 2023 (*NVIDIA*). [[Paper](https://arxiv.org/abs/2206.09959)][[PyTorch](https://github.com/NVlabs/GCViT)]
* **MAGNETO**: "MAGNETO: A Foundation Transformer", ICML, 2023 (*Microsoft*). [[Paper](https://arxiv.org/abs/2210.06423)]
* **Fcaformer**: "Fcaformer: Forward Cross Attention in Hybrid Vision Transformer", ICCV, 2023 (*Intellifusion, China*). [[Paper](https://arxiv.org/abs/2211.07198)][[PyTorch](https://github.com/hkzhang91/CabViT)]
* **SMT**: "Scale-Aware Modulation Meet Transformer", ICCV, 2023 (*Alibaba*). [[Paper](https://arxiv.org/abs/2307.08579)][[PyTorch](https://github.com/AFeng-x/SMT)]
* **FLatten-Transformer**: "FLatten Transformer: Vision Transformer using Focused Linear Attention", ICCV, 2023 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2308.00442)][[PyTorch](https://github.com/LeapLabTHU/FLatten-Transformer)]
* **Path-Ensemble**: "Revisiting Vision Transformer from the View of Path Ensemble", ICCV, 2023 (*Alibaba*). [[Paper](https://arxiv.org/abs/2308.06548)]
* **SG-Former**: "SG-Former: Self-guided Transformer with Evolving Token Reallocation", ICCV, 2023 (*NUS*). [[Paper](https://arxiv.org/abs/2308.12216)][[PyTorch](https://github.com/OliverRensu/SG-Former)]
* **SimPool**: "Keep It SimPool: Who Said Supervised Transformers Suffer from Attention Deficit?", ICCV, 2023 (*National Technical University of Athens*). [[Paper](https://arxiv.org/abs/2309.06891)]
* **LaPE**: "LaPE: Layer-adaptive Position Embedding for Vision Transformers with Independent Layer Normalization", ICCV, 2023 (*Peking*). [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Yu_LaPE_Layer-adaptive_Position_Embedding_for_Vision_Transformers_with_Independent_Layer_ICCV_2023_paper.html)][[PyTorch](https://github.com/Ingrid725/LaPE)]
* **CB**: "Scratching Visual Transformer's Back with Uniform Attention", ICCV, 2023 (*NAVER*). [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Hyeon-Woo_Scratching_Visual_Transformers_Back_with_Uniform_Attention_ICCV_2023_paper.html)]
* **STL**: "Fully Attentional Networks with Self-emerging Token Labeling", ICCV, 2023 (*NVIDIA*). [[Paper](https://arxiv.org/abs/2401.03844)][[PyTorch](https://github.com/NVlabs/STL)]
* **ClusterFormer**: "ClusterFormer: Clustering As A Universal Visual Learner", NeurIPS, 2023 (*Rochester Institute of Technology (RIT)*). [[Paper](https://arxiv.org/abs/2309.13196)]
* **SVT**: "Scattering Vision Transformer: Spectral Mixing Matters", NeurIPS, 2023 (*Microsoft*). [[Paper](https://arxiv.org/abs/2311.01310)][[PyTorch](https://github.com/badripatro/svt)][[Website](https://badripatro.github.io/svt/)]
* **CrossFormer++**: "CrossFormer++: A Versatile Vision Transformer Hinging on Cross-scale Attention", arXiv, 2023 (*Zhejiang University*). [[Paper](https://arxiv.org/abs/2303.06908)][[PyTorch](https://github.com/cheerss/CrossFormer)]
* **QFormer**: "Vision Transformer with Quadrangle Attention", arXiv, 2023 (*The University of Sydney*). [[Paper](https://arxiv.org/abs/2303.15105)][[Code (in construction)](https://github.com/ViTAE-Transformer/QFormer)]
* **ViT-Calibrator**: "ViT-Calibrator: Decision Stream Calibration for Vision Transformer", arXiv, 2023 (*Zhejiang University*). [[Paper](https://arxiv.org/abs/2304.04354)]
* **SpectFormer**: "SpectFormer: Frequency and Attention is what you need in a Vision Transformer", arXiv, 2023 (*Microsoft*). [[Paper](https://arxiv.org/abs/2304.06446)][[PyTorch](https://github.com/badripatro/SpectFormers)][[Website](https://badripatro.github.io/SpectFormers/)]
* **UniNeXt**: "UniNeXt: Exploring A Unified Architecture for Vision Recognition", arXiv, 2023 (*Alibaba*). [[Paper](https://arxiv.org/abs/2304.13700)]
* **CageViT**: "CageViT: Convolutional Activation Guided Efficient Vision Transformer", arXiv, 2023 (*Southern University of Science and Technology*). [[Paper](https://arxiv.org/abs/2305.09924)]
* **?**: "Making Vision Transformers Truly Shift-Equivariant", arXiv, 2023 (*UIUC*). [[Paper](https://arxiv.org/abs/2305.16316)]
* **2-D-SSM**: "2-D SSM: A General Spatial Layer for Visual Transformers", arXiv, 2023 (*Tel Aviv*). [[Paper](https://arxiv.org/abs/2306.06635)][[PyTorch](https://github.com/ethanbar11/ssm_2d)]
* **NaViT**: "Patch n' Pack: NaViT, a Vision Transformer for any Aspect Ratio and Resolution", NeurIPS, 2023 (*DeepMind*). [[Paper](https://arxiv.org/abs/2307.06304)]
* **DAT++**: "DAT++: Spatially Dynamic Vision Transformer with Deformable Attention", arXiv, 2023 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2309.01430)][[PyTorch](https://github.com/LeapLabTHU/DAT)]
* **?**: "Replacing softmax with ReLU in Vision Transformers", arXiv, 2023 (*DeepMind*). [[Paper](https://arxiv.org/abs/2309.08586)]
* **RMT**: "RMT: Retentive Networks Meet Vision Transformers", arXiv, 2023 (*CAS*). [[Paper](https://arxiv.org/abs/2309.11523)]
* **reg**: "Vision Transformers Need Registers", arXiv, 2023 (*Meta*). [[Paper](https://arxiv.org/abs/2309.16588)]
* **ChannelViT**: "Channel Vision Transformers: An Image Is Worth C x 16 x 16 Words", arXiv, 2023 (*Insitro, CA*). [[Paper](https://arxiv.org/abs/2309.16108)]
* **EViT**: "EViT: An Eagle Vision Transformer with Bi-Fovea Self-Attention", arXiv, 2023 (*Nankai University*). [[Paper](https://arxiv.org/abs/2310.06629)]
* **ViR**: "ViR: Vision Retention Networks", arXiv, 2023 (*NVIDIA*). [[Paper](https://arxiv.org/abs/2310.19731)]
* **abs-win**: "Window Attention is Bugged: How not to Interpolate Position Embeddings", arXiv, 2023 (*Meta*). [[Paper](https://arxiv.org/abs/2311.05613)]
* **FMViT**: "FMViT: A multiple-frequency mixing Vision Transformer", arXiv, 2023 (*Alibaba*). [[Paper](https://arxiv.org/abs/2311.05707)][[Code (in construction)](https://github.com/tany0699/FMViT)]
* **GroupMixFormer**: "Advancing Vision Transformers with Group-Mix Attention", arXiv, 2023 (*HKU*). [[Paper](https://arxiv.org/abs/2311.15157)][[PyTorch](https://github.com/AILab-CVC/GroupMixFormer)]
* **PGT**: "Perceptual Group Tokenizer: Building Perception with Iterative Grouping", arXiv, 2023 (*DeepMind*). [[Paper](https://arxiv.org/abs/2311.18296)]
* **SCHEME**: "SCHEME: Scalable Channer Mixer for Vision Transformers", arXiv, 2023 (*UCSD*). [[Paper](https://arxiv.org/abs/2312.00412)]
* **Agent-Attention**: "Agent Attention: On the Integration of Softmax and Linear Attention", arXiv, 2023 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2312.08874)][[PyTorch](https://github.com/LeapLabTHU/Agent-Attention)]
* **ViTamin**: "ViTamin: Designing Scalable Vision Models in the Vision-Language Era", CVPR, 2024 (*ByteDance*). [[Paper](https://arxiv.org/abs/2404.02132)][[PyTorch](https://github.com/Beckschen/ViTamin)]
* **HIRI-ViT**: "HIRI-ViT: Scaling Vision Transformer with High Resolution Inputs", TPAMI, 2024 (*HiDream.ai, China*). [[Paper](https://arxiv.org/abs/2403.11999)]
* **SPFormer**: "SPFormer: Enhancing Vision Transformer with Superpixel Representation", arXiv, 2024 (*JHU*). [[Paper](https://arxiv.org/abs/2401.02931)]
* **manifold-K**: "A Manifold Representation of the Key in Vision Transformers", arXiv, 2024 (*University of Oslo, Norway*). [[Paper](https://arxiv.org/abs/2402.00534)]
* **BiXT**: "Perceiving Longer Sequences With Bi-Directional Cross-Attention Transformers", arXiv, 2024 (*University of Melbourne*). [[Paper](https://arxiv.org/abs/2402.12138)]
* **VisionLLaMA**: "VisionLLaMA: A Unified LLaMA Interface for Vision Tasks", arXiv, 2024 (*Meituan*). [[Paper](https://arxiv.org/abs/2403.00522)][[Code (in construction)](https://github.com/Meituan-AutoML/VisionLLaMA)]
* **xT**: "xT: Nested Tokenization for Larger Context in Large Images", arXiv, 2024 (*Berkeley*). [[Paper](https://arxiv.org/abs/2403.01915)]
* **ACC-ViT**: "ACC-ViT: Atrous Convolution's Comeback in Vision Transformers", arXiv, 2024 (*Purdue*). [[Paper](https://arxiv.org/abs/2403.04200)]
* **ViTAR**: "ViTAR: Vision Transformer with Any Resolution", arXiv, 2024 (*CAS*). [[Paper](https://arxiv.org/abs/2403.18361)]
* **iLLaMA**: "Adapting LLaMA Decoder to Vision Transformer", arXiv, 2024 (*Shanghai AI Lab*). [[Paper](https://arxiv.org/abs/2404.06773)]
#### Efficient Vision Transformer
* **DeiT**: "Training data-efficient image transformers & distillation through attention", ICML, 2021 (*Facebook*). [[Paper](https://arxiv.org/abs/2012.12877)][[PyTorch](https://github.com/facebookresearch/deit)]
* **ConViT**: "ConViT: Improving Vision Transformers with Soft Convolutional Inductive Biases", ICML, 2021 (*Facebook*). [[Paper](https://arxiv.org/abs/2103.10697)][[Code](https://github.com/facebookresearch/convit)]
* **?**: "Improving the Efficiency of Transformers for Resource-Constrained Devices", DSD, 2021 (*NavInfo Europe, Netherlands*). [[Paper](https://arxiv.org/abs/2106.16006)]
* **PS-ViT**: "Vision Transformer with Progressive Sampling", ICCV, 2021 (*CPII*). [[Paper](https://arxiv.org/abs/2108.01684)]
* **HVT**: "Scalable Visual Transformers with Hierarchical Pooling", ICCV, 2021 (*Monash University*). [[Paper](https://arxiv.org/abs/2103.10619)][[PyTorch](https://github.com/MonashAI/HVT)]
* **CrossViT**: "CrossViT: Cross-Attention Multi-Scale Vision Transformer for Image Classification", ICCV, 2021 (*MIT-IBM*). [[Paper](https://arxiv.org/abs/2103.14899)][[PyTorch](https://github.com/IBM/CrossViT)]
* **ViL**: "Multi-Scale Vision Longformer: A New Vision Transformer for High-Resolution Image Encoding", ICCV, 2021 (*Microsoft*). [[Paper](https://arxiv.org/abs/2103.15358)][[PyTorch](https://github.com/microsoft/vision-longformer)]
* **Visformer**: "Visformer: The Vision-friendly Transformer", ICCV, 2021 (*Beihang University*). [[Paper](https://arxiv.org/abs/2104.12533)][[PyTorch](https://github.com/danczs/Visformer)]
* **MultiExitViT**: "Multi-Exit Vision Transformer for Dynamic Inference", BMVC, 2021 (*Aarhus University, Denmark*). [[Paper](https://arxiv.org/abs/2106.15183)][[Tensorflow](https://gitlab.au.dk/maleci/multiexitvit)]
* **SViTE**: "Chasing Sparsity in Vision Transformers: An End-to-End Exploration", NeurIPS, 2021 (*UT Austin*). [[Paper](https://arxiv.org/abs/2106.04533)][[PyTorch](https://github.com/VITA-Group/SViTE)]
* **DGE**: "Dynamic Grained Encoder for Vision Transformers", NeurIPS, 2021 (*Megvii*). [[Paper](https://papers.nips.cc/paper/2021/hash/2d969e2cee8cfa07ce7ca0bb13c7a36d-Abstract.html)][[PyTorch](https://github.com/StevenGrove/vtpack)]
* **GG-Transformer**: "Glance-and-Gaze Vision Transformer", NeurIPS, 2021 (*JHU*). [[Paper](https://arxiv.org/abs/2106.02277)][[Code (in construction)](https://github.com/yucornetto/GG-Transformer)]
* **DynamicViT**: "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification", NeurIPS, 2021 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2106.02034)][[PyTorch](https://github.com/raoyongming/DynamicViT)][[Website](https://dynamicvit.ivg-research.xyz/)]
* **ResT**: "ResT: An Efficient Transformer for Visual Recognition", NeurIPS, 2021 (*Nanjing University*). [[Paper](https://arxiv.org/abs/2105.13677)][[PyTorch](https://github.com/wofmanaf/ResT)]
* **Adder-Transformer**: "Adder Attention for Vision Transformer", NeurIPS, 2021 (*Huawei*). [[Paper](https://proceedings.neurips.cc/paper/2021/hash/a57e8915461b83adefb011530b711704-Abstract.html)]
* **SOFT**: "SOFT: Softmax-free Transformer with Linear Complexity", NeurIPS, 2021 (*Fudan*). [[Paper](https://arxiv.org/abs/2110.11945)][[PyTorch](https://github.com/fudan-zvg/SOFT)][[Website](https://fudan-zvg.github.io/SOFT/)]
* **IA-RED<sup>2</sup>**: "IA-RED<sup>2</sup>: Interpretability-Aware Redundancy Reduction for Vision Transformers", NeurIPS, 2021 (*MIT-IBM*). [[Paper](https://arxiv.org/abs/2106.12620)][[Website](http://people.csail.mit.edu/bpan/ia-red/)]
* **LocalViT**: "LocalViT: Bringing Locality to Vision Transformers", arXiv, 2021 (*ETHZ*). [[Paper](https://arxiv.org/abs/2104.05707)][[PyTorch](https://github.com/ofsoundof/LocalViT)]
* **CCT**: "Escaping the Big Data Paradigm with Compact Transformers", arXiv, 2021 (*University of Oregon*). [[Paper](https://arxiv.org/abs/2104.05704)][[PyTorch](https://github.com/SHI-Labs/Compact-Transformers)]
* **DiversePatch**: "Vision Transformers with Patch Diversification", arXiv, 2021 (*UT Austin + Facebook*). [[Paper](https://arxiv.org/abs/2104.12753)][[PyTorch](https://github.com/ChengyueGongR/PatchVisionTransformer)] 
* **SL-ViT**: "Single-Layer Vision Transformers for More Accurate Early Exits with Less Overhead", arXiv, 2021 (*Aarhus University*). [[Paper](https://arxiv.org/abs/2105.09121)]
* **?**: "Multi-Exit Vision Transformer for Dynamic Inference", arXiv, 2021 (*Aarhus University, Denmark*). [[Paper](https://arxiv.org/abs/2106.15183)]
* **ViX**: "Vision Xformers: Efficient Attention for Image Classification", arXiv, 2021 (*Indian Institute of Technology Bombay*). [[Paper](https://arxiv.org/abs/2107.02239)]
* **Transformer-LS**: "Long-Short Transformer: Efficient Transformers for Language and Vision", NeurIPS, 2021 (*NVIDIA*). [[Paper](https://arxiv.org/abs/2107.02192)][[PyTorch](https://github.com/NVIDIA/transformer-ls)]
* **WideNet**: "Go Wider Instead of Deeper", arXiv, 2021 (*NUS*). [[Paper](https://arxiv.org/abs/2107.11817)]
* **Armour**: "Armour: Generalizable Compact Self-Attention for Vision Transformers", arXiv, 2021 (*Arm*). [[Paper](https://arxiv.org/abs/2108.01778)]
* **IPE**: "Exploring and Improving Mobile Level Vision Transformers", arXiv, 2021 (*CUHK*). [[Paper](https://arxiv.org/abs/2108.13015)]
* **DS-Net++**: "DS-Net++: Dynamic Weight Slicing for Efficient Inference in CNNs and Transformers", arXiv, 2021 (*Monash University*). [[Paper](https://arxiv.org/abs/2109.10060)][[PyTorch](https://github.com/changlin31/DS-Net)]
* **UFO-ViT**: "UFO-ViT: High Performance Linear Vision Transformer without Softmax", arXiv, 2021 (*Kakao*). [[Paper](https://arxiv.org/abs/2109.14382)]
* **Evo-ViT**: "Evo-ViT: Slow-Fast Token Evolution for Dynamic Vision Transformer", AAAI, 2022 (*Tencent*). [[Paper](https://arxiv.org/abs/2108.01390)][[PyTorch](https://github.com/YifanXu74/Evo-ViT)]
* **PS-Attention**: "Pale Transformer: A General Vision Transformer Backbone with Pale-Shaped Attention", AAAI, 2022 (*Baidu*). [[Paper](https://arxiv.org/abs/2112.14000)][[Paddle](https://github.com/BR-IDL/PaddleViT)]
* **ShiftViT**: "When Shift Operation Meets Vision Transformer: An Extremely Simple Alternative to Attention Mechanism", AAAI, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2201.10801)][[PyTorch](https://github.com/microsoft/SPACH)]
* **EViT**: "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations", ICLR, 2022 (*Tencent*). [[Paper](https://arxiv.org/abs/2202.07800)][[PyTorch](https://github.com/youweiliang/evit)]
* **QuadTree**: "QuadTree Attention for Vision Transformers", ICLR, 2022 (*Simon Fraser + Alibaba*). [[Paper](https://arxiv.org/abs/2201.02767)][[PyTorch](https://github.com/Tangshitao/QuadtreeAttention)]
* **Anti-Oversmoothing**: "Anti-Oversmoothing in Deep Vision Transformers via the Fourier Domain Analysis: From Theory to Practice", ICLR, 2022 (*UT Austin*). [[Paper](https://arxiv.org/abs/2203.05962)][[PyTorch](https://github.com/VITA-Group/ViT-Anti-Oversmoothing)]
* **QnA**: "Learned Queries for Efficient Local Attention", CVPR, 2022 (*Tel-Aviv*). [[Paper](https://arxiv.org/abs/2112.11435)][[JAX](https://github.com/moabarar/qna)]
* **LVT**: "Lite Vision Transformer with Enhanced Self-Attention", CVPR, 2022 (*Adobe*). [[Paper](https://arxiv.org/abs/2112.10809)][[PyTorch](https://github.com/Chenglin-Yang/LVT)]
* **A-ViT**: "A-ViT: Adaptive Tokens for Efficient Vision Transformer", CVPR, 2022 (*NVIDIA*). [[Paper](https://arxiv.org/abs/2112.07658)][[Website](https://a-vit.github.io/)]
* **PS-ViT**: "Patch Slimming for Efficient Vision Transformers", CVPR, 2022 (*Huawei*). [[Paper](https://arxiv.org/abs/2106.02852)]
* **Rev-MViT**: "Reversible Vision Transformers", CVPR, 2022 (*Meta*). [[Paper](https://arxiv.org/abs/2302.04869)][[PyTorch-1](https://github.com/karttikeya/minREV)][[PyTorch-2](https://github.com/facebookresearch/slowfast)]
* **AdaViT**: "AdaViT: Adaptive Vision Transformers for Efficient Image Recognition", CVPR, 2022 (*Fudan*). [[Paper](https://arxiv.org/abs/2111.15668)]
* **DQS**: "Dynamic Query Selection for Fast Visual Perceiver", CVPRW, 2022 (*Sorbonne Universite', France*). [[Paper](https://arxiv.org/abs/2205.10873)]
* **ATS**: "Adaptive Token Sampling For Efficient Vision Transformers", ECCV, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2111.15667)][[Website](https://adaptivetokensampling.github.io/)]
* **EdgeViT**: "EdgeViTs: Competing Light-weight CNNs on Mobile Devices with Vision Transformers", ECCV, 2022 (*Samsung*). [[Paper](https://arxiv.org/abs/2205.03436)][[PyTorch](https://github.com/saic-fi/edgevit)]
* **SReT**: "Sliced Recursive Transformer", ECCV, 2022 (*CMU + MBZUAI*). [[Paper](https://arxiv.org/abs/2111.05297)][[PyTorch](https://github.com/szq0214/SReT)]
* **SiT**: "Self-slimmed Vision Transformer", ECCV, 2022 (*SenseTime*). [[Paper](https://arxiv.org/abs/2111.12624)][[PyTorch](https://github.com/Sense-X/SiT)]
* **DFvT**: "Doubly-Fused ViT: Fuse Information from Vision Transformer Doubly with Local Representation", ECCV, 2022 (*Alibaba*). [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/322_ECCV_2022_paper.php)]
* **M<sup>3</sup>ViT**: "M<sup>3</sup>ViT: Mixture-of-Experts Vision Transformer for Efficient Multi-task Learning with Model-Accelerator Co-design", NeurIPS, 2022 (*UT Austin*). [[Paper](https://arxiv.org/abs/2210.14793)][[PyTorch](https://github.com/VITA-Group/M3ViT)]
* **ResT-V2**: "ResT V2: Simpler, Faster and Stronger", NeurIPS, 2022 (*Nanjing University*). [[Paper](https://arxiv.org/abs/2204.07366)][[PyTorch](https://github.com/wofmanaf/ResT)]
* **DeiT-Manifold**: "Learning Efficient Vision Transformers via Fine-Grained Manifold Distillation", NeurIPS, 2022 (*Huawei*). [[Paper](https://arxiv.org/abs/2107.01378)]
* **EfficientFormer**: "EfficientFormer: Vision Transformers at MobileNet Speed", NeurIPS, 2022 (*Snap*). [[Paper](https://arxiv.org/abs/2206.01191)][[PyTorch](https://github.com/snap-research/EfficientFormer)]
* **GhostNetV2**: "GhostNetV2: Enhance Cheap Operation with Long-Range Attention", NeurIPS, 2022 (*Huawei*). [[Paper](https://arxiv.org/abs/2211.12905)][[PyTorch](https://github.com/huawei-noah/Efficient-AI-Backbones/tree/master/ghostnetv2_pytorch)]
* **?**: "Training a Vision Transformer from scratch in less than 24 hours with 1 GPU", NeurIPSW, 2022 (*Borealis AI, Canada*). [[Paper](https://arxiv.org/abs/2211.05187)]
* **TerViT**: "TerViT: An Efficient Ternary Vision Transformer", arXiv, 2022 (*Beihang University*). [[Paper](https://arxiv.org/abs/2201.08050)]
* **MT-ViT**: "Multi-Tailed Vision Transformer for Efficient Inference", arXiv, 2022 (*Wuhan University*). [[Paper](https://arxiv.org/abs/2203.01587)]
* **ViT-P**: "ViT-P: Rethinking Data-efficient Vision Transformers from Locality", arXiv, 2022 (*Chongqing University of Technology*). [[Paper](https://arxiv.org/abs/2203.02358)]
* **CF-ViT**: "Coarse-to-Fine Vision Transformer", arXiv, 2022 (*Xiamen University + Tencent*). [[Paper](https://arxiv.org/abs/2203.03821)][[PyTorch](https://github.com/ChenMnZ/CF-ViT)]
* **EIT**: "EIT: Efficiently Lead Inductive Biases to ViT", arXiv, 2022 (*Academy of Military Sciences, China*). [[Paper](https://arxiv.org/abs/2203.07116)]
* **SepViT**: "SepViT: Separable Vision Transformer", arXiv, 2022 (*University of Electronic Science and Technology of China*). [[Paper](https://arxiv.org/abs/2203.15380)]
* **TRT-ViT**: "TRT-ViT: TensorRT-oriented Vision Transformer", arXiv, 2022 (*ByteDance*). [[Paper](https://arxiv.org/abs/2205.09579)]
* **SuperViT**: "Super Vision Transformer", arXiv, 2022 (*Xiamen University*). [[Paper](https://arxiv.org/abs/2205.11397)][[PyTorch](https://github.com/lmbxmu/SuperViT)]
* **Tutel**: "Tutel: Adaptive Mixture-of-Experts at Scale", arXiv, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2206.03382)][[PyTorch](https://github.com/microsoft/tutel)]
* **SimA**: "SimA: Simple Softmax-free Attention for Vision Transformers", arXiv, 2022 (*Maryland + UC Davis*). [[Paper](https://arxiv.org/abs/2206.08898)][[PyTorch](https://github.com/UCDvision/sima)]
* **EdgeNeXt**: "EdgeNeXt: Efficiently Amalgamated CNN-Transformer Architecture for Mobile Vision Applications", arXiv, 2022 (*MBZUAI*). [[Paper](https://arxiv.org/abs/2206.10589)][[PyTorch](https://github.com/mmaaz60/EdgeNeXt)]
* **VVT**: "Vicinity Vision Transformer", arXiv, 2022 (*Australian National University*). [[Paper](https://arxiv.org/abs/2206.10552)][[Code (in construction)](https://github.com/OpenNLPLab/Vicinity-Vision-Transformer)]
* **SOFT**: "Softmax-free Linear Transformers", arXiv, 2022 (*Fudan*). [[Paper](https://arxiv.org/abs/2207.03341)][[PyTorch](https://github.com/fudan-zvg/SOFT)]
* **MaiT**: "MaiT: Leverage Attention Masks for More Efficient Image Transformers", arXiv, 2022 (*Samsung*). [[Paper](https://arxiv.org/abs/2207.03006)]
* **LightViT**: "LightViT: Towards Light-Weight Convolution-Free Vision Transformers", arXiv, 2022 (*SenseTime*). [[Paper](https://arxiv.org/abs/2207.05557)][[Code (in construction)](https://github.com/hunto/LightViT)]
* **Next-ViT**: "Next-ViT: Next Generation Vision Transformer for Efficient Deployment in Realistic Industrial Scenarios", arXiv, 2022 (*ByteDance*). [[Paper](https://arxiv.org/abs/2207.05501)]
* **XFormer**: "Lightweight Vision Transformer with Cross Feature Attention", arXiv, 2022 (*Samsung*). [[Paper](https://arxiv.org/pdf/2207.07268.pdf)]
* **PatchDropout**: "PatchDropout: Economizing Vision Transformers Using Patch Dropout", arXiv, 2022 (*KTH, Sweden*). [[Paper](https://arxiv.org/abs/2208.07220)]
* **ClusTR**: "ClusTR: Exploring Efficient Self-attention via Clustering for Vision Transformers", arXiv, 2022 (*The University of Adelaide, Australia*). [[Paper](https://arxiv.org/abs/2208.13138)]
* **DiNAT**: "Dilated Neighborhood Attention Transformer", arXiv, 2022 (*University of Oregon*). [[Paper](https://arxiv.org/abs/2209.15001)][[PyTorch](https://github.com/SHI-Labs/Neighborhood-Attention-Transformer)]
* **MobileViTv3**: "MobileViTv3: Mobile-Friendly Vision Transformer with Simple and Effective Fusion of Local, Global and Input Features", arXiv, 2022 (*Micron*). [[Paper](https://arxiv.org/abs/2209.15159)][[PyTorch](https://github.com/micronDLA/MobileViTv3)]
* **ViT-LSLA**: "ViT-LSLA: Vision Transformer with Light Self-Limited-Attention", arXiv, 2022 (*Southwest University*). [[Paper](https://arxiv.org/abs/2210.17115)]
* **Token-Pooling**: "Token Pooling in Vision Transformers for Image Classification", WACV, 2023 (*Apple*). [[Paper](https://openaccess.thecvf.com/content/WACV2023/html/Marin_Token_Pooling_in_Vision_Transformers_for_Image_Classification_WACV_2023_paper.html)]
* **Tri-Level**: "Peeling the Onion: Hierarchical Reduction of Data Redundancy for Efficient Vision Transformer Training", AAAI, 2023 (*Northeastern University*). [[Paper](https://arxiv.org/abs/2211.10801)][[Code (in construction)](https://github.com/ZLKong/Tri-Level-ViT)]
* **ViTCoD**: "ViTCoD: Vision Transformer Acceleration via Dedicated Algorithm and Accelerator Co-Design", IEEE International Symposium on High-Performance Computer Architecture (HPCA), 2023 (*Georgia Tech*). [[Paper](https://arxiv.org/abs/2210.09573)]
* **ViTALiTy**: "ViTALiTy: Unifying Low-rank and Sparse Approximation for Vision Transformer Acceleration with a Linear Taylor Attention", IEEE International Symposium on High-Performance Computer Architecture (HPCA), 2023 (*Rice University*). [[Paper](https://arxiv.org/abs/2211.05109)]
* **HeatViT**: "HeatViT: Hardware-Efficient Adaptive Token Pruning for Vision Transformers", IEEE International Symposium on High-Performance Computer Architecture (HPCA), 2023 (*Northeastern University*). [[Paper](https://arxiv.org/abs/2211.08110)]
* **ToMe**: "Token Merging: Your ViT But Faster", ICLR, 2023 (*Meta*). [[Paper](https://arxiv.org/abs/2210.09461)][[PyTorch](https://github.com/facebookresearch/ToMe)]
* **HiViT**: "HiViT: A Simpler and More Efficient Design of Hierarchical Vision Transformer", ICLR, 2023 (*CAS*). [[Paper](https://arxiv.org/abs/2205.14949)][[PyTorch](https://github.com/zhangxiaosong18/hivit)]
* **STViT**: "Making Vision Transformers Efficient from A Token Sparsification View", CVPR, 2023 (*Alibaba*). [[Paper](https://arxiv.org/abs/2303.08685)][[PyTorch](https://github.com/changsn/STViT-R)]
* **SparseViT**: "SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer", CVPR, 2023 (*MIT*). [[Paper](https://arxiv.org/abs/2303.17605)][[Website](https://sparsevit.mit.edu/)]
* **Slide-Transformer**: "Slide-Transformer: Hierarchical Vision Transformer with Local Self-Attention", CVPR, 2023 (*Tsinghua University*). [[Paper](https://arxiv.org/abs/2304.04237)][[Code (in construction)](https://github.com/LeapLabTHU/Slide-Transformer)]
* **RIFormer**: "RIFormer: Keep Your Vision Backbone Effective While Removing Token Mixer", CVPR, 2023 (*Shanghai AI Lab*). [[Paper](https://arxiv.org/abs/2304.05659)][[PyTorch](https://github.com/open-mmlab/mmpretrain/tree/main/configs/riformer)][[Website](https://techmonsterwang.github.io/RIFormer/)]
* **EfficientViT**: "EfficientViT: Memory Efficient Vision Transformer with Cascaded Group Attention", CVPR, 2023 (*Microsoft*). [[Paper](https://arxiv.org/abs/2305.07027)][[PyTorch](https://github.com/microsoft/Cream/tree/main/EfficientViT)]
* **Castling-ViT**: "Castling-ViT: Compressing Self-Attention via Switching Towards Linear-Angular Attention During Vision Transformer Inference", CVPR, 2023 (*Meta*). [[Paper](https://arxiv.org/abs/2211.10526)]
* **ViT-Ti**: "RGB no more: Minimally-decoded JPEG Vision Transformers", CVPR, 2023 (*UMich*). [[Paper](https://arxiv.org/abs/2211.16421)]
* **Sparsifiner**: "Sparsifiner: Learning Sparse Instance-Dependent Attention for Efficient Vision Transformers", CVPR, 2023 (*University of Toronto*). [[Paper](https://arxiv.org/abs/2303.13755)]
* **?**: "Beyond Attentive Tokens: Incorporating Token Importance and Diversity for Efficient Vision Transformers", CVPR, 2023 (*Baidu*). [[Paper](https://arxiv.org/abs/2211.11315)]
* **LTMP**: "Learned Thresholds Token Merging and Pruning for Vision Transformers", ICMLW, 2023 (*Ghent University, Belgium*). [[Paper](https://arxiv.org/abs/2307.10780)][[PyTorch](https://github.com/Mxbonn/ltmp)][[Website](https://maxim.bonnaerens.com/publication/ltmp/)]
* **ReViT**: "Make A Long Image Short: Adaptive Token Length for Vision Transformers", ECML PKDD, 2023 (*Midea Grou, China*). [[Paper](https://arxiv.org/abs/2307.02092)]
* **EfficientViT**: "EfficientViT: Enhanced Linear Attention for High-Resolution Low-Computation Visual Recognition", ICCV, 2023 (*MIT*). [[Paper](https://arxiv.org/abs/2205.14756)][[PyTorch](https://github.com/mit-han-lab/efficientvit)]
* **MPCViT**: "MPCViT: Searching for Accurate and Efficient MPC-Friendly Vision Transformer with Heterogeneous Attention", ICCV, 2023 (*Peking*). [[Paper](https://arxiv.org/abs/2211.13955)][[PyTorch](https://github.com/PKU-SEC-Lab/mpcvit)]
* **MST**: "Masked Spiking Transformer", ICCV, 2023 (*HKUST*). [[Paper](https://arxiv.org/abs/2210.01208)]
* **EfficientFormerV2**: "Rethinking Vision Transformers for MobileNet Size and Speed", ICCV, 2023 (*Snap*). [[Paper](https://arxiv.org/abs/2212.08059)][[PyTorch](https://github.com/snap-research/EfficientFormer)]
* **DiffRate**: "DiffRate: Differentiable Compression Rate for Efficient Vision Transformers", ICCV, 2023 (*Shanghai AI Lab*). [[Paper](https://arxiv.org/abs/2305.17997)][[PyTorch](https://github.com/OpenGVLab/DiffRate)]
* **ElasticViT**: "ElasticViT: Conflict-aware Supernet Training for Deploying Fast Vision Transformer on Diverse Mobile Devices", ICCV, 2023 (*Microsoft*). [[Paper](https://arxiv.org/abs/2303.09730)]
* **FastViT**: "FastViT: A Fast Hybrid Vision Transformer using Structural Reparameterization", ICCV, 2023 (*Apple*). [[Paper](https://arxiv.org/abs/2303.14189)][[PyTorch](https://github.com/apple/ml-fastvit)]
* **SeiT**: "SeiT: Storage-Efficient Vision Training with Tokens Using 1% of Pixel Storage", ICCV, 2023 (*NAVER*). [[Paper](https://arxiv.org/abs/2303.11114)][[PyTorch](https://github.com/naver-ai/seit)]
* **TokenReduction**: "Which Tokens to Use? Investigating Token Reduction in Vision Transformers", ICCVW, 2023 (*Aalborg University, Denmark*). [[Paper](https://arxiv.org/abs/2308.04657)][[PyTorch](https://github.com/JoakimHaurum/TokenReduction)][[Website](https://vap.aau.dk/tokens/)]
* **LGViT**: "LGViT: Dynamic Early Exiting for Accelerating Vision Transformer", ACMMM, 2023 (*Beijing Institute of Technology*). [[Paper](https://arxiv.org/abs/2308.00255)]
* **LBP-WHT**: "Efficient Low-rank Backpropagation for Vision Transformer Adaptation", NeurIPS, 2023 (*UT Austin*). [[Paper](https://arxiv.org/abs/2309.15275)]
* **FAT**: "Lightweight Vision Transformer with Bidirectional Interaction", NeurIPS, 2023 (*CAS*). [[Paper](https://arxiv.org/abs/2306.00396)][[PyTorch](https://github.com/qhfan/FAT)]
* **MCUFormer**: "MCUFormer: Deploying Vision Transformers on Microcontrollers with Limited Memory", NeurIPS, 2023 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2310.16898)][[PyTorch](https://github.com/liangyn22/MCUFormer)]
* **SoViT**: "Getting ViT in Shape: Scaling Laws for Compute-Optimal Model Design", NeurIPS, 2023 (*DeepMind*). [[Paper](https://arxiv.org/abs/2305.13035)]
* **CloFormer**: "Rethinking Local Perception in Lightweight Vision Transformer", arXiv, 2023 (*CAS*). [[Paper](https://arxiv.org/abs/2303.17803)]
* **Quadformer**: "Vision Transformers with Mixed-Resolution Tokenization", arXiv, 2023 (*Tel Aviv*). [[Paper](https://arxiv.org/abs/2304.00287)][[Code (in construction)](https://github.com/TomerRonen34/mixed-resolution-vit)]
* **SparseFormer**: "SparseFormer: Sparse Visual Recognition via Limited Latent Tokens", arXiv, 2023 (*NUS*). [[Paper](https://arxiv.org/abs/2304.03768)][[Code (in construction)](https://github.com/showlab/sparseformer)]
* **EMO**: "Rethinking Mobile Block for Efficient Attention-based Models", arXiv, 2023 (*Tencent*). [[Paper](https://arxiv.org/abs/2301.01146)][[PyTorch](https://github.com/zhangzjn/EMO)]
* **ByteFormer**: "Bytes Are All You Need: Transformers Operating Directly On File Bytes", arXiv, 2023 (*Apple*). [[Paper](https://arxiv.org/abs/2306.00238)]
* **?**: "Muti-Scale And Token Mergence: Make Your ViT More Efficient", arXiv, 2023 (*Jilin University*). [[Paper](https://arxiv.org/abs/2306.04897)]
* **FasterViT**: "FasterViT: Fast Vision Transformers with Hierarchical Attention", arXiv, 2023 (*NVIDIA*). [[Paper](https://arxiv.org/abs/2306.06189)]
* **NextViT**: "Vision Transformer with Attention Map Hallucination and FFN Compaction", arXiv, 2023 (*Baidu*). [[Paper](https://arxiv.org/abs/2306.10875)]
* **SkipAt**: "Skip-Attention: Improving Vision Transformers by Paying Less Attention", arXiv, 2023 (*Qualcomm*). [[Paper](https://arxiv.org/abs/2301.02240)]
* **MSViT**: "MSViT: Dynamic Mixed-Scale Tokenization for Vision Transformers", arXiv, 2023 (*Qualcomm*). [[Paper](https://arxiv.org/abs/2307.02321)]
* **DiT**: "DiT: Efficient Vision Transformers with Dynamic Token Routing", arXiv, 2023 (*Meituan*). [[Paper](https://arxiv.org/abs/2308.03409)][[Code (in construction)](https://github.com/Maycbj/DiT)]
* **?**: "Which Transformer to Favor: A Comparative Analysis of Efficiency in Vision Transformers", arXiv, 2023 (*German Research Center for Artificial Intelligence (DFKI)*). [[Paper](https://arxiv.org/abs/2308.09372)][[PyTorch](https://github.com/tobna/WhatTransformerToFavor)]
* **Mobile-V-MoEs**: "Mobile V-MoEs: Scaling Down Vision Transformers via Sparse Mixture-of-Experts", arXiv, 2023 (*Apple*). [[Paper](https://arxiv.org/abs/2309.04354)]
* **PPT**: "PPT: Token Pruning and Pooling for Efficient Vision Transformers", arXiv, 2023 (*Huawei*). [[Paper](https://arxiv.org/abs/2310.01812)]
* **MatFormer**: "MatFormer: Nested Transformer for Elastic Inference", arXiv, 2023 (*Google*). [[Paper](https://arxiv.org/abs/2310.07707)]
* **SparseFormer**: "Bootstrapping SparseFormers from Vision Foundation Models", arXiv, 2023 (*NUS*). [[Paper](https://arxiv.org/abs/2312.01987)][[PyTorch](https://github.com/showlab/sparseformer)]
* **GTP-ViT**: "GTP-ViT: Efficient Vision Transformers via Graph-based Token Propagation", WACV, 2024 (*CSIRO Data61, Australia*). [[Paper](https://arxiv.org/abs/2311.03035)][[PyTorch](https://github.com/Ackesnal/GTP-ViT)]
* **ToFu**: "Token Fusion: Bridging the Gap between Token Pruning and Token Merging", WACV, 2024 (*Samsung*). [[Paper](https://arxiv.org/abs/2312.01026)]
* **Cached-Transformer**: "Cached Transformers: Improving Transformers with Differentiable Memory Cache", AAAI, 2024 (*CUHK*). [[Paper](https://arxiv.org/abs/2312.12742)]
* **LF-ViT**: "LF-ViT: Reducing Spatial Redundancy in Vision Transformer for Efficient Image Recognition", AAAI, 2024 (*Harbin Institute of Technology*). [[Paper](https://arxiv.org/abs/2402.00033)][[PyTorch](https://github.com/edgeai1/LF-ViT)]
* **EfficientMod**: "Efficient Modulation for Vision Networks", ICLR, 2024 (*Microsoft*). [[Paper](https://arxiv.org/abs/2403.19963)][[PyTorch](https://github.com/ma-xu/EfficientMod)]
* **NOSE**: "MLP Can Be A Good Transformer Learner", CVPR, 2024 (*MBZUAI*). [[Paper](https://arxiv.org/abs/2404.05657)][[PyTorch](https://github.com/sihaoevery/lambda_vit)]
* **SLAB**: "SLAB: Efficient Transformers with Simplified Linear Attention and Progressive Re-parameterized Batch Normalization", ICML, 2024 (*Huawei*). [[Paper](https://arxiv.org/abs/2405.11582)][[PyTorch](https://github.com/xinghaochen/SLAB)]
* **S<sup>2</sup>**: "When Do We Not Need Larger Vision Models?", arXiv, 2024 (*Berkeley*). [[Paper](https://arxiv.org/abs/2403.13043)][[PyTorch](https://github.com/bfshi/scaling_on_scales)]
#### Conv + Transformer
* **LeViT**: "LeViT: a Vision Transformer in ConvNet's Clothing for Faster Inference", ICCV, 2021 (*Facebook*). [[Paper](https://arxiv.org/abs/2104.01136)][[PyTorch](https://github.com/facebookresearch/LeViT)]
* **CeiT**: "Incorporating Convolution Designs into Visual Transformers", ICCV, 2021 (*SenseTime*). [[Paper](https://arxiv.org/abs/2103.11816)][[PyTorch (rishikksh20)](https://github.com/rishikksh20/CeiT)]
* **Conformer**: "Conformer: Local Features Coupling Global Representations for Visual Recognition", ICCV, 2021 (*CAS*). [[Paper](https://arxiv.org/abs/2105.03889)][[PyTorch](https://github.com/pengzhiliang/Conformer)]
* **CoaT**: "Co-Scale Conv-Attentional Image Transformers", ICCV, 2021 (*UCSD*). [[Paper](https://arxiv.org/abs/2104.06399)][[PyTorch](https://github.com/mlpc-ucsd/CoaT)]
* **CvT**: "CvT: Introducing Convolutions to Vision Transformers", ICCV, 2021 (*Microsoft*). [[Paper](https://arxiv.org/abs/2103.15808)][[Code](https://github.com/leoxiaobin/CvT)]
* **ViTc**: "Early Convolutions Help Transformers See Better", NeurIPS, 2021 (*Facebook*). [[Paper](https://arxiv.org/abs/2106.14881)]
* **ConTNet**: "ConTNet: Why not use convolution and transformer at the same time?", arXiv, 2021 (*ByteDance*). [[Paper](https://arxiv.org/abs/2104.13497)][[PyTorch](https://github.com/yan-hao-tian/ConTNet)]
* **SPACH**: "A Battle of Network Structures: An Empirical Study of CNN, Transformer, and MLP", arXiv, 2021 (*Microsoft*). [[Paper](https://arxiv.org/abs/2108.13002)]
* **MobileViT**: "MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer", ICLR, 2022 (*Apple*). [[Paper](https://arxiv.org/abs/2110.02178)][[PyTorch](https://github.com/apple/ml-cvnets)]
* **CMT**: "CMT: Convolutional Neural Networks Meet Vision Transformers", CVPR, 2022 (*Huawei*). [[Paper](https://arxiv.org/abs/2107.06263)]
* **Mobile-Former**: "Mobile-Former: Bridging MobileNet and Transformer", CVPR, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2108.05895)][[PyTorch (in construction)](https://github.com/aaboys/mobileformer)]
* **TinyViT**: "TinyViT: Fast Pretraining Distillation for Small Vision Transformers", ECCV, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2207.10666)][[PyTorch](https://github.com/microsoft/Cream/tree/main/TinyViT)]
* **CETNet**: "Convolutional Embedding Makes Hierarchical Vision Transformer Stronger", ECCV, 2022 (*OPPO*). [[Paper](https://arxiv.org/abs/2207.13317)]
* **ParC-Net**: "ParC-Net: Position Aware Circular Convolution with Merits from ConvNets and Transformer", ECCV, 2022 (*Intellifusion, China*). [[Paper](https://arxiv.org/abs/2203.03952)][[PyTorch](https://github.com/hkzhang91/ParC-Net)]
* **?**: "How to Train Vision Transformer on Small-scale Datasets?", BMVC, 2022 (*MBZUAI*). [[Paper](https://arxiv.org/abs/2210.07240)][[PyTorch](https://github.com/hananshafi/vits-for-small-scale-datasets)]
* **DHVT**: "Bridging the Gap Between Vision Transformers and Convolutional Neural Networks on Small Datasets", NeurIPS, 2022 (*USTC*). [[Paper](https://arxiv.org/abs/2210.05958)][[Code (in construction)](https://github.com/ArieSeirack/DHVT)]
* **iFormer**: "Inception Transformer", NeurIPS, 2022 (*Sea AI Lab*). [[Paper](https://arxiv.org/abs/2205.12956)][[PyTorch](https://github.com/sail-sg/iFormer)]
* **DenseDCT**: "Explicitly Increasing Input Information Density for Vision Transformers on Small Datasets", NeurIPSW, 2022 (*University of Kansas*). [[Paper](https://arxiv.org/abs/2210.14319)]
* **CXV**: "Convolutional Xformers for Vision", arXiv, 2022 (*IIT Bombay*). [[Paper](https://arxiv.org/abs/2201.10271)][[PyTorch](https://github.com/pranavphoenix/CXV)]
* **ConvMixer**: "Patches Are All You Need?", arXiv, 2022 (*CMU*). [[Paper](https://arxiv.org/abs/2201.09792)][[PyTorch](https://github.com/locuslab/convmixer)]
* **MobileViTv2**: "Separable Self-attention for Mobile Vision Transformers", arXiv, 2022 (*Apple*). [[Paper](https://arxiv.org/abs/2206.02680)][[PyTorch](https://github.com/apple/ml-cvnets)]
* **UniFormer**: "UniFormer: Unifying Convolution and Self-attention for Visual Recognition", arXiv, 2022 (*SenseTime*). [[Paper](https://arxiv.org/abs/2201.09450)][[PyTorch](https://github.com/Sense-X/UniFormer)]
* **EdgeFormer**: "EdgeFormer: Improving Light-weight ConvNets by Learning from Vision Transformers", arXiv, 2022 (*?*). [[Paper](https://arxiv.org/abs/2203.03952)]
* **MoCoViT**: "MoCoViT: Mobile Convolutional Vision Transformer", arXiv, 2022 (*ByteDance*). [[Paper](https://arxiv.org/abs/2205.12635)]
* **DynamicViT**: "Dynamic Spatial Sparsification for Efficient Vision Transformers and Convolutional Neural Networks", arXiv, 2022 (*Tsinghua University*). [[Paper](https://arxiv.org/abs/2207.01580)][[PyTorch](https://github.com/raoyongming/DynamicViT)]
* **ConvFormer**: "ConvFormer: Closing the Gap Between CNN and Vision Transformers", arXiv, 2022 (*National University of Defense Technology, China*). [[Paper](https://arxiv.org/abs/2209.07738)]
* **Fast-ParC**: "Fast-ParC: Position Aware Global Kernel for ConvNets and ViTs", arXiv, 2022 (*Intellifusion, China*). [[Paper](https://arxiv.org/abs/2210.04020)]
* **MetaFormer**: "MetaFormer Baselines for Vision", arXiv, 2022 (*Sea AI Lab*). [[Paper](https://arxiv.org/abs/2210.13452)][[PyTorch](https://github.com/sail-sg/metaformer)]
* **STM**: "Demystify Transformers & Convolutions in Modern Image Deep Networks", arXiv, 2022 (*Tsinghua University*). [[Paper](https://arxiv.org/abs/2211.05781)][[Code (in construction)](https://github.com/OpenGVLab/STM-Evaluation)]
* **ParCNetV2**: "ParCNetV2: Oversized Kernel with Enhanced Attention", arXiv, 2022 (*Intellifusion, China*). [[Paper](https://arxiv.org/abs/2211.07157)]
* **VAN**: "Visual Attention Network", arXiv, 2022 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2202.09741)][[PyTorch](https://github.com/Visual-Attention-Network)]
* **SD-MAE**: "Masked autoencoders is an effective solution to transformer data-hungry", arXiv, 2022 (*Hangzhou Dianzi University*). [[Paper](https://arxiv.org/abs/2212.05677)][[PyTorch (in construction)](https://github.com/Talented-Q/SDMAE)]
* **SATA**: "Accumulated Trivial Attention Matters in Vision Transformers on Small Datasets", WACV, 2023 (*University of Kansas*). [[Paper](https://arxiv.org/abs/2210.12333)][[PyTorch (in construction)](https://github.com/xiangyu8/SATA)]
* **SparK**: "Sparse and Hierarchical Masked Modeling for Convolutional Representation Learning", ICLR, 2023 (*Bytedance*). [[Paper](https://openreview.net/forum?id=NRxydtWup1S)][[PyTorch](https://github.com/keyu-tian/SparK)]
* **MOAT**: "MOAT: Alternating Mobile Convolution and Attention Brings Strong Vision Models", ICLR, 2023 (*Google*). [[Paper](https://arxiv.org/abs/2210.01820)][[Tensorflow](https://github.com/google-research/deeplab2)]
* **InternImage**: "InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions", CVPR, 2023 (*Shanghai AI Laboratory*). [[Paper](https://arxiv.org/abs/2211.05778)][[PyTorch](https://github.com/OpenGVLab/InternImage)]
* **SwiftFormer**: "SwiftFormer: Efficient Additive Attention for Transformer-based Real-time Mobile Vision Applications", ICCV, 2023 (*MBZUAI*). [[Paper](https://arxiv.org/abs/2303.15446)][[PyTorch](https://github.com/Amshaker/SwiftFormer)]
* **SCSC**: "SCSC: Spatial Cross-scale Convolution Module to Strengthen both CNNs and Transformers", ICCVW, 2023 (*Megvii*). [[Paper](https://arxiv.org/abs/2308.07110)]
* **PSLT**: "PSLT: A Light-weight Vision Transformer with Ladder Self-Attention and Progressive Shift", TPAMI, 2023 (*Sun Yat-sen University*). [[Paper](https://arxiv.org/abs/2304.03481)][[Website](https://isee-ai.cn/wugaojie/PSLT.html)]
* **RepViT**: "RepViT: Revisiting Mobile CNN From ViT Perspective", arXiv, 2023 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2307.09283)][[PyTorch](https://github.com/jameslahm/RepViT)]
* **?**: "Interpret Vision Transformers as ConvNets with Dynamic Convolutions", arXiv, 2023 (*NTU, Singapore*). [[Paper](https://arxiv.org/abs/2309.10713)]
* **UPDP**: "UPDP: A Unified Progressive Depth Pruner for CNN and Vision Transformer", AAAI, 2024 (*AMD*). [[Paper](https://arxiv.org/abs/2401.06426)]
#### Training + Transformer
* **iGPT**: "Generative Pretraining From Pixels", ICML, 2020 (*OpenAI*). [[Paper](http://proceedings.mlr.press/v119/chen20s.html)][[Tensorflow](https://github.com/openai/image-gpt)]
* **CLIP**: "Learning Transferable Visual Models From Natural Language Supervision", ICML, 2021 (*OpenAI*). [[Paper](https://arxiv.org/abs/2103.00020)][[PyTorch](https://github.com/openai/CLIP)]
* **MoCo-V3**: "An Empirical Study of Training Self-Supervised Vision Transformers", ICCV, 2021 (*Facebook*). [[Paper](https://arxiv.org/abs/2104.02057)]
* **DINO**: "Emerging Properties in Self-Supervised Vision Transformers", ICCV, 2021 (*Facebook*). [[Paper](https://arxiv.org/abs/2104.14294)][[PyTorch](https://github.com/facebookresearch/dino)]
* **drloc**: "Efficient Training of Visual Transformers with Small Datasets", NeurIPS, 2021 (*University of Trento*). [[Paper](https://arxiv.org/abs/2106.03746)][[PyTorch](https://github.com/yhlleo/VTs-Drloc)]
* **CARE**: "Revitalizing CNN Attentions via Transformers in Self-Supervised Visual Representation Learning", NeurIPS, 2021 (*Tencent*). [[Paper](https://arxiv.org/abs/2110.05340)][[PyTorch](https://github.com/ChongjianGE/CARE)]
* **MST**: "MST: Masked Self-Supervised Transformer for Visual Representation", NeurIPS, 2021 (*SenseTime*). [[Paper](https://arxiv.org/abs/2106.05656)]
* **SiT**: "SiT: Self-supervised Vision Transformer", arXiv, 2021 (*University of Surrey*). [[Paper](https://arxiv.org/abs/2104.03602)][[PyTorch](https://github.com/Sara-Ahmed/SiT)]
* **MoBY**: "Self-Supervised Learning with Swin Transformers", arXiv, 2021 (*Microsoft*). [[Paper](https://arxiv.org/abs/2105.04553)][[PyTorch](https://github.com/SwinTransformer/Transformer-SSL)]
* **?**: "Investigating Transfer Learning Capabilities of Vision Transformers and CNNs by Fine-Tuning a Single Trainable Block", arXiv, 2021 (*Pune Institute of Computer Technology, India*). [[Paper](https://arxiv.org/abs/2110.05270)]
* **Annotations-1.3B**: "Billion-Scale Pretraining with Vision Transformers for Multi-Task Visual Representations", WACV, 2022 (*Pinterest*). [[Paper](https://arxiv.org/abs/2108.05887)]
* **BEiT**: "BEiT: BERT Pre-Training of Image Transformers", ICLR, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2106.08254)][[PyTorch](https://github.com/microsoft/unilm/tree/master/beit)]
* **EsViT**: "Efficient Self-supervised Vision Transformers for Representation Learning", ICLR, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2106.09785)]
* **iBOT**: "Image BERT Pre-training with Online Tokenizer", ICLR, 2022 (*ByteDance*). [[Paper](https://arxiv.org/abs/2111.07832)][[PyTorch](https://github.com/bytedance/ibot)]
* **MaskFeat**: "Masked Feature Prediction for Self-Supervised Visual Pre-Training", CVPR, 2022 (*Facebook*). [[Paper](https://arxiv.org/abs/2112.09133)]
* **AutoProg**: "Automated Progressive Learning for Efficient Training of Vision Transformers", CVPR, 2022 (*Monash University, Australia*). [[Paper](https://arxiv.org/abs/2203.14509)][[Code (in construction)](https://github.com/changlin31/AutoProg)]
* **MAE**: "Masked Autoencoders Are Scalable Vision Learners", CVPR, 2022 (*Facebook*). [[Paper](https://arxiv.org/abs/2111.06377)][[PyTorch](https://github.com/facebookresearch/mae)][[PyTorch (pengzhiliang)](https://github.com/pengzhiliang/MAE-pytorch)]
* **SimMIM**: "SimMIM: A Simple Framework for Masked Image Modeling", CVPR, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2111.09886)][[PyTorch](https://github.com/microsoft/SimMIM)]
* **SelfPatch**: "Patch-Level Representation Learning for Self-Supervised Vision Transformers", CVPR, 2022 (*KAIST*). [[Paper](https://arxiv.org/abs/2206.07990)][[PyTorch](https://github.com/alinlab/SelfPatch)]
* **Bootstrapping-ViTs**: "Bootstrapping ViTs: Towards Liberating Vision Transformers from Pre-training", CVPR, 2022 (*Zhejiang University*). [[Paper](https://arxiv.org/abs/2112.03552)][[PyTorch](https://github.com/zhfeing/Bootstrapping-ViTs-pytorch)]
* **TransMix**: "TransMix: Attend to Mix for Vision Transformers", CVPR, 2022 (*JHU*). [[Paper](https://arxiv.org/abs/2111.09833)][[PyTorch](https://github.com/Beckschen/TransMix)]
* **PatchRot**: "PatchRot: A Self-Supervised Technique for Training Vision Transformers", CVPRW, 2022 (*Arizona State*). [[Paper](https://drive.google.com/file/d/1ZHdBMa-MCx05Y0teqb0vmgiiYj8t5xBB/view)]
* **SplitMask**: "Are Large-scale Datasets Necessary for Self-Supervised Pre-training?", CVPRW, 2022 (*Meta*). [[Paper](https://arxiv.org/abs/2112.10740)]
* **MC-SSL**: "MC-SSL: Towards Multi-Concept Self-Supervised Learning", CVPRW, 2022 (*University of Surrey, UK*). [[Paper](https://arxiv.org/abs/2111.15340)]
* **RelViT**: "Where are my Neighbors? Exploiting Patches Relations in Self-Supervised Vision Transformer", CVPRW, 2022 (*University of Padova, Italy*). [[Paper](https://arxiv.org/abs/2206.00481?context=cs)]
* **data2vec**: "data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language", ICML, 2022 (*Meta*). [[Paper](https://arxiv.org/abs/2202.03555)][[PyTorch](https://github.com/facebookresearch/fairseq/tree/main/examples/data2vec)]
* **SSTA**: "Self-supervised Models are Good Teaching Assistants for Vision Transformers", ICML, 2022 (*Tencent*). [[Paper](https://proceedings.mlr.press/v162/wu22c.html)][[Code (in construction)](https://github.com/GlassyWu/SSTA)]
* **MP3**: "Position Prediction as an Effective Pretraining Strategy", ICML, 2022 (*Apple*). [[Paper](https://arxiv.org/abs/2207.07611)][[PyTorch](https://github.com/arshadshk/Position-Prediction-Pretraining)]
* **CutMixSL**: "Visual Transformer Meets CutMix for Improved Accuracy, Communication Efficiency, and Data Privacy in Split Learning", IJCAI, 2022 (*Yonsei University, Korea*). [[Paper](https://arxiv.org/abs/2207.00234)]
* **BootMAE**: "Bootstrapped Masked Autoencoders for Vision BERT Pretraining", ECCV, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2207.07116)][[PyTorch](https://github.com/LightDXY/BootMAE)]
* **TokenMix**: "TokenMix: Rethinking Image Mixing for Data Augmentation in Vision Transformers", ECCV, 2022 (*CUHK*). [[Paper](https://arxiv.org/abs/2207.08409)][[PyTorch](https://github.com/Sense-X/TokenMix)]
* **?**: "Locality Guidance for Improving Vision Transformers on Tiny Datasets", ECCV, 2022 (*Peking University*). [[Paper](https://arxiv.org/abs/2207.10026)][[PyTorch](https://github.com/lkhl/tiny-transformers)]
* **HAT**: "Improving Vision Transformers by Revisiting High-frequency Components", ECCV, 2022 (*Tsinghua*). [[Paper](https://arxiv.org/abs/2204.00993)][[PyTorch](https://github.com/jiawangbai/HAT)]
* **IDMM**: "Training Vision Transformers with Only 2040 Images", ECCV, 2022 (*Nanjing University*). [[Paper](https://arxiv.org/abs/2201.10728)]
* **AttMask**: "What to Hide from Your Students: Attention-Guided Masked Image Modeling", ECCV, 2022 (*National Technical University of Athens*). [[Paper](https://arxiv.org/abs/2203.12719)][[PyTorch](https://github.com/gkakogeorgiou/attmask)]
* **SLIP**: "SLIP: Self-supervision meets Language-Image Pre-training", ECCV, 2022 (*Berkeley + Meta*). [[Paper](https://arxiv.org/abs/2112.12750)][[Pytorch](https://github.com/facebookresearch/SLIP)]
* **mc-BEiT**: "mc-BEiT: Multi-Choice Discretization for Image BERT Pre-training", ECCV, 2022 (*Peking University*). [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/1197_ECCV_2022_paper.php)]
* **SL2O**: "Scalable Learning to Optimize: A Learned Optimizer Can Train Big Models", ECCV, 2022 (*UT Austin*). [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/2909_ECCV_2022_paper.php)][[PyTorch](https://github.com/VITA-Group/Scalable-L2O)]
* **TokenMixup**: "TokenMixup: Efficient Attention-guided Token-level Data Augmentation for Transformers", NeurIPS, 2022 (*Korea University*). [[Paper](https://arxiv.org/abs/2210.07562)][[PyTorch](https://github.com/mlvlab/TokenMixup)]
* **PatchRot**: "PatchRot: A Self-Supervised Technique for Training Vision Transformers", NeurIPSW, 2022 (*Arizona State University*). [[Paper](https://arxiv.org/abs/2210.15722)]
* **GreenMIM**: "Green Hierarchical Vision Transformer for Masked Image Modeling", NeurIPS, 2022 (*The University of Tokyo*). [[Paper](https://arxiv.org/abs/2205.13515)][[PyTorch](https://github.com/LayneH/GreenMIM)]
* **DP-CutMix**: "Differentially Private CutMix for Split Learning with Vision Transformer", NeurIPSW, 2022 (*Yonsei University*). [[Paper](https://arxiv.org/abs/2210.15986)]
* **?**: "How to train your ViT? Data, Augmentation, and Regularization in Vision Transformers", Transactions on Machine Learning Research (TMLR), 2022 (*Google*). [[Paper](https://openreview.net/forum?id=4nPswr1KcP)][[Tensorflow](https://github.com/google-research/vision_transformer)][[PyTorch (rwightman)](https://github.com/rwightman/pytorch-image-models)]
* **PeCo**: "PeCo: Perceptual Codebook for BERT Pre-training of Vision Transformers", arXiv, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2111.12710)]
* **RePre**: "RePre: Improving Self-Supervised Vision Transformer with Reconstructive Pre-training", arXiv, 2022 (*Beijing University of Posts and Telecommunications*). [[Paper](https://arxiv.org/abs/2201.06857)]
* **Beyond-Masking**: "Beyond Masking: Demystifying Token-Based Pre-Training for Vision Transformers", arXiv, 2022 (*CAS*). [[Paper](https://arxiv.org/abs/2203.14313)][[Code (in construction)](https://github.com/sunsmarterjie/beyond_masking)]
* **Kronecker-Adaptation**: "Parameter-efficient Fine-tuning for Vision Transformers", arXiv, 2022 (*Microsoft*). [[Paper](https://arxiv.org/abs/2203.16329)]
* **DILEMMA**: "DILEMMA: Self-Supervised Shape and Texture Learning with Transformers", arXiv, 2022 (*University of Bern, Switzerland*). [[Paper](https://arxiv.org/abs/2204.04788)]
* **DeiT-III**