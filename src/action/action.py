from ..node import Node
from ..utils import get_nested_dict_value


class Action(Node):

    def __init__(self, seed, type=["normal"]):
        super().__init__(seed, data_file="actions.toml")
        self.type = type

    CATEGORY = Node.CATEGORY + "/Components"

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()

        action_data = cls().components["action"].data
        action_list = action_data.keys()
        action_list.insert(0, "random")

        # Update the required inputs
        required_inputs = {
            "action_type": (action_list,),
            "seed": inputs["required"]["seed"]
        }
        inputs["required"] = required_inputs
        return inputs

    def run_node(self, action_type):

        if action_type == "random":
            action_type = self.select_tags(self.data)

        data = self.data[action_type]
        prompt = self.select_tags(data)

        return (prompt,)

    def build_prompt(self):
        data = get_nested_dict_value(self.data, self.type)
        action = self.select_tags(data)
        self.prompt = [action]
