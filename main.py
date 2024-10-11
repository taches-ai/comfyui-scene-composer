import random
from src.scene import Scene


def main():

    seed = random.randint(0, 1000)
    print(f"Seed: {seed}")

    # Standard scene
    scene = Scene(seed)
    print(scene)

    # Preliminary scene
    scene_preliminary = Scene(seed)
    scene_preliminary.define_action("preliminary")
    print(scene_preliminary)


if __name__ == "__main__":
    main()
