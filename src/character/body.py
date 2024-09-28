from src.components import Component


class Body(Component):

    def __init__(self, data):
        super().__init__(data)

    def build_prompt(self):
        type = self.data.random_data["character"]["body"]["types"]
        color = self.data.random_data["character"]["body"]["colors"]
        extras = self.data.random_data["character"]["body"]["extras"]["types"]
        if extras == "":
            extras = []
        breast_size = self.data.random_data["character"]["body"]["breasts"]["sizes"]
        nipples = self.data.random_data["character"]["body"]["breasts"]["nipples"]
        breasts = breast_size + nipples
        skin_color = [" ".join(color + ['skin'])]
        self.prompt = type + skin_color + breasts + extras
