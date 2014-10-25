import math

class Vector:
    def __init__(self, x, y, polar=False):
        if not polar:
            self._x = x
            self._y = y
        else:
            # x is mag, y is theta, convert to cartesian
            self._x = x * math.cos(y)
            self._y = x * math.sin(y)

    def __add__(self, other):
        new_x = self._x + other.x
        new_y = self._y + other.y
        return Vector(new_x, new_y)
    def __sub__(self, other):
        return self.__add__(-other)
    def __neg__(self):
        return Vector(-self._x, -self._y)
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self._x * other, self._y * other)
        else:
            # returns dot product of vectors, not cross
            return self._x*other.x + self._y*other.y
    def __rmul__(self, other):
        return self.__mul__(other)
    def __str__(self):
        return '(' + str(self._x) + ', ' + str(self._y) + ')'

    def rotate(self, theta):
        # Rotate vector by theta, anticlockwise if theta is positive,
        # clockwise if negative.
        new_x = self._x*math.cos(theta) - self._y*math.sin(theta)
        new_y = self._x*math.sin(theta) + self._y*math.cos(theta)
        return Vector(new_x, new_y)

    def __len__(self):
        return math.sqrt(self.get_len_squared())

    def to_polar(self):
        mag = len(self)
        theta = math.atan2(self._y, self._x)
        return [mag, theta]

    def normalise(self):
        pol_vect = Vector.to_polar(self)
        pol_vect[0] = 1
        pol_vect = Vector(pol_vect[0], pol_vect[1], True)
        return pol_vect

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def direction(self):
        return math.atan2(self._y, self._x)

    @property
    def magnitude(self):
        return len(self)

    def get_len_squared(self):
        return self._x**2 + self._y**2