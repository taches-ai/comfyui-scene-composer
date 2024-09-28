from src.components import Component


class Environment(Component):
    def __init__(self, data):
        super().__init__(data)

    def build_prompt(self):
        environment = self.data.random_data["environment"]
        self.prompt = environment["time"] + environment["weather"] + environment["locations"]
