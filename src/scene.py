from .node import Node
from .composition.composition import Composition
from .action.action import Action
from .subject.character import Character
from .environment.environment import Environment


class Scene(Node):

    def __init__(self, seed=0):
        super().__init__(seed)

        self.components = {
            'composition': Composition(self.seed),
            'action': Action(self.seed),
            'subject': Character(self.seed),
            'environment': Environment(self.seed)
        }

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        components = cls().components
        action_data = components["action"].data
        action_list = action_data["normal"]["list"]
        action_list.insert(0, "random")

        # Update the required inputs
        required_inputs = {
            "action_type": (action_list,),
            "seed": inputs["required"]["seed"]
        }
        inputs["required"] = required_inputs

        # Update the optional inputs
        optional_components = {
            key: ("STRING", {
                "default": "",
                "forceInput": True
            })
            for key in components.keys()}

        inputs["optional"] = optional_components
        return inputs

    def run_node(self, action_type, seed, **kwargs):

        if action_type != "random":
            self.components["action"].type = ["normal", action_type]

        # Update components based on kwargs
        for key, value in kwargs.items():
            if key in self.components and value != "":
                self.components[key] = value

        self.update_seed(seed)
        prompt = self.get_prompt()
        return (prompt,)
