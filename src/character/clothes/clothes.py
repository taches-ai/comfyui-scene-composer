from src.components import Component
from src.character.clothes.piece import Piece


class Clothes(Component):

    def __init__(self, data, seed):
        super().__init__(data, seed)
        self.components = {
            'vest': Piece(self.data["vest"], self.seed),
            'top': Piece(self.data["top"], self.seed),
            'bottom': Piece(self.data["bottom"], self.seed)
        }

    def build_prompt(self):
        self.prompt = [
            self.components["vest"],
            self.components["top"],
            self.components["bottom"]
        ]
