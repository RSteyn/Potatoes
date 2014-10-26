from ..ellipse import Ellipse


class Collidable:
    def __init__(self, x, y, width, height, gx):
        # Holds ellipse used for collision detection
        self.bounding_ellipse = Ellipse(x, y, width // 2, height // 2, gx)

    def collided_with(self, other):
        return Ellipse.collision(self.bounding_ellipse, other.bounding_ellipse)