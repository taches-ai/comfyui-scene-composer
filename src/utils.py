import numpy as np


def stringify_tags(tags):
    tags = ", ".join(map(str, tags))
    tags = tags.replace(", ,", ",")
    return tags


def is_true(seed, p=0.5):
    rng = np.random.default_rng(seed)
    return rng.random() < p
