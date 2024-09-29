from src.components import Component
from src.composition.action import Action
from src.composition.protagonists import Protagonists

from src.utils import stringify_tags


class Composition(Component):
    def __init__(self, data):
        super().__init__(data)
        prefix = self.data.data["composition"]["prefix"]
        composition = self.data.random_data["composition"]
        camera = composition["camera"]
        self.action = Action(data)
        self.protagonists = Protagonists(data)
        print(composition["protagonists"])
        self.components = {
            'prefix': stringify_tags(prefix),
            'camera': stringify_tags([
                stringify_tags(camera["angles"]),
                stringify_tags(camera["framings"])
            ]),
            'protagonists': self.protagonists,
            'action': self.action
        }
