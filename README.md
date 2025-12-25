# LinkForge

Have you ever tried pasting a documentation link into ChatGPT, Claude, or Copilot — only to watch it fail miserably at finding the relevant function or example you needed? We’ve all been there. Even the smartest AI assistants crumble when faced with sprawling documentation sites full of hidden pages, nested links, and outdated structures. LinkForge fixes that once and for all; simply put any URL into our website and you can point any AI agent to a documentation site and instantly make it understandable, searchable, and truly useful.

## Features

- 🕷️ **Web Crawling**: Automatically crawls documentation websites
- 🤖 **AI-Powered Conversion**: Converts HTML to clean Markdown using Groq LLM
- 🔍 **Semantic Search**: Vector embeddings with ChromaDB for intelligent search
- ✨ **Claude Enhancement**: Enhances search results with Claude-generated examples and explanations
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
<<<<<<< Updated upstream
- Claude API key
- Groq API key (get one at [console.groq.com](https://console.groq.com))
- Bright Data API key (get one at [brightdata.com](https://brightdata.com))
=======
- Groq API key (required - get one at [console.groq.com](https://console.groq.com))
- Claude API key (required - get one at [console.anthropic.com](https://console.anthropic.com))
- Bright Data API key (optional - get one at [brightdata.com](https://brightdata.com))
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
 # LinkForge — Documentation MCP Server
=======
# GROQ_API_KEY=your_groq_api_key_here
# CLAUDE_API_KEY=your_claude_api_key_here
# BRIGHTDATA_API_KEY=your_brightdata_api_key_here (optional)
```
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
Minimal checklist for deployment:
- Ensure `requirements.txt` is installed
- Provide required environment variables (e.g. `GROQ_API_KEY`, `CLAUDE_API_KEY` if used)
- Expose ports 8000 and 8001 (or update `server.py` to use provider ports)
- Start the Python process (e.g., `python3 server.py` or via a process manager)
=======
## Deployment to Render

### Option 1: One-Click Deploy

1. Fork this repository
2. Click the "Deploy to Render" button above
3. Set your `GROQ_API_KEY` environment variable in Render dashboard
4. Deploy!

Your server will be available at `https://your-service-name.onrender.com/mcp`

### Option 2: Manual Deployment

1. Fork this repository
2. Sign up/login to [Render](https://render.com)
3. Create a new **Web Service**
4. Connect your forked repository
5. Render will automatically detect the `render.yaml` configuration
6. Add environment variables in the Render dashboard:
   - `GROQ_API_KEY`: Your Groq API key (required)
   - `CLAUDE_API_KEY`: Your Claude API key (required)
   - `BRIGHTDATA_API_KEY`: Your Bright Data API key (optional)
7. Deploy!

## Usage with Cursor

Add to your Cursor MCP configuration (`~/.cursor/mcp.json` or `C:\Users\<username>\.cursor\mcp.json`):

```json
{
  "mcpServers": {
    "documentation": {
      "url": "http://localhost:8000/mcp",
      "transport": "http"
    }
  }
}
```

For deployed version:
```json
{
  "mcpServers": {
    "documentation": {
      "url": "https://your-service-name.onrender.com/mcp",
      "transport": "http"
    }
  }
}
```

## Usage with Poke

Connect your MCP server to Poke at [poke.com/settings/connections](https://poke.com/settings/connections).

To test the connection explicitly:
```
Tell the subagent to use the "documentation" integration's "process_documentation_url" tool
```

If you run into persistent issues (e.g., after renaming the connection), send `clearhistory` to Poke to delete all message history and start fresh.

## Example Workflow

1. **Process documentation**:
```
Use process_documentation_url with:
- url: "https://docs.example.com"
- max_urls: 20
- crawler_workers: 50
```

2. **Check status**:
```
Use get_processing_status with the job_id from step 1
```

3. **Query documentation** (with Claude enhancement):
```
Use query_documentation with:
- query: "how to authenticate users"
- collection_name: "docs_example_com"
- max_results: 5
- enhance_with_claude: true (default)

This will return:
1. Claude-enhanced explanation with code examples
2. Original documentation chunks with similarity scores
```

4. **List available collections**:
```
Use list_collections to see all processed documentation
```

## Customization

### Adding More Tools

Add more tools by decorating functions with `@mcp.tool()` in `src/server.py`:

```python
@mcp.tool()
async def your_custom_tool(param: str) -> str:
    """Tool description for AI agents."""
    # Your implementation
    return result
```

### Adjusting Processing Parameters

Edit default values in `src/server.py`:

```python
async def process_documentation_url(
    url: str, 
    max_urls: int = 20,  # Change default max URLs
    crawler_workers: int = 50,  # Change default workers
    collection_name: str = None
) -> str:
```

## Project Structure

```
linkforge/
├── src/
│   └── server.py           # FastMCP server implementation
├── full_doc_pipeline.py    # Documentation processing pipeline
├── vector_db.py            # ChromaDB vector database wrapper
├── requirements.txt        # Python dependencies
├── render.yaml            # Render deployment configuration
├── .env                   # Environment variables (local only)
└── README.md              # This file
```

## Environment Variables

- `GROQ_API_KEY` (required): Your Groq API key for HTML to Markdown conversion
- `CLAUDE_API_KEY` (required): Your Claude API key for enhanced documentation queries
- `BRIGHTDATA_API_KEY` (optional): Your Bright Data API key for advanced web scraping
- `PYTHON_VERSION` (optional): Python version for deployment (default: 3.12)

## Troubleshooting

### Server won't start
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify your `GROQ_API_KEY` and `CLAUDE_API_KEY` are set in `.env`
- Ensure port 8000 is not already in use

### Processing fails
- Verify the documentation URL is accessible
- Check Groq API key is valid and has credits
- Review server logs for specific error messages

### ChromaDB errors
- Delete `chroma_db/` directory and restart to reset database
- Ensure sufficient disk space for vector storage

### Cursor/Poke connection issues
- Verify the server URL includes `/mcp` path
- Check that transport is set to "http" or "streamable-http"
- Restart Cursor/Poke after updating `mcp.json`

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the [FastMCP documentation](https://github.com/jlowin/fastmcp)
>>>>>>> Stashed changes
