from ..vector import Vector
from ..ellipse import Ellipse

class Entity:
    def __init__(self, pos, width=1, height=1, screen_wrap=False):
        self._pos = pos
        self.screen_wrap = screen_wrap

    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, value):
        self._pos = value

    def update(self, delta, gx):
        pass
