def dict2schema(d, style="string", indent=0):
    """
    Generates a schema of a dictionary's organization, showing each key and the type of its value.
    It also handles nested dictionaries within lists. The schema can be returned as a string or as
    a nested dictionary.

    :param d: The dictionary or list to analyze.
    :param style: The output format, either "string" or "dict".
    :param indent: The indentation level (used for recursive calls and string formatting).
    :return: The schema as a string or a nested dictionary, depending on the 'style' parameter.
    """
    schema = ""
    schema_dict = {}

    if isinstance(d, dict):
        items = d.items()
    elif isinstance(d, list):
        # Representing each item in the list as a dictionary entry with index as key
        items = enumerate(d)
    else:
        raise ValueError("Input must be a dictionary or a list")

    for key, value in items:
        key_type_info = f"{key} ({type(value).__name__})"
        # String style formatting
        if style == "string":
            schema += ' ' * indent + key_type_info + "\n"
        # Dictionary style formatting
        else:
            schema_dict[key] = {'type': type(value).__name__}

        # Recursively handle nested dictionaries and lists
        if isinstance(value, dict) or isinstance(value, list):
            nested_schema = dict2schema(value, style, indent + 4)
            if style == "string":
                schema += nested_schema
            else:
                schema_dict[key]['nested'] = nested_schema

    return schema if style == "string" else schema_dict