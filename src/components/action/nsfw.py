from ...node import Node


class ActionNSFW(Node):

    def __init__(self, seed=0):
        super().__init__(seed, data_file="actions.toml")

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        seed = inputs["required"]["seed"]
        data = cls.data["nsfw"]
        actions = cls.build_inputs_list(data["actions"].keys())

        # Update the required inputs
        inputs["required"] = {
            "action": (actions,),
            "seed": seed,
        }

        return inputs

    def build_prompt(self, seed, action):

        self.seed = seed

        # Handle random action case
        if action == "random":
            action = self.select_tags(
                tags=self.data["nsfw"]["actions"],
            )

        # Define action
        action = self.select_tags(
            tags=self.data["nsfw"]["actions"][action],
        )

        prompt = action
        return (prompt,)
