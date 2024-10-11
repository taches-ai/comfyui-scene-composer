from .src.scene import Scene
from .src.composition.composition import Composition
from .src.action import Action
from .src.subject.character import subject
from .src.environment.environment import Environment


NODE_CLASS_MAPPINGS = {
    "Scene": Scene,
    "Composition": Composition,
    "Action": Action,
    "subject": subject,
    "Environment": Environment,
}

__all__ = ["NODE_CLASS_MAPPINGS"]
