from ..node import Node

from ..utils import get_nested_dict_value


class Clothes(Node):

    def __init__(self, seed=0, state="random", type="random"):
        self.state = state
        self.type = type
        super().__init__(seed, data_file="clothes.toml")

    def build_prompt(self, seed):
        self.seed = seed
        prompt = ""

        if self.state == "random":
            self.state = self.select_tags(self.data["states"])

        if self.type == "random":
            self.type = self.select_tags(self.data["types"])

        match self.state:
            case "clothed":
                prompt = self.build_clothes()
            case "underwear":
                prompt = self.build_underwear()
            case "nude":
                prompt = "nude"

        return (prompt,)

    def build_clothes(self):
        prompt = ""
        match self.type:
            case "casual":
                vest = Piece(self, self.seed+1, ["casual", "vest"])
                top = Piece(self, self.seed+2, ["casual", "top"])
                bottom = Piece(self, self.seed+3, ["casual", "bottom"])
                prompt = [vest, top, bottom]

            case "dress":
                suffix = "dress"
                color = self.select_tags(self.data["colors"])
                length = self.select_tags(self.data["dress"]["length"])
                style = self.select_tags(self.data["dress"]["style"])
                prompt = (f"{color} {suffix}, "
                          f"{length} {suffix}, "
                          f"{style} {suffix}")

            case "swimsuit":
                color = self.select_tags(self.data["colors"])
                type = self.select_tags(self.data["swimsuit"])
                prompt = f"{color} swimsuit, {type}"

            case "uniform":
                color = self.select_tags(self.data["colors"])
                type = self.select_tags(self.data["uniform"])
                prompt = f"{color} uniform, {type} uniform"

            case _:
                color = self.select_tags(self.data["colors"])
                type = self.select_tags(self.data[self.type])
                prompt = f"{color} {type}"
        return prompt

    def build_underwear(self):
        color = self.select_tags(self.data["colors"])
        prompt = f"{color} bra, {color} panties"
        return prompt


class Piece(Node):
    """Return a colored piece of clothing"""

    def __init__(self, cls, seed, type):
        super().__init__(seed)
        self.data = cls().data
        self.seed = seed
        self.type = get_nested_dict_value(self.data, type)

    def build_prompt(self):
        color = self.select_tags(self.data["colors"])
        type = self.select_tags(self.type)
        piece = f"{color} {type}"

        if type == "":
            piece = ""

        prompt = f"{piece}"
        return (prompt,)
