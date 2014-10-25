from . import Entity
from ..attributes import Movable, Renderable, Shootable
from ..vector import Vector
import math


class Alien(Entity, Movable, Renderable, Shootable):
    MOVE_VELOCITY = 80
    ROTATE_VELOCITY = 0.1
    ACCEL = 125

    DIST_FROM_PLAYER = 400

    def __init__(self, canvas, player: Entity):
        Entity.__init__(self, 100, 100)
        Movable.__init__(self, 0, 0, self.ACCEL)
        Renderable.__init__(self, self._pos.x, self._pos.y,
                            'resources/dean.gif', canvas)
        Shootable.__init__(self)

        self._rotating = 0
        self._target = player

    def ai_update(self):
        target_diff = self._target.pos - self._pos
        if target_diff.magnitude > self.DIST_FROM_PLAYER + 30:
            vel = self.MOVE_VELOCITY
            direc = target_diff.direction
        elif target_diff.magnitude > self.DIST_FROM_PLAYER - 30:
            vel = self.MOVE_VELOCITY
            direc = target_diff.direction + (math.pi / 2)
        else:
            vel = -self.MOVE_VELOCITY
            direc = target_diff.direction + (math.pi / 2)
        self._moving = Vector(vel, direc, polar=True)

    def update(self, delta, gx):
        super().update(delta, gx)
        self.ai_update()
        self.rotate(self._rotating)
        self.move(delta)
        self.update_bullets(delta, gx)
        gx.coords(self.img, (self._pos.x, self._pos.y))
