from pathlib import Path
import numpy as np

ROOT_DIR = Path(__file__).parent.parent


def is_true(seed, p=0.5):
    """Return True with probability p"""
    rng = np.random.default_rng(seed)
    return rng.random() < p


def get_nested_dict_value(data, keys):
    """Get a nested value from a dictionary defined by a list of keys."""
    if isinstance(keys, str):
        return keys

    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, key)
        else:
            return key
    return data
