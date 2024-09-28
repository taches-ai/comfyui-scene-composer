import os
import yaml

import random

from src.scene import Scene
from src.data import Data
from src.character.character import Character


def main():

    # Settings
    config_path = "config"
    seed = 542
    print(f"Seed: {seed}")
    data = Data(path="config", seed=seed)
    scene = Scene(data)
    scene.define_action("sexual.preliminary.masturbation")
    print(scene.get_prompt())
    print("")
    data.set_random_data(145)
    print(scene.get_prompt())




if __name__ == "__main__":
    main()
