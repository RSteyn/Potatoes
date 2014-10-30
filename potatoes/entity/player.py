from .entity import Entity
from ..attributes import Movable, Renderable, Shootable, Killable
from ..attributes.collidable import Collidable
from ..vector import Vector
from ..values import GAME_WIDTH, GAME_HEIGHT
import math


class Player(Entity, Movable, Renderable, Shootable, Killable, Collidable):
    MOVE_VELOCITY = 400             # TODO: Balance this
    ROTATE_VELOCITY = 0.08       # TODO: Balance this
    ROTATE_ACCEL = math.pi/64        # TODO: Balance this
    ACCEL = 50                     # TODO: Balance this
    DIRECTION_OVAL_DISTANCE = 100
    DIRECTION_OVAL_COLOR = '#ff0000'
    DIRECTION_OVAL_WIDTH = 5
    SHOOT_INTERVAL = 0.5

    def __init__(self, state, bind_to, canvas):
        Entity.__init__(self, state,
                        Vector(GAME_WIDTH//2, GAME_HEIGHT//2),
                        screen_wrap=True)
        Movable.__init__(self, 0, 0,
                         accel=Player.ACCEL,
                         ang_accel=Player.ROTATE_ACCEL,
                         max_speed=Player.MOVE_VELOCITY,
                         max_rot_val=Player.ROTATE_VELOCITY)
        Renderable.__init__(self, self.pos, 80, 110,
                            'resources/gardiner.gif', canvas)
        Shootable.__init__(self, Player.SHOOT_INTERVAL)
        Killable.__init__(self, 1)
        Collidable.__init__(self, self.pos,
                            40, 55, canvas)
        self._rotating = 0
        self._invul_time = 1
        self.invulnerable = True

        # Movement event bindings
        bind_to.bind('<KeyPress-Up>',
                     lambda _: self.is_accelerating(True))
        bind_to.bind('<KeyPress-Down>',
                     lambda _: None)
        bind_to.bind('<KeyPress-Left>',
                     lambda _: self.rot_dir(Movable.COUNTERCLOCKWISE))
        bind_to.bind('<KeyPress-Right>',
                     lambda _: self.rot_dir(Movable.CLOCKWISE))

        bind_to.bind('<KeyRelease-Up>',
                     lambda _: self.is_accelerating(False))
        bind_to.bind('<KeyRelease-Down>',
                     lambda _: None)
        bind_to.bind('<KeyRelease-Left>',
                     lambda _: self.rot_dir(Movable.NO_ROTATION))
        bind_to.bind('<KeyRelease-Right>',
                     lambda _: self.rot_dir(Movable.NO_ROTATION))

        # Bind shooting
        bind_to.bind('<space>',
                     lambda _: self.shoot(self.pos,
                                          -self.direction,
                                          canvas))

        # Create direction pointer
        self._oval = canvas.create_oval(
            0, 0, self.DIRECTION_OVAL_WIDTH, self.DIRECTION_OVAL_WIDTH,
            outline=self.DIRECTION_OVAL_COLOR
        )
    def _direction_oval_loc_(self):
        rloc = Vector(self.DIRECTION_OVAL_DISTANCE, self.direction, polar=True)
        return Vector(self._pos.x + rloc.x, self._pos.y - rloc.y)

    def _oval_bbox_(self, v):
        size_v = Vector(self.DIRECTION_OVAL_WIDTH, self.DIRECTION_OVAL_WIDTH)
        tl = v - size_v
        br = v + size_v
        return tl.x, tl.y, br.x, br.y

    def update(self, delta, gx):
        super().update(delta, gx)
        Renderable.update(self)
        Shootable.update(self, delta, gx)

        if self._invul_time > 0:
            self._invul_time -= delta
        else:
            self.invulnerable = False
        self.move(delta)
        self.perform_screen_wrap()
        self.bounding_ellipse.update(gx, self.pos)

        # Move image on canvas
        self.state.canvas.dtag(self._oval, 'idle')
        gx.coords(self.img, (self._pos.x, self._pos.y))

        # Move directional pointer on canvas
        new_oval_loc = self._direction_oval_loc_()
        gx.coords(self._oval, self._oval_bbox_(new_oval_loc))

    def perform_screen_wrap(self):
        # Do screen wrapping
        if self.pos.x + self.width//2 < 0:
            # Beyond left edge of screen, move to right
            self._pos = Vector(GAME_WIDTH + self.width//2, self._pos.y)
        elif self.pos.x - self.width//2 > GAME_WIDTH:
            # Beyond right edge of screen, move to left
            self._pos = Vector(-self.width//2, self._pos.y)

        if self.pos.y + self.height//2 < 0:
            # Beyond top edge of screen, move to bottom
            self._pos = Vector(self._pos.x, GAME_HEIGHT + self.height//2)
        elif self.pos.y - self.height//2 > GAME_HEIGHT:
            # Beyond bottom edge of screen, move to left
            self._pos = Vector(self._pos.x, -self.height//2)

    def collide_with_bullet(self, bullet):
        if not self.invulnerable:
            self.state.player_respawn()