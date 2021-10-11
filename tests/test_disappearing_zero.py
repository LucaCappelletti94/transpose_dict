"""Test for issue #1 from GitHub.

The issue states that, possibly, when a dictionary contains zero as value, it causes
the values to disappear as follows:

```python
from transpose_dict import TD

d = {
   "a":{
      "0":0,
      "1":1
   },
   "b":{
      "0":0,
      "1":1
   }
}

TD(d, 1)
```

The expected result would be:

```python
{
   "1":{
      "a":1,
      "b":1
   },
   "0":{
      "a":0,
      "b":0
   }
}
```

While the obtained one is:

```python
{
   "1":{
      "a":1,
      "b":1
   },
   "0":{
      
   }
}
```

"""
from transpose_dict import TD


def test_disappearing_zero():
    """Test that everything works correctly in considered use case."""
    d = {
        "a": {
            "0": 0,
            "1": 1
        },
        "b": {
            "0": 0,
            "1": 1
        }
    }

    expected = {
        "1": {
            "a": 1,
            "b": 1
        },
        "0": {
            "a": 0,
            "b": 0
        }
    }

    assert TD(d, 1) == expected
