from .entity import *


class Player(Entity, Movable, Renderable, Shootable):
    def __init__(self, bind_to):
        Entity.__init__(self)
        Movable.__init__(self)
        Renderable.__init__(self, 'resources/dean.gif', bind_to)
        Shootable.__init__(self)

        self._vel = 5           # TODO: Balance this
        bind_to.bind('<KeyPress-Up>', lambda _: self.start_moving_y(-1))
        bind_to.bind('<KeyPress-Down>', lambda _: self.start_moving_y(1))
        bind_to.bind('<KeyPress-Left>', lambda _: self.start_moving_x(-1))
        bind_to.bind('<KeyPress-Right>', lambda _: self.start_moving_x(1))

        bind_to.bind('<KeyRelease-Up>', lambda _: self.stop_moving_y())
        bind_to.bind('<KeyRelease-Down>', lambda _: self.stop_moving_y())
        bind_to.bind('<KeyRelease-Left>', lambda _: self.stop_moving_x())
        bind_to.bind('<KeyRelease-Right>', lambda _: self.stop_moving_x())

    def start_moving_x(self, direction=1):
        self.moving.x *= self._vel * direction

    def stop_moving_x(self):
        self.moving.x = 0

    def start_moving_y(self, direction=1):
        self.moving.y *= -self._vel * direction

    def stop_moving_y(self):
        self.moving.y = 0

    def update(self, delta):
        super().update(delta)
        self.move()
