from .entity import *


class Player(Entity, Movable, Renderable, Shootable):
    UP = -1
    DOWN = 1
    LEFT = -1
    RIGHT = 1

    def __init__(self, bind_to, canvas):
        Entity.__init__(self)
        Movable.__init__(self)
        Renderable.__init__(self, self._pos._x, self._pos._y,
                            'resources/dean.gif', canvas)
        Shootable.__init__(self)

        self._vel = 5           # TODO: Balance this
        bind_to.bind('<KeyPress-Up>',
                     lambda _: self.start_moving_y(self.UP))
        bind_to.bind('<KeyPress-Down>',
                     lambda _: self.start_moving_y(self.DOWN))
        bind_to.bind('<KeyPress-Left>',
                     lambda _: self.start_moving_x(self.LEFT))
        bind_to.bind('<KeyPress-Right>',
                     lambda _: self.start_moving_x(self.RIGHT))

        bind_to.bind('<KeyRelease-Up>',
                     lambda _: self.stop_moving_y())
        bind_to.bind('<KeyRelease-Down>',
                     lambda _: self.stop_moving_y())
        bind_to.bind('<KeyRelease-Left>',
                     lambda _: self.stop_moving_x())
        bind_to.bind('<KeyRelease-Right>',
                     lambda _: self.stop_moving_x())

    def start_moving_x(self, direction):
        self.moving.x = self._vel * direction

    def stop_moving_x(self):
        self.moving.x = 0

    def start_moving_y(self, direction):
        self.moving.y = self._vel * direction

    def stop_moving_y(self):
        self.moving.y = 0

    def update(self, delta, gx):
        super().update(delta, gx)
        self.move()
        gx.coords(self.img, (self._pos._x, self._pos._y))