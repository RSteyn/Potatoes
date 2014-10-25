class Killable:
    def __init__(self, start_health=10):
        self._health = start_health

    def hit(self, *, kill=False):
        if kill:
            self._health = 0
        else:
            self._health -= 1

    @property
    def health(self):
        return self._health

    @property
    def dead(self):
        return self._health <= 0
