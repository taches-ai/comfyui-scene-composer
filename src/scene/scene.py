from src.scene.component import Component
from src.composition.composition import Composition
from src.action.action import Action
from src.subject.character import Character
from src.environment.environment import Environment


class Scene(Component):
    def __init__(self, seed=None):
        super().__init__(seed)

        self.components = {
            'composition': Composition(self.seed),
            'action': Action(self.seed),
            'subject': Character(self.seed),
            'environment': Environment(self.seed)
        }

    def define_action(self, action_type):
        self.components['action'] = Action(self.seed, action_type)
