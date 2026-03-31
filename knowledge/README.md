# 📚 Knowledge & Learning

Courses, tutorials, SDKs, curated lists, roadmaps, and educational resources for AI/ML mastery.

## Overview

This directory contains **34 submodules** of the world's best AI learning resources — from comprehensive university-style courses and hands-on coding tutorials to official provider SDKs and curated awesome lists. Whether you're building LLMs from scratch or learning production ML engineering, start here.

## Submodules (34)

### Courses & Tutorials
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`generative-ai-for-beginners`](https://github.com/microsoft/generative-ai-for-beginners) | Microsoft | 21-lesson GenAI course (~80k★) |
| [`ai-for-beginners`](https://github.com/microsoft/AI-For-Beginners) | Microsoft | 24-week AI curriculum with labs (~35k★) |
| [`llm-course`](https://github.com/mlabonne/llm-course) | mlabonne | Complete guide to LLMs — fundamentals to deployment |
| [`ai-agents-masterclass`](https://github.com/MasterAI-EAF/ai-agents-masterclass) | MasterAI | Building production AI agents step-by-step |
| [`llm-zoomcamp`](https://github.com/DataTalksClub/llm-zoomcamp) | DataTalks | Free LLM engineering bootcamp with projects |
| [`llama-recipes`](https://github.com/meta-llama/llama-recipes) | Meta | Official Llama usage recipes and fine-tuning guides |
| [`hands-on-llm`](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) | HandsOnLLM | Practical LLM book with code and visuals |

### Build From Scratch
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`llms-from-scratch`](https://github.com/rasbt/LLMs-from-scratch) | Sebastian Raschka | Build a GPT from scratch — code-first book (~60k★) |
| [`minimind`](https://github.com/jingyaogong/minimind) | jingyaogong | Train a mini GPT in 2 hours (~30k★) |
| [`nanogpt`](https://github.com/karpathy/nanoGPT) | Andrej Karpathy | Simplest/fastest GPT training — educational reference |
| [`mingpt`](https://github.com/karpathy/minGPT) | Andrej Karpathy | Minimal GPT implementation for learning |
| [`llm-c`](https://github.com/karpathy/llm.c) | Andrej Karpathy | LLM training in pure C/CUDA |
| [`made-with-ml`](https://github.com/GokuMohandas/Made-With-ML) | Goku Mohandas | MLOps course — design, develop, deploy, iterate |

### Official SDKs & Cookbooks
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`openai-python`](https://github.com/openai/openai-python) | OpenAI | Official Python SDK for OpenAI API |
| [`anthropic-sdk-python`](https://github.com/anthropics/anthropic-sdk-python) | Anthropic | Official Python SDK for Claude API |

### Production ML Engineering
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`ml-engineering`](https://github.com/stas00/ml-engineering) | Stas Bekman | Open book on practical ML engineering (~15k★) |
| [`ml-systems-design`](https://github.com/chiphuyen/machine-learning-systems-design) | Chip Huyen | ML systems design for production |
| [`tuning-playbook`](https://github.com/google-research/tuning_playbook) | Google Research | Practical hyperparameter tuning guide |
| [`nvidia-ai-examples`](https://github.com/NVIDIA/GenerativeAIExamples) | NVIDIA | Enterprise GenAI deployment examples |

### Curated Lists & Guides
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`Awesome-LLM`](https://github.com/Hannibal046/Awesome-LLM) | Hannibal046 | Comprehensive LLM resource collection |
| [`Awesome-LLMOps`](https://github.com/tensorchord/Awesome-LLMOps) | TensorChord | LLMOps tools and platforms |
| [`awesome-ai-agents`](https://github.com/e2b-dev/awesome-ai-agents) | E2B | Curated list of AI agents |
| [`awesome-chatgpt-prompts`](https://github.com/f/awesome-chatgpt-prompts) | f | Best ChatGPT prompt collection (~120k★) |
| [`awesome-ai-guidelines`](https://github.com/EthicalML/awesome-ai-guidelines) | EthicalML | AI governance and ethics resources |
| [`awesome-genai`](https://github.com/amirgholami/awesome-generative-ai) | amirgholami | Generative AI tools and resources |
| [`awesome-genai-guide`](https://github.com/aishwaryanr/awesome-generative-ai-guide) | aishwaryanr | Comprehensive GenAI learning guide (~15k★) |
| [`ai-collection`](https://github.com/ai-collection/ai-collection) | ai-collection | Directory of AI/ML tools and startups |
| [`papers-with-code`](https://github.com/paperswithcode/paperswithcode-data) | Papers With Code | ML papers and benchmarks data |

### Roadmaps & Fundamentals
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`developer-roadmap`](https://github.com/kamranahmedse/developer-roadmap) | Kamran Ahmed | Community-driven developer roadmaps (~320k★) |
| [`ai-expert-roadmap`](https://github.com/AMAI-GmbH/AI-Expert-Roadmap) | AMAI | Roadmap to becoming an AI expert |
| [`system-design-primer`](https://github.com/donnemartin/system-design-primer) | Donne Martin | Learn system design for interviews (~300k★) |
| [`coding-interview`](https://github.com/jwasham/coding-interview-university) | jwasham | Complete CS study plan (~320k★) |
| [`build-your-own-x`](https://github.com/codecrafters-io/build-your-own-x) | Codecrafters | Build your own database, OS, shell, etc. (~360k★) |
| [`free-programming-books`](https://github.com/EbookFoundation/free-programming-books) | Ebook Foundation | Largest collection of free programming books (~360k★) |

## Learning Paths

| Goal | Start With |
|------|-----------|
| **LLM Basics** | generative-ai-for-beginners → llm-course |
| **Build GPT from Scratch** | nanogpt → llms-from-scratch → minimind |
| **Production ML** | ml-engineering → tuning-playbook → nvidia-ai-examples |
| **AI Agents** | ai-agents-masterclass → llama-recipes |
| **Interview Prep** | coding-interview → system-design-primer |

## Usage

```bash
# Start the Microsoft GenAI course
git submodule update --init --depth 1 knowledge/generative-ai-for-beginners
cd knowledge/generative-ai-for-beginners

# Build GPT from scratch
git submodule update --init --depth 1 knowledge/nanogpt
cd knowledge/nanogpt && python train.py
```
