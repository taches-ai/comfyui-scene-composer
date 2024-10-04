from src.components import Component
from src.composition.composition import Composition
from src.character.character import Character
from src.environment.environment import Environment


class Scene(Component):
    def __init__(self, data):
        super().__init__(data)
        self.components = {
            'composition': Composition(data),
            'character': Character(data),
            'environment': Environment(data)
        }

    def define_action(self, action):
        self.components['composition'].action.type = action