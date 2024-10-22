from ...node import Node


class Body(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="character.toml")

    def build_prompt(self):
        data = self.data["body"]
        type = self.select_tags(data["types"])
        colors = self.select_tags(data["colors"])
        color = f"{colors} skin" if colors else ""
        breasts = Breasts(self.seed)
        breasts = breasts.build_prompt()[0]
        extras = self.select_tags(data["extras"])

        components = [type, color, breasts, extras]
        prompt = self.stringify_tags(components)
        return (prompt,)


class Breasts(Node):

    def __init__(self, seed):
        super().__init__(seed, data_file="character.toml")

    def build_prompt(self):
        data = self.data["body"]["breasts"]
        size = self.select_tags(data["sizes"])

        # TODO: Handle nipple display according to clothes state
        # nipples = self.select_tags(self.data["nipples"])

        prompt = f"{size}"
        return (prompt,)
