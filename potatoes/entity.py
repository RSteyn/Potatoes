from .vector import Vector


class Entity:
    def __init__(self):
        self._pos = Vector(0, 0)

    def update(self, delta):
        pass


class Renderable:
    def render(self, gx):
        pass


class Shootable:
    def shoot(self, x, y):
        pass


class Movable:
    def __init__(self):
        self._moving = Vector(0, 0)

    @property
    def moving(self):
        return self._moving

    @moving.setter
    def moving(self, val):
        self._moving = val

    def move(self):
        self._pos += self._moving
