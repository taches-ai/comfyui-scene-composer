import argparse
import random
from src.scene import Scene


def main(node, seed=0):

    if not seed:
        seed = random.randint(0, 0xffffffffffffffff)

    scene = Scene(seed)

    if node:
        output = scene.components[node]

    output = scene

    print(f"SEED: {seed}")
    print(f"TAGS: {output}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simulate a scene")

    parser.add_argument(
        "--seed", "-s",
        type=int,
        default=0,
        help="Seed for the node"
    )

    parser.add_argument(
        "--node", "-n",
        type=str,
        choices=["composition", "subject", "action", "environment"],
        help="Name of the node to simulate"
    )

    args = parser.parse_args()
    main(args.node, args.seed)
