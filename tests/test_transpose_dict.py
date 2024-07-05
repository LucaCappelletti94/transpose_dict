"""Tests for transpose_dict package."""

import json
from transpose_dict import TD


def test_transpose_dict():
    """Test transpose_dict function."""
    with open("tests/start.json", "r", encoding="utf8") as f:
        start = json.load(f)
    for i in range(3):
        with open(f"tests/test_{i}.json", "r", encoding="utf8") as f:
            print(TD(start, i))
            assert json.load(f) == TD(start, i)
