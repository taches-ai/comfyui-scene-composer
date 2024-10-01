from src.components import Component
from src.utils import search_dict


class Action(Component):

    def __init__(self, data, seed):
        super().__init__(data, seed)
        self.type = ""

    def build_prompt(self):
        data = search_dict(self.data, self.type)
        action = self.select_tags(data)
        self.prompt = [action]
