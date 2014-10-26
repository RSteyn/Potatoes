import math


class Vector:
    RECT_FORM = 'rect'
    POLAR_FORM = 'polar'

    def __init__(self, x, y, polar=False):
        if not polar:
            self._x = x
            self._y = y
            self._mag = self._theta = None
            self._form = self.RECT_FORM
        else:
            # x is mag, y is theta
            self._mag = x
            self._theta = y
            self._x = self._y = None
            self._form = self.POLAR_FORM

    def rotate(self, theta):
        if self.form == self.RECT_FORM:
            return self._rotate_rect_(theta)
        elif self.form == self.POLAR_FORM:
            return self._rotate_polar_(theta)

    def _rotate_rect_(self, theta):
        # Rotate vector by theta, anticlockwise if theta is positive,
        # clockwise if negative.
        new_x = self._x*math.cos(theta) - self._y*math.sin(theta)
        new_y = self._x*math.sin(theta) + self._y*math.cos(theta)
        return Vector(new_x, new_y)

    def _rotate_polar_(self, theta):
        return Vector(self._mag, self._theta + theta, polar=True)

    def to_polar(self):
        return Vector(self.x, self.y)

    def to_rect(self):
        return Vector(self.magnitude, self.direction, polar=True)

    def _to_polar_list_(self):
        return [self.magnitude, self.direction]

    def normalise(self):
        pol_vect = Vector._to_polar_list_(self)
        pol_vect[0] = 1
        pol_vect = Vector(pol_vect[0], pol_vect[1], True)
        return pol_vect

    @property
    def form(self):
        return self._form

    @property
    def x(self):
        if self.form == self.RECT_FORM:
            return self._x
        elif self.form == self.POLAR_FORM:
            return self._mag * math.cos(self._theta)

    @property
    def y(self):
        if self.form == self.RECT_FORM:
            return self._y
        elif self.form == self.POLAR_FORM:
            return self._mag * math.sin(self._theta)

    @property
    def magnitude(self):
        if self.form == self.RECT_FORM:
            return math.sqrt(self._x**2 + self._y**2)
        elif self.form == self.POLAR_FORM:
            return self._mag

    @property
    def direction(self):
        if self.form == self.RECT_FORM:
            return math.atan2(self._y, self._x)
        elif self.form == self.POLAR_FORM:
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