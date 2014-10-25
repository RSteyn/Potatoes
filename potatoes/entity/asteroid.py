from ..attributes import Movable, Renderable
from .entity import Entity
import random
import math

class Asteroid(Entity, Movable, Renderable):
    MAX_VEL = 50    # TODO: Balance this
    MIN_VEL = 20    # TODO: Balance this
    ACCEL = 125     # TODO: Balance this

    def __init__(self, canvas):
        Entity.__init__(self, random.randrange(0, 800),
                        random.randrange(0, 500))
        dir = 2*math.pi * random.random()
        vel = random.randrange(self.MIN_VEL, self.MAX_VEL)
        Movable.__init__(self, velocity=vel, direction=dir, accel=self.ACCEL)
        Renderable.__init__(self, self._pos.x, self._pos.y,
                            'resources/potato_chip.gif', canvas)
    def update(self, delta, gx):
        self.move(delta)
        gx.coords(self.img, (self._pos.x, self._pos.y))