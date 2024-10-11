import random
from src.scene.scene import Scene


def main():

    seed = random.randint(0, 1000)
    print(f"Seed: {seed}")
    scene = Scene(seed)
    print(scene)


if __name__ == "__main__":
    main()
