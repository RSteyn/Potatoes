__author__ = 'rileysteyn'
from .entity import *
class Bullet(Entity, Movable, Renderable):
    def __init__(self, x, y, direction, canvas):
        Entity.__init__(self, x, y)
        Movable.__init__(self, direction)
        Renderable.__init__(self._pos.x, self._pos.y,
                            'resources/dean.gif', canvas)

