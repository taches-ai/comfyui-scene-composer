from ..node import Node

from .body import Body
from .hair import Hair
from .eyes import Eyes
from .clothes import Clothes


class Character(Node):

    CATEGORY = Node.CATEGORY + "/Components"

    def build_components(self):
        self.components = {
            'body': Body(self.seed),
            'hair': Hair(self.seed),
            'eyes': Eyes(self.seed),
            'clothes': Clothes(self.seed)
        }
