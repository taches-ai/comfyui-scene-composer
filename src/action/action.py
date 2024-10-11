from ..node import Node


class Action(Node):

    def __init__(self, seed, type="normal"):
        super().__init__(seed, data_file="actions.toml")
        self.type = type

    def build_prompt(self):
        action = self.select_tags(self.data)
        self.prompt = [action]
