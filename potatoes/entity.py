

class Entity:
    def __init__(self):
        self._x = 0
        self._y = 0

    def update(self, delta):
        pass


class Renderable:
    def render(self, gx):
        pass


class Shootable:
    def shoot(self, x, y):
        pass


class Movable:
    def move(self, x, y):
        self._x += x
        self._y += y
