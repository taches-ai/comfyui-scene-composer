import os
import yaml

import random

import numpy as np
from src.utils import stringify_tags, is_true


class Data:
    def __init__(self, path="", seed=1, data=None):
        if data is not None:
            self.data = data
        else:
            self.data = self.merge_config_data(path)
        self.set_seed(seed)
        self.set_random_data()

    def merge_config_data(self, path):
        """Merge all yaml files in a directory into a single dictionary"""
        config_files = [f for f in os.listdir(path) if f.endswith('.yaml')]
        merged_data = {}
        for file in config_files:
            file_path = os.path.join(path, file)
            file_name = os.path.splitext(file)[0]
            try:
                with open(file_path, 'r') as f:
                    data = yaml.safe_load(f)
                    if data is not None:
                        merged_data[file_name] = data
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        return merged_data
    
    def set_seed(self, seed):
        self.seed = seed

    def set_random_data(self, seed=None):
        if seed is not None:
            self.seed = seed
        self.random_data = self.select_random_dictionary_tags(self.data)
        return self.random_data

    def select_random_dictionary_tags(self, tags, n=1, p=1):
        if isinstance(tags, dict):
            if "repeat" in tags:
                n = tags["repeat"]
                tags.pop("repeat")
            if "probability" in tags:
                p = tags["probability"]
                tags.pop("probability")
            if "define" in tags:
                tags.pop("define")
            return dict(map(lambda key: 
                (key, self.select_random_dictionary_tags(tags[key], n, p)),
                tags.keys()))
        if isinstance(tags, list):
            return self.select_tags(tags, n, p)

    def select_tags(self, tags, n=1, p=1):
        """Return a random number of n tags from a list.
        The probability of returning an empty string is defined by p."""

        rng = np.random.default_rng(self.seed)

        # Probability to keep the tags
        if not is_true(self.seed, p):
            return ""

        # Recursive selection of tags
        if isinstance(tags, dict):
            tags = self.recursive_random_choice(tags, rng)

        # Choose tags randomly according to defined weights
        # If none are defined, tag weight is 1
        # Example: "foo:1.5, bar:0.5" -> 75% chance of foo, 25% chance of bar
        tag_names = []
        weights = []
        for tag in tags:
            if ':' in tag:
                tag_name, weight = tag.split(':')
                tag_names.append(tag_name)
                weights.append(float(weight))
            else:
                tag_names.append(tag)
                weights.append(1)

        probabilities = np.array(weights) / sum(weights)

        # Choose n tags
        # n can be an integer or a range (min-max)
        # Example: 1, [2,4]
        if isinstance(n, list):
            min_n = n[0]
            max_n = min(n[1], len(tags))
            n = rng.integers(int(min_n), int(max_n))

        selected_tags = rng.choice(
            tag_names,
            size=n,
            replace=False,
            p=probabilities)

        tags = list(map(str, selected_tags))
        return tags
    
    def random_data_union(self, dict):
        self.random_data = self.union(self.random_data, dict)
        return self.random_data
    
    def union(self, group_a, group_b):
        if isinstance(group_a, list) and isinstance(group_b, list):
            return list(set(group_a)|set(group_b))
        if isinstance(group_a, dict) and isinstance(group_b, dict):
            keys = list(set(group_a.keys())|set(group_b.keys()))
            return dict(map(lambda key:
                (key, self.union(group_a.get(key), group_b.get(key))),
                keys))
        if group_a is None:
            return group_b
        if group_b is None:
            return group_a