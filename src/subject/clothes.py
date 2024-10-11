from src.scene.component import Component


class Clothes(Component):

    def __init__(self, seed):
        super().__init__(seed)
        self.components = {
            'vest': Piece(self.seed+1, "vest"),
            'top': Piece(self.seed+2, "top"),
            'bottom': Piece(self.seed+3, "bottom")
        }

    def build_prompt(self):
        self.prompt = [
            self.components["vest"],
            self.components["top"],
            self.components["bottom"]
        ]


class Piece(Component):

    def __init__(self, seed, type):
        super().__init__(seed)
        self.data = self.load_data("config/clothes.toml")[type]

    def build_prompt(self):
        type = self.select_tags(self.data["types"])
        color = self.select_tags(self.data["colors"])

        self.prompt = [
            f"{color} {type}",
        ]
