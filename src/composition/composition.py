from ..node import Node


class Composition(Node):

    def __init__(self, seed=0):
        super().__init__(seed, data_file="composition.toml")

    CATEGORY = Node.CATEGORY + "/Components"

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        data = cls.load_data(cls.data_path)

        prefix = data["prefix"]
        protagonists = list("random", data["protagonists"])
        camera_framings = list("random", data["camera"]["framings"])
        camera_angles = list("random", data["camera"]["angles"])

        # Update the required inputs
        required_inputs = {
            "prefix": ("STRING", {"default": prefix, "multiline": True}),
            "protagonists": (protagonists,),
            "camera_framings": (camera_framings,),
            "camera_angles": (camera_angles,),
            "seed": inputs["required"]["seed"]
        }

        # Update the inputs
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
