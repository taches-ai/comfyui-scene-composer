from .node import Node
from .composition.composition import Composition
from .action.action import Action
from .subject.character import Character
from .environment.environment import Environment


class Scene(Node):

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        components = cls().components

        # Add the components as optional inputs
        optional_components = {
            key: ("STRING", {
                "default": "",
                "forceInput": True
            })
            for key in components.keys()
        }
        inputs["optional"] = optional_components

        return inputs

    def build_components(self):
        composition = Composition(self.seed)
        action = Action(self.seed)
        character = Character(self.seed)
        environment = Environment(self.seed)

        self.components = {
            'composition': composition,
            'action': action,
            'subject': character,
            'environment': environment
        }
