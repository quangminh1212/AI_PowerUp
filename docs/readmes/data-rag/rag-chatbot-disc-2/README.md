<!-- source: https://github.com/Kumargaurvit/RAG-ChatBot.git sha: 9808dbc3b0a7ccf13d892a7d50202d5ec84a9d09 readme: main/README.md -->
# Kumargaurvit/RAG-ChatBot

A Conversational AI application that supports both general chat and PDF document question-answering using Retrieval-Augmented Generation (RAG) with conversation history.

---

# RAG Chatbot with Memory

A Streamlit-based conversational AI application that supports both general chat and PDF document question-answering using Retrieval-Augmented Generation (RAG) with conversation history.

## Features

- **Conversational Memory**: Maintains chat history across sessions with session management
- **PDF Document Processing**: Upload and query multiple PDF documents
- **RAG Implementation**: Uses vector embeddings and retrieval for accurate document-based responses
- **Multiple Chat Sessions**: Create and switch between different conversation sessions
- **LangSmith Integration**: Built-in tracking and monitoring support

## Architecture

The application switches between two modes:

1. **RAG Mode** (when PDFs are uploaded): Uses document retrieval with chat history
2. **Basic Chat Mode** (no PDFs): Standard conversational interface with memory

## Prerequisites

- Python 3.8+
- Ollama installed locally with `gpt-oss:120b-cloud` model

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:
```env
LANGCHAIN_API_KEY = your_langchain_api_key
LANGCHAIN_PROJECT = your_project_name
GROQ_API_KEY = your_groq_api_key
HF_TOKEN = your_hugging_face_token
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Access the application in your browser (typically at `http://localhost:8501`)

3. **Optional**: Upload PDF files using the sidebar file uploader

4. Start chatting! The bot will:
   - Answer general questions if no PDFs are uploaded
   - Answer questions based on uploaded PDFs when documents are provided

5. Manage sessions:
   - Create new chat sessions using the "Session ID" input
   - Switch between sessions using the "Chat History" dropdown

## Project Structure

```
.
├── app.py                 # Main application file
├── prompts/
│   └── prompts.py        # Contains prompt templates
├── .env                  # Environment variables (not in repo)
└── README.md            # This file
```

## Configuration

### Model Configuration
The application uses the `gpt-oss:120b-cloud` model from Ollama. To use a different model, modify this line:
```python
llm = ChatOllama(model="your-model-name")
```

### Text Splitting
Default chunk settings:
- Chunk size: 1000 characters
- Chunk overlap: 200 characters

## Required Prompts

Create a `prompts/prompts.py` file with the following variables:
```python
history_prompt = "Your history-aware retriever prompt"
system_prompt = "Your QA system prompt"
basic_prompt = "Your basic chat prompt"
```

## Dependencies

- `streamlit`: Web interface
- `langchain-ollama`: Ollama LLM integration
- `langchain-community`: Document loaders and vector stores
- `langchain-core`: Core LangChain functionality
- `langchain-huggingface`: HuggingFace embeddings
- `chromadb`: Vector database
- `pypdf`: PDF processing
- `python-dotenv`: Environment variable management

## Features in Detail

### Session Management
- Create multiple chat sessions
- Switch between sessions without losing history
- Each session maintains its own conversation context

### PDF Processing
- Supports multiple PDF uploads
- Automatic text extraction and chunking
- Vector embeddings for semantic search
- Persistent retriever across the session

### Chat History
- Displays full conversation history
- Maintains context across multiple turns
- History-aware retrieval for better answers

## Limitations

- PDFs are processed into temporary storage (not persisted)
- Vector store is created in-memory for each session
- Requires Ollama to be running locally

## Troubleshooting

**Model not found**: Ensure Ollama is running and the `gpt-oss:120b-cloud` model is installed:
```bash
ollama pull gpt-oss:120b-cloud
```

**PDF processing fails**: Check that uploaded files are valid PDFs and not corrupted.

**Memory issues**: Large PDFs may consume significant memory during processing.