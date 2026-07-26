<!-- source: https://github.com/adamf9898/mtg-player.git sha: 976c1e34ff965566222266763a43226d91005f97 readme: main/README.md -->
# adamf9898/mtg-player

An AI agent that learns to play Magic: The Gathering Commander using LLM-powered reasoning, Chain-of-Thought decision making, and a custom rules engine.

---

# MTG Commander AI - Agentic Implementation

An AI agent that learns to play Magic: The Gathering Commander using LLM-powered reasoning, Chain-of-Thought decision making, and a custom rules engine.

Credit: Inspired by Discord User "SkillsMcGee" (210509006043742208)

## 🎯 Project Goals

- Build an AI that can play Commander format MTG
- Use **agentic architecture** (LLM + tools) instead of fine-tuning
- Implement Chain-of-Thought reasoning for strategic planning
- Create a testable, explainable, and extensible system
- Learn modern AI development practices

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                   LLM Agent                         │
│  (GPT-4, Claude, or Local Model)                   │
│  • Strategic Decision Making                        │
│  • Chain-of-Thought Reasoning                       │
│  • Multi-turn Planning                              │
└─────────────┬───────────────────────────────────────┘
              │
              │ Tool Calls
              │
┌─────────────▼───────────────────────────────────────┐
│                  Tools Layer                        │
│  • get_game_state()                                 │
│  • get_legal_actions()                              │
│  • execute_action()                                 │
│  • analyze_threats()                                │
│  • get_stack_state()                                │
│  • can_respond()                                    │
│  • evaluate_position()                              │
└─────────────┬───────────────────────────────────────┘
              │
              │ Validated Actions
              │
┌─────────────▼───────────────────────────────────────┐
│              Rules Engine                           │
│  • Game State Management                            │
│  • Move Validation                                  │
│  • Turn Structure                                   │
│  • Combat Resolution                                │
│  • Stack Management                                 │
└─────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- OpenAI API key (or Anthropic, or local Ollama/LM Studio)

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd mtg-player

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API key
```

### Run the Game

```bash
# Basic commands
python run.py                      # Default: 4 players, 10 turns, quiet mode, balanced aggression
python run.py --verbose            # With turn-by-turn output to console
python run.py --help               # Show all available options

# Customize game
python run.py --players=2          # 2-player game
python run.py --players=2 --verbose  # 2-player with console output
python run.py --max-turns=5        # Short 5-turn game
python run.py --max-turns=100      # Longer game (more likely to see winners)

# Aggression levels (affects combat strategy)
python run.py --aggression=aggressive --max-turns=50   # Attack with ALL creatures
python run.py --aggression=balanced                    # Attack with power 2+ (default)
python run.py --aggression=conservative                # Only attack with power 3+

# Heuristic mode (no LLM calls - for testing without API costs)
python run.py --no-llm --verbose   # Use rule-based AI instead of LLM
python run.py --heuristic          # Alternative flag name
python run.py --no-llm --aggression=aggressive  # Aggressive heuristic AI

# Combine options
python run.py --players=2 --max-turns=50 --aggression=aggressive --verbose
python run.py --no-llm --aggression=aggressive --max-turns=100 --verbose

# Alternative entry (without run.py)
PYTHONPATH=./src python src/main.py --verbose
```

**Available Options:**
- `--verbose` or `-v` - Show detailed turn-by-turn output to console
- `--no-llm` or `--heuristic` - Use rule-based AI (no API costs)
- `--players=N` - Number of players (2-4, default: 4)
- `--max-turns=N` - Maximum full turns before ending (default: 10)
- `--aggression=LEVEL` - Combat aggression level (default: balanced)
  - **`aggressive`**: Attack with ALL creatures every turn (maximum pressure)
  - **`balanced`**: Attack with power 2+ or when at ≤30 life (default)
  - **`conservative`**: Only attack with power 3+ or when desperate (≤20 life)
- `--help` or `-h` - Display help message with all options

**Aggression Levels**: Control how aggressively the AI attacks in combat:
- 🔴 **Aggressive**: All-out attacks every turn. Faster games, higher risk. Best for eliminating opponents quickly.
- ⚖️ **Balanced**: Strategic attacks with decent creatures or when behind. Good mix of offense and defense.
- 🛡️ **Conservative**: Defensive play, only attack with strong creatures. Hold back blockers for protection.

**Heuristic Mode**: Use `--no-llm` or `--heuristic` to run games without making LLM API calls. This uses an **enhanced rule-based AI** that demonstrates the agentic architecture:
- ✅ Uses the same tool-calling pattern as the LLM
- ✅ Queries game state, analyzes threats, checks stack
- ✅ Makes strategic decisions (ramp, removal, combat)
- ✅ Respects aggression level settings
- ✅ Shows the architecture works without LLM dependency
- 💰 **Perfect for**: Testing engine, rapid iteration, demos, no API costs
- 🎯 **Performance**: ~70-80% as effective as LLM in current implementation (see [ARCHITECTURE.md](ARCHITECTURE.md) for detailed analysis)

> **Note**: The heuristic AI is surprisingly effective because MTG has constrained action spaces (limited legal moves at any time). The LLM's advantages are mainly in complex board evaluation, political decisions in multiplayer, and creative line-finding. See the "Heuristic vs LLM" section in [ARCHITECTURE.md](ARCHITECTURE.md) for a full comparison.

### LLM Provider Options

The project supports multiple LLM providers, configured via the `.env` file:

**Cloud Providers:**
- **OpenAI** (GPT-4, GPT-3.5): Set `LLM_PROVIDER=openai` and configure `OPENAI_API_KEY`
- **Anthropic** (Claude): Set `LLM_PROVIDER=anthropic` and configure `ANTHROPIC_API_KEY`
- **OpenRouter** (Multi-provider gateway): Set `LLM_PROVIDER=openrouter` and configure `OPENROUTER_API_KEY`

**Local Providers:**
- **Ollama**: Run models locally via Ollama. Set `LLM_PROVIDER=ollama` and configure `OLLAMA_BASE_URL` (default: `http://localhost:11434`)
- **LM Studio**: Run models locally via LM Studio's OpenAI-compatible server. Set `LLM_PROVIDER=lmstudio` and configure `LMSTUDIO_BASE_URL` (default: `http://localhost:1234/v1`)

**Example `.env` configuration for LM Studio:**
```bash
LLM_PROVIDER=lmstudio
LMSTUDIO_BASE_URL=http://localhost:1234/v1
LMSTUDIO_MODEL=local-model  # Use your loaded model's name from LM Studio
```

See `.env.example` for all configuration options.

**Setup Guides:**
- [LM Studio Setup Guide](LMSTUDIO_SETUP.md) - Run models locally with zero API costs
- [OpenRouter Setup Guide](OPENROUTER_SETUP.md) - Access multiple LLM providers through one API

### Logging

The game creates detailed log files in the `logs/` directory:

- **Game logs** (`logs/game_YYYYMMDD_HHMMSS_gameid.log`)
  - Turn progression
  - Phase changes
  - Player actions
  - Win/loss conditions

- **LLM logs** (`logs/llm_YYYYMMDD_HHMMSS_gameid.log`)
- **Heuristic logs** (`logs/heuristic_YYYYMMDD_HHMMSS_gameid.log`)
  - Only used when running with `--no-llm` / `--heuristic`
  - Context snapshot per decision point (turn/phase/step, threat/action counts)
  - Position evaluation (score/status/breakdown/summary)
  - Tool executions relevant to heuristics
  - Final decision and reasoning
  - Full prompts sent to the LLM
  - Complete responses (including reasoning/thinking for o-series models)
  - Tool calls and results
  - Token usage statistics
  - Decision reasoning

**Console output** (with `--verbose` flag):
- High-level game progress
- Turn announcements
- Player life totals and board state
- Game results

All detailed logging goes to files only, keeping console output clean and readable.

## 📁 Project Structure (src layout)

```
mtg-player/
├── README.md
├── ROADMAP.md              # Detailed implementation roadmap
├── requirements.txt
├── .env.example
├── logs/                   # Auto-generated logs (game, LLM, heuristic)
├── src/
│   ├── main.py            # Entry point (supports archetype decks)
│   ├── core/
│   │   ├── game_state.py  # Game state representation
│   │   ├── player.py      # Player state
│   │   ├── card.py        # Card models
│   │   ├── rules_engine.py # Core rules implementation
│   │   └── stack.py       # Stack implementation
│   ├── agent/
│   │   ├── llm_agent.py   # LLM decision-making agent
│   │   └── prompts.py     # Prompt templates
│   ├── tools/
│   │   ├── game_tools.py          # Game state/action/stack/response tools
│   │   └── evaluation_tools.py    # Position evaluation tool (score/breakdown)
│   ├── utils/
│   │   └── logger.py      # Game, LLM, and Heuristic logging utilities
│   └── data/
│       └── cards.py       # Card database + deck builders
├── tests/
│   ├── test_rules_engine.py
│   ├── test_stack.py
│   ├── test_instant_speed.py
│   └── test_llm_agent.py
└── notebooks/
    └── exploration.ipynb  # For experimentation
```

## 🔧 Technology Stack

- Data Models: Pydantic v2
- LLM Providers: OpenAI and Anthropic (optional via .env)
- Testing: pytest
- Type Checking: mypy (src layout configured)
- CLI/Utilities: Rich (optional) and requests

## 📚 Key Concepts

### Agentic Architecture
Instead of fine-tuning a model, we give the LLM tools it can call to interact with the game. This allows:
- Validation of all actions through the rules engine
- Explainable decision-making
- Easy debugging and iteration
- No need for expensive GPU training

### Chain-of-Thought Reasoning
The AI is prompted to "think out loud" before making decisions:
1. **Analyze**: What's the current situation?
2. **Plan**: What are my goals this turn?
3. **Evaluate**: What are my options?
4. **Decide**: Which action is best?
5. **Execute**: Make the move

### Tool-Based Interaction
The LLM doesn't directly manipulate game state. Instead, it calls tools:
- `get_legal_actions()` - Ask what moves are available
- `execute_action(action)` - Perform a validated move
- `analyze_threats()` - Get strategic analysis

This ensures the AI can never make illegal moves or hallucinate game state.

## 🎮 Current Status

**Phase 5a: Strategic Reasoning Enhancement** 🔥 IN PROGRESS

### Latest Feature: Political Combat Intelligence ✨

The LLM agent now makes politically-aware multiplayer combat decisions:
- **Smart Target Selection**: 4-factor priority scoring (threat, vulnerability, revenge, political safety)
- **Revenge Tracking**: Remembers who attacked you recently and retaliates strategically
- **Political Awareness**: Avoids attacking trailing players (politically risky), targets leaders (justified)
- **Combat Tool**: `recommend_combat_targets()` returns prioritized target list with emoji advice

### What's Working
- Phase 4 core complete (stack and instant-speed interactions) ✅
- Phase 5a.1: Chain-of-Thought enforcement ✅
- Phase 5a.3: Turn history & memory ✅
- Phase 5a.4: Political combat intelligence ✅ NEW!
- 152-card Commander staples database ✅
- Archetype-based deck builder: ramp, control, midrange ✅
- 4-player Commander setup with 40 life and commander zone ✅
- 20 tests passing (pytest) ✅
- Type checks clean (mypy) ✅

### Next Up (Phase 5a)
- Multi-turn planning system
- Memory & context between turns
- Enhanced combat intelligence (political target selection)
- Improved prompt engineering

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_rules_engine.py -v
```

## ✅ Type Checking

```bash
python -m mypy --config-file mypy.ini src
```

## 🧰 Utilities

Validate card data against Scryfall (optional):
```bash
python validate_cards.py
```

## 🧩 Deck Archetypes

Decks are built via archetype functions in `data/cards.py`:
- `create_ramp_deck()` – acceleration + big threats
- `create_control_deck()` – counters + removal + finishers
- `create_midrange_deck()` – balanced creatures and interaction

Use the dispatcher:
```python
from data.cards import create_simple_deck
deck = create_simple_deck(commander_card=None, archetype="control")
```

## 📖 Learning Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [MTG Comprehensive Rules](https://magic.wizards.com/en/rules)
- [Scryfall API](https://scryfall.com/docs/api) - Card data
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [LM Studio](https://lmstudio.ai) - Run LLMs locally
- [Ollama](https://ollama.ai) - Another local LLM option

## 🤝 Contributing

This is primarily a learning project, but feedback and suggestions are welcome!

1. Check the [ROADMAP.md](ROADMAP.md) for current priorities
2. Open an issue to discuss major changes
3. Keep the focus on learning and experimentation

## 📝 License

MIT License - Feel free to learn from and adapt this code.

## 🙏 Acknowledgments

- Inspired by the challenge of building AI for complex strategy games
- Thanks to the MTG community and Scryfall for card data
- Built to learn about agentic AI architectures and LLM tool use

---

**Remember**: The goal is not to build the perfect MTG AI, but to learn about modern AI development, agent architectures, and strategic reasoning systems. Have fun! 🎲✨
