# RAG System on Structured Data

A research and development project on implementing a Retrieval-Augmented Generation (RAG) system that works with structured database data.

## Overview

This project explores how Large Language Models (LLMs) can effectively interact with structured data stored in databases. Using a SQL agent architecture, it enables natural language querying of SQLite databases, with a focus on the sample Chinook database.

## Features

- **SQL Agent**: Interact with a database using natural language queries
- **Local LLM Integration**: Leverages Ollama to run open-source LLMs locally
- **SQLite Database Support**: Works with the Chinook sample database
- **Pydantic AI Framework**: Ensures type-safe responses and structured outputs

## Prerequisites

- Python 3.10.14
- Ollama installed locally
- Local LLM models (default: qwen3:8b)

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd rag-structured-data
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Make sure you have Ollama installed and the required models available:
   ```bash
   ollama pull qwen3:8b
   ```

### Configuration

Create a `.env` file in the root directory with the following settings:

```
LLM_MODEL_NAME = "qwen3:8b"
OLLAMA_BASE_URL = "http://localhost:11434/v1"
DB_PATH = "sqlite:///data/databases/chinook_sample.sqlite3"
```

You can modify these settings based on your preferences or available models.

## Usage

### Command Line Interface

Run the main script to interact with the SQL agent through a command-line interface:

```bash
python main.py
```

This will start an interactive session where you can query the database using natural language.

### Example Queries

- "What tables are available in the database?"
- "What columns does the Album table have?"
- "How many albums did Aerosmith release?"
- "Which customers spent the most money?"

### Using in Notebooks

You can also use the SQL agent in Jupyter notebooks. See the examples in the `notebooks/` directory:

- `nb--test-sql-agent.ipynb`: Example of using the SQL agent
- `nb--test-sqlite-db.ipynb`: Basic SQLite database operations
- `nb--test-ollama-models.ipynb`: Testing different Ollama models
- `nb--test-pydantic_ai.ipynb`: Examples of using Pydantic AI with Ollama

## Project Structure

```
rag-structured-data/
├── data/
│   └── databases/
│       └── chinook_sample.sqlite3  # Sample SQLite database
├── notebooks/                      # Jupyter notebooks for testing
├── src/
│   ├── agents/                     # Agent implementations
│   │   └── sql_agent.py            # SQL agent implementation
│   ├── data_ops/                   # Data operations
│   │   └── sql_ops.py              # SQL operations
│   ├── llm/                        # LLM configurations
│   │   └── models.py               # LLM model definitions
│   ├── prompts/                    # System prompts
│   │   └── sql_agent_system_prompt.py  # SQL agent system prompt
│   └── schemas/                    # Data schemas
│       ├── dependency.py           # Dependencies schema
│       └── response.py             # Response schema
├── .env                            # Environment variables
├── main.py                         # Main entry point
└── requirements.txt                # Python dependencies
```

## Extending the Project

### Adding New Models

To use a different LLM model:

1. Pull the model using Ollama:
   ```bash
   ollama pull model-name
   ```

2. Update the `.env` file:
   ```
   LLM_MODEL_NAME = "model-name"
   ```

### Working with Different Databases

To use a different SQLite database:

1. Place your database file in the `data/databases/` directory
2. Update the `.env` file:
   ```
   DB_PATH = "sqlite:///data/databases/your_database.sqlite3"
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.