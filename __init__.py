from .src.scene import Scene
from .src.composition.composition import Composition
from .src.action.action import Action
from .src.subject.character import Character
from .src.environment.environment import Environment

NODE_CLASS_MAPPINGS = {
    "🎞️ Scene": Scene,
    "📹 Composition": Composition,
    "🎬 Action": Action,
    "👤 Character": Character,
    "⛅️ Environment": Environment,
}

__all__ = ['NODE_CLASS_MAPPINGS']
