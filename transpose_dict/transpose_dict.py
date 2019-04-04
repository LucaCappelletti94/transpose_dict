from typing import Dict, Set

def dict_of_dict(D:Dict)->bool:
    """Return a bool representing if given dictionary contains only dictionaries.
        D:Dict, dictionary of which to determine if contains only dictionaries
    """
    return all([isinstance(d, dict) for d in D.values()])

def min_depth(D:Dict)->int:
    """Return minimum depth of given dictionary.
        D:Dict, dictionary of which to determine the width
    """
    return 1+ min([
        min_depth(d) for d in D.values()
    ]) if dict_of_dict(D) else 0

def axis_keys(D:Dict, axis:int)->Set:
    """Return set of keys at given depth.
        D:Dict, dictionary to determine keys of
        axis:int, depth of keys
    """
    return set.union(*[
        axis_keys(d, axis-1) for d in D.values()
    ]) if axis else set(D.keys())

def reindex_key(D:Dict, key, axis:int)->Dict:
    """Return reindex dictionary to given key.
        D:Dict, dictionary to reindex
        key, key to reindex
        axis, depth of key to reindex
    """
    return dict((x for x in (
        (k,reindex_key(d, key, axis-1)) for k,d in D.items()
    ) if x[1])) if axis else D[key] if key in D else None

def transpose_dict(D:Dict, axis:int)->Dict:
    """Transpose given dictionary on given axis.
        D:Dict, dictionary to transpose.
        axis:int, axis to traspose.
    """
    assert min_depth(D) >= axis
    return {
        new_key:reindex_key(D, new_key, axis) for new_key in axis_keys(D, axis)
    }