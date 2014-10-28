from . import Entity
from ..attributes import Movable, Renderable, Shootable, Killable
from ..attributes.collidable import Collidable
from ..vector import Vector
from random import randrange
from ..values import GAME_WIDTH, GAME_HEIGHT


class Alien(Entity, Movable, Renderable, Shootable, Killable, Collidable):
    MOVE_VELOCITY = 80              # TODO: Balance this
    ROTATE_VELOCITY = 0.1           # TODO: Balance this
    ROTATE_ACCEL = 100              # TODO: Balance this
    ACCEL = 125                     # TODO: Balance this

    SHOOT_INTERVAL = 3              # TODO: Balance this
    DIST_FROM_PLAYER = 400          # TODO: Balance this

    def __init__(self, canvas, player: Entity):
        Entity.__init__(self, Vector(100, 100))
        Movable.__init__(self, 0, 0,
                         accel=Alien.ACCEL,
                         ang_accel=Alien.ROTATE_ACCEL,
                         max_speed=Alien.MOVE_VELOCITY,
                         max_rot_val=Alien.ROTATE_VELOCITY)
        Renderable.__init__(self, self.pos, 69, 110,
                            'resources/ruan.gif', canvas)
        Shootable.__init__(self, Alien.SHOOT_INTERVAL)
        Killable.__init__(self, 5)
        Collidable.__init__(self, self.pos.x, self.pos.y,
                            32, 55, canvas)
        self._rotating = 0
        self._target = player
        self._shoot_timer = 0
        self._target_pos = Vector(GAME_WIDTH//2, GAME_HEIGHT//2)

    def ai_update(self, delta, gx):
        """
        Alien behavior is just to wander around the screen,
        though not getting too near the player
        :param delta: Time since last update
        :param gx: Graphics device, canvas in this case.
        """
        target_pos_diff = self._target_pos - self._pos
        if target_pos_diff.magnitude < 1:
            # Choose new target
            new_x = randrange(0, GAME_WIDTH)
            new_y = randrange(0, GAME_HEIGHT)
            self._target_pos = Vector(new_x, new_y)
        else:
            self._cur_velocity = target_pos_diff
            if self._cur_velocity.magnitude > Alien.MOVE_VELOCITY:
                self._cur_velocity.to_magnitude(Alien.MOVE_VELOCITY)

        shoot_target_diff = self._target.pos - self.pos
        self.shoot(self.pos, shoot_target_diff.direction, gx)

    def update(self, delta, gx):
        super().update(delta, gx)
        Shootable.update(self, delta, gx)
        self.ai_update(delta, gx)
        self.move(delta)

        gx.coords(self.img, (self._pos.x, self._pos.y))
        self.bounding_ellipse.update(gx, self.pos)
