from src.components import Component


class Action(Component):

    def __init__(self, data, seed):
        super().__init__(data, seed)
        self.type = ""

    def build_prompt(self):
        keys = self.type.split('.')
        data = self.data
        for key in keys:
            if data is None or key not in data:
                raise KeyError(f"Key '{key}' not found in data")
            data = data[key]

        action = self.select_tags(data)
        
        self.prompt = [action]
