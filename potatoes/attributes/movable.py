from potatoes.vector import Vector


class Movable:
    FRICTION = 75           # TODO: Balance this

    def __init__(self, velocity=0, direction=0, accel=50):
        self._target_velocity = Vector(velocity, direction, polar=True)
        self._direction = direction
        self._accel = accel
        self._cur_speed = 0

    @property
    def speed(self):
        return self._target_velocity.magnitude

    @speed.setter
    def speed(self, val):
        self._target_velocity = Vector(val, self._direction, polar=True)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, val):
        self._direction = val
        self._target_velocity = Vector(self.speed, val,
                                       polar=True)
    def rotate(self, theta, delta):
        self._target_velocity = self._target_velocity.rotate(theta * delta)
        self._direction = self._target_velocity.direction

    def move(self, delta):
        # Adds current velocity to position, possibly?
        if self._cur_speed < self._target_velocity.magnitude:
            self._cur_speed += self._accel * delta
            moving = Vector(self._cur_speed,
                            self._target_velocity.direction, polar=True)
        elif self._target_velocity.magnitude < self._cur_speed:
            self._cur_speed -= self.FRICTION * delta
            moving = Vector(self._cur_speed,
                            self._target_velocity.direction, polar=True)
        else:
            moving = self._target_velocity
        self._pos += moving * delta