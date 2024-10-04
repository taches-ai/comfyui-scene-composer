from src.components import Component
from src.utils import stringify_tags

class Hair(Component):
    def __init__(self, data):
        super().__init__(data)

    def build_prompt(self):
        suffix = "hair"

        color = stringify_tags(self.data.random_data["character"]["hair"]["colors"])
        length = stringify_tags(self.data.random_data["character"]["hair"]["lengths"])
        appearance = stringify_tags(self.data.random_data["character"]["hair"]["appearances"])
        style = stringify_tags(self.data.random_data["character"]["hair"]["styles"])

        self.prompt = [
            f"{color} {suffix}",
            f"{length} {suffix}",
            f"{appearance} {suffix}",
            style
        ]
