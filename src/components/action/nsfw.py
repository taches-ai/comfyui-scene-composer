from ...node import Node
from ...utils import is_true


class ActionNSFW(Node):

    def __init__(self, seed=0):
        super().__init__(seed, data_file="actions.toml")

    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        seed = inputs["required"]["seed"]
        data = cls().data

        positions = cls().build_inputs_list(data["sfw"]["positions"])
        gestures = cls().build_inputs_list(data["sfw"]["gestures"])
        act_types = cls().build_inputs_list(data["nsfw"]["acts"].keys())

        # Update the required inputs
        inputs["required"] = {
            "nsfw": ("BOOLEAN", {"default": False}),
            # SFW inputs
            "position": (positions,),
            "gesture": (gestures,),
            # NSFW inputs
            "act_type": (act_types,),
            "seed": seed
        }

        return inputs

    def build_prompt(self, seed, nsfw, position, gesture, act_type):

        self.seed = seed
        prompt = ""

        if nsfw:
            prompt = self.handle_nsfw_scene(act_type)
        else:
            prompt = self.handle_sfw_scene(position, gesture)

        return (prompt,)

    def handle_sfw_scene(self, position, gesture):
        data = self.data["sfw"]

        position = self.select_tags(
            tags=data["positions"],
            selected=position
        )

        gesture = self.select_tags(
            tags=data["gestures"],
            selected=gesture
        )

        prompt = f"{position}, {gesture}"
        return prompt

    def handle_nsfw_scene(self, act_type):
        data = self.data["nsfw"]

        # Handle random action case
        action = self.select_tags(
            tags=data["acts"],
            selected=act_type
        )

        settings = self.apply_settings(data["settings"])
        prompt = self.enhance_prompt(data["acts"], action, settings)
        return prompt

    def apply_settings(self, data):

        settings = {}

        for key, value in data.items():
            settings[key] = self.select_tags(data[key])

        return settings

    def enhance_prompt(self, data, act_type, settings):

        act = act_type
        if act_type in data:
            act = self.select_tags(data[act_type])

        penis, pussy = self.build_sex_parts(settings)
        sweat = "sweat"

        # Enhance act
        if act_type in data["intercourses"]:
            insertion = self.select_tags(settings["insertions"])
            act += f", {insertion}"

        # Enhance preliminary
        if act_type in data["preliminaries"]:
            if "fingering" in act_type:
                penis = ""
                if is_true(self.seed, 0.5):
                    act += ", fingering from behind"
            else:
                pussy = ""

        # Enhance teasing
        if "flashing" in act_type:
            # TODO: Add random body part flashing
            penis = ""
            pussy = ""
            act += ", nipples, clothes lift"

        components = [act, penis, pussy, sweat]
        act = self.stringify_tags(components)
        return act

    def build_sex_parts(self, settings):

        # Penis
        penis = f"{settings['penis_sizes']} penis"

        if settings["hide_male"]:
            penis += ", disembodied penis"

        # Testicles
        testicles = ""
        if is_true(self.seed, 0.3):
            testicles = f"{settings['testicles_sizes']} testicles"

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
