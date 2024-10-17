from ..node import Node
from ..utils import get_nested_dict_value


class Action(Node):

    def __init__(self, seed=0, type=["normal"]):
        super().__init__(seed, data_file="actions.toml")
        self.type = type

    CATEGORY = Node.CATEGORY + "/Components"

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        data = cls.load_data(cls.data_path)

        action_list = cls.build_inputs_list(
            data["sexual"]["intercourses"]["list"])
        penis_list = cls.build_inputs_list(data["sexual"]["penis_size"])
        insertion_list = cls.build_inputs_list(
            data["sexual"]["intercourses"]["insertion"])

        # Update the required inputs
        required_inputs = {
            "action_type": (action_list,),
            "penis_list": (penis_list,),
            "insertion_list": (insertion_list,),
            "seed": inputs["required"]["seed"]
        }
        inputs["required"] = required_inputs
        return inputs

    def run_node(self, action_type, penis, insertion, seed):

        self.update_seed(seed)

        # TODO: The construction of inputs should be simplified
        # There is too much repetition
        if action_type == "random":
            preliminary = self.data["sexual"]["intercourses"]["preliminary"]
            main = self.data["sexual"]["intercourses"]["main"]
            intercourses = list(preliminary + main)
            action_type = self.select_tags(intercourses)

        if penis == "random":
            penis = self.select_tags(self.data["sexual"]["penis_size"])

        if insertion == "random":
            insertion = self.select_tags(self.data["sexual"]["insertion"])

        data = self.data[action_type]
        prompt = self.select_tags(data)

        return (prompt,)

    def build_prompt(self):

        # TODO: seperate more clearly normal actions and sexual actions
        # Dynamic selection directly in the node or seperated node
        data = get_nested_dict_value(self.data, self.type)
        action = self.select_tags(data)

        male_is_hidden = self.data["sexual"]["hide_male"]
        penises = self.data["sexual"]["penis_size"]
        penis = self.select_tags(penises)

        if male_is_hidden:
            penis = f"{penis}, disembodied penis"

        intercourse = self.data["sexual"]["intercourse"]
        prompt = ""

        if action in intercourse["preliminary"]:
            prompt = f"{action}, {penis}"

        if action in intercourse["main"]:
            insertion = self.data["sexual"]["insertion"]
            prompt = f"{action}, {insertion}, pussy, anus"

        self.prompt = [prompt]
