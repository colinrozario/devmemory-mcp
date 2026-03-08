# devmemory MCP 

Hey there! Welcome to **devmemory MCP**. This is my very first time building a **Model Context Protocol (MCP)** server, and I'm super excited to share it.

This project is a minimal prototype of a **memory-backed assistant framework** designed to give AI coding assistants long-term memory. It stores project decisions, code snippets, file paths, function-level context, and debugging insights, then retrieves relevant knowledge using semantic vector search powered by **ChromaDB** and **Sentence Transformers**.

## Why This Exists

Modern AI coding assistants are incredibly powerful, but they still suffer from several major limitations that slow down real-world development workflows.

### 1. Short-Term Memory Only

Most assistants forget everything between sessions. Important architectural decisions, debugging insights, and reasoning are lost once a conversation ends. Developers repeatedly have to explain the same project context again and again.

### 2. Lack of Project-Level Understanding

AI tools typically reason only over the files currently in context. They rarely retain deeper understanding of the system's architecture, design decisions, or historical changes across the repository.

### 3. No “Why” Behind the Code

AI assistants can read code, but they usually cannot answer questions like:

* *Why was this function implemented this way?*
* *Why was this architecture chosen?*
* *What bug led to this workaround?*

The reasoning behind code decisions often disappears over time.

### 4. No Persistent Debugging History

Bug fixes, root causes, and troubleshooting steps are rarely preserved in a structured way. When similar problems appear later, developers must rediscover the same solutions.

### 5. Fragmented Context Across Tools

Developers often switch between multiple AI tools and IDE assistants. Each tool maintains its own isolated context, meaning project knowledge cannot be easily shared or reused across environments.

## What devmemory MCP Solves

devmemory MCP introduces a **persistent memory layer for AI assistants**. It allows agents to:

• Store project decisions, coding standards, and debugging insights
• Attach knowledge to specific files and functions
• Retrieve relevant historical context using semantic search
• Maintain a searchable “why did we do this?” knowledge base
• Automatically generate project context for future AI sessions

By giving AI assistants a structured memory system, devmemory MCP helps transform stateless AI tools into **context-aware collaborators that improve over time**.


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
