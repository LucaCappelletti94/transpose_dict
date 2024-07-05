🎲 Transpose Dictionary
======================
|pip| |downloads| |github|

Python package to transpose python dictionaries.

Multilevel dictionaries can be viewed as projections of sparse n-dimensional matrices: as such, you can transpose them on any of their axes.

The package provides a function that allows you to transpose a dictionary on any of its axes.

Installing the transpose dict package
-------------------------------------------
As usual, just use pip as follows:

.. code:: shell

    pip install transpose_dict

Basic usage example
---------------------

.. code:: python

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

License
--------------
The software is released under the MIT license.

.. |pip| image:: https://badge.fury.io/py/transpose-dict.svg
    :target: https://badge.fury.io/py/transpose-dict

.. |downloads| image:: https://pepy.tech/badge/transpose-dict
    :target: https://pepy.tech/badge/transpose-dict
    :alt: Pypi total project downloads 

.. |github| image:: https://github.com/LucaCappelletti94/transpose_dict/actions/workflows/python.yml/badge.svg
    :target: https://github.com/LucaCappelletti94/transpose_dict/actions/
    :alt: Github Actions