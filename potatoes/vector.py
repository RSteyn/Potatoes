import math


class Vector:
    @staticmethod
    def to_polar(vect):
        mag = vect.get_len()
        theta = math.atan2(vect.y, vect.x)
        return [mag, theta]
    @staticmethod
    def normalise(vect):
        pol_vect = Vector.to_polar(vect)
        pol_vect[0] = 1
        pol_vect = Vector(pol_vect[0], pol_vect[1], True)
        return pol_vect

    def __init__(self, x, y, polar=False):
        if not polar:
            self.x = x
            self.y = y
        else:
            # x is mag, y is theta, convert to cartesian
            self.x = x * math.cos(y)
            self.y = x * math.sin(y)
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    def __sub__(self, other):
        return self.__add__(-other)
    def __neg__(self):
        return Vector(-self.x, -self.y)
    def __mul__(self, other):
        # returns dot product of vectors, not cross
        return self.x*other.x + self.y*other.y
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def get_len_squared(self):
        return self.x**2 + self.y**2
    def get_len(self):
        return math.sqrt(self.get_len_squared())
