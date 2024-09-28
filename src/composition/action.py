from src.components import Component
from src.utils import stringify_tags


class Action(Component):

    def __init__(self, data):
        super().__init__(data)
        self.type = ""

    def build_prompt(self):
        keys = self.type.split('.')
        data = self.data.random_data["composition"]["actions"]
        for key in keys:
            if data is None or key not in data:
                raise KeyError(f"Key '{key}' not found in data")
            data = data[key]

        action = stringify_tags(data)
        
        self.prompt = [action]
