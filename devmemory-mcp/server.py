from mcp.server.fastmcp import FastMCP
from memory.memory_manager import store_memory, query_memory
from sessions.session_summarizer import summarize_session
from context.context_builder import build_context, write_claude_md

# Create an MCP server
mcp = FastMCP("DevMemory")

@mcp.tool()
def add_memory(memory_type: str, content: str, file_path: str = None, function_name: str = None) -> dict:
    """Add a new memory to the project vector store."""
    return store_memory(memory_type, content, file_path, function_name)

@mcp.tool()
def search_memory(query: str) -> dict:
    """Search your vector store using natural language."""
    return query_memory(query)

@mcp.tool()
def summarize(notes: str) -> str:
    """Generate a summary of your session notes and store it for future reasoning."""
    return summarize_session(notes)

@mcp.tool()
def build_and_write_context(query: str) -> str:
    """Build a context document from your memory and export it to CLAUDE.md."""
    context = build_context(query)
    write_claude_md(context)
    return "Context successfully written to CLAUDE.md"

def main():
    """Main entry point for the package script."""
    mcp.run()

if __name__ == "__main__":
    main()