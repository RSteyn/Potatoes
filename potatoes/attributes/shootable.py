from ..entity.bullet import Bullet
from ..ellipse import Ellipse

class Shootable:
    def __init__(self, interval):
        self.bullets = []
        self.interval = interval
        self._shoot_timer = 0

    def shoot(self, pos, direction, canvas):
        """
        Shoots a bullet
        :param pos: Initial position of bullet
        :param direction: Direction in which bullet moves
        :param canvas: The game canvas
        """
        if self._shoot_timer >= self.interval:
            self.bullets.append(Bullet(self.state, self,
                                       pos, direction, canvas))
            self._shoot_timer = 0

    def _update_bullets(self, delta, gx):
        for i in range(len(self.bullets)-1, -1, -1):
            bullet = self.bullets[i]
            bullet.update(delta, gx)

    def remove(self, bullet):
        if bullet in self.bullets:
            self.bullets.remove(bullet)

    def update(self, delta, gx):
        self._shoot_timer += delta
        self._update_bullets(delta, gx)

    def check_bullet_collisions(self, collidables):
        n_collided = 0
        for entity in collidables:
            for i in range(len(self.bullets)-1, -1, -1):
                bullet = self.bullets[i]
                if Ellipse.collision(bullet.bounding_ellipse,
                                     entity.bounding_ellipse):
                    # Collision has occurred:
                    entity.kill(bullet)
                    self.bullets.remove(bullet)
                    n_collided += 1
        return n_collided
