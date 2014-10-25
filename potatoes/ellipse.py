__author__ = 'rileysteyn'

class Ellipse:
    def __init__(self, x, y,
                 half_width,
                 half_height
                 ):
        """

        :param x: position along x-axis
        :param y: position along y-axis
        :param half_horizontal_distance: half the horizontal width of
        the ellipse, related to semi-axes
        :param half_vertical_distance: half the vertical length of
        the ellipse, related to semi-axes
        """
        self.x = x
        self.y = y

        self.a = half_width
        self.b = half_height
        self.width = half_width * 2
        self.height = half_height * 2

    def point_in_ellise(self, vector):
        to_check = (((vector.x - self.x)**2 / self.a**2) +
                    ((vector.y - self.y)**2 / self.b**2))
        if to_check <= 1:
            return True
        else:
            return False