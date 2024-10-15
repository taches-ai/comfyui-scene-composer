from ..node import Node
from ..utils import get_nested_dict_value


class Action(Node):

    def __init__(self, seed, type=["normal"]):
        super().__init__(seed, data_file="actions.toml")
        self.type = type

    CATEGORY = Node.CATEGORY + "/Components"

    def build_prompt(self):
        data = get_nested_dict_value(self.data, self.type)
        action = self.select_tags(data)
        self.prompt = [action]
