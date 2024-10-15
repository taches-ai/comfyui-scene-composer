from ..node import Node


class Composition(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="composition.toml")

    CATEGORY = "Scene Composer/Components"

    def build_prompt(self):
        super().build_prompt()

        prefix = self.select_tags(self.data["prefix"])

        camera = self.stringify_tags([
            self.select_tags(self.data["camera"]["angles"]),
            self.select_tags(self.data["camera"]["framings"])
        ])

        protagonists = self.data["protagonists"]
        match protagonists:
            case "1girl":
                protagonists = "1girl, solo"
            case "1girl, 1boy":
                protagonists = "1girl, 1boy, solo focus"
        protagonists = self.stringify_tags(protagonists)

        self.prompt = [prefix, camera, protagonists]
