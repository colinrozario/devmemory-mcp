# DevMemory MCP 

Hey there!  Welcome to **DevMemory MCP**. This is my very first time building a Model Context Protocol (MCP) server, and I'm super excited to share it! 

This project is a minimal prototype of a memory-backed assistant framework. It's designed to give your AI assistants long-term memory by storing context, code snippets, file paths, and function names, then pulling up relevant memories using vector embeddings. Under the hood, it uses ChromaDB and Sentence Transformers to keep track of everything your AI needs to know across sessions.

##  Features

- **Store Memories**: Save important context and associate it with specific file paths or functions.
- **Search Context**: Quickly find relevant memories using semantic search queries.
- **Session Summaries**: Automatically summarize your development sessions to keep a log of what was done.
- **Context Builder**: Compile relevant context documents for your AI and automatically export them to Markdown (`write_claude_md`).

##  Getting Started

### Prerequisites

Make sure you have Python 3.10 or higher installed on your machine.

### Installation

You can easily install the package and its dependencies (`chromadb`, `sentence-transformers`, etc.) for local development:

```bash
# Clone the repository
git clone <your-repo-url>
cd devmemory-mcp

# Install via pip in editable mode
pip install -e .
```

*Note: The server uses FastAPI, so make sure to install it along with Uvicorn or another ASGI server to run it.*

### Running the Server

You can start the server in a couple of ways depending on your setup:

**Run the module directly:**
```bash
python -m devmemory_mcp
```

**Or run it via the installed console script:**
```bash
devmemory-mcp
```

##  API Endpoints

Once the server is running, the following endpoints are available:

- `POST /store_memory`: Add a new memory (requires `type`, `content`, and optional `file_path`, `function_name`).
- `GET /search_memory?query=...`: Search your vector store using natural language.
- `POST /summarize_session`: Generate a summary of your session notes.
- `GET /build_context?query=...`: Build a context document from your memory and write it out for Claude/Other AI editors.

##  Built With

- **Python 3.10+**
- **FastAPI** — For highly performant API endpoints
- **ChromaDB** — Vector database for long-term storage
- **Sentence Transformers** (`all-MiniLM-L6-v2`) — For embedding text

##  Final Thoughts

Since this is my first MCP server, it's definitely a work in progress, but it's been an awesome learning experience shaping up this memory tier. Feel free to use it, break it, dive into the code, or contribute!

Happy coding! Built with love by Colin Michael
