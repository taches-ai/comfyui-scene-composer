from ..node import Node


class Hair(Node):

    def __init__(self):
        super().__init__(data_file="character.toml")
        self.data = self.data["hair"]

    def build_prompt(self):
        suffix = "hair"

        color = self.select_tags(self.data["colors"])
        length = self.select_tags(self.data["lengths"])
        appearance = self.select_tags(self.data["appearances"])
        style = self.select_tags(self.data["styles"])

        self.prompt = [
            f"{color} {suffix}",
            f"{length} {suffix}",
            f"{appearance} {suffix}",
            style
        ]
