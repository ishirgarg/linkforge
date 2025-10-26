# LinkForge

Have you ever tried pasting a documentation link into ChatGPT, Claude, or Copilot — only to watch it fail miserably at finding the relevant function or example you needed? We’ve all been there. Even the smartest AI assistants crumble when faced with sprawling documentation sites full of hidden pages, nested links, and outdated structures. LinkForge fixes that once and for all; simply put any URL into our website and you can point any AI agent to a documentation site and instantly make it understandable, searchable, and truly useful.

## Features

- 🕷️ **Web Crawling**: Automatically crawls documentation websites
- 🤖 **AI-Powered Conversion**: Converts HTML to clean Markdown using Groq LLM
- 🔍 **Semantic Search**: Vector embeddings with ChromaDB for intelligent search
- ⚡ **Async Processing**: Non-blocking background processing for long-running tasks
- 🌐 **HTTP Transport**: FastMCP with streamable HTTP for easy integration
- 📦 **Persistent Storage**: ChromaDB for reliable vector storage

## Tools

The server exposes 4 MCP tools:

1. **`process_documentation_url`** - Crawl and embed a documentation website
2. **`get_processing_status`** - Check the status of processing jobs
3. **`query_documentation`** - Semantic search across embedded documentation
4. **`list_collections`** - View all available documentation collections

### Prerequisites

- Python 3.12+
- Claude API key
- Groq API key (get one at [console.groq.com](https://console.groq.com))
- Bright Data API key (get one at [brightdata.com](https://brightdata.com))

### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd linkforge
```

2. **Create and activate a virtual environment**
```bash
# Using conda
conda create -n mcp-server python=3.12
conda activate mcp-server

# Or using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Copy the example file
cp env.example .env

# Edit .env and add your API keys:
 # LinkForge — Documentation MCP Server

Lightweight MCP server for crawling, processing and searching documentation. This README is intentionally concise — the repo contains a Python MCP/REST server and a small frontend under `website/`.

## Quick summary
- REST API (processing/status): http://localhost:8000
- MCP endpoint (streamable HTTP): http://localhost:8001/mcp
- Local run: use the bundled `startup.bash` to start the Python server and the frontend
- Deploy: you can run a public MCP server by uploading `server.py` (and required files) to any host/provider that runs Python

## Run locally (fast)
The repository includes a small Bash script `startup.bash` that starts the Python server and the frontend for local development.

Make it executable and run it:

```bash
chmod +x startup.bash
./startup.bash
```

## Deploying a public MCP server
You can deploy this project as a public MCP server by copying `server.py` and the required modules (`full_doc_pipeline.py`, `vector_db.py`, `chroma_db/` if needed, and `requirements.txt`) to any provider that can run Python (VM, container, serverless framework, etc.).

Minimal checklist for deployment:
- Ensure `requirements.txt` is installed
- Provide required environment variables (e.g. `GROQ_API_KEY`, `CLAUDE_API_KEY` if used)
- Expose ports 8000 and 8001 (or update `server.py` to use provider ports)
- Start the Python process (e.g., `python3 server.py` or via a process manager)