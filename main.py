import os
import yaml

import random

from src.scene import Scene


def main():

    # Settings
    config_path = "config"
    seed = random.randint(0, 1000)
    print(f"Seed: {seed}")

    data = merge_config_files(config_path)
    scene = Scene(data, seed)

    # Output
    scene.define_action("normal")
    print(scene.components["composition"].action)
    scene.define_action("sexual.preliminary")
    print(scene.components["composition"].action)


def merge_config_files(path):
    """Merge all yaml files in a directory into a single dictionary"""
    config_files = [f for f in os.listdir(path) if f.endswith('.yaml')]
    merged_data = {}
    for file in config_files:
        file_path = os.path.join(path, file)
        file_name = os.path.splitext(file)[0]
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
                if data is not None:
                    merged_data[file_name] = data
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    return merged_data


if __name__ == "__main__":
    main()
