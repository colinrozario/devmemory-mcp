#  devmemory MCP

> **Give your AI coding assistants the long-term memory they deserve.**

Hey there! Welcome to **devmemory MCP**. If you've ever felt the pain of explaining your project's architecture, past bugs, and coding standards to an AI assistant for the hundredth time, you're in the right place.

This project is a powerful **memory-backed assistant framework** designed to give your AI tools persistent, long-term memory. It stores your project's critical decisions, code snippets, file paths, function-level context, and debugging insights. It then retrieves exactly what the AI needs using semantic vector search powered by **ChromaDB** and **Sentence Transformers**, directly integrating into Cursor, Claude Desktop, and beyond through the **Model Context Protocol (MCP)**.

---

##  Why You Need This (The Problem)

Modern AI coding assistants are incredibly impressive, but they suffer from gold-fish memory. They are limited by the context window of your current session.

### 1. Groundhog Day, Every Day 
Most assistants forget everything between sessions. Important architectural decisions, debugging insights, and complex reasoning are lost once a conversation ends. You repeatedly have to explain the same project context over and over.

### 2. Lack of Project-Wide Intelligence 
AI tools typically reason **only** over the files currently open in your editor. They rarely retain a deep understanding of the system's architecture, design decisions, or historical changes across your repository.

### 3. The Missing “Why” 
AI assistants can read code and understand *what* it does, but they usually cannot answer questions like:
* *Why was this specific function implemented this way?*
* *Why was this architecture chosen over the alternatives?*
* *What specific bug from three months ago led to this weird workaround?*

The reasoning behind code decisions vanishes the moment the PR is merged.

### 4. No Persistent Debugging History 
Bug fixes, root causes, and troubleshooting steps are rarely preserved in a structured way. When similar problems appear months later, you and your AI must rediscover the exact same solutions from scratch.

---

##  What devmemory MCP Solves (The Solution)

**devmemory MCP** introduces a **persistent memory layer** for your AI assistants. By plugging this MCP server into Claude Desktop, Cursor, or any MCP-compatible client, your AI can suddenly:

-  **Store and Retrieve Project Decisions:** Automatically save coding standards and debugging insights.
-  **Attach Knowledge to Code:** Bind specific memories, rationale, and context to exact file paths and functions.
-  **Semantic Search (ChromaDB):** Retrieve highly relevant historical context using natural language vector search.
-  **Maintain a “Why Did We Do This?” Database:** Keep a searchable knowledge base of your architecture.
-  **Generate Project Context:** Automatically compile relevant context documents for future AI sessions.

By giving AI assistants a structured, queryable memory system, devmemory MCP transforms stateless AI autocomplete tools into **context-aware senior collaborators that improve over time**.

---

##  Features

Through the powers of the Model Context Protocol, this server exposes powerful tools directly to the AI:

- **`add_memory`**: Save important context and associate it with specific file paths or functions.
- **`search_memory`**: Quickly find relevant memories using semantic natural language search queries.
- **`summarize`**: Automatically summarize your development sessions to keep a log of what was done.
- **`build_and_write_context`**: Compile relevant context documents from your memory and automatically export them to a `CLAUDE.md` file for deep editor integration.

---

##  Getting Started

### Prerequisites

You need **Python 3.10+** installed on your machine.

### Installation

Clone the repository and install the package along with its dependencies (`chromadb`, `sentence-transformers`, `mcp`, etc.) for local development:

```bash
# Clone the repository
git clone <your-repo-url>
cd <your-repo-dir>/devmemory-mcp

# Install via pip in editable mode
pip install -e .
```

### Hooking it up to your AI Assistant

Because `devmemory` uses the **Model Context Protocol (MCP)** via `FastMCP`, integrating it into your AI workflows is incredibly easy.

####  Claude Desktop Integration

To use it in **Claude Desktop**, edit your `claude_desktop_config.json` (found in `%APPDATA%\Claude\claude_desktop_config.json` on Windows or `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS) and add the following:

```json
{
  "mcpServers": {
    "devmemory": {
      "command": "uvx",
      "args": [
        "--directory",
        "<ABSOLUTE_PATH_TO_YOUR_REPO>/devmemory-mcp",
        "devmemory-mcp"
      ]
    }
  }
}
```

*Alternatively, if you installed it globally or simply want to point to the virtual environment's executable, you can use the absolute path to `devmemory-mcp` as the command.*

####  Cursor IDE Integration

1. Open **Cursor Settings** -> **Features** -> **MCP**.
2. Click **+ Add New MCP Server**.
3. Select type: `command`.
4. Name: `devmemory`.
5. Command: `devmemory-mcp` *(Note: Provide the absolute path to your Python virtual environment's binary if it's not in your global PATH, e.g., `<path-to-repo>/.venv/Scripts/devmemory-mcp`)*.

Boom! Cursor and Claude now have an immortal memory. When you work, ask them to "save this architecture decision to memory" or "search memory for why we configured the database this way".

---

##  Built With

- **Python 3.10+**
- **[FastMCP](https://github.com/jlowin/fastmcp)** — A high-level framework for building MCP servers easily
- **ChromaDB** — The open-source AI-native vector database
- **Sentence Transformers** (`all-MiniLM-L6-v2`) — For incredibly fast and accurate local text embedding

---

## ❤️ Final Thoughts

Since this is my very first MCP server, it's definitely a work in progress, but it's been an awesome learning experience building a memory tier for AIs. The future of AI isn't just large windows—it's persistent state.

Feel free to use it, break it, dive into the code, or contribute via PRs!

Happy coding! Built with love by **Colin Michael**
