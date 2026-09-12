[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/hee9joon/Awesome-Diffusion-Models) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Made With Love](https://img.shields.io/badge/Made%20With-Love-red.svg)](https://github.com/chetanraj/awesome-github-badges)

This repository contains a collection of resources and papers on ***Diffusion Models***.

Please refer to [this page](https://diff-usion.github.io/Awesome-Diffusion-Models/) as this page may not contain all the information due to page constraints.

## Contents
- [Resources](#resources)
  - [Introductory Posts](#introductory-posts)
  - [Introductory Papers](#introductory-papers)
  - [Introductory Videos](#introductory-videos)
  - [Introductory Lectures](#introductory-lectures)
  - [Tutorial and Jupyter Notebook](#tutorial-and-jupyter-notebook)
- [Papers](#papers)
  - [Survey](#survey)
  - [Vision](#vision)
    - [Generation](#generation)
    - [Classification](#classification)
    - [Segmentation](#segmentation)
    - [Image Translation](#image-translation)
    - [Inverse Problems](#inverse-problems)
    - [Medical Imaging](#medical-imaging)
    - [Multi-modal Learning](#multi-modal-learning)
    - [3D Vision](#3d-vision)
    - [Adversarial Attack](#adversarial-attack)
    - [Miscellany](#miscellany)
  - [Audio](#audio)
    - [Generation](#generation-1)
    - [Conversion](#conversion)
    - [Enhancement](#enhancement)
    - [Separation](#separation)
    - [Text-to-Speech](#text-to-speech)
    - [Miscellany](#miscellany-1)
  - [Natural Language](#natural-language)
  - [Tabular and Time Series](#tabular-and-time-series)
    - [Generation](#generation-2)
    - [Forecasting](#forecasting)
    - [Imputation](#imputation)
    - [Miscellany](#miscellany-2)
  - [Graph](#graph)
    - [Generation](#generation-3)
    - [Molecular and Material Generation](#molecular-and-material-generation)
  - [Reinforcement Learning](#reinforcement-learning)
  - [Theory](#theory)
  - [Applications](#applications)


# Resources
## Introductory Posts

**:fast_forward: DiffusionFastForward: 01-Diffusion-Theory** \
*Mikolaj Czerkawski (@mikonvergence)* \
[[Website](https://github.com/mikonvergence/DiffusionFastForward/blob/master/notes/01-Diffusion-Theory.md)] \
4 Feb 2023

**How diffusion models work: the math from scratch** \
*Sergios Karagiannakos,Nikolas Adaloglou* \
[[Website](https://theaisummer.com/diffusion-models/?fbclid=IwAR1BIeNHqa3NtC8SL0sKXHATHklJYphNH-8IGNoO3xZhSKM_GYcvrrQgB0o)] \
24 Sep 2022

**A Path to the Variational Diffusion Loss** \
*Alex Alemi* \
[[Website](https://blog.alexalemi.com/diffusion.html)] [[Colab](https://colab.research.google.com/github/google-research/vdm/blob/main/colab/SimpleDiffusionColab.ipynb)] \
15 Sep 2022

**The Annotated Diffusion Model** \
*Niels Rogge, Kashif Rasul* \
[[Website](https://huggingface.co/blog/annotated-diffusion)] \
06 Jun 2022

**The recent rise of diffusion-based models** \
*Maciej Domagała* \
[[Website](https://maciejdomagala.github.io/generative_models/2022/06/06/The-recent-rise-of-diffusion-based-models.html)] \
06 Jun 2022

**Introduction to Diffusion Models for Machine Learning** \
*Ryan O'Connor* \
[[Website](https://www.assemblyai.com/blog/diffusion-models-for-machine-learning-introduction/)] \
12 May 2022

**Improving Diffusion Models as an Alternative To GANs** \
*Arash Vahdat and Karsten Kreis* \
[[Website-Part 1](https://developer.nvidia.com/blog/improving-diffusion-models-as-an-alternative-to-gans-part-1/)] [[Website-Part 2](https://developer.nvidia.com/blog/improving-diffusion-models-as-an-alternative-to-gans-part-2/)] \
26 Apr 2022

**An introduction to Diffusion Probabilistic Models** \
*Ayan Das* \
[[Website](https://ayandas.me/blog-tut/2021/12/04/diffusion-prob-models.html)] \
04 Dec 2021

**Introduction to deep generative modeling: Diffusion-based Deep Generative Models** \
*Jakub Tomczak* \
[[Website](https://jmtomczak.github.io/blog/10/10_ddgms_lvm_p2.html)] \
30 Aug 2021

**What are Diffusion Models?** \
*Lilian Weng* \
[[Website](https://lilianweng.github.io/lil-log/2021/07/11/diffusion-models.html)] \
11 Jul 2021

**Diffusion Models as a kind of VAE** \
*Angus Turner* \
[[Website](https://angusturner.github.io/generative_models/2021/06/29/diffusion-probabilistic-models-I.html)] \
29 Jun 2021

**Generative Modeling by Estimating Gradients of the Data Distribution** \
*Yang Song* \
[[Website](https://yang-song.github.io/blog/2021/score/)] \
5 May 2021

## Introductory Papers

**Understanding Diffusion Models: A Unified Perspective** \
*Calvin Luo* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.11970)] \
25 Aug 2022

**How to Train Your Energy-Based Models** \
*Yang Song, Diederik P. Kingma* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2101.03288)] \
9 Jan 2021

## Introductory Videos

**:fast_forward: DiffusionFastForward** \
*Mikolaj Czerkawski (@mikonvergence)* \
[[Video](https://www.youtube.com/playlist?list=PL5RHjmn-MVHDMcqx-SI53mB7sFOqPK6gN)] \
4 Mar 2023

**Diffusion models from scratch in PyTorch** \
*DeepFindr* \
[[Video](https://www.youtube.com/watch?v=a4Yfz2FxXiY)] \
18 Jul 2022

**Diffusion Models | Paper Explanation | Math Explained** \
*Outlier* \
[[Video](https://www.youtube.com/watch?v=HoKDTa5jHvg)] \
6 Jun 2022

**What are Diffusion Models?** \
*Ari Seff* \
[[Video](https://www.youtube.com/watch?v=fbLgFrlTnGU&list=LL&index=2)] \
20 Apr 2022

**Diffusion models explained** \
*AI Coffee Break with Letitia* \
[[Video](https://www.youtube.com/watch?v=344w5h24-h8&ab_channel=AICoffeeBreakwithLetitia)] \
23 Mar 2022

## Introductory Lectures

**Denoising Diffusion-based Generative Modeling: Foundations and Applications** \
*Karsten Kreis, Ruiqi Gao, Arash Vahdat* \
[[Page](https://cvpr2022-tutorial-diffusion-models.github.io/)] \
19 Jun 2022

**Diffusion Probabilistic Models** \
*Jascha Sohl-Dickstein, MIT 6.S192 - Lecture 22* \
[[Video](https://www.youtube.com/watch?v=XCUlnHP1TNM)] \
19 Apr 2022

## Tutorial and Jupyter Notebook

**:fast_forward: DiffusionFastForward: train from scratch in colab** \
*Mikolaj Czerkawski (@mikonvergence)* \
[[Github](https://github.com/mikonvergence/DiffusionFastForward)]
[[notebook](https://github.com/mikonvergence/DiffusionFastForward#computer-code)]

**diffusion-for-beginners** \
*ozanciga* \
[[Github](https://github.com/ozanciga/diffusion-for-beginners)]

**Beyond Diffusion: What is Personalized Image Generation and How Can You Customize Image Synthesis?** \
*J. Rafid Siddiqui* \
[[Github](https://github.com/azad-academy/personalized-diffusion)] [[Medium](https://medium.com/mlearning-ai/beyond-diffusion-what-is-personalized-image-generation-and-how-can-you-customize-image-synthesis-26a89d5b335)]

**Diffusion_models_tutorial** \
*FilippoMB* \
[[Github](https://github.com/FilippoMB/Diffusion_models_tutorial)]

**ScoreDiffusionModel** \
*JeongJiHeon* \
[[Github](https://github.com/JeongJiHeon/ScoreDiffusionModel)]

**Minimal implementation of diffusion models** \
*VSehwag* \
[[Github](https://github.com/VSehwag/minimal-diffusion)]

**diffusion_tutorial** \
*sunlin-ai* \
[[Github](https://github.com/sunlin-ai/diffusion_tutorial)] 

**Denoising diffusion probabilistic models** \
*acids-ircam* \
[[Github](https://github.com/acids-ircam/diffusion_models)] 


**Centipede Diffusion** \
*Zalring* \
[[Notebook](https://colab.research.google.com/github/Zalring/Centipede_Diffusion/blob/main/Centipede_Diffusion.ipynb)]

**Deforum Stable Diffusion** \
*deforum* \
[[Notebook](https://colab.research.google.com/github/deforum/stable-diffusion/blob/main/Deforum_Stable_Diffusion.ipynb)]

**Stable Diffusion Interpolation** \
*None* \
[[Notebook](https://colab.research.google.com/drive/1EHZtFjQoRr-bns1It5mTcOVyZzZD9bBc?usp=sharing)]

**Keras Stable Diffusion: GPU starter example** \
*None* \
[[Notebook](https://colab.research.google.com/drive/1zVTa4mLeM_w44WaFwl7utTaa6JcaH1zK)]

**Huemin Jax Diffusion** \
*huemin-art* \
[[Notebook](https://colab.research.google.com/github/huemin-art/jax-guided-diffusion/blob/v2.7/Huemin_Jax_Diffusion_2_7.ipynb)]

**Disco Diffusion** \
*alembics* \
[[Notebook](https://colab.research.google.com/github/alembics/disco-diffusion/blob/main/Disco_Diffusion.ipynb)]

**Simplified Disco Diffusion** \
*entmike* \
[[Notebook](https://colab.research.google.com/github/entmike/disco-diffusion-1/blob/main/Simplified_Disco_Diffusion.ipynb)]

**WAS's Disco Diffusion - Portrait Generator Playground** \
*WASasquatch* \
[[Notebook](https://colab.research.google.com/github/WASasquatch/disco-diffusion-portrait-playground/blob/main/WAS's_Disco_Diffusion_v5_6_9_%5BPortrait_Generator_Playground%5D.ipynb)]

**Diffusers - Hugging Face** \
*huggingface* \
[[Notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/diffusers_intro.ipynb)] 


# Papers

## Survey

**A Survey on Video Diffusion Models** \
*Zhen Xing, Qijun Feng, Haoran Chen, Qi Dai, Han Hu, Hang Xu, Zuxuan Wu and Yu-Gang Jiang*
arXiv 2023. [[Paper](https://arxiv.org/pdf/2310.10647.pdf)] \
16 Oct 2023

**State of the Art on Diffusion Models for Visual Computing** \
*Ryan Po, Wang Yifan, Vladislav Golyanik, Kfir Aberman, Jonathan T. Barron, Amit H. Bermano, Eric Ryan Chan, Tali Dekel, Aleksander Holynski, Angjoo Kanazawa, C. Karen Liu, Lingjie Liu, Ben Mildenhall, Matthias Nießner, Björn Ommer, Christian Theobalt, Peter Wonka, Gordon Wetzstein* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.07204)] \
11 Oct 2023

**Memory in Plain Sight: A Survey of the Uncanny Resemblances between Diffusion Models and Associative Memories** \
*Benjamin Hoover, Hendrik Strobelt, Dmitry Krotov, Judy Hoffman, Zsolt Kira, Duen Horng Chau* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.16750)] \
28 Sep 2023

**A Survey of Diffusion Based Image Generation Models: Issues and Their Solutions** \
*Tianyi Zhang, Zheng Wang, Jing Huang, Mohiuddin Muhammad Tasnim, Wei Shi* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.13142)] \
25 Aug 2023

**Diffusion Models for Image Restoration and Enhancement -- A Comprehensive Survey** \
*Xin Li, Yulin Ren, Xin Jin, Cuiling Lan, Xingrui Wang, Wenjun Zeng, Xinchao Wang, Zhibo Chen* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.09388)] \
18 Aug 2023

**A Comprehensive Survey on Generative Diffusion Models for Structured Data** \
*Heejoon Koo, To Eun Kim* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.04139)] \
7 Jun 2023

**On the Design Fundamentals of Diffusion Models: A Survey** \
*Ziyi Chang, George A. Koulieris, Hubert P. H. Shum* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.04542)] \
7 Jun 2023

**Diffusion Models in NLP: A Survey** \
*Hao Zou, Zae Myung Kim, Dongyeop Kang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.14671)] \
24 May 2023

**Diffusion Models for Time Series Applications: A Survey** \
*Lequan Lin, Zhengkun Li, Ruikun Li, Xuliang Li, Junbin Gao* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.00624)] \
1 May 2023

**A Comprehensive Survey on Knowledge Distillation of Diffusion Models** \
*Weijian Luo* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.04262)] \
9 Apr 2023

**A Survey on Graph Diffusion Models: Generative AI in Science for Molecule, Protein and Material** \
*Mengchun Zhang, Maryam Qamar, Taegoo Kang, Yuna Jung, Chenshuang Zhang, Sung-Ho Bae, Chaoning Zhang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.01565)] \
4 Apr 2023

**Audio Diffusion Model for Speech Synthesis: A Survey on Text To Speech and Speech Enhancement in Generative AI** \
*Chenshuang Zhang, Chaoning Zhang, Sheng Zheng, Mengchun Zhang, Maryam Qamar, Sung-Ho Bae, In So Kweon* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.13336)] \
23 Mar 2023

**Diffusion Models in NLP: A Survey** \
*Yuansong Zhu, Yu Zhao* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.07576)] \
14 Mar 2023

**Text-to-image Diffusion Model in Generative AI: A Survey** \
*Chenshuang Zhang, Chaoning Zhang, Mengchun Zhang, In So Kweon* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.07909)] \
14 Mar 2023

**Diffusion Models for Non-autoregressive Text Generation: A Survey** \
*Yifan Li, Kun Zhou, Wayne Xin Zhao, Ji-Rong Wen* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.06574)] \
12 Mar 2023

**Diffusion Models in Bioinformatics: A New Wave of Deep Learning Revolution in Action** \
*Zhiye Guo, Jian Liu, Yanli Wang, Mengrui Chen, Duolin Wang, Dong Xu, Jianlin Cheng* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.10907)] \
13 Feb 2023

**Generative Diffusion Models on Graphs: Methods and Applications** \
*Wenqi Fan, Chengyi Liu, Yunqing Liu, Jiatong Li, Hang Li, Hui Liu, Jiliang Tang, Qing Li* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.02591)] \
6 Feb 2023

**Diffusion Models for Medical Image Analysis: A Comprehensive Survey** \
*Amirhossein Kazerouni, Ehsan Khodapanah Aghdam, Moein Heidari, Reza Azad, Mohsen Fayyaz, Ilker Hacihaliloglu, Dorit Merhof* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.07804)] [[Github](https://github.com/amirhossein-kz/Awesome-Diffusion-Models-in-Medical-Imaging)] \
14 Nov 2022

**Efficient Diffusion Models for Vision: A Survey** \
*Anwaar Ulhaq, Naveed Akhtar, Ganna Pogrebna* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2210.09292)] \
7 Oct 2022

**Diffusion Models in Vision: A Survey** \
*Florinel-Alin Croitoru, Vlad Hondru, Radu Tudor Ionescu, Mubarak Shah* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2209.04747)] \
10 Sep 2022

**A Survey on Generative Diffusion Model** \
*Hanqun Cao, Cheng Tan, Zhangyang Gao, Guangyong Chen, Pheng-Ann Heng, Stan Z. Li* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2209.02646)] \
6 Sep 2022

**Diffusion Models: A Comprehensive Survey of Methods and Applications** \
*Ling Yang, Zhilong Zhang, Shenda Hong, Wentao Zhang* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2209.00796)] \
2 Sep 2022

## Vision
### Generation

**DiffEnc: Variational Diffusion with a Learned Encoder** \
*Beatrix M. G. Nielsen, Anders Christensen, Andrea Dittadi, Ole Winther* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.19789)] \
30 Oct 2023

**Upgrading VAE Training With Unlimited Data Plans Provided by Diffusion Models** \
*Tim Z. Xiao, Johannes Zenn, Robert Bamler* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.19653)] \
30 Oct 2023

**Successfully Applying Lottery Ticket Hypothesis to Diffusion Model** \
*Chao Jiang, Bo Hui, Bohan Liu, Da Yan* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.18823)] \
28 Oct 2023

**Noise-Free Score Distillation** \
*Oren Katzir, Or Patashnik, Daniel Cohen-Or, Dani Lischinski* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.17590)] \
26 Oct 2023

**The statistical thermodynamics of generative diffusion models** \
*Luca Ambrogioni* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.17467)] \
26 Oct 2023

**Improving Denoising Diffusion Models via Simultaneous Estimation of Image and Noise** \
*Zhenkai Zhang, Krista A. Ehinger, Tom Drummond* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.17167)] \
26 Oct 2023

**Hierarchical Semi-Implicit Variational Inference with Application to Diffusion Model Acceleration** \
*Longlin Yu, Tianyu Xie, Yu Zhu, Tong Yang, Xiangyu Zhang, Cheng Zhang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.17153)] [[Github](https://github.com/longinyu/hsivi)] \
26 Oct 2023

**RePoseDM: Recurrent Pose Alignment and Gradient Guidance for Pose Guided Image Synthesis** \
*Anant Khandelwal* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.16074)] \
24 Oct 2023

**Improved Techniques for Training Consistency Models** \
*Yang Song, Prafulla Dhariwal* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.14189)] \
22 Oct 2023

**ScaleLong: Towards More Stable Training of Diffusion Model via Scaling Network Long Skip Connection** \
*Zhongzhan Huang, Pan Zhou, Shuicheng Yan, Liang Lin* \
NeurIPS 2023. [[Paper](https://arxiv.org/abs/2310.13545)] [[Github](https://github.com/sail-sg/ScaleLong)] \
20 Oct 2023


**Particle Guidance: non-I.I.D. Diverse Sampling with Diffusion Models** \
*Gabriele Corso, Yilun Xu, Valentin de Bortoli, Regina Barzilay, Tommi Jaakkola* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.13102)] [[Github](https://github.com/gcorso/particle-guidance)] \
19 Oct 2023

**Closed-Form Diffusion Models** \
*Christopher Scarvelis, Haitz Sáez de Ocáriz Borde, Justin Solomon* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.12395)] \
19 Oct 2023

**Elucidating The Design Space of Classifier-Guided Diffusion Generation** \
*Jiajun Ma, Tianyang Hu, Wenjia Wang, Jiacheng Sun* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.11311)] [[Github](https://github.com/alexmaols/elucd)] \
17 Oct 2023


**BayesDiff: Estimating Pixel-wise Uncertainty in Diffusion via Bayesian Inference** \
*Siqi Kou, Lei Gan, Dequan Wang, Chongxuan Li, Zhijie Deng* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.11142)] \
17 Oct 2023

**Unsupervised Discovery of Interpretable Directions in h-space of Pre-trained Diffusion Models** \
*Zijian Zhang, Luping Liu. Zhijie Lin, Yichen Zhu, Zhou Zhao* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.09912)] \
15 Oct 2023

**Towards More Accurate Diffusion Model Acceleration with A Timestep Aligner** \
*Mengfei Xia, Yujun Shen, Changsong Lei, Yu Zhou, Ran Yi, Deli Zhao, Wenping Wang, Yong-jin Liu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.09469)] \
14 Oct 2023

**Unseen Image Synthesis with Diffusion Models** \
*Ye Zhu, Yu Wu, Zhiwei Deng, Olga Russakovsky, Yan Yan* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.09213)] \
13 Oct 2023

**Debias the Training of Diffusion Models** \
*Hu Yu, Li Shen, Jie Huang, Man Zhou, Hongsheng Li, Feng Zhao* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.08442)] \
12 Oct 2023

**Neural Diffusion Models** \
*Grigory Bartosh, Dmitry Vetrov, Christian A. Naesseth* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.08337)] \
12 Oct 2023

**Efficient Integrators for Diffusion Generative Models** \
*Kushagra Pandey, Maja Rudolph, Stephan Mandt* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.07894)] \
11 Oct 2023


**Learning Stackable and Skippable LEGO Bricks for Efficient, Reconfigurable, and Variable-Resolution Diffusion Modeling** \
*Huangjie Zheng, Zhendong Wang, Jianbo Yuan, Guanghan Ning, Pengcheng He, Quanzeng You, Hongxia Yang, Mingyuan Zhou* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.06389)] \
10 Oct 2023

**Language Model Beats Diffusion -- Tokenizer is Key to Visual Generation** \
*Lijun Yu, José Lezama, Nitesh B. Gundavarapu, Luca Versari, Kihyuk Sohn, David Minnen, Yong Cheng, Agrim Gupta, Xiuye Gu, Alexander G. Hauptmann, Boqing Gong, Ming-Hsuan Yang, Irfan Essa, David A. Ross, Lu Jiang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.05737)] [[Github](https://github.com/lucidrains/magvit2-pytorch)] \
9 Oct 2023

**The Emergence of Reproducibility and Consistency in Diffusion Models** \
*Huijie Zhang, Jinfan Zhou, Yifu Lu, Minzhe Guo, Liyue Shen, Qing Qu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.05264)] \
8 Oct 2023

**DiffNAS: Bootstrapping Diffusion Models by Prompting for Better Architectures** \
*Wenhao Li, Xiu Su, Shan You, Fei Wang, Chen Qian, Chang Xu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.04750)] \
7 Oct 2023

**Observation-Guided Diffusion Probabilistic Models** \
*Junoh Kang, Jinyoung Choi, Sungik Choi, Bohyung Han* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.04041)] \
6 Oct 2023

**Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference** \
*Simian Luo, Yiqin Tan, Longbo Huang, Jian Li, Hang Zhao* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.04378)] \
6 Oct 2023

**Denoising Diffusion Step-aware Models** \
*Shuai Yang, Yukang Chen, Luozhou Wang, Shu Liu, Yingcong Chen* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.03337)] \
5 Oct 2023


**EfficientDM: Efficient Quantization-Aware Fine-Tuning of Low-Bit Diffusion Models** \
*Yefei He, Jing Liu, Weijia Wu, Hong Zhou, Bohan Zhuang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.03270)] \
5 Oct 2023

**Learning Energy-Based Prior Model with Diffusion-Amortized MCMC** \
*Peiyu Yu, Yaxuan Zhu, Sirui Xie, Xiaojian Ma, Ruiqi Gao, Song-Chun Zhu, Ying Nian Wu* \
NeurIPS 2023. [[Paper](https://arxiv.org/abs/2310.03218)] [[Github](https://github.com/yuPeiyu98/Diffusion-Amortized-MCMC)] \
5 Oct 2023

**On Memorization in Diffusion Models** \
*Xiangming Gu, Chao Du, Tianyu Pang, Chongxuan Li, Min Lin, Ye Wang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.02664)] [[Github](https://github.com/sail-sg/DiffMemorize)] \
4 Oct 2023


**Sequential Data Generation with Groupwise Diffusion Process** \
*Sangyun Lee, Gayoung Lee, Hyunsu Kim, Junho Kim, Youngjung Uh* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.01400)] \
2 Oct 2023

**Consistency Trajectory Models: Learning Probability Flow ODE Trajectory of Diffusion** \
*Dongjun Kim, Chieh-Hsin Lai, Wei-Hsiang Liao, Naoki Murata, Yuhta Takida, Toshimitsu Uesaka, Yutong He, Yuki Mitsufuji, Stefano Ermon* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.02279)] \
1 Oct 2023

**Completing Visual Objects via Bridging Generation and Segmentation** \
*Xiang Li, Yinpeng Chen, Chung-Ching Lin, Rita Singh, Bhiksha Raj, Zicheng Liu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.00808)] \
1 Oct 2023

**Decoding Realistic Images from Brain Activity with Contrastive Self-supervision and Latent Diffusion** \
*Jingyuan Sun, Mingxiao Li, Marie-Francine Moens* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.00318)] \
30 Sep 2023

**FashionFlow: Leveraging Diffusion Models for Dynamic Fashion Video Synthesis from Static Imagery** \
*Tasin Islam, Alina Miron, XiaoHui Liu, Yongmin Li* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.00106)] \
29 Sep 2023

**Denoising Diffusion Bridge Models** \
*Linqi Zhou, Aaron Lou, Samar Khanna, Stefano Ermon* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.16948)] \
29 Sep 2023


**DeeDiff: Dynamic Uncertainty-Aware Early Exiting for Accelerating Diffusion Model Generation** \
*Shengkun Tang, Yaqing Wang, Caiwen Ding, Yi Liang, Yao Li, Dongkuan Xu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.17074)] \
29 Sep 2023


**Distilling ODE Solvers of Diffusion Models into Smaller Steps** \
*Sanghwan Kim, Hao Tang, Fisher Yu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.16421)] \
28 Sep 2023

**Factorized Diffusion Architectures for Unsupervised Image Generation and Segmentation** \
*Xin Yuan, Michael Maire* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.15726)] \
27 Sep 2023

**Generative Escher Meshes** \
*Noam Aigerman, Thibault Groueix* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.14564)] \
25 Sep 2023

**Soft Mixture Denoising: Beyond the Expressive Bottleneck of Diffusion Models** \
*Yangming Li, Boris van Breugel, Mihaela van der Schaar* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.14068)] \
25 Sep 2023

**GLOBER: Coherent Non-autoregressive Video Generation via GLOBal Guided Video DecodER** \
*Mingzhen Sun, Weining Wang, Zihan Qin, Jiahui Sun, Sihan Chen, Jing Liu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.13274)] [[Github](https://github.com/iva-mzsun/glober)] \
23 Sep 2023

**Score Mismatching for Generative Modeling** \
*Senmao Ye, Fei Liu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.11043)] \
20 Sep 2023

**Generalised Probabilistic Diffusion Scale-Spaces** \
*Pascal Peter* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.08511)] \
15 Sep 2023

**Generative Image Dynamics** \
*Zhengqi Li, Richard Tucker, Noah Snavely, Aleksander Holynski* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.07906)] [[Project](https://generative-dynamics.github.io/)] \
14 Sep 2023

**Beta Diffusion** \
*Mingyuan Zhou, Tianqi Chen, Zhendong Wang, Huangjie Zheng* \
NeurIPS 2023. [[Paper](https://arxiv.org/abs/2309.07867)] \
14 Sep 2023

**Adapt and Diffuse: Sample-adaptive Reconstruction via Latent Diffusion Models** \
*Zalan Fabian, Berk Tinaz, Mahdi Soltanolkotabi* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.06642)] \
12 Sep 2023

**Elucidating the solution space of extended reverse-time SDE for diffusion models** \
*Qinpeng Cui, Xinyi Zhang, Zongqing Lu, Qingmin Liao* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.06169)] \
12 Sep 2023


**Learning Energy-Based Models by Cooperative Diffusion Recovery Likelihood** \
*Yaxuan Zhu, Jianwen Xie, Yingnian Wu, Ruiqi Gao* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.05153)] \
10 Sep 2023

**Relay Diffusion: Unifying diffusion process across resolutions for image synthesis** \
*Jiayan Teng, Wendi Zheng, Ming Ding, Wenyi Hong, Jianqiao Wangni, Zhuoyi Yang, Jie Tang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.03350)] \
4 Sep 2023

**Gradient Domain Diffusion Models for Image Synthesis** \
*Yuanhao Gong* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.01875)] \
5 Sep 2023


**Hierarchical Masked 3D Diffusion Model for Video Outpainting** \
*Fanda Fan, Chaoxu Guo, Litong Gong, Biao Wang, Tiezheng Ge, Yuning Jiang, Chunjie Luo, Jianfeng Zhan* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.02119)] [[Github](https://fanfanda.github.io/M3DDM/)] \
5 Sep 2023

**Diffusion Models with Deterministic Normalizing Flow Priors** \
*Mohsen Zand, Ali Etemad, Michael Greenspan* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2309.01274)] [[Github](https://github.com/MohsenZand/DiNof)] \
3 Sep 2023

**Diffusion Inertial Poser: Human Motion Reconstruction from Arbitrary Sparse IMU Configurations** \
*Tom Van Wouwe, Seunghwan Lee, Antoine Falisse, Scott Delp, C. Karen Liu* \
AAAI 2024. [[Paper](https://arxiv.org/abs/2308.16682)] \
31 Aug 2023

**Conditioning Score-Based Generative Models by Neuro-Symbolic Constraints** \
*Davide Scassola, Sebastiano Saccani, Ginevra Carbone, Luca Bortolussi* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.16534)] \
31 Aug 2023

**Elucidating the Exposure Bias in Diffusion Models** \
*Mang Ning, Mingxiao Li, Jianlin Su, Albert Ali Salah, Itir Onal Ertugrul* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.15321)] \
29 Aug 2023

**Residual Denoising Diffusion Models** \
*Jiawei Liu, Qiang Wang, Huijie Fan, Yinong Wang, Yandong Tang, Liangqiong Qu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.13712)] [[Github](https://github.com/nachifur/RDDM)] \
25 Aug 2023

**Efficient Transfer Learning in Diffusion Models via Adversarial Noise** \
*Xiyu Wang, Baijiong Lin, Daochang Liu, Chang Xu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.11948)] \
23 Aug 2023

**Boosting Diffusion Models with an Adaptive Momentum Sampler** \
*Xiyu Wang, Anh-Dung Dinh, Daochang Liu, Chang Xu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.11941)] \
23 Aug 2023

**Make-It-4D: Synthesizing a Consistent Long-Term Dynamic Scene Video from a Single Image** \
*Liao Shen, Xingyi Li, Huiqiang Sun, Juewen Peng, Ke Xian, Zhiguo Cao, Guosheng Lin* \
ACM MM 2023. [[Paper](https://arxiv.org/abs/2308.10257)] \
20 Aug 2023

**Spiking-Diffusion: Vector Quantized Discrete Diffusion Model with Spiking Neural Networks** \
*Mingxuan Liu, Rui Wen, Hong Chen* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.10187)] \
20 Aug 2023

**SciRE-Solver: Efficient Sampling of Diffusion Probabilistic Models by Score-integrand Solver with Recursive Derivative Estimation** \
*Shigui Li, Wei Chen, Delu Zeng* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.07896)] \
15 Aug 2023

**Improved Order Analysis and Design of Exponential Integrator for Diffusion Models Sampling** \
*Qinsheng Zhang, Jiaming Song, Yongxin Chen* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.02157)] \
4 Aug 2023

**Patched Denoising Diffusion Models For High-Resolution Image Synthesis** \
*Zheng Ding, Mengqi Zhang, Jiajun Wu, Zhuowen Tu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2308.01316)] \
2 Aug 2023

**Spatial-Frequency U-Net for Denoising Diffusion Probabilistic Models** \
*Xin Yuan, Linjie Li, Jianfeng Wang, Zhengyuan Yang, Kevin Lin, Zicheng Liu, Lijuan Wang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.14648)] \
27 Jul 2023

**Synthesis of Batik Motifs using a Diffusion -- Generative Adversarial Network** \
*One Octadion, Novanto Yudistira, Diva Kurnianingtyas* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.12122)] \
22 Jul 2023

**DPM-OT: A New Diffusion Probabilistic Model Based on Optimal Transport** \
*Zezeng Li, ShengHao Li, Zhanpeng Wang, Na Lei, Zhongxuan Luo, Xianfeng Gu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.11308)] [[Github](https://github.com/cognaclee/DPM-OT)] \
21 Jul 2023

**Diffusion Sampling with Momentum for Mitigating Divergence Artifacts** \
*Suttisak Wizadwongsa, Worameth Chinchuthakun, Pramook Khungurn, Amit Raj, Supasorn Suwajanakorn* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.11118)] \
20 Jul 2023

**Flow Matching in Latent Space** \
*Quan Dao, Hao Phung, Binh Nguyen, Anh Tran* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.08698)] [[Project](https://vinairesearch.github.io/LFM/)] \
17 Jul 2023

**Manifold-Guided Sampling in Diffusion Models for Unbiased Image Generation** \
*Xingzhe Su, Wenwen Qiang, Zeen Song, Hang Gao, Fengge Wu, Changwen Zheng* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.08199)] \
17 Jul 2023

**Complexity Matters: Rethinking the Latent Space for Generative Modeling** \
*Tianyang Hu, Fei Chen, Haonan Wang, Jiawei Li, Wenjia Wang, Jiacheng Sun, Zhenguo Li* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.08283)] \
17 Jul 2023

**Collaborative Score Distillation for Consistent Visual Synthesis** \
*Subin Kim, Kyungmin Lee, June Suk Choi, Jongheon Jeong, Kihyuk Sohn, Jinwoo Shin* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.04787)] [[Project](https://subin-kim-cv.github.io/CSD/)] [[Github](https://github.com/subin-kim-cv/CSD)] \
4 Jul 2023

**ProtoDiffusion: Classifier-Free Diffusion Guidance with Prototype Learning** \
*Gulcin Baykal, Halil Faruk Karagoz, Taha Binhuraib, Gozde Unal* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.01924)] \
4 Jul 2023

**SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis** \
*Dustin Podell, Zion English, Kyle Lacey, Andreas Blattmann, Tim Dockhorn, Jonas Müller, Joe Penna, Robin Rombach* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.01952)] [[Github](https://github.com/Stability-AI/generative-models)] \
4 Jul 2023

**Bidirectional Temporal Diffusion Model for Temporally Consistent Human Animation** \
*Tserendorj Adiya, Sanghun Kim, Jung Eun Lee, Jae Shin Yoon, Hwasup Lim* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2307.00574)] \
2 Jul 2023


**Spiking Denoising Diffusion Probabilistic Models** \
*Jiahang Cao, Ziqing Wang, Hanzhong Guo, Hao Cheng, Qiang Zhang, Renjing Xu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.17046)] \
29 Jun 2023

**DomainStudio: Fine-Tuning Diffusion Models for Domain-Driven Image Generation using Limited Data** \
*Jingyuan Zhu, Huimin Ma, Jiansheng Chen, Jian Yuan* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.14153)] \
25 Jun 2023

**Decoupled Diffusion Models with Explicit Transition Probability** \
*Yuhang Huang, Zheng Qin, Xinwang Liu, Kai Xu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.13720)] \
23 Jun 2023

**Continuous Layout Editing of Single Images with Diffusion Models** \
*Zhiyuan Zhang, Zhitong Huang, Jing Liao* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.13078)] \
22 Jun 2023

**Semi-Implicit Denoising Diffusion Models (SIDDMs)** \
*Yanwu Xu, Mingming Gong, Shaoan Xie, Wei Wei, Matthias Grundmann, kayhan Batmanghelich, Tingbo Hou* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.12511)] \
21 Jun 2023

**Eliminating Lipschitz Singularities in Diffusion Models** \
*Zhantao Yang, Ruili Feng, Han Zhang, Yujun Shen, Kai Zhu, Lianghua Huang, Yifei Zhang, Yu Liu, Deli Zhao, Jingren Zhou, Fan Cheng* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.11251)] \
20 Jun 2023

**GD-VDM: Generated Depth for better Diffusion-based Video Generation** \
*Ariel Lapid, Idan Achituve, Lior Bracha, Ethan Fetaya* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.11173)] \
19 Jun 2023

**Image Harmonization with Diffusion Model** \
*Jiajie Li, Jian Wang, Chen Wang, Jinjun Xiong* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.10441)] \
17 Jun 2023


**Training Diffusion Classifiers with Denoising Assistance** \
*Chandramouli Sastry, Sri Harsha Dumpala, Sageev Oore* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.09192)] \
15 Jun 2023


**Conditional Human Sketch Synthesis with Explicit Abstraction Control** \
*Dar-Yen Chen* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.09274)] \
15 Jun 2023

**Fast Training of Diffusion Models with Masked Transformers** \
*Hongkai Zheng, Weili Nie, Arash Vahdat, Anima Anandkumar* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.09305)] [[Github](https://github.com/Anima-Lab/MaskDiT)] \
15 Jun 2023


**Relation-Aware Diffusion Model for Controllable Poster Layout Generation** \
*Fengheng Li, An Liu, Wei Feng, Honghe Zhu, Yaoyu Li, Zheng Zhang, Jingjing Lv, Xin Zhu, Junjie Shen, Zhangang Lin, Jingping Shao* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.09086)] \
15 Jun 2023

**OMS-DPM: Optimizing the Model Schedule for Diffusion Probabilistic Models** \
*Enshu Liu, Xuefei Ning, Zinan Lin, Huazhong Yang, Yu Wang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.08860)] \
15 Jun 2023


**DORSal: Diffusion for Object-centric Representations of Scenes $\textit{et al.}$** \
*Allan Jabri, Sjoerd van Steenkiste, Emiel Hoogeboom, Mehdi S. M. Sajjadi, Thomas Kipf* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.08068)] \
13 Jun 2023


**Fast Diffusion Model** \
*Zike Wu, Pan Zhou, Kenji Kawaguchi, Hanwang Zhang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.06991)] [[Github](https://github.com/sail-sg/FDM)] \
12 Jun 2023

**ADDP: Learning General Representations for Image Recognition and Generation with Alternating Denoising Diffusion Process** \
*Changyao Tian, Chenxin Tao, Jifeng Dai, Hao Li, Ziheng Li, Lewei Lu, Xiaogang Wang, Hongsheng Li, Gao Huang, Xizhou Zhu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.05423)] \
8 Jun 2023

**Multi-Architecture Multi-Expert Diffusion Models** \
*Yunsung Lee, Jin-Young Kim, Hyojun Go, Myeongho Jeong, Shinhyeok Oh, Seungtaek Choi* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.04990)] \
8 Jun 2023

**Interpreting and Improving Diffusion Models Using the Euclidean Distance Function** \
*Frank Permenter, Chenyang Yuan* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.04848)] \
8 Jun 2023

**Video Diffusion Models with Local-Global Context Guidance** \
*Siyuan Yang, Lu Zhang, Yu Liu, Zhizhuo Jiang, You He* \
IJCAI 2023. [[Paper](https://arxiv.org/abs/2306.02562)] [[Github](https://github.com/exisas/LGC-VD)] \
5 Jun 2023

**Brain Diffusion for Visual Exploration: Cortical Discovery using Large Scale Generative Models** \
*Andrew F. Luo, Margaret M. Henderson, Leila Wehbe, Michael J. Tarr* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.03089)] \
5 Jun 2023

**Faster Training of Diffusion Models and Improved Density Estimation via Parallel Score Matching** \
*Etrit Haxholli, Marco Lorenzi* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.02658)] \
5 Jun 2023

**Temporal Dynamic Quantization for Diffusion Models** \
*Junhyuk So, Jungwon Lee, Daehyun Ahn, Hyungjun Kim, Eunhyeok Park* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.02316)] \
4 Jun 2023

**Conditional Generation from Unconditional Diffusion Models using Denoiser Representations** \
*Alexandros Graikos, Srikar Yellapragada, Dimitris Samaras* \
BMVC 2023. [[Paper](https://arxiv.org/abs/2306.01900)] [[Github](https://github.com/cvlab-stonybrook/fewshot-conditional-diffusion)] \
2 Jun 2023

**Conditioning Diffusion Models via Attributes and Semantic Masks for Face Generation** \
*Nico Giambi, Giuseppe Lisanti* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.00914)] \
1 Jun 2023

**Differential Diffusion: Giving Each Pixel Its Strength** \
*Eran Levin, Ohad Fried* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.00950)] \
1 Jun 2023


**Addressing Discrepancies in Semantic and Visual Alignment in Neural Networks** \
*Natalie Abreu, Nathan Vaska, Victoria Helus* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.01148)] \
1 Jun 2023


**Addressing Negative Transfer in Diffusion Models** \
*Hyojun Go, JinYoung Kim, Yunsung Lee, Seunghyun Lee, Shinhyeok Oh, Hyeongdon Moon, Seungtaek Choi* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2306.00354)] \
1 Jun 2023

**A Geometric Perspective on Diffusion Models** \
*Defang Chen, Zhenyu Zhou, Jian-Ping Mei, Chunhua Shen, Chun Chen, Can Wang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.19947)] \
31 May 2023



**Spontaneous symmetry breaking in generative diffusion models** \
*Gabriel Raya, Luca Ambrogioni* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.19693)] \
31 May 2023

**Perturbation-Assisted Sample Synthesis: A Novel Approach for Uncertainty Quantification** \
*Yifei Liu, Rex Shen, Xiaotong Shen* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.18671)] \
30 May 2023

**One-Line-of-Code Data Mollification Improves Optimization of Likelihood-based Generative Models** \
*Ba-Hien Tran, Giulio Franzese, Pietro Michiardi, Maurizio Filippone* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.18900)] \
30 May 2023

**Ambient Diffusion: Learning Clean Distributions from Corrupted Data** \
*Giannis Daras, Kulin Shah, Yuval Dagan, Aravind Gollakota, Alexandros G. Dimakis, Adam Klivans* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.19256)] \
30 May 2023

**Towards Accurate Data-free Quantization for Diffusion Models** \
*Changyuan Wang, Ziwei Wang, Xiuwei Xu, Yansong Tang, Jie Zhou, Jiwen Lu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.18723)] \
30 May 2023

**BRIGHT: Bi-level Feature Representation of Image Collections using Groups of Hash Tables** \
*Dingdong Yang, Yizhi Wang, Ali Mahdavi-Amiri, Hao Zhang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.18601)] [[Project](https://bright-project01.github.io/)] \
29 May 2023

**Diff-Instruct: A Universal Approach for Transferring Knowledge From Pre-trained Diffusion Models** \
*Weijian Luo, Tianyang Hu, Shifeng Zhang, Jiacheng Sun, Zhenguo Li, Zhihua Zhang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.18455)] \
29 May 2023

**Learning to Jump: Thinning and Thickening Latent Counts for Generative Modeling** \
*Tianqi Chen, Mingyuan Zhou* \
ICML 2023. [[Paper](https://arxiv.org/abs/2305.18375)] [[Github](https://github.com/tqch/poisson-jump)] \
28 May 2023

**Reconstructing the Mind's Eye: fMRI-to-Image with Contrastive Learning and Diffusion Priors** \
*Paul S. Scotti, Atmadeep Banerjee, Jimmie Goode, Stepan Shabalin, Alex Nguyen, Ethan Cohen, Aidan J. Dempster, Nathalie Verlinde, Elad Yundler, David Weisberg, Kenneth A. Norman, Tanishq Mathew Abraham* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.18274)] [[Github](https://medarc-ai.github.io/mindeye/)] \
29 May 2023

**Contrast, Attend and Diffuse to Decode High-Resolution Images from Brain Activities** \
*Jingyuan Sun, Mingxiao Li, Zijiao Chen, Yunhao Zhang, Shaonan Wang, Marie-Francine Moens* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.17214)] \
26 May 2023

**Parallel Sampling of Diffusion Models** \
*Andy Shih, Suneel Belkhale, Stefano Ermon, Dorsa Sadigh, Nima Anari* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.16317)] [[Github](https://github.com/AndyShih12/paradigms)] \
25 May 2023

**Trans-Dimensional Generative Modeling via Jump Diffusion Models** \
*Andrew Campbell, William Harvey, Christian Weilbach, Valentin De Bortoli, Tom Rainforth, Arnaud Doucet* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.16261)] \
25 May 2023

**UDPM: Upsampling Diffusion Probabilistic Models** \
*Shady Abu-Hussein, Raja Giryes* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.16269)] \
25 May 2023


**Unifying GANs and Score-Based Diffusion as Generative Particle Models** \
*Jean-Yves Franceschi, Mike Gartrell, Ludovic Dos Santos, Thibaut Issenhuth, Emmanuel de Bézenac, Mickaël Chen, Alain Rakotomamonjy* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.16150)] \
25 May 2023

**DuDGAN: Improving Class-Conditional GANs via Dual-Diffusion** \
*Taesun Yeom, Minhyeok Lee* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.14849)] \
24 May 2023

**Alleviating Exposure Bias in Diffusion Models through Sampling with Shifted Time Steps** \
*Mingxiao Li, Tingyu Qu, Wei Sun, Marie-Francine Moens* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.15583)] \
24 May 2023


**Robust Classification via a Single Diffusion Model** \
*Huanran Chen, Yinpeng Dong, Zhengyi Wang, Xiao Yang, Chengqi Duan, Hang Su, Jun Zhu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.15241)] \
24 May 2023

**On the Generalization of Diffusion Model** \
*Mingyang Yi, Jiacheng Sun, Zhenguo Li* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.14712)] \
24 May 2023

**VDT: An Empirical Study on Video Diffusion with Transformers** \
*Haoyu Lu, Guoxing Yang, Nanyi Fei, Yuqi Huo, Zhiwu Lu, Ping Luo, Mingyu Ding* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.13311)] [[Github](https://github.com/RERV/VDT)] \
22 May 2023

**Cinematic Mindscapes: High-quality Video Reconstruction from Brain Activity** \
*Zijiao Chen, Jiaxin Qing, Juan Helen Zhou* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.11675)] [[Project](https://mind-video.com/)] \
19 May 2023

**PTQD: Accurate Post-Training Quantization for Diffusion Models** \
*Yefei He, Luping Liu, Jing Liu, Weijia Wu, Hong Zhou, Bohan Zhuang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.10657)] \
18 May 2023

**Blackout Diffusion: Generative Diffusion Models in Discrete-State Spaces** \
*Javier E Santos, Zachary R. Fox, Nicholas Lubbers, Yen Ting Lin* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.11089)] \
18 May 2023

**Structural Pruning for Diffusion Models** \
*Gongfan Fang, Xinyin Ma, Xinchao Wang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.10924)] [[Github](https://github.com/VainF/Diff-Pruning)] \
18 May 2023


**Catch-Up Distillation: You Only Need to Train Once for Accelerating Sampling** \
*Shitong Shao, Xu Dai, Shouyi Yin, Lujun Li, Huanran Chen, Yang Hu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.10769)] \
18 May 2023

**Controllable Mind Visual Diffusion Model** \
*Bohan Zeng, Shanglin Li, Xuhui Liu, Sicheng Gao, Xiaolong Jiang, Xu Tang, Yao Hu, Jianzhuang Liu, Baochang Zhang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.10135)] \
17 May 2023

**Analyzing Bias in Diffusion-based Face Generation Models** \
*Malsha V. Perera, Vishal M. Patel* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.06402)] \
10 May 2023


**Improved Techniques for Maximum Likelihood Estimation for Diffusion ODEs** \
*Kaiwen Zheng, Cheng Lu, Jianfei Chen, Jun Zhu* \
ICML 2023. [[Paper](https://arxiv.org/abs/2305.03935)] \
6 May 2023

**LEO: Generative Latent Image Animator for Human Video Synthesis** \
*Yaohui Wang, Xin Ma, Xinyuan Chen, Antitza Dantcheva, Bo Dai, Yu Qiao* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.03989)] [[Project](https://wyhsirius.github.io/LEO-project/)] [[Github](https://github.com/wyhsirius/LEO)] \
6 May 2023

**Iterative α-(de)Blending: a Minimalist Deterministic Diffusion Model** \
*Eric Heitz, Laurent Belcour, Thomas Chambon* \
SIGGRAPH 2023. [[Paper](https://arxiv.org/abs/2305.03486)] \
5 May 2023


**Reconstructing seen images from human brain activity via guided stochastic search** \
*Reese Kneeland, Jordyn Ojeda, Ghislain St-Yves, Thomas Naselaris* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2305.00556)] \
30 Apr 2023


**Motion-Conditioned Diffusion Model for Controllable Video Synthesis** \
*Tsai-Shien Chen, Chieh Hubert Lin, Hung-Yu Tseng, Tsung-Yi Lin, Ming-Hsuan Yang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.14404)] [[Project](https://tsaishien-chen.github.io/MCDiff/)] \
27 Apr 2023

**Score-based Generative Modeling Through Backward Stochastic Differential Equations: Inversion and Generation** \
*Zihao Wang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.13224)] \
26 Apr 2023

**Exploring Compositional Visual Generation with Latent Classifier Guidance** \
*Changhao Shi, Haomiao Ni, Kai Li, Shaobo Han, Mingfu Liang, Martin Renqiang Min* \
CVPR Workshop 2023. [[Paper](https://arxiv.org/abs/2304.12536)] \
25 Apr 2023

**Patch Diffusion: Faster and More Data-Efficient Training of Diffusion Models** \
*Zhendong Wang, Yifan Jiang, Huangjie Zheng, Peihao Wang, Pengcheng He, Zhangyang Wang, Weizhu Chen, Mingyuan Zhou* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.12526)] \
25 Apr 2023


**Variational Diffusion Auto-encoder: Deep Latent Variable Model with Unconditional Diffusion Prior** \
*Georgios Batzolis, Jan Stanczuk, Carola-Bibiane Schönlieb* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.12141)] \
24 Apr 2023


**LaMD: Latent Motion Diffusion for Video Generation** \
*Yaosi Hu, Zhenzhong Chen, Chong Luo* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.11603)] \
23 Apr 2023


**Lookahead Diffusion Probabilistic Models for Refining Mean Estimation** \
*Guoqiang Zhang, Niwa Kenta, W. Bastiaan Kleijn* \
CVPR 2023. [[Paper](https://arxiv.org/abs/2304.11312)] [[Github](https://github.com/guoqiang-zhang-x/LA-DPM)] \
22 Apr 2023

**NeuralField-LDM: Scene Generation with Hierarchical Latent Diffusion Models** \
*Seung Wook Kim, Bradley Brown, Kangxue Yin, Karsten Kreis, Katja Schwarz, Daiqing Li, Robin Rombach, Antonio Torralba, Sanja Fidler* \
CVPR 2023. [[Paper](https://arxiv.org/abs/2304.09787)] \
19 Apr 2023

**Attributing Image Generative Models using Latent Fingerprints** \
*Guangyu Nie, Changhoon Kim, Yezhou Yang, Yi Ren* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.09752)] \
17 Apr 2023


**Identity Encoder for Personalized Diffusion** \
*Yu-Chuan Su, Kelvin C.K. Chan, Yandong Li, Yang Zhao, Han Zhang, Boqing Gong, Huisheng Wang, Xuhui Jia* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.07429)] \
14 Apr 2023

**Memory Efficient Diffusion Probabilistic Models via Patch-based Generation** \
*Shinei Arakawa, Hideki Tsunashima, Daichi Horita, Keitaro Tanaka, Shigeo Morishima* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.07087)] \
14 Apr 2023

**DCFace: Synthetic Face Generation with Dual Condition Diffusion Model** \
*Minchul Kim, Feng Liu, Anil Jain, Xiaoming Liu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.07060)] [[Github](https://github.com/mk-minchul/dcface)] \
14 Apr 2023

**DiffFit: Unlocking Transferability of Large Diffusion Models via Simple Parameter-Efficient Fine-Tuning** \
*Enze Xie, Lewei Yao, Han Shi, Zhili Liu, Daquan Zhou, Zhaoqiang Liu, Jiawei Li, Zhenguo Li* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.06648)] \
13 Apr 2023

**RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment** \
*Hanze Dong, Wei Xiong, Deepanshu Goyal, Rui Pan, Shizhe Diao, Jipeng Zhang, Kashun Shum, Tong Zhang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.06767)] \
13 Apr 2023

**DreamPose: Fashion Image-to-Video Synthesis via Stable Diffusion** \
*Johanna Karras, Aleksander Holynski, Ting-Chun Wang, Ira Kemelmacher-Shlizerman* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.06025)] [[Project](https://grail.cs.washington.edu/projects/dreampose/)] [[Github](https://github.com/johannakarras/DreamPose)] \
12 Apr 2023

**Reflected Diffusion Models** \
*Aaron Lou, Stefano Ermon* \
ICML 2023. [[Paper](https://arxiv.org/abs/2304.04740)] [[Project](https://aaronlou.com/blog/2023/reflected-diffusion/)] [[Github](https://github.com/louaaron/Reflected-Diffusion)] \
10 Apr 2023

**Binary Latent Diffusion** \
*Ze Wang, Jiang Wang, Zicheng Liu, Qiang Qiu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.04820)] \
10 Apr 2023


**Diffusion Models as Masked Autoencoders** \
*Chen Wei, Karttikeya Mangalam, Po-Yao Huang, Yanghao Li, Haoqi Fan, Hu Xu, Huiyu Wang, Cihang Xie, Alan Yuille, Christoph Feichtenhofer* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2304.03283)] [[Project](https://weichen582.github.io/diffmae.html)] \
6 Apr 2023

**Few-shot Semantic Image Synthesis with Class Affinity Transfer** \
*Marlène Careil, Jakob Verbeek, Stéphane Lathuilière* \
CVPR 2023. [[Paper](https://arxiv.org/abs/2304.02321)] \
5 Apr 2023


**EGC: Image Generation and Classification via a Diffusion Energy-Based Model** \
*Qiushan Guo, Chuofan Ma, Yi Jiang, Zehuan Yuan, Yizhou Yu, Ping Luo* \
arxiv 2023. [[Paper](https://arxiv.org/abs/2304.02012)] [[Project](https://guoqiushan.github.io/egc.github.io/)] \
4 Apr 2023



**Token Merging for Fast Stable Diffusion** \
*Daniel Bolya, Judy Hoffman* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.17604)] [[Github](https://github.com/dbolya/tomesd)] \
30 Mar 2023

**A Closer Look at Parameter-Efficient Tuning in Diffusion Models** \
*Chendong Xiang, Fan Bao, Chongxuan Li, Hang Su, Jun Zhu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.18181)] \
31 Mar 2023

**-Diff: Infinite Resolution Diffusion with Subsampled Mollified States** \
*Sam Bond-Taylor, Chris G. Willcocks* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.18242)] \
31 Mar 2023

**3D-aware Image Generation using 2D Diffusion Models** \
*Jianfeng Xiang, Jiaolong Yang, Binbin Huang, Xin Tong* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.17905)] [[Project](https://jeffreyxiang.github.io/ivid/)] \
31 Mar 2023

**Consistent View Synthesis with Pose-Guided Diffusion Models** \
*Hung-Yu Tseng, Qinbo Li, Changil Kim, Suhib Alsisan, Jia-Bin Huang, Johannes Kopf* \
CVPR 2023. [[Paper](https://arxiv.org/abs/2303.17598)] \
30 Mar 2023


**DiffCollage: Parallel Generation of Large Content with Diffusion Models** \
*Qinsheng Zhang, Jiaming Song, Xun Huang, Yongxin Chen, Ming-Yu Liu* \
CVPR 2023. [[Paper](https://arxiv.org/abs/2303.17076)] [[Project](https://research.nvidia.com/labs/dir/diffcollage/)] \
30 Mar 2023

**Masked Diffusion Transformer is a Strong Image Synthesizer** \
*Shanghua Gao, Pan Zhou, Ming-Ming Cheng, Shuicheng Yan* \
arXiv 2023.  [[Paper](https://arxiv.org/abs/2303.14389)] [[Github](https://github.com/sail-sg/MDT)] \
25 Mar 2023

**Conditional Image-to-Video Generation with Latent Flow Diffusion Models** \
*Haomiao Ni, Changhao Shi, Kai Li, Sharon X. Huang, Martin Renqiang Min* \
CVPR 2023. [[Paper](https://arxiv.org/abs/2303.13744)] [[Github](https://github.com/nihaomiao/CVPR23_LFDM)] \
24 Mar 2023

**NUWA-XL: Diffusion over Diffusion for eXtremely Long Video Generation** \
*Shengming Yin, Chenfei Wu, Huan Yang, Jianfeng Wang, Xiaodong Wang, Minheng Ni, Zhengyuan Yang, Linjie Li, Shuguang Liu, Fan Yang, Jianlong Fu, Gong Ming, Lijuan Wang, Zicheng Liu, Houqiang Li, Nan Duan* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.12346)] [[Project](https://msra-nuwa.azurewebsites.net/#/)] \
22 Mar 2023

**Object-Centric Slot Diffusion** \
*Jindong Jiang, Fei Deng, Gautam Singh, Sungjin Ahn* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.10834)] \
20 Mar 2023


**LDMVFI: Video Frame Interpolation with Latent Diffusion Models** \
*Duolikun Danier, Fan Zhang, David Bull* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.09508)] \
16 Mar 2023

**Efficient Diffusion Training via Min-SNR Weighting Strategy** \
*Tiankai Hang, Shuyang Gu, Chen Li, Jianmin Bao, Dong Chen, Han Hu, Xin Geng, Baining Guo* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.09556)] \
16 Mar 2023

**VideoFusion: Decomposed Diffusion Models for High-Quality Video Generation** \
CVPR 2023. [[Paper](https://arxiv.org/abs/2303.08320)] \
15 Mar 2023

**Interpretable ODE-style Generative Diffusion Model via Force Field Construction** \
*Weiyang Jin, Yongpei Zhu, Yuxi Peng* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.08063)] \
14 Mar 2023

**Regularized Vector Quantization for Tokenized Image Synthesis** \
*Jiahui Zhang, Fangneng Zhan, Christian Theobalt, Shijian Lu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.06424)] \
11 Mar 2023


**PARASOL: Parametric Style Control for Diffusion Image Synthesis** \
*Gemma Canet Tarrés, Dan Ruta, Tu Bui, John Collomosse* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.06464)] \
11 Mar 2023

**Brain-Diffuser: Natural scene reconstruction from fMRI signals using generative latent diffusion** \
*Furkan Ozcelik, Rufin VanRullen* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.05334)] \
9 Mar 2023

**Multilevel Diffusion: Infinite Dimensional Score-Based Diffusion Models for Image Generation** \
*Paul Hagemann, Lars Ruthotto, Gabriele Steidl, Nicole Tianjiao Yang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.04772)] \
8 Mar 2023


**TRACT: Denoising Diffusion Models with Transitive Closure Time-Distillation** \
*David Berthelot, Arnaud Autef, Jierui Lin, Dian Ang Yap, Shuangfei Zhai, Siyuan Hu, Daniel Zheng, Walter Talbott, Eric Gu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.04248)] \
7 Mar 2023

**Generative Diffusions in Augmented Spaces: A Complete Recipe** \
*Kushagra Pandey, Stephan Mandt* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.01748)] \
3 Mar 2023

**Consistency Models** \
*Yang Song, Prafulla Dhariwal, Mark Chen, Ilya Sutskever* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.01469)] \
2 Mar 2023

**Diffusion Probabilistic Fields** \
*Peiye Zhuang, Samira Abnar, Jiatao Gu, Alex Schwing, Joshua M. Susskind, Miguel Ángel Bautista* \
ICLR 2023. [[Paper](https://arxiv.org/abs/2303.00165)] \
1 Mar 2023

**Unsupervised Discovery of Semantic Latent Directions in Diffusion Models** \
*Yong-Hyun Park, Mingi Kwon, Junghyo Jo, Youngjung Uh* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.12469)] \
24 Feb 2023

**Reduce, Reuse, Recycle: Compositional Generation with Energy-Based Diffusion Models and MCMC** \
*Yilun Du, Conor Durkan, Robin Strudel, Joshua B. Tenenbaum, Sander Dieleman, Rob Fergus, Jascha Sohl-Dickstein, Arnaud Doucet, Will Grathwohl* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.11552)] [[Project](https://energy-based-model.github.io/reduce-reuse-recycle/)] \
22 Feb 2023

**Learning 3D Photography Videos via Self-supervised Diffusion on Single Images** \
*Xiaodong Wang, Chenfei Wu, Shengming Yin, Minheng Ni, Jianfeng Wang, Linjie Li, Zhengyuan Yang, Fan Yang, Lijuan Wang, Zicheng Liu, Yuejian Fang, Nan Duan* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.10781)] \
21 Feb 2023

**On Calibrating Diffusion Probabilistic Models** \
*Tianyu Pang, Cheng Lu, Chao Du, Min Lin, Shuicheng Yan, Zhijie Deng* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.10688)] [[Github](https://github.com/thudzj/Calibrated-DPMs)] \
21 Feb 2023

**Diffusion Models and Semi-Supervised Learners Benefit Mutually with Few Labels** \
*Zebin You, Yong Zhong, Fan Bao, Jiacheng Sun, Chongxuan Li, Jun Zhu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.10586)] \
21 Feb 2023

**Cross-domain Compositing with Pretrained Diffusion Models** \
*Roy Hachnochi, Mingrui Zhao, Nadav Orzech, Rinon Gal, Ali Mahdavi-Amiri, Daniel Cohen-Or, Amit Haim Bermano* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.10167)] [[Github](https://github.com/cross-domain-compositing/cross-domain-compositing)] \
20 Feb 2023



**Restoration based Generative Models** \
*Jaemoo Choi, Yesom Park, Myungjoo Kang* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.05456)] \
20 Feb 2023



**Consistent Diffusion Models: Mitigating Sampling Drift by Learning to be Consistent** \
*Giannis Daras, Yuval Dagan, Alexandros G. Dimakis, Constantinos Daskalakis* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.09057)] [[Github](https://github.com/giannisdaras/cdm)] \
17 Feb 2023

**LayoutDiffuse: Adapting Foundational Diffusion Models for Layout-to-Image Generation** \
*Jiaxin Cheng, Xiao Liang, Xingjian Shi, Tong He, Tianjun Xiao, Mu Li* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.08908)] \
16 Feb 2023

**Video Probabilistic Diffusion Models in Projected Latent Space** \
*Sihyun Yu, Kihyuk Sohn, Subin Kim, Jinwoo Shin* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.07685)] [[Github](https://sihyun.me/PVDM/)] \
15 Feb 2023

**DiffFaceSketch: High-Fidelity Face Image Synthesis with Sketch-Guided Latent Diffusion Model** \
*Yichen Peng, Chunqi Zhao, Haoran Xie, Tsukasa Fukusato, Kazunori Miyata* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.06908)] \
14 Feb 2023

**Where to Diffuse, How to Diffuse, and How to Get Back: Automated Learning for Multivariate Diffusions** \
*Raghav Singhal, Mark Goldstein, Rajesh Ranganath* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.07261)] \
14 Feb 2023


**Preconditioned Score-based Generative Models** \
*Li Zhang, Hengyuan Ma, Xiatian Zhu, Jianfeng Feng* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.06504)] [Github](https://github.com/fudan-zvg/PDS)] \
13 Feb 2023

**Star-Shaped Denoising Diffusion Probabilistic Models** \
*Andrey Okhotin, Dmitry Molchanov, Vladimir Arkhipkin, Grigory Bartosh, Aibek Alanov, Dmitry Vetrov* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.05259)] \
10 Feb 2023 


**UniPC: A Unified Predictor-Corrector Framework for Fast Sampling of Diffusion Models** \
*Wenliang Zhao, Lujia Bai, Yongming Rao, Jie Zhou, Jiwen Lu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.04867)] [[Project](https://unipc.ivg-research.xyz)] [[Github](https://github.com/wl-zhao/UniPC)] \
9 Feb 2023

**Geometry of Score Based Generative Models** \
*Sandesh Ghimire, Jinyang Liu, Armand Comas, Davin Hill, Aria Masoomi, Octavia Camps, Jennifer Dy* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.04411)] \
9 Feb 2023

**Q-Diffusion: Quantizing Diffusion Models** \
*Xiuyu Li, Long Lian, Yijiang Liu, Huanrui Yang, Zhen Dong, Daniel Kang, Shanghang Zhang, Kurt Keutzer* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.04304)] \
8 Feb 2023

**PFGM++: Unlocking the Potential of Physics-Inspired Generative Models** \
*Yilun Xu, Ziming Liu, Yonglong Tian, Shangyuan Tong, Max Tegmark, Tommi Jaakkola* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.04265)] [[Github](https://github.com/Newbeeer/pfgmpp)] \
8 Feb 2023

**Long Horizon Temperature Scaling** \
*Andy Shih, Dorsa Sadigh, Stefano Ermon* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.03686)] \
7 Feb 2023

**Spatial Functa: Scaling Functa to ImageNet Classification and Generation** \
*Matthias Bauer, Emilien Dupont, Andy Brock, Dan Rosenbaum, Jonathan Schwarz, Hyunjik Kim* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.03130)] \
6 Feb 2023

**ShiftDDPMs: Exploring Conditional Diffusion Models by Shifting Diffusion Trajectories** \
*Zijian Zhang, Zhou Zhao, Jun Yu, Qi Tian* \
AAAI 2023. [[Paper](https://arxiv.org/abs/2302.02373)] \
5 Feb 2023

**Divide and Compose with Score Based Generative Models** \
*Sandesh Ghimire, Armand Comas, Davin Hill, Aria Masoomi, Octavia Camps, Jennifer Dy* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.02272)] [[Github](https://github.com/sandeshgh/Score-based-disentanglement)] \
5 Feb 2023


**Stable Target Field for Reduced Variance Score Estimation in Diffusion Models** \
*Yilun Xu, Shangyuan Tong, Tommi Jaakkola* \
ICLR 2023. [[Paper](https://arxiv.org/abs/2302.00670)] [[Github](https://github.com/Newbeeer/stf)] \
1 Feb 2023

**DisDiff: Unsupervised Disentanglement of Diffusion Probabilistic Models** \
*Tao Yang, Yuwang Wang, Yan Lv, Nanning Zheng* \
NeurIPS 2023. [[Paper](https://arxiv.org/abs/2301.13721)] \
31 Jan 2023


**Optimizing DDPM Sampling with Shortcut Fine-Tuning** \
*Ying Fan, Kangwook Lee* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2301.13362)] \
31 Jan 2023

**Learning Data Representations with Joint Diffusion Models** \
*Kamil Deja, Tomasz Trzcinski, Jakub M. Tomczak* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2301.13622)] \
31 Jan 2023

**ERA-Solver: Error-Robust Adams Solver for Fast Sampling of Diffusion Probabilistic Models** \
*Shengmeng Li, Luping Liu, Zenghao Chai, Runnan Li, Xu Tan* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2301.12935)] \
30 Jan 2023

**Don't Play Favorites: Minority Guidance for Diffusion Models** \
*Soobin Um, Jong Chul Ye* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2301.12334)] [[Github](https://github.com/sangyun884/fast-ode)] \
29 Jan 2023

**Accelerating Guided Diffusion Sampling with Splitting Numerical Methods** \
*Suttisak Wizadwongsa, Supasorn Suwajanakorn* \
ICLR 2023. [[Paper](https://arxiv.org/abs/2301.11558)] \
27 Jan 2023

**Input Perturbation Reduces Exposure Bias in Diffusion Models** \
*Mang Ning, Enver Sangineto, Angelo Porrello, Simone Calderara, Rita Cucchiara* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2301.11706)] [[Github](https://github.com/forever208/DDPM-IP)] \
27 Jan 2023

**Minimizing Trajectory Curvature of ODE-based Generative Models** \
*Sangyun Lee, Beomsu Kim, Jong Chul Ye* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2301.12003)] \
27 Jan 2023


**On the Importance of Noise Scheduling for Diffusion Models** \
*Ting Chen* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2301.10972)] \
26 Jan 2023

**simple diffusion: End-to-end diffusion for high resolution images** \
*Emiel Hoogeboom, Jonathan Heek, Tim Salimans* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2301.11093)] \
26 Jan 2023

**Fast Inference in Denoising Diffusion Models via MMD Finetuning** \
*Emanuele Aiello, Diego Valsesia, Enrico Magli* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2301.07969)] [[Github](https://github.com/diegovalsesia/MMD-DDM)] \
19 Jan 2023

**Exploring Transformer Backbones for Image Diffusion Models** \
*Princy Chahal* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.14678)] \
27 Dec 2022

**Unsupervised Representation Learning from Pre-trained Diffusion Probabilistic Models** \
*Zijian Zhang, Zhou Zhao, Zhijie Lin* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.12990)] \
26 Dec 2022


**Scalable Adaptive Computation for Iterative Generation** \
*Allan Jabri, David Fleet, Ting Chen* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.11972)] \
22 Dec 2022

**Hierarchically branched diffusion models for efficient and interpretable multi-class conditional generation** \
*Alex M. Tseng, Tommaso Biancalani, Max Shen, Gabriele Scalia* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.10777)] \
21 Dec 2022


**MM-Diffusion: Learning Multi-Modal Diffusion Models for Joint Audio and Video Generation** \
*Ludan Ruan, Yiyang Ma, Huan Yang, Huiguo He, Bei Liu, Jianlong Fu, Nicholas Jing Yuan, Qin Jin, Baining Guo* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.09478)] [[Github](https://github.com/researchmm/MM-Diffusion)] \
19 Dec 2022


**Scalable Diffusion Models with Transformers** \
*William Peebles, Saining Xie* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.09748)] [[Project](https://www.wpeebles.com/DiT)] [[Github](https://github.com/facebookresearch/DiT)] \
19 Dec 2022


**DAG: Depth-Aware Guidance with Denoising Diffusion Probabilistic Models** \
*Gyeongnyeon Kim, Wooseok Jang, Gyuseong Lee, Susung Hong, Junyoung Seo, Seungryong Kim* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.08861)] [[Project](https://ku-cvlab.github.io/DAG/)] \
17 Dec 2022


**Towards Practical Plug-and-Play Diffusion Models** \
*Hyojun Go, Yunsung Lee, Jin-Young Kim, Seunghyun Lee, Myeongho Jeong, Hyun Seung Lee, Seungtaek Choi* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.05973)] \
12 Dec 2022

**Semantic Brain Decoding: from fMRI to conceptually similar image reconstruction of visual stimuli** \
*Matteo Ferrante, Tommaso Boccato, Nicola Toschi* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.06726)] \
13 Dec 2022

**MAGVIT: Masked Generative Video Transformer** \
*Lijun Yu, Yong Cheng, Kihyuk Sohn, José Lezama, Han Zhang, Huiwen Chang, Alexander G. Hauptmann, Ming-Hsuan Yang, Yuan Hao, Irfan Essa, Lu Jiang* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.05199)] [Project](https://magvit.cs.cmu.edu/)] \
10 Dec 2022

**Diffusion Video Autoencoders: Toward Temporally Consistent Face Video Editing via Disentangled Video Encoding** \
*Gyeongman Kim, Hajin Shim, Hyunsu Kim, Yunjey Choi, Junho Kim, Eunho Yang* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.02802)] \
6 Dec 2022

**Fine-grained Image Editing by Pixel-wise Guidance Using Diffusion Models** \
*Naoki Matsunaga, Masato Ishii, Akio Hayakawa, Kenji Suzuki, Takuya Narihira* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.02024)] \
5 Dec 2022


**VIDM: Video Implicit Diffusion Models** \
*Kangfu Mei, Vishal M. Patel* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.00235)] [[Project](https://kfmei.page/vidm/)] [[Github](https://github.com/MKFMIKU/VIDM)] \
1 Dec 2022

**Why Are Conditional Generative Models Better Than Unconditional Ones?** \
*Fan Bao, Chongxuan Li, Jiacheng Sun, Jun Zhu* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2212.00362)] \
1 Dec 2022


**High-Fidelity Guided Image Synthesis with Latent Diffusion Models** \
*Jaskirat Singh, Stephen Gould, Liang Zheng* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.17084)] [[Project](https://1jsingh.github.io/gradop)] \
30 Nov 2022


**Score-based Continuous-time Discrete Diffusion Models** \
*Haoran Sun, Lijun Yu, Bo Dai, Dale Schuurmans, Hanjun Dai* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.16750)] \
30 Nov 2022

**Wavelet Diffusion Models are fast and scalable Image Generators** \
*Hao Phung, Quan Dao, Anh Tran* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.16152)] \
29 Nov 2022


**Dimensionality-Varying Diffusion Process** \
*Han Zhang, Ruili Feng, Zhantao Yang, Lianghua Huang, Yu Liu, Yifei Zhang, Yujun Shen, Deli Zhao, Jingren Zhou, Fan Cheng* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.16032)] \
29 Nov 2022

**Refining Generative Process with Discriminator Guidance in Score-based Diffusion Models** \
*Dongjun Kim, Yeongmin Kim, Wanmo Kang, Il-Chul Moon* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.17091)] \
28 Nov 2022



**Diffusion Probabilistic Model Made Slim** \
*Xingyi Yang, Daquan Zhou, Jiashi Feng, Xinchao Wang* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.17106)] \
27 Nov 2022


**Fast Sampling of Diffusion Models via Operator Learning** \
*Hongkai Zheng, Weili Nie, Arash Vahdat, Kamyar Azizzadenesheli, Anima Anandkumar* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.13449)] \
24 Nov 2022

**Latent Video Diffusion Models for High-Fidelity Video Generation with Arbitrary Lengths** \
*Yingqing He, Tianyu Yang, Yong Zhang, Ying Shan, Qifeng Chen* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.13221)] \
23 Nov 2022



**Paint by Example: Exemplar-based Image Editing with Diffusion Models** \
*Binxin Yang, Shuyang Gu, Bo Zhang, Ting Zhang, Xuejin Chen, Xiaoyan Sun, Dong Chen, Fang Wen* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.13227)] \
23 Nov 2022


**SinDiffusion: Learning a Diffusion Model from a Single Natural Image** \
*Weilun Wang, Jianmin Bao, Wengang Zhou, Dongdong Chen, Dong Chen, Lu Yuan, Houqiang Li* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.12445)] [[Github](https://github.com/WeilunWang/SinDiffusion)] \
22 Nov 2022

**Accelerating Diffusion Sampling with Classifier-based Feature Distillation** \
*Wujie Sun, Defang Chen, Can Wang, Deshi Ye, Yan Feng, Chun Chen* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.12039)] \
22 Nov 2022

**SceneComposer: Any-Level Semantic Image Synthesis** \
*Yu Zeng, Zhe Lin, Jianming Zhang, Qing Liu, John Collomosse, Jason Kuen, Vishal M. Patel* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.11742)] [[Project](https://zengyu.me/scenec/)] \
21 Nov 2022

**Diffusion-Based Scene Graph to Image Generation with Masked Contrastive Pre-Training** \
*Ling Yang, Zhilin Huang, Yang Song, Shenda Hong, Guohao Li, Wentao Zhang, Bin Cui, Bernard Ghanem, Ming-Hsuan Yang* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.11138)] \
21 Nov 2022

**SinFusion: Training Diffusion Models on a Single Image or Video** \
*Yaniv Nikankin, Niv Haim, Michal Irani* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.11743)] \
21 Nov 2022

**MagicVideo: Efficient Video Generation With Latent Diffusion Models** \
*Daquan Zhou, Weimin Wang, Hanshu Yan, Weiwei Lv, Yizhe Zhu, Jiashi Feng* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.11018)] [[Project](https://magicvideo.github.io/)] \
20 Nov 2022

**Seeing Beyond the Brain: Conditional Diffusion Model with Sparse Masked Modeling for Vision Decoding** \
*Zijiao Chen, Jiaxin Qing, Tiange Xiang, Wan Lin Yue, Juan Helen Zhou* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.06956)] [[Project](https://mind-vis.github.io/)] [[Github](https://github.com/zjc062/mind-vis)] \
13 Nov 2022

**Few-shot Image Generation with Diffusion Models** \
*Jingyuan Zhu, Huimin Ma, Jiansheng Chen, Jian Yuan* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.03264)] \
7 Nov 2022

**From Denoising Diffusions to Denoising Markov Models** \
*Joe Benton, Yuyang Shi, Valentin De Bortoli, George Deligiannidis, Arnaud Doucet* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.03595)] [[Github](https://github.com/yuyang-shi/generalized-diffusion)] \
7 Nov 2022


**Efficient Spatially Sparse Inference for Conditional GANs and Diffusion Models** \
*Muyang Li, Ji Lin, Chenlin Meng, Stefano Ermon, Song Han, Jun-Yan Zhu* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2211.02048)] [[Github](https://github.com/lmxyy/sige)] \
4 Nov 2022

**An optimal control perspective on diffusion-based generative modeling** \
*Julius Berner, Lorenz Richter, Karen Ullrich* \
NeurIPS Workshop 2022. [[Paper](https://arxiv.org/abs/2211.01364)] \
2 Nov 2022

**Entropic Neural Optimal Transport via Diffusion Processes** \
*Nikita Gushchin, Alexander Kolesov, Alexander Korotin, Dmitry Vetrov, Evgeny Burnaev* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2211.01156)] \
2 Nov 2022

**DPM-Solver++: Fast Solver for Guided Sampling of Diffusion Probabilistic Models** \
*Cheng Lu, Yuhao Zhou, Fan Bao, Jianfei Chen, Chongxuan Li, Jun Zhu* \
NeurIPS 2022 (Oral). [[Paper](https://arxiv.org/abs/2211.01095)] [[Github](https://github.com/LuChengTHU/dpm-solver)] \
2 Nov 2022

**Score-based Denoising Diffusion with Non-Isotropic Gaussian Noise Models** \
*Vikram Voleti, Christopher Pal, Adam Oberman* \
NeurIPS Workshop 2022. [[Paper](https://arxiv.org/abs/2210.12254)] \
21 Oct 2022


**Deep Equilibrium Approaches to Diffusion Models** \
*Ashwini Pokle, Zhengyang Geng, Zico Kolter* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2210.12867)] [[Github](https://github.com/locuslab/deq-ddim)] \
23 Oct 2022

**Representation Learning with Diffusion Models** \
*Jeremias Traub* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2210.11058)] [[Github](https://github.com/jeremiastraub/diffusion)] \
20 Oct 2022

**Self-Guided Diffusion Models** \
*Vincent Tao Hu, David W Zhang, Yuki M. Asano, Gertjan J. Burghouts, Cees G. M. Snoek* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2210.06462)] [[Project](http://taohu.me/sgdm/)] \
12 Oct 2022

**GENIE: Higher-Order Denoising Diffusion Solvers** \
*Tim Dockhorn, Arash Vahdat, Karsten Kreis* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2210.05475)] [[Project](https://nv-tlabs.github.io/GENIE/) [[Github](https://github.com/nv-tlabs/GENIE)] \
11 Oct 2022

**f-DM: A Multi-stage Diffusion Model via Progressive Signal Transformation** \
*Jiatao Gu, Shuangfei Zhai, Yizhe Zhang, Miguel Angel Bautista, Josh Susskind* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2210.04955)] [[Project](http://jiataogu.me/fdm/)] \
10 Oct 2022

**On Distillation of Guided Diffusion Models** \
*Chenlin Meng, Ruiqi Gao, Diederik P. Kingma, Stefano Ermon, Jonathan Ho, Tim Salimans* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2210.03142)] \
6 Oct 2022


**Improving Sample Quality of Diffusion Model Using Self-Attention Guidance** \
*Susung Hong, Gyuseong Lee, Wooseok Jang, Seungryong Kim* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2210.00939)] [[Project](https://ku-cvlab.github.io/Self-Attention-Guidance/)] \
3 Oct 2022

**OCD: Learning to Overfit with Conditional Diffusion Models** \
*Shahar Shlomo Lutati, Lior Wolf* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2210.00471)] [[Github](https://github.com/ShaharLutatiPersonal/OCD)] \
2 Oct 2022

**Generated Faces in the Wild: Quantitative Comparison of Stable Diffusion, Midjourney and DALL-E 2** \
*Ali Borji* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2210.00586)] [[Github](https://github.com/aliborji/GFW)] \
2 Oct 2022

**Denoising MCMC for Accelerating Diffusion-Based Generative Models** \
*Beomsu Kim, Jong Chul Ye* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2209.14593)] [[Github](https://github.com/1202kbs/DMCMC)] \
29 Sep 2022

**All are Worth Words: a ViT Backbone for Score-based Diffusion Models** \
*Fan Bao, Chongxuan Li, Yue Cao, Jun Zhu* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2209.12152)] \
25 Sep 2022


**Neural Wavelet-domain Diffusion for 3D Shape Generation** \
*Ka-Hei Hui, Ruihui Li, Jingyu Hu, Chi-Wing Fu* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2209.08725)] \
19 Sep 2022

**Can segmentation models be trained with fully synthetically generated data?** \
*Virginia Fernandez, Walter Hugo Lopez Pinaya, Pedro Borges, Petru-Daniel Tudosiu, Mark S Graham, Tom Vercauteren, M Jorge Cardoso* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2209.08256)] \
17 Sep 2022

**Blurring Diffusion Models** \
*Emiel Hoogeboom, Tim Salimans* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2209.05557)] \
12 Sep 2022

**Soft Diffusion: Score Matching for General Corruptions** \
*Giannis Daras, Mauricio Delbracio, Hossein Talebi, Alexandros G. Dimakis, Peyman Milanfar* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2209.05442)] \
12 Sep 2022

**Improved Masked Image Generation with Token-Critic** \
*José Lezama, Huiwen Chang, Lu Jiang, Irfan Essa* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2209.04439)] \
9 Sep 2022


**Let us Build Bridges: Understanding and Extending Diffusion Generative Models** \
*Xingchao Liu, Lemeng Wu, Mao Ye, Qiang Liu* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.14699)] \
31 Aug 2022

**Frido: Feature Pyramid Diffusion for Complex Scene Image Synthesis** \
*Wan-Cyuan Fan, Yen-Chun Chen, DongDong Chen, Yu Cheng, Lu Yuan, Yu-Chiang Frank Wang* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.13753)] \
29 Aug 2022


**Adaptively-Realistic Image Generation from Stroke and Sketch with Diffusion Model** \
*Shin-I Cheng, Yu-Jie Chen, Wei-Chen Chiu, Hsin-Ying Lee, Hung-Yu Tseng* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.12675)] [[Project](https://cyj407.github.io/DiSS/)] \
26 Aug 2022

**Cold Diffusion: Inverting Arbitrary Image Transforms Without Noise** \
*Arpit Bansal, Eitan Borgnia, Hong-Min Chu, Jie S. Li, Hamid Kazemi, Furong Huang, Micah Goldblum, Jonas Geiping, Tom Goldstein* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.09392)] [[Github](https://github.com/arpitbansal297/Cold-Diffusion-Models)] \
19 Aug 2022

**Enhancing Diffusion-Based Image Synthesis with Robust Classifier Guidance** \
*Bahjat Kawar, Roy Ganz, Michael Elad* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.08664)] \
18 Aug 2022

**Your ViT is Secretly a Hybrid Discriminative-Generative Diffusion Model** \
*Xiulong Yang, Sheng-Min Shih, Yinlin Fu, Xiaoting Zhao, Shihao Ji* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.07791)] [[Github](https://github.com/sndnyang/Diffusion_ViT)] \
16 Aug 2022



**Applying Regularized Schrödinger-Bridge-Based Stochastic Process in Generative Modeling** \
*Ki-Ung Song* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.07131)] [[Github](https://github.com/KiUngSong/RSB)] \
15 Aug 2022

**Analog Bits: Generating Discrete Data using Diffusion Models with Self-Conditioning** \
*Ting Chen, Ruixiang Zhang, Geoffrey Hinton* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.04202)] \
8 Aug 2022


**Pyramidal Denoising Diffusion Probabilistic Models** \
*Dohoon Ryu, Jong Chul Ye* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.01864)] \
3 Aug 2022

**Progressive Deblurring of Diffusion Models for Coarse-to-Fine Image Synthesis** \
*Sangyun Lee, Hyungjin Chung, Jaehyeon Kim, Jong Chul Ye* \
arxiv 2022. [[Paper](https://arxiv.org/abs/2207.11192)] [[Github](https://github.com/sangyun884/blur-diffusion)] \
16 Jul 2022

**Improving Diffusion Model Efficiency Through Patching** \
*Troy Luhman, Eric Luhman* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2207.04316)] [[Github](https://github.com/ericl122333/PatchDiffusion-Pytorch)] \
9 Jul 2022

**Accelerating Score-based Generative Models with Preconditioned Diffusion Sampling** \
*Hengyuan Ma, Li Zhang, Xiatian Zhu, Jianfeng Feng* \
ECCV 2022. [[Paper](https://arxiv.org/abs/2207.02196)] \
5 Jul 2022

**SPI-GAN: Distilling Score-based Generative Models with Straight-Path Interpolations** \
*Jinsung Jeon, Noseong Park* \
arxiv 2022. [[Paper](https://arxiv.org/abs/2206.14464)] \
29 Jun 2022

**Entropy-driven Sampling and Training Scheme for Conditional Diffusion Generation** \
*Shengming Li, Guangcong Zheng, Hui Wang, Taiping Yao, Yang Chen, Shoudong Ding, Xi Li* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.11474)] \
23 Jun 2022

**Generative Modelling With Inverse Heat Dissipation** \
*Severi Rissanen, Markus Heinonen, Arno Solin* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.13397)] [[Project](https://aaltoml.github.io/generative-inverse-heat-dissipation/)] \
21 Jun 2022

**Diffusion models as plug-and-play priors** \
*Alexandros Graikos, Nikolay Malkin, Nebojsa Jojic, Dimitris Samaras* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2206.09012)] [[Github](https://github.com/alexgraikos/diffusion_priors)] \
17 Jun 2022

**A Flexible Diffusion Model** \
*Weitao Du, Tao Yang, He Zhang, Yuanqi Du* \
ICML 2023. [[Paper](https://arxiv.org/abs/2206.10365)] \
17 Jun 2022

**Lossy Compression with Gaussian Diffusion** \
*Lucas Theis, Tim Salimans, Matthew D. Hoffman, Fabian Mentzer* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.08889)] \
17 Jun 2022

**Maximum Likelihood Training for Score-Based Diffusion ODEs by High-Order Denoising Score Matching** \
*Cheng Lu, Kaiwen Zheng, Fan Bao, Jianfei Chen, Chongxuan Li, Jun Zhu* \
ICML 2022. [[Paper](https://arxiv.org/abs/2206.08265)] [[Github](https://github.com/LuChengTHU/mle_score_ode)] \
16 Jun 2022

**Estimating the Optimal Covariance with Imperfect Mean in Diffusion Probabilistic Models** \
*Fan Bao, Chongxuan Li, Jiacheng Sun, Jun Zhu, Bo Zhang* \
ICML 2022. [[Paper](https://arxiv.org/abs/2206.07309)] [[Github](https://github.com/baofff/Extended-Analytic-DPM)] \
15 Jun 2022


**Diffusion Models for Video Prediction and Infilling** \
*Tobias Höppe, Arash Mehrjou, Stefan Bauer, Didrik Nielsen, Andrea Dittadi* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.07696)] \
15 Jun 2022

**Discrete Contrastive Diffusion for Cross-Modal and Conditional Generation** \
*Ye Zhu, Yu Wu, Kyle Olszewski, Jian Ren, Sergey Tulyakov, Yan Yan* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.07771)] [[Github](https://github.com/L-YeZhu/CDCD)] \
15 Jun 2022

**gDDIM: Generalized denoising diffusion implicit models** \
*Qinsheng Zhang, Molei Tao, Yongxin Chen* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.05564)] [[Github](https://github.com/qsh-zh/gDDIM)] \
11 Jun 2022

**How Much is Enough? A Study on Diffusion Times in Score-based Generative Models** \
*Giulio Franzese, Simone Rossi, Lixuan Yang, Alessandro Finamore, Dario Rossi, Maurizio Filippone, Pietro Michiardi* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.05173)] \
10 Jun 2022

**Image Generation with Multimodal Priors using Denoising Diffusion Probabilistic Models** \
*Nithin Gopalakrishnan Nair, Wele Gedara Chaminda Bandara, Vishal M Patel* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.05039)] \
10 Jun 2022

**Accelerating Score-based Generative Models for High-Resolution Image Synthesis** \
*Hengyuan Ma, Li Zhang, Xiatian Zhu, Jingfeng Zhang, Jianfeng Feng* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.04029)] \
8 Jun 2022

**Diffusion-GAN: Training GANs with Diffusion** \
*Zhendong Wang, Huangjie Zheng, Pengcheng He, Weizhu Chen, Mingyuan Zhou* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.02262)] \
5 Jun 2022

**DPM-Solver: A Fast ODE Solver for Diffusion Probabilistic Model Sampling in Around 10 Steps** \
*Cheng Lu, Yuhao Zhou, Fan Bao, Jianfei Chen, Chongxuan Li, Jun Zhu* \
NeurrIPS 2022. [[Paper](https://arxiv.org/abs/2206.00927)] [[Github](https://github.com/LuChengTHU/dpm-solver)] \
2 Jun 2022

**Elucidating the Design Space of Diffusion-Based Generative Models** \
*Tero Karras, Miika Aittala, Timo Aila, Samuli Laine* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2206.00364)] \
1 Jun 2022

**On Analyzing Generative and Denoising Capabilities of Diffusion-based Deep Generative Models** \
*Kamil Deja, Anna Kuzina, Tomasz Trzciński, Jakub M. Tomczak* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2206.00070)] \
31 May 2022

**Few-Shot Diffusion Models** \
*Giorgio Giannone, Didrik Nielsen, Ole Winther* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2205.15463)] \
30 May 2022

**A Continuous Time Framework for Discrete Denoising Models** \
*Andrew Campbell, Joe Benton, Valentin De Bortoli, Tom Rainforth, George Deligiannidis, Arnaud Doucet* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2205.14987)] \
30 May 2022

**Maximum Likelihood Training of Implicit Nonlinear Diffusion Models** \
*Dongjun Kim, Byeonghu Na, Se Jung Kwon, Dongsoo Lee, Wanmo Kang, Il-Chul Moon* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2205.13699)] \
27 May 2022

**Accelerating Diffusion Models via Early Stop of the Diffusion Process** \
*Zhaoyang Lyu, Xudong XU, Ceyuan Yang, Dahua Lin, Bo Dai* \
ICML 2022. [[Paper](https://arxiv.org/abs/2205.12524)] \
25 May 2022



**Flexible Diffusion Modeling of Long Videos** \
*William Harvey, Saeid Naderiparizi, Vaden Masrani, Christian Weilbach, Frank Wood* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2205.11495)] [[Github](https://github.com/plai-group/flexible-video-diffusion-modeling)] \
23 May 2022

**MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation** \
*Vikram Voleti, Alexia Jolicoeur-Martineau, Christopher Pal* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2205.09853)] [[Github](https://github.com/voletiv/mcvd-pytorch)] \
19 May 2022

**On Conditioning the Input Noise for Controlled Image Generation with Diffusion Models** \
*Vedant Singh, Surgan Jandial, Ayush Chopra, Siddharth Ramesh, Balaji Krishnamurthy, Vineeth N. Balasubramanian* \
CVPR Workshop 2022. [[Paper](https://arxiv.org/abs/2205.03859)] \
8 May 2022

**Subspace Diffusion Generative Models** \
*Bowen Jing, Gabriele Corso, Renato Berlinghieri, Tommi Jaakkola* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2205.01490)] [[Github](https://github.com/bjing2016/subspace-diffusion)] \
3 May 2022

**Fast Sampling of Diffusion Models with Exponential Integrator** \
*Qinsheng Zhang, Yongxin Chen* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2204.13902)] \
29 Apr 2022

**Semi-Parametric Neural Image Synthesis** \
*Andreas Blattmann, Robin Rombach, Kaan Oktay, Jonas Müller, Björn Ommer* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2204.11824)] \
25 Apr 2022


**Video Diffusion Models** \
*Jonathan Ho, Tim Salimans, Alexey Gritsenko, William Chan, Mohammad Norouzi, David J. Fleet* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2204.03458)] \
7 Apr 2022

**Perception Prioritized Training of Diffusion Models** \
*Jooyoung Choi, Jungbeom Lee, Chaehun Shin, Sungwon Kim, Hyunwoo Kim, Sungroh Yoon* \
CVPR 2022. [[Paper](https://arxiv.org/abs/2204.00227)] [[Github](https://github.com/jychoi118/P2-weighting)] \
1 Apr 2022

**Generating High Fidelity Data from Low-density Regions using Diffusion Models** \
*Vikash Sehwag, Caner Hazirbas, Albert Gordo, Firat Ozgenel, Cristian Canton Ferrer* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2203.17260)] \
31 Mar 2022

**Diffusion Models for Counterfactual Explanations** \
*Guillaume Jeanneret, Loïc Simon, Frédéric Jurie* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2203.15636)] \
29 Mar 2022

**Denoising Likelihood Score Matching for Conditional Score-based Data Generation** \
*Chen-Hao Chao, Wei-Fang Sun, Bo-Wun Cheng, Yi-Chen Lo, Chia-Che Chang, Yu-Lun Liu, Yu-Lin Chang, Chia-Ping Chen, Chun-Yi Lee* \
ICLR 2022. [[Paper](https://arxiv.org/abs/2203.14206)] \
27 Mar 2022

**Diffusion Probabilistic Modeling for Video Generation** \
*Ruihan Yang, Prakhar Srivastava, Stephan Mandt* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2203.09481)] [[Github](https://github.com/buggyyang/rvd)] \
16 Mar 2022

**Dynamic Dual-Output Diffusion Models** \
*Yaniv Benny, Lior Wolf* \
CVPR 2022. [[Paper](https://arxiv.org/abs/2203.04304)] \
8 Mar 2022

**Conditional Simulation Using Diffusion Schrödinger Bridges** \
*Yuyang Shi, Valentin De Bortoli, George Deligiannidis, Arnaud Doucet* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2202.13460)] \
27 Feb 2022

**Diffusion Causal Models for Counterfactual Estimation** \
*Pedro Sanchez, Sotirios A. Tsaftaris* \
PMLR 2022. [[Paper](https://arxiv.org/abs/2202.10166)] \
21 Feb 2022

**Pseudo Numerical Methods for Diffusion Models on Manifolds** \
*Luping Liu, Yi Ren, Zhijie Lin, Zhou Zhao* \
ICLR 2022. [[Paper](https://arxiv.org/abs/2202.09778)] [[Github](https://github.com/luping-liu/PNDM)] \
20 Feb 2022

**Truncated Diffusion Probabilistic Models** \
*Huangjie Zheng, Pengcheng He, Weizhu Chen, Mingyuan Zhou* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2202.09671)] \
19 Feb 2022

**Understanding DDPM Latent Codes Through Optimal Transport** \
*Valentin Khrulkov, Ivan Oseledets* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2202.07477)] \
14 Feb 2022

**Learning Fast Samplers for Diffusion Models by Differentiating Through Sample Quality** \
*Daniel Watson, William Chan, Jonathan Ho, Mohammad Norouzi* \
ICLR 2022. [[Paper](https://arxiv.org/abs/2202.05830)] \
11 Feb 2022


**Diffusion bridges vector quantized Variational AutoEncoders** \
*Max Cohen, Guillaume Quispe, Sylvain Le Corff, Charles Ollion, Eric Moulines* \
ICML 2022. [[Paper](https://arxiv.org/abs/2202.04895)] \
10 Feb 2022

**Progressive Distillation for Fast Sampling of Diffusion Models** \
*Tim Salimans, Jonathan Ho* \
ICLR 2022. [[Paper](https://arxiv.org/abs/2202.00512)] \
1 Feb 2022

**Analytic-DPM: an Analytic Estimate of the Optimal Reverse Variance in Diffusion Probabilistic Models** \
*Fan Bao, Chongxuan Li, Jun Zhu, Bo Zhang* \
ICLR 2022. [[Paper](https://arxiv.org/abs/2201.06503)] \
17 Jan 2022

**DiffuseVAE: Efficient, Controllable and High-Fidelity Generation from Low-Dimensional Latents** \
*Kushagra Pandey, Avideep Mukherjee, Piyush Rai, Abhishek Kumar* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2201.00308)] [[Github](https://github.com/kpandey008/DiffuseVAE)] \
2 Jan 2022

**Itô-Taylor Sampling Scheme for Denoising Diffusion Probabilistic Models using Ideal Derivatives** \
*Hideyuki Tachibana, Mocho Go, Muneyoshi Inahara, Yotaro Katayama, Yotaro Watanabe* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2112.13339)] \
26 Dec 2021

**GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models** \
*Alex Nichol, Prafulla Dhariwal, Aditya Ramesh, Pranav Shyam, Pamela Mishkin, Bob McGrew, Ilya Sutskever, Mark Chen* \
ICML 2021. [[Paper](https://arxiv.org/abs/2112.10741)] [[Github](https://github.com/openai/glide-text2im)] \
20 Dec 2021

**High-Resolution Image Synthesis with Latent Diffusion Models** \
*Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2112.10752)] [[Github](https://github.com/CompVis/latent-diffusion)] \
20 Dec 2021

**Heavy-tailed denoising score matching** \
*Jacob Deasy, Nikola Simidjievski, Pietro Liò* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2112.09788)] \
17 Dec 2021

**High Fidelity Visualization of What Your Self-Supervised Representation Knows About** \
*Florian Bordes, Randall Balestriero, Pascal Vincent* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2112.09164)] \
16 Dec 2021

**Tackling the Generative Learning Trilemma with Denoising Diffusion GANs** \
*Zhisheng Xiao, Karsten Kreis, Arash Vahdat* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2112.07804)] [[Project](https://nvlabs.github.io/denoising-diffusion-gan)] \
15 Dec 2021

**Score-Based Generative Modeling with Critically-Damped Langevin Diffusion** \
*Tim Dockhorn, Arash Vahdat, Karsten Kreis* \
ICLR 2022. [[Paper](https://arxiv.org/abs/2112.07068)] [[Project](https://nv-tlabs.github.io/CLD-SGM/)] \
14 Dec 2021

**More Control for Free! Image Synthesis with Semantic Diffusion Guidance** \
*Xihui Liu, Dong Huk Park, Samaneh Azadi, Gong Zhang, Arman Chopikyan, Yuxiao Hu, Humphrey Shi, Anna Rohrbach, Trevor Darrell* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2112.05744)] \
10 Dec 2021

**Global Context with Discrete Diffusion in Vector Quantised Modelling for Image Generation** \
*Minghui Hu, Yujie Wang, Tat-Jen Cham, Jianfei Yang, P.N.Suganthan* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2112.01799)] \
3 Dec 2021

**Diffusion Autoencoders: Toward a Meaningful and Decodable Representation** \
*Konpat Preechakul, Nattanat Chatthee, Suttisak Wizadwongsa, Supasorn Suwajanakorn* \
CVPR 2022. [[Paper](https://arxiv.org/abs/2111.15640)] [[Project](https://diff-ae.github.io/)] [[Github](https://github.com/phizaz/diffae)] \
30 Dec 2021

**Conditional Image Generation with Score-Based Diffusion Models** \
*Georgios Batzolis, Jan Stanczuk, Carola-Bibiane Schönlieb, Christian Etmann* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2111.13606)] \
26 Nov 2021

**Unleashing Transformers: Parallel Token Prediction with Discrete Absorbing Diffusion for Fast High-Resolution Image Generation from Vector-Quantized Codes** \
*Sam Bond-Taylor, Peter Hessey, Hiroshi Sasaki, Toby P. Breckon, Chris G. Willcocks* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2111.12701)] [[Github](https://github.com/samb-t/unleashing-transformers)] \
24 Nov 2021

**Diffusion Normalizing Flow** \
*Qinsheng Zhang, Yongxin Chen* \
NeurIPS 2021. [[Paper](https://arxiv.org/abs/2110.07579)] [[Github](https://github.com/qsh-zh/DiffFlow)] \
14 Oct 2021

**Denoising Diffusion Gamma Models** \
*Eliya Nachmani, Robin San Roman, Lior Wolf* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2110.05948)] \
10 Oct 2021

**Score-based Generative Neural Networks for Large-Scale Optimal Transport** \
*Max Daniels, Tyler Maunu, Paul Hand* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2110.03237)] \
7 Oct 2021

**Score-Based Generative Classifiers** \
*Roland S. Zimmermann, Lukas Schott, Yang Song, Benjamin A. Dunn, David A. Klindt* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2110.00473)] \
1 Oct 2021

**Classifier-Free Diffusion Guidance** \
*Jonathan Ho, Tim Salimans* \
NeurIPS Workshop 2021. [[Paper](https://arxiv.org/abs/2207.12598)] \
28 Sep 2021


**Bilateral Denoising Diffusion Models** \
*Max W. Y. Lam, Jun Wang, Rongjie Huang, Dan Su, Dong Yu* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2108.11514)] [[Project](https://bilateral-denoising-diffusion-model.github.io)] \
26 Aug 2021

**ImageBART: Bidirectional Context with Multinomial Diffusion for Autoregressive Image Synthesis** \
*Patrick Esser, Robin Rombach, Andreas Blattmann, Björn Ommer* \
NeurIPS 2021. [[Paper](https://arxiv.org/abs/2108.08827)] [[Project](https://compvis.github.io/imagebart/)] \
19 Aug 2021

**ILVR: Conditioning Method for Denoising Diffusion Probabilistic Models** \
*Jooyoung Choi, Sungwon Kim, Yonghyun Jeong, Youngjune Gwon, Sungroh Yoon* \
ICCV 2021 (Oral). [[Paper](https://arxiv.org/abs/2108.02938)] [[Github](https://github.com/jychoi118/ilvr_adm)] \
6 Aug 2021

**SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations** \
*Chenlin Meng, Yutong He, Yang Song, Jiaming Song, Jiajun Wu, Jun-Yan Zhu, Stefano Ermon* \
ICLR  2022. [[Paper](https://arxiv.org/abs/2108.01073)] [[Project](https://sde-image-editing.github.io/)] [[Github](https://github.com/ermongroup/SDEdit)] \
2 Aug 2021

**Structured Denoising Diffusion Models in Discrete State-Spaces** \
*Jacob Austin, Daniel D. Johnson, Jonathan Ho, Daniel Tarlow, Rianne van den Berg* \
NeurIPS 2021. [[Paper](https://arxiv.org/abs/2107.03006)] \
7 Jul 2021 

**Variational Diffusion Models** \
*Diederik P. Kingma, Tim Salimans, Ben Poole, Jonathan Ho* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2107.00630)] [[Github](https://github.com/google-research/vdm)] \
1 Jul 2021 

**Diffusion Priors In Variational Autoencoders** \
*Antoine Wehenkel, Gilles Louppe* \
ICML Workshop 2021. [[Paper](https://arxiv.org/abs/2106.15671)] \
29 Jun 2021

**Deep Generative Learning via Schrödinger Bridge** \
*Gefei Wang, Yuling Jiao, Qian Xu, Yang Wang, Can Yang* \
ICML 2021. [[Paper](https://arxiv.org/abs/2106.10410)] \
19 Jun 2021

**Non Gaussian Denoising Diffusion Models** \
*Eliya Nachmani, Robin San Roman, Lior Wolf* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2106.07582)] [[Project](https://enk100.github.io/Non-Gaussian-Denoising-Diffusion-Models/)] \
14 Jun 2021 

**D2C: Diffusion-Denoising Models for Few-shot Conditional Generation** \
*Abhishek Sinha, Jiaming Song, Chenlin Meng, Stefano Ermon* \
NeurIPS 2021. [[Paper](https://arxiv.org/abs/2106.06819)] [[Project](https://d2c-model.github.io/)] [[Github](https://github.com/d2c-model/d2c-model.github.io)] \
12 Jun 2021

**Score-based Generative Modeling in Latent Space** \
*Arash Vahdat, Karsten Kreis, Jan Kautz* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2106.05931)] \
10 Jun 2021

**Learning to Efficiently Sample from Diffusion Probabilistic Models** \
*Daniel Watson, Jonathan Ho, Mohammad Norouzi, William Chan* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2106.03802)] \
7 Jun 2021 

**A Variational Perspective on Diffusion-Based Generative Models and Score Matching** \
*Chin-Wei Huang, Jae Hyun Lim, Aaron Courville* \
NeurIPS 2021. [[Paper](https://arxiv.org/abs/2106.02808)] [[Github](https://github.com/CW-Huang/sdeflow-light)] \
5 Jun 2021 

**Soft Truncation: A Universal Training Technique of Score-based Diffusion Model for High Precision Score Estimation** \
*Dongjun Kim, Seungjae Shin, Kyungwoo Song, Wanmo Kang, Il-Chul Moon* \
ICML 2022. [[Paper](https://arxiv.org/abs/2106.05527)] \
10 Jun 2021

**Diffusion Schrödinger Bridge with Applications to Score-Based Generative Modeling** \
*Valentin De Bortoli, James Thornton, Jeremy Heng, Arnaud Doucet* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2106.01357)] [[Project](https://jtt94.github.io/papers/schrodinger_bridge)] [[Github](https://github.com/JTT94/diffusion_schrodinger_bridge)] \
1 Jun 2021

**On Fast Sampling of Diffusion Probabilistic Models** \
*Zhifeng Kong, Wei Ping* \
ICML Workshop 2021. [[Paper](https://arxiv.org/abs/2106.00132)] [[Github](https://github.com/FengNiMa/FastDPM_pytorch)] \
31 May 2021 

**Cascaded Diffusion Models for High Fidelity Image Generation** \
*Jonathan Ho, Chitwan Saharia, William Chan, David J. Fleet, Mohammad Norouzi, Tim Salimans* \
JMLR 2021. [[Paper](https://arxiv.org/abs/2106.15282)] [[Project](https://cascaded-diffusion.github.io/)] \
30 May 2021 

**Gotta Go Fast When Generating Data with Score-Based Models** \
*Alexia Jolicoeur-Martineau, Ke Li, Rémi Piché-Taillefer, Tal Kachman, Ioannis Mitliagkas* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2105.14080)] [[Github](https://github.com/AlexiaJM/score_sde_fast_sampling)] \
28 May 2021

**Diffusion Models Beat GANs on Image Synthesis** \
*Prafulla Dhariwal, Alex Nichol* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2105.05233)] [[Github](https://github.com/openai/guided-diffusion)] \
11 May 2021 

**Image Super-Resolution via Iterative Refinement** \
*Chitwan Saharia, Jonathan Ho, William Chan, Tim Salimans, David J. Fleet, Mohammad Norouzi* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2104.07636)] [[Project](https://iterative-refinement.github.io/)] [[Github](https://github.com/Janspiry/Image-Super-Resolution-via-Iterative-Refinement)] \
15 Apr 2021 

**Noise Estimation for Generative Diffusion Models** \
*Robin San-Roman, Eliya Nachmani, Lior Wolf* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2104.02600)] \
6 Apr 2021 

**Improved Denoising Diffusion Probabilistic Models** \
*Alex Nichol, Prafulla Dhariwal* \
ICLR 2021. [[Paper](https://arxiv.org/abs/2102.09672)] [[Github](https://github.com/openai/improved-diffusion)] \
18 Feb 2021 

**Maximum Likelihood Training of Score-Based Diffusion Models** \
*Yang Song, Conor Durkan, Iain Murray, Stefano Ermon* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2101.09258)] \
22 Jan 2021 

**Knowledge Distillation in Iterative Generative Models for Improved Sampling Speed** \
*Eric Luhman, Troy Luhman* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2101.02388)] [[Github](https://github.com/tcl9876/Denoising_Student)] \
7 Jan 2021

**Learning Energy-Based Models by Diffusion Recovery Likelihood** \
*Ruiqi Gao, Yang Song, Ben Poole, Ying Nian Wu, Diederik P. Kingma* \
ICLR 2021. [[Paper](https://arxiv.org/abs/2012.08125)] [[Github](https://github.com/ruiqigao/recovery_likelihood)] \
15 Dec 2020 

**Score-Based Generative Modeling through Stochastic Differential Equations** \
*Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, Ben Poole* \
ICLR 2021 (Oral). [[Paper](https://arxiv.org/abs/2011.13456)] [[Github](https://github.com/yang-song/score_sde)] \
26 Nov 2020 

**Variational (Gradient) Estimate of the Score Function in Energy-based Latent Variable Models** \
*Fan Bao, Kun Xu, Chongxuan Li, Lanqing Hong, Jun Zhu, Bo Zhang* \
ICML 2021. [[Paper](https://arxiv.org/abs/2010.08258)] \
16 Oct 2020

**Denoising Diffusion Implicit Models**  \
*Jiaming Song, Chenlin Meng, Stefano Ermon* \
ICLR 2021. [[Paper](https://arxiv.org/abs/2010.02502)] [[Github](https://github.com/ermongroup/ddim)] \
6 Oct 2020

**Adversarial score matching and improved sampling for image generation** \
*Alexia Jolicoeur-Martineau, Rémi Piché-Taillefer, Rémi Tachet des Combes, Ioannis Mitliagkas* \
ICLR 2021. [[Paper](https://arxiv.org/abs/2009.05475)] [[Github](https://github.com/AlexiaJM/AdversarialConsistentScoreMatching)] \
11 Sep 2020

**Denoising Diffusion Probabilistic Models** \
*Jonathan Ho, Ajay Jain, Pieter Abbeel* \
NeurIPS 2020. [[Paper](https://arxiv.org/abs/2006.11239)] [[Github](https://github.com/hojonathanho/diffusion)] [[Github2](https://github.com/pesser/pytorch_diffusion)] \
19 Jun 2020 

**Improved Techniques for Training Score-Based Generative Models** \
*Yang Song, Stefano Ermon* \
NeurIPS 2020. [[Paper](https://arxiv.org/abs/2006.09011)] [[Github](https://github.com/ermongroup/ncsnv2)] \
16 Jun 2020 

**Generative Modeling by Estimating Gradients of the Data Distribution** \
*Yang Song, Stefano Ermon* \
NeurIPS 2019. [[Paper](https://arxiv.org/abs/1907.05600)] [[Project](https://yang-song.github.io/blog/2021/score/)] [[Github](https://github.com/ermongroup/ncsn)] \
12 Jul 2019 

**Neural Stochastic Differential Equations: Deep Latent Gaussian Models in the Diffusion Limit** \
*Belinda Tzen, Maxim Raginsky* \
arXiv 2019. [[Paper](https://arxiv.org/abs/1905.09883)] \
23 May 2019 

**Deep Unsupervised Learning using Nonequilibrium Thermodynamics** \
*Jascha Sohl-Dickstein, Eric A. Weiss, Niru Maheswaranathan, Surya Ganguli* \
ICML 2015. [[Paper](https://arxiv.org/abs/1503.03585)] [[Github](https://github.com/Sohl-Dickstein/Diffusion-Probabilistic-Models)] \
2 Mar 2015

### Classification

**Likelihood-based Out-of-Distribution Detection with Denoising Diffusion Probabilistic Models** \
*Joseph Goodier, Neill D. F. Campbell* \
BMVC 2023. [[Paper](https://arxiv.org/abs/2310.17432)] \
26 Oct 2023

**Multi-scale Diffusion Denoised Smoothing** \
*Jongheon Jeong, Jinwoo Shin* \
NeurIPS 2023. [[Paper](https://arxiv.org/abs/2310.16779)] \
25 Oct 2023

**DiffRef3D: A Diffusion-based Proposal Refinement Framework for 3D Object Detection** \
*Se-Ho Kim, Inyong Koo, Inyoung Lee, Byeongjun Park, Changick Kim* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2310.16349)] \
25 Oct 2023

**Denoising Task Routing for Diffusion Models** \
*Byeongjun Park, 