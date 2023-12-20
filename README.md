# Florida

<img src="https://github.com/wjbmattingly/florida/raw/main/images/florida.png" alt="florida logo" width="500" height="500">


Welcome to Florida, a Python utility library designed to simplify and enhance your coding experience. Florida is built with the goal of providing easy-to-use, efficient tools to aid developers in various tasks, making coding more intuitive and productive.

## Features

As of now, Florida includes the following feature:

- `dict2schema`: A function that generates a schema of a dictionary's organization, showing each key and the type of its value. The schema can be returned as a string or as a nested dictionary.
- `target2index`: A function that takes in a nested dictionary or list and a target key or index, and returns Python code snippets to access instances of that key or index. It's useful for navigating complex nested structures.

## Installation

Currently, Florida is not available on PyPI, so it can be installed by cloning the repository:

```bash
pip install florida
```

## Usage

```python
from florida import dict2schema

# Example dictionary
# Example dictionary
example_dict = {
    'key1': 'value1',
    'key2': {
        'subkey1': 'subvalue1',
        'subkey2': {
            'subsubkey1': 'subsubvalue1',
            "list1": [{"test": "case"}]
        },
        'subkey3': 123,
        'subkey4': [1, 2, 3]
    },
    'key3': True
}

# Get the schema as a string
print(dict2schema(example_dict, indent=0))

# Get the schema as a dictionary
# print(dict2schema(example_dict, style="dict"))
```

### Expected Output:
```
key1 (str)
key2 (dict)
    subkey1 (str)
    subkey2 (dict)
        subsubkey1 (str)
        list1 (list)
            0 (dict)
                test (str)
    subkey3 (int)
    subkey4 (list)
        0 (int)
        1 (int)
        2 (int)
key3 (bool)
```

## Using target2index

```python
from florida import target2index

# Example nested structure
nested_structure = {
    'item1': 'value1',
    'nested': {
        'item2': 'value2',
        'content': 'some text',
    },
    'list': [{'content': 'another text'}, {'item3': 'value3'}]
}

# Get the Python code to access 'content'
print(target2index('content', nested_structure))
```

### Expected Output

```python
['structure['nested']['content']',
'structure['list'][0]['content']']

```

## License
Florida is released under the MIT License.