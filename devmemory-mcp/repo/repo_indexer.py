import os
from .function_parser import extract_functions


def scan_repo(repo_path):

    repo_map = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                path = os.path.join(root, file)

                functions = extract_functions(path)

                repo_map.append({
                    "file": path,
                    "functions": functions
                })

    return repo_map