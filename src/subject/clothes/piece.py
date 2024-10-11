from node import Node


class Piece(Node):

    def __init__(self, seed):
        super().__init__(seed)
        self.data = self.load_data("config/clothes.toml")["eyes"]

    def build_prompt(self):
        type = self.select_tags(self.data["types"])
        color = self.select_tags(self.data["colors"])

        self.prompt = [
            f"{color} {type}",
        ]
