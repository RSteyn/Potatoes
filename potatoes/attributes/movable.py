from potatoes.vector import Vector


class Movable:
    def __init__(self, velocity=0, direction=0):
        self._moving = Vector(velocity, direction, polar=True)
        self._direction = direction

    @property
    def velocity(self):
        return self._moving.magnitude

    @velocity.setter
    def velocity(self, val):
        self._moving = Vector(val, self._direction, polar=True)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, val):
        self._direction = val
        self._moving = Vector(self._moving.magnitude, val, polar=True)

    def rotate(self, theta):
        self._moving = self._moving.rotate(theta)
        if theta != 0:
            self._direction = self._moving.direction

    def move(self, delta):
        self._pos += self._moving * delta