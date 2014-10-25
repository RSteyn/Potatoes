from .entity import *
from tkinter import *

class Player(Entity, Movable, Renderable, Shootable):
    UP = -1
    DOWN = 1
    LEFT = -1
    RIGHT = 1

    def __init__(self, canvas):
        Entity.__init__(self)
        Movable.__init__(self)
        Renderable.__init__(self, self._pos.x, self._pos.y,
                            'resources/dean.gif', canvas)
        Shootable.__init__(self)

        self._vel = 5           # TODO: Balance this
        canvas.bind('<KeyPress-Up>',
                     lambda _: self.start_moving_y(self.UP))
        canvas.bind('<KeyPress-Down>',
                     lambda _: self.start_moving_y(self.DOWN))
        canvas.bind('<KeyPress-Left>',
                     lambda _: self.start_moving_x(self.LEFT))
        canvas.bind('<KeyPress-Right>',
                     lambda _: self.start_moving_x(self.RIGHT))

        canvas.bind('<KeyRelease-Up>',
                     lambda _: self.stop_moving_y())
        canvas.bind('<KeyRelease-Down>',
                     lambda _: self.stop_moving_y())
        canvas.bind('<KeyRelease-Left>',
                     lambda _: self.stop_moving_x())
        canvas.bind('<KeyRelease-Right>',
                     lambda _: self.stop_moving_x())

    def start_moving_x(self, direction=DOWN):
        self.moving.x *= self._vel * direction

    def stop_moving_x(self):
        self.moving.x = 0

    def start_moving_y(self, direction=RIGHT):
        self.moving.y *= self._vel * direction

    def stop_moving_y(self):
        self.moving.y = 0

    def update(self, delta):
        super().update(delta)
        self.move()