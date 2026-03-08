from git import Repo
from memory.memory_manager import store_memory


def analyze_last_commit(repo_path):

    repo = Repo(repo_path)

    commit = repo.head.commit

    diff = commit.diff(commit.parents[0])

    for change in diff:

        file_path = change.a_path

        summary = f"""
File changed: {file_path}
Commit message: {commit.message}
"""

        store_memory(
            "code_change",
            summary,
            file_path
        )