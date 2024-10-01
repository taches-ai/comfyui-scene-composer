import numpy as np


def stringify_tags(tags):
    tags = ", ".join(map(str, tags))
    tags = tags.replace(", ,", ",")
    return tags


def is_true(seed, p=0.5):
    rng = np.random.default_rng(seed)
    return rng.random() < p


def search_dict(data, keys):
    """Search a nested dictionary for a key and return its value"""
    keys = keys.split('.')
    for key in keys:
        if data is None or key not in data:
            raise KeyError(f"Key '{key}' not found in data")
        data = data[key]
    return data
