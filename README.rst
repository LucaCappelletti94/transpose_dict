.. role:: py(code)
   :language: python

.. role:: json(code)
   :language: json


Transpose Dictionary
====================

|travis| |sonar_quality| |sonar_maintainability| |sonar_coverage| |code_climate_maintainability| |pip|

Simple python package to transpose python dictionaries.

Multilevel dictionaries can be viewed as projections of sparse n-dimensional matrices: as such, you can transpose them on any of their axes. This package offers a simple function to do that

Installing Transpose_Dict
------------------------

.. code:: shell

    pip install transpose_dict

Basic usage example
---------------------

.. code:: python

    from transpose_dict import TD # or from transpose_dict import transpose_dict
    
    test = {
        "a":{
            "0":{
                "I":[1,2,3],
                "II":[4,5,6]
            }
        },
        "b":{
            "0":{
                "I":[8,9,10],
                "II":[467,23,23]
            },
            "1":{
                "III":[6,7,9]
            }
        }
    }

    TD(test, 0) # The given dictionary does not change
    #> {"b": {"0": {"I": [8, 9, 10], "II": [467, 23, 23]}, "1": {"III": [6, 7, 9]}}, "a": {"0": {"I": [1, 2, 3], "II": [4, 5, 6]}}}
    TD(test, 1) # The new main axis is the one with ("0", "1")
    #> {"0": {"a": {"I": [1, 2, 3], "II": [4, 5, 6]}, "b": {"I": [8, 9, 10], "II": [467, 23, 23]}}, "1": {"b": {"III": [6, 7, 9]}}}
    TD(test, 2) # The new main axis is the one with ("I", "II", "III")
    #> {"I": {"a": {"0": [1, 2, 3]}, "b": {"0": [8, 9, 10]}}, "III": {"b": {"1": [6, 7, 9]}}, "II": {"a": {"0": [4, 5, 6]}, "b": {"0": [467, 23, 23]}}}

License
--------------
The software is released under the MIT license.

.. |preview| image:: https://github.com/LucaCappelletti94/transpose_dict/blob/master/preview.png?raw=true

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/transpose_dict.png
   :target: https://travis-ci.org/LucaCappelletti94/transpose_dict

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=transpose_dict.lucacappelletti&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/transpose_dict.lucacappelletti

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=transpose_dict.lucacappelletti&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/transpose_dict.lucacappelletti

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=transpose_dict.lucacappelletti&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/transpose_dict.lucacappelletti

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/25fb7c6119e188dbd12c/maintainability
   :target: https://codeclimate.com/github/LucaCappelletti94/transpose_dict/maintainability
   :alt: Maintainability

.. |pip| image:: https://badge.fury.io/py/transpose_dict.svg
    :target: https://badge.fury.io/py/transpose_dict
