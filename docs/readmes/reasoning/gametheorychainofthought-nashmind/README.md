<!-- source: https://github.com/Anuj0x/gametheoryChainOfThought-nashMind-.git sha: 22c595fbb44a1d5e6b1c7eae718b8bdb1a563a5a readme: main/README.md -->
# Anuj0x/gametheoryChainOfThought-nashMind-

 An advanced multi-agent reasoning framework that uses game theory principles to achieve balanced, bias-resistant AI decision-making through Nash equilibrium consensus.

---

# NashMind

An advanced multi-agent reasoning framework that uses game theory principles to achieve balanced, bias-resistant AI decision-making through Nash equilibrium consensus.

**Created by [Anuj0x](https://github.com/Anuj0x)** - Expert in Programming & Scripting Languages, Deep Learning & State-of-the-Art AI Models, Generative Models & Autoencoders, Advanced Attention Mechanisms & Model Optimization, Multimodal Fusion & Cross-Attention Architectures, Reinforcement Learning & Neural Architecture Search, AI Hardware Acceleration & MLOps, Computer Vision & Image Processing, Data Management & Vector Databases, Agentic LLMs & Prompt Engineering, Forecasting & Time Series Models, Optimization & Algorithmic Techniques, Blockchain & Decentralized Applications, DevOps, Cloud & Cybersecurity, Quantum AI & Circuit Design, Web Development Frameworks.

## 🚀 Features

- 🎯 **Nash Equilibrium Reasoning**: Multi-path inference with preference equilibrium for balanced decision-making
- ⚡ **High Performance**: Async inference with optimized memory usage and concurrent agent reasoning
- 🧠 **Intelligent Consensus**: Game theory-based consensus building among specialized reasoning agents
- 🎨 **Modern CLI**: Beautiful terminal interface with progress bars and rich formatting
- 📊 **Multiple Benchmarks**: Support for diverse reasoning tasks and datasets
- 🔧 **Type-Safe Configuration**: Pydantic-based configuration with validation and defaults

## Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Or use modern packaging
pip install -e .
```

### Usage

```bash
# Evaluate on reasoning benchmarks
nash-mind evaluate --dataset aqua --samples 100 --verbose

# Reason about any question
nash-mind reason --question "What is the optimal strategy for this problem?" --reasoning

# Show configuration options
nash-mind config
```

### Python API

```python
from nash_mind import Config, LowLevelDecoder, NashReasoner

# Configure the reasoning system
config = Config(
    model_path="microsoft/DialoGPT-medium",
    num_players=4,
    temperature=0.7
)

# Initialize components
decoder = LowLevelDecoder(config)
reasoner = NashReasoner(config, decoder)

# Get balanced reasoning result
answer = await reasoner.reach_nash_equilibrium("What is 2 + 2?")
print(f"Balanced Answer: {answer}")
```

## How It Works

### Nash Equilibrium Reasoning Process

1. **Multi-Agent Reasoning**: Specialized agents with different perspectives reason about the query
2. **Preference Equilibrium**: Filter responses based on confidence and coherence
3. **Nash Consensus**: Reach balanced agreement through game theory optimization
4. **Robust Output**: Produce stable, well-reasoned answers resistant to individual agent biases

### Agent Specializations

- **Mathematician**: Logical and analytical reasoning
- **Philosopher**: Deep conceptual analysis
- **Scientist**: Empirical and evidence-based thinking
- **Analyst**: Systematic problem decomposition

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| model_path | str | Required | Path to the language model |
| num_players | int | 4 | Number of reasoning agents |
| temperature | float | 0.7 | Sampling creativity |
| max_tokens | int | 256 | Maximum response length |
| outer_loops | int | 3 | Consensus refinement rounds |

## Supported Tasks

- **Mathematical Reasoning**: GSM8K, AQuA, SVAMP
- **Commonsense Reasoning**: CommonsenseQA, StrategyQA
- **Logical Inference**: BigBench tasks, Coin Flip
- **Custom Queries**: Any reasoning-intensive question

## Performance Features

- **Concurrent Processing**: Async agent reasoning for speed
- **Memory Optimization**: Efficient model loading and inference
- **GPU Acceleration**: Automatic CUDA utilization
- **Scalable Architecture**: Easy extension to more agents/tasks

## Development

### Code Quality

```bash
# Format and lint
ruff format . && ruff check . --fix

# Type checking
mypy nash_mind/

# Testing
pytest tests/
```

### Extending the Framework

```python
# Add custom agent types
class CustomAgent(NashAgent):
    def __init__(self):
        super().__init__("expert", "Domain-specific expertise...", 0)

# Create specialized reasoners
reasoner = NashReasoner(config, decoder, custom_agents=[CustomAgent()])
```

## Citation

```bibtex
@misc{nash_mind,
      title={NashMind: Multi-Agent Reasoning with Nash Equilibrium},
      author={Anuj0x},
      year={2024},
      url={https://github.com/Anuj0x/nash-mind}
}
```