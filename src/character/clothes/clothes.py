from src.components import Component
from src.character.clothes.piece import Piece
from src.utils import stringify_tags


class Clothes(Component):

    def __init__(self, data):
        super().__init__(data)

    def build_prompt(self):
        vest_type = stringify_tags(self.data.random_data["clothes"]["vest"]["types"])
        vest_color = stringify_tags(self.data.random_data["clothes"]["vest"]["colors"])
        top_type = stringify_tags(self.data.random_data["clothes"]["top"]["types"])
        top_color = stringify_tags(self.data.random_data["clothes"]["top"]["colors"])
        bottom_type = stringify_tags(self.data.random_data["clothes"]["bottom"]["types"])
        bottom_color = stringify_tags(self.data.random_data["clothes"]["bottom"]["colors"])
        self.prompt = [
            f"{vest_color} {vest_type}",
            f"{top_color} {top_type}",
            f"{bottom_color} {bottom_type}"
        ]
