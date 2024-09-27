from src.components import Component
from src.composition.action import Action

from src.utils import stringify_tags


class Composition(Component):
    def __init__(self, data, seed):
        super().__init__(data, seed)
        self.action = Action(self.data["actions"], self.seed)
        self.components = {
            'prefix': stringify_tags(self.data["prefix"]),
            'camera': stringify_tags([
                self.select_tags(self.data["camera"]["angles"]),
                self.select_tags(self.data["camera"]["framings"])
            ]),
            'protagonists': self.select_tags(self.data["protagonists"]),
            'action': self.action
        }
