from memory.memory_manager import query_memory


def build_context(query):

    results = query_memory(query)

    docs = results["documents"][0]

    context = "\n".join(docs)

    prefix = f"""
PROJECT MEMORY CONTEXT

Important past decisions:

{context}

Follow these conventions when writing code.
"""

    return prefix


def write_claude_md(context):

    with open("CLAUDE.md", "w") as f:
        f.write(context)