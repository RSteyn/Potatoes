from ..attributes.movable import Movable
from ..attributes.renderable import Renderable
from .entity import Entity


class Bullet(Entity, Movable, Renderable):
    VELOCITY = 200          # TODO: Balance this
    ACCEL = 125             # TODO: Balance this

    def __init__(self, shooter, x, y, direction, canvas):
        Entity.__init__(self, x, y)
        Movable.__init__(self, self.VELOCITY, direction, self.ACCEL)
        Renderable.__init__(self, self._pos.x, self._pos.y,
                            'resources/dean.gif', canvas)
        self.shooter = shooter  # Stores reference to who shot this bullet.

    def update(self, delta, gx):
        self.move(delta)
        gx.coords(self.img, (self._pos.x, self._pos.y))