from src.scene import Scene

from src.action.action import Action


def main():

    # Simluate a Scene node with seed
    scene = Scene(seed=1)
    print(f"Seed: {scene.seed}\n{scene}")

    # Change the seed of the whole scene
    scene.update_seed(2)
    print(f"Seed: {scene.seed}\n{scene}")

    # Change Action seed to match the first one
    scene.components["action"] = Action(seed=1)
    print(f"Action changed: {scene.components['action']}")

    # Define the action type
    scene.components["action"].type = "drinking"
    print(f"Action changed: {scene.components['action']}")


if __name__ == "__main__":
    main()
