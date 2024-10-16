from ..node import Node


class Body(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="character.toml")
        self.data = self.data["body"]

    def build_prompt(self):
        self.components = {
            'breasts': Breasts(self.seed)
        }

        type = self.select_tags(self.data["types"])
        colors = self.select_tags(self.data["colors"])
        color = f"{colors} skin" if colors else ""
        breasts = self.components['breasts']
        extras = self.select_tags(self.data["extras"])

        self.prompt = [type, color, breasts, extras]


class Breasts(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="character.toml")
        self.data = self.data["body"]["breasts"]

    def build_prompt(self):
        size = self.select_tags(self.data["sizes"])

        # TODO: Handle nipple display according to clothes state
        # nipples = self.select_tags(self.data["nipples"])

        self.prompt = [size]
