import numpy as np
from src.utils import stringify_tags, is_true


class Component():
    """Component of a scene.
    Will build and return a prompt according to other sub-components.
    """

    def __init__(self, data):
        self.data = data
        self.components = {}
        self.prompt = []

    def get_prompt(self):
        """Build the prompt and return it as a string"""
        self.build_prompt()
        prompt = stringify_tags(self.prompt)
        return prompt

    def build_prompt(self):
        """Populate the properties of the object"""
        self.prompt = [self.components[component]
                       for component in self.components]
        pass

    def update_seed(self, seed=None):
        """Update the seed for the RNG. Get a random one if none is provided"""
        new_seed = seed
        if (new_seed is None):
            new_seed = np.random.randint(0, 1000)
        self.seed = new_seed
        for component in self.components.values():
            component.update_seed(self.seed)

    def select_tags(self, tags, n=1, p=1):
        """Return a random number of n tags from a list.
        The probability of returning an empty string is defined by p."""

        rng = np.random.default_rng(self.seed)

        # Probability to keep the tags
        if not is_true(self.seed, p):
            return ""

        # Recusrive selection of tags
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

        tags = stringify_tags(selected_tags)
        return tags

    def recursive_random_choice(self, data, rng):

        if isinstance(data, dict):
            key = rng.choice(list(data.keys()))
            return self.recursive_random_choice(data[key], rng)

        if isinstance(data, list):
            return data

    def __str__(self):
        return self.get_prompt()
