from ..scene.component import Component


class Action(Component):

    def __init__(self, seed, type="normal"):
        super().__init__(seed)
        self.data = self.load_data("config/actions.toml")[type]
        self.type = type

    def build_prompt(self):
        action = self.select_tags(self.data)
        self.prompt = [action]
