from ..node import Node


class Environment(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="environment.toml")

    CATEGORY = Node.CATEGORY + "/Components"

    def build_prompt(self):
        time = self.select_tags(self.data["time"])
        weather = self.select_tags(self.data["weather"])
        location = self.select_tags(self.data["locations"])

        self.prompt = [time, weather, location]
