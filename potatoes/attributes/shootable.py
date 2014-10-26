from ..entity.bullet import Bullet

class Shootable:
    def __init__(self, interval):
        self.bullets = []
        self.interval = interval
        self._shoot_timer = 0

    def shoot(self, x, y, direction, canvas):
        if self._shoot_timer >= self.interval:
            self.bullets.append(Bullet(self, x, y, direction, canvas))
            self._shoot_timer = 0

    def _update_bullets(self, delta, gx):
        for i in range(len(self.bullets)-1, -1, -1):
            bullet = self.bullets[i]
            bullet.update(delta, gx)

    def remove(self, bullet):
        self.bullets.remove(bullet)

    def update(self, delta, gx):
        self._shoot_timer += delta
        self._update_bullets(delta, gx)