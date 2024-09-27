from src.components import Component
from src.composition.composition import Composition
from src.character.character import Character
from src.environment.environment import Environment


class Scene(Component):
    def __init__(self, data, seed=None):
        super().__init__(data, seed)

        self.components = {
            'composition': Composition(self.data["composition"], self.seed),
            'character': Character(
                {
                    'character': data["character"],
                    'clothes': data["clothes"]
                },
                self.seed),
            'environment': Environment(self.data["environment"], self.seed)
        }

    def define_action(self, action):
        self.components['composition'].action.type = action
