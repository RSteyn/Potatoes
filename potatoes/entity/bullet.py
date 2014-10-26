from ..attributes.movable import Movable
from ..attributes.renderable import Renderable
from ..attributes.killable import Killable
from ..attributes.collidable import Collidable
from .entity import Entity


class Bullet(Entity, Movable, Renderable, Killable, Collidable):
    VELOCITY = 200          # TODO: Balance this
    ACCEL = 2000            # TODO: Balance this

    def __init__(self, shooter, x, y, direction, canvas):
        Entity.__init__(self, x, y)
        Movable.__init__(self, self.VELOCITY, direction, self.ACCEL)
        Renderable.__init__(self, self._pos.x, self._pos.y, 110, 143,
                            'resources/dean.gif', canvas)
        Killable.__init__(self, 1)
         # TODO: Set correct ellipse dimensions
        Collidable.__init__(self, self.pos.x, self.pos.y,
                            50, 50, canvas)
        self.shooter = shooter  # Stores reference to who shot this bullet.

    def update(self, delta, gx):
        self.move(delta)
        gx.coords(self.img, (self._pos.x, self._pos.y))
        self.bounding_ellipse.update(self.pos, gx)