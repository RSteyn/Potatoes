from .entity import *


class Player(Entity, Movable, Renderable, Shootable):
    CW = -1
    ACW = 1

    MOVE_VELOCITY = 5           # TODO: Balance this
    ROTATE_VELOCITY = 0.1

    def __init__(self, bind_to, canvas):
        Entity.__init__(self)
        Movable.__init__(self)
        Renderable.__init__(self, self._pos.x, self._pos.y,
                            'resources/dean.gif', canvas)
        Shootable.__init__(self)

        self._rotating = 0
        self._rotating_cw_ = False
        self._rotating_acw_ = False

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

    def start_moving_forward(self):
        self.velocity = self.MOVE_VELOCITY

    def stop_moving_forward(self):
        self.velocity = 0

    def start_rotating(self, direction):
        self._rotating = self.ROTATE_VELOCITY * direction

    def stop_rotating(self):
        self._rotating = 0

    def update(self, delta, gx):
        super().update(delta, gx)
        self.rotate(self._rotating)
        self.move()
        gx.coords(self.img, (self._pos.x, self._pos.y))