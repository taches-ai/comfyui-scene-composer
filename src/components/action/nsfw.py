from ...node import Node
from ...utils import is_true


class ActionNSFW(Node):

    def __init__(self, seed=0):
        super().__init__(seed, data_file="actions.toml")
        self.data = self.data["nsfw"]

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        seed = inputs["required"]["seed"]
        data = cls().data
        actions = cls().build_inputs_list(data["actions"].keys())

        # Update the required inputs
        inputs["required"] = {
            "action_type": (actions,),
            "seed": seed,
        }

        return inputs

    def build_prompt(self, seed, action_type):

        self.seed = seed

        # Handle random action case
        action = self.select_tags(
            tags=self.data["actions"],
            selected=action_type
        )

        settings = self.apply_settings(self.data["settings"])
        prompt = self.enhance_prompt(self.data["actions"], action, settings)
        return (prompt,)

    def apply_settings(self, data):

        settings = {}

        for key, value in data.items():
            settings[key] = self.select_tags(data[key])

        return settings

    def enhance_prompt(self, data, action_type, settings):

        action = action_type
        if action_type in data:
            action = self.select_tags(data[action_type])

        penis, pussy = self.build_sex_parts(settings)
        sweat = "sweat"

        # Enhance position
        if action_type in data["position"]:
            insertion = self.select_tags(settings["insertion"])
            action += f", {insertion}"

        # Enhance preliminary
        if action_type in data["preliminary"]:
            if "fingering" in action_type:
                penis = ""
                if is_true(self.seed, 0.5):
                    action += ", fingering from behind"
            else:
                pussy = ""

        # Enhance teasing
        if "flashing" in action_type:
            # TODO: Add random body part flashing
            penis = ""
            pussy = ""
            action += ", nipples, clothes lift"

        components = [action, penis, pussy, sweat]
        action = self.stringify_tags(components)
        return action

    def build_sex_parts(self, settings):

        # Penis
        penis = f"{settings['penis_size']} penis"

        if settings["hide_male"]:
            penis += ", disembodied penis"

        # Testicles
        testicles = ""
        if is_true(self.seed, 0.3):
            testicles = f"{settings['testicles_size']} testicles"

        # Pussy
        pussy = "pussy"
        pussy_juice = "pussy juice"
        pussy_juice_weight = settings["pussy_juice"]

        if pussy_juice_weight >= 1:
            additional_tags = {
                "repeat": [1, 2],
                "tags": ["pussy juice trail", "pussy juice puddle"]
            }
            pussy_juice += ", " + self.select_tags(additional_tags)

        if pussy_juice_weight >= 1.1:
            pussy_juice = f"excessive {pussy_juice}"

        # Merge
        penis = self.stringify_tags([penis, testicles])
        pussy = self.stringify_tags([pussy, pussy_juice])
        return penis, pussy
