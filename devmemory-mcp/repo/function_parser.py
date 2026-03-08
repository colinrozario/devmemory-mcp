import ast


def extract_functions(file_path):

    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    functions = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            functions.append({
                "name": node.name,
                "line": node.lineno
            })

    return functions