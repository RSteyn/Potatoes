from ..vector import Vector
from ..ellipse import Ellipse

class Entity:
    def __init__(self, x=0, y=0, width=1, height=1):
        self._pos = Vector(x, y)

    @property
    def pos(self):
        return self._pos

    def update(self, delta, gx):
        pass
