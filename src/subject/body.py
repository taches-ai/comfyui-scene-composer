from ..node import Node


class Body(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="character.toml")
        self.data = self.data["body"]

        self.components = {
            'breasts': Breasts(self.seed)
        }

    def build_prompt(self):
        type = self.select_tags(self.data["types"])
        color = self.select_tags(self.data["colors"])
        extras = self.build_extras_prompt(self.data["extras"])

        self.prompt = [
            type,
            f"{color} skin",
            self.components["breasts"],
            extras
        ]

    def build_extras_prompt(self, extras):
        extras_prompt = self.select_tags(extras["types"])
        return extras_prompt


class Breasts(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="character.toml")
        self.data = self.data["body"]["breasts"]

    def build_prompt(self):
        size = self.select_tags(self.data["sizes"])
        nipples = self.select_tags(self.data["nipples"])

        self.prompt = [size, nipples]
