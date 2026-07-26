<!-- source: https://github.com/UmiMarch/OpenVideo.git sha: 3556d49d840175d692d0dbaa62894dfbfe0a80f8 readme: main/README.md -->
# UmiMarch/OpenVideo

OpenVideo specializes in the domain of text-to-video generation, with the goal of providing high-quality and diverse video datasets to AI researchers globally. 

---

<h1 align="center">
<img src="docs/assets/openvideo-logo2.png" width="600">
</h1><br>


[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-OpenVideo-yellow)](https://huggingface.co/OpenVideo)
[![ModelScope](https://img.shields.io/badge/ModelScope-OpenVideo-purple)](https://www.modelscope.cn/organization/OpenVideo)
[![OpenDataLab](https://img.shields.io/badge/OpenDataLab-OpenVideo-blue)](https://opendatalab.com/OpenDataLab/OpenVideo)
[![PyPi version](https://badgen.net/pypi/v/openvideo/)](https://pypi.org/pypi/openvideo/)
[![PyPI pyversions](https://img.shields.io/badge/dynamic/json?color=blue&label=python&query=info.requires_python&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fdata4co%2Fjson)](https://pypi.python.org/pypi/openvideo/) 
[![Downloads](https://static.pepy.tech/badge/openvideo)](https://pepy.tech/project/openvideo)
[![GitHub stars](https://img.shields.io/github/stars/UmiMarch/OpenVideo.svg?style=social&label=Star&maxAge=8640)](https://GitHub.com/UmiMarch/OpenVideo/stargazers/)

OpenVideo specializes in the domain of text-to-video generation, with the goal of providing high-quality and diverse video datasets to AI researchers globally. In addition, it offers comprehensive tools for data collection, cleaning, and annotation, thereby contributing to the advancement of the artificial intelligence industry.

[中文主页](./README_ZH.md)

## 📚Dataset


|   Source | Resolution | Hours |  Clips |
| :--------: | :--: | :--: | :---------: |
| Pexels-Raw | 720p | 672h | 106k+ clips |


### Download：

From [ModelScope](https://www.modelscope.cn/datasets/OpenVideo/pexel-0808-complete-final-test)：

```
bash git clone https://user_id:access_token@www.modelscope.cn/datasets/OpenVideo/pexel-0808-complete-final-test.git
```

From [Huggingface](https://huggingface.co/datasets/OpenVideo/pexel-0808-complete-final-test)：

```
bash git clone https://user_id:access_token@huggingface.co/datasets/OpenVideo/pexel-0808-complete-final-test
```

(user_id is your username, and access_token needs to be generated in the settings)


### Script:

```
python ./openvideo/video/preprocess/utils/decode_parquet_file.py --parquet_dir your_parquet_path --save_dir your_save_path
```


## ⚡Tools


You can install this package via PyPI by entering the following command in the terminal:

```bash
$ pip install openvideo
```

Alternatively, you can obtain the latest version from GitHub:

```bash
$ pip install -U https://github.com/UmiMarch/OpenVideo/archive/master.zip # with --user for user install (no root)
```

The dependencies for `OpenVideo` are as follows:

```
huggingface_hub>=0.22.2
tqdm>=4.66.1
wget>=3.2
requests>=2.31.0
aiohttp>=3.9.3
async_timeout>=4.0.3
moviepy>=1.0.3
opencv-python>=4.9.0.80
selenium>=4.19.0
scenedetect>=0.6.3
texttable>=1.7.0
bs4>=0.0.2
```

### Video Download

* Mixkit [https://mixkit.co/free-stock-video/](https://mixkit.co/free-stock-video/)
```python
from openvideo.video.fetch import MixkitVideoFetch
 
mixkit_fetch = MixkitVideoFetch(root_dir="your/video/save/path")
mixkit_fetch.download_with_category_page_idx(
    category="sky", # Video category
    page_idx=1, # Start downloading from this page
    start_idx=22, # Start downloading from this video
    platform="linux" # Running platform
)
```

* Pixabay [https://pixabay.com/zh](https://pixabay.com/zh)
```python
from openvideo.video.fetch import PixabayVideoFetch

pixabay = PixabayVideoFetch("your/video/save/path")
pixabay.download(
    chrome_exe_path=r"your/chrome/exe/path",
    username="your/pixabay/username",
    password="your/pixabay/password",
    headless=False,
    platform="windows" # Currently only supports Windows
)
```

* Pexels [https://www.pexels.com/](https://www.pexels.com/)
```python
from openvideo.video.fetch import PexelsVdieoFetch, PexelsAPI

# Step 1: Call the API to obtain video links
pexels_api = PexelsAPI(
    api="your/pexels/api", 
    save_path="pexels_api.npy"
)
pexels_api.fetch_api(
    start_page=1, # Starting page
    end_page=2, # Ending page
    save_api_dict_every_pages=1 # Save the API dictionary every n pages
)

# Step 2: Download videos
pexels = PexelsVdieoFetch("pexels")
pexels.download(
    api_npy_save_path="pexels_api.npy", 
    chrome_exe_path=r"your/chrome/exe/path",
    headless=False
)
```

### Video Annotation Platform

We have developed a [video annotation platform]((https://huggingface.co/spaces/OpenVideo/GPT4o-Azure-Caption-Pixel)) based on the Rust programming language, designed to efficiently generate labels for various media types, including images and videos. This platform supports the invocation of state-of-the-art AI models such as GPT-4o, Gemini, and Claude3, and offers flexible configuration options. It is designed for high performance, capable of processing 100 queries per second, with task processing capacity scalable to 200 million queries. Utilizing 100 API accounts, this tool can synthesize a dataset containing 200,000 videos within 8 hours. All outputs are categorized and organized by model and prompt, ensuring a clear structure for subsequent research and application integration.

![image-20250123193428569](./docs/assets/caption_platform.png)

(If display issues occur, please try using other browsers. e.g. Edge.)


### Annotation Validation Platform

We provide an [annotation validation platform](https://huggingface.co/spaces/OpenVideo/AIL-Caption-lalala-Dup) where users can view, validate, and modify annotations for already annotated video datasets.

**Usage:**


1. Open the HuggingFace link and enter your [personal token](https://huggingface.co/settings/tokens).

2. Play videos, view the corresponding annotation texts, modify them, than switch to the next video.

   ![openvideo_tagger](./docs/assets/openvideo_tagger.png)


**For custom datasets:**

1. The dataset and code must be on the same platform (e.g., the dataset is hosted on HuggingFace).

2. Modify the dataset path in [run.py](https://huggingface.co/spaces/OpenVideo/AIL-Caption-lalala-Dup/blob/main/run.py#L7).

### Data Migration

We provide a general-purpose [data migration platform](https://huggingface.co/spaces/OpenVideo/HF_To_MS) for transferring datasets from HuggingFace to ModelScope, facilitating access and usage of datasets across different regional networks.

**Usage：**

Enter your HuggingFace access token & dataset path, ModelScope access token & repository directory, then click `Submit` to run the dataset migration from HuggingFace to the corresponding ModelScope repository automatically.

![data_transfer](./docs/assets/data_transfer.png)


## 👨‍💻 Contributors

Crawling Algorithms：@yangming @heatingma @ZZY @晚来风雪

Video Download: @yangming @晚来风雪 @杰杰杰

Data Cleaning：@一马平川  @zjukop @伊小布

Prompt: @Tiger.C @dpyneo @巧克力

Labeling: @YUE @zjukop

Validation Platform: @YUE @晚来风雪

Data Migration: @晚来风雪 @heatingma

Manual Validation: @一马平川 @dpyneo @杨嘉昊 @flipped @yi @believe @思恩

Project Research: @dingby @believe

Aesthetic Guidance: @图拉 @杨嘉昊

Documentation: @ZZY @枪枪

Project Coordination: @巧克力


## 🙏 Acknowledgments

Server/Financial Support: Li Bai AI Lab

Storage: HuggingFace, ModelScope, OPENDataLab

Techno-sharing：@shoulder @王铁震 @杨欢 @新年京

Discussion：@前仰跳投 @浮羽 @MYX @Winniy @GUI @Planet

## ✨ Connection

![connect](./docs/assets/connect.png)

## ©️ License

This project is licensed under the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hans) open-source license.




