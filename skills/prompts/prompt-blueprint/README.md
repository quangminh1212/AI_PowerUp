# Prompt Blueprint

**A comprehensive collection of AI prompt engineering resources: distilled best-practice guides, a professional prompt-engineering agent, and ready-to-use prompt examples.**

> 🎯 **Perfect for:** Developers, AI practitioners, and anyone looking to improve their prompt engineering skills with proven techniques from industry leaders.

---

## 🚀 What You'll Find Here

- **📚 [Curated Guides](#-prompt-engineering-guides)** — Distilled best practices from OpenAI, Anthropic, Google, and more
- **🤖 [AI Agent](#-using-the-prompt-engineering-agent)** — Transform simple requirements into production-ready prompts
- **📝 [Ready-Made Examples](#-repository-structure)** — Copy-paste prompts for common use cases
- **🔧 [Meta-Prompts](#-repository-structure)** — Advanced tools for creating and refining prompts

---

## ⚡ Quick Start

**New to prompt engineering?** Start here:

```bash
# 1. Clone the repository
git clone https://github.com/thibaultyou/prompt-blueprint.git
cd prompt-blueprint

# 2. Read the unified best practices guide (recommended first read)
open guides/unified-best-practices__claude_sonnet_4.md

# 3. Try the prompt engineering agent
open meta-prompts/prompt-engineering-agent.md
# Copy the content and paste it into ChatGPT, Claude, or your preferred AI

# 4. Explore ready-made examples
open examples/customer-support-agent.md
```

**Already experienced?** Jump to the [prompt engineering agent](#-using-the-prompt-engineering-agent) or browse [specific guides](#available-guides) for your AI model.

---

## 📚 Prompt Engineering Guides

**What are these?** Concise, actionable guides that distill official documentation and best practices from major AI providers into practical advice you can use immediately.

### Available Guides

| Guide | What It Covers | Created By |
|-------|----------------|------------|
| [`unified-best-practices__claude_sonnet_4.md`](guides/unified-best-practices__claude_sonnet_4.md) | **⭐ START HERE** — Comprehensive best practices combining insights from all major providers | Claude Sonnet 4 |
| [`openai-best-practices__chatgpt-4_5.md`](guides/openai-best-practices__chatgpt-4_5.md) | OpenAI's official prompt engineering guidelines and techniques | ChatGPT-4/5 |
| [`anthropic-best-practices__chatgpt-4_5.md`](guides/anthropic-best-practices__chatgpt-4_5.md) | Anthropic's Claude prompting strategies and best practices | ChatGPT-4/5 |
| [`google-best-practices__chatgpt-4_5.md`](guides/google-best-practices__chatgpt-4_5.md) | Google's Gemini prompt engineering recommendations | ChatGPT-4/5 |
| [`prompting-guide-ai-best-practices__chatgpt-4_5.md`](guides/prompting-guide-ai-best-practices__chatgpt-4_5.md) | General AI prompting principles and advanced techniques | ChatGPT-4/5 |

### How to Use These Guides

1. **🌟 Start with the unified guide** — Get a comprehensive overview of all best practices
2. **🎯 Choose provider-specific guides** — Dive deeper into techniques for your preferred AI model
3. **🔄 Reference during prompt creation** — Use alongside our [prompt-engineering agent](#-using-the-prompt-engineering-agent)
4. **📈 Iterate and improve** — Combine insights from multiple guides for optimal results

> **Important:** These are AI-generated summaries of official documentation, optimized for practical use. They are not official provider documents but are based on official sources.

---

## 🤖 Using the Prompt Engineering Agent

**What is it?** A sophisticated AI agent that transforms your simple requirements into professional, production-ready prompts with documentation and usage guidelines.

### 🔄 How It Works

```mermaid
flowchart LR
    A[👤 Your Request<br/>I need a customer service prompt] --> B{Add Context?}
    
    B -->|No| C[🤖 Agent Only]
    B -->|Yes| D[📚 Unified Guide<br/>+ 🤖 Agent]
    
    C --> E[✅ Good Prompt]
    D --> F[⭐ Better Prompt<br/>with advanced techniques]
    
    style A fill:#e3f2fd
    style D fill:#f3e5f5
    style F fill:#fff9c4
```

**Simple workflow:**
1. **Ask the agent** what you need
2. **Optional:** Load the [unified guide](guides/unified-best-practices__claude_sonnet_4.md) first for enhanced results
3. **Get your prompt** — ready to use!

### Why Use This Agent?

- ✅ **Save hours** — No need to research best practices or iterate manually
- ✅ **Professional quality** — Get enterprise-grade prompts with proper formatting
- ✅ **Cross-platform** — Works with GPT-4, Claude, Gemini, and other models
- ✅ **Complete package** — Includes usage guidelines, troubleshooting, and metrics

### Quick Start Guide

#### Step 1: Load the Agent
1. Open [`meta-prompts/prompt-engineering-agent.md`](meta-prompts/prompt-engineering-agent.md)
2. Copy the entire content
3. Paste it into your preferred AI interface (ChatGPT, Claude, etc.)

**💡 Pro Tip:** For even better results, first load the [`unified-best-practices__claude_sonnet_4.md`](guides/unified-best-practices__claude_sonnet_4.md) guide to give the agent additional context about advanced techniques.

#### Step 2: Describe What You Need
Just tell the agent what kind of prompt you want:

**Simple examples:**
- "I need a customer service chatbot prompt"
- "Create a code review prompt for my team"
- "Design a creative writing prompt for marketing copy"

**Detailed examples (even better results):**
- "I need a customer support prompt for a SaaS company, handling 100+ daily conversations, optimized for Claude"
- "Create a technical documentation prompt for API references that must be GDPR compliant"

#### Step 3: Get Professional Results
The agent delivers a complete package:
- 📝 **Production-ready prompt** with professional formatting
- 📋 **Usage guidelines** and implementation notes
- 📊 **Performance benchmarks** and success metrics
- 🔧 **Troubleshooting guide** for common issues
- 🌐 **Cross-platform compatibility** notes

#### Step 4: Refine (Optional)
Ask for specific adjustments:
- "Make it more concise for high-volume use"
- "Add compliance requirements for healthcare"
- "Optimize specifically for GPT-4"

### Example Workflow
```
You: "I need a prompt for customer service chatbot that handles complaints professionally"

Agent: [Executes 7-stage professional workflow]
       [Delivers complete prompt package with documentation]

You: "Great! Can you make it more concise for high-volume use?"

Agent: [Provides optimized version focused on efficiency]
```

---

## 📁 Repository Structure

| Directory | What's Inside | Best For |
|-----------|---------------|----------|
| **[`/guides`](guides)** | Distilled best practices from major AI providers | Learning prompt engineering fundamentals |
| **[`/meta-prompts`](meta-prompts)** | Advanced AI agents for prompt creation and documentation | Creating custom prompts and tools |
| **[`/examples`](examples)** | Ready-to-use prompts for common scenarios | Quick implementation and inspiration |

### Key Files

- **[`prompt-engineering-agent.md`](meta-prompts/prompt-engineering-agent.md)** — The main agent that creates professional prompts from your requirements
- **[`documentation-expert-agent.md`](meta-prompts/documentation-expert-agent.md)** — The agent that creates and updates the guides themselves
- **[`customer-support-agent.md`](examples/customer-support-agent.md)** — Example of a production-ready prompt created by the agent

---

## 🔄 How This Repository Works

1. **📖 Research & Distillation** — The [`documentation-expert-agent`](meta-prompts/documentation-expert-agent.md) processes official documentation from AI providers and creates the guides in [`/guides`](guides)

2. **🧠 Knowledge Integration** — The [`prompt-engineering-agent`](meta-prompts/prompt-engineering-agent.md) embodies these best practices, using them to create high-quality prompts

3. **📚 Example Generation** — The agent's outputs are collected in [`/examples`](examples) as ready-to-use prompts

4. **🔄 Continuous Improvement** — As the agents evolve, the guides and examples are updated to reflect the latest best practices

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

- 🐛 **Report issues** — Found a problem? Let us know
- 📝 **Suggest improvements** — Ideas for better guides or examples
- 🔧 **Submit pull requests** — New guides, examples, or improvements
- 💡 **Share feedback** — How are you using these resources?

> **Note:** This is a personal research project that evolves over time. It may not reach production-grade maturity but aims to be a valuable learning resource.

---

## ⚠️ Important Disclaimers

- **🚧 Work in Progress** — This repository is provided as-is for educational purposes
- **📄 Unofficial Content** — Guides are AI-generated summaries, not official provider documentation
- **🔒 No Warranties** — Use at your own discretion; no guarantees for production use
- **🎓 Educational Focus** — Designed for learning and experimentation, not commercial deployment

---

## 📞 Questions?

- Check the [guides](#-prompt-engineering-guides) for fundamentals
- Try the [prompt engineering agent](#-using-the-prompt-engineering-agent) for custom prompts
- Browse [examples](examples) for inspiration
- Open an issue for specific problems or suggestions