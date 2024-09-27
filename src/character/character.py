from src.components import Component

from src.character.eyes import Eyes
from src.character.hair import Hair
from src.character.body import Body
from src.character.clothes.clothes import Clothes


class Character(Component):

    def __init__(self, data, seed):
        super().__init__(data, seed)
        self.components = {
            'body': Body(self.data["character"]["body"], self.seed),
            'hair': Hair(self.data["character"]["hair"], self.seed),
            'eyes': Eyes(self.data["character"]["eyes"], self.seed),
            'clothes': Clothes(self.data["clothes"], self.seed)
        }
