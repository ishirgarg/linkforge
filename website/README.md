# LinkForge Website

A React-based web interface for the LinkForge MCP documentation server.

## Prerequisites

- Node.js 18+ and npm
- Python 3.12+ with the MCP server running

## Running the Website

1. **Install dependencies:**
   ```bash
   cd website
   npm install
   ```

2. **Make sure the MCP server is running:**
   ```bash
   # In the project root directory
   python src/server.py
   ```
   The server should be running on `http://localhost:8000`

3. **Start the development server:**
   ```bash
   npm run dev
   ```
   The website will be available at `http://localhost:5173`

4. **Open your browser:**
   Navigate to `http://localhost:5173` to see the LinkForge interface

## Features

- Enter any documentation URL to process it
- View available MCP tools
- See real-time processing status
- Query documentation collections

## Architecture

The website communicates with the MCP server using the proper JSON-RPC protocol:

- **Frontend:** React + Vite + Tailwind CSS
- **Backend:** FastMCP server on `localhost:8000`
- **Protocol:** MCP JSON-RPC over HTTP
- **Proxy:** Vite dev server proxies `/mcp` requests to the MCP server

## Request Format

The website uses the standard MCP JSON-RPC format with FastMCP's `http` transport:

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "tool_name",
    "arguments": { ... }
  },
  "id": 1
}
```

**Why `http` instead of `streamable-http`?**

- `http`: Simple, works great for web clients, standard HTTP requests
- `streamable-http`: More complex, requires session management, better for persistent connections

For a React web app making HTTP requests, `http` transport is simpler and better suited.

## Development

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

