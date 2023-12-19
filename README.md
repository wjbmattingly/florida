# Florida

![florida logo](images/florida.png)

Welcome to Florida, a Python utility library designed to simplify and enhance your coding experience. Florida is built with the goal of providing easy-to-use, efficient tools to aid developers in various tasks, making coding more intuitive and productive.

## Features

As of now, Florida includes the following feature:

- `dict2schema`: A function that generates a schema of a dictionary's organization, showing each key and the type of its value. The schema can be returned as a string or as a nested dictionary.

## Installation

Currently, Florida is not available on PyPI, so it can be installed by cloning the repository:

```bash
pip install florida
```

## Usage

```python
from florida import dict2schema

# Example dictionary
example_dict = {
    'key1': 'value1',
    'key2': {
        'subkey1': 'subvalue1',
        'subkey2': {
            'subsubkey1': 'subsubvalue1'
        },
        'subkey3': 123,
        'subkey4': [1, 2, 3]
    },
    'key3': True
}

# Get the schema as a string
print(dict2schema(example_dict))

# Get the schema as a dictionary
print(dict2schema(example_dict, style="dict"))
```

## License
Florida is released under the MIT License.