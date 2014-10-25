from potatoes.vector import Vector


class Movable:
    FRICTION = 75           # TODO: Balance this

    def __init__(self, velocity=0, direction=0, accel=50):
        self._moving = Vector(velocity, direction, polar=True)
        self._direction = direction
        self._accel = accel
        self._c_vel = 0

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
        if self._c_vel < self._moving.magnitude:
            self._c_vel += self._accel * delta
            moving = Vector(self._c_vel, self._moving.direction, polar=True)
        elif self._moving.magnitude < self._c_vel:
            self._c_vel -= self.FRICTION * delta
            moving = Vector(self._c_vel, self._moving.direction, polar=True)
        else:
            moving = self._moving
        self._pos += moving * delta