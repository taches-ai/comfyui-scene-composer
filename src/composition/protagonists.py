from src.components import Component
from src.utils import stringify_tags

class Protagonists(Component):

    def __init__(self, data):
        super().__init__(data)
        self.type = ""

    def build_prompt(self):
        protagonists = self.data.random_data["composition"]["protagonists"]
        self.prompt = stringify_tags(protagonists)
