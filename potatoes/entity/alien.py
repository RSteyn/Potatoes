from . import Entity
from ..attributes import Movable, Renderable, Shootable, Killable
from ..attributes.collidable import Collidable
from ..vector import Vector
import math


class Alien(Entity, Movable, Renderable, Shootable, Killable, Collidable):
    MOVE_VELOCITY = 80              # TODO: Balance this
    ROTATE_VELOCITY = 0.1           # TODO: Balance this
    ACCEL = 125                     # TODO: Balance this

    SHOOT_INTERVAL = 3              # TODO: Balance this
    DIST_FROM_PLAYER = 400          # TODO: Balance this

    def __init__(self, canvas, player: Entity):
        Entity.__init__(self, 100, 100)
        Movable.__init__(self, 0, 0, self.ACCEL)
        Renderable.__init__(self, self._pos.x, self._pos.y, 110, 143,
                            'resources/dean.gif', canvas)
        Shootable.__init__(self)
        Killable.__init__(self, 5)
        # TODO: Set correct ellipse dimensions
        Collidable.__init__(self, self.pos.x, self.pos.y,
                            80, 100, canvas)
        self._rotating = 0
        self._target = player
        self._shoot_timer = 0

    def ai_update(self, delta, gx):
        target_diff = self._target.pos - self._pos
        # TODO: remove magic number?
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

        self._shoot_timer += delta
        if self._shoot_timer >= self.SHOOT_INTERVAL:
            self.shoot(self.pos.x, self.pos.y, target_diff.direction, gx)
            self._shoot_timer = 0

    def update(self, delta, gx):
        super().update(delta, gx)
        self.ai_update(delta, gx)
        self.rotate(self._rotating, delta)
        self.move(delta)
        self.update_bullets(delta, gx)
        gx.coords(self.img, (self._pos.x, self._pos.y))
        self.bounding_ellipse.update(gx, self.pos)
