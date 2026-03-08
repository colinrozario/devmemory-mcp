from memory.memory_manager import store_memory


def summarize_session(notes):

    summary = f"""
Session Summary

{notes}

Stored for future reasoning.
"""

    store_memory(
        "session_summary",
        summary
    )

    return summary