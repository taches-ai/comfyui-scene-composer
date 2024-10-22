from ...node import Node


class Action(Node):

    def __init__(self, seed=0):
        super().__init__(seed, data_file="actions.toml")

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        seed = inputs["required"]["seed"]
        data = cls().data["normal"]

        position = cls().build_inputs_list(data["position"])
        action = cls().build_inputs_list(data["action"])

        # Update the required inputs
        inputs["required"] = {
            "position": (position,),
            "action": (action,),
            "seed": seed,
        }

        return inputs

    def build_prompt(self, seed, position, action):

        self.seed = seed

        position = self.select_tags(
            tags=self.data["normal"]["position"],
            selected=position
        )

        action = self.select_tags(
            tags=self.data["normal"]["action"],
            selected=action
        )

        prompt = f"{position}, {action}"
        return (prompt,)
