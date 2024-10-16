import numpy as np
import toml

from .utils import ROOT_DIR


class Node:
    """ComfyUI Node parent class
    Will build and return a prompt according to other sub-components.
    """

    def __init__(self, seed=0, data_file=""):
        self.seed = seed

        self.data_file = data_file
        self.data_path = f"{ROOT_DIR}/config/{self.data_file}"
        self.data = self.load_data(self.data_path)

        self.components = {}
        self.prompt = []

    @classmethod
    def INPUT_TYPES(cls):
        """ComfyUI node inputs"""
        required = {
            "seed": ("INT", {
                "default": 0,
                "min": 0,
                "max": 0xffffffffffffffff
            })
        }
        optional = {}
        inputs = {
            "required": required,
            "optional": optional
        }
        return inputs

    RETURN_TYPES = ("STRING",)
    FUNCTION = "run_node"
    CATEGORY = "🎞️ Scene Composer"

    def run_node(self, seed):
        """Return the prompt according to node's seed"""
        self.update_seed(seed)
        prompt = self.get_prompt()
        return (prompt,)

    def get_prompt(self):
        """Build the prompt and return it as a string"""
        self.build_prompt()
        prompt = self.stringify_tags(self.prompt)
        return prompt

    def build_prompt(self):
        """Build the prompt according to the components"""
        self.prompt = [self.components[component]
                       for component in self.components]

    def update_seed(self, seed):
        """Update the seed of the node and its components"""
        self.seed = seed
        for component in self.components:
            if hasattr(self.components[component], "seed"):
                self.components[component].seed = seed

    def select_tags(self, tags, p=1, n=1,):
        """Return n tags from a string, list or dict"""
        rng = np.random.default_rng(self.seed)

        if isinstance(tags, str):
            return tags

        if isinstance(tags, dict):

            p = tags.get("probability", p)
            n = tags.get("repeat", n)

            # TODO: list is just an extra unnecessary step
            # Remove it and chose directly among the defined properties
            if "list" in tags:
                selected_from_list = self.select_tags(tags["list"], p, n)
                tags = tags[selected_from_list]

            if "tags" in tags:
                tags = tags.get("tags", [])

            # If n is a list, choose a random number between the 2 first values
            if isinstance(n, list):
                min_n = n[0]
                max_n = min(n[1], len(tags))
                n = rng.integers(int(min_n), int(max_n))

            if rng.random() > p:
                return ""

        tag_names, weights = self.parse_tag_distribution(tags)

        selected_tags = rng.choice(
            tag_names,
            size=n,
            replace=False,
            p=weights
        )

        tags = self.stringify_tags(selected_tags)
        return tags

    @staticmethod
    def parse_tag_distribution(tags):
        """Choose tags randomly according to defined weights
        If none are defined, tag weight is 1
        Example: "foo:1.5, bar:0.5" -> 75% chance of foo, 25% chance of bar"""
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
        return tag_names, probabilities

    @staticmethod
    def load_data(path):
        """Load data from a TOML file"""
        try:
            with open(path) as file:
                data = toml.load(file)
        except Exception:
            data = {}
        return data

    @staticmethod
    def stringify_tags(tags):
        """Return a string from a list of tags"""
        tags = ", ".join(map(str, tags))
        tags = tags.replace(", ,", ",")
        return tags

    def __str__(self):
        return self.get_prompt()
