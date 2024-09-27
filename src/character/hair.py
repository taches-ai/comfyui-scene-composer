from src.components import Component


class Hair(Component):

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
