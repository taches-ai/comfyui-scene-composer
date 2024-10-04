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

    def __str__(self):
        return self.get_prompt()
