from .vector import Vector


class Entity:
    def __init__(self, x=0, y=0):
        self._pos = Vector(x, y)

    def update(self, delta, gx):
        pass
