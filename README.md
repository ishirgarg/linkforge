# Documentation MCP Server

A FastMCP server that processes documentation websites and provides semantic search capabilities. Built for deployment on Render with streamable HTTP transport.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

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

## Local Development

### Prerequisites

- Python 3.12+
- Groq API key (get one at [console.groq.com](https://console.groq.com))
- Bright Data API key (optional - get one at [brightdata.com](https://brightdata.com))

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
# GROQ_API_KEY=your_groq_api_key_here
# BRIGHTDATA_API_KEY=your_brightdata_api_key_here (optional)
```

5. **Run the server**
```bash
python src/server.py
```

The server will start on `http://localhost:8000/mcp`

### Test with MCP Inspector

In another terminal:

```bash
npx @modelcontextprotocol/inspector
```

Open <http://localhost:3000> and connect to `http://localhost:8000/mcp` using **"Streamable HTTP"** transport (NOTE THE `/mcp` path!).

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

3. **Query documentation**:
```
Use query_documentation with:
- query: "how to authenticate users"
- collection_name: "docs_example_com"
- max_results: 5
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

- `GROQ_API_KEY` (required): Your Groq API key for LLM processing
- `BRIGHTDATA_API_KEY` (optional): Your Bright Data API key for advanced web scraping
- `PYTHON_VERSION` (optional): Python version for deployment (default: 3.12)

## Troubleshooting

### Server won't start
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify your `GROQ_API_KEY` is set in `.env`
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
