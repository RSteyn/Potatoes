from .entity import Entity
from ..attributes import Movable, Renderable, Shootable
from ..vector import Vector


class Player(Entity, Movable, Renderable, Shootable):
    CW = 1
    ACW = -1

    MOVE_VELOCITY = 100           # TODO: Balance this
    ROTATE_VELOCITY = 0.1
    DIRECTION_OVAL_DISTANCE = 100
    DIRECTION_OVAL_COLOR = '#ff0000'
    DIRECTION_OVAL_WIDTH = 5

    def __init__(self, bind_to, canvas):
        Entity.__init__(self)
        Movable.__init__(self)
        Renderable.__init__(self, self._pos.x, self._pos.y,
                            'resources/dean.gif', canvas)
        Shootable.__init__(self)

        self._rotating = 0
        self._rotating_cw_ = False
        self._rotating_acw_ = False

        # Movement event bindings
        bind_to.bind('<KeyPress-Up>',
                     lambda _: self.start_moving_forward())
        bind_to.bind('<KeyPress-Down>',
                     lambda _: None)
        bind_to.bind('<KeyPress-Left>',
                     lambda _: self.start_rotating(self.ACW))
        bind_to.bind('<KeyPress-Right>',
                     lambda _: self.start_rotating(self.CW))

        bind_to.bind('<KeyRelease-Up>',
                     lambda _: self.stop_moving_forward())
        bind_to.bind('<KeyRelease-Down>',
                     lambda _: None)
        bind_to.bind('<KeyRelease-Left>',
                     lambda _: self.stop_rotating())
        bind_to.bind('<KeyRelease-Right>',
                     lambda _: self.stop_rotating())

        # Bind shooting
        bind_to.bind('<space>',
                     lambda _: self.shoot(self._pos.x,
                                          self._pos.y,
                                          self.direction,
                                          canvas))

        # Create direction pointer
        self._oval = canvas.create_oval(
            0, 0, self.DIRECTION_OVAL_WIDTH, self.DIRECTION_OVAL_WIDTH,
            outline=self.DIRECTION_OVAL_COLOR
        )

    def start_moving_forward(self):
        self.velocity = self.MOVE_VELOCITY

    def stop_moving_forward(self):
        self.velocity = 0

    def start_rotating(self, direction):
        self._rotating = self.ROTATE_VELOCITY * direction

    def stop_rotating(self):
        self._rotating = 0

    def _direction_oval_loc_(self):
        rloc = Vector(self.DIRECTION_OVAL_DISTANCE, self.direction, polar=True)
        return Vector(self._pos.x + rloc.x, self._pos.y + rloc.y)

    def _oval_bbox_(self, v):
        size_v = Vector(self.DIRECTION_OVAL_WIDTH, self.DIRECTION_OVAL_WIDTH)
        tl = v - size_v
        br = v + size_v
        return tl.x, tl.y, br.x, br.y

    def update(self, delta, gx):
        super().update(delta, gx)
        self.rotate(self._rotating)
        self.move(delta)
        self.update_bullets(delta, gx)
        gx.coords(self.img, (self._pos.x, self._pos.y))
        new_oval_loc = self._direction_oval_loc_()
        gx.coords(self._oval, self._oval_bbox_(new_oval_loc))
