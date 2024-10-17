from ..node import Node


class Body(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="character.toml")

    def build_components(self):
        data = self.data["body"]
        type = self.select_tags(data["types"])
        colors = self.select_tags(data["colors"])
        color = f"{colors} skin" if colors else ""
        breasts = Breasts(self.seed)
        extras = self.select_tags(data["extras"])

        self.components = {
            "type": type,
            "color": color,
            "breasts": breasts,
            "extras": extras
        }


class Breasts(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="character.toml")

    def build_components(self):
        data = self.data["body"]["breasts"]
        size = self.select_tags(data["sizes"])

        # TODO: Handle nipple display according to clothes state
        # nipples = self.select_tags(self.data["nipples"])

        self.components = {
            "size": size
        }
