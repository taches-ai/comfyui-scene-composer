from .node import Node
from .composition.composition import Composition
from .action.action import Action
from .subject.character import Character
from .environment.environment import Environment


class Scene(Node):
    def __init__(self, seed=0):
        super().__init__(seed)

        self.components = {
            'composition': Composition(self.seed),
            'action': Action(self.seed),
            'subject': Character(self.seed),
            'environment': Environment(self.seed)
        }

    def define_action(self, action_type):
        self.components['action'] = Action(type=action_type)
