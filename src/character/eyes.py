from src.components import Component
from src.utils import stringify_tags, is_true


class Eyes(Component):

    def build_prompt(self):
        suffix = "eyes"
        color = self.select_tags(self.data["colors"])
        eyewear = self.build_eyewear_prompt(self.data["eyewears"])

        self.prompt = [
            f"{color} {suffix}",
            eyewear
        ]

    def build_eyewear_prompt(self, eyewear):
        p = eyewear["probability"]

        suffix = "eyewear"
        type = self.select_tags(eyewear["types"])
        color = self.select_tags(eyewear["colors"])
        colored_element = self.select_tags(["framed", "tinted"])

        tags = [
            f"{type}",
            f"{color}-{colored_element} {suffix}",
        ]

        eyewear_prompt = stringify_tags(tags) if is_true(self.seed, p) else ""
        return eyewear_prompt
