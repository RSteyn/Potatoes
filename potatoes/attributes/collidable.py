from ..ellipse import Ellipse


class Collidable:
    def __init__(self, pos, width, height, gx):
        # Holds ellipse used for collision detection
        self.bounding_ellipse = Ellipse(pos, width // 2, height // 2, gx)

    def collided_with(self, other):
        return Ellipse.collision(self.bounding_ellipse, other.bounding_ellipse)