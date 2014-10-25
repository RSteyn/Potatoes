from ..entity.bullet import Bullet

class Shootable:
    def __init__(self):
        self.bullets = []

    def shoot(self, x, y, direction, canvas):
        self.bullets.append(Bullet(self, x, y, direction, canvas))

    def update_bullets(self, delta, gx):
        for bullet in self.bullets:
            bullet.update(delta, gx)