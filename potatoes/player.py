from .entity import *


class Player(Entity, Movable, Renderable, Shootable):
    def __init__(self):
        super().__init__()

    def update(self, delta):
        super().update(delta)

    def render(self, gx):
        super().render(gx)
