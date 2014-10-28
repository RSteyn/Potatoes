import math


class Vector:
    RECT_FORM = 'rect'
    POLAR_FORM = 'polar'

    def __init__(self, x, y, polar=False):
        if not polar:
            self._x = x
            self._y = y
            self._mag = math.sqrt(x**2 + y**2)
            self._theta = math.atan2(y, x)
            self._form = self.RECT_FORM
        else:
            # x is mag, y is theta
            self._mag = x
            self._theta = y
            self._x = math.cos(y) * x
            self._y = math.sin(y) * x
            self._form = self.POLAR_FORM

    def rotate(self, theta):
        # Rotate vector by theta, anticlockwise if theta is positive,
        # clockwise if negative.
        new_x = self._x*math.cos(theta) - self._y*math.sin(theta)
        new_y = self._x*math.sin(theta) + self._y*math.cos(theta)
        self._theta += theta
        return Vector(new_x, new_y)

    def _to_polar_list_(self):
        return [self.magnitude, self.direction]

    def normalise(self):
        pol_vect = Vector._to_polar_list_(self)
        pol_vect[0] = 1
        pol_vect = Vector(pol_vect[0], pol_vect[1], polar=True)
        return pol_vect

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def magnitude(self):
        return self._mag

    @property
    def direction(self):
        return self._theta

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        else:
            # returns dot product of vectors, not cross
            return self.x*other.x + self.y*other.y

    def __rmul__(self, other):
        return self.__mul__(other)

    def __len__(self):
        return self.magnitude

    def __str__(self):
        return '(' + str(self._x) + ', ' + str(self._y) + ')'