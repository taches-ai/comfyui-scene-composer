from src.components import Component
from src.utils import stringify_tags


class Eyes(Component):
    def __init__(self, data):
        super().__init__(data)

    def build_prompt(self):
        suffix = "eyes"
        color = stringify_tags(self.data.random_data["character"]["eyes"]["colors"])
        eye_prompt = [f"{color} {suffix}"]
        
        eyewear_prompt = self.build_eyewear_prompt(self.data.random_data["character"]["eyes"]["eyewears"])

        self.prompt = eye_prompt + eyewear_prompt

    def build_eyewear_prompt(self, eyewear):
        suffix = "eyewear"
        type = stringify_tags(eyewear["types"])
        color = stringify_tags(eyewear["colors"])
        colored_element = stringify_tags(eyewear["colored_element"])

        if type == "":
            return []
        else:
            return [
                f"{type}",
                f"{color}-{colored_element} {suffix}",
            ]
