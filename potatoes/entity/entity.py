from ..vector import Vector
from ..ellipse import Ellipse

class Entity:
    def __init__(self, pos, width=1, height=1):
        self._pos = pos

    @property
    def pos(self):
        return self._pos

    def update(self, delta, gx):
        pass
