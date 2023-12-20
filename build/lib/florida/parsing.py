def dict2schema(d, style="string", indent=0, show_pipes=True, pipe_levels=None):
    """
    Generates a schema of a dictionary's organization, showing each key and the type of its value.
    It also handles nested dictionaries within lists. The schema can be returned as a string or as
    a nested dictionary. Optionally adds pipes and indentation for better visualization in string format.

    :param d: The dictionary or list to analyze.
    :param style: The output format, either "string" or "dict".
    :param indent: The indentation level (used for recursive calls and string formatting).
    :param show_pipes: Whether to show pipes in the string output for better visualization.
    :param pipe_levels: A list to keep track of pipe positions at different levels.
    :return: The schema as a string or a nested dictionary, depending on the 'style' parameter.
    """
    if pipe_levels is None:
        pipe_levels = []

    schema = ""
    schema_dict = {}

    if isinstance(d, dict):
        items = list(d.items())
    elif isinstance(d, list):
        items = list(enumerate(d))
    else:
        raise ValueError("Input must be a dictionary or a list")

    for index, (key, value) in enumerate(items):
        key_type_info = f"{key} ({type(value).__name__})"
        
        if show_pipes:
            pipe_str = ''.join(['│   ' if level else '    ' for level in pipe_levels])
        else:
            indent_str = ' ' * 4 * len(pipe_levels)
            pipe_str = indent_str

        if style == "string":
            if show_pipes == True:
                schema += pipe_str + '├── ' + key_type_info + "\n"
            else:
                schema += pipe_str + '    ' + key_type_info + "\n"
        else:
            schema_dict[key] = {'type': type(value).__name__}

        if isinstance(value, dict) or isinstance(value, list):
            new_pipe_levels = pipe_levels + [index < len(items) - 1]
            nested_schema = dict2schema(value, style, indent + 4, show_pipes, new_pipe_levels)
            if style == "string":
                schema += nested_schema
            else:
                schema_dict[key]['nested'] = nested_schema

    return schema if style == "string" else schema_dict





def find_path_to_item(nested_structure, target, path=None, found_paths=None):
    """
    Recursively finds all paths to an item in a nested dictionary or list structure.

    :param nested_structure: The nested dictionary or list to search.
    :param target: The target key or index to find.
    :param path: The current path being explored (used internally for recursion).
    :param found_paths: Accumulator for all found paths (used internally for recursion).
    :return: A list of paths, where each path is a list of keys and/or indices leading to an instance of the target.
    """
    if path is None:
        path = []
    if found_paths is None:
        found_paths = []

    if isinstance(nested_structure, dict):
        for key, value in nested_structure.items():
            if key == target:
                found_paths.append(path + [key])
            if isinstance(value, (dict, list)):
                find_path_to_item(value, target, path + [key], found_paths)

    elif isinstance(nested_structure, list):
        for index, item in enumerate(nested_structure):
            if isinstance(item, (dict, list)):
                find_path_to_item(item, target, path + [index], found_paths)

    return found_paths

def target2index(target, structure):
    """
    Generates Python code snippets for accessing instances of a target key or index in a nested structure.

    :param target: The target key or index to generate access code for.
    :param structure: The nested dictionary or list structure to search.
    :return: A list of strings, each string being a Python code snippet for accessing one instance of the target.
             Returns a message if no such target is found or if there are multiple targets.
    """
    paths = find_path_to_item(structure, target)
    if not paths:
        return f"No item named '{target}' found."
    
    access_codes = []
    for path in paths:
        access_code = 'structure'
        for step in path:
            if isinstance(step, int):
                access_code += f'[{step}]'
            else:
                access_code += f"['{step}']"
        access_codes.append(access_code)

    return access_codes
