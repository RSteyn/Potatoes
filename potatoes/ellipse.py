from potatoes.vector import Vector
import math

class Circle:
    @staticmethod
    def collision(circle1, circle2):
        diff = circle1._pos - circle2._pos
        return diff.magnitude <= circle1.rad + circle2.rad

    def __init__(self, pos, radius):
        self._pos = pos
        self.rad = radius

    def update(self, gx, pos=None):
        if pos is not None:
            self._pos = pos
class Ellipse(Circle):
    PRETTY_MUCH_CIRCULAR_CUTOFF = 0.28
    ECCENTRICITY_CUTOFF = 0.45
    """
    The maths was just too hard, so now all ellipses are
    approximated using up to 5 circles, depending on eccentricity,
    as I assumed that we were not going to use ellipses that are
    too stretched out.
    """
    @staticmethod
    def collision(e1, e2):
        # Perform bounding box checking first to optimise
        dy = abs(e1.pos.y - e2.pos.y)
        dx = abs(e1.pos.x - e2.pos.x)
        if (dy > e1.half_height + e2.half_height or
                dx > e1.half_width + e2.half_width):
            return False
        # Check each ellipses' circle with each other, 9 checks total
        for circle1 in e1.circles:
            for circle2 in e2.circles:
                if Circle.collision(circle1, circle2):
                    return True
        return False

    def __init__(self, pos, half_width, half_height, gx):
        """
        This whole thing assumes that the ellipse is taller than it
        is wide, as with faces or whatnot.
        :param x: position along x-axis
        :param y: position along y-axis
        :param half_width: half the horizontal width of
        the ellipse, related to semi-axes
        :param half_height: half the vertical length of
        the ellipse, related to semi-axes
        """
        Circle.__init__(self, pos, half_width)
        self.half_width = half_width
        self.half_height = half_height
        self.width = half_width * 2
        self.height = half_height * 2
        focus = math.sqrt(self.half_height**2 - self.half_width**2)
        self.eccentricity = (focus / math.sqrt(half_height**2 + half_width**2))

        self.circles = list()
        # Create default three circles
        self.circles.append(Circle(self._pos, half_width))

        if self.eccentricity > Ellipse.PRETTY_MUCH_CIRCULAR_CUTOFF:
            self.circles.append(Circle(Vector(self._pos.x, self._pos.y+focus),
                                       half_height-focus))

        if self.eccentricity > Ellipse.ECCENTRICITY_CUTOFF:
            # Use two additional circles to compensate for additional
            # eccentricity
            half_focus = focus // 2
            rad = min(half_height-half_focus,
                      self.get_x(self._pos.y-half_focus))
            self.circles.append(Circle(
                Vector(self._pos.x, self._pos.y-half_focus), rad))
            self.circles.append(Circle(
                Vector(self._pos.x, self._pos.y+half_focus), rad))

        # Create draw ellipse:
        tag = str(self)
        self.ellipse = gx.create_oval(
            self._pos.x-self.width // 2,
            self._pos.y-self.height // 2,
            self._pos.x+self.width // 2,
            self._pos.y+self.height // 2,
            outline='yellow',
            tag=tag
        )

    def get_x(self, y):
        return self.half_width * math.sqrt(
            1 - (((y-self._pos.y)/self.half_height)**2))

    def update(self, gx, pos=None):
        if pos is not None:
            self._pos = pos
        gx.coords(self.ellipse, (
            self._pos.x-self.half_width, self._pos.y-self.half_height,
            self._pos.x+self.half_width, self._pos.y+self.half_height)
        )
        for circle in self.circles:
            circle.update(gx, pos)
        # # For debugging:
        # for circle in self.circles:
        #     circle.update(gx)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        diff = value - self.pos
        self._pos += diff
        for circle in self.circles:
            circle._pos += diff

# # Testing code
# from tkinter import *
# root = Tk()
# c = Canvas(root, width=500, height=500, bg='black')
# e1 = Ellipse(200, 200, 93, 100, c)
# e2 = Ellipse(360, 290, 65, 110, c)
# e1.update(c)
# e2.update(c)
# print(e1.eccentricity)
# print(Ellipse.collision(e1, e2))
#
# c.pack()
# root.mainloop()
