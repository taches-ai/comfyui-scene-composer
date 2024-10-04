from src.components import Component

from src.character.eyes import Eyes
from src.character.hair import Hair
from src.character.body import Body
from src.character.clothes.clothes import Clothes


class Character(Component):

    def __init__(self, data):
        super().__init__(data)
        self.components = {
            'body': Body(data),
            'hair': Hair(data),
            'eyes': Eyes(data),
            'clothes': Clothes(data)
        }
