__author__ = 'rileysteyn'
from .entity import *
import random
import math
class Asteroid(Entity, Movable, Renderable):
    MAX_VEL = 5  # TODO: Balance this
    MIN_VEL = 2  # TODO: Balance this
    VEL_RANGE = MAX_VEL - MIN_VEL
    def __init__(self, canvas):
        Entity.__init__(self)
        Movable.__init__(self)
        Renderable.__init__(self, self._pos.x, self._pos.y,
                            'resources/dean.gif', canvas)
        self._pos = Vector(400, 250)
        dir = 2*math.pi * random.random()
        vel = Asteroid.VEL_RANGE * random.random() + Asteroid.MIN_VEL
        self._moving = Vector(vel, dir, polar=True)
    def update(self, delta, gx):
        self.move()
        gx.coords(self.img, (self._pos.x, self._pos.y))