from .attributes import *


class Player(Entity, Movable, Renderable, Shootable):
    def __init__(self):
        super().__init__()
