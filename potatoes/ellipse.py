from potatoes.vector import Vector
import math

class Circle:
    @staticmethod
    def collision(circle1, circle2):
        diff = circle1.pos - circle2.pos
        return diff.magnitude <= circle1.rad + circle2.rad

    def __init__(self, x, y, radius):
        self.pos = Vector(x, y)
        self.rad = radius

    def update(self, gx, pos=None):
        if pos is not None:
            self.pos = pos
        gx.create_oval(self.pos.x-self.rad, self.pos.y-self.rad,
                       self.pos.x+self.rad, self.pos.y+self.rad,
                       outline='red')

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
        if (abs(e1.y - e2.y) > e1.half_height + e2.half_height or
                abs(e1.x - e2.x) > e1.half_width + e2.half_width):
            return False
        # Check each ellipses' circle with each other, 9 checks total
        for circle1 in e1.circles:
            for circle2 in e2.circles:
                if Circle.collision(circle1, circle2):
                    return True
        return False

    def __init__(self, x, y,
                 half_width,
                 half_height,
                 gx
                 ):
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
        Circle.__init__(self, x, y, half_width)
        self.x = x
        self.y = y

        self.half_width = half_width
        self.half_height = half_height
        self.width = half_width * 2
        self.height = half_height * 2
        focus = math.sqrt(self.half_height**2 - self.half_width**2)
        self.eccentricity = (focus / math.sqrt(half_height**2 + half_width**2))

        self.circles = list()
        # Create default three circles
        self.circles.append(Circle(self.x, self.y, half_width))

        if self.eccentricity > Ellipse.PRETTY_MUCH_CIRCULAR_CUTOFF:
            self.circles.append(Circle(self.x, self.y-focus, half_height-focus))
            self.circles.append(Circle(self.x, self.y+focus, half_height-focus))

        if self.eccentricity > Ellipse.ECCENTRICITY_CUTOFF:
            # Use two additional circles to compensate for additional
            # eccentricity
            half_focus = focus // 2
            rad = min(half_height-half_focus, self.get_x(self.y-half_focus))
            self.circles.append(Circle(self.x, self.y-half_focus, rad))
            self.circles.append(Circle(self.x, self.y+half_focus, rad))

        # Create draw ellipse:
        self.ellipse = gx.create_oval(
            self.pos.x-self.width // 2,
            self.pos.y-self.height // 2,
            self.pos.x+self.width // 2,
            self.pos.y+self.height // 2,
            outline='yellow'
        )

    def get_x(self, y):
        return self.half_width * math.sqrt(
            1 - (((y-self.pos.y)/self.half_height)**2))

    def update(self, gx, pos=None):
        if pos is not None:
            self.pos = pos
        gx.coords(self.ellipse, (
            self.pos.x-self.half_width, self.pos.y-self.half_height,
            self.pos.x+self.half_width, self.pos.y+self.half_height)
        )
        # For debugging:
        for circle in self.circles:
            circle.update(gx)

# Testing code
# from tkinter import *
# root = Tk()
# c = Canvas(root, width=500, height=500, bg='black')
# e1 = Ellipse(200, 200, 93, 100, c)
# e2 = Ellipse(360, 290, 50, 100, c)
# e1.update(c)
# e2.update(c)
# print(e1.eccentricity)
# print(Ellipse.collision(e1, e2))
#
# c.pack()
# root.mainloop()
