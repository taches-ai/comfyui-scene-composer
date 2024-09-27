from src.components import Component


class Body(Component):

    def __init__(self, data, seed):
        super().__init__(data, seed)
        self.components = {
            'breasts': Breasts(self.data["breasts"], self.seed)
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

        n = extras["repeat"]
        p = extras["probability"]

        extras_prompt = self.select_tags(extras["types"], n, p)
        return extras_prompt


class Breasts(Component):

    def build_prompt(self):
        size = self.select_tags(self.data["sizes"])
        nipples = self.select_tags(self.data["nipples"])

        self.prompt = [size, nipples]
