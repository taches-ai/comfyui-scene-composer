from ..node import Node

from .body import Body
from .hair import Hair
from .eyes import Eyes
from .clothes import Clothes


class Character(Node):

    def __init__(self):
        super().__init__()
        self.components = {
            'body': Body(),
            'hair': Hair(),
            'eyes': Eyes(),
            'clothes': Clothes()
        }
