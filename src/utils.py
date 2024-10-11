import numpy as np


def is_true(seed, p=0.5):
    rng = np.random.default_rng(seed)
    return rng.random() < p