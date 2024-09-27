from src.components import Component


class Environment(Component):
    def build_prompt(self):
        time = self.select_tags(self.data["time"])
        weather = self.select_tags(self.data["weather"])
        location = self.select_tags(self.data["locations"])

        self.prompt = [time, weather, location]
