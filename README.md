# 🎲 Transpose Dictionary

[![pip](https://badge.fury.io/py/transpose-dict.svg)](https://pypi.org/project/transpose-dict/)
![python](https://img.shields.io/pypi/pyversions/transpose-dict)
[![license](https://img.shields.io/pypi/l/transpose-dict)](https://github.com/LucaCappelletti94/deflate_dict/blob/master/LICENSE)
[![downloads](https://pepy.tech/badge/transpose-dict)](https://www.pepy.tech/projects/transpose-dict)
[![github](https://github.com/LucaCappelletti94/transpose_dict/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/transpose_dict/actions/)

Python package to transpose Python dictionaries.

Multilevel dictionaries can be viewed as projections of sparse n-dimensional matrices: as such, you can transpose them on any of their axes.

The package provides a function that allows you to transpose a dictionary on any of its axes.

## Installing the transpose_dict package

As usual, just use pip as follows:

```shell
pip install transpose_dict
```

## Basic usage example

```python
from transpose_dict import transpose_dict # or from transpose_dict import TD, for brevity

your_dictionary = {
    "a" : {
        "0" : {
            "I" : [1, 2, 3],
            "II" : [4, 5, 6]
        }
    },
    "b" : {
        "0" : {
            "I" : [8, 9, 10],
            "II" : [467, 23, 23]
        },
        "1" : {
            "III" : [6, 7, 9]
        }
    }
}

transpose_dict(your_dictionary, axis=0) # The given dictionary does not change
#> {"b": {"0": {"I": [8, 9, 10], "II": [467, 23, 23]}, "1": {"III": [6, 7, 9]}}, "a": {"0": {"I": [1, 2, 3], "II": [4, 5, 6]}}}
transpose_dict(your_dictionary, axis=1) # The new main axis is the one with ("0", "1")
#> {"0": {"a": {"I": [1, 2, 3], "II": [4, 5, 6]}, "b": {"I": [8, 9, 10], "II": [467, 23, 23]}}, "1": {"b": {"III": [6, 7, 9]}}}
transpose_dict(your_dictionary, axis=2) # The new main axis is the one with ("I", "II", "III")
#> {"I": {"a": {"0": [1, 2, 3]}, "b": {"0": [8, 9, 10]}}, "III": {"b": {"1": [6, 7, 9]}}, "II": {"a": {"0": [4, 5, 6]}, "b": {"0": [467, 23, 23]}}}
```

## License

The software is released under the MIT license.