from ..node import Node


class Hair(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="character.toml")

    def build_components(self):
        data = self.data["hair"]
        suffix = "hair"

        color = self.select_tags(data["colors"])
        length = self.select_tags(data["lengths"])
        style = self.select_tags(data["styles"])

        self.components = {
            "color": f"{color} {suffix}",
            "length": f"{length} {suffix}",
            "style": style
        }
