from ..node import Node


class Clothes(Node):

    def __init__(self):
        super().__init__()
        self.components = {
            'vest': Piece("vest", self.seed+1),
            'top': Piece("top", self.seed+2),
            'bottom': Piece("bottom", self.seed+3)
        }

    def build_prompt(self):
        self.prompt = [
            self.components["vest"],
            self.components["top"],
            self.components["bottom"]
        ]


class Piece(Node):

    def __init__(self, type, seed_modifier):
        super().__init__(data_file="clothes.toml")
        self.seed = self.seed + seed_modifier
        self.data = self.data[type]

    def build_prompt(self):
        type = self.select_tags(self.data["types"])
        color = self.select_tags(self.data["colors"])

        self.prompt = [
            f"{color} {type}",
        ]
