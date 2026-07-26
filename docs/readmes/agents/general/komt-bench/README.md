<!-- source: https://github.com/LG-AI-EXAONE/KoMT-Bench.git sha: 56d4f3af437543dce39f08aecfb818abed81210d readme: main/README.md -->
# LG-AI-EXAONE/KoMT-Bench

Official repository for KoMT-Bench built by LG AI Research

---

# KoMT-Bench

| 🤗 [**HuggingFace**](https://huggingface.co/datasets/LGAI-EXAONE/KoMT-Bench) | 📑 [**EXAONE 3.0 7.8B Tech Report**](https://arxiv.org/abs/2408.03541) |

<br>

## Introduction

This is an official repository for **KoMT Bench** built by LG AI Research, used to evaluate Korean instruction-following capability of language models, as described in the “[EXAONE 3.0 7.8B Instruction-Tuned Language Model](https://arxiv.org/abs/2408.03541)” (Technical Report). KoMT Bench is developed by translating [MT-Bench](https://arxiv.org/abs/2306.05685) [1] dataset into Korean and modifying some questions to reflect the characteristics and cultural nuances of the Korean language. 

All source code in this repository is based on [LMSYS’s FastChat repository](https://github.com/lm-sys/FastChat), and we have adapted it to implement EXAONE 3.0 7.8B model.


<br>
<p>Here are examples from KoMT-Bench:</p>
<br>

<table>
<tr>
	<th>Category</th>
	<th>MT-Bench</th>
	<th>KoMT-Bench</th>
</tr>
<tr height=40>
	<th colspan=3 align="left">Writing</th>
</tr>
<tr>
	<td align="center">1st Turn</td>
	<td>Imagine you are writing a blog post comparing two popular smartphone models. Develop an outline for the blog post, including key points and subheadings to effectively compare and contrast the features, performance, and user experience of the two models. Please answer in fewer than 200 words.</td>
	<td>두 개의 인기 스마트폰 모델을 비교하는 블로그 게시물을 작성한다고 가정합니다. 두 모델의 기능, 성능, 사용자 경험을 효과적으로 비교하고 대조할 수 있도록 핵심 사항과 소제목을 포함하여 블로그 게시물의 개요를 작성하세요. 200자 이내로 답하십시오.</td>
</tr>
<tr>
	<td align="center">2nd Turn</td>
	<td>Take your previous response and rephrase it as a limerick.</td>
	<td>이전 답변을 충청도 사투리로 재작성하십시오.</td>
</tr>

<tr height=40>
	<th colspan=3 align="left">Math</th>
</tr>
<tr>
	<td align="center">1st Turn</td>
	<td>When a number is divided by 10, the remainder is 4. What is the remainder when twice the number is divided by 4?</td>
	<td>어떤 숫자를 10으로 나눈 나머지는 4입니다. 그 숫자의 두 배를 4로 나눈 나머지를 구하세요.</td>
</tr>
<tr>
	<td align="center">2nd Turn</td>
	<td>What about when twice the number is divided by 5?</td>
	<td>그 숫자의 두 배를 5로 나누면 어떨까요?</td>
</tr>

<tr height=40>
	<th colspan=3 align="left">Humanities</th>
</tr>
<tr>
	<td align="center">1st Turn</td>
	<td>Provide insights into the correlation between economic indicators such as GDP, inflation, and unemployment rates. Explain how fiscal and monetary policies affect those indicators.</td>
	<td>GDP, 인플레이션, 실업률과 같은 경제 지표 간의 상관관계에 대한 통찰을 제시하세요. 이러한 지표들에 재정 및 통화 정책이 어떤 영향을 미치는지 설명하세요.</td>
</tr>
<tr>
	<td align="center">2nd Turn</td>
	<td>Now, explain them again like I'm five.</td>
	<td>이제 제가 5살이라 생각하고 다시 설명해 주세요.</td>
</tr>
</table>

<br>

## Setting & Installation

```bash
git clone https://github.com/LG-AI-EXAONE/KoMT-Bench
cd FastChat
bash setting.sh
export OPENAI_API_KEY=<openai key>
export PYTHONPATH=${PYTHONPATH}:${PWD}
```

- Note that we have implemented a *square root* penalty for non-Korean responses, which requires to detect what language each response is written in. To accomplish this, we utilize a language detector developed by Google. **We recommend users check that the detector has been installed correctly in the following path**: `./fastchat/llm_judge/data/mt_bench/model_judgment/language_detector.tflite`

<br>

## Run

```bash
bash run_ko_mt.sh
```

- To evaluate the EXAONE model with a single line of code, just execute the command above.

To run each step separately, please follow the steps below:

### 1. Generating model Answer

```bash
cd fastchat/llm_judge/

# Generating Model Answers
CUDA_VISIBLE_DEVICES=0 python gen_model_answer.py \
		--model-path <model_name or model_path> \
		--model-id <model_id> \
		--dtype bfloat16 
```

- To evaluate the EXAONE model, `<model_name or model_path>` must include the keyword `exaone`.

### 2. Evaluating model Answer

```bash
cd fastchat/llm_judge/

# Assessing Nodel Answers through a LLM-as-a-judge (here, "gpt-4-0613" is used)
python gen_judgment.py --model-list <model_id>
		

# Giving a penalty to the score of non-Korean responses
cd data/mt_bench/model_judgment
python detector.py --model_id <model_id>
		
```

### 3. Show Result

```bash
cd fastchat/llm_judge/

# Getting Results
python show_result.py --mode single --input-file <file_path>

```

- Please put `./data/mt_bench/model_judgment/<model_id>_single_final.jsonl` into `<file_path>` to obtain the language-penalized results (default).
- If you want to see the unpenalized results, put `./data/mt_bench/model_judgment/<model_id>_single.jsonl` into `<file_path>` instead.

<br>

## Results

Here are the evaluation results of various language models including the EXAONE 3.0 7.8B instruction-tuned model on KoMT-Bench. Please refer to [EXAONE 3.0 technical report](https://arxiv.org/abs/2408.03541) for details.

| | EXAONE 3.0 7.8B Inst. | Llama 3.1 8B Inst. | Gemma 2 9B Inst. | QWEN 2 7B Inst. | Phi 3 7B Inst. | Mistral 7B Inst. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| KoMT-Bench | **8.92**  | 6.06 | 7.92 | 7.69 | 4.87 | 5.20 |

<br>

## Notice

### Why penalize scores for non-Korean response?

We found that, even when generated responses were in a language other than Korean, GPT-4-0613, acting as the judge, continued to award high scores. To handle such cases, we adopt a *square root penalty* which applies the square root to the score of non-Korean responses in order to adjust for this discrepancy.

By applying the square root penalty, the range of score for non-Korean responses falls within $[1,\sqrt{10}]$. It's worth noting that we do not apply this penalty to questions 138 and 140, as their potential responses could be non-Korean.

<br>

## References

[1] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph E Gonzalez, and Ion Stoica. Judging llm-as-a-judge with mt-bench and chatbot arena. In A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, Advances in Neural Information Processing Systems, volume 36, pages 46595–46623. Curran Associates, Inc., 2023.

<br>

## Citation

```
@misc{KoMT-Bench,
  author = {LG AI Research},
  title = {KoMT-Bench},
  year = {2024},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{https://huggingface.co/datasets/LGAI-EXAONE/KoMT-Bench}}
}
```
