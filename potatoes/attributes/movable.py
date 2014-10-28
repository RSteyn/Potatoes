from potatoes.vector import Vector
import math

class Movable:
    _FRICTION = 0.98         # TODO: Balance this
    ANG_FRICTION = 0.85      # TODO: Balance this
    CLOCKWISE = -1
    NO_ROTATION = 0
    COUNTERCLOCKWISE = 1
    def __init__(self, velocity=0, direction=0, accel=0,
                 ang_accel=0, max_speed=0, max_rot_val=0,
                 friction=_FRICTION):
        # Linear variables
        # Current velocity:
        self._cur_velocity = Vector(velocity, direction, polar=True)
        self._accel_vector = Vector(0, direction, polar=True)
        self._direction = direction
        self._acceleration = accel
        self._is_accelerating = False
        self.max_speed = max_speed
        self.friction_coefficient = friction

        # Rotational variables
        self.angular_vel = 0
        self.max_rot_vel = max_rot_val
        self._ang_accel = ang_accel
        self._rot_dir = Movable.NO_ROTATION

    @property
    def speed(self):
        return self._cur_velocity.magnitude

    @speed.setter
    def speed(self, val):
        self._cur_velocity = Vector(val, self._direction, polar=True)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, val):
        self._direction = val
        if self.direction < -math.pi:
            self.direction += 2*math.pi
        if self.direction > math.pi:
            self.direction -= 2*math.pi
        self._accel_vector = Vector(self._acceleration,
                                    -self.direction, polar=True)

    def is_accelerating(self, value):
        self._is_accelerating = value
    def rot_dir(self, value):
        self._rot_dir = value

    def move(self, delta):
        # Move linearly
        if self._is_accelerating:
            # Add acceleration vector to current velocity
            self._cur_velocity += self._accel_vector
        elif self.speed < 0.1:
            self._cur_velocity = Vector(0, 0)
        else:
            self._cur_velocity *= self.friction_coefficient
        if self.speed > self.max_speed:
            self._cur_velocity = self._cur_velocity.normalise()*self.max_speed
        # Adds current velocity to position
        self.pos += self._cur_velocity * delta

        # Rotate
        if abs(self.angular_vel) < 0.001:  # TODO: Balance this
            self.angular_vel = 0
        if abs(self.angular_vel) > self.max_rot_vel:
            if self.angular_vel < 0:
                self.angular_vel = -self.max_rot_vel
            else:
                self.angular_vel = self.max_rot_vel
        elif self._rot_dir == Movable.NO_ROTATION:
            self.angular_vel *= Movable.ANG_FRICTION*(1-delta)
        self.angular_vel += self._ang_accel * self._rot_dir
        self.direction += self.angular_vel