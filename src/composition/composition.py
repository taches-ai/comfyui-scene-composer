from ..node import Node


class Composition(Node):

    def __init__(self):
        super().__init__(data_file="composition.toml")

        self.components = {
            'prefix': self.select_tags(self.data["prefix"]),
            'camera': self.stringify_tags([
                self.select_tags(self.data["camera"]["angles"]),
                self.select_tags(self.data["camera"]["framings"])
            ]),
            'protagonists': self.select_tags(self.data["protagonists"]),
        }

    def build_prompt(self):
        protagonists = self.build_protagonists_prompt()

        self.prompt = [
            self.components["prefix"],
            self.components["camera"],
            protagonists
        ]

    def build_protagonists_prompt(self):

        prompt = self.components["protagonists"]

        match prompt:
            case "1girl":
                prompt = "1girl, solo"
            case "1girl, 1boy":
                prompt = "1girl, 1boy, solo focus"

        return prompt
