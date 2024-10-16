from ..node import Node


class Composition(Node):

    def __init__(self, seed=0):
        super().__init__(seed, data_file="composition.toml")

    CATEGORY = Node.CATEGORY + "/Components"

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()

        seed = inputs["required"]["seed"]
        composition_data = cls(seed).data
        prefix = composition_data["prefix"]
        protagonists = list(composition_data["protagonists"])
        protagonists.insert(0, "random")

        # Update the required inputs
        required_inputs = {
            "prefix": ("STRING", {"default": prefix, "multiline": True}),
            "protagonists": (protagonists,),
            "seed": seed
        }
        inputs["required"] = required_inputs
        return inputs

    def run_node(self, prefix, protagonists, seed):

        self.data["prefix"] = prefix

        if protagonists != "random":
            self.data["protagonists"] = protagonists

        self.update_seed(seed)
        prompt = self.get_prompt()
        return (prompt,)

    def build_prompt(self):
        super().build_prompt()

        prefix = self.select_tags(self.data["prefix"])

        camera = self.stringify_tags([
            self.select_tags(self.data["camera"]["angles"]),
            self.select_tags(self.data["camera"]["framings"])
        ])

        protagonists = self.data["protagonists"]
        protagonists = self.select_tags(protagonists)
        match protagonists:
            case "1girl":
                protagonists = "1girl, solo"
            case "1girl, 1boy":
                protagonists = "1girl, 1boy, solo focus"

        self.prompt = [prefix, camera, protagonists]
