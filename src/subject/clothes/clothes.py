from node import Node
from src.subject.clothes.piece import Piece


class Clothes(Node):

    def __init__(self, seed):
        super().__init__(seed)
        self.components = {
            'vest': Piece(self.seed),
            'top': Piece(self.seed),
            'bottom': Piece(self.seed)
        }

    def build_prompt(self):
        self.prompt = [
            self.components["vest"],
            self.components["top"],
            self.components["bottom"]
        ]
