from ..node import Node


class Environment(Node):

    def __init__(self, seed=0):
        super().__init__(seed, data_file="environment.toml")

    CATEGORY = Node.CATEGORY + "/Components"

    def build_components(self):
        time = self.select_tags(self.data["time"])
        location_type = self.select_tags(self.data["locations"]["list"])
        location = self.select_tags(self.data["locations"][location_type])
        effects = self.select_tags(self.data["effects"])
        weather = self.build_weather(location_type, location)

        self.components = {
            "time": time,
            "effects": effects,
            "weather": weather,
            "location": location
        }

    def build_weather(self, location, location_type):
        weather = self.data["weather"]

        if location_type == "indoors":
            return ""

        if location == "beach":
            remove_from_list = ["snow", "rain"]
            weather = [w for w in weather if w not in remove_from_list]

        prompt = self.select_tags(weather)
        return prompt
