from ..vector import Vector


class Entity:
    def __init__(self, x=0, y=0):
        self._pos = Vector(x, y)

    @property
    def pos(self):
        return self._pos

    def update(self, delta, gx):
        pass
