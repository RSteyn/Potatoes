from ..attributes import Movable, Renderable, Killable
from .entity import Entity
from ..values import GAME_WIDTH, GAME_HEIGHT, KILL_MIN, KILL_RIGHT, KILL_BOT
from random import random, randrange
import math

class Asteroid(Entity, Movable, Renderable, Killable):
    MAX_VEL = 50    # TODO: Balance this
    MIN_VEL = 20    # TODO: Balance this
    ACCEL = 125     # TODO: Balance this

    EIGHTH = math.pi / 4
    POINT_1 = 7 * EIGHTH
    POINT_2 = EIGHTH
    POINT_3 = 3 * EIGHTH
    POINT_4 = 5 * EIGHTH

    def __init__(self, canvas):
        dir = 2*math.pi * random()
        vel = randrange(self.MIN_VEL, self.MAX_VEL)
        if self.POINT_1 <= dir < self.POINT_2:
            start_pos = (KILL_MIN + 1, randrange(0, GAME_HEIGHT))
        elif self.POINT_2 <= dir < self.POINT_3:
            start_pos = (randrange(0, GAME_WIDTH), KILL_BOT - 1)
        elif self.POINT_3 <= dir < self.POINT_4:
            start_pos = (KILL_RIGHT - 1, randrange(0, GAME_HEIGHT))
        else:
            start_pos = (randrange(0, GAME_WIDTH), KILL_MIN + 1)
        print(dir, start_pos)
        Entity.__init__(self, *start_pos)
        Movable.__init__(self, velocity=vel, direction=dir, accel=self.ACCEL)
        Renderable.__init__(self, self._pos.x, self._pos.y,
                            'resources/potato_chip.gif', canvas)
        Killable.__init__(self, 1)
    def update(self, delta, gx):
        self.move(delta)
        gx.coords(self.img, (self._pos.x, self._pos.y))