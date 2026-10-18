<p align="left">
    English</a>&nbsp ｜ &nbsp<a href="README_CN.md">中文</a>&nbsp
</p>
<br><br>

<p align="center">
    <img src="imgs/logo.png" width="400"/>
<p>
<br>


<div align="center">
  <a href='https://huggingface.co/Kwai-Kolors/Kolors'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-HF-yellow'></a> &ensp;
  <a href="https://Kwai-Kolors/Kolors"><img src="https://img.shields.io/static/v1?label=Kolors Code&message=Github&color=blue&logo=github-pages"></a> &ensp;
  <a href="https://kwai-kolors.github.io/"><img src="https://img.shields.io/static/v1?label=Team%20Page&message=Page&color=green"></a> &ensp;

<a href='https://huggingface.co/spaces/Kwai-Kolors/Kolors '><img src='https://img.shields.io/badge/%F0%9F%A4%97%20HF Space-HF-yellow'></a> &ensp;
  <a href="https://Kwai-Kolors/Kolors/blob/master/imgs/Kolors_paper.pdf"><img src="https://img.shields.io/static/v1?label=Tech Report&message=Arxiv:Kolors&color=red&logo=arxiv"></a> &ensp;
  <a href="https://kolors.kuaishou.com/"><img src="https://img.shields.io/static/v1?label=Official Website&message=Page&color=green"></a> &ensp;
</div>



# Kolors: Effective Training of Diffusion Model for Photorealistic Text-to-Image Synthesis
<figure>
  <img src="imgs/head_final3.png">
</figure>
<br><br>

## Contents

- [🎉 News](#News)
- [📑 Open-source Plan](#open-source-plan)
- [📖 Introduction](#Introduction)
- [📊 Evaluation 🥇🥇🔥🔥](#Evaluation)
- [🎥 Visualization](#Visualization)
- [🛠️ Usage](#Usage)
- [📜 License & Citation & Acknowledgments](#License)
<br><br>


## <a name="News"></a>🎉 News
* 2024.11.13 🔥 [Kolors-Portrait-with-Flux](https://huggingface.co/spaces/Kwai-Kolors/Kolors-Portrait-with-Flux) and [Kolors-Character-With-Flux](https://huggingface.co/spaces/Kwai-Kolors/Kolors-Character-With-Flux), which enable to preserve identity, are available on HuggingFace Space for free trials! Hope you enjoy it!
* 2024.09.01 🔥 Kolors-Virtual-Try-On, a virtual try-on demo based on Kolors is released! Enjoy trying on [Kolors-Virtual-Try-On](https://huggingface.co/spaces/Kwai-Kolors/Kolors-Virtual-Try-On), [WeChat post](https://mp.weixin.qq.com/s/Wk_Eq7OAywlrPqNC6zWZJQ).

* 2024.08.06 🔥 Pose ControlNet is released! Please check [ControlNet(Pose)](./controlnet/) for more details.

* 2024.08.01 🔥 The Kolors-Dreambooth-LoRA training and inference code is released! Please check [Dreambooth-LoRA](./dreambooth/) for more details.
  
* 2024.07.31 🔥 The Kolors-IP-Adapter-FaceID-Plus weights and inference code is released! Please check [IP-Adapter-FaceID-Plus](./ipadapter_FaceID/) for more details.

* 2024.07.26 🔥 ControlNet and Inpainting Model are released! Please check [ControlNet(Canny, Depth)](./controlnet/) and [Inpainting Model](./inpainting/) for more details.


* 2024.07.17 🔥 The Kolors-IP-Adapter-Plus weights and infernce code is released! Please check [IP-Adapter-Plus](./ipadapter/) for more details.

* 2024.07.12 🤗 Kolors is now available in **Diffusers**! Please check [kolors-diffusers](https://huggingface.co/Kwai-Kolors/Kolors-diffusers) or the [example](#using-with-diffusers) below for detail! Thanks to the Diffusers team for their technical support.
* 2024.07.10 🤖 Kolors supports [ModelScope](https://modelscope.cn/models/Kwai-Kolors/Kolors).
* 2024.07.09 💥 Kolors supports [ComfyUI](https://comfyanonymous/ComfyUI#manual-install-windows-linux). Thanks to [@kijai](https://kijai/ComfyUI-KwaiKolorsWrapper) with his great work.
* 2024.07.06 🔥🔥🔥 We release **Kolors**, a large text-to-image model trained on billions of text-image pairs. This model is bilingual in both Chinese and English, and supports a context length of 256 tokens. For more technical details, please refer to [technical report](https://Kwai-Kolors/Kolors/blob/master/imgs/Kolors_paper.pdf).
* 2024.07.03 📊 Kolors won the second place on [FlagEval Multimodal Text-to-Image Leaderboard](https://flageval.baai.ac.cn/#/leaderboard/multimodal?kind=t2i), excelling particularly in the Chinese and English subjective quality assessment where Kolors took the first place.
* 2024.07.02 🎉 Congratulations! Our paper on controllable video generation, [DragAnything: Motion Control for Anything using Entity Representation](https://arxiv.org/abs/2403.07420), have been accepted by ECCV 2024.
* 2024.02.08 🎉 Congratulations! Our paper on generative model evaluation, [Learning Multi-dimensional Human Preference for Text-to-Image Generation](https://wangbohan97.github.io/MPS/), have been accepted by CVPR 2024.
<br><br>

## <a name="open-source-plan"></a>📑 Open-source Plan

- Kolors (Text-to-Image Model)
  - [x] Inference 
  - [x] Checkpoints 
  - [x] IP-Adapter
  - [x] ControlNet (Canny, Depth)
  - [x] Inpainting
  - [x] IP-Adapter-FaceID
  - [x] LoRA
  - [x] ControlNet (Pose)
- [x] ComfyUI
- [x] Gradio
- [x] Diffusers
<br><br>

## 
## <a name="Introduction"></a>📖 Introduction

Kolors is a large-scale text-to-image generation model based on latent diffusion, developed by the Kuaishou Kolors team. Trained on billions of text-image pairs, Kolors exhibits significant advantages over both open-source and closed-source models in visual quality, complex semantic accuracy, and text rendering for both Chinese and English characters. Furthermore, Kolors supports both Chinese and English inputs, demonstrating strong performance in understanding and generating Chinese-specific content. For more details, please refer to this <a href="https://Kwai-Kolors/Kolors/blob/master/imgs/Kolors_paper.pdf">technical report</a></b>.
<br><br>

## <a name="Evaluation"></a>📊 Evaluation
We have collected a comprehensive text-to-image evaluation dataset named KolorsPrompts to compare Kolors with other state-of-the-art open models and closed-source models. KolorsPrompts includes over 1,000 prompts across 14 catagories and 12 evaluation dimensions. The evaluation process incorporates both human and machine assessments. In relevant benchmark evaluations, Kolors demonstrated highly competitive performance, achieving industry-leading standards.

<br><br>

### Human Assessment

For the human evaluation, we invited 50 imagery experts to conduct comparative evaluations of the results generated by different models. The experts rated the generated images based on three criteria: visual appeal, text faithfulness, and overall satisfaction. In the evaluation, Kolors achieved the highest overall satisfaction score and significantly led in visual appeal compared to other models.

|       Model       | Average Overall Satisfaction | Average Visual Appeal | Average Text Faithfulness |
| :--------------: | :--------: | :--------: | :--------: |
|  Adobe-Firefly   |    3.03    |    3.46    |    3.84    |
| Stable Diffusion 3 |    3.26    |    3.50    |    4.20    |
|     DALL-E 3      |    3.32    |    3.54    |    4.22    |
|  Midjourney-v5   |    3.32    |    3.68    |    4.02    |
| Playground-v2.5  |    3.37    |    3.73    |    4.04    |
|  Midjourney-v6   |    3.58    |    3.92    |    4.18    |
|    **Kolors**    |    **3.59**    |    **3.99**    |    **4.17**    |

------

<div style="color: gray; font-size: small;">

**All model results are tested with the April 2024 product versions**

</div>
<br>

### Machine Assessment
We used [MPS](https://arxiv.org/abs/2405.14705) (Multi-dimensional Human Preference Score) on KolorsPrompts as the evaluation metric for machine assessment. Kolors achieved the highest MPS score, which is consistent with the results of the human evaluations.

<div style="text-align:center">

| Models            | Overall MPS |
|:-------------------:|:-------------:|
| Adobe-Firefly     | 8.5     |
| Stable Diffusion 3  | 8.9      |
| DALL-E 3           |   9.0    |
| Midjourney-v5     | 9.4      |
| Playground-v2.5   | 9.8      |
| Midjourney-v6     | 10.2      |
| **Kolors**        | **10.3**      |
</div>


<br>

For more experimental results and details, please refer to our [technical report](https://Kwai-Kolors/Kolors/blob/master/imgs/Kolors_paper.pdf).

<br><br>


## <a name="Visualization"></a>🎥 Visualization

* **High-quality Portrait**
<div style="display: flex; justify-content: space-between;">
  <img src="imgs/zl8.png" />
</div>
<br>

* **Chinese Elements Generation**
<div style="display: flex; justify-content: space-between;">
  <img src="imgs/cn_all.png"/>
</div>
<br>

* **Complex Semantic Understanding**
<div style="display: flex; justify-content: space-between;">
  <img src="imgs/fz_all.png"/>
</div>
<br>

* **Text Rendering**
<div style="display: flex; justify-content: space-between;">
  <img src="imgs/wz_all.png" />
</div>
<br>
</div>

The visualized case prompts mentioned above can be accessed [here](https://Kwai-Kolors/Kolors/blob/master/imgs/prompt_vis.txt). 
<br><br>

## <a name="Usage"></a>🛠️ Usage

### Requirements

* Python 3.8 or later
* PyTorch 1.13.1 or later
* Transformers 4.26.1 or later
* Recommended: CUDA 11.7 or later
<br>

1. Repository Cloning and Dependency Installation

```bash
apt-get install git-lfs
git clone https://Kwai-Kolors/Kolors
cd Kolors
conda create --name kolors python=3.8
conda activate kolors
pip install -r requirements.txt
python3 setup.py install
```
2. Weights download（[link](https://huggingface.co/Kwai-Kolors/Kolors)）：
```bash
huggingface-cli download --resume-download Kwai-Kolors/Kolors --local-dir weights/Kolors
```
or
```bash
git lfs clone https://huggingface.co/Kwai-Kolors/Kolors weights/Kolors
```
3. Inference：
```bash
python3 scripts/sample.py "一张瓢虫的照片，微距，变焦，高质量，电影，拿着一个牌子，写着“可图”"
# The image will be saved to "scripts/outputs/sample_text.jpg"
```
4. Web demo：
```bash
python3 scripts/sampleui.py
```

### Using with Diffusers
Make sure you upgrade to the latest version(0.30.0.dev0) of diffusers: 
```
git clone https://huggingface/diffusers
cd diffusers
python3 setup.py install
```
**Notes:**
- The pipeline uses the `EulerDiscreteScheduler` by default. We recommend using this scheduler with `guidance scale=5.0` and `num_inference_steps=50`.
- The pipeline also supports the `EDMDPMSolverMultistepScheduler`. `guidance scale=5.0` and `num_inference_steps=25` is a good default for this scheduler.
- In addition to Text-to-Image, `KolorsImg2ImgPipeline` also supports Image-to-Image.

And then you can run:
```python
import torch
from diffusers import KolorsPipeline
pipe = KolorsPipeline.from_pretrained(
    "Kwai-Kolors/Kolors-diffusers", 
    torch_dtype=torch.float16, 
    variant="fp16"
).to("cuda")
prompt = '一张瓢虫的照片，微距，变焦，高质量，电影，拿着一个牌子，写着"可图"'
image = pipe(
    prompt=prompt,
    negative_prompt="",
    guidance_scale=5.0,
    num_inference_steps=50,
    generator=torch.Generator(pipe.device).manual_seed(66),
).images[0]
image.show()
```

### IP-Adapter-Plus

We provide IP-Adapter-Plus weights and inference code, detailed in the [ipadapter](./ipadapter/README.md).

```bash
# Weights download
huggingface-cli download --resume-download Kwai-Kolors/Kolors-IP-Adapter-Plus --local-dir weights/Kolors-IP-Adapter-Plus
```

```bash
# Inference：
python3 ipadapter/sample_ipadapter_plus.py ./ipadapter/asset/test_ip.jpg "穿着黑色T恤衫，上面中文绿色大字写着“可图”"

python3 ipadapter/sample_ipadapter_plus.py ./ipadapter/asset/test_ip2.png "一只可爱的小狗在奔跑"

# The image will be saved to "scripts/outputs/"
```

### ControlNet

We provide three ControlNet weights and inference code, detailed in the [controlnet](./controlnet/README.md).

```bash
# Weights download

# Canny - ControlNet
huggingface-cli download --resume-download Kwai-Kolors/Kolors-ControlNet-Canny --local-dir weights/Kolors-ControlNet-Canny

# Depth - ControlNet
huggingface-cli download --resume-download Kwai-Kolors/Kolors-ControlNet-Depth --local-dir weights/Kolors-ControlNet-Depth

# Pose - ControlNet
huggingface-cli download --resume-download Kwai-Kolors/Kolors-ControlNet-Pose --local-dir weights/Kolors-ControlNet-Pose
```

If you intend to utilize the depth estimation network, please make sure to download its corresponding model weights.
```
huggingface-cli download lllyasviel/Annotators ./dpt_hybrid-midas-501f0c75.pt --local-dir ./controlnet/annotator/ckpts
```

Thanks to [DWPose](https://IDEA-Research/DWPose/tree/onnx?tab=readme-ov-file), you can utilize the pose estimation network. Please download the Pose model dw-ll_ucoco_384.onnx ([baidu](https://pan.baidu.com/s/1nuBjw-KKSxD_BkpmwXUJiw?pwd=28d7), [google](https://drive.google.com/file/d/12L8E2oAgZy4VACGSK9RaZBZrfgx7VTA2/view?usp=sharing)) and Det model yolox_l.onnx ([baidu](https://pan.baidu.com/s/1fpfIVpv5ypo4c1bUlzkMYQ?pwd=mjdn), [google](https://drive.google.com/file/d/1w9pXC8tT0p9ndMN-CArp1__b2GbzewWI/view?usp=sharing)). Then please put them into `controlnet/annotator/ckpts/`.


```bash
# Inference：

python ./controlnet/sample_controlNet.py ./controlnet/assets/woman_1.png 一个漂亮的女孩，高品质，超清晰，色彩鲜艳，超高分辨率，最佳品质，8k，高清，4K Canny

python ./controlnet/sample_controlNet.py ./controlnet/assets/woman_2.png 新海诚风格，丰富的色彩，穿着绿色衬衫的女人站在田野里，唯美风景，清新明亮，斑驳的光影，最好的质量，超细节，8K画质 Depth

python ./controlnet/sample_controlNet.py ./controlnet/assets/woman_3.png 一位穿着紫色泡泡袖连衣裙、戴着皇冠和白色蕾丝手套的女孩双手托脸，高品质，超清晰，色彩鲜艳，超高分辨率，最佳品质，8k，高清，4K Pose

# The image will be saved to "controlnet/outputs/"
```


### Inpainting

We provide Inpainting weights and inference code, detailed in the [inpainting](./inpainting/README.md).

```bash
# Weights download
huggingface-cli download --resume-download Kwai-Kolors/Kolors-Inpainting --local-dir weights/Kolors-Inpainting
```

```bash
# Inference：
python3 inpainting/sample_inpainting.py ./inpainting/asset/3.png ./inpainting/asset/3_mask.png 穿着美少女战士的衣服，一件类似于水手服风格的衣服，包括一个白色紧身上衣，前胸搭配一个大大的红色蝴蝶结。衣服的领子部分呈蓝色，并且有白色条纹。她还穿着一条蓝色百褶裙，超高清，辛烷渲染，高级质感，32k，高分辨率，最好的质量，超级细节，景深

python3 inpainting/sample_inpainting.py ./inpainting/asset/4.png ./inpainting/asset/4_mask.png 穿着钢铁侠的衣服，高科技盔甲，主要颜色为红色和金色，并且有一些银色装饰。胸前有一个亮起的圆形反应堆装置，充满了未来科技感。超清晰，高质量，超逼真，高分辨率，最好的质量，超级细节，景深

# The image will be saved to "scripts/outputs/"
```

### IP-Adapter-FaceID-Plus

We provide IP-Adapter-FaceID-Plus weights and inference code, detailed in the [ipadapter_FaceID](./ipadapter_FaceID/README.md).

```bash
# Weights download
huggingface-cli download --resume-download Kwai-Kolors/Kolors-IP-Adapter-FaceID-Plus --local-dir weights/Kolors-IP-Adapter-FaceID-Plus
```

```bash
# Inference：
python ipadapter_FaceID/sample_ipadapter_faceid_plus.py ./ipadapter_FaceID/assets/image1.png "穿着晚礼服，在星光下的晚宴场景中，烛光闪闪，整个场景洋溢着浪漫而奢华的氛围"

python ipadapter_FaceID/sample_ipadapter_faceid_plus.py ./ipadapter_FaceID/assets/image2.png "西部牛仔，牛仔帽，荒野大镖客，背景是西部小镇，仙人掌，,日落余晖, 暖色调, 使用XT4胶片拍摄, 噪点, 晕影, 柯达胶卷，复古"

# The image will be saved to "scripts/outputs/"
```

### Dreambooth-LoRA

We provide LoRA training and inference code, detailed in the [Dreambooth-LoRA](./dreambooth/README.md).

```bash
# Training:
sh train.sh
```

```bash
# Inference：
python infer_dreambooth.py "ktxl狗在草地上跑"
```

<br><br>

## <a name="License"></a>📜 License & Citation & Acknowledgments

### License

Kolors weights are fully open for academic research. If you intend to use the Kolors model or its derivatives for commercial purposes under the licensing terms and conditions, please send the [questionnaire](https://Kwai-Kolors/Kolors/blob/master/imgs/可图KOLORS模型商业授权申请书.docx) to kwai-kolors@kuaishou.com to register with the licensor. If the monthly active users of all products or services made available by or for Licensee does not exceed 300 million monthly active users in the preceding calendar month, Your registration with the Licensor will be deemed to have obtained the corresponding business license; If, the monthly active users of all products or services made available by or for Licensee is greater than 300 million monthly active users in the preceding calendar month, You must request a license from Licensor, which the Licensor may grant to You in its sole discretion, and You are not authorized to exercise any of the rights under this Agreement unless or until We otherwise expressly grants You such rights.

 
We open-source Kolors to promote the development of large text-to-image models in collaboration with the open-source community. The code of this project is open-sourced under the Apache-2.0 license. We sincerely urge all developers and users to strictly adhere to the [open-source license](MODEL_LICENSE), avoiding the use of the open-source model, code, and its derivatives for any purposes that may harm the country and society or for any services not evaluated and registered for safety. Note that despite our best efforts to ensure the compliance, accuracy, and safety of the data during training, due to the diversity and combinability of generated content and the probabilistic randomness affecting the model, we cannot guarantee the accuracy and safety of the output content, and the model is susceptible to misleading. This project does not assume any legal responsibility for any data security issues, public opinion risks, or risks and liabilities arising from the model being misled, abused, misused, or improperly utilized due to the use of the open-source model and code.

### Citation
If you find our work helpful, please cite it!

```
@article{kolors,
  title={Kolors: Effective Training of Diffusion Model for Photorealistic Text-to-Image Synthesis},
  author={Kolors Team},
  journal={arXiv preprint},
  year={2024}
}
```

### Acknowledgments
- Thanks to [Diffusers](https://huggingface/diffusers) for providing the codebase.
- Thanks to [ChatGLM3](https://THUDM/ChatGLM3) for providing the powerful Chinese language model.
<br>

### Contact Us

If you want to leave a message for our R&D team and product team, feel free to join our [WeChat group](https://Kwai-Kolors/Kolors/blob/master/imgs/wechat.png). You can also contact us via email (kwai-kolors@kuaishou.com).

[![Star History Chart](https://api.star-history.com/svg?repos=Kwai-Kolors/Kolors&type=Date)](https://star-history.com/#Kwai-Kolors/Kolors&Date)
