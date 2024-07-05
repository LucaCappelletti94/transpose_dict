"""Module providing tooling to elaborate a dictionary object."""

from typing import Dict, Set, Any


def is_dict_of_dict(dictionary: Dict) -> bool:
    """Return whether given dictionary contains only dictionaries.

    Parameters
    -------------------------------
    dictionary: Dict
        Dictionary of which to determine if contains only dictionaries.

    Returns
    -------------------------------
    Boolean representing whether given dictionary contains only dictionaries.
    """
    return all(isinstance(value, dict) for value in dictionary.values())


def min_depth(dictionary: Dict) -> int:
    """Return minimum depth of given dictionary.

    Parameters
    -------------------------------
    dictionary: Dict
        Dictionary of which to determine the width

    Returns
    -------------------------------
    Minimum depth of dictionary.
    """
    return (
        1 + min(min_depth(value) for value in dictionary.values())
        if is_dict_of_dict(dictionary)
        else 0
    )


def axis_keys(dictionary: Dict, axis: int) -> Set[Any]:
    """Return set of keys at given axis.

    Parameters
    -------------------------------
    dictionary: Dict
        Dictionary to determine keys of.
    Axis:int
        Depth of keys.

    Returns
    -------------------------------
    The set of keys at given axis
    """
    return (
        set.union(*[set(axis_keys(value, axis - 1)) for value in dictionary.values()])
        if axis != 0
        else dictionary.keys()
    )


def reindex_key(dictionary: Dict, key: Any, axis: int) -> Dict:
    """Return reindex dictionary to given key.

    Parameters
    -------------------------------
    dictionary: Dict
        Dictionary to reindex.
    key: Any
        Key to reindex.
    axis: int
        Depth of key to reindex.

    Returns
    -------------------------------
    Reindexed dictionary.
    """
    if axis == 0:
        return dictionary.get(key)
    return {
        subkey: value
        for subkey, value in (
            (
                subkey,
                (
                    value
                    if not isinstance(value, dict)
                    else reindex_key(value, key, axis - 1)
                ),
            )
            for subkey, value in dictionary.items()
        )
        if value is not None and (not isinstance(value, dict) or len(value) != 0)
    }


def transpose_dict(dictionary: Dict, axis: int) -> Dict:
    """Transpose given dictionary on given axis.

    Parameters
    -------------------------------
    dictionary: Dict
        Dictionary to transpose.
    axis: int
        Axis to traspose.

    Returns
    -------------------------------
    Transposed dictionary.
    """
    return {
        key: reindex_key(dictionary, key, axis) for key in axis_keys(dictionary, axis)
    }
