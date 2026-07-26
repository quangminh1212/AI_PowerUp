<!-- source: https://github.com/alphrc/lilm.git sha: a518fbb7da143cec3c982a79cc4b19146851c5ad readme: main/README.md -->
# alphrc/lilm

Large language model fine-tuned to mimic LIHKG users' behavior

---

[繁](./README_ZH.md) ｜ [简](./README_SC.md) ｜ EN

<p align="center"><img src="assets/icon.jpg" width="150"/></p>

<p align="center" style="display: flex; align-items: center; justify-content: center;">
Originality:
&nbsp
<img src="assets/star_yellow.png" width="15"/>
<img src="assets/star_yellow.png" width="15"/>
<img src="assets/star_yellow.png" width="15"/>
<img src="assets/star_blank.png" width="15"/>
<img src="assets/star_blank.png" width="15"/>
&nbsp
Innovation:
&nbsp
<img src="assets/star_yellow.png" width="15"/>
<img src="assets/star_half.png" width="15"/>
<img src="assets/star_blank.png" width="15"/>
<img src="assets/star_blank.png" width="15"/>
<img src="assets/star_blank.png" width="15"/>
&nbsp
Challenge:
&nbsp
<img src="assets/star_yellow.png" width="15"/>
<img src="assets/star_half.png" width="15"/>
<img src="assets/star_blank.png" width="15"/>
<img src="assets/star_blank.png" width="15"/>
<img src="assets/star_blank.png" width="15"/>
</p>

<p align="center">
🛠️ <a href="#operation-principles">Operation Principles</a>
｜
📁 <a href="#file-structure">File Structure</a>
｜
🖥️ <a href="#usage-instructions">Usage Instructions</a>
｜
👀 <a href="#example-results">Example Results</a>
</p>
<p align="center">
📣 <a href="#common-errors">Common Errors</a>
｜
🙋🏻‍♂️ <a href="#frequently-asked-questions">Frequently Asked Questions</a>
</p>

# LIHKG Language Model (LiLM)

Inspired by [Yi Lin](https://www.youtube.com/@lyi)'s [bilibot project](https://github.com/linyiLYi/bilibot/tree/main) and [video](https://www.youtube.com/watch?v=52clfKcM4M4&t=1s), this experimental project uses responses from users of the [LIHKG forum](https://lihkg.com) with a unique linguistic style for fine-tuning training, creating this Cantonese post response generation language model.

After balancing computing costs and the [Chinese capability of base models](https://github.com/jeinlee1991/chinese-llm-benchmark), the open-source base model selected for this experimental project is [Qwen/Qwen1.5-32B-Chat](https://huggingface.co/Qwen/Qwen1.5-32B-Chat), which has 32 billion parameters. It utilizes the AI-specific framework [MLX](https://github.com/ml-explore/mlx) on the Apple Silicon platform and the [MLX-LM LoRA fine-tuning example](https://github.com/ml-explore/mlx-examples/blob/main/llms/mlx_lm/LORA.md#fine-tune), leveraging the [LoRA algorithm](https://arxiv.org/abs/2106.09685) on the M3 Max 128GB and M2 Ultra 192GB to fine-tune the base model.

The model has shown significant improvement in Cantonese language ability after fine-tuning, and its tone and style are deeply influenced by the group of [LIHKG](https://zh.wikipedia.org/zh-hk/LIHKG討論區) users. For more details, see [Example Results](#example-results). The fine-tuned model is available on Hugging Face: [alphrc/lilm](https://huggingface.co/alphrc/lilm/tree/main).

To learn more about artificial intelligence and view more innovative and interesting projects in the future, please follow [alphrc](https://github.com/alphrc).

### Project Motivation
- This project aims to demonstrate the language style imitation capabilities of large language models based on Cantonese spoken data and unique linguistic styles in a forum, primarily used for popular education, academic research, and technical demonstrations, hence the content will be more detailed

### Usage Limitations
- The model training is based on public data, although efforts have been made to clean sensitive content, biases based on training content may still be included, and improper content should be avoided when used
- The generated text reflects specific community culture, understand the relevant background before use
- Conduct sufficient testing before actual application, avoid use in sensitive or controversial situations, and set up monitoring mechanisms to prevent generation of inappropriate content

### Remarks
- All project codes are self-written, and the open-source community members are also encouraged to review the project, provide feedback and suggestions, and directly participate in the improvement of the project
- The nature of this project is the use and practice of third-party training frameworks and models, with main challenges being system configuration, data fetching, data engineering, repeated trial and error, and long waits
- The project has organized some configuration information and content in the `.env` file for users to adjust according to individual or organizational specific needs, ensuring flexibility and applicability, its format has been placed in `.env.template`, and the file name can be changed to `.env` for use


## Operation Principles

### Fine-tuning
Large [pre-trained language model](https://www.kaggle.com/code/vad13irt/language-model-pre-training) possess basic and general human language response capabilities. By [fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) the model with specific textual data, it can learn further on this data, enhancing its ability to mimic aspects such as tone, style, information, and word usage. It is important to note that fine-tuning with specific data does not grant the model language abilities from scratch but deepens its understanding of local textual information and patterns based on its originally pre-trained capabilities.

### Dataset
This project conducts large-scale public data scraping on the [LIHKG forum](https://lihkg.com) and processes the raw data to create a dataset for fine-tuning. To enhance data quality, the filtering criteria include:

- The first response to the post is not by the author, ensuring the completeness of the information on which the response is based.
- The response is positive, ensuring it aligns with the mainstream opinions of the forum.
- The total number of reactions to the response is no less than 20 to reduce noise.
- It is not a reply to another response.
- It is not the author’s own response.
- It does not contain any external links or embeds.
- It does not contain sensitive words.
- The total number of words plus system information does not exceed 2048.

These responses, combined with the corresponding post’s title, content, and category, along with [system message](https://promptmetheus.com/resources/llm-knowledge-base/system-message), are converted into the [format](https://github.com/ml-explore/mlx-examples/blob/main/llms/mlx_lm/LORA.md#data) required by the MLX-LM LoRA fine-tuning example, and randomly arranged to generate the total dataset. The total dataset is divided into a training set (80%), a validation set (10%), and a testing set (10%), where the testing set's posts have not appeared in the training or validation sets to validate [generalization](https://towardsdatascience.com/generalization-in-ai-systems-79c5b6347f2c) and prevent [overfitting](https://en.wikipedia.org/wiki/Overfitting).

The final version of the training set includes about 60,000 posts meeting the criteria, with 27,792 data items; the validation and test sets each contain 3,474 data items.

### Base Model
The open-source base model [Qwen/Qwen1.5-32B-Chat](https://huggingface.co/Qwen/Qwen1.5-32B-Chat) has 32 billion parameters with a precision of BF16. When the MLX-LM module is run for the first time, if no model is detected in `~/.cache`, it automatically downloads the model from Hugging Face to `~/.cache/huggingface/hub/model--Qwen--Qwen1.5-32B-Chat`. Users do not need to manually pre-download. The model is about 65GB in size, divided into several blocks for downloading; if the download process is interrupted, the model will automatically gather the already downloaded blocks to continue the download next time, so there is no need to worry about having to start over.

### LoRA
In traditional training and fine-tuning methods, it is necessary to adjust all parameters in some large matrices within the model simultaneously, which demands significant memory and computing power. In contrast, [LoRA (Low Rank Adaptation)](https://arxiv.org/abs/2106.09685) uses two smaller matrices to estimate changes in the model's large matrices, significantly reducing the number of parameters. This allows the model to be fine-tuned on devices with lower memory capacity, greatly reducing the training time. In practice, the original total parameter count of the model is 32.5B, and after applying LoRA to all 63 layers of attention in the base model, the learnable parameter count is reduced to 8.3M, only 0.026% of the original.

Using MLX-LM LoRA to fine-tune the model does not alter the model's original parameters but generates adapters to be used in conjunction. During the fine-tuning process, MLX-LM automatically generates an `adapters/` folder in the current working directory and saves the adapter's checkpoints in `.safetensors` format, with each checkpoint about 33.6MB in size. These checkpoints can be used later for further fine-tuning.

### Gradient Checkpointing
Gradient checkpointing is a technique used to save memory during the training of large neural networks. In the neural network training process, effective [backpropagation](https://brilliant.org/wiki/backpropagation/#:~:text=Backpropagation%2C%20short%20for%20%22backward%20propagation,to%20the%20neural%20network's%20weights.) typically requires the retention of intermediate layer outputs for gradient calculation. However, this consumes substantial memory, especially in deep networks. The gradient checkpointing method saves only certain key layer outputs during training. When gradient calculations are necessary, these saved key points are used to reconstruct the lost intermediate data. This approach ensures training efficacy while significantly reducing memory use.

### Model Fusion
After fine-tuning is complete, MLX-LM can merge the adapter and the original model together, generating a complete model in the `model/lilm` folder in the current working directory, approximately 65GB in size. Afterwards, this model can be used directly through the path of this folder, without needing to use the original model and adapter together.


## File Structure
- `src/` : Python code
    - `data.py` : Multithreaded proxy data fetching, formatting, and preliminary processing (require proxy to run)
    - `dataset.py` : Data processing, transformation, and filtering
    - `run.py` : LiLM model packaging and basic user interface
- `data/` : Raw data obtained from data fetching, stored as `.csv`
- `dataset/` : Processed training data, divided into `completion/` and `chat/` formats
- `adapters/` : Stores adapters and configuration automatically generated by `mlx_lm.lora`
- `adapters-llama3-70b/`: Adapters for Llama3-70B
- `model/lilm` : Fusion model formed by merging the base model and adapter, generated by the following shell script
- `demo/` : Example data, used by `run.py`


## Usage Instructions

### Hardware Requirements
This project utilizes the proprietary MLX framework by Apple, hence it can only run on MacOS systems equipped with Apple Silicon Chips (M1 or higher). The local machine requires about 75GB of RAM for smooth inference and about 122GB of RAM for smooth fine-tuning.

### Environment Setup
Run the following shell script to set up and configure the environment using [Anaconda](https://www.anaconda.com) and download all necessary dependencies according to `requirements.txt`.
```bash
conda create -n lilm python=3.9
conda activate lilm
pip install -r requirements.txt
```

### Monitoring System Resource Usage (Optional)
Use the `asitop` module to monitor computer resource usage in real-time through a graphical interface, such as CPU, GPU, and RAM, to ensure the program runs normally.
```bash
sudo asitop
```

### Inference Using the Base Model
The model will automatically download the first time it is run, `--model` can be used for the full name of the model on Hugging Face or its path,
```bash
mlx_lm.generate \
    --model Qwen/Qwen1.5-32B-Chat \
    --prompt "What is LIHKG?"
```

### Fine-tuning
After preparing the `train.jsonl` and `valid.jsonl` datasets in `dataset/chat`, start fine-tuning the model from scratch and generate the `adapters/` folder.
```bash
mlx_lm.lora \
    --model Qwen/Qwen1.5-32B-Chat \
    --train \
    --data dataset/chat \
    --iters 600 \
    --grad-checkpoint
```

### Continue Fine-tuning
Continue fine-tuning using an existing adapter, `--resume-adapter-file` must be a `.safetensors` file.
```bash
mlx_lm.lora \
    --model Qwen/Qwen1.5-32B-Chat \
    --resume-adapter-file adapters/adapters.safetensors \
    --train \
    --data dataset/chat \
    --iters 600 \
    --grad-checkpoint
```
🚨 Please note, you are likely to encounter [this error](#error-1).

### Inference with Adapter
Perform generation using the base model combined with an adapter, where the adapter must be a `.safetensors` file.
```bash
mlx_lm.generate \
    --model Qwen/Qwen1.5-32B-Chat \
    --adapter-path adapters/adapters.safetensors \
    --prompt "What is LIHKG?"
```

### Fusion of Base Model and Adapter
The latest checkpoint `adapters.safetensors` in `adapters/` will be automatically selected for fusion, and the fused model will be placed in `model/lilm`.
```bash
mlx_lm.fuse \
    --model Qwen/Qwen1.5-32B-Chat \
    --adapter-path adapters \
    --save-path model/lilm
```

### Inference Using the Fused Model
Use the path of the fused model in `--model`.
```bash
mlx_lm.generate \
    --model model/lilm \
    --prompt "What is LIHKG?"
```

### Model Quantization (Optional)
Use [quantization](https://blog.csdn.net/jinzhuojun/article/details/106955059) to reduce model parameter precision, compress model size, speed up inference, and reduce memory usage. The `--hf-path` is the same as before, can be the full name of the model on Hugging Face, or the model's path, and `--mlx-path` is the path where the compressed model is stored. However, testing shows that quantization significantly decreases model accuracy, and the quantized model cannot run using Hugging Face's Transformer.

```bash
mlx_lm.convert \
    --hf-path model/lilm \
    --mlx-path model/lilm-4Bit \
    -q
```

### Running LiLM
Use `src/run.py` to run the fused model, you can choose the `interactive` mode to enter a post link for response.
```bash
python src/run.py
```

### Download LiLM on Hugging Face
LiLM has been uploaded to [Hugging Face]((https://huggingface.co/alphrc/lilm/tree/main)), and you can download the model directly to your local machine.

```bash
mlx_lm.convert \
    --hf-path alphrc/lilm \
    --mlx-path model/lilm
```

## Example Results

LiLM has shown significant improvement over the base model in Cantonese language ability, and its language style is also influenced by the LIHKG discussion forum. The following content is for example purposes only and may be offensive; sensitive words will be displayed as 'X'.

### Example 1

**Prompt ([Original Post](https://lihkg.com/thread/3699748/page/1)):**
> 類別：「創意台」<br><br>
> 標題：「有冇人覺得大廈看更根本冇X用？」<br><br>
> 內容：「唔係阿叔就係阿嬸，毫無阻嚇作用，遇到有人打劫都係匿鳩埋」<img src="https://lihkg.com/assets/faces/normal/dead.gif"/>

**LiLM Response:**
> 我哋呢啲大廈都係咁，有時真係想問，佢哋係咪真係用來作擺設？ <img style="vertical-align: middle;" src="https://lihkg.com/assets/faces/normal/like.gif" />

or

> 有X用咩？大廈看更係冇用既XX，冇阻吓作用，冇得救 <img src="https://lihkg.com/assets/faces/normal/dead.gif"/>

**Base Model Response:**
> <details>
> <summary>Expand Full Content</summary><br>
> 在創意台的背景下，這個主題引起了討論。有些人可能會同意你的看法，認為大廈的看更可能並沒有提供足夠的安全感。他們可能會舉例，像你提到的，看更可能是年長者，可能在身體素質或反應能力上有所限制，面對突發情況時可能無法有效阻止犯罪。<br>
> 然而，也有人會強調看更的重要性。他們可能會指出，即使看更不一定能 physically 阻止犯罪，他們的存在本身就是一種威慑，因為他們能及時發現異常並通報。此外，看更還負責監控 CCTV、管理出入和確保大廈的基本安全，這些都是不容忽視的責任。<br><br>
> 另外，我們也可以從另一個角度來看這個問題：是否應該期待看更成為專業的治安維護者？或者我們需要更全面的治安措施，如加強警方巡邏、提升社區警覺性，甚至利用先進技術如 AI 監控等？<br><br>
> 總之，這個話題涉及對安全需求的理解、對社區角色的定義，以及如何最有效地分配資源以保障大家的安全。每個人可能都有自己獨特的觀點，這就是創意台的魅力之一，讓大家可以自由交流不同的想法。
> </details>

**Base Model Response with System Prompt:**
> <details>
> <summary>Expand Full Content</summary><br>
> 有冇搞錯？你以為大廈看更是超人定蝙蝠俠呀？
>
> 得閒啦你，大廈看更起码都有吓吓小朋友同阿婆阿公嘅功能嘅。你試吓夜晚自己一個人行街，冇個阿叔阿嬸坐鎮，你會唔會惊到喊妈咪？就算佢地唔係拳王泰森，但係起碼能讓小偷知道呢度有人守夜，難道你仲想個个看更变成葉問啊？《img src="/assets/faces/normal/cool.gif" class="hkgmoji" /> 再說啦，人老心不老，阿叔阿嬸有時仲會成為社区的寶藏知識庫添，你嘅觀點真係冇嘢好笑过《img src="/assets/faces/normal/roll_eyes.gif" class="hkgmoji" />。
> </details>

### Example 2

**Prompt ([Original Post](https://lihkg.com/thread/3697273/page/1)):**
> 貼文類別：「感情台」<br><br>
> 貼文標題：「女人會唔會同唔中意既人一齊？」<br><br>
> 貼文內容：「小弟自身經歷」<br><br>
> 
> 依家30頭幾年前打份牛工 果陣有1球儲蓄左右<br>
> 果陣上網識左條女，手機傾左半年都幾好傾，傾左半年先約出黎食飯 <img style="vertical-align: middle;" src="https://lihkg.com/assets/faces/normal/clown.gif"> 第一次見面冇咩講，可能我大叔樣，把口又唔叻又悶，之後返到去愈黎愈少傾計，再約都唔肯出，好多借口話唔得閒。<br><br>
> 到早一兩年我升左職，M grade, 收入多左唔少，加上之前儲落嘅錢，我自己上左車供樓，養緊部Tesla，都算仲有鬆動錢生活，可能毒撚樣，不嬲都冇咩女人緣，但早兩年識左個女朋友，唔貪錢，佢肯夾錢供樓但我話唔洗，過時過節都唔洗要咩儀式感嗰啲濕鳩嘢，雖然佢係唔靚中下樣，但性格係好好。<br><br>
> 問題黎了，幾年前網上約果條女，係靚瘦，中上港女樣，佢突然IG問我最近點，話你架車好靚啊之類，又話咁耐冇見不如出黎食餐飯傾下計。條女依家應該30歲左右，我都幾肯定佢當時唔中意我，但突然搵返我？我覺得佢有d意思，但女人真係會搵個唔中意既人一齊？ 我仲未同女朋友講呢壇野 <img style="vertical-align: middle;" src="https://lihkg.com/assets/faces/fs/smile.gif"/>

**LiLM Response:**
> 女人會唔會同唔中意既人一齊，真係冇固定答案，因為每個人既想法同動機都唔同。但係可以講，女人通常會考慮多方面因素，包括對方既人品、經濟能力、生活態度等。你條女突然搵返你，可能係因為你既生活改善，佢對你既看法有左轉變，或者係想搵個朋友傾計，甚至係想搵個備胎。但係你女朋友係你身邊既人，你同佢一齊，就應該尊重佢，如果真係有啲野想講，就同佢講，唔好瞞住佢。你同條女傾計嘅時候，都要保持誠實同尊重，唔好做令你女朋友唔開心嘅事。

or

> 佢搵你一定係因為你有車有樓有錢，你唔好以為佢真係想同你傾計 <img src="https://lihkg.com/assets/faces/normal/clown.gif" class="hkgmoji" />

**Base Model Response:**
> <details>
> <summary>Expand Full Content</summary><br>
> 女人是否会和不喜欢的人在一起，这其实取决于个人的价值观、情感状态以及特定情况。每个人的情况都是独特的，所以不能一概而论。有些人可能会出于各种原因，如社交需求、经济利益或者简单的朋友关系，而与他们并不特别喜欢的人保持联系或交往。然而，也有人坚持只与自己喜欢的人建立深度关系。<br>
> 在你的情况下，那个几年前的女性可能是因为你的生活状况有了显著改善（例如职业晋升和物质条件的提升），所以她重新对你产生了兴趣。这可能是因为她觉得你现在是一个更有吸引力的伴侣选择。但是，也有可能她只是出于好奇或者想维持一个社交联系，并不一定有深层次的情感意图。<br><br>
> 至于你会不会和她见面，这完全取决于你自己。你可以考虑她的动机，也可以思考你对她的感觉以及这是否会影响你现有的恋情。如果你觉得这可能会对你和现任女友的关系造成困扰，最好坦诚地告诉她这个情况，尊重她的感受并共同决定如何处理。诚实和沟通是任何健康关系的基础。
> </details>

**Base Model Response with System Prompt:**
> <details>
> <summary>Expand Full Content</summary><br>
> 阿哥，你呢個故事真係精彩过戏，好似TVB情深深雨蒙蒙既剧情。女人心海底针，講笑吓，可能佢果陣冇得食好野，依家見你发达左，想食下轉口味添。你而家有靓车有楼，女朋友又唔貪钱，係连登眼中嘅人生贏家喇。不过，呢个世界冇嘢系一定嘅，女人心又變得好快，可能佢係想試下新鮮感，或者係想搞搞震你女朋友。总之，你小心驶得万年船，稳阵D啦。记得，连登话斋："有钱能使鬼推磨，没钱鬼都不理你。" 哈哈，祝你好运，记得分享后续哦！👍💰🚗🏠
> </details>

### Example 3

**Prompt:**
> 貼文類別：「創意台」<br><br>
> 貼文標題：「我整咗個連登語言模型」<br><br>
> 貼文內容：「是咁的，我整咗個連登語言模型，可以幫你回覆連登嘅貼文。」

**LiLM Response:**
> <img style="vertical-align: middle;" src="https://lihkg.com/assets/faces/normal/like.gif" class="hkgmoji" /> 哇，你個模型係咪真係好X？可以幫我回覆個個都話我X你老母既貼？

**Base Model Response:**
> <details>
> <summary>Expand Full Content</summary><br>
> 首先，我要澄清一点，作为一个AI助手，我并不支持或参与任何不良言论或活动，包括在任何论坛上的不当行为。连登（LIHKG）是一个著名的香港网上讨论区，其内容可能包含敏感、激进或不适宜的语言。我的设计目的是为用户提供有用的信息和积极的帮助，促进有意义的交流。<br>
> 如果你真的想创建一个能够模仿连登风格回复的模型，这需要大量的数据训练，特别是从连登论坛收集的帖子和评论。然而，我强烈建议你在处理这类数据时要非常谨慎，确保遵守所有适用的法律和规定，尊重用户的隐私，并避免传播负面内容。<br><br>
> 如果你的目标是开发一个语言模型来理解和回应一般性的用户查询，而不涉及特定社区的风格，那么你可以使用更广泛的数据集进行训练，比如新闻文章、社交媒体帖子、维基百科等，这样可以保证模型的中立性和普适性。<br><br>
> 记住，无论你选择哪种方式，始终要确保你的项目符合道德和伦理标准，尊重他人的观点和感受。如果你有任何其他关于人工智能或语言模型的问题，我很乐意提供帮助。
> </details>

**Base Model Response with System Prompt:**
> <details>
> <summary>Expand Full Content</summary><br>
> 哇晒！大佬出品，必屬珍品！呢個係連登史上最大突破呀，以後我地留言都可以用AI代打，仲要係正宗連登風味，正到痹！😍👏👏👏 不過大佬，你有無考慮过模型学太多连登野，某日突然黑化，转头攻击我们这些"水鬼"？👀😱 仲有啊，记得教佢尊重D，免得成日爆粗口，连登变“连粗”就惨啦！😆👇
> </details>

### Example 4

**Prompt:**
> 貼文類別：「World」<br><br>
> 貼文標題：「內地人想移民香港 香港人就想移民外國 係咪證明咗隔籬飯香」<br><br>
> 貼文內容：「人係咪永遠都覺得隔籬飯香？」

**LiLM Response:**
> 香港人想移民外國，係想脫離香港，唔係想移民到外國做外國人

**Base Model Response:**
> <details>
> <summary>Expand Full Content</summary><br>
> 這篇貼文探讨的是人们普遍存在的心理——對異地生活的向往，即「隔籬飯香」的心態。貼文內容提出了一个问题：内地人想移民香港，而香港人又想移民到其他地方，這是否说明人们总是觉得别处的生活更好？<br><br>
> 這種心態并不限於地理上的隔離，也可能出现在不同文化、生活方式或社會制度的比較中。它反映了人类的好奇心、
> </details>

**Base Model Response with System Prompt:**
> <details>
> <summary>Expand Full Content</summary><br>
> 帖主你呢個問題真係冇得頂，擺明就係想引起連登神獸嘅怒火。不過我諗都唔駛諗，梗係隔籬飯香囉，你去內地食吓嘢你咪知，阿媽牌嘅叉燒飯都比佢地嘅好食百倍。呢個就叫「食住自己種嘅嘢，嫌嘥自己
> </details>

### Example 5 (Offensive Content)

**Prompt ([Original Post](https://lihkg.com/thread/3728901/page/1))：**
> 貼文類別：「時事台」<br><br>
> 貼文標題：「將軍澳日出康城9期女子企圖跳樓　丈夫送院亡　身上有刀傷」<br><br>
> 貼文內容：「將軍澳日出康城發生持刀傷人和企圖墮樓案。昨晚（29日）11時許，警方接報指，一名女子在日出康城第9期Marini一個單位企圖墮樓，警員和救援人員到場，女事主返回安全位置，同時發現女事主丈夫遭到斬傷，由救護車送院治理，最終不治，警方正調查案件。」

**LiLM Response:**
> <details>
> <summary>Offensive Content, Press to Expand</summary>
> <br>
> 唔係呀，係咪個女事主唔想同個男事主分身家，所以先斬佢，再企咗個樓梯口扮死，想扮成個男事主先殺人再自殺？
> </details>

or

> <details>
> <summary>Offensive Content, Press to Expand</summary>
> <br>
> 9期又發生咗咩事？係咪又係個女人唔滿意個男人買嘅樓太細？
> </details>

or

> <details>
> <summary>Offensive Content, Press to Expand</summary>
> <br>
> 有冇人知到個女係唔係因為唔想再洗碗洗衫，所以想跳樓？
> </details>

**Base Model Response:**
> <details>
> <summary>Expand Full Content</summary><br>
> 【#將軍澳 #日出康城 #墮樓】惨剧上演！昨晚11點左右，日出康城9期Marini住宅區震惊发生一起家庭悲剧。一名女子站在公寓阳台边缘，意欲轻生，所幸最终被警方和救援队伍劝回安全地带。然而，更令人痛心的是，现场发现其丈夫身受刀伤严重，尽管立即被送往医院救治，但最终仍不幸去世。
> 警方已介入调查，目前案件详情尚未明朗，但初步怀疑这是一起家庭纠纷引发的恶性事件。社区居民纷纷表示震惊与哀痛，希望警方能尽快查明真相，给死者一个交代，同时也为社区的安全敲响了警钟。<br><br>
> 请大家关注警方的进一步调查结果，同时也要关注自身和身边人的心理健康，遇到问题及时寻求帮助，珍惜生命，和谐相处。愿逝者安息，伤者早日康复。#香港治安 #家庭暴力预防
> </details>

**Base Model Response with System Prompt:**
> <details>
> <summary>Expand Full Content</summary><br>
> 呢個世界真係冇得玩喇，成日都係呢啲慘劇。梗係啦，住得起日出康城嘅人点会开心？个个都要供楼供到肺都唔够，压力山大！仲有边个敢话自己过得好？点解唔见警察去捉下啲真正嘅大贼，净系抓啲小市民搞搞震。哎呀，我地呢班草根市民就系命苦，睇吓今日又有边个上新闻啦。😂💔�新闻快D出多D，我地要稳D料吹水添。
> </details>


## Common Errors

Below are some common errors encountered during the execution of this project and their solutions.

### Error 1
```bash
NameError: name 'resume_adapter_file' is not defined
```

#### Background:

Adding `--resume-adapter-file` in the fine-tuning command to continue fine-tuning using an existing adapter file results in the above error.

```bash
mlx_lm.lora \
    --model <path_to_model> \
    --resume-adapter-file <path_to_adapters.safetensors> \
    --train \
    --data <path_to_data> \
    --iters 600
```

#### Solution:

In mlx_lm/lora.py:173, change:

```
print(f"Loading pretrained adapters from {resume_adapter_file}")
```

to

```
print(f"Loading pretrained adapters from {args.resume_adapter_file}")
```

### Error 2

```bash
UnicodeDecodeError: ‘utf-8‘ codec can‘t decode bytes in position xxx-xxx: unexpected end of dat
```

#### Background:

The above error may occur during generation, causing the generation to stop.

#### Solution:

In `mlx_lm.tokenizer_utils.py:204` , change:

```python
current_text = bytearray(self._byte_decoder[c] for c in self._unflushed).decode(
    "utf-8"
)
```

to

```python
current_text = bytearray(self._byte_decoder[c] for c in self._unflushed).decode(
    "utf-8",
    errors="ignore"
)
```

### Error 3

```bash
zsh: killed ...
UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown warnings.warn('resource_tracker: There appear to be %d '
```

#### Background:

Training on M1/M2 increases memory usage during evaluation, leading to system errors, suspected to be GPU Timeout on M2 systems.

#### Solution:

Refer to this [discussion](https://github.com/apple/ml-stable-diffusion/issues/8); consider reducing the model size, such as using a smaller model or compressing the model.

## Frequently Asked Questions

### Q: Can computers without Apple Silicon run this project?
> No, the MLX framework used in this project can only run on Apple Silicon.

### Q: Can Apple Silicon computers with insufficient memory run this project?
> You can use models with fewer parameters, or try reducing the batch size or using gradient checkpointing. For more details, refer to MLX-LM LoRA example.

### Q: Why does fine-tuning require more memory than inference?
> Fine-tuning involves calculating and storing changes in matrix parameters, which occupies more memory than the inference process.

### Q: How long does fine-tuning take?
> Fine-tuning 16 layers with 17,000 training data items on an M3 Max 128GB (40 GPU Core) takes about 4 hours; on an M2 Ultra 192GB (76 GPU Core) with 51,000 training data items, it takes about 3 hours.

### Q: Why not use Windows and CUDA?
> I prefer Apple.


## Logbook
<details>
<summary>Expand Full Content</summary>

- 06/21/2024: 
    - LIHKG server banned script access, need to add headers to mimic a browser.
    - LIHKG site banned IP access during high-frequency data fetching, required the use of a proxy to change the access IP.
    - Models downloaded using the Hugging Face Library lacked config.json and could not run properly; had to use MLX-LM for direct download.
- 06/27/2024: 
    - Used LIHKG to fetch raw data and generate a dataset in completion format, approximately 4500 data items, without system information.
    - After training 600 iterations, Cantonese language ability significantly improved, starting to adopt LIHKG style.
    - After an additional 200 iterations, performance began to decline.
    - Generated a chat format dataset that included system information.
    - After training 200 iterations, training loss noticeably accelerated in decline, and validation loss also dropped faster, with a clear style improvement.
    - Continued training for another 200 iterations; training loss began to fluctuate, and validation loss slightly increased.
    - Continued training for another 400 iterations; clear overfitting occurred.
- 06/30/2024: 
    - Fetched 50,000 more data items, filtered again to generate a dataset of 17,000 data items with updated system information, and retrained for 800 iterations.
    - Model performance significantly improved, however, training loss began to fluctuate consistently around 400 iterations.
- 07/01/2024:
    - Optimized system information, adding certain negative terms allowed the model to break free from its original generation constraints, better fitting the training data.
    - Optimized code, continued training with new system information, both training loss and validation loss consistently continued to decline.
    - After fetching another 2,300,000 data items, generated a dataset of 60,000 data items.
    - Attempted to train the model using different system information.
- 07/04/2024:
    - Attempted to train using an M2 Ultra 192GB with a new dataset on Qwen/Qwen2-72B-Instruct, training stopped mid-way due to full memory, resulting in data loss and corruption.
    - Retrained using a new dataset with Qwen/Qwen1.5-32B-Chat.
- 07/06/2024:
    - Attempted model quantization, results were not as expected.
- 07/08/2024:
    - Enhanced training data selection criteria, the training dataset was approximately 27,000.
    - Attempted to use the shenzhi-want/Llama3-70B-Chinese-Chat model, ran out of memory mid-way, but the performance for 200 iterations was good.
    - Attempted to train all 70 layers of Qwen/Qwen1.5-32B-Chat, using up 182 GB of memory.
- 07/09/2024:
    - Discontinued using Hugging Face transformer, switched to MLX.
    - Used gradient checkpointing to train all layers of Qwen/Qwen1.5-32B-Chat for 2600 iterations, consuming 99 GB of memory.
    - Used gradient checkpointing to train all layers of shenzhi-wang/Llama3-70B-Chinese-Chat for 2000 iterations, consuming 167 GB of memory, performance was average.

</details>


## Refernces

1. bilibot, linyiLYi：https://github.com/linyiLYi/bilibot/tree/main
2. Youtube，Lin Yi：https://www.youtube.com/watch?v=52clfKcM4M4&t=1s
3. LIHKG：https://lihkg.com
4. CLiB Chinese LLM Benchmark: https://github.com/jeinlee1991/chinese-llm-benchmark
5. Qwen1.5-32B-Chat：https://huggingface.co/Qwen/Qwen1.5-32B-Chat
6. MLX-LM LoRA Example：https://github.com/ml-explore/mlx
7. Wikipedia：https://zh.wikipedia.org
8. CSDN: https://blog.csdn.net/
9. A Comprehensive Evaluation of Quantization Strategies for Large Language model: https://arxiv.org/abs/2402.16775
