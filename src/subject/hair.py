from ..scene.component import Component


class Hair(Component):

    def __init__(self, seed):
        super().__init__(seed)
        self.data = self.load_data("config/character.toml")["hair"]

    def build_prompt(self):
        suffix = "hair"

        color = self.select_tags(self.data["colors"])
        length = self.select_tags(self.data["lengths"])
        appearance = self.select_tags(self.data["appearances"])
        style = self.select_tags(self.data["styles"])

        self.prompt = [
            f"{color} {suffix}",
            f"{length} {suffix}",
            f"{appearance} {suffix}",
            style
        ]
