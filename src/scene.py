from .node import Node
from .composition.composition import Composition
from .action.action import Action
from .subject.character import Character
from .environment.environment import Environment


class Scene(Node):
    def __init__(self):
        super().__init__()

        self.components = {
            'composition': Composition(),
            'action': Action(),
            'subject': Character(),
            'environment': Environment()
        }

    def define_action(self, action_type):
        self.components['action'] = Action(type=action_type)
