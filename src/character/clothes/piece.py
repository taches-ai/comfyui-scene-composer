from src.components import Component


class Piece(Component):
    def build_prompt(self):
        type = self.select_tags(self.data["types"])
        color = self.select_tags(self.data["colors"])

        self.prompt = [
            f"{color} {type}",
        ]
