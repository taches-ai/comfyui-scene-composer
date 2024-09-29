import os
import yaml

import random

from src.scene import Scene
from src.data import Data
from src.character.character import Character


def main():

    # Settings
    config_path = "config"
    seed = random.randint(0, 1000)
    print(f"Seed: {seed}")

    data = Data(path="config", seed=seed)
    scene = Scene(data)

    scene.define_action("normal")
    print(scene.get_prompt())
    print("")

    sexual_acts = data.random_data["composition"]["actions"]["sexual"]
    scene.define_action("sexual")

    if "masturbation" in sexual_acts:
        data.random_data_union({
            "composition": {
                "protagonists": ["1girl"],
                "actions": {
                    "sexual":
                        ["fingering"]
                }
            }
        })
    if "handjob" in sexual_acts:
        data.random_data_union({
            "composition": {
                "protagonists": ["1girl", "1boy"],
                "actions": {
                    "sexual": 
                        ["caressing testicles"]
                }
            }
        })
    if "fellatio" in sexual_acts:
        data.random_data_union({
            "composition": {
                "protagonists": ["1girl", "1boy"],
                "actions": {
                    "sexual":
                        ["deepthroat"]
                }
            }
        })
    if "paizuri" in sexual_acts:
        data.random_data_union({
            "composition": {
                "protagonists": ["1girl", "1boy"],
                "actions": {
                    "sexual": 
                        ["straddling paizuri"]
                }
            }
        })
    if "doggystyle" in sexual_acts:
        data.random_data_union({
            "composition": {
                "protagonists": ["1girl", "2boy"],
                "actions": {
                    "sexual":
                        ["double penetration"]
                }
            }
        })
    if "standing_sex" in sexual_acts:
        data.random_data_union({
            "composition": {
                "protagonists": ["1girl", "1boy"],
                "actions": {
                    "sexual":
                        ["anal sex"]
                }
            }
        })
    print(scene.get_prompt())




if __name__ == "__main__":
    main()
