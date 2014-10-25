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
    def move(self, by):
        self._pos += by
