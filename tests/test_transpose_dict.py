from transpose_dict import TD
import json

def test_transpose_dict():
    with open("tests/start.json", "r") as f:
        start = json.load(f)
    for i in range(3):
        with open("tests/test_{i}.json".format(i=i), "r") as f:
            print(TD(start, i))
            assert json.load(f) == TD(start, i)