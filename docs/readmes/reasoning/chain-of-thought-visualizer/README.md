<!-- source: https://github.com/Kushsharma1/chain-of-thought-visualizer.git sha: cbc03c1750d6dc7a1d2ba66d657d76bca5c00274 readme: main/README.md -->
# Kushsharma1/chain-of-thought-visualizer

Web-based tool that visualizes AI reasoning patterns step by step

---

# Chain-of-Thought Visualizer

A web-based tool that visualizes how AI models think step by step when solving problems. Built with Python, Flask, and Ollama for local AI processing.

## 🎯 Problem Statement

When AI models generate responses, we only see the final answer without understanding their reasoning process. This makes it difficult to trust AI decisions, debug reasoning errors, or understand where AI gets stuck.

## 🚀 Solution

This tool captures and visualizes AI's internal "thinking" process, showing:
- **Time spent** on different reasoning stages
- **Types of thinking** used (analysis, planning, research, synthesis, evaluation, problem-solving)
- **Sequential flow** of thoughts through interactive charts
- **Bottlenecks** where AI spends most processing time

## 📊 Features

- **Interactive Web Interface**: Clean, responsive design for easy querying
- **Real-time AI Analysis**: Connects to local Ollama models (no API keys needed)
- **Dual Visualization**: 
  - Interval charts showing thinking sequence and duration
  - Pie charts showing time distribution across thinking types
- **Intelligent Classification**: Automatically categorizes thinking stages
- **Error Handling**: Graceful error management and user feedback

## 🛠️ Technology Stack

- **Backend**: Python 3.8+, Flask
- **AI Model**: Ollama with Llama3 (local processing)
- **Visualization**: Plotly.js for interactive charts
- **Frontend**: HTML5, CSS3, JavaScript

## ⚡ Quick Start

### Prerequisites
- Python 3.8+
- Ollama installed and running
- Llama3 model pulled

### Installation

1. **Setup virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Ensure Ollama is running**:
```bash
ollama serve
ollama pull llama3:latest
```

4. **Start the application**:
```bash
python web_portal.py
```

5. **Access the web interface**:
   - Open browser to `http://localhost:8080`

## 🎮 Usage

1. Enter a query in the input field (e.g., "Explain photosynthesis")
2. Click "Analyze Chain of Thought"
3. View the AI's thinking process and final answer
4. Examine the visualizations:
   - **Left chart**: Sequence of thinking stages over time
   - **Right chart**: Time distribution across thinking types

## 📁 Project Structure

```
maincode_adk/
├── chain_of_thought_visualizer.py  # Core analysis logic
├── web_portal.py                   # Flask web interface
├── requirements.txt                # Python dependencies
└── README.md                      # This file
```

## 🔧 Key Components

### ChainOfThoughtVisualizer Class
- **get_thinking()**: Queries AI model with structured prompts
- **parse_thinking()**: Breaks down thinking into stages
- **classify_stage()**: Categorizes thinking types using keyword matching
- **create_visualizations()**: Generates interactive charts

### Web Interface
- **Flask routes**: Handle HTTP requests and responses
- **JavaScript frontend**: Manages user interactions and chart rendering
- **Responsive design**: Works across different screen sizes

## 🎨 Thinking Stage Categories

- **Analysis**: Problem examination and breakdown
- **Planning**: Strategy and approach development
- **Research**: Information gathering and recall
- **Synthesis**: Combining ideas and concepts
- **Evaluation**: Option assessment and comparison
- **Problem Solving**: Active solution development

## 🚀 Example Queries

- "How does quantum computing work?"
- "Solve this math problem: 2x + 5 = 15"
- "What are the pros and cons of renewable energy?"
- "Explain the process of photosynthesis"

## 💡 Technical Highlights

- **Local AI Processing**: No external API dependencies
- **Real-time Visualization**: Interactive charts with hover details
- **Intelligent Parsing**: Regex-based thinking stage extraction
- **Error Resilience**: Comprehensive error handling
- **Scalable Design**: Modular architecture for easy extension

## 🔍 Understanding the Output

The visualizations help identify:
- **Thinking patterns**: How AI approaches different problem types
- **Time distribution**: Which reasoning stages take most effort
- **Bottlenecks**: Where AI spends disproportionate time
- **Reasoning quality**: Completeness of thinking process

## 🎯 Future Enhancements

- Real-time streaming of thinking process
- Support for multiple AI models
- Historical analysis and pattern tracking
- Export functionality for research
- Collaborative features for team analysis

## ⚠️ Limitations

- Timing estimation is simulated (0.5s per sentence)
- Classification based on keyword matching
- Requires local Ollama installation
- Single-user session management

## 📊 Performance Considerations

- Average response time: 3-8 seconds depending on query complexity
- Memory usage: ~500MB for Llama3 model
- Concurrent users: Limited by AI model processing capacity

---

**Built for understanding AI reasoning patterns through interactive visualization.** 