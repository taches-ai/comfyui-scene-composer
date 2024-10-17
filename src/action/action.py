from ..node import Node
from ..utils import get_nested_dict_value


class Action(Node):

    def __init__(self, seed=0, type=["normal"]):
        self.action_type = type
        super().__init__(seed, data_file="actions.toml")

    CATEGORY = Node.CATEGORY + "/Components"

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        seed = inputs["required"]["seed"]

        action_type = ["normal", "nsfw", "nsfw.preliminary", "nsfw.main"]

        # Update the required inputs
        inputs["required"] = {
            "action_type": (action_type,),
            "seed": seed,
        }

        return inputs

    def build_components(self):

        # TODO: seperate more clearly normal actions and nsfw actions
        # Dynamic selection directly in the node or seperated node
        data = get_nested_dict_value(self.data, self.action_type)
        action = self.select_tags(data)

        male_is_hidden = self.data["nsfw"]["settings"]["hide_male"]
        penises = self.data["nsfw"]["settings"]["penis_size"]
        penis = self.select_tags(penises)

        if male_is_hidden:
            penis = f"{penis}, disembodied penis"

        intercourse = self.data["nsfw"]
        action = self.select_tags(self.data[action])
        action = self.select_tags(self.data["normal"][action])

        if action in intercourse["preliminary"]:
            action = f"{action}, {penis}"

        if action in intercourse["main"]:
            insertion = self.select_tags(intercourse["insertion"])
            action = f"{action}, {insertion}, pussy, anus"

        self.components = {"action_type": action}
