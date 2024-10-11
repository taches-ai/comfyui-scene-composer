from src.scene.component import Component


class Environment(Component):

    def __init__(self, seed):
        super().__init__(seed)
        self.data = self.load_data("config/environment.toml")

    def build_prompt(self):
        time = self.select_tags(self.data["time"])
        weather = self.select_tags(self.data["weather"])
        location = self.select_tags(self.data["locations"])

        self.prompt = [time, weather, location]
