from src.scene.component import Component

from src.subject.body import Body
from src.subject.hair import Hair
from src.subject.eyes import Eyes
from src.subject.clothes import Clothes


class Character(Component):

    def __init__(self, seed):
        super().__init__(seed)
        self.components = {
            'body': Body(self.seed),
            'hair': Hair(self.seed),
            'eyes': Eyes(self.seed),
            'clothes': Clothes(self.seed)
        }
