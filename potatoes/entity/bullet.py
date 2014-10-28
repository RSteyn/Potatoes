from ..attributes.movable import Movable
from ..attributes.renderable import Renderable
from ..attributes.killable import Killable
from ..attributes.collidable import Collidable
from .entity import Entity
from ..values import GAME_HEIGHT, GAME_WIDTH


class Bullet(Entity, Movable, Renderable, Killable, Collidable):
    VELOCITY = 200         # TODO: Balance this
    ACCEL = 2000            # TODO: Balance this

    def __init__(self, state, shooter, pos, direction, canvas):
        Entity.__init__(self, state, pos)
        Movable.__init__(self, Bullet.VELOCITY, direction,
                 accel=Bullet.ACCEL,
                 max_speed=Bullet.VELOCITY,
                 friction=1)
        Renderable.__init__(self, self.pos, 22, 35,
                            'resources/cutter.gif', canvas)
        Killable.__init__(self, 1)
         # TODO: Set correct ellipse dimensions
        Collidable.__init__(self, self.pos,
                            8, 8, canvas)
        self.shooter = shooter  # Stores reference to who shot this bullet.

    def update(self, delta, gx):
        Renderable.update(self)
        self.move(delta)
        gx.coords(self.img, (self._pos.x, self._pos.y))
        self.bounding_ellipse.update(gx, self.pos)
        # Do boundary checking
        if self.pos.x + self.width//2 <=0 \
                or self.pos.x - self.width//2 > GAME_WIDTH:
            self.shooter.remove(self)
        if self.pos.y + self.height//2 <=0 \
                or self.pos.y - self.height//2 > GAME_HEIGHT:
            self.shooter.remove(self)