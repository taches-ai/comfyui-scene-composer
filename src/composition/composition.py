from ..node import Node


class Composition(Node):

    def __init__(self, seed=0):
        super().__init__(seed, data_file="composition.toml")

    CATEGORY = Node.CATEGORY + "/Components"

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        seed = inputs["required"]["seed"]
        data = cls(seed).data

        prefix = data["prefix"]
        protagonists = cls.build_inputs_list(data["protagonists"])
        camera_framings = cls.build_inputs_list(data["camera"]["framings"])
        camera_angles = cls.build_inputs_list(data["camera"]["angles"])

        # Update the inputs
        inputs["required"] = {
            "prefix": ("STRING", {"default": prefix, "multiline": True}),
            "protagonists": (protagonists,),
            "camera_framings": (camera_framings,),
            "camera_angles": (camera_angles,),
            "seed": inputs["required"]["seed"]
        }
        return inputs

    def build_components(self):

        prefix = self.select_tags(self.data["prefix"])
        camera_angles = self.select_tags(self.data["camera"]["angles"])
        camera_framings = self.select_tags(self.data["camera"]["framings"])

        protagonists = self.data["protagonists"]
        protagonists = self.select_tags(protagonists)
        match protagonists:
            case "1girl":
                protagonists = "1girl, solo"
            case "1girl, 1boy":
                protagonists = "1girl, 1boy, solo focus"

        self.components = {
            'prefix': prefix,
            'protagonist': protagonists,
            'camera_angles': camera_angles,
            'camera_framings': camera_framings
        }
