from node import Node

from src.subject.eyes import Eyes
from src.subject.hair import Hair
from src.subject.body import Body
from subject.clothes import Clothes


class subject(Node):

    def __init__(self, data, seed):
        super().__init__(data, seed)
        self.components = {
            'body': Body(self.data["subject"]["body"], self.seed),
            'hair': Hair(self.data["subject"]["hair"], self.seed),
            'eyes': Eyes(self.data["subject"]["eyes"], self.seed),
            'clothes': Clothes(self.data["clothes"], self.seed)
        }
