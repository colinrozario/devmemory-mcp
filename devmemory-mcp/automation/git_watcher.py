import time
from git_integration.diff_intelligence import analyze_last_commit


def watch_repo(repo_path):

    while True:

        analyze_last_commit(repo_path)

        time.sleep(60)