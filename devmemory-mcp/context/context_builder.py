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


import os

def write_claude_md(context):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    FILE_PATH = os.path.join(BASE_DIR, "CLAUDE.md")
    
    with open(FILE_PATH, "w") as f:
        f.write(context)