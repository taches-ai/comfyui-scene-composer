from ..node import Node
from ..utils import is_true


class Eyes(Node):

    def __init__(self):
        super().__init__(data_file="character.toml")
        self.data = self.data["eyes"]

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
        type = self.select_tags(eyewear["types"], p)
        color = self.select_tags(eyewear["colors"], p)
        colored_element = self.select_tags(["framed", "tinted"])

        tags = [
            f"{type}",
            f"{color}-{colored_element} {suffix}",
        ]

        eyewear_prompt = self.stringify_tags(
            tags) if is_true(self.seed, p) else ""
        return eyewear_prompt
