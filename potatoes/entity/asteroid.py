from ..attributes import Movable, Renderable
from . import Entity
import random
import math

class Asteroid(Entity, Movable, Renderable):
    MAX_VEL = 50  # TODO: Balance this
    MIN_VEL = 20  # TODO: Balance this
    VEL_RANGE = MAX_VEL - MIN_VEL
    def __init__(self, canvas):
        Entity.__init__(self, 400, 250)
        dir = 2*math.pi * random.random()
        vel = Asteroid.VEL_RANGE * random.random() + Asteroid.MIN_VEL
        Movable.__init__(self, velocity=vel, direction=dir)
        Renderable.__init__(self, self._pos.x, self._pos.y,
                            'resources/potato_chip.gif', canvas)
    def update(self, delta, gx):
        self.move(delta)
        gx.coords(self.img, (self._pos.x, self._pos.y))